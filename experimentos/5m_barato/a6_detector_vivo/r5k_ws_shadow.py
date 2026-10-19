#!/usr/bin/env python3
"""r5k_ws_shadow.py -- A6: detector R5K EN VIVO en modo observación (sin órdenes, sin claves, sin endpoints privados).

Cliente WS mínimo, SOLO canal público de mercado del CLOB, una conexión por mercado BTC 5m (2 tokens) desde cierre-330 s hasta
cierre-50 s. NO mantiene libro: el 85-90 % del tráfico (price_change) se descarta por subcadena antes de json.loads, para que el
consumidor no sea lento (el servidor cierra con 1013 "slow consumer"; visto con ejecutor_rapido.Libro a nice 19 bajo load 25).
Hora de recepción = time_ns() inmediatamente tras ws.recv(). Toda escritura a disco en un hilo aparte.

Salida JSONL por día UTC en --salida:
  {"t":"trade","r":recv_ms,"tk":token,"p":precio,"s":lado_tomador,"z":tamaño,"e":timestamp_msg,"h":tx_hash|null}
  {"t":"cruce"|"cosecha_completa",...}  {"t":"gap","r":ms,"tk":..,"m":motivo} {"t":"snap","r":ms,"tk":token}
  {"t":"mercado_fin","mkt":id,"cierre":s,"completo":bool,"cum":{lado:acc},"n_msg":n,"n_trades":n,"reconexiones":n}
Uso (solo prueba acotada; un despliegue permanente exige /code-review + OK de Javi):
  /root/polymarket-research/.venv/bin/python -I r5k_ws_shadow.py --minutos 60 --salida DIR
"""
import argparse
import asyncio
import json
import queue
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from detector_r5k import DetectorR5K  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
ANTES_S, DESPUES_S = 330, 50          # la banda es T in (60, 300]: margen de 30 s antes y 10 s después


def ahora_ms():
    return time.time_ns() // 1_000_000


def mercado_btc5(ini):
    ev = requests.get(f"{GAMMA}/events", params={"slug": f"btc-updown-5m-{ini}"}, timeout=5).json()
    if not ev:
        return None
    m = ev[0]["markets"][0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"btc-updown-5m-{ini}: outcomes {out} inesperados (fail-closed)")
    return {"id": str(m["id"]), "up": toks[0], "down": toks[1]}


class Salida:
    """Cola + hilo escritor: el hilo del WS solo hace put_nowait."""

    def __init__(self, d):
        self.d, self.q, self.f, self.dia = Path(d), queue.SimpleQueue(), None, None
        self.d.mkdir(parents=True, exist_ok=True)
        self.parar = threading.Event()
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="r5k_escritor")
        self.hilo.start()

    def put(self, obj):
        self.q.put_nowait(obj)

    def _vaciar(self):
        lineas = []
        try:
            while True:
                lineas.append(json.dumps(self.q.get_nowait(), separators=(",", ":")))
        except queue.Empty:
            pass
        if lineas:
            dia = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if dia != self.dia:
                if self.f:
                    self.f.close()
                self.f, self.dia = open(self.d / f"r5k_{dia}.jsonl", "a"), dia
            self.f.write("\n".join(lineas) + "\n")
            self.f.flush()

    def _bucle(self):
        while not self.parar.is_set():
            time.sleep(0.5)
            self._vaciar()

    def cerrar(self):
        self.parar.set()
        self.hilo.join(timeout=3)
        self._vaciar()


