#!/usr/bin/env python3
"""binance_jump_leadlag_fase0.py -- A3b "ganarles al entrar" disparado por BINANCE, FASE 0 (25-Sep,
Javi: "mide si el libro sigue a Binance"). SOLO OBSERVACIÓN: nunca envía órdenes.

Hallazgo que lo motiva (event study 25-Sep 00:00-08:00, bookTicker Binance vs trades Polymarket 5min,
mercados con 20<tte<240 s, saltos de Binance >=2,5-5 bps en 1 s): tras el salto, la prob. Up de
Polymarket sube (en el sentido del salto) +4/+12c a los 0,25 s, +8/+14c a 1 s, +13/+22c a 2 s y
+22/+30c a 4 s (BTC/ETH/SOL/XRP, %positivos 89-100% a 2-4 s; n=17-54 por moneda, un solo día).
Correlaciones a 250 ms: Polymarket refleja el retorno de Chainlink-RECEPCIÓN con ~0-0,75 s de retraso
y el de Binance con ~2,5-3 s -> el libro sigue al oráculo, no a Binance, y Binance adelanta a la
recepción RTDS ~2,5 s. El A3 clásico (saltos de p_justo por Chainlink) daba EV -0,071 al ask real
porque dispara CUANDO el libro ya se está moviendo; aquí se dispara 2-3 s antes.

Qué hace: mantiene su propio WebSocket bookTicker de Binance (6 monedas, mismo stream que
fetch_binance_bookticker.py). Ante un salto |ln(mid/mid hace 1 s)| >= UMBRAL[moneda] (dedup 5 s por
moneda), para cada mercado 5/15min vigente con 20<=resto<=240 s lee el libro PÚBLICO del token del
lado del salto en los offsets OFFSETS_S (0 = "antes", luego 0,3/0,6/1/2/4 s) y registra ask, bid,
profundidad y latencia real. Después (analisis_binance_jump_leadlag.py) se resuelve el resultado
oficial y se calcula el EV al ask REAL entrando en cada offset (retener a resolución) y el markout
(bid a +4 s - ask de entrada). Solo cuenta lo medido aquí, con la latencia de esta máquina.
-> data/shadow/binance_jump_leadlag_fase0.csv
"""
import asyncio
import csv
import json
import math
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import _CACHE_MKT, mercado_slot, token_ids

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "binance_jump_leadlag_fase0.csv"
SIMBOLOS = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL", "XRPUSDT": "XRP",
            "DOGEUSDT": "DOGE", "BNBUSDT": "BNB"}
WS_URL = "wss://stream.binance.com:9443/stream?streams=" + "/".join(f"{s.lower()}@bookTicker" for s in SIMBOLOS)
UMBRAL = {"BTC": 2.5e-4, "ETH": 3e-4, "SOL": 4e-4, "XRP": 4e-4, "DOGE": 5e-4, "BNB": 3e-4}   # retorno en 1 s
DEDUP_S = 5.0
MARCOS = {"5m": 300, "15m": 900}
RESTO_MIN, RESTO_MAX = 20, 240
OFFSETS_S = [0.0, 0.3, 0.6, 1.0, 2.0, 4.0]
STAKE = 1.05
CAMPOS = ["ts_evento", "activo", "marco", "slug", "market_id", "resto_s", "direccion", "ret_1s", "offset_s",
          "t_real_s", "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms", "error"]
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=8)
_ticks = {a: deque() for a in SIMBOLOS.values()}   # (t_recv, mid), ~2,5 s
_ult_ev = {}


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _escribir(fila):
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _leer_libro(token_id):
    """(ask, bid, profundidad_eur, ratio, error). Profundidad = niveles a <=1,05x el mejor ask."""
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return None, None, None, None, "sin respuesta del libro"
    try:
        asks = [(float(l["price"]), float(l["size"])) for l in (book.get("asks") or [])]
        bids = [(float(l["price"]), float(l["size"])) for l in (book.get("bids") or [])]
    except (TypeError, ValueError, KeyError):
        return None, None, None, None, "libro ilegible"
    ask = min((p for p, _ in asks), default=None)
    bid = max((p for p, _ in bids), default=None)
    prof = sum(p * s for p, s in asks if ask is not None and p <= ask * 1.05) if ask is not None else 0.0
    return ask, bid, round(prof, 2), round(prof / STAKE, 1), ""


