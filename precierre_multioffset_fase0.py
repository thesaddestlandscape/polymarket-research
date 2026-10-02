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
MARCOS = {"5m": 300, "15m": 900, "4h": 14400}   # 30-Sep: 4 h (misma regla TWAP Chainlink, 6 cierres al día, menos bots)
OFFSETS = [-120, -90, -60, -45, -30, -20, -10]
OFFSETS_EXTRA = {"4h": [-600, -300, -180]}      # los marcos largos se miran también antes
TOLERANCIA_S = 1.0             # si el bucle llega tarde a un offset más de esto, se descarta ese punto
CADA_S = 0.2
STAKE = 1.05
CHAINLINK_MAX_EDAD_S = 10.0
TWAP_N_MIN_TICKS, TWAP_N_MIN_CIERRE = 20, 10
Z_VOL_VENTANA_S = 300
CAMPOS = ["ts_utc", "activo", "marco", "slug", "market_id", "offset_s", "resto_s", "z", "proy", "ref_twap",
          "direccion", "ask", "bid", "profundidad_eur", "ratio_vs_stake", "lat_libro_ms", "error",
          # 30-Sep (Javi: "necesitamos datos reales y fieles, no optimistas"): libro REAL del lado CONTRARIO al que
          # marca el TWAP, leído en paralelo en el mismo instante. Antes solo podía estimarse como 1 - bid.
          "ask_contrario", "bid_contrario", "profundidad_contrario_eur", "ratio_contrario", "lat_contrario_ms",
          # 02-Oct (OK Javi): el ejecutor live usa desde hoy la ventana OFICIAL del twap60, [e-62, e-3]
          # (no [e-60, e]). Columnas _v2 = lo que decide el live (medias alineadas, misma varianza de z).
          # Las columnas viejas NO cambian: las hipótesis H1-H6 están congeladas sobre ellas.
          "proy_v2", "ref_twap_v2", "z_v2", "direccion_v2"]
VENTANA_DESDE_S, VENTANA_HASTA_S = 62.0, 3.0
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=6)
_pool_c = ThreadPoolExecutor(max_workers=6, thread_name_prefix="multioffset_contrario")


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


def _migrar_cabecera():
    """Si el CSV existe con la cabecera antigua, lo reescribe con las columnas nuevas vacías (una sola vez)."""
    if not OUT.exists():
        return
    with open(OUT, encoding="utf-8", newline="") as f:
        cab = next(csv.reader(f), None)
    if cab == CAMPOS:
        return
    tmp = OUT.with_name(OUT.name + ".migrando")
    with _lock, open(OUT, encoding="utf-8", errors="replace", newline="") as f, open(tmp, "w", newline="", encoding="utf-8") as g:
        w = csv.DictWriter(g, fieldnames=CAMPOS, extrasaction="ignore")
        w.writeheader()
        for r in csv.DictReader(f):
            w.writerow({c: r.get(c, "") for c in CAMPOS})
    tmp.replace(OUT)
    _log(f"cabecera migrada a {len(CAMPOS)} columnas")


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


def _proy_v2(activo, fin):
    """Como _proy pero con la ventana oficial [fin-62, fin-3] (mismo cálculo que el ejecutor)."""
    ult = _ultimo(activo)
    if ult is None or time.time() - ult[0] > CHAINLINK_MAX_EDAD_S + 2.0:
        return None
    t_ult, spot = ult
    v0, v1 = fin - VENTANA_DESDE_S, fin - VENTANA_HASTA_S
    t_hasta = min(t_ult, v1)
    m, n = _media(activo, v0, t_hasta)
    resto = max(0.0, min(60.0, v1 - t_hasta))
    if resto >= 60.0:
        return spot
    if m is None or n < TWAP_N_MIN_CIERRE:
        return None
    return (m * n + spot * resto) / (n + resto)


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


def _libro_cronometrado(token_id):
    t = time.perf_counter()
    r = _libro(token_id)
    return r, round((time.perf_counter() - t) * 1000)


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
        ref2, n_ref2 = _media(activo, ini - VENTANA_DESDE_S, ini - VENTANA_HASTA_S)
        proy2 = _proy_v2(activo, fin)
        if ref2 is not None and n_ref2 >= TWAP_N_MIN_TICKS and proy2 is not None and proy2 != ref2:
            z2 = _z(activo, proy2, ref2, t_hasta, resto)   # misma varianza que el live (sin alinear)
            fila.update({"proy_v2": proy2, "ref_twap_v2": ref2, "z_v2": None if z2 is None else round(z2, 4),
                         "direccion_v2": "Up" if proy2 > ref2 else "Down"})
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
        tok_c = tn if direccion == "Up" else ty
        t = time.perf_counter()
        fut_c = _pool_c.submit(_libro_cronometrado, tok_c) if tok_c else None     # en paralelo: mismo instante
        ask, bid, prof, ratio, err = _libro(tok)
        fila.update({"ask": ask, "bid": bid, "profundidad_eur": prof, "ratio_vs_stake": ratio,
                     "lat_libro_ms": round((time.perf_counter() - t) * 1000), "error": err})
        if fut_c is not None:
            try:
                (ask_c, bid_c, prof_c, ratio_c, err_c), lat_c = fut_c.result(timeout=5)
                if not err_c:
                    fila.update({"ask_contrario": ask_c, "bid_contrario": bid_c, "profundidad_contrario_eur": prof_c,
                                 "ratio_contrario": ratio_c, "lat_contrario_ms": lat_c})
            except Exception:
                pass
    except Exception as e:
        fila["error"] = f"{type(e).__name__}: {e}"[:120]
    _escribir(fila)


def main():
    _migrar_cabecera()
    _log(f"precierre_multioffset_fase0 arrancado (marcos {list(MARCOS)}, offsets {OFFSETS}, con lado contrario real; solo observación)")
    hechos = set()
    while True:
        ahora = time.time()
        for activo in ASSETS:
            for tag, dur in MARCOS.items():
                ini = int(ahora // dur) * dur
                fin = ini + dur
                for off in OFFSETS_EXTRA.get(tag, []) + OFFSETS:
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
