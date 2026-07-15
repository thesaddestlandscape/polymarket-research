#!/usr/bin/env python3
"""
Calibración retrospectiva de un filtro de Kalman 1D (random walk) como
alternativa OBSERVACIONAL a DRIFT_DAMPING (shadow_predict.py) para el drift
que alimenta mu_h en UPDOWN_GBM.

No cambia nada en producción. Solo mide, con datos reales de results.csv
(forward, no backfill de 90d), si un KF que se auto-ajusta ciclo a ciclo
habría clasificado mejor que la fracción fija actual (0.30/0.20/0.05/0.10
por ventana) — grid search de Q/R, simulación cronológica por ventana_min
(mismo split que DRIFT_DAMPING, no por activo todavía — fase 2 si esto
confirma).

Metodología (evita lookahead): el KF predice con el estado PREVIO a ver la
observación de este ciclo (mu_prior), y solo DESPUÉS actualiza su estado con
z_t=drift_60min de este ciclo. La decisión/IC de cada fila usa mu_prior, no
el estado ya actualizado con su propio dato.

Uso: python3 analisis_kalman_drift.py
"""
import csv
import json
import math
from collections import defaultdict

RESULTS_CSV = "data/shadow/results.csv"
EDGE_MINIMO = 0.02
SLIPPAGE_ESTIMADO = 0.02

DRIFT_DAMPING = {5: 0.30, 15: 0.20, 60: 0.05, 240: 0.10}
DRIFT_DAMPING_DEFAULT = 0.10


def _norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _gbm_p_up(spot_over_ref_pct, sigma_h, T_h, mu_h):
    if sigma_h <= 0 or T_h <= 0:
        return None
    sigma_T = sigma_h * math.sqrt(T_h)
    if sigma_T < 1e-9:
        return None
    log_ratio = math.log(1 + spot_over_ref_pct / 100)
    d2 = (log_ratio + mu_h * T_h) / sigma_T
    return _norm_cdf(d2)


def _ic(wins, n, n_ref=50):
    return ((wins + 1) / (n + 2) - 0.5) * min(1.0, n / n_ref)


def _ventana_de_subtype(subtype):
    if "#" not in subtype:
        return None
    suf = subtype.split("#", 1)[1]
    if suf == "daily":
        return None  # T_h no comparable en fracción de hora simple, fuera del scope
    if suf.endswith("min"):
        try:
            return int(suf[:-3])
        except ValueError:
            return None
    return None