async def vigilar(det, out, cierre, m, tolerancia_reconexion_s=0.5):
    toks = [m["up"], m["down"]]
    for tk, lado in ((m["up"], "YES"), (m["down"], "NO")):       # Up = clobTokenIds[0] = YES (igual que las filas k del registro)
        det.alta(tk, m["id"], lado, cierre)
    inicio_ms = (cierre - ANTES_S) * 1000
    for tk in toks:
        det.on_gap(tk, min(inicio_ms, ahora_ms()))                # hasta el primer snapshot no hay continuidad
    n_msg = n_tr = reconex = 0
    fin_s = cierre - DESPUES_S
    while time.time() < fin_s:
        try:
            async with websockets.connect(WS_URL, open_timeout=10, close_timeout=2, max_size=None, ping_interval=None) as ws:
                await ws.send(json.dumps({"assets_ids": toks, "type": "market"}))

                async def latido():
                    while True:
                        await asyncio.sleep(2.0)
                        await ws.send("PING")
                tl = asyncio.create_task(latido())
                try:
                    while time.time() < fin_s:
                        raw = await asyncio.wait_for(ws.recv(), timeout=10)
                        t_recv = ahora_ms()
                        if raw == "PONG" or not raw:
                            continue
                        n_msg += 1
                        es_trade, es_book = '"last_trade_price"' in raw, '"book"' in raw
                        if not (es_trade or es_book):
                            continue                                  # price_change & co: ni se parsean
                        try:
                            datos = json.loads(raw)
                        except ValueError:
                            continue
                        for msg in (datos if isinstance(datos, list) else [datos]):
                            if not isinstance(msg, dict):
                                continue
                            et, tk = msg.get("event_type"), msg.get("asset_id")
                            if et == "book" and tk in toks:
                                det.on_snapshot(tk, t_recv)
                                out.put({"t": "snap", "r": t_recv, "tk": tk})
                            elif et == "last_trade_price" and tk in toks:
                                n_tr += 1
                                out.put({"t": "trade", "r": t_recv, "tk": tk, "p": msg.get("price"), "s": msg.get("side"),
                                         "z": msg.get("size"), "e": msg.get("timestamp"), "h": msg.get("transaction_hash")})
                                for ev in det.al_trade(tk, t_recv, msg):
                                    ev = dict(ev)
                                    ev["t"] = ev.pop("evento")
                                    out.put(ev)
                finally:
                    tl.cancel()
        except Exception as e:                                       # caída: hueco desde AHORA hasta el próximo snapshot
            t = ahora_ms()
            reconex += 1
            for tk in toks:
                det.on_gap(tk, t)
            out.put({"t": "gap", "r": t, "tk": None, "m": f"{type(e).__name__}: {str(e)[:60]}"})
            await asyncio.sleep(tolerancia_reconexion_s)
    mk = m["id"]
    out.put({"t": "mercado_fin", "mkt": mk, "cierre": cierre, "completo": det.completo(mk, cierre),
             "cum": {l: round(det.cum.get((mk, l), 0.0), 3) for l in ("YES", "NO")}, "n_msg": n_msg, "n_trades": n_tr,
             "reconexiones": reconex, "arrancado_tarde": ahora_ms() > inicio_ms + 30000})


async def principal(minutos, out):
    det = DetectorR5K(max_edad_s=900, guardar_filas=False)
    hasta, lanzados, tareas = time.time() + minutos * 60, set(), []
    loop = asyncio.get_running_loop()
    out.put({"t": "inicio", "r": ahora_ms(), "minutos": minutos})
    while time.time() < hasta:
        ahora = time.time()
        c = int(ahora // 300) * 300 + 300
        for cierre in (c, c + 300):
            if cierre in lanzados or ahora < cierre - ANTES_S:
                continue
            try:
                m = await loop.run_in_executor(None, mercado_btc5, cierre - 300)
            except Exception as e:
                out.put({"t": "error", "r": ahora_ms(), "m": f"gamma {cierre}: {type(e).__name__}: {e}"[:120]})
                continue
            if m is None:
                continue
            lanzados.add(cierre)
            tareas.append(asyncio.create_task(vigilar(det, out, cierre, m)))
        det.podar(time.time())
        await asyncio.sleep(1.0)
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)
    out.put({"t": "fin", "r": ahora_ms(), "cruces": len(det.cruces), "stats": dict(det.stats)})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutos", type=float, required=True, help="duración de la prueba (acotada; no es un servicio)")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    out = Salida(a.salida)
    try:
        asyncio.run(principal(a.minutos, out))
    finally:
        out.cerrar()


if __name__ == "__main__":
    main()
