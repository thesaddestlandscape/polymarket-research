#!/usr/bin/env python3
"""ejecutor_rapido.py — NÚCLEO del ejecutor dedicado de baja latencia (Javi 15-Oct: "tenemos que estar en 175 ms para todas
las estrategias de pares, en este caso 5m barato"). Diseño y presupuesto: informes/ejecutor_baja_latencia_diseno_15oct.md.

KPI: hora de casado de NUESTRA orden (exchange) − hora de RECEPCIÓN del evento disparador. Objetivo p50 ≤ 175 ms.
Camino caliente (todo en memoria, cero REST): evento WS → decisión (callback de la estrategia) → orden PREFIRMADA →
POST por la conexión HTTP/2 caliente de py_clob_client_v2. Lo lento (firmar, precargar mercado, leer riesgo) va FUERA del
camino caliente, en hilos de fondo.

Piezas (sin estrategia dentro: la estrategia es un callback que recibe el libro y devuelve una intención):
  Libro      : libro L2 por token desde el WS de mercado del CLOB (conexión PROPIA), hora de recepción en ms.
  Armero     : órdenes FIRMADAS por adelantado por (token, precio, tamaño, lado); cada orden se usa UNA vez (salt único);
               reposición en segundo plano; caducidad configurable (el servidor valida el `timestamp` firmado: F1 lo mide).
  Riesgo     : foto del estado de riesgo refrescada en segundo plano; el camino caliente solo lee la foto y NO opera si
               tiene más de RIESGO_MAX_EDAD_S o si alguna comprobación falla (fail-closed).
  Enviador   : ledger de INTENCIÓN antes del POST, idempotencia por clave, POST en hilo de un pool ya arrancado,
               latido HTTP para mantener la sesión TLS caliente, tiempos en ns del ciclo completo.
DRY_RUN=True por defecto: firma y registra pero NO envía. Enviar exige dry_run=False explícito del llamador.
"""
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RIESGO_MAX_EDAD_S = 2.0
LATIDO_S = 4.0
PING_WS_S = 2.0          # < umbral de frescura (3 s): una conexión quieta pero viva no se da por rota
WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"


def ahora_ms() -> int:
    return time.time_ns() // 1_000_000


