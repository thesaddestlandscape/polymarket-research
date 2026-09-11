#!/usr/bin/env python3
"""
analisis_gap_sigma_implicita_realizada_22jul.py -- repite el hallazgo
21-Jul (idea_gap_sigma_implicita_realizada_gbm_21jul, P19 en CLAUDE.md)
con el rigor pendiente: desagregado por FAMILIA/ACTIVO por separado (el
21-Jul estaba agregado, mismo riesgo de mezclar mecanismos distintos que
ya se vio con el corte de precio) + fill-ability real del subconjunto
"gap bajo" excluido (join contra libro_snapshots.csv).

Idea (adaptada del paper SSRN 6712647, VRP en equity): nuestro propio
modelo GBM (_gbm_p_up en shadow_predict.py) es matemáticamente un pricing
de opción binaria. Invirtiendo esa fórmula con el PRECIO DE MERCADO de
Polymarket en vez de sigma_h propia, se obtiene la volatilidad que el
mercado está precian do implícitamente -- el análogo de la "volatilidad
implícita" de opciones.

    mu_h = (drift_60min/100) * DRIFT_DAMPING[ventana]   -- mismo drift
           amortiguado que usa el modelo real (shadow_predict.py:1721-22)
    log_ratio = log(1 + pct_spot_vs_ref/100)
    d2_mercado = norm_ppf(precio_yes_mercado)
    sigma_implicita = (log_ratio + mu_h*T_h) / (d2_mercado * sqrt(T_h))
    gap = sigma_implicita - sigma_h

Nota importante: la fórmula documentada en la memoria 21-Jul omitía el
término mu_h*T_h (asumía drift cero). Aquí se incluye para que la
inversión sea EXACTAMENTE la contraparte de _gbm_p_up tal y como se usa
en producción -- si mu_h se omite, sigma_implicita queda sesgada cuando
el drift es fuerte, y el gap deja de medir lo que dice medir.

Puramente análisis/shadow, solo lectura -- no toca shadow_predict.py,
prob_yes ni ninguna decisión real.

Uso: python3 analisis_gap_sigma_implicita_realizada_22jul.py
"""
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).parent
RESULTS = DIR / "data/shadow/results.csv"
LIBRO = DIR / "data/live/libro_snapshots.csv"

FAMILIA_GBM = {
    "UPDOWN_GBM", "UPDOWN_GBM_15M_TARDIO", "GBM_LATE_15M",
    "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR",
    "GBM_LATE_15M_PYCONFIRMADO", "GBM_LATE_60M",
    "GBM_LATE_60M_PYCONFIRMADO", "GBM_LATE_5M",
}
DRIFT_DAMPING = {5: 0.30, 15: 0.20, 60: 0.05, 240: 0.10}
DRIFT_DAMPING_DEFAULT = 0.10


def _norm_cdf(x):
    if x < -8.0: return 0.0
    if x > 8.0: return 1.0
    sign = 1.0 if x >= 0 else -1.0
    x = abs(x)
    t = 1.0 / (1.0 + 0.2316419 * x)
    d = 0.3989422820 * math.exp(-0.5 * x * x)
    p = d * t * (0.3193815302 + t * (-0.3565637813 + t * (1.7814779372
        + t * (-1.8212559978 + t * 1.3302744929))))
    return 1.0 - p if sign > 0 else p


def _norm_ppf(p, lo=-8.0, hi=8.0, it=60):
    if p <= 1e-9: return -8.0
    if p >= 1 - 1e-9: return 8.0
    for _ in range(it):
        mid = (lo + hi) / 2
        if _norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _marco_min(subtype):
    if "#" not in subtype:
        return None
    m = subtype.split("#")[1]
    try:
        return int(m.replace("min", ""))
    except ValueError:
        return None


def _wilson(hits, n, z=1.645):
    if n == 0:
        return (0.0, 0.0)
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((centro - margen) / denom, (centro + margen) / denom)


def _z_two_prop(h1, n1, h2, n2):
    if n1 == 0 or n2 == 0:
        return 1.0
    p1, p2 = h1 / n1, h2 / n2
    p_pool = (h1 + h2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    z = (p1 - p2) / se
    return 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))


