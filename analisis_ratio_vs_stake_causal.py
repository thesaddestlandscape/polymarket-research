#!/usr/bin/env python3
"""
analisis_ratio_vs_stake_causal.py — #9 del backlog (10-Jul): ¿libro fino en
el momento de la señal predice IC mayor? Hoy ratio_vs_stake solo VETA
ejecución (live_trade.py, libro_snapshots.csv); nunca se ha probado como
señal causal.

Alcance deliberadamente MÁS BARATO que "añadir la feature a
shadow_predict.py": eso exigiría una consulta de libro (HTTP) en CADA
predicción de las ~170 estrategias shadow, exactamente el coste que el
commit 546ccd4c1 (10-Jul) eliminó para todo lo que no ejecuta. El dato de
profundidad YA EXISTE gratis para las tuplas live/candidatas en
libro_snapshots.csv — este script cruza esas filas contra results.csv por
(market_id, strategy, subtype, direction) y mide el hit-rate por bucket de
ratio_vs_stake directamente, sin tocar el pipeline de predicción en vivo.
Si el patrón es fuerte, ENTONCES se justifica pagar el coste de plumbing
hacia shadow_predict.py — no antes.
"""
import csv
from collections import defaultdict
from pathlib import Path

LIBRO = Path("data/live/libro_snapshots.csv")
RESULTS = Path("data/shadow/results.csv")

BUCKETS = [(0, 5), (5, 10), (10, 20), (20, 50), (50, float("inf"))]


def bucket_de(ratio: float) -> str:
    for lo, hi in BUCKETS:
        if lo <= ratio < hi:
            return f"[{lo},{hi if hi != float('inf') else '+inf'})"
    return "?"


def ic_bayes(aciertos: int, n: int) -> float:
    return (aciertos + 1) / (n + 2) - 0.5


def main():
    resultados = {}  # (market_id, strategy, subtype, direction) -> acierto bool
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            acierto = row.get("acierto", "")
            if acierto not in ("True", "False", "1", "0"):
                continue
            key = (row["market_id"], row["strategy"], row["subtype"], row["decision"])
            resultados[key] = acierto in ("True", "1")

    por_bucket = defaultdict(lambda: {"n": 0, "aciertos": 0})
    emparejados = 0
    with open(LIBRO, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                ratio = float(row["ratio_vs_stake"])
            except (ValueError, TypeError):
                continue
            key = (row["market_id"], row["strategy"], row["subtype"], row["direction"])
            if key not in resultados:
                continue
            emparejados += 1
            b = bucket_de(ratio)
            por_bucket[b]["n"] += 1
            por_bucket[b]["aciertos"] += int(resultados[key])

    print(f"Snapshots con ratio_vs_stake cruzados contra resolución real: {emparejados}\n")
    print(f"{'bucket ratio':16} {'n':>5} {'hit%':>7} {'ic_bayes':>9}")
    for lo, hi in BUCKETS:
        b = f"[{lo},{hi if hi != float('inf') else '+inf'})"
        d = por_bucket.get(b, {"n": 0, "aciertos": 0})
        n = d["n"]
        if n == 0:
            print(f"{b:16} {n:>5}")
            continue
        hit = d["aciertos"] / n
        ic = ic_bayes(d["aciertos"], n)
        flag = "  ⚠️ n<15" if n < 15 else ""
        print(f"{b:16} {n:>5} {hit:6.1%} {ic:+9.4f}{flag}")


if __name__ == "__main__":
    main()
