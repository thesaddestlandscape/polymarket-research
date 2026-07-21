#!/usr/bin/env python3
"""Reabre la revisión de fill-ability de BUY_NO#15min pendiente desde el
05-Jul ("inminente" en CLAUDE.md, nunca cerrada formalmente).

21-Jul: primera versión de este script reusaba la lista PRIORIDAD de
analisis_fills.py para elegir un único motivo por señal -- esa lista NO
incluye "candidato_evaluacion" (el motivo real que domina para tuplas que
solo están en candidatos_evaluacion_live, no en pares_permitidos_live), así
que el reporte lo descartaba en silencio y parecía que el dato llevaba
congelado desde el 11-Jul. Era un bug del script, no un freeze real -- el
dato se sigue acumulando sin parar (miles de filas nuevas cada semana).

Corregido: usa directamente candidato_evaluacion como proxy de profundidad
(ratio_vs_stake>=5 = habría pasado el gate real de _consultar_profundidad_
libro) cruzado con el outcome shadow a precio de plan, un mercado único por
(market_id, strategy) con el snapshot más reciente disponible.
"""
import csv
import math
from pathlib import Path

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"
N_MIN = 30


def main():
    outcomes = {}
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r.get("direction") == "BUY_NO" and "15min" in r.get("subtype", "")
                and r.get("motivo") == "candidato_evaluacion"]

    ultimo = {}
    for r in rows:
        key = (r["market_id"], r["strategy"])
        if key not in ultimo or r["timestamp_utc"] > ultimo[key]["timestamp_utc"]:
            ultimo[key] = r

    pasaria, no_pasaria = [], []
    for (mid, strat), r in ultimo.items():
        out = outcomes.get((mid, strat, "BUY_NO"))
        if out is None:
            continue
        try:
            ratio = float(r.get("ratio_vs_stake") or 0.0)
        except ValueError:
            ratio = 0.0
        (pasaria if ratio >= 5 else no_pasaria).append(out)

    def resumen(label, lst):
        n = len(lst)
        if n == 0:
            print(f"{label}: n=0")
            return None
        hit = sum(a for a, _ in lst) / n
        pnl = sum(p for _, p in lst)
        print(f"{label}: n={n} hit={hit*100:.1f}% pnl_total={pnl:+.2f}€ "
              f"pnl_medio={pnl/n:+.3f}€  {'OK' if n >= N_MIN else f'({n}/{N_MIN})'}")
        return n, hit

    p1 = resumen("Habría PASADO el gate 5x (ratio>=5)", pasaria)
    p2 = resumen("Habría sido VETADO (ratio<5)", no_pasaria)

    if p1 and p2:
        n1, h1 = p1
        n2, h2 = p2
        x1, x2 = n1 * h1, n2 * h2
        p_pool = (x1 + x2) / (n1 + n2)
        se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
        z = (h2 - h1) / se if se > 0 else 0.0
        p_val = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
        print(f"\nz={z:.2f} p≈{p_val:.2e}")
        gap = h2 - h1
        if p_val < 0.05 and gap > 0.15:
            print("-> Selección adversa RECONFIRMADA con dato fresco y n grande. "
                  "Sigue bloqueado -- no reabrir BUY_NO#15min a taker plano.")
        else:
            print("-> Gap no significativo o por debajo del umbral -- revisar antes de decidir.")


if __name__ == "__main__":
    main()
