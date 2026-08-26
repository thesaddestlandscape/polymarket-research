#!/usr/bin/env python3
"""analisis_candidata9_precio_fillability_26ago.py -- Extension de
Candidata 9 (consenso mayoritario bots): ¿el hit-rate de 65-76% ya
implica edge de PRECIO real, y es fillable? Usa mejor_ask_deteccion/
profundidad_eur_deteccion (nuestro propio libro en el momento de cada
trade del bot) sobre bot_wallets_gate_bucket_fase0.csv.

Para cada mercado con consenso mayoritario (N_MIN_BOTS>=3, sin empate),
toma el PRIMER trade del lado mayoritario que ya establece mayoria (o el
ultimo disponible del lado mayoritario si no se puede determinar el
momento exacto de giro) como proxy de nuestra entrada, y mide:
  - ask medio en ese momento (nuestro precio de entrada aproximado)
  - breakeven = ask (mercado binario, ignorando fee 7% de momento)
  - edge_bruto = hit_mayoria - ask_medio
  - fill-ability = % con profundidad_eur_deteccion >= 5.25 (5x stake 1.05)

Solo lectura.
"""
import csv
import math
import zlib
from collections import defaultdict

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
N_MIN_BOTS = 3
STAKE = 1.05
UMBRAL_PROFUNDIDAD = 5 * STAKE


def shuffle_test_prop(hits, n, p0, iters=5000, seed_key="cand9precio"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n, p0, size=iters)
    obs = hits
    if obs >= n * p0:
        return float(np.mean(sims >= obs))
    return float(np.mean(sims <= obs))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    por_mercado = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            por_mercado[r["condition_id"]].append(r)

    resultados = defaultdict(lambda: {
        "n": 0, "aciertos": 0, "asks": [], "profundidades": [], "fillable": 0,
    })

    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS:
            continue
        activo = filas[0]["activo"]
        marco = filas[0]["marco"]
        clave = (activo, marco)
        votos = defaultdict(list)
        for r in filas:
            votos[r["lado_wallet"]].append(r)
        if len(votos) == 1:
            continue
        lado_mayoria = max(votos, key=lambda k: len(votos[k]))
        n_mayoria = len(votos[lado_mayoria])
        n_total = sum(len(v) for v in votos.values())
        if n_mayoria == n_total - n_mayoria:
            continue
        outcome = filas[0]["outcome_real"]
        acierto = 1 if lado_mayoria == outcome else 0

        # proxy de nuestra entrada: mediana del ask entre los trades del lado
        # mayoritario que tuvieran libro consultable
        asks = [to_float(r["mejor_ask_deteccion"]) for r in votos[lado_mayoria]]
        asks = [a for a in asks if a is not None]
        prof = [to_float(r["profundidad_eur_deteccion"]) for r in votos[lado_mayoria]]
        prof = [p for p in prof if p is not None]

        d = resultados[clave]
        d["n"] += 1
        d["aciertos"] += acierto
        if asks:
            d["asks"].append(float(np.median(asks)))
        if prof:
            d["profundidades"].append(float(np.median(prof)))
            if float(np.median(prof)) >= UMBRAL_PROFUNDIDAD:
                d["fillable"] += 1

    print(f"{'activo':6} {'marco':6} {'n':6} {'hit':7} {'ask_med':8} {'edge_bruto':11} {'p_shuffle':10} {'fill%':7} {'n_ask':6}")
    for (activo, marco), d in sorted(resultados.items(), key=lambda kv: -kv[1]["n"]):
        n = d["n"]
        if n < 15:
            continue
        hit = d["aciertos"] / n
        ask_med = float(np.median(d["asks"])) if d["asks"] else None
        n_ask = len(d["asks"])
        fill_pct = 100.0 * d["fillable"] / n_ask if n_ask else None
        if ask_med is not None:
            edge = hit - ask_med
            p = shuffle_test_prop(d["aciertos"], n, p0=ask_med, seed_key=f"{activo}#{marco}#precio")
            print(f"{activo:6} {marco:6} {n:6} {hit*100:6.1f}% {ask_med:7.3f} {edge*100:+9.1f}pp {p:10.4f} "
                  f"{fill_pct:6.1f}% {n_ask:6}")
        else:
            print(f"{activo:6} {marco:6} {n:6} {hit*100:6.1f}%    n/a         n/a        n/a       n/a    0")


if __name__ == "__main__":
    main()