# ───────────────────────────── Libro (feed WS propio) ─────────────────────────────
class Libro:
    """(No reutiliza libro_estado_ws: aquel vive en un proceso hijo de `observadores` con registro a disco y universo de
    cientos de tokens; aquí hace falta una conexión PROPIA y mínima para los 2-4 tokens del par — misma lección de
    "una conexión por moneda#marco" contra el slow consumer.)
    Libro L2 por token en memoria. `al_cambiar(token, t_recv_ms, top)` se llama en el hilo del WS en cada cambio de
    top: debe ser O(1) y no bloquear (la decisión de la estrategia vive ahí)."""

    def __init__(self, tokens, al_cambiar=None, al_trade=None, al_nivel=None):
        """al_nivel(token, lado 'bids'|'asks', precio, tamaño_nuevo, tamaño_viejo, t_recv_ms): cada cambio de NIVEL."""
        self.tokens = list(tokens)
        self.al_nivel = al_nivel
        self.vivo_tk = {}                   # token -> t_recv del último mensaje que lo tocó (frescura POR TOKEN)
        self.lib = {t: {"bids": {}, "asks": {}} for t in self.tokens}
        self.top = {}                       # token -> (t_recv_ms, bid, bid_sz, ask, ask_sz)
        self.al_cambiar, self.al_trade = al_cambiar, al_trade
        self._parar = threading.Event()
        self.hilo = threading.Thread(target=self._correr, daemon=True, name="libro_ws")
        self.n_msg = 0
        self.vivo_ms = 0
        self.errores = []                   # (t_ms, texto) de mensajes/callbacks que fallaron (no tumban la conexión)

    def iniciar(self):
        self.hilo.start()
        return self

    def parar(self):
        self._parar.set()

    def _top_de(self, tk):
        L = self.lib[tk]
        bb = max((p for p, s in L["bids"].items() if s > 0), default=None)
        ba = min((p for p, s in L["asks"].items() if s > 0), default=None)
        return bb, L["bids"].get(bb) if bb is not None else None, ba, L["asks"].get(ba) if ba is not None else None

    def _aplicar(self, msg, t_recv):
        et = msg.get("event_type")
        if et == "last_trade_price":
            if self.al_trade and msg.get("asset_id") in self.lib:
                self.al_trade(msg["asset_id"], t_recv, msg)
            return
        tocados = set()
        if "price_changes" in msg:
            for pc in msg["price_changes"]:
                tk = pc.get("asset_id")
                if tk not in self.lib:
                    continue
                try:
                    p, s = float(pc["price"]), float(pc.get("size") or 0)
                except (KeyError, TypeError, ValueError):
                    continue
                nom = "bids" if pc.get("side") == "BUY" else "asks"
                lado = self.lib[tk][nom]
                viejo = lado.get(p, 0.0)
                if s <= 0:
                    lado.pop(p, None)
                else:
                    lado[p] = s
                tocados.add(tk)
                if self.al_nivel:
                    self.al_nivel(tk, nom, p, s, viejo, t_recv)
        elif msg.get("asset_id") in self.lib and ("bids" in msg or "asks" in msg):
            tk = msg["asset_id"]
            self.lib[tk] = {"bids": {float(b["price"]): float(b["size"]) for b in (msg.get("bids") or [])},
                            "asks": {float(a["price"]): float(a["size"]) for a in (msg.get("asks") or [])}}
            self.vivo_tk[tk] = t_recv       # SOLO un snapshot completo hace apto el libro de un token
            tocados.add(tk)
        for tk in tocados:
            if tk not in self.vivo_tk:
                continue                    # sin snapshot desde la última conexión: el libro no vale todavía
            bb, bs, ba, as_ = self._top_de(tk)
            nuevo = (t_recv, bb, bs, ba, as_)
            viejo = self.top.get(tk)
            self.top[tk] = nuevo
            if self.al_cambiar and (viejo is None or viejo[1:] != nuevo[1:]):
                self.al_cambiar(tk, t_recv, nuevo)

    def _correr(self):
        import asyncio
        import websockets

        async def bucle():
            while not self._parar.is_set():
                try:
                    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=2, max_size=None,
                                                  ping_interval=None) as ws:
                        self.vivo_tk = {}           # tras (re)conectar, ningún libro vale hasta su snapshot nuevo
                        self.lib = {t: {"bids": {}, "asks": {}} for t in self.tokens}
                        self.top = {}
                        await ws.send(json.dumps({"assets_ids": self.tokens, "type": "market"}))

                        async def latido():
                            while True:
                                await asyncio.sleep(PING_WS_S)
                                await ws.send("PING")
                        tl = asyncio.create_task(latido())
                        try:
                            while not self._parar.is_set():
                                raw = await asyncio.wait_for(ws.recv(), timeout=30)
                                t_recv = ahora_ms()
                                self.vivo_ms = t_recv
                                if raw == "PONG" or not raw:
                                    continue
                                try:
                                    datos = json.loads(raw)
                                except ValueError:
                                    continue
                                for msg in (datos if isinstance(datos, list) else [datos]):
                                    if isinstance(msg, dict):
                                        self.n_msg += 1
                                        try:
                                            self._aplicar(msg, t_recv)
                                        except Exception as e:      # un mensaje/callback roto no tumba la conexión
                                            self.errores.append((t_recv, f"{type(e).__name__}: {e}"))
                                            del self.errores[:-100]
                        finally:
                            tl.cancel()
                except Exception as e:
                    self.errores.append((ahora_ms(), f"conexión: {type(e).__name__}: {e}"))
                    del self.errores[:-100]
                    self.vivo_tk = {}
                    await asyncio.sleep(1)

        asyncio.run(bucle())

    def fresco(self, token, max_edad_ms=3000):
        """Conexión viva (cualquier mensaje, incluido PONG, en max_edad_ms) Y libro de ESE token recibido alguna vez desde
        la última conexión. Un token callado con la conexión viva es un libro quieto, no uno roto; uno nunca recibido NO
        es apto (fail-closed)."""
        return ahora_ms() - self.vivo_ms <= max_edad_ms and token in self.vivo_tk