def main():
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in FAMILIA_GBM:
                continue
            if row.get("acierto") not in ("0", "1", "0.0", "1.0", "True", "False"):
                continue
            feats_raw = row.get("features") or "{}"
            try:
                feats = json.loads(feats_raw)
            except json.JSONDecodeError:
                continue
            sigma_h = feats.get("sigma_h")
            T_h = feats.get("T_h")
            if sigma_h is None or T_h is None or sigma_h <= 0 or T_h <= 0:
                continue

            # Esquema A: UPDOWN_GBM / UPDOWN_GBM_15M_TARDIO -- features crudas.
            pct = feats.get("pct_spot_vs_ref")
            drift_60 = feats.get("drift_60min")
            # Esquema B: familia GBM_LATE_* -- ya trae d_gbm (=d2 del modelo) y py_entrada.
            d_gbm = feats.get("d_gbm")
            py_entrada = feats.get("py_entrada")

            d2_mercado = None
            sigma_implicita = None
            if pct is not None and drift_60 is not None:
                try:
                    precio_yes = float(row["precio_yes_mercado"])
                except (ValueError, TypeError):
                    continue
                if not (0.001 < precio_yes < 0.999):
                    continue
                marco = _marco_min(row["subtype"])
                dd = DRIFT_DAMPING.get(marco, DRIFT_DAMPING_DEFAULT)
                mu_h = (drift_60 / 100.0) * dd
                log_ratio = math.log(1 + pct / 100.0)
                d2_mercado = _norm_ppf(precio_yes)
                if abs(d2_mercado) < 1e-6:
                    continue
                sigma_implicita = (log_ratio + mu_h * T_h) / (d2_mercado * math.sqrt(T_h))
            elif d_gbm is not None and py_entrada is not None:
                if not (0.001 < py_entrada < 0.999):
                    continue
                d2_mercado = _norm_ppf(py_entrada)
                if abs(d2_mercado) < 1e-6:
                    continue
                # d_gbm = (log_ratio + mu_h*T_h) / (sigma_h*sqrt(T_h))  =>
                # sigma_implicita = d_gbm*sigma_h/d2_mercado (mismo numerador, sigma distinta)
                sigma_implicita = d_gbm * sigma_h / d2_mercado
            else:
                continue

            if sigma_implicita <= 0 or sigma_implicita > 1.0:
                continue  # rango no fisico -> descartar (d2_mercado casi 0 u otros outliers)
            gap = sigma_implicita - sigma_h

            hit = 1 if row["acierto"] in ("1", "1.0", "True") else 0
            pnl = float(row["pnl_neto"]) if row.get("pnl_neto") else 0.0
            activo = row["subtype"].split("#")[0] if "#" in row["subtype"] else "?"
            rows.append({
                "strategy": row["strategy"], "subtype": row["subtype"], "activo": activo,
                "marco": marco, "decision": row["decision"], "market_id": row["market_id"],
                "gap": gap, "hit": hit, "pnl": pnl,
            })

    print(f"[gap_sigma] filas GBM con features completas y sigma_implicita fisica: {len(rows)}")
    if not rows:
        return

    gaps = sorted(r["gap"] for r in rows)
    n_tot = len(gaps)
    t1 = gaps[n_tot // 3]
    t2 = gaps[2 * n_tot // 3]
    print(f"[gap_sigma] terciles globales (replicando corte 21-Jul): t1={t1:.5f} t2={t2:.5f}")

    for r in rows:
        r["gap_bajo"] = r["gap"] <= t1

    # --- replica agregada (sanity check vs 21-Jul: n=443/886, hit=53.3%/69.8%) ---
    bajo = [r for r in rows if r["gap_bajo"]]
    resto = [r for r in rows if not r["gap_bajo"]]
    for nombre, grupo in [("GAP BAJO (agregado, replica 21-Jul)", bajo), ("RESTO (agregado)", resto)]:
        n = len(grupo)
        hits = sum(r["hit"] for r in grupo)
        pnl_medio = sum(r["pnl"] for r in grupo) / n if n else 0
        lo, hi = _wilson(hits, n)
        print(f"  {nombre}: n={n} hit={hits/n:.1%} Wilson90%=[{lo:.1%},{hi:.1%}] pnl/trade={pnl_medio:+.3f}")

    # --- desagregado por FAMILIA (strategy) ---
    print("\n=== POR FAMILIA (strategy), usando el corte global t1 ===")
    por_familia = defaultdict(lambda: {"bajo": [], "resto": []})
    for r in rows:
        por_familia[r["strategy"]]["bajo" if r["gap_bajo"] else "resto"].append(r)
    for fam, g in sorted(por_familia.items()):
        b, rs = g["bajo"], g["resto"]
        if len(b) < 15 or len(rs) < 15:
            print(f"  {fam}: n_bajo={len(b)} n_resto={len(rs)} -- INSUFICIENTE (n<15), no concluye")
            continue
        hb, hr = sum(x["hit"] for x in b), sum(x["hit"] for x in rs)
        pb = sum(x["pnl"] for x in b) / len(b)
        pr = sum(x["pnl"] for x in rs) / len(rs)
        pval = _z_two_prop(hb, len(b), hr, len(rs))
        print(f"  {fam}: bajo n={len(b)} hit={hb/len(b):.1%} pnl/trade={pb:+.3f} | "
              f"resto n={len(rs)} hit={hr/len(rs):.1%} pnl/trade={pr:+.3f} | p={pval:.4f}")

    # --- desagregado por ACTIVO ---
    print("\n=== POR ACTIVO, usando el corte global t1 ===")
    por_activo = defaultdict(lambda: {"bajo": [], "resto": []})
    for r in rows:
        por_activo[r["activo"]]["bajo" if r["gap_bajo"] else "resto"].append(r)
    for act, g in sorted(por_activo.items()):
        b, rs = g["bajo"], g["resto"]
        if len(b) < 15 or len(rs) < 15:
            print(f"  {act}: n_bajo={len(b)} n_resto={len(rs)} -- INSUFICIENTE (n<15), no concluye")
            continue
        hb, hr = sum(x["hit"] for x in b), sum(x["hit"] for x in rs)
        pb = sum(x["pnl"] for x in b) / len(b)
        pr = sum(x["pnl"] for x in rs) / len(rs)
        pval = _z_two_prop(hb, len(b), hr, len(rs))
        print(f"  {act}: bajo n={len(b)} hit={hb/len(b):.1%} pnl/trade={pb:+.3f} | "
              f"resto n={len(rs)} hit={hr/len(rs):.1%} pnl/trade={pr:+.3f} | p={pval:.4f}")

    # --- fill-ability real del subconjunto "gap bajo" excluido (join libro_snapshots) ---
    print("\n=== FILL-ABILITY real (libro_snapshots.csv) — gap_bajo vs resto ===")
    libro_idx = defaultdict(list)  # (market_id, strategy, subtype, direction) -> [motivo,...]
    with open(LIBRO, encoding="utf-8") as f:
        for lr in csv.DictReader(f):
            key = (lr["market_id"], lr["strategy"], lr["subtype"], lr["direction"])
            libro_idx[key].append(lr["motivo"])

    def _fillrate(grupo):
        con_snapshot = 0
        ejecutada = 0
        veto_profundidad = 0
        for r in grupo:
            key = (r["market_id"], r["strategy"], r["subtype"], r["decision"])
            motivos = libro_idx.get(key)
            if not motivos:
                continue
            con_snapshot += 1
            if "ejecutada" in motivos:
                ejecutada += 1
            if "veto_profundidad" in motivos:
                veto_profundidad += 1
        return con_snapshot, ejecutada, veto_profundidad

    cb, eb, vb = _fillrate(bajo)
    cr, er, vr = _fillrate(resto)
    print(f"  GAP BAJO: {cb}/{len(bajo)} con snapshot de libro | ejecutada={eb} veto_profundidad={vb}"
          + (f" | fill-rate={eb/cb:.1%}" if cb else " | sin snapshots suficientes"))
    print(f"  RESTO:    {cr}/{len(resto)} con snapshot de libro | ejecutada={er} veto_profundidad={vr}"
          + (f" | fill-rate={er/cr:.1%}" if cr else " | sin snapshots suficientes"))


if __name__ == "__main__":
    main()
