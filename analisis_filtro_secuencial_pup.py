#!/usr/bin/env python3
"""Propuesta #1 backlog quant-desk (13-jul, Part IV particle filter):
¿suavizar el spot (media móvil 2-3min) en vez del snapshot instantáneo que
usa hoy _s_gbm_late reduce el ruido de la señal, o empeora?

_s_gbm_late (shadow_predict.py:2204) usa spot = _cargar_spot()[activo], un
único tick, para d = ln(spot/ref)/(sigma_h*sqrt(T_h)) → p_up. sigma_h
alimenta GBM_LATE_15M EN VIVO (5 tuplas whitelisted) — mismo rigor que
código de dinero real (project_state_2026-07-11): SOLO ANÁLISIS, no toca
shadow_predict.py salvo que el resultado sea contundente.

Metodología: para cada predicción histórica resuelta de la familia
GBM_LATE_15M (results.csv, 02-Jul→hoy, n=4512), reconstruye spot_raw (tick
más cercano al timestamp de la predicción) y ref (despejado de
drift_ventana_pct ya logueado, ambos desde data/prices/) para VALIDAR la
reconstrucción, luego calcula spot_smoothed (media de los ticks de los
últimos 2/3min) con el MISMO ref y sigma_h/T_h ya logueados → p_up_raw vs
p_up_smoothed, comparados contra el outcome_real real vía Brier score
(calibración) y tasa de acierto en los casos de desacuerdo de dirección.

Uso: python3 analisis_filtro_secuencial_pup.py
"""
import csv
import json
import math
import statistics
from datetime import datetime, timezone, timedelta

from analisis_ewma_vol import cargar_precios, _series_por_asset, _ventana

RESULTS_CSV = "data/shadow/results.csv"
FAMILIA = {"GBM_LATE_15M", "GBM_LATE_15M_ESPACIO_ATR", "GBM_LATE_15M_TARDIO"}
SMOOTH_WINDOWS_MIN = [2, 3]


def _norm_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _tick_mas_cercano(ts_list, precio_list, ts, tol_min=3):
    import bisect
    i = bisect.bisect_left(ts_list, ts)
    candidatos = []
    if i < len(ts_list):
        candidatos.append(i)
    if i > 0:
        candidatos.append(i - 1)
    mejor, mejor_d = None, None
    for c in candidatos:
        d = abs((ts_list[c] - ts).total_seconds())
        if mejor_d is None or d < mejor_d:
            mejor_d, mejor = d, c
    if mejor is not None and mejor_d <= tol_min * 60:
        return precio_list[mejor]
    return None