def _muestrear(base, token_id, t0):
    """Un hilo por (evento, mercado): lee el libro en cada offset. t_real_s = tiempo real desde el evento."""
    for off in OFFSETS_S:
        espera = t0 + off - time.time()
        if espera > 0:
            time.sleep(espera)
        t = time.perf_counter()
        ask, bid, prof, ratio, err = _leer_libro(token_id)
        fila = dict(base)
        fila.update({"offset_s": off, "t_real_s": round(time.time() - t0, 3), "ask": ask, "bid": bid,
                     "profundidad_eur": prof, "ratio_vs_stake": ratio,
                     "lat_libro_ms": round((time.perf_counter() - t) * 1000), "error": err})
        _escribir(fila)


def _evento(activo, t0, ret):
    direccion = "Up" if ret > 0 else "Down"
    for tag, dur in MARCOS.items():
        ini = int(t0 // dur) * dur
        resto = ini + dur - t0
        if not (RESTO_MIN <= resto <= RESTO_MAX):
            continue
        slug = f"{activo.lower()}-updown-{tag}-{ini}"
        mkt = _CACHE_MKT.get(slug)    # solo caché (la llena _calentar): nunca bloquear el bucle del WebSocket
        if not mkt:
            continue
        ty, tn = token_ids(mkt)
        tok = ty if direccion == "Up" else tn
        if not tok:
            continue
        base = {"ts_evento": datetime.fromtimestamp(t0, timezone.utc).isoformat(timespec="milliseconds"),
                "activo": activo, "marco": tag, "slug": slug, "market_id": mkt.get("id", ""),
                "resto_s": round(resto, 1), "direccion": direccion, "ret_1s": round(ret, 6)}
        _pool.submit(_muestrear, base, tok, t0)


def _procesar(activo, mid, t):
    dq = _ticks[activo]
    dq.append((t, mid))
    while dq and dq[0][0] < t - 2.5:
        dq.popleft()
    ref = None
    for tt, mm in dq:                       # último tick con edad >= 1 s
        if t - tt >= 1.0:
            ref = mm
        else:
            break
    if ref is None or ref <= 0 or mid <= 0:
        return
    ret = math.log(mid / ref)
    if abs(ret) >= UMBRAL[activo] and t - _ult_ev.get(activo, -1e9) >= DEDUP_S:
        _ult_ev[activo] = t
        _evento(activo, t, ret)


async def _ws():
    import websockets
    while True:
        try:
            async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20) as ws:
                _log("conectado a Binance bookTicker")
                async for raw in ws:
                    try:
                        d = json.loads(raw).get("data") or {}
                        a = SIMBOLOS.get(d.get("s"))
                        if a:
                            _procesar(a, (float(d["b"]) + float(d["a"])) / 2, time.time())
                    except (ValueError, KeyError, TypeError):
                        continue
        except Exception as e:
            _log(f"conexión perdida ({type(e).__name__}: {e}), reconectando en 5 s")
            await asyncio.sleep(5)


def _calentar():
    """Precarga en la caché de mercado_slot el mercado vigente (y el siguiente) de cada moneda/marco,
    para que un evento no pague el GET a gamma antes de la primera lectura de libro."""
    while True:
        ahora = time.time()
        for a in SIMBOLOS.values():
            for tag, dur in MARCOS.items():
                ini = int(ahora // dur) * dur
                for i in (ini, ini + dur):
                    try:
                        mercado_slot(a, tag, i)
                    except Exception:
                        pass
        time.sleep(5)


def main():
    _log(f"binance_jump_leadlag_fase0 arrancado (umbrales {UMBRAL}, offsets {OFFSETS_S}, solo observación)")
    threading.Thread(target=_calentar, daemon=True).start()
    asyncio.run(_ws())


if __name__ == "__main__":
    main()