def cargar_filas():
    filas = []
    with open(RESULTS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") != "UPDOWN_GBM":
                continue
            if row.get("outcome_real") not in ("YES", "NO"):
                continue
            feats_raw = row.get("features")
            if not feats_raw:
                continue
            try:
                feats = json.loads(feats_raw)
            except Exception:
                continue
            drift_60min = feats.get("drift_60min")
            sigma_h = feats.get("sigma_h")
            pct_spot = feats.get("pct_spot_vs_ref")
            if drift_60min is None or sigma_h is None or pct_spot is None:
                continue
            ventana_min = _ventana_de_subtype(row.get("subtype", ""))
            if ventana_min is None:
                continue
            ts = row.get("prediction_timestamp")
            if not ts:
                continue
            try:
                filas.append({
                    "ts": ts,
                    "ventana_min": ventana_min,
                    "drift_60": float(drift_60min) / 100,  # fracción/hora
                    "sigma_h": float(sigma_h),
                    "pct_spot": float(pct_spot),
                    "T_h": ventana_min / 60,
                    "outcome": row["outcome_real"],
                })
            except (ValueError, TypeError):
                continue
    filas.sort(key=lambda r: r["ts"])
    return filas


def evaluar_static(filas):
    """Baseline: DRIFT_DAMPING estático actual, mismo subset/orden que el KF."""
    wins = n = 0
    por_ventana = defaultdict(lambda: {"wins": 0, "n": 0})
    for r in filas:
        dd = DRIFT_DAMPING.get(r["ventana_min"], DRIFT_DAMPING_DEFAULT)
        mu_h = r["drift_60"] * dd
        p_up = _gbm_p_up(r["pct_spot"], r["sigma_h"], r["T_h"], mu_h)
        if p_up is None:
            continue
        edge = abs(p_up - 0.5)
        if edge - EDGE_MINIMO - SLIPPAGE_ESTIMADO <= 0:
            continue
        dec = "YES" if p_up > 0.5 else "NO"
        acierto = int(dec == r["outcome"])
        wins += acierto
        n += 1
        por_ventana[r["ventana_min"]]["wins"] += acierto
        por_ventana[r["ventana_min"]]["n"] += 1
    return wins, n, por_ventana


def evaluar_kalman(filas, Q, R, P0=1.0):
    """
    Simulación cronológica de un KF random-walk POR ventana_min (mismo split
    que DRIFT_DAMPING). Predice con mu_prior (antes de ver la observación de
    esta fila), luego actualiza el estado con z_t=drift_60 de esta fila.
    """
    estado = defaultdict(lambda: {"mu": 0.0, "P": P0})
    wins = n = 0
    por_ventana = defaultdict(lambda: {"wins": 0, "n": 0})
    for r in filas:
        v = r["ventana_min"]
        st = estado[v]
        mu_prior = st["mu"]

        mu_h = mu_prior
        p_up = _gbm_p_up(r["pct_spot"], r["sigma_h"], r["T_h"], mu_h)
        if p_up is not None:
            edge = abs(p_up - 0.5)
            if edge - EDGE_MINIMO - SLIPPAGE_ESTIMADO > 0:
                dec = "YES" if p_up > 0.5 else "NO"
                acierto = int(dec == r["outcome"])
                wins += acierto
                n += 1
                por_ventana[v]["wins"] += acierto
                por_ventana[v]["n"] += 1

        # Update KF con la observación de este ciclo (drift_60 crudo, no amortiguado)
        z = r["drift_60"]
        K = st["P"] / (st["P"] + R)
        mu_post = mu_prior + K * (z - mu_prior)
        P_post = (1 - K) * st["P"] + Q
        estado[v] = {"mu": mu_post, "P": P_post}

    return wins, n, por_ventana


def main():
    filas = cargar_filas()
    print(f"Filas UPDOWN_GBM con features completas + outcome: {len(filas)}")
    if len(filas) < 100:
        print("  n insuficiente para calibrar con rigor, abortando.")
        return

    por_v = defaultdict(int)
    for r in filas:
        por_v[r["ventana_min"]] += 1
    print("Distribución por ventana_min:", dict(sorted(por_v.items())))

    wins_s, n_s, pv_s = evaluar_static(filas)
    ic_s = _ic(wins_s, n_s) if n_s else None
    print(f"\n== BASELINE (DRIFT_DAMPING estático actual) ==")
    print(f"  n={n_s}  {wins_s}/{n_s} ({wins_s/n_s*100:.1f}%)  IC={ic_s:+.4f}" if n_s else "  n=0")
    for v, d in sorted(pv_s.items()):
        if d["n"] >= 15:
            ic = _ic(d["wins"], d["n"])
            print(f"    ventana={v:>4}min  n={d['n']:5d}  hit={d['wins']/d['n']*100:.1f}%  IC={ic:+.4f}")

    print(f"\n== GRID SEARCH Kalman (Q,R) — random walk, P0=1.0 ==")
    resultados = []
    for Q in [0.0001, 0.001, 0.005, 0.01, 0.05]:
        for R in [0.05, 0.1, 0.25, 0.5, 1.0, 2.0]:
            wins_k, n_k, pv_k = evaluar_kalman(filas, Q, R)
            if n_k < 30:
                continue
            ic_k = _ic(wins_k, n_k)
            resultados.append((Q, R, wins_k, n_k, ic_k, pv_k))

    resultados.sort(key=lambda x: -x[4])
    print(f"  {'Q':>8} {'R':>6} {'n':>6} {'hit%':>7} {'IC':>8}")
    for Q, R, wins_k, n_k, ic_k, pv_k in resultados[:15]:
        print(f"  {Q:>8} {R:>6} {n_k:>6} {wins_k/n_k*100:>6.1f}% {ic_k:>+8.4f}")

    if resultados:
        best = resultados[0]
        Q_best, R_best, wins_b, n_b, ic_b, pv_b = best
        print(f"\n  → MEJOR: Q={Q_best} R={R_best}  n={n_b}  IC={ic_b:+.4f}  "
              f"(baseline IC={ic_s:+.4f}, n={n_s})")
        print(f"  Desagregado por ventana (mejor Q,R):")
        for v, d in sorted(pv_b.items()):
            if d["n"] >= 15:
                ic = _ic(d["wins"], d["n"])
                print(f"    ventana={v:>4}min  n={d['n']:5d}  hit={d['wins']/d['n']*100:.1f}%  IC={ic:+.4f}")


if __name__ == "__main__":
    main()
