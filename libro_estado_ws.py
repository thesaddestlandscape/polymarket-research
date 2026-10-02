#!/usr/bin/env python3
"""libro_estado_ws.py -- estado del libro L2 en memoria por token, mantenido
por WebSocket del CLOB (canal market) con histórico corto de imbalance/mejor
bid-ask con TIMESTAMP EN MS, para poder preguntar "¿cómo estaba el libro en
el instante T?" (29-Sep, principio Javi: micro-latencia/detección rápida).

Motivo: gbm_late_imbalance_fase0 medía el libro por REST ~0,5-22 s DESPUÉS
de la señal (ciclo de predictions ~100 s + poll); aquí el libro se conoce en
todo momento y se consulta en el ms exacto de la señal.

Uso (desde otro módulo, mismo proceso):
    import libro_estado_ws as LE
    LE.iniciar(filtro_marcos=("15min",))          # idempotente
    LE.en(token_id, t_ms)  -> dict|None           # último estado con t<=t_ms
Solo lectura, sin órdenes. Universo = mercados abiertos de los marcos pedidos
(fetch_libro_ambos_lados._universo_activo), refrescado cada 30 s con
suscripciones incrementales (sin reconectar, sin huecos).

02-Oct, LECTOR EN PROCESO SEPARADO (OK Javi): dentro de la screen `observadores` (~60 hilos, nice 10, máquina a
load 8-11) el hilo que leía el socket se quedaba sin turno y el servidor cortaba (1013 "slow consumer" / ping
vencido): ~85 caídas/h, ~10 s de hueco cada una. Subir el hilo a nice 0 lo dejó en ~27/h; un lector aislado no cae
nunca. Ahora:
  - HIJO (`python libro_estado_ws.py --hijo`, nice 0, solo stdlib + websockets): lee el socket, parsea, mantiene el
    libro L2, muestrea cada MUESTREO_MS y manda lotes de registros compactos por stdout (tramas longitud+pickle).
    Un hilo emisor desacopla el envío: el socket se lee siempre aunque el padre vaya lento. Logs por stderr.
  - PADRE (este módulo importado): calcula el universo (REST) y los tokens on-demand (pedir) y se los manda al hijo
    por stdin; un hilo lector aplica los lotes a _HIST/_TOP/_TRADES. La API pública no cambia.
  - Si el padre muere, el hijo ve EOF en stdin y sale. Si el hijo muere, el padre lo relanza en 2 s.
  Se usa subprocess y no multiprocessing: spawn/forkserver reimportarían el __main__ del padre (observadores_fase0
  con ~100 módulos).
"""
import asyncio
import collections
import json
import os
import pickle
import struct
import subprocess
import sys
import threading
import time
from bisect import bisect_right
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
REFRESCO_S = 30
HIST_MAX = 3000            # eventos por token (>= varios minutos a ritmo alto)
RECV_TIMEOUT_S = 0.25      # corto: las altas on-demand (pedir) se atienden en <=0,25 s
MUESTREO_MS = 100
SUB_TROZO, SUB_PAUSA_S = 20, 0.25   # alta de tokens en trozos (ver _sesion_hija)
LOTE_S = 0.02              # el hijo agrupa registros y los manda cada 20 ms

_LIB = {}                  # (hijo) token -> {"bids": {p: s}, "asks": {p: s}}
_ULT = {}                  # (hijo) token -> t_ms del último registro (muestreo mínimo entre registros)
_HIST = {}                 # token -> deque[(t_ms, bb, ba, i1, i5, i10, dask5, bid_size, ask_size)]
_LOCK = threading.Lock()
_EXTRA = {}                # token -> expiración (epoch s): tokens pedidos on-demand por otros módulos (suscripción inmediata)
_TRADES = {}               # token -> deque[(t_ms, price, side, size)] de last_trade_price (29-Sep, requote/maker sim)
_MARCOS = {}               # marco -> conjunto de activos permitidos (None = todos); unión de todos los llamantes
_TOP = {}                  # token -> (t_ms, best_bid, bid_size, best_ask, ask_size): último estado O(1) (detectores de alta frecuencia)
_ESTADO = {"iniciado": False, "n_tokens": 0, "n_eventos": 0, "ultimo_evento_ms": 0, "reinicios_hijo": 0}
_ES_HIJO = False