# ───────────────────────────── Armero (órdenes prefirmadas) ─────────────────────────────
class Armero:
    """Reserva de órdenes firmadas por clave (token, precio, tamaño, lado). `tomar()` es O(1) y nunca firma en el camino
    caliente: si no hay orden lista devuelve None (la estrategia NO opera; fail-closed)."""

    def __init__(self, cliente, tick_size: str, neg_risk: bool, caducidad_s: float = 60.0, reserva: int = 2):
        from py_clob_client_v2 import PartialCreateOrderOptions
        self.c, self.caducidad_s, self.reserva = cliente, caducidad_s, reserva
        self.opts = PartialCreateOrderOptions(tick_size=tick_size, neg_risk=neg_risk)
        self.pool = {}                      # clave -> [(t_firma_s, signed)]
        self.claves = set()
        self.lock = threading.Lock()
        self.n_firmadas = 0
        self.errores = []

    def _firmar(self, clave):
        from py_clob_client_v2 import OrderArgs
        tok, precio, tam, lado = clave
        return self.c.create_order(OrderArgs(token_id=tok, price=precio, size=tam, side=lado), self.opts)

    def armar(self, claves):
        """Declara las claves que deben estar listas (p. ej. rejilla de precios del mercado vivo) y las rellena."""
        with self.lock:
            self.claves = set(claves)
            for k in list(self.pool):
                if k not in self.claves:
                    del self.pool[k]
        self.reponer()

    def reponer(self):
        ahora = time.time()
        for k in list(self.claves):
            with self.lock:
                vivas = [x for x in self.pool.get(k, []) if ahora - x[0] < self.caducidad_s]
                self.pool[k] = vivas
                falta = self.reserva - len(vivas)
            for _ in range(max(0, falta)):
                try:
                    s = self._firmar(k)
                except Exception as e:
                    self.errores.append((time.time(), k, f"{type(e).__name__}: {e}"))
                    break                   # esta clave queda sin reserva (tomar() -> None = no opera); las demás siguen
                with self.lock:
                    if k in self.claves:    # armar() pudo retirarla mientras firmábamos fuera del lock
                        self.pool.setdefault(k, []).append((time.time(), s))
                        self.n_firmadas += 1

    def tomar(self, clave):
        ahora = time.time()
        with self.lock:
            lista = self.pool.get(clave) or []
            while lista:
                t, s = lista.pop(0)
                if ahora - t < self.caducidad_s:
                    return s
        return None


# ───────────────────────────── Riesgo (foto en segundo plano) ─────────────────────────────
class Riesgo:
    """`comprobaciones`: lista de funciones sin argumentos que devuelven (ok: bool, motivo: str). Se evalúan en un hilo
    cada `cada_s`; el camino caliente solo lee la foto. Excepción en una comprobación = NO operar."""

    def __init__(self, comprobaciones, cada_s=0.5, max_edad_s=RIESGO_MAX_EDAD_S):
        self.comp, self.cada_s, self.max_edad_s = list(comprobaciones), cada_s, max_edad_s
        self.foto = (0.0, False, "sin_evaluar")
        threading.Thread(target=self._bucle, daemon=True, name="riesgo").start()

    def _bucle(self):
        while True:
            ok, motivo = True, "ok"
            for f in self.comp:
                try:
                    r, m = f()
                except Exception as e:
                    r, m = False, f"error {type(e).__name__}: {e}"
                if not r:
                    ok, motivo = False, m
                    break
            self.foto = (time.time(), ok, motivo)
            time.sleep(self.cada_s)

    def puede(self):
        t, ok, motivo = self.foto
        if time.time() - t > self.max_edad_s:
            return False, f"foto de riesgo vieja ({time.time() - t:.1f} s)"
        return ok, motivo


