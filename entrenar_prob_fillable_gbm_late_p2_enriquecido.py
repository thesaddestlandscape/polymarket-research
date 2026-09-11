#!/usr/bin/env python3
"""P2 enriquecido (18-Ago, idea_p2_enriquecido_momentum_liquidaciones_18ago):
extiende el P2 original (entrenar_prob_fillable_gbm_late_p2.py, AUC=0.669
en su población, 5 features) con 2 features nuevas -- momentum_reciente_2min
(magnitud del cambio de precio Chainlink en los 2min previos a la señal) y
usd_liquidado_3min (log1p del USD liquidado en Bybit en los 3min previos,
mismo activo) -- validadas el 18-Ago con walk-forward honesto sobre la
ventana 14-17 Ago (única con ambas fuentes disponibles): AUC 0.5952 ->
0.6227 (+0.0275), momentum_2min el coeficiente más fuerte de los 7.

Objetivo: producir el modelo final (reentrenado con el 100% del histórico
disponible) para desplegar como logging puro en gbm_late_15min_executor.py
-- PURAMENTE INFORMATIVO, nunca decide si se dispara la señal ni cambia
prob_yes/edge/stake. Mismo criterio de barrera que P2 original/P17: forward
logging primero, cualquier uso operativo requiere aprobación explícita de
Javi + /code-review sobre el camino de decisión real.

Target: `fillable` = ratio_vs_stake>=5 en data/live/libro_snapshots.csv,
igual que P2 original. Solo lectura de libro_snapshots.csv/results.csv/
data/prices/chainlink_*.csv/data/shadow/liquidaciones_bybit_eventos_*.csv,
solo escritura de data/shadow/prob_fillable_gbm_late_enriquecido_model.json.

Uso: python3 entrenar_prob_fillable_gbm_late_p2_enriquecido.py
(requiere sklearn -- disponible en el python3 del sistema, no en .venv)
"""
import bisect
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
PRICES_DIR = DIR / "data/prices"
BYBIT_DIR = DIR / "data/shadow"
MODELO_OUT = DIR / "data/shadow/prob_fillable_gbm_late_enriquecido_model.json"

RATIO_OBJETIVO = 5.0
MOMENTUM_VENTANA_S = 120.0
LIQ_VENTANA_S = 180.0
FEATURE_ORDER = ["libro_spread", "libro_liquidez", "dist_050", "hora_sin", "hora_cos",
                  "momentum_reciente_2min", "log_usd_liquidado_3min"]


def _parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _dias_disponibles():
    """Días con AMBAS fuentes (chainlink + liquidaciones bybit) en disco --
    la intersección real, no asumida."""
    dias_chainlink = {p.stem.replace("chainlink_", "") for p in PRICES_DIR.glob("chainlink_*.csv")}
    dias_bybit = {p.stem.replace("liquidaciones_bybit_eventos_", "")
                  for p in BYBIT_DIR.glob("liquidaciones_bybit_eventos_*.csv")}
    return sorted(dias_chainlink & dias_bybit)


def cargar_chainlink_por_activo(dias):
    por_activo = {}
    for dia in dias:
        path = PRICES_DIR / f"chainlink_{dia}.csv"
        with open(path, newline="", encoding="utf-8") as f:
            next(f, None)
            for linea in f:
                partes = linea.rstrip("\n").split(",")
                if len(partes) < 3:
                    continue
                try:
                    ts = _parse_ts(partes[0])
                    activo = partes[1]
                    precio = float(partes[2])
                except (ValueError, IndexError):
                    continue
                if precio <= 0:
                    continue
                por_activo.setdefault(activo, []).append((ts, precio))
    for a in por_activo:
        por_activo[a].sort()
    return por_activo


