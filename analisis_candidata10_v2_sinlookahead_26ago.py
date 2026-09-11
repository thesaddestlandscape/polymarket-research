#!/usr/bin/env python3
"""analisis_candidata10_v2_sinlookahead_26ago.py -- Candidata 10, v2 sin
look-ahead: la confirmacion cruzada solo cuenta si el trade confirmador
en el OTRO activo ocurrio ANTES (o en el mismo instante) que el trade
que estamos evaluando -- el v1 miraba +-30min sin restriccion temporal,
lo que podia usar un trade FUTURO como si ya se supiera en el momento de
decidir. Ademas usa el ask del trade evaluado (ya lo hacia bien) y añade
split-half cronologico.

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


def shuffle_test_prop(hits, n, p0, iters=5000, seed_key="c10v2"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n, p0, size=iters)
    obs = hits
    if obs >= n * p0:
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

    resultados = defaultdict(lambda: {"con": [], "sin": []})

    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = sorted([(parse_ts(t["trade_timestamp"]), t) for t in trs], key=lambda x: x[0])
        for idx, (ts_i, ti) in enumerate(trs_ts):
            if ti["activo"] != "BTC":
                continue
            confirm = False
            # solo trades PREVIOS (ts_j <= ts_i), otro activo, mismo lado,
            # dentro de la ventana -- sin look-ahead
            for ts_j, tj in trs_ts[:idx]:
                if tj["activo"] == ti["activo"]:
                    continue
                if (ts_i - ts_j).total_seconds() <= VENTANA_MIN * 60 and tj["lado_wallet"] == ti["lado_wallet"]:
                    confirm = True
                    break
            grupo = "con" if confirm else "sin"
            marco = ti["marco"]
            ask = to_float(ti["mejor_ask_deteccion"])
            prof = to_float(ti["profundidad_eur_deteccion"])
            resultados[marco][grupo].append({"ts": ts_i, "hit": int(ti["acierto"]), "ask": ask, "prof": prof})

    print(f"{'marco':6} {'grupo':5} {'n':6} {'hit':7} {'ask_med':8} {'edge_bruto':11} {'p_shuffle':10} {'fill%':7} "
          f"{'split1':8} {'split2':8}")
    for marco, d in sorted(resultados.items()):
        for grupo in ("con", "sin"):
            datos = sorted(d[grupo], key=lambda e: e["ts"])
            n = len(datos)
            if n < N_MIN:
                print(f"{marco:6} {grupo:5} n={n}<{N_MIN}, insuficiente")
                continue
            hits = sum(e["hit"] for e in datos)
            hit = hits / n
            asks = [e["ask"] for e in datos if e["ask"] is not None]
            profs = [e["prof"] for e in datos if e["prof"] is not None]
            n_ask = len(asks)
            if not n_ask:
                print(f"{marco:6} {grupo:5} {n:6} {hit*100:6.1f}%    n/a")
                continue
            ask_med = float(np.median(asks))
            edge = hit - ask_med
            p = shuffle_test_prop(hits, n, p0=ask_med, seed_key=f"{marco}#{grupo}#v2")
            fillable = sum(1 for pf in profs if pf >= UMBRAL_PROFUNDIDAD)
            fill_pct = 100.0 * fillable / len(profs) if profs else None
            fill_str = f"{fill_pct:6.1f}%" if fill_pct is not None else "  n/a "

            mid = n // 2
            h1, h2 = datos[:mid], datos[mid:]
            def edge_split(sub):
                sub_ask = [e["ask"] for e in sub if e["ask"] is not None]
                if len(sub_ask) < 8:
                    return None
                hh = sum(e["hit"] for e in sub) / len(sub)
                am = float(np.median(sub_ask))
                return hh - am
            e1, e2 = edge_split(h1), edge_split(h2)
            e1_str = f"{e1*100:+.1f}pp" if e1 is not None else "n/a"
            e2_str = f"{e2*100:+.1f}pp" if e2 is not None else "n/a"

            print(f"{marco:6} {grupo:5} {n:6} {hit*100:6.1f}% {ask_med:7.3f} {edge*100:+9.1f}pp {p:10.4f} {fill_str} "
                  f"{e1_str:8} {e2_str:8}")


if __name__ == "__main__":
    main()
