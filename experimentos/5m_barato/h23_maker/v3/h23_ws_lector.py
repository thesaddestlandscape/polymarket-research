#!/usr/bin/env python3
"""h23_ws_lector.py -- LECTOR WS en PROCESO HIJO para el shadow H23 v3r (22-Oct-2026, misión 5m barato). SOLO LECTURA del WS público del CLOB (canal market): sin órdenes, sin claves.

Por qué: el shadow v3/v1 lee el socket DENTRO del bucle asyncio que además ejecuta toda la lógica (8 traders x evaluar por mensaje). Con 100-500 k mensajes por par y la máquina a load 8-14,
el 50 % de los pares (los más ocupados, donde hay rellenos) sufre cortes `1013 slow consumer` (20-22 Oct: 139 de 152 huecos). Aquí el socket lo lee un proceso aparte, con una conexión por
GRUPO de tokens (por defecto UNA POR TOKEN: el límite es el búfer de envío del servidor por conexión, ver CLAUDE.md «WS del libro que cae por slow consumer»), nada de lógica de decisión, y
envía al padre por stdout TRAMAS (longitud + pickle) con la hora de RECEPCIÓN tomada en el propio read. El padre puede ir lento: la cola del hijo es no acotada hasta MAX_COLA tramas
(si se supera: se marca hueco `cola_llena`, se vacía y se reconectan los grupos para recibir fotos nuevas; nunca se pierde en silencio).

Protocolo (padre -> hijo, líneas JSON por stdin):
  {"op":"sub","pair":P,"grp":G,"tokens":[...],"fin_ms":T}   abre la conexión del grupo G del par P hasta la hora T (ms epoch); reconecta sola si cae
  {"op":"unsub","pair":P}                                   cierra todos los grupos del par
  {"op":"exit"}                                             sale. EOF de stdin = salir.
Tramas (hijo -> padre): tupla pickle (kind, recv_ms, pair, grp, payload)
  m  mensaje WS (payload = texto crudo)          p  PONG de texto (liveness)
  c  conectado y suscrito (payload = nº tokens)  g  hueco: la conexión cayó / cola llena (payload = motivo)
  f  grupo terminado (llegó fin_ms)              h  latido del reloj del hijo cada HB_MS (pair=None): el padre ordena eventos propios con él
  e  aviso (payload = texto)
Uso: python3 -I h23_ws_lector.py --hijo   (lo lanza h23_shadow_v3r.py).
"""
import asyncio
import json
import os
import pickle
import queue
import struct
import sys
import threading
import time

WS_URL = os.environ.get("H23_WS_URL", "wss://ws-subscriptions-clob.polymarket.com/ws/market")   # override solo para tests con servidor local
HB_MS = 50
PING_S = 5.0
MAX_COLA = int(os.environ.get("H23_LECTOR_MAX_COLA", "400000"))
RECONECTA_S = 0.05                 # reconexión inmediata (el hueco es lo que cuesta datos); backoff progresivo si falla seguido
BACKOFF_MAX_S = 1.0


def ahora_ms():
    return time.time_ns() // 1_000_000


class Salida:
    """Cola -> hilo escritor -> stdout. El hilo del socket solo encola (sin pickle ni E/S)."""

    def __init__(self, out):
        self.out = out
        self.q = queue.SimpleQueue()
        self.desbordada = False
        self.gen_llena = 0          # sube cada vez que la cola desborda: cada grupo, al verlo cambiar, marca hueco y reconecta
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="escritor_stdout")
        self.hilo.start()

    def put(self, kind, recv, pair, grp, payload=None):
        if kind in ("m", "p"):
            if self.q.qsize() >= MAX_COLA:
                if not self.desbordada:
                    self.desbordada = True
                    self.gen_llena += 1
                return False
            self.desbordada = False
        self.q.put((kind, recv, pair, grp, payload))
        return True

    def _bucle(self):
        buf = self.out
        while True:
            fr = self.q.get()
            if fr is None:
                return
            lote = [fr]
            try:
                while len(lote) < 256:
                    x = self.q.get_nowait()
                    if x is None:
                        lote.append(None)
                        break
                    lote.append(x)
            except queue.Empty:
                pass
            partes = []
            salir = False
            for x in lote:
                if x is None:
                    salir = True
                    break
                b = pickle.dumps(x, protocol=4)
                partes.append(struct.pack("<I", len(b)) + b)
            try:
                buf.write(b"".join(partes))
                buf.flush()
            except (BrokenPipeError, ValueError, OSError):
                os._exit(0)             # el padre murió
            if salir:
                return

    def cerrar(self):
        self.q.put(None)
        self.hilo.join(timeout=3)