# ───────────────────────────── Enviador ─────────────────────────────
class Enviador:
    """`riesgo`: objeto con puede() -> (ok, motivo); OBLIGATORIO (fail-closed también si el llamador olvida comprobarlo).
    Idempotencia PERSISTENTE: al arrancar relee las claves de intención del ledger. El ledger se escribe en un hilo
    propio (cola) para no pagar disco en el camino caliente; es pequeño (una línea por orden) y vive en datalogs.
    Plan de disco (regla 6b): ~1 línea por orden (KB/día con decenas de órdenes) -> sin gz; cuando el ejecutor opere en
    continuo, un fichero por día (el llamador pasa la ruta con fecha) y retención 30 d en el archivador."""
    def __init__(self, cliente, ledger: Path, riesgo, dry_run: bool = True, hilos: int = 4):
        import queue
        self.c, self.ledger, self.dry_run, self.riesgo = cliente, ledger, dry_run, riesgo
        self.pool = ThreadPoolExecutor(max_workers=hilos, thread_name_prefix="envio")
        barrera = threading.Barrier(hilos + 1)       # obliga a crear los `hilos` trabajadores YA (no en el 1er envío)
        for _ in range(hilos):
            self.pool.submit(barrera.wait, 10)
        barrera.wait(10)
        self.enviadas = set()
        try:
            with open(ledger) as f:
                for ln in f:
                    try:
                        ev = json.loads(ln)
                    except ValueError:
                        continue
                    if ev.get("fase") == "intencion" and not ev.get("dry_run"):
                        self.enviadas.add(ev.get("clave"))
        except FileNotFoundError:
            pass
        self.lock = threading.Lock()
        self._cola = queue.Queue()
        # intención: escritura SÍNCRONA antes del POST con un descriptor ya abierto (O_APPEND, ~decenas de µs; sin
        # open/close en el camino caliente) -> un reinicio nunca pierde una intención ya enviada
        import os
        self._fd = os.open(str(ledger), os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
        self._fd_lock = threading.Lock()
        threading.Thread(target=self._escritor, daemon=True, name="ledger").start()
        self._lat = threading.Thread(target=self._latido, daemon=True, name="latido_http")
        self._lat.start()

    def _latido(self):
        while True:
            try:
                self.c.get_server_time()             # misma sesión HTTP/2 que post_order: mantiene TLS caliente
            except Exception:
                pass
            time.sleep(LATIDO_S)

    def _escritor(self):
        import os
        import sys
        while True:
            ev = self._cola.get()
            try:
                with self._fd_lock:
                    os.write(self._fd, (json.dumps(ev, default=str) + "\n").encode())
            except Exception as e:                   # nunca morir en silencio: aviso por stderr y seguir
                print(f"[ejecutor_rapido] ledger: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
            finally:
                self._cola.task_done()

    def _log(self, ev):
        self._cola.put(ev)

    def vaciar_ledger(self):
        self._cola.join()                            # espera a que se ESCRIBA lo ya sacado de la cola, no solo a vaciarla

    def enviar(self, clave_idem, signed, tipo, t_evento_ms, meta=None, post_only=False):
        """Devuelve un Future con el registro completo, o None si la clave ya se usó. Intención al ledger ANTES del POST."""
        from py_clob_client_v2 import OrderType
        ok, motivo = self.riesgo.puede()
        if not ok:
            self._log({"fase": "veto_riesgo", "clave": clave_idem, "motivo": motivo})
            return None
        with self.lock:
            if clave_idem in self.enviadas:
                return None
            self.enviadas.add(clave_idem)
        t_dec = time.time_ns()
        reg = {"clave": clave_idem, "tipo": tipo, "t_evento_ms": t_evento_ms, "t_decision_ns": t_dec,
               "dry_run": self.dry_run, **(meta or {})}
        import os
        with self._fd_lock:
            os.write(self._fd, (json.dumps({"fase": "intencion", **reg}, default=str) + "\n").encode())

        def _post():
            ok2, motivo2 = self.riesgo.puede()        # re-chequeo en el hilo, justo antes del POST (pudo esperar cola)
            if not ok2:
                out = {**reg, "fase": "abortada_riesgo", "motivo": motivo2, "res": {"abortada": motivo2}}
                self._log(out)
                return {**out, "ms_post": None}
            t0 = time.time_ns()
            if self.dry_run:
                res = {"dry_run": True}
            else:
                try:
                    res = self.c.post_order(signed, getattr(OrderType, tipo), post_only=post_only)
                except Exception as e:
                    res = {"error": f"{type(e).__name__}: {e}"}
            t1 = time.time_ns()
            out = {**reg, "fase": "respuesta", "t_envio_ns": t0, "t_respuesta_ns": t1,
                   "ms_decision_a_envio": round((t0 - t_dec) / 1e6, 2), "ms_post": round((t1 - t0) / 1e6, 2),
                   "ms_evento_a_respuesta": round(t1 / 1e6 - t_evento_ms, 2), "res": res}
            self._log(out)
            return out
        return self.pool.submit(_post)

    def cancelar(self, order_id, meta=None):
        """Cancela UNA orden propia por id (nunca cancel_all: hay ejecutores live en otras wallets/procesos)."""
        from py_clob_client_v2.clob_types import OrderPayload
        t0 = time.time_ns()
        try:
            res = {"dry_run": True} if self.dry_run else self.c.cancel_order(OrderPayload(orderID=order_id))
        except Exception as e:
            res = {"error": f"{type(e).__name__}: {e}"}
        t1 = time.time_ns()
        out = {"fase": "cancelacion", "order_id": order_id, "ms_cancel": round((t1 - t0) / 1e6, 2), "res": res,
               **(meta or {})}
        self._log(out)
        return out
