#!/usr/bin/env python3
"""Read-only, one-off (17-Jul, punto 5 de la lista Shannon del checkpoint
del mismo día). `_tendencia_profundidad()` (live_trade.py, commit
`8cb32c967`, 12-Jul) ya mide y loguea `delta_profundidad_eur` en
libro_snapshots.csv -- delta de profundidad entre la lectura actual y la
anterior de la MISMA tupla (VPIN/order-book-imbalance, ver
reference_toxic_flow_mm_tecnicas). Puramente observacional desde entonces,
NUNCA validado: la propia nota de implementación decía "validar con
vigia_causal_vs_fillable.py cuando acumule n≥15" -- 5 días después, 608
filas con delta poblado, momento de comprobarlo.

Hipótesis (VPIN clásico): delta NEGATIVO grande (la profundidad se vacía
justo antes de que intentemos ejecutar) es señal de flujo tóxico/informado
activo en el momento -- debería predecir un acierto PEOR en las señales
que sí llegamos a ejecutar (mismo mecanismo de selección adversa ya
confirmado hoy con ballenas, ahora visto desde el lado del libro en vez
del lado de las wallets).

Método: cruza libro_snapshots.csv (motivo=ejecutada, delta_profundidad_eur
poblado) contra results.csv (mismo market_id+strategy+direction) para el
outcome real, bucketiza por delta y compara hit rate.

No escribe nada, no toca dinero ni config.
Uso: python3 analisis_validacion_tendencia_profundidad_17jul.py
"""
import csv
from pathlib import Path

REPO = Path(__file__).resolve().parent
LIBRO = REPO / "data" / "live" / "libro_snapshots.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"


def cargar_resultados_idx() -> dict:
    """(market_id, strategy, direction) -> acierto (0/1)."""
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1"):
                continue
            idx[(r["market_id"], r["strategy"], r["decision"])] = int(r["acierto"])
    return idx


def main():
    idx = cargar_resultados_idx()
    filas = []  # (delta, acierto)
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            delta_raw = r.get("delta_profundidad_eur")
            if delta_raw in (None, ""):
                continue
            try:
                delta = float(delta_raw)
            except ValueError:
                continue
            ac = idx.get((r["market_id"], r["strategy"], r["direction"]))
            if ac is None:
                continue
            filas.append((delta, ac))

    print(f"Filas (cualquier motivo) con delta_profundidad_eur + outcome real conocido: {len(filas)}")
    if not filas:
        print("Sin datos suficientes, salir.")
        return

    buckets = [(-999999, -50), (-50, -10), (-10, 0), (0, 10), (10, 999999)]
    print(f"\n{'bucket delta_profundidad_eur':<30} {'n':>5} {'hit%':>8}")
    print("-" * 48)
    for lo, hi in buckets:
        sub = [f for f in filas if lo <= f[0] < hi]
        if not sub:
            print(f"[{lo},{hi})".ljust(30) + f"{0:>5}")
            continue
        hit = sum(f[1] for f in sub) / len(sub)
        print(f"[{lo},{hi})".ljust(30) + f"{len(sub):>5}" + f"{hit*100:>7.1f}%")

    # Corte simple: negativo (vaciándose) vs no-negativo (estable/llenándose)
    neg = [f for f in filas if f[0] < 0]
    pos = [f for f in filas if f[0] >= 0]
    print(f"\nCorte simple:")
    if neg:
        print(f"  delta<0 (vaciándose): n={len(neg)} hit={100*sum(f[1] for f in neg)/len(neg):.1f}%")
    if pos:
        print(f"  delta>=0 (estable/llenándose): n={len(pos)} hit={100*sum(f[1] for f in pos)/len(pos):.1f}%")


if __name__ == "__main__":
    main()
