"""P17 (CLAUDE.md): lectura FORWARD de meta_score_gbm_late contra acierto real.

Puramente informativo -- NO decide nada, no toca prob_yes/edge/decision.
Compara el meta-score (P17, Ridge/logistica sobre 6 features) contra el
prob_yes_modelo que ya usa la estrategia real (basado en norm_cdf(d_gbm)),
sobre las filas resueltas desde que empezo a loguearse (2026-07-18 ~09:13
UTC). Lectura temprana explicitamente parcial: CLAUDE.md exige >=2 semanas
o n>=300 forward antes de proponer sustituir prob_yes -- este script no
adelanta esa decision, solo deja ver donde esta el marcador hoy.

Uso: python3 analisis_meta_score_gbm_late_forward.py
"""
import csv
import json
import sys
from datetime import datetime, timezone

from sklearn.metrics import roc_auc_score, brier_score_loss

RES = "data/shadow/results.csv"
INICIO_LOGUEO = datetime(2026, 7, 18, 9, 13, 0, tzinfo=timezone.utc)

FAMILIA_GBM_LATE = {
    "GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR",
    "GBM_LATE_60M", "GBM_LATE_15M_PYCONFIRMADO",
}


def cargar_filas():
    filas = []
    with open(RES, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in FAMILIA_GBM_LATE:
                continue
            try:
                ts = datetime.fromisoformat(row["resolution_timestamp"].replace("Z", "+00:00"))
            except ValueError:
                continue
            if ts < INICIO_LOGUEO:
                continue
            try:
                feats = json.loads(row["features"])
            except (json.JSONDecodeError, TypeError):
                continue
            score = feats.get("meta_score_gbm_late")
            if score is None:
                continue
            try:
                prob_baseline = float(row["prob_yes_modelo"])
            except (ValueError, TypeError):
                continue
            y_true = 1 if row["outcome_real"] == "YES" else 0
            filas.append({
                "strategy": row["strategy"], "subtype": row["subtype"],
                "decision": row["decision"], "meta_score": score,
                "prob_baseline": prob_baseline, "y_true": y_true,
                "ts": ts,
            })
    return filas


def reportar(nombre, filas):
    n = len(filas)
    print(f"\n--- {nombre} (n={n}) ---")
    if n < 30:
        print("  n<30, no se calcula AUC/Brier (demasiado ruido).")
        return
    y = [f["y_true"] for f in filas]
    meta = [f["meta_score"] for f in filas]
    base = [f["prob_baseline"] for f in filas]
    if len(set(y)) < 2:
        print("  outcome_real sin variación (todo YES o todo NO) -- AUC no definido.")
        return
    auc_meta = roc_auc_score(y, meta)
    auc_base = roc_auc_score(y, base)
    brier_meta = brier_score_loss(y, meta)
    brier_base = brier_score_loss(y, base)
    print(f"  AUC   meta_score_gbm_late = {auc_meta:.3f}  |  prob_yes_modelo (baseline) = {auc_base:.3f}")
    print(f"  Brier meta_score_gbm_late = {brier_meta:.4f} |  prob_yes_modelo (baseline) = {brier_base:.4f}  (menor=mejor)")


def main():
    filas = cargar_filas()
    if not filas:
        print("Sin filas con meta_score_gbm_late resuelto todavia.")
        sys.exit(0)

    dias = (max(f["ts"] for f in filas) - INICIO_LOGUEO).total_seconds() / 86400
    print(f"Filas totales familia GBM_LATE con meta_score logueado: {len(filas)}")
    print(f"Ventana forward acumulada: {dias:.2f} dias desde {INICIO_LOGUEO.isoformat()}")
    print("Gate CLAUDE.md antes de tocar prob_yes: >=2 semanas (14d) O n>=300 forward, "
          "+ aprobacion explicita de Javi + /code-review. Este script NO decide, solo informa.")

    reportar("TODAS (5 hermanas, ambas direcciones)", filas)
    reportar("Solo BUY_YES (población de entrenamiento original)",
              [f for f in filas if f["decision"] == "BUY_YES"])
    reportar("Solo BUY_NO (generalización a la dirección opuesta, nunca entrenada)",
              [f for f in filas if f["decision"] == "BUY_NO"])

    por_estrategia = {}
    for f in filas:
        por_estrategia.setdefault(f["strategy"], []).append(f)
    print("\n--- Desagregado por estrategia ---")
    for estr, fs in sorted(por_estrategia.items()):
        reportar(estr, fs)


if __name__ == "__main__":
    main()
