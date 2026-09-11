#!/usr/bin/env python3
"""analisis_gate_riguroso_momentumibs15m_btc_fillable_25ago.py -- gate
riguroso completo (Wilson90+shuffle+split-half) sobre el SUBCONJUNTO
FILLABLE de MOMENTUM_IBS_15M_BALLENA#BTC#15min#BUY_YES bucket [0.40,0.45)
-- petición explícita Javi 25-Ago, mismo principio que P23/P25/P27: el
gate_bucket_propio.json mide sobre TODO results.csv (shadow), pero solo
importa si el edge sobrevive en el subconjunto donde el libro real
tenía profundidad suficiente (colapso canónico por market_id,
libro_snapshots.csv, ratio_vs_stake>=5x -- CLAUDE.md pt.3b, nunca contar
filas sueltas).

Solo lectura. No promociona nada por sí solo -- reporta el veredicto.
"""
import csv
import math
from collections import defaultdict

import numpy as np

STRATEGY, SUBTYPE, DECISION = "MOMENTUM_IBS_15M_BALLENA", "BTC#15min", "BUY_YES"
BUCKET_LO, BUCKET_HI = 0.40, 0.45
FEE = 0.07
PRIORIDAD = ['ejecutada', 'abort_requote', 'veto_profundidad', 'veto_sin_datos',
             'fok_kill', 'no_viable_stake', 'senal_caducada', 'fuera_ventana',
             'candidato_evaluacion']
PRIO_RANK = {m: i for i, m in enumerate(PRIORIDAD)}


def wilson90(hits, n):
    if n == 0:
        return (0.0, 0.0)
    z = 1.6448536269514722  # 90% two-sided
    p = hits / n
    denom = 1 + z**2 / n
    centro = p + z**2 / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2))
    return ((centro - margen) / denom, (centro + margen) / denom)


def main():
    # 1. Colapso canónico de libro_snapshots.csv por market_id -- motivo de mayor prioridad.
    por_market = defaultdict(list)
    with open("data/live/libro_snapshots.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r["strategy"], r["subtype"], r["direction"]) == (STRATEGY, SUBTYPE, DECISION):
                por_market[r["market_id"]].append(r)
    fillable_market_ids = set()
    for mid, filas in por_market.items():
        filas.sort(key=lambda r: PRIO_RANK.get(r["motivo"], 99))
        top = filas[0]
        try:
            ratio = float(top.get("ratio_vs_stake") or 0)
        except (TypeError, ValueError):
            ratio = 0.0
        if ratio >= 5.0:
            fillable_market_ids.add(mid)
    print(f"market_ids con snapshot de esta tupla: {len(por_market)} | fillable (ratio>=5x): {len(fillable_market_ids)}")

    # 2. Filas de results.csv (shadow) de esta tupla en el bucket, con y sin filtro fillable.
    todas, fillable = [], []
    with open("data/shadow/results.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") != STRATEGY or r.get("subtype") != SUBTYPE or r.get("decision") != DECISION:
                continue
            if r.get("acierto") not in ("0", "1"):
                continue
            try:
                py = float(r["precio_yes_mercado"])
                pnl = float(r["pnl_neto"])
            except (TypeError, ValueError):
                continue
            if not (BUCKET_LO <= py < BUCKET_HI):
                continue
            fila = (r.get("prediction_timestamp", ""), py, pnl, int(r["acierto"]), r.get("market_id", ""))
            todas.append(fila)
            if r.get("market_id", "") in fillable_market_ids:
                fillable.append(fila)

    for etiqueta, filas in (("TODO el bucket (shadow, sin filtrar fill-ability)", todas),
                             ("SOLO subconjunto FILLABLE (ratio>=5x)", fillable)):
        n = len(filas)
        if n == 0:
            print(f"\n=== {etiqueta} === n=0, nada que evaluar")
            continue
        hits = sum(f[3] for f in filas)
        pnl_medio = sum(f[2] for f in filas) / n
        wlo, whi = wilson90(hits, n)
        breakeven = sum(f[1] for f in filas) / n  # aproximación: precio medio como proxy breakeven YES
        print(f"\n=== {etiqueta} === n={n} hit={hits/n:.3f} wilson90=[{wlo:.3f},{whi:.3f}] "
              f"pnl_medio={pnl_medio:+.4f} py_medio={breakeven:.3f}")
        if n >= 15:
            pnl_arr = np.array([f[2] for f in filas])
            rng = np.random.default_rng(2508)
            signos = rng.choice([-1, 1], size=(2000, n))
            medias_shuffle = (pnl_arr[None, :] * signos).mean(axis=1)
            p_shuffle = float(np.mean(np.abs(medias_shuffle) >= abs(pnl_medio)))
            ordenado = sorted(filas, key=lambda f: f[0])
            mid = n // 2
            m1, m2 = ordenado[:mid], ordenado[mid:]
            pnl1 = sum(f[2] for f in m1) / len(m1) if m1 else 0
            pnl2 = sum(f[2] for f in m2) / len(m2) if m2 else 0
            consist = (pnl1 > 0) == (pnl2 > 0)
            boots = rng.choice(pnl_arr, size=(2000, n), replace=True).mean(axis=1)
            boots.sort()
            ci_lo = boots[int(0.05 * len(boots))]
            ci_hi = boots[int(0.95 * len(boots))]
            print(f"    shuffle p={p_shuffle:.4f} | split-half: 1a={pnl1:+.3f}(n={len(m1)}) "
                  f"2a={pnl2:+.3f}(n={len(m2)}) consistente={consist} | "
                  f"bootstrap CI90%=[{ci_lo:+.4f},{ci_hi:+.4f}]")
        else:
            print("    n<15 -- sin gate riguroso, solo informativo")


if __name__ == "__main__":
    main()