def _log(msg):
    # en el hijo stdout es el canal de datos: los logs van SIEMPRE a stderr (mismo fichero de log de la screen)
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [libro_estado_ws] {msg}",
          file=sys.stderr if _ES_HIJO else sys.stdout, flush=True)


def _trama(obj):
    b = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    return struct.pack("<I", len(b)) + b


def _leer_trama(f):
    cab = f.read(4)
    if len(cab) < 4:
        return None
    n = struct.unpack("<I", cab)[0]
    b = f.read(n)
    if len(b) < n:
        return None
    return pickle.loads(b)


def subir_prioridad_hilo():
    """02-Oct: los procesos de observación corren con nice 10 y, con la máquina a load 8-11 en 4 cores, un hilo que
    lee un socket se queda sin turno. Solo SUBE la prioridad del hilo que llama a 0 (nunca la baja si ya está a 0 o
    negativa); sin permisos, no hace nada. Lo usa binance_jump_leadlag (y el hijo de este módulo)."""
    try:
        tid = threading.get_native_id()
        if os.getpriority(os.PRIO_PROCESS, tid) > 0:
            os.setpriority(os.PRIO_PROCESS, tid, 0)
    except (OSError, AttributeError) as e:
        _log(f"no se pudo subir la prioridad del hilo: {e}")


# ----------------------------------------------------------------------------------------------- API (padre)

def en(token, t_ms):
    """Último estado del libro con timestamp <= t_ms: dict con edad_ms respecto a t_ms, o None."""
    with _LOCK:
        h = _HIST.get(token)
        if not h:
            return None
        arr = list(h)
    i = bisect_right([x[0] for x in arr], t_ms) - 1
    if i < 0:
        return None
    t, bb, ba, i1, i5, i10, d5, bbs, bas = arr[i]
    return {"t_ms": t, "edad_ms": t_ms - t, "best_bid": bb, "best_ask": ba, "imb1": i1, "imb5": i5, "imb10": i10,
            "depth_ask5_usd": d5, "bid_size": bbs, "ask_size": bas}


def pedir(tokens, ttl_s=900):
    """Pide seguimiento ms de tokens arbitrarios (p.ej. mercado de un evento recién detectado). Se suscribe en
    <=~0,3 s y se da de baja solo al expirar. Idempotente."""
    exp = time.time() + ttl_s
    nuevos = False
    for t in tokens:
        if t:
            nuevos |= t not in _EXTRA or _EXTRA[t] <= time.time()
            _EXTRA[t] = max(_EXTRA.get(t, 0), exp)
    if nuevos:
        _enviar_deseados()


def trades(token, t0_ms, t1_ms):
    with _LOCK:
        d = list(_TRADES.get(token, ()))
    return [x for x in d if t0_ms <= x[0] <= t1_ms]


def hist_rango(token, t0_ms, t1_ms):
    with _LOCK:
        h = list(_HIST.get(token, ()))
    return [x for x in h if t0_ms <= x[0] <= t1_ms]


def ultimo(token):
    """(t_ms, best_bid, bid_size, best_ask, ask_size) más reciente del token, O(1). None si sin datos."""
    return _TOP.get(token)


def estado():
    return dict(_ESTADO)


# ----------------------------------------------------------------------------------------------- padre

_HIJO = {"proc": None, "lock": threading.Lock()}
_UNIVERSO = {"toks": None}


def _tokens_universo(filtro_marcos=None):
    import live_trade as lt
    from fetch_libro_ambos_lados import _universo_activo
    out = []
    for mid, (activo, marco, _cid, _edt) in _universo_activo().items():
        permitidos = _MARCOS.get(marco, "no")
        if permitidos == "no" or (permitidos is not None and activo not in permitidos):
            continue
        try:
            yes, no, _ = lt._get_token_ids(mid)
        except Exception:
            continue
        out += [t for t in (yes, no) if t]
    return out