def momentum_en(por_activo, activo, ts_epoch, ventana_s=MOMENTUM_VENTANA_S):
    serie = por_activo.get(activo)
    if not serie:
        return None
    tss = [t for t, _ in serie]
    idx = bisect.bisect_right(tss, ts_epoch) - 1
    if idx < 0:
        return None
    t_now, p_now = serie[idx]
    if ts_epoch - t_now > 30:
        return None
    idx_prev = bisect.bisect_left(tss, t_now - ventana_s)
    if idx_prev >= len(serie) or idx_prev < 0:
        return None
    t_prev, p_prev = serie[idx_prev]
    if t_now - t_prev < ventana_s * 0.5 or p_prev <= 0:
        return None
    return abs((p_now - p_prev) / p_prev) * 100.0


def cargar_bybit_por_activo(dias):
    por_activo = {}
    for dia in dias:
        path = BYBIT_DIR / f"liquidaciones_bybit_eventos_{dia}.csv"
        if not path.exists():
            continue
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                try:
                    ts = _parse_ts(r["timestamp_utc"])
                    usd = float(r["usd"])
                    activo = r["activo"]
                except (ValueError, KeyError):
                    continue
                por_activo.setdefault(activo, []).append((ts, usd))
    for a in por_activo:
        por_activo[a].sort()
    return por_activo


def usd_liquidado_en(por_activo, activo, ts_epoch, ventana_s=LIQ_VENTANA_S):
    serie = por_activo.get(activo)
    if not serie:
        return 0.0
    tss = [t for t, _ in serie]
    lo = bisect.bisect_left(tss, ts_epoch - ventana_s)
    hi = bisect.bisect_right(tss, ts_epoch)
    return sum(usd for _, usd in serie[lo:hi])


def _cargar_fillable_por_senal():
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


def cargar_dataset(dias, por_activo_price, por_activo_liq):
    fillable_por_senal = _cargar_fillable_por_senal()
    dia_min, dia_max = dias[0] + "T00:00:00", dias[-1] + "T23:59:59"
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            strategy = r.get("strategy") or ""
            if not strategy.startswith(("GBM_LATE_15M", "GBM_LATE_5M")):
                continue
            ts_str = r.get("prediction_timestamp", "")
            if not (dia_min <= ts_str <= dia_max):
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
            subtype = r.get("subtype", "")
            activo = subtype.split("#")[0] if "#" in subtype else None
            if not activo:
                continue
            try:
                ts_epoch = _parse_ts(ts_str)
            except ValueError:
                continue
            mom = momentum_en(por_activo_price, activo, ts_epoch)
            if mom is None:
                continue
            liq = usd_liquidado_en(por_activo_liq, activo, ts_epoch)
            dist_050 = abs(float(py) - 0.5)
            hora_sin = math.sin(2 * math.pi * float(hora_utc) / 24)
            hora_cos = math.cos(2 * math.pi * float(hora_utc) / 24)
            filas.append({
                "ts": ts_str,
                "x": [float(libro_spread), float(libro_liquidez), dist_050, hora_sin, hora_cos,
                      mom, math.log1p(liq)],
                "y": int(ratio >= RATIO_OBJETIVO),
            })
    filas.sort(key=lambda r: r["ts"])
    return filas


def main():
    dias = _dias_disponibles()
    print(f"Días con chainlink+bybit disponibles: {dias}")
    if len(dias) < 2:
        print("Ventana insuficiente -- abortando.")
        return 1
    por_activo_price = cargar_chainlink_por_activo(dias)
    por_activo_liq = cargar_bybit_por_activo(dias)

    filas = cargar_dataset(dias, por_activo_price, por_activo_liq)
    n = len(filas)
    print(f"Dataset GBM_LATE_15M*/GBM_LATE_5M con features enriquecidas: n={n}")
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
        "dias_entrenamiento": dias,
        "fillable_rate": round(float(y.mean()), 4),
        "auc_walkforward_test": round(float(auc_test), 4),
        "n_walkforward_train": len(X_train),
        "n_walkforward_test": len(X_test),
        "momentum_ventana_s": MOMENTUM_VENTANA_S,
        "liq_ventana_s": LIQ_VENTANA_S,
    }
    MODELO_OUT.write_text(json.dumps(modelo, indent=2))
    print(f"Modelo guardado en {MODELO_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
