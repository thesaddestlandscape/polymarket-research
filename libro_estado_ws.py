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
    LE.iniciar(filtro_marcos=("15min",))          # hilo daemon, idempotente
    LE.en(token_id, t_ms)  -> dict|None           # último estado con t<=t_ms
Solo lectura, sin órdenes. Universo = mercados abiertos de los marcos pedidos
(fetch_libro_ambos_lados._universo_activo), refrescado cada 30 s con
suscripciones incrementales (sin reconectar, sin huecos).
"""
import asyncio
import collections
import json
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
RECV_TIMEOUT_S = 1.0       # corto: las suscripciones on-demand (pedir) se atienden en <=1 s

_LIB = {}                  # token -> {"bids": {p: s}, "asks": {p: s}}
_HIST = {}                 # token -> deque[(t_ms, bb, ba, i1, i5, i10, dask5)]
_LOCK = threading.Lock()
_EXTRA = {}                # token -> expiración (epoch s): tokens pedidos on-demand por otros módulos (suscripción inmediata)
_TRADES = {}               # token -> deque[(t_ms, price, side, size)] de last_trade_price (29-Sep, requote/maker sim)
_MARCOS = {}               # marco -> conjunto de activos permitidos (None = todos); unión de todos los llamantes
_TOP = {}                  # token -> (t_ms, best_bid, bid_size, best_ask, ask_size): último estado O(1) (detectores de alta frecuencia)
_ULT = {}                  # token -> t_ms del último registro (muestreo mínimo entre registros)
MUESTREO_MS = 100
SUB_TROZO, SUB_PAUSA_S = 20, 0.25   # alta de tokens en trozos (ver _sesion)
_ESTADO = {"iniciado": False, "n_tokens": 0, "n_eventos": 0, "ultimo_evento_ms": 0}


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [libro_estado_ws] {msg}", flush=True)


def _imb(bids, asks, n):
    sb = sum(s for _, s in bids[:n])
    sa = sum(s for _, s in asks[:n])
    t = sb + sa
    return round((sb - sa) / t, 4) if t > 0 else None


def _registrar(token, t_ms):
    L = _LIB.get(token)
    if L is None:
        return
    bids = sorted(((p, s) for p, s in L["bids"].items() if s > 0), reverse=True)
    asks = sorted((p, s) for p, s in L["asks"].items() if s > 0)
    bb = bids[0][0] if bids else None
    ba = asks[0][0] if asks else None
    dask5 = round(sum(p * s for p, s in asks[:5]), 2)
    _TOP[token] = (t_ms, bb, bids[0][1] if bids else None, ba, asks[0][1] if asks else None)
    h = _HIST.setdefault(token, deque(maxlen=HIST_MAX))
    h.append((t_ms, bb, ba, _imb(bids, asks, 1), _imb(bids, asks, 5), _imb(bids, asks, 10), dask5,
              bids[0][1] if bids else None, asks[0][1] if asks else None))
    _ESTADO["n_eventos"] += 1
    _ESTADO["ultimo_evento_ms"] = t_ms


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
    <=1 s y se da de baja solo al expirar. Idempotente."""
    exp = time.time() + ttl_s
    for t in tokens:
        if t:
            _EXTRA[t] = max(_EXTRA.get(t, 0), exp)


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


def _aplicar(msg):
    t_ev = int(msg.get("timestamp") or time.time() * 1000)
    if msg.get("event_type") == "last_trade_price":
        tk = msg.get("asset_id")
        if tk in _LIB:
            try:
                with _LOCK:
                    _TRADES.setdefault(tk, deque(maxlen=500)).append((t_ev, float(msg["price"]), msg.get("side"),
                                                                     float(msg.get("size") or 0)))
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
        with _LOCK:
            for tk in tocados:
                if t_ev - _ULT.get(tk, 0) >= MUESTREO_MS:   # el libro se actualiza siempre; se muestrea el histórico
                    _ULT[tk] = t_ev
                    _registrar(tk, t_ev)
    elif "asset_id" in msg and ("bids" in msg or "asks" in msg):
        tk = msg["asset_id"]
        if tk in _LIB or True:
            _LIB[tk] = {"bids": {float(b["price"]): float(b["size"]) for b in (msg.get("bids") or [])},
                        "asks": {float(a["price"]): float(a["size"]) for a in (msg.get("asks") or [])}}
            with _LOCK:
                _ULT[tk] = t_ev
                _registrar(tk, t_ev)


