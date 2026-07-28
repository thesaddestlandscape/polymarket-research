#!/usr/bin/env python3
"""
analisis_touch_vs_win_smartexit_28jul.py — mide el hueco "toca vs gana"
sobre data/live/smart_exit_prices.csv (dinero real), por estrategia y por
umbral de precio_lado, mismo espíritu que "Flip Harvester" (backlog ítem C,
idea_moondev_10_hallazgos_priorizados_28jul): dogs tocan el líder mucho más
de lo que ganan sosteniendo hasta resolución — mide si eso también aplica
aquí, para calibrar P18 (take-profit) por familia con datos propios, no
con el múltiplo de la fuente externa.

Solo lectura. n<40 (gate riguroso del proyecto) → SOLO observacional,
NO proponer ningún umbral de TP con esto todavía.
"""
import csv
from collections import defaultdict
from pathlib import Path

PRICES_CSV = Path("data/live/smart_exit_prices.csv")
UMBRALES = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85]
N_MIN_GATE = 40


def cargar():
    por_estrategia = defaultdict(lambda: defaultdict(list))
    for r in csv.DictReader(open(PRICES_CSV, encoding="utf-8")):
        try:
            seg = float(r["seg_desde_entrada"])
            precio_lado = float(r["precio_lado"])
            entry = float(r["entry_price"])
        except (ValueError, TypeError, KeyError):
            continue
        por_estrategia[r["strategy"]][r["market_id"]].append(
            (seg, precio_lado, entry, r["mkt_closed"])
        )
    return por_estrategia


def analizar(mercados: dict):
    resultados = []
    for mid, ticks in mercados.items():
        ticks.sort()
        max_precio = max(t[1] for t in ticks)
        cerrados = [t for t in ticks if t[3] == "1"]
        if not cerrados:
            continue
        ultimo = sorted(cerrados, key=lambda t: t[0])[-1]
        gano = ultimo[1] >= 0.9
        resultados.append((mid, max_precio, gano))
    return resultados


def main():
    por_estrategia = cargar()
    print(f"{'estrategia':<28} {'n_mercados':>10} {'n_cerrados':>11}")
    for strat, mercados in sorted(por_estrategia.items(), key=lambda kv: -len(kv[1])):
        print(f"{strat:<28} {len(mercados):>10} {'':>11}")

    for strat, mercados in por_estrategia.items():
        resultados = analizar(mercados)
        n = len(resultados)
        print(f"\n=== {strat} — n_cerrados={n} "
              f"{'(< gate n>=' + str(N_MIN_GATE) + ', SOLO observacional)' if n < N_MIN_GATE else '(GATE n cumplido)'} ===")
        if n == 0:
            continue
        gano_total = sum(1 for r in resultados if r[2])
        print(f"  win-rate total (hold to resolution): {gano_total}/{n} = {100*gano_total/n:.1f}%")
        for u in UMBRALES:
            tocaron = [r for r in resultados if r[1] >= u]
            if not tocaron:
                continue
            gano_tocaron = sum(1 for r in tocaron if r[2])
            print(f"  umbral={u:.2f}: tocaron={len(tocaron)}/{n} ({100*len(tocaron)/n:.1f}%) "
                  f"| P(gana|tocó)={100*gano_tocaron/len(tocaron):.1f}%")


if __name__ == "__main__":
    main()