def _enviar_deseados():
    """Manda al hijo el conjunto completo deseado (universo + on-demand vigentes; los on-demand primero)."""
    ahora = time.time()
    extra = [t for t, e in list(_EXTRA.items()) if e > ahora]
    univ = _UNIVERSO["toks"]
    if univ is None:
        return                                   # sin universo aún: se mandará en cuanto exista
    with _HIJO["lock"]:
        p = _HIJO["proc"]
        if p is None or p.poll() is not None:
            return
        try:
            p.stdin.write(_trama(("tokens", list(univ), extra)))
            p.stdin.flush()
        except (BrokenPipeError, OSError, ValueError):
            pass


def _podar(vivos):
    """Fuga del 30-Sep: tokens que ya no están en el universo ni pedidos se tiran del histórico (3.000 muestras/token)."""
    with _LOCK:
        for d in (_HIST, _TRADES, _TOP):
            for t in [t for t in d if t not in vivos]:
                d.pop(t, None)


def _hilo_universo():
    while True:
        try:
            toks = _tokens_universo()
            ahora = time.time()
            for t in [t for t, e in list(_EXTRA.items()) if e <= ahora]:
                _EXTRA.pop(t, None)
            _UNIVERSO["toks"] = toks
            _ESTADO["n_tokens"] = len(set(toks) | set(_EXTRA))
            _podar(set(toks) | set(_EXTRA))
            _enviar_deseados()
        except Exception as e:
            _log(f"refresco de universo falló: {type(e).__name__}: {e}")
        time.sleep(REFRESCO_S)


def _hilo_lector(proc):
    """Aplica los lotes del hijo. Si el padre va lento, los lotes esperan en la tubería / el emisor del hijo, nunca
    en el socket: el servidor no ve un consumidor lento."""
    f = proc.stdout
    while True:
        try:
            lote = _leer_trama(f)
        except Exception as e:
            _log(f"lector del hijo: {type(e).__name__}: {e}")
            lote = None
        if lote is None:
            return                                   # EOF: el hijo murió (el supervisor lo relanza)
        ult = None
        with _LOCK:
            for tipo, tk, rec in lote:
                if tipo == "h":
                    _HIST.setdefault(tk, deque(maxlen=HIST_MAX)).append(rec)
                    _TOP[tk] = (rec[0], rec[1], rec[7], rec[2], rec[8])
                    ult = rec[0]
                    _ESTADO["n_eventos"] += 1
                elif tipo == "t":
                    _TRADES.setdefault(tk, deque(maxlen=500)).append(rec)
        if ult is not None:
            _ESTADO["ultimo_evento_ms"] = ult


def _supervisor():
    while True:
        try:
            proc = subprocess.Popen([sys.executable, "-u", str(Path(__file__).resolve()), "--hijo"],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None, cwd=str(REPO))
        except Exception as e:
            _log(f"no se pudo lanzar el lector hijo: {type(e).__name__}: {e}; reintento en 5 s")
            time.sleep(5)
            continue
        with _HIJO["lock"]:
            _HIJO["proc"] = proc
        _log(f"lector hijo lanzado (pid {proc.pid})")
        _enviar_deseados()
        lector = threading.Thread(target=_hilo_lector, args=(proc,), daemon=True, name="libro_ws_lector")
        lector.start()
        proc.wait()
        lector.join(timeout=5)
        _ESTADO["reinicios_hijo"] += 1
        _log(f"lector hijo terminó (rc {proc.returncode}); relanzo en 2 s")
        time.sleep(2)


def iniciar(filtro_marcos=("15min",), activos=None):
    """Idempotente y ACUMULATIVO: cada llamante añade sus marcos (activos=None -> todos)."""
    for m in filtro_marcos:
        if m in _MARCOS and _MARCOS[m] is None:
            continue
        if activos is None:
            _MARCOS[m] = None
        else:
            _MARCOS[m] = set(_MARCOS.get(m) or ()) | set(activos)
    if _ESTADO["iniciado"]:
        return
    _ESTADO["iniciado"] = True
    threading.Thread(target=_supervisor, daemon=True, name="libro_estado_ws").start()
    threading.Thread(target=_hilo_universo, daemon=True, name="libro_ws_universo").start()


