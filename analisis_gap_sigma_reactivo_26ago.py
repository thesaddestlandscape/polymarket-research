#!/usr/bin/env python3
"""
analisis_gap_sigma_reactivo_26ago.py — 26-Ago, corrección explícita de
Javi sobre analisis_gap_sigma_fillability_real_26ago.py: ese script usó
libro_snapshots.csv (motivo candidato_evaluacion, cadencia ~20s) como
fuente de fill-ability -- la MISMA fuente lenta que ya se demostró
adversamente seleccionada para GBM_LATE (fill-ability 0,1% baseline,
resuelto con gbm_late_reactivo_fase0.py, websocket ~145ms). Usar la
fuente lenta para "refutar" un filtro de GBM_LATE es exactamente el
error que feedback_predictions_csv_no_libro_snapshots_baja_latencia_
26ago ya advirtió: comprobar SIEMPRE si existe una fuente de fill-
ability dedicada antes de concluir con la genérica.

Repite la verificación de gap_sigma_implicita (P19) pero contra la
fill-ability REACTIVA real (gbm_late_reactivo_fase0.csv, ratio_vs_
stake>=5x), no contra libro_snapshots.csv.
"""
import csv
import json
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_gap_sigma_implicita_realizada_22jul import FAMILIA_GBM  # noqa: E402
from analisis_gap_sigma_gate_riguroso_23jul import calcular_gap  # noqa: E402
from analisis_gate_riguroso import gate  # noqa: E402

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
REACTIVO = REPO / "data/shadow/gbm_late_reactivo_fase0.csv"
RATIO_MIN = 5.0


def cargar_fillable_reactivo():
    """market_id -> True si ratio_vs_stake>=5x en el ejecutor reactivo
    (websocket, ~145ms) -- no está desglosado por decision/subtype, el
    trigger reactivo es por (activo, market_id), aplica a cualquier
    variante GBM_LATE que dispare sobre ese mismo mercado."""
    fillable = set()
    with open(REACTIVO) as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                ratio = float(row["ratio_vs_stake"])
            except (TypeError, ValueError):
                continue
            if ratio >= RATIO_MIN:
                fillable.add(row["market_id"])
    return fillable


def main():
    fillable = cargar_fillable_reactivo()
    print(f"market_id únicos fillable (reactivo, ratio>=5x): {len(fillable)}")

    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in FAMILIA_GBM:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            if row["market_id"] not in fillable:
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

    print(f"Filas GBM_LATE-family con gap físico Y fillable reactivo: {len(rows)}")
    if len(rows) < 15:
        print("n insuficiente incluso para split en dos grupos -- reportar agregado solo.")
        if rows:
            n = len(rows)
            hit = sum(float(r["acierto"]) for r in rows) / n
            pnl = sum(float(r["pnl_neto"]) for r in rows) / n
            print(f"  AGREGADO (sin split por gap): n={n} hit={hit:.1%} pnl/trade={pnl:+.3f}")
        return

    gaps = sorted(r["_gap"] for r in rows)
    t1 = gaps[len(gaps) // 3]
    print(f"tercil inferior (n={len(gaps)}): t1={t1:.5f}\n")

    bajo = [r for r in rows if r["_gap"] <= t1]
    resto = [r for r in rows if r["_gap"] > t1]

    def _reporta(nombre, grupo):
        n = len(grupo)
        if n < 15:
            print(f"  {nombre}: n={n} -- INSUFICIENTE (n<15)")
            return
        hit = sum(float(r["acierto"]) for r in grupo) / n
        pnl = sum(float(r["pnl_neto"]) for r in grupo) / n
        if n >= 40:
            g = gate(grupo)
            print(f"  {nombre}: n={n} hit={g['hit']:.1%} IC={g['ic']:+.4f} Wilson90%=[{g['lo']:.1%},{g['hi']:.1%}] "
                  f"p_shuf={g['p_shuf']:.3f} pnl/trade={g.get('pnl_media', float('nan')):+.3f} -> {g['veredicto']}")
        else:
            print(f"  {nombre}: n={n} hit={hit:.1%} pnl/trade={pnl:+.3f} (n<40, informativo)")

    print("=== FILLABLE REACTIVO -- GAP BAJO (tercil inf.) ===")
    _reporta("GAP BAJO", bajo)
    print("\n=== FILLABLE REACTIVO -- RESTO (tercil medio+alto) ===")
    _reporta("RESTO", resto)


if __name__ == "__main__":
    main()
