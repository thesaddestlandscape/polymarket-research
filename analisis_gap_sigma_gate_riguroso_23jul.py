#!/usr/bin/env python3
"""
analisis_gap_sigma_gate_riguroso_23jul.py -- P19, siguiente paso pendiente
tras confirmar (22-Jul, idea_gap_sigma_replicado_por_familia_activo_22jul)
que el corte por gap_sigma_implicita replica 8/8 familias y 4/4 activos con
un simple test z de dos proporciones, y tras instrumentar la feature como
logging puro en producción (commit 04c3dffea6, 22-Jul).

Lo que faltaba: el gate RIGUROSO del proyecto (Wilson + shuffle + PnL
bootstrap, analisis_gate_riguroso.gate -- el mismo que usa
franja_milimetrica_ballenas.py, no reimplementado aquí) sobre el subconjunto
"gap bajo" (tercil inferior), por FAMILIA y por ACTIVO, exigiendo n>=40 en
ambos lados + split-half cronológico (primera vs segunda mitad de fechas)
antes de considerar el hallazgo robusto -- mismo criterio que el resto del
proyecto usa para no reportar sobreajuste post-hoc.

Solo lectura. No toca prob_yes, shadow_predict.py ni config_live.json.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_gap_sigma_implicita_realizada_22jul import (  # noqa: E402
    FAMILIA_GBM, DRIFT_DAMPING, DRIFT_DAMPING_DEFAULT, _norm_ppf, _marco_min,
)
from analisis_gate_riguroso import gate  # noqa: E402
import math

RESULTS = Path(__file__).parent / "data/shadow/results.csv"


def calcular_gap(feats, precio_yes, subtype):
    sigma_h = feats.get("sigma_h")
    T_h = feats.get("T_h")
    if sigma_h is None or T_h is None or sigma_h <= 0 or T_h <= 0:
        return None
    pct = feats.get("pct_spot_vs_ref")
    drift_60 = feats.get("drift_60min")
    d_gbm = feats.get("d_gbm")
    py_entrada = feats.get("py_entrada")

    if pct is not None and drift_60 is not None:
        if not (0.001 < precio_yes < 0.999):
            return None
        marco = _marco_min(subtype)
        dd = DRIFT_DAMPING.get(marco, DRIFT_DAMPING_DEFAULT)
        mu_h = (drift_60 / 100.0) * dd
        log_ratio = math.log(1 + pct / 100.0)
        d2_mercado = _norm_ppf(precio_yes)
        if abs(d2_mercado) < 1e-6:
            return None
        sigma_implicita = (log_ratio + mu_h * T_h) / (d2_mercado * math.sqrt(T_h))
    elif d_gbm is not None and py_entrada is not None:
        if not (0.001 < py_entrada < 0.999):
            return None
        d2_mercado = _norm_ppf(py_entrada)
        if abs(d2_mercado) < 1e-6:
            return None
        sigma_implicita = d_gbm * sigma_h / d2_mercado
    else:
        return None

    if not (0 < sigma_implicita <= 1.0):
        return None
    return sigma_implicita - sigma_h


def main():
    import json
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in FAMILIA_GBM:
                continue
            if row.get("acierto") not in ("0", "1"):
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
            row["_activo"] = row["subtype"].split("#")[0] if "#" in row["subtype"] else "?"
            rows.append(row)

    print(f"[gap_sigma gate riguroso] filas GBM con gap fisico: {len(rows)}")
    if not rows:
        return

    gaps = sorted(r["_gap"] for r in rows)
    n_tot = len(gaps)
    t1 = gaps[n_tot // 3]
    print(f"tercil inferior global (fresco, n={n_tot}): t1={t1:.5f}\n")

    def _split_half_ok(grupo):
        """Ordena por timestamp y compara primera vs segunda mitad — ambas
        deben tener PnL medio del mismo signo que el conjunto completo."""
        ordenado = sorted(grupo, key=lambda r: r.get("timestamp_utc", ""))
        mid = len(ordenado) // 2
        h1, h2 = ordenado[:mid], ordenado[mid:]
        if len(h1) < 10 or len(h2) < 10:
            return None
        pnl1 = sum(float(r["pnl_neto"]) for r in h1) / len(h1)
        pnl2 = sum(float(r["pnl_neto"]) for r in h2) / len(h2)
        return pnl1, pnl2

    def _reporta(nombre, grupo_bajo):
        n = len(grupo_bajo)
        if n < 40:
            print(f"  {nombre}: n={n} -- INSUFICIENTE para gate riguroso (n<40)")
            return
        g = gate(grupo_bajo)
        sh = _split_half_ok(grupo_bajo)
        sh_txt = f" | split-half pnl1={sh[0]:+.3f} pnl2={sh[1]:+.3f}" if sh else " | split-half sin n suficiente"
        print(f"  {nombre}: n={n} hit={g['hit']:.1%} IC={g['ic']:+.4f} Wilson90%=[{g['lo']:.1%},{g['hi']:.1%}] "
              f"p_shuf={g['p_shuf']:.3f} pnl/trade={g.get('pnl_media', float('nan')):+.3f} "
              f"PnL_CI90%=[{g.get('pnl_lo', float('nan')):+.3f},{g.get('pnl_hi', float('nan')):+.3f}] "
              f"-> {g['veredicto']}{sh_txt}")

    print("=== GATE RIGUROSO sobre GAP BAJO (tercil inf.), por FAMILIA (strategy) ===")
    por_familia = defaultdict(list)
    for r in rows:
        if r["_gap"] <= t1:
            por_familia[r["strategy"]].append(r)
    for fam in sorted(por_familia):
        _reporta(fam, por_familia[fam])

    print("\n=== GATE RIGUROSO sobre GAP BAJO (tercil inf.), por ACTIVO ===")
    por_activo = defaultdict(list)
    for r in rows:
        if r["_gap"] <= t1:
            por_activo[r["_activo"]].append(r)
    for act in sorted(por_activo):
        _reporta(act, por_activo[act])

    print("\n=== Para contraste: GATE RIGUROSO sobre RESTO (tercil medio+alto), agregado ===")
    resto = [r for r in rows if r["_gap"] > t1]
    _reporta("RESTO (todas familias/activos)", resto)


if __name__ == "__main__":
    main()