# ----------------------------------------------------------------------------------------------- hijo

def _imb(bids, asks, n):
    sb = sum(s for _, s in bids[:n])
    sa = sum(s for _, s in asks[:n])
    t = sb + sa
    return round((sb - sa) / t, 4) if t > 0 else None


def _registrar(token, t_ms, salida):
    L = _LIB.get(token)
    if L is None:
        return
    bids = sorted(((p, s) for p, s in L["bids"].items() if s > 0), reverse=True)
    asks = sorted((p, s) for p, s in L["asks"].items() if s > 0)
    bb = bids[0][0] if bids else None
    ba = asks[0][0] if asks else None
    dask5 = round(sum(p * s for p, s in asks[:5]), 2)
    salida.append(("h", token, (t_ms, bb, ba, _imb(bids, asks, 1), _imb(bids, asks, 5), _imb(bids, asks, 10), dask5,
                                bids[0][1] if bids else None, asks[0][1] if asks else None)))


def _aplicar(msg, salida):
    t_ev = int(msg.get("timestamp") or time.time() * 1000)
    if msg.get("event_type") == "last_trade_price":
        tk = msg.get("asset_id")
        if tk in _LIB:
            try:
                salida.append(("t", tk, (t_ev, float(msg["price"]), msg.get("side"), float(msg.get("size") or 0))))
            except (KeyError, TypeError, ValueError):
                pass
        return
    if "price_changes" in msg:
        tocados = set()
        for pc in msg["price_changes"]:
            tk = pc.get("asset_id")
            L = _LIB.get(tk)
            if L is None:
                continue
            try:
                p, s = float(pc["price"]), float(pc.get("size") or 0)
            except (KeyError, TypeError, ValueError):
                continue
            lado = "bids" if pc.get("side") == "BUY" else "asks"
            if s <= 0:
                L[lado].pop(p, None)
            else:
                L[lado][p] = s
            tocados.add(tk)
        for tk in tocados:
            if t_ev - _ULT.get(tk, 0) >= MUESTREO_MS:   # el libro se actualiza siempre; se muestrea el histórico
                _ULT[tk] = t_ev
                _registrar(tk, t_ev, salida)
    elif "asset_id" in msg and ("bids" in msg or "asks" in msg):
        tk = msg["asset_id"]
        _LIB[tk] = {"bids": {float(b["price"]): float(b["size"]) for b in (msg.get("bids") or [])},
                    "asks": {float(a["price"]): float(a["size"]) for a in (msg.get("asks") or [])}}
        _ULT[tk] = t_ev
        _registrar(tk, t_ev, salida)


class _Emisor:
    """Cola de salida del hijo + hilo que la vuelca a stdout por lotes. El bucle del socket solo hace append."""

    def __init__(self):
        self.buf = []
        self.cv = threading.Condition()
        threading.Thread(target=self._loop, daemon=True, name="emisor").start()

    def extend(self, recs):
        if recs:
            with self.cv:
                self.buf.extend(recs)

    def _loop(self):
        out = sys.stdout.buffer
        while True:
            time.sleep(LOTE_S)
            with self.cv:
                lote, self.buf = self.buf, []
            if lote:
                try:
                    out.write(_trama(lote))
                    out.flush()
                except (BrokenPipeError, OSError):
                    os._exit(0)                     # el padre murió


_DESEADOS = {"univ": [], "extra": [], "ver": 0}
_DES_LOCK = threading.Lock()


def _hilo_stdin():
    f = sys.stdin.buffer
    while True:
        try:
            m = _leer_trama(f)
        except Exception:
            m = None
        if m is None:
            os._exit(0)                             # EOF: el padre murió o cerró -> el hijo sale
        if m[0] == "tokens":
            with _DES_LOCK:
                _DESEADOS["univ"], _DESEADOS["extra"] = m[1], m[2]
                _DESEADOS["ver"] += 1


