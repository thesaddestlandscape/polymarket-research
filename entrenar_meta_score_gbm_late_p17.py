#!/usr/bin/env python3
"""P17 (CLAUDE.md backlog, análisis original 11-Jul): meta-score Ridge
(regresión logística L2) sobre GBM_LATE_15M#BUY_YES combinando
d_gbm+sigma_h+drift_ventana_pct+hora_utc+restante_min+T_h, en vez de solo
norm_cdf(d_gbm). 11-Jul: walk-forward 70/30 (n=1580) dio AUC=0.670 — este
script reproduce ese resultado con el dataset actual (n=2605, 18-Jul) y
GUARDA el modelo para que shadow_predict.py lo cargue y loguee
`meta_score_gbm_late` como feature PURAMENTE INFORMATIVA (no toca prob_yes
ni ninguna decisión — CLAUDE.md exige ≥2 semanas / n≥300 forward de este
logueo antes de siquiera proponer sustituir norm_cdf(d_gbm), y aprobación
explícita de Javi + /code-review para tocar la probabilidad real).

Split walk-forward temporal (no aleatorio -- evita fuga de autocorrelación
entre ventanas cercanas): 70% más antiguo = train, 30% más reciente = test.
AUC de test es la honesta; el modelo final que se GUARDA se reentrena con
el 100% de los datos (sin fuga hacia el futuro real: todo esto es pasado,
lo que cuenta para "no fuga" es que el logueo forward de aquí en adelante
usa datos que el modelo nunca ha visto, sea cual sea el split usado para
validar).

Solo lectura de results.csv, solo escritura de
data/shadow/meta_score_gbm_late_model.json. No toca config_live.json,
pares_permitidos_live ni ningún gate de dinero real.

Uso: python3 entrenar_meta_score_gbm_late_p17.py
(requiere sklearn -- disponible en el python3 del sistema, no en .venv)
"""
import csv
import json
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

DIR = Path(__file__).parent
RESULTS = DIR / "data/shadow/results.csv"
MODELO_OUT = DIR / "data/shadow/meta_score_gbm_late_model.json"

FEATURES = ["d_gbm", "sigma_h", "drift_ventana_pct", "hora_utc", "restante_min", "T_h"]


def cargar_dataset():
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") != "GBM_LATE_15M" or r.get("decision") != "BUY_YES":
                continue
            if r.get("acierto") not in ("0", "1"):
                continue
            try:
                feats = json.loads(r["features"])
            except Exception:
                continue
            if any(feats.get(k) is None for k in FEATURES):
                continue
            filas.append({
                "ts": r.get("prediction_timestamp", ""),
                "x": [float(feats[k]) for k in FEATURES],
                "y": int(r["acierto"]),
            })
    filas.sort(key=lambda r: r["ts"])
    return filas


def main():
    filas = cargar_dataset()
    n = len(filas)
    print(f"Dataset GBM_LATE_15M#BUY_YES con features completas: n={n}")
    if n < 200:
        print("n insuficiente para entrenar con confianza -- abortando.")
        return 1

    X = np.array([r["x"] for r in filas])
    y = np.array([r["y"] for r in filas])

    corte = int(n * 0.7)
    X_train, X_test = X[:corte], X[corte:]
    y_train, y_test = y[:corte], y[corte:]
    print(f"Walk-forward: train n={len(X_train)} (más antiguo) / test n={len(X_test)} (más reciente)")

    mean, std = X_train.mean(axis=0), X_train.std(axis=0)
    std[std == 0] = 1.0

    def estandarizar(M):
        return (M - mean) / std

    clf = LogisticRegression(C=1.0, max_iter=1000)  # penalty='l2' es el default
    clf.fit(estandarizar(X_train), y_train)
    p_test = clf.predict_proba(estandarizar(X_test))[:, 1]
    auc_test = roc_auc_score(y_test, p_test)
    print(f"AUC walk-forward (test, out-of-sample honesto): {auc_test:.3f}")

    # Modelo final para desplegar: reentrenado con el 100% del histórico
    # (todo pasado real -- no hay fuga hacia las predicciones forward que
    # generará shadow_predict.py de aquí en adelante, que es lo que
    # realmente hay que validar antes de proponer sustituir nada).
    mean_full, std_full = X.mean(axis=0), X.std(axis=0)
    std_full[std_full == 0] = 1.0
    clf_full = LogisticRegression(C=1.0, max_iter=1000)  # penalty='l2' es el default
    clf_full.fit((X - mean_full) / std_full, y)

    modelo = {
        "feature_order": FEATURES,
        "mean": mean_full.tolist(),
        "std": std_full.tolist(),
        "coef": clf_full.coef_[0].tolist(),
        "intercept": float(clf_full.intercept_[0]),
        "fecha_entrenamiento": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc).isoformat(timespec="seconds"),
        "n_train_final": n,
        "auc_walkforward_test": round(float(auc_test), 4),
        "n_walkforward_train": len(X_train),
        "n_walkforward_test": len(X_test),
    }
    MODELO_OUT.write_text(json.dumps(modelo, indent=2))
    print(f"Modelo guardado en {MODELO_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