async def grupo(sal, pair, grp, tokens, fin_ms, vivos):
    import websockets
    clave = (pair, grp)
    fallos = 0
    try:
        while ahora_ms() < fin_ms and vivos.get(clave):
            try:
                async with websockets.connect(WS_URL, open_timeout=10, close_timeout=1, max_size=None, ping_interval=None, max_queue=None) as ws:
                    await ws.send(json.dumps({"assets_ids": tokens, "type": "market"}))
                    gen = sal.gen_llena
                    sal.put("c", ahora_ms(), pair, grp, len(tokens))
                    fallos = 0

                    async def latido():
                        while True:
                            await asyncio.sleep(PING_S)
                            await ws.send("PING")
                    tl = asyncio.create_task(latido())
                    try:
                        while ahora_ms() < fin_ms and vivos.get(clave):
                            if sal.gen_llena != gen:
                                raise RuntimeError("cola_llena")
                            try:
                                raw = await asyncio.wait_for(ws.recv(), timeout=0.5)
                            except asyncio.TimeoutError:
                                continue
                            t = ahora_ms()
                            if raw == "PONG":
                                sal.put("p", t, pair, grp)
                            elif raw:
                                sal.put("m", t, pair, grp, raw if isinstance(raw, str) else raw.decode("utf-8", "replace"))
                    finally:
                        tl.cancel()
                if ahora_ms() >= fin_ms or not vivos.get(clave):
                    break
                raise ConnectionError("cierre_limpio_inesperado")
            except asyncio.CancelledError:
                raise
            except Exception as e:
                fallos += 1
                sal.put("g", ahora_ms(), pair, grp, f"{type(e).__name__}: {str(e)[:100]}")
                await asyncio.sleep(min(RECONECTA_S * (2 ** min(fallos - 1, 5)), BACKOFF_MAX_S))
    finally:
        vivos.pop(clave, None)
        sal.put("f", ahora_ms(), pair, grp, None)


async def principal(sal):
    loop = asyncio.get_running_loop()
    vivos, tareas = {}, {}
    cmds = asyncio.Queue()

    def lee_stdin():
        for ln in sys.stdin:
            try:
                loop.call_soon_threadsafe(cmds.put_nowait, json.loads(ln))
            except ValueError:
                continue
        loop.call_soon_threadsafe(cmds.put_nowait, {"op": "exit"})
    threading.Thread(target=lee_stdin, daemon=True, name="stdin").start()

    async def hb():
        while True:
            sal.put("h", ahora_ms(), None, None, None)
            await asyncio.sleep(HB_MS / 1000.0)
    th = asyncio.create_task(hb())
    try:
        while True:
            c = await cmds.get()
            op = c.get("op")
            if op == "exit":
                return
            if op == "sub":
                clave = (c["pair"], c["grp"])
                if clave in vivos:
                    continue
                vivos[clave] = True
                tareas[clave] = asyncio.create_task(grupo(sal, c["pair"], c["grp"], list(c["tokens"]), int(c["fin_ms"]), vivos))
            elif op == "unsub":
                for clave in [k for k in vivos if k[0] == c["pair"]]:
                    vivos[clave] = False
            for clave in [k for k, t in tareas.items() if t.done()]:
                tareas.pop(clave)
    finally:
        th.cancel()
        for t in tareas.values():
            t.cancel()


def main():
    try:
        os.nice(0)
    except OSError:
        pass
    sal = Salida(sys.stdout.buffer)
    try:
        asyncio.run(principal(sal))
    finally:
        sal.cerrar()


if __name__ == "__main__":
    if "--hijo" not in sys.argv:
        sys.exit("lector interno de h23_shadow_v3r.py: usar --hijo")
    main()
