#!/usr/bin/env python3
"""
analisis_gap_sigma_fillability_real_26ago.py — 26-Ago, paso obligatorio
antes de proponer el filtro gap_sigma_implicita (P19) para /code-review:
el gate riguroso de analisis_gap_sigma_gate_riguroso_23jul.py corre
sobre results.csv (shadow, TODAS las señales, incluidas las que nunca
se podrían ejecutar de verdad) -- mismo patrón que TODO lo demás
revisado esta sesión (GBM reactivo, fade de arquetipo A, sol5min
contrario): el shadow agregado sistemáticamente sobreestima el edge
real, casi siempre por selección adversa en el fill.

Repite el mismo cálculo de gap (reusa calcular_gap/FAMILIA_GBM del
script del 23-Jul, sin reimplementar) pero restringido al subconjunto
REALMENTE fillable: colapsa libro_snapshots.csv por market_id (prioridad
canónica de analisis_fills.py), exige ratio_vs_stake>=5x, y solo cuenta
señales GBM_LATE-family cuyo market_id aparece ahí.

Solo lectura.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

csv.field_size_limit(sys.maxsize)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_gap_sigma_implicita_realizada_22jul import FAMILIA_GBM  # noqa: E402
from analisis_gap_sigma_gate_riguroso_23jul import calcular_gap  # noqa: E402
from analisis_gate_riguroso import gate  # noqa: E402
from libro_snapshots_prioridad import prio  # noqa: E402

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
LIBRO = REPO / "data/live/libro_snapshots.csv"
RATIO_MIN = 5.0


def cargar_fillable():
    """(strategy,subtype,decision) -> set(market_id) con ratio_vs_stake>=5x,
    colapsado por prioridad canónica (una señal = un market_id, no filas
    sueltas -- CLAUDE.md pt.3b)."""
    best = {}
    with open(LIBRO) as f:
        r = csv.DictReader(f)
        for row in r:
            if row["strategy"] not in FAMILIA_GBM:
                continue
            key = (row["strategy"], row["subtype"], row["direction"])
            mid = row["market_id"]
            p = prio(row["motivo"])
            cur = best.get((key, mid))
            if cur is None or p < cur[0]:
                best[(key, mid)] = (p, row)
    fillable = defaultdict(set)
    for (key, mid), (p, row) in best.items():
        try:
            ratio = float(row["ratio_vs_stake"])
        except (TypeError, ValueError):
            continue
        if ratio >= RATIO_MIN:
            fillable[key].add(mid)
    return fillable


def main():
    print("Cargando libro_snapshots.csv (colapsado, ratio>=5x)...")
    fillable = cargar_fillable()
    n_fillable_total = sum(len(v) for v in fillable.values())
    print(f"  señales fillable reales (todas las tuplas GBM_LATE-family): {n_fillable_total}")

    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in FAMILIA_GBM:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            key = (row["strategy"], row["subtype"], row["decision"])
            if row["market_id"] not in fillable.get(key, ()):
                continue
            try:
                feats = json.loads(row.get("features") or "{}")
                precio_yes = float(row["precio_yes_mercado"])
            except (ValueError, TypeError, json.JSONDecodeError):
                continue
            gap = calcular_gap(feats, precio_yes, row["subtype"])
            if gap is None:
                continue
            row["_gap"] = gap
            rows.append(row)

    print(f"\nFilas GBM_LATE-family con gap físico Y fillable real: {len(rows)}")
    if not rows:
        print("Sin datos suficientes -- abortando.")
        return

    gaps = sorted(r["_gap"] for r in rows)
    t1 = gaps[len(gaps) // 3]
    print(f"tercil inferior (sobre el subconjunto fillable, n={len(gaps)}): t1={t1:.5f}\n")

    bajo = [r for r in rows if r["_gap"] <= t1]
    resto = [r for r in rows if r["_gap"] > t1]

    def _reporta(nombre, grupo):
        n = len(grupo)
        if n < 15:
            print(f"  {nombre}: n={n} -- INSUFICIENTE (n<15)")
            return
        if n < 40:
            print(f"  {nombre}: n={n} -- por debajo del umbral de gate riguroso (n<40), informativo:")
        g = gate(grupo) if n >= 40 else None
        hit = sum(float(r["acierto"]) for r in grupo) / n
        pnl = sum(float(r["pnl_neto"]) for r in grupo) / n
        if g:
            print(f"  {nombre}: n={n} hit={g['hit']:.1%} IC={g['ic']:+.4f} Wilson90%=[{g['lo']:.1%},{g['hi']:.1%}] "
                  f"p_shuf={g['p_shuf']:.3f} pnl/trade={g.get('pnl_media', float('nan')):+.3f} "
                  f"PnL_CI90%=[{g.get('pnl_lo', float('nan')):+.3f},{g.get('pnl_hi', float('nan')):+.3f}] "
                  f"-> {g['veredicto']}")
        else:
            print(f"    hit={hit:.1%} pnl/trade={pnl:+.3f} (n<40, no gate riguroso completo)")

    print("=== Subconjunto FILLABLE REAL -- GAP BAJO (tercil inf.) ===")
    _reporta("GAP BAJO", bajo)
    print("\n=== Subconjunto FILLABLE REAL -- RESTO (tercil medio+alto) ===")
    _reporta("RESTO", resto)


if __name__ == "__main__":
    main()
