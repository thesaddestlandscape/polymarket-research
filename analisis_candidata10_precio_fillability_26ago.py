#!/usr/bin/env python3
"""analisis_candidata10_precio_fillability_26ago.py -- Extension de
Candidata 10 (cross-activo, BTC): ¿el +14.7/+18.2pp de hit-rate ya
implica edge de PRECIO real (vs mejor_ask_deteccion, nuestro propio
libro) y es fillable (profundidad_eur_deteccion>=5.25)? Restringido a
BTC (unico activo con n_sin suficiente en el analisis original).

Solo lectura.
"""
import csv
import zlib
from collections import defaultdict
from datetime import datetime

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
VENTANA_MIN = 30
N_MIN = 15
STAKE = 1.05
UMBRAL_PROFUNDIDAD = 5 * STAKE


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def shuffle_test_prop(hits_a, n_a, p0, iters=5000, seed_key="c10precio"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n_a, p0, size=iters)
    obs = hits_a
    if obs >= n_a * p0:
        return float(np.mean(sims >= obs))
    return float(np.mean(sims <= obs))


def main():
    filas = []
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or not r.get("acierto"):
                continue
            filas.append(r)

    por_wallet = defaultdict(list)
    for r in filas:
        por_wallet[r["wallet"]].append(r)

    resultados = defaultdict(lambda: {"con": [], "sin": []})  # marco -> lista de (acierto, ask, prof)

    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = [(parse_ts(t["trade_timestamp"]), t) for t in trs]
        for ts_i, ti in trs_ts:
            if ti["activo"] != "BTC":
                continue
            confirm = False
            for ts_j, tj in trs_ts:
                if tj is ti or tj["activo"] == ti["activo"]:
                    continue
                if abs((ts_j - ts_i).total_seconds()) <= VENTANA_MIN * 60 and tj["lado_wallet"] == ti["lado_wallet"]:
                    confirm = True
                    break
            grupo = "con" if confirm else "sin"
            marco = ti["marco"]
            ask = to_float(ti["mejor_ask_deteccion"])
            prof = to_float(ti["profundidad_eur_deteccion"])
            resultados[marco][grupo].append((int(ti["acierto"]), ask, prof))

    print(f"{'marco':6} {'grupo':5} {'n':6} {'hit':7} {'ask_med':8} {'edge_bruto':11} {'p_shuffle':10} {'fill%':7} {'n_ask':6}")
    for marco, d in sorted(resultados.items()):
        for grupo in ("con", "sin"):
            datos = d[grupo]
            n = len(datos)
            if n < N_MIN:
                print(f"{marco:6} {grupo:5} n={n}<{N_MIN}, insuficiente")
                continue
            hits = sum(x[0] for x in datos)
            hit = hits / n
            asks = [x[1] for x in datos if x[1] is not None]
            profs = [x[2] for x in datos if x[2] is not None]
            n_ask = len(asks)
            if n_ask:
                ask_med = float(np.median(asks))
                edge = hit - ask_med
                p = shuffle_test_prop(hits, n, p0=ask_med, seed_key=f"{marco}#{grupo}#precio")
                fillable = sum(1 for pf in profs if pf is not None and pf >= UMBRAL_PROFUNDIDAD)
                fill_pct = 100.0 * fillable / len(profs) if profs else None
                fill_str = f"{fill_pct:6.1f}%" if fill_pct is not None else "  n/a "
                print(f"{marco:6} {grupo:5} {n:6} {hit*100:6.1f}% {ask_med:7.3f} {edge*100:+9.1f}pp {p:10.4f} {fill_str} {n_ask:6}")
            else:
                print(f"{marco:6} {grupo:5} {n:6} {hit*100:6.1f}%    n/a         n/a        n/a       n/a    0")


if __name__ == "__main__":
    main()