async def _sesion_hija(emisor):
    suscritos = set()
    # esperar al primer conjunto deseado ANTES de conectar: el servidor cierra con 1008 "no subscribe received" si
    # el socket queda abierto sin suscripción (el padre tarda ~35 s en su primer universo al arrancar observadores)
    while True:
        with _DES_LOCK:
            ver, univ, extra = _DESEADOS["ver"], list(_DESEADOS["univ"]), list(_DESEADOS["extra"])
        if ver and (univ or extra):
            break
        await asyncio.sleep(0.2)
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        toks = list(dict.fromkeys(extra + univ))   # on-demand por delante
        # 30-Sep: suscribir 150+ tokens de golpe hace que el servidor mande todas las fotos del libro en una ráfaga,
        # llene SU buffer de envío y corte con 1013. Se suscribe en trozos de SUB_TROZO, uno cada SUB_PAUSA_S,
        # leyendo el socket entre medias; lo mismo para las altas posteriores.
        cola_sub, t_sub = collections.deque(toks[SUB_TROZO:]), time.time()
        await ws.send(json.dumps({"type": "market", "assets_ids": toks[:SUB_TROZO]}))
        suscritos.update(toks)
        for t in toks:
            _LIB.setdefault(t, {"bids": {}, "asks": {}})
        for t in [t for t in _LIB if t not in suscritos]:
            _LIB.pop(t, None)
            _ULT.pop(t, None)
        _log(f"conectado, {len(toks)} tokens (lector en proceso separado, pid {os.getpid()})")
        ver_aplicada = ver
        while True:
            try:
                raw = await asyncio.wait_for(ws.recv(), RECV_TIMEOUT_S)
            except asyncio.TimeoutError:
                raw = None
            with _DES_LOCK:
                ver = _DESEADOS["ver"]
                if ver != ver_aplicada:
                    univ, extra = list(_DESEADOS["univ"]), list(_DESEADOS["extra"])
            if ver != ver_aplicada:
                ver_aplicada = ver
                deseados = set(univ) | set(extra)
                add_x = [t for t in extra if t not in suscritos]
                add_u = [t for t in univ if t not in suscritos and t not in set(add_x)]
                if add_x:
                    cola_sub.extendleft(reversed(add_x))   # on-demand en el siguiente trozo
                cola_sub.extend(add_u)
                for t in add_x + add_u:
                    _LIB.setdefault(t, {"bids": {}, "asks": {}})
                suscritos.update(add_x + add_u)
                viejos = [t for t in suscritos if t not in deseados]
                if viejos:
                    await ws.send(json.dumps({"assets_ids": viejos, "operation": "unsubscribe"}))
                    for t in viejos:
                        suscritos.discard(t)
                        _LIB.pop(t, None)
                        _ULT.pop(t, None)
            if cola_sub and time.time() - t_sub >= SUB_PAUSA_S:
                trozo = [cola_sub.popleft() for _ in range(min(SUB_TROZO, len(cola_sub)))]
                trozo = [t for t in trozo if t in suscritos]          # por si se dio de baja mientras esperaba
                if trozo:
                    await ws.send(json.dumps({"assets_ids": trozo, "operation": "subscribe"}))
                t_sub = time.time()
            if not raw:
                continue
            try:
                j = json.loads(raw)
            except Exception:
                continue
            salida = []
            for e in (j if isinstance(j, list) else [j]):
                if isinstance(e, dict):
                    _aplicar(e, salida)
            emisor.extend(salida)


def _main_hijo():
    global _ES_HIJO
    _ES_HIJO = True
    try:
        if os.getpriority(os.PRIO_PROCESS, 0) > 0:
            os.setpriority(os.PRIO_PROCESS, 0, 0)    # el padre corre a nice 10; el lector no
    except OSError as e:
        _log(f"no se pudo subir la prioridad del hijo: {e}")
    emisor = _Emisor()
    threading.Thread(target=_hilo_stdin, daemon=True, name="stdin").start()
    while True:
        try:
            asyncio.run(_sesion_hija(emisor))
        except Exception as e:
            _log(f"sesión caída: {type(e).__name__}: {e}; reconecta en 2 s")
        time.sleep(2)


if __name__ == "__main__":
    if "--hijo" in sys.argv:
        _main_hijo()
    else:
        iniciar(("5min", "15min"))
        while True:
            time.sleep(10)
            print(estado(), flush=True)