def main():
    rows = list(csv.DictReader(open(RESULTS_CSV)))
    fam = [r for r in rows if r["strategy"] in FAMILIA and r.get("outcome_real") in ("YES", "NO")]
    print(f"Filas de la familia GBM_LATE_15M resueltas: {len(fam)}")

    precios = cargar_precios()
    series = _series_por_asset(precios)
    print(f"Precios cargados: {len(precios)} puntos")

    n_total = 0
    n_reconstruccion_ok = 0
    brier_raw_sum = 0.0
    brier_smooth_sum = {w: 0.0 for w in SMOOTH_WINDOWS_MIN}
    n_disagree = {w: 0 for w in SMOOTH_WINDOWS_MIN}
    n_disagree_raw_gano = {w: 0 for w in SMOOTH_WINDOWS_MIN}
    n_disagree_smooth_gano = {w: 0 for w in SMOOTH_WINDOWS_MIN}

    for r in fam:
        try:
            feats = json.loads(r.get("features", "{}") or "{}")
            d_raw = float(feats["d_gbm"])
            sigma_h = float(feats["sigma_h"])
            T_h = float(feats["T_h"])
            drift_pct = float(feats["drift_ventana_pct"])  # ya en %
        except (KeyError, ValueError, TypeError):
            continue
        if sigma_h <= 0 or T_h <= 0:
            continue
        subtype = r.get("subtype", "")
        activo = subtype.split("#")[0] if "#" in subtype else subtype
        if activo not in series:
            continue
        try:
            ts_pred = datetime.fromisoformat(r["prediction_timestamp"].replace("Z", "+00:00"))
            if ts_pred.tzinfo is None:
                ts_pred = ts_pred.replace(tzinfo=timezone.utc)
        except Exception:
            continue

        ts_list, precio_list = series[activo]
        spot_raw = _tick_mas_cercano(ts_list, precio_list, ts_pred, tol_min=3)
        if spot_raw is None:
            continue
        n_total += 1

        ref = spot_raw / (1 + drift_pct / 100)
        if ref <= 0:
            continue

        # Validar reconstrucción: d recalculado con spot_raw reconstruido
        # debe aproximar el d_gbm ya logueado en producción.
        denom = sigma_h * math.sqrt(max(T_h, 1e-6))
        d_recalc = math.log(spot_raw / ref) / denom
        if abs(d_recalc - d_raw) > 0.05:
            continue  # reconstrucción no fiable para esta fila, descartar
        n_reconstruccion_ok += 1

        outcome_yes = 1.0 if r["outcome_real"] == "YES" else 0.0
        p_up_raw = _norm_cdf(d_raw)
        brier_raw_sum += (p_up_raw - outcome_yes) ** 2

        for w in SMOOTH_WINDOWS_MIN:
            ventana = _ventana(ts_list, precio_list, ts_pred - timedelta(minutes=w), ts_pred)
            if len(ventana) < 2:
                continue
            spot_smooth = statistics.mean(p for _, p in ventana)
            d_smooth = math.log(spot_smooth / ref) / denom
            p_up_smooth = _norm_cdf(d_smooth)
            brier_smooth_sum[w] += (p_up_smooth - outcome_yes) ** 2

            signo_raw = d_raw >= 0
            signo_smooth = d_smooth >= 0
            if signo_raw != signo_smooth:
                n_disagree[w] += 1
                acierto_raw = (signo_raw and outcome_yes == 1.0) or (not signo_raw and outcome_yes == 0.0)
                acierto_smooth = (signo_smooth and outcome_yes == 1.0) or (not signo_smooth and outcome_yes == 0.0)
                if acierto_raw:
                    n_disagree_raw_gano[w] += 1
                if acierto_smooth:
                    n_disagree_smooth_gano[w] += 1

    print(f"Filas con spot reconstruido: {n_total}")
    print(f"Filas con reconstrucción validada (|d_recalc-d_gbm|<=0.05): {n_reconstruccion_ok}")
    if n_reconstruccion_ok < 15:
        print("n insuficiente (<15) para concluir nada — parar aquí.")
        return

    print()
    print(f"Brier score p_up_raw (actual, snapshot único): {brier_raw_sum / n_reconstruccion_ok:.5f}")
    for w in SMOOTH_WINDOWS_MIN:
        n_ok_w = n_reconstruccion_ok
        print(f"Brier score p_up_smoothed_{w}min: {brier_smooth_sum[w] / n_ok_w:.5f}")

    print()
    print("Casos donde raw y smoothed discrepan en signo de d (dirección de la señal):")
    for w in SMOOTH_WINDOWS_MIN:
        n_d = n_disagree[w]
        if n_d == 0:
            print(f"  ventana {w}min: 0 discrepancias")
            continue
        print(f"  ventana {w}min: n={n_d} | raw acierta {n_disagree_raw_gano[w]} "
              f"({100*n_disagree_raw_gano[w]/n_d:.1f}%) | smoothed acierta "
              f"{n_disagree_smooth_gano[w]} ({100*n_disagree_smooth_gano[w]/n_d:.1f}%)")

    print()
    print("=" * 70)
    print("Lectura: Brier MÁS BAJO = mejor calibrado. Si smoothed no mejora Brier "
          "Y no gana más en los casos de discrepancia, no hay caso para tocar "
          "_s_gbm_late (que alimenta GBM_LATE_15M en vivo).")


if __name__ == "__main__":
    main()
