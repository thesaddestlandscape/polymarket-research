#!/usr/bin/env python3
"""precierre_multioffset_fase0.py -- "explotar el naive" (25-Sep, Javi: "tiene que haber una forma"):
PRECIERRE A VARIOS INSTANTES, FASE 0. SOLO OBSERVACIÓN: nunca envía órdenes.

Motivo (barrido de 10 días 15-24 Sep, Chainlink RTDS como TWAP, ask del libro <=10 s, banda ask
[0,25-0,85), z>=1; IN-SAMPLE y con ask posiblemente rancio, por eso hace falta esta medición):
  5min  T-120: 183/día EV +0,033 | T-90: 111/día +0,070 | T-60: 52/día +0,147 | T-45: 16/día +0,455 |
        T-30: 11/día +0,31 | T-20: 11/día +0,39 | T-10: 7/día +0,39   (días+ 8-10/10)
  15min T-90: 22/día +0,118 | T-45: 2,8/día +0,362 ; T-60/-20 ~0
  primer disparo por mercado entre T-120 y T-10: 339/día, EV +0,089 (10/10 días)
Hoy el ejecutor solo mira T-45 (5,6/día). Este observador replica la MISMA decisión (TWAP proyectado
en tiempo de oráculo, z de margen, dirección) a cada offset y lee el libro PÚBLICO real (~55 ms) del
token del lado predicho: ask, bid, profundidad. El resultado oficial (gamma) permite calcular después
el EV al ask REAL y la frecuencia por offset (analisis_precierre_multioffset.py).
Usa la cola de ticks del oráculo _TAIL de resolution_sniper_observer (ya arrancada en observadores).
-> /root/polymarket-research-datalogs/precierre_multioffset_fase0.csv
"""
import csv
import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import ASSETS, _TAIL, mercado_slot, token_ids

OUT = Path("/root/polymarket-research-datalogs") / "precierre_multioffset_fase0.csv"
MARCOS = {"5m": 300, "15m": 900}
OFFSETS = [-120, -90, -60, -45, -30, -20, -10]
TOLERANCIA_S = 1.0             # si el bucle llega tarde a un offset más de esto, se descarta ese punto
CADA_S = 0.2
STAKE = 1.05
CHAINLINK_MAX_EDAD_S = 10.0
TWAP_N_MIN_TICKS, TWAP_N_MIN_CIERRE = 20, 10
Z_VOL_VENTANA_S = 300
CAMPOS = ["ts_utc", "activo", "marco", "slug", "market_id", "offset_s", "resto_s", "z", "proy", "ref_twap",
          "direccion", "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms", "error"]
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=6)


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


def _ultimo(activo):
    with _TAIL._lock:
        dq = _TAIL._buf_oracle.get(activo)
        return dq[-1] if dq else None


def _media(activo, t0, t1):
    """(media, n) de ticks del oráculo con t0<=t<=t1 (misma lógica que el ejecutor)."""
    with _TAIL._lock:
        dq = list(_TAIL._buf_oracle.get(activo, ()))
    v = [p for t, p in dq if t0 <= t <= t1 and p > 0]
    return (sum(v) / len(v), len(v)) if v else (None, 0)


def _proy(activo, fin):
    ult = _ultimo(activo)
    if ult is None or time.time() - ult[0] > CHAINLINK_MAX_EDAD_S + 2.0:
        return None, None, None
    t_ult, spot = ult
    t_hasta = min(t_ult, fin)
    m, n = _media(activo, fin - 60, t_hasta)
    resto = max(0.0, min(60.0, fin - t_hasta))
    if resto >= 60.0:
        return spot, t_hasta, resto
    if m is None or n < TWAP_N_MIN_CIERRE:
        return None, t_hasta, resto
    return (m * n + spot * resto) / (n + resto), t_hasta, resto


def _z(activo, proy, ref, t_hasta, resto):
    if proy is None or proy <= 0 or ref is None or ref <= 0 or t_hasta is None:
        return None
    precios = []
    with _TAIL._lock:
        for t, p in reversed(_TAIL._buf_oracle.get(activo, ())):
            if t < t_hasta - Z_VOL_VENTANA_S:
                break
            if t <= t_hasta and p > 0:
                precios.append(p)
    precios.reverse()
    if len(precios) < 60:
        return None
    rets = [math.log(b / a) for a, b in zip(precios, precios[1:])]
    mu = sum(rets) / len(rets)
    vol = math.sqrt(sum((r - mu) ** 2 for r in rets) / len(rets))
    var_s = (resto / 60.0) ** 2 * resto / 3.0
    if vol <= 0 or var_s <= 0:
        return None
    return abs(math.log(proy / ref)) / (vol * math.sqrt(var_s))


def _libro(token_id):
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


def _punto(activo, tag, ini, fin, off):
    fila = {c: "" for c in CAMPOS}
    fila.update({"ts_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), "activo": activo,
                 "marco": tag, "slug": f"{activo.lower()}-updown-{tag}-{ini}", "offset_s": off})
    try:
        ref, n_ref = _media(activo, ini - 60, ini)
        if ref is None or n_ref < TWAP_N_MIN_TICKS:
            fila["error"] = "sin_ref_twap"
            return _escribir(fila)
        proy, t_hasta, resto = _proy(activo, fin)
        z = _z(activo, proy, ref, t_hasta, resto) if proy is not None else None
        fila.update({"resto_s": round(fin - time.time(), 2), "proy": proy, "ref_twap": ref,
                     "z": None if z is None else round(z, 4)})
        if proy is None or proy == ref:
            fila["error"] = "sin_proy_o_empate"
            return _escribir(fila)
        direccion = "Up" if proy > ref else "Down"
        fila["direccion"] = direccion
        _, mkt = mercado_slot(activo, tag, ini)
        if not mkt:
            fila["error"] = "sin_mercado"
            return _escribir(fila)
        fila["market_id"] = mkt.get("id", "")
        ty, tn = token_ids(mkt)
        tok = ty if direccion == "Up" else tn
        if not tok:
            fila["error"] = "sin_token"
            return _escribir(fila)
        t = time.perf_counter()
        ask, bid, prof, ratio, err = _libro(tok)
        fila.update({"ask": ask, "bid": bid, "profundidad_eur": prof, "ratio_vs_stake": ratio,
                     "lat_libro_ms": round((time.perf_counter() - t) * 1000), "error": err})
    except Exception as e:
        fila["error"] = f"{type(e).__name__}: {e}"[:120]
    _escribir(fila)


def main():
    _log(f"precierre_multioffset_fase0 arrancado (offsets {OFFSETS}, solo observación)")
    hechos = set()
    while True:
        ahora = time.time()
        for activo in ASSETS:
            for tag, dur in MARCOS.items():
                ini = int(ahora // dur) * dur
                fin = ini + dur
                for off in OFFSETS:
                    k = (activo, tag, ini, off)
                    objetivo = fin + off
                    if k in hechos or ahora < objetivo:
                        continue
                    hechos.add(k)
                    if ahora - objetivo <= TOLERANCIA_S and objetivo > ini + 30:
                        _pool.submit(_punto, activo, tag, ini, fin, off)
        if len(hechos) > 20000:
            corte = ahora - 3600
            hechos = {k for k in hechos if k[2] + MARCOS[k[1]] > corte}
        time.sleep(CADA_S)


if __name__ == "__main__":
    _TAIL.arrancar()
    time.sleep(5)
    main()
