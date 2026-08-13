#!/usr/bin/env python3
"""P2 del plan de profundidad de libro (13-Ago, petición Javi "adelante,
constrúyelo" tras validar con walk-forward que hay señal real): clasificador
de fill-ability EX-ANTE (antes de disparar la señal) para la familia
GBM_LATE_15M/5M completa, usando solo features ya logueadas sin coste extra
(libro_spread, libro_liquidez de `_libro_calidad()`, distancia del precio a
0.50, hora del día seno/coseno).

Validación previa (walk-forward 70/30, n=27.111, sesión 13-Ago): AUC=0.671
para GBM_LATE* (toda la familia) — mismo orden de magnitud que P17
(meta_score_gbm_late, AUC=0.683, ya en producción). El coeficiente
dominante con diferencia es la distancia a 0.50: confirma con n=27k (no
n=18 como el hallazgo aislado de XRP) que la profundidad del libro se
concentra donde el precio está más indeciso — coherente con el mecanismo
ya documentado (idea_gbmlate15m_espacioatr_xrp_arquetipo_a_confirmado_12ago):
el libro tiene fondo antes de que nadie tome partido, se vacía justo
cuando el precio se confirma.

Target: `fillable` = ratio_vs_stake>=5 en data/live/libro_snapshots.csv
(el mismo umbral "ejecutable" que usa live_trade.py/analisis_fills.py en
todo el proyecto), colapsado por (market_id,strategy,direction) tomando el
ratio MÁXIMO visto entre reintentos. NO es lo mismo que `acierto` (P17) --
aquí predecimos si el libro va a tener profundidad, no si la predicción
direccional va a acertar. Son dos preguntas distintas y complementarias:
P17 dice si el modelo tiene razón, esto dice si vamos a poder ejecutarlo.

PURAMENTE INFORMATIVO -- se loguea como feature `prob_fillable_gbm_late`,
NUNCA decide si se dispara la señal ni cambia prob_yes/edge/stake. Mismo
criterio de barrera que P17: forward logging primero, cualquier uso
operativo (filtrar candidatos, priorizar el fade cuando la señal tiene
alta prob_fillable) requiere aprobación explícita de Javi + `/code-review`
si toca el camino de decisión real.

Solo lectura de libro_snapshots.csv/results.csv, solo escritura de
data/shadow/prob_fillable_gbm_late_model.json. No toca config_live.json,
pares_permitidos_live ni ningún gate de dinero real.

Uso: python3 entrenar_prob_fillable_gbm_late_p2.py
(requiere sklearn -- disponible en el python3 del sistema, no en .venv)
"""
import csv
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
RESULTS = DIR / "data/shadow/results.csv"
MODELO_OUT = DIR / "data/shadow/prob_fillable_gbm_late_model.json"

RATIO_OBJETIVO = 5.0  # mismo umbral "fillable" que gbmlate_fade_depth_fase0.py/veto_profundidad
FEATURE_ORDER = ["libro_spread", "libro_liquidez", "dist_050", "hora_sin", "hora_cos"]


def _cargar_fillable_por_senal():
    """(market_id, strategy, direction) -> ratio_vs_stake MÁXIMO visto entre
    reintentos (mismo criterio 'mejor oportunidad que tuvo' que el resto de
    la familia *_fade_depth_fase0.py)."""
    mejor = {}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                ratio = float(r.get("ratio_vs_stake") or "")
            except (TypeError, ValueError):
                continue
            key = (r["market_id"], r["strategy"], r["direction"])
            if key not in mejor or ratio > mejor[key]:
                mejor[key] = ratio
    return mejor


def cargar_dataset():
    fillable_por_senal = _cargar_fillable_por_senal()
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            strategy = r.get("strategy") or ""
            if not strategy.startswith(("GBM_LATE_15M", "GBM_LATE_5M")):
                continue
            key = (r["market_id"], strategy, r.get("decision"))
            ratio = fillable_por_senal.get(key)
            if ratio is None:
                continue
            try:
                feats = json.loads(r["features"])
            except Exception:
                continue
            libro_spread = feats.get("libro_spread")
            libro_liquidez = feats.get("libro_liquidez")
            py = feats.get("py_entrada")
            hora_utc = feats.get("hora_utc")
            if any(v is None for v in (libro_spread, libro_liquidez, py, hora_utc)):
                continue
            dist_050 = abs(float(py) - 0.5)
            hora_sin = math.sin(2 * math.pi * float(hora_utc) / 24)
            hora_cos = math.cos(2 * math.pi * float(hora_utc) / 24)
            filas.append({
                "ts": r.get("prediction_timestamp", ""),
                "x": [float(libro_spread), float(libro_liquidez), dist_050, hora_sin, hora_cos],
                "y": int(ratio >= RATIO_OBJETIVO),
            })
    # de-duplicar por (market_id,strategy,decision): results.csv puede tener
    # varias filas si la señal se reevaluó en ciclos sucesivos -- solo la
    # primera vista de cada clave está sincronizada con la primera fila real
    # de libro_snapshots.csv, así que ordenar por ts y quedarnos con todas es
    # correcto igualmente (cada fila de results.csv es una resolución real
    # distinta, no un duplicado de la señal).
    filas.sort(key=lambda r: r["ts"])
    return filas


def main():
    filas = cargar_dataset()
    n = len(filas)
    print(f"Dataset GBM_LATE_15M*/GBM_LATE_5M con features+fillability cruzadas: n={n}")
    if n < 200:
        print("n insuficiente para entrenar con confianza -- abortando.")
        return 1

    X = np.array([r["x"] for r in filas])
    y = np.array([r["y"] for r in filas])
    print(f"fillable_rate={y.mean():.1%}")

    corte = int(n * 0.7)
    X_train, X_test = X[:corte], X[corte:]
    y_train, y_test = y[:corte], y[corte:]
    print(f"Walk-forward: train n={len(X_train)} (más antiguo) / test n={len(X_test)} (más reciente)")

    mean, std = X_train.mean(axis=0), X_train.std(axis=0)
    std[std == 0] = 1.0

    def estandarizar(M):
        return (M - mean) / std

    clf = LogisticRegression(C=1.0, max_iter=1000)
    clf.fit(estandarizar(X_train), y_train)
    p_test = clf.predict_proba(estandarizar(X_test))[:, 1]
    auc_test = roc_auc_score(y_test, p_test)
    print(f"AUC walk-forward (test, out-of-sample honesto): {auc_test:.3f}")
    print("coef (estandarizados):", dict(zip(FEATURE_ORDER, clf.coef_[0].round(3))))

    # Modelo final para desplegar: reentrenado con el 100% del histórico.
    mean_full, std_full = X.mean(axis=0), X.std(axis=0)
    std_full[std_full == 0] = 1.0
    clf_full = LogisticRegression(C=1.0, max_iter=1000)
    clf_full.fit((X - mean_full) / std_full, y)

    modelo = {
        "feature_order": FEATURE_ORDER,
        "mean": mean_full.tolist(),
        "std": std_full.tolist(),
        "coef": clf_full.coef_[0].tolist(),
        "intercept": float(clf_full.intercept_[0]),
        "fecha_entrenamiento": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_train_final": n,
        "fillable_rate": round(float(y.mean()), 4),
        "auc_walkforward_test": round(float(auc_test), 4),
        "n_walkforward_train": len(X_train),
        "n_walkforward_test": len(X_test),
    }
    MODELO_OUT.write_text(json.dumps(modelo, indent=2))
    print(f"Modelo guardado en {MODELO_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
