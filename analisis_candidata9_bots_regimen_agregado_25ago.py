#!/usr/bin/env python3
"""analisis_candidata9_bots_regimen_agregado_25ago.py -- Candidata 9:
consenso agregado de las 84 bot wallets por mercado (% comprando Up vs
Down) como señal de régimen, sin exigir coincidencia de estrategia
propia. Usa bot_wallets_gate_bucket_fase0.csv (ya filtrado a las 84 bot
wallets, con outcome_real resuelto).

Agrupa por condition_id -- para mercados con >=3 bots operando, mide si
el lado MAYORITARIO acierta mas que el minoritario/que un 50% base.
Desagrega por activo y marco (CLAUDE.md pt.17).

Solo lectura.
"""
import csv
import math
import sys
import zlib
from collections import defaultdict

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
N_MIN_BOTS = 3


def shuffle_test_prop(hits, n, p0=0.5, iters=5000, seed_key="cand9"):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    sims = rng.binomial(n, p0, size=iters)
    obs = hits
    p_valor = float(np.mean(sims >= obs)) if obs >= n * p0 else float(np.mean(sims <= obs))
    return p_valor


def main():
    por_mercado = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            por_mercado[r["condition_id"]].append(r)

    resultados = defaultdict(lambda: {"n_mercados": 0, "aciertos_mayoria": 0, "n_unanime": 0, "aciertos_unanime": 0})

    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS:
            continue
        activo = filas[0]["activo"]
        marco = filas[0]["marco"]
        clave = (activo, marco)
        votos = defaultdict(int)
        for r in filas:
            votos[r["lado_wallet"]] += 1
        if len(votos) == 1:
            continue  # no hay 2 lados distintos, no aporta info de consenso
        lado_mayoria = max(votos, key=votos.get)
        n_mayoria = votos[lado_mayoria]
        n_total = sum(votos.values())
        if n_mayoria == n_total - n_mayoria:
            continue  # empate exacto
        outcome = filas[0]["outcome_real"]
        acierto_mayoria = 1 if lado_mayoria == outcome else 0
        d = resultados[clave]
        d["n_mercados"] += 1
        d["aciertos_mayoria"] += acierto_mayoria
        if n_mayoria == n_total:  # unanimidad
            d["n_unanime"] += 1
            d["aciertos_unanime"] += acierto_mayoria

    print(f"{'activo':6} {'marco':6} {'n_mercados':10} {'hit_mayoria':11} {'p_shuffle':10} {'n_unanime':10} {'hit_unanime':11}")
    for (activo, marco), d in sorted(resultados.items(), key=lambda kv: -kv[1]["n_mercados"]):
        n = d["n_mercados"]
        if n < 15:
            print(f"{activo:6} {marco:6} {n:10} n<15, insuficiente")
            continue
        hit = d["aciertos_mayoria"] / n
        p = shuffle_test_prop(d["aciertos_mayoria"], n, seed_key=f"{activo}#{marco}")
        n_u = d["n_unanime"]
        hit_u = d["aciertos_unanime"] / n_u if n_u >= 15 else None
        hit_u_str = f"{hit_u*100:.1f}%" if hit_u is not None else f"n={n_u}<15"
        print(f"{activo:6} {marco:6} {n:10} {hit*100:9.1f}% {p:10.4f} {n_u:10} {hit_u_str}")


if __name__ == "__main__":
    main()