async def _sesion(filtro_marcos):
    suscritos = set()
    # max_queue=None: si este hilo se retrasa (GIL, 40 hilos en la screen) los mensajes se acumulan en memoria en
    # vez de frenar el socket; con la cola por defecto el servidor cortaba con 1013 "slow consumer".
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        loop = asyncio.get_running_loop()
        toks = await loop.run_in_executor(None, _tokens_universo, filtro_marcos)
        # 30-Sep: suscribir 150+ tokens de golpe hace que el servidor mande todas las fotos del libro en una ráfaga,
        # llene SU buffer de envío y corte con 1013 "slow consumer" (caídas a 1-25 s de conectar, ~100 por hora,
        # con el hilo ocioso en select: no era lentitud nuestra). Se suscribe en trozos de SUB_TROZO, uno cada
        # SUB_PAUSA_S, leyendo el socket entre medias; lo mismo para las altas on-demand y las del refresco.
        cola_sub, t_sub = collections.deque(toks[SUB_TROZO:]), time.time()
        await ws.send(json.dumps({"type": "market", "assets_ids": toks[:SUB_TROZO]}))
        suscritos.update(toks)
        for t in toks:
            _LIB.setdefault(t, {"bids": {}, "asks": {}})
        # 30-Sep, fuga: tras una reconexión `suscritos` nace vacío y los tokens de la sesión anterior que ya no
        # están en el universo nunca pasaban por la baja de más abajo -> _HIST (hasta 3.000 muestras por token)
        # crecía ~90 MB/h hasta el OOM. Al conectar se tira todo lo que no esté en el universo ni pedido on-demand.
        vivos = set(toks) | set(_EXTRA)
        with _LOCK:
            for d in (_LIB, _HIST, _TRADES, _TOP, _ULT):
                for t in [t for t in d if t not in vivos]:
                    d.pop(t, None)
        refresco = None
        _ESTADO["n_tokens"] = len(suscritos)
        _log(f"conectado, {len(toks)} tokens ({','.join(filtro_marcos)})")
        prox = time.time() + REFRESCO_S
        while True:
            try:
                raw = await asyncio.wait_for(ws.recv(), RECV_TIMEOUT_S)
            except asyncio.TimeoutError:
                raw = None
            # tokens on-demand: alta inmediata, baja al expirar
            ahora_s = time.time()
            add_x = [t for t, e in _EXTRA.items() if e > ahora_s and t not in suscritos]
            if add_x:
                cola_sub.extendleft(reversed(add_x))      # on-demand por delante: se atienden en el siguiente trozo
                for t in add_x:
                    _LIB.setdefault(t, {"bids": {}, "asks": {}})
                suscritos.update(add_x)
            if cola_sub and time.time() - t_sub >= SUB_PAUSA_S:
                trozo = [cola_sub.popleft() for _ in range(min(SUB_TROZO, len(cola_sub)))]
                trozo = [t for t in trozo if t in suscritos]          # por si se dio de baja mientras esperaba
                if trozo:
                    await ws.send(json.dumps({"assets_ids": trozo, "operation": "subscribe"}))
                t_sub = time.time()
            # 30-Sep: el refresco del universo (REST, varios segundos) se esperaba AQUÍ dentro, sin leer el socket:
            # cada 30 s el servidor nos cortaba por "slow consumer" (~1.000 caídas en 10 h, huecos de >5 s en el
            # histórico ms). Ahora corre en segundo plano y se recoge cuando termina; el recv no se detiene nunca.
            if refresco is None and time.time() >= prox:
                prox = time.time() + REFRESCO_S
                refresco = loop.run_in_executor(None, _tokens_universo, filtro_marcos)
            if refresco is not None and refresco.done():
                try:
                    nuevos = refresco.result()
                except Exception as e:
                    _log(f"refresco de universo falló: {type(e).__name__}: {e}")
                    nuevos = None
                refresco = None
            else:
                nuevos = None
            if nuevos is not None:
                for t in [t for t, e in _EXTRA.items() if e <= ahora_s]:
                    _EXTRA.pop(t, None)
                nuevos = list(set(nuevos) | set(_EXTRA))
                add = [t for t in nuevos if t not in suscritos]
                if add:
                    cola_sub.extend(add)
                    for t in add:
                        _LIB.setdefault(t, {"bids": {}, "asks": {}})
                    suscritos.update(add)
                    _ESTADO["n_tokens"] = len(suscritos)
                viejos = [t for t in suscritos if t not in set(nuevos)]
                if viejos:
                    await ws.send(json.dumps({"assets_ids": viejos, "operation": "unsubscribe"}))
                    for t in viejos:
                        suscritos.discard(t)
                        _LIB.pop(t, None)
                        with _LOCK:
                            _HIST.pop(t, None)
                            _TRADES.pop(t, None)
                            _TOP.pop(t, None)
                            _ULT.pop(t, None)
            if not raw:
                continue
            try:
                j = json.loads(raw)
            except Exception:
                continue
            for e in (j if isinstance(j, list) else [j]):
                if isinstance(e, dict):
                    _aplicar(e)


def _hilo(filtro_marcos):
    while True:
        try:
            asyncio.run(_sesion(filtro_marcos))
        except Exception as e:
            _log(f"sesión caída: {type(e).__name__}: {e}; reconecta en 5 s")
        time.sleep(5)


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
    threading.Thread(target=_hilo, args=(tuple(filtro_marcos),), daemon=True, name="libro_estado_ws").start()


if __name__ == "__main__":
    iniciar()
    while True:
        time.sleep(10)
        print(estado(), flush=True)
