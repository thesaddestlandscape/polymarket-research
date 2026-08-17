#!/usr/bin/env python3
"""
analisis_hurst_vs_fillability_p2_17ago.py — cruce obligatorio (petición
explícita Javi 17-Ago: "ya tenemos la solución a selección adversa, payout
asimétrico, profundidad de libro") del hallazgo de
idea_hurst_regimen_gbmlate_reversion_gana_17ago contra los 3 mecanismos YA
construidos para GBM_LATE, EN VEZ DE repetir un análisis de libro aislado
desde cero (feedback_gbm_soluciones_existentes_siempre_cruzar_17ago):

1. gate_calibracion.json — estado Platt por sub-familia (ya sabido: 15M
   base/ESPACIO_ATR mal_calibrado con Platt activo, TARDIO/MULTIHORIZONTE
   bien_calibrado). El hallazgo Hurst es idéntico en dirección en las 3
   sub-familias pese a estados de calibración distintos -> no es artefacto
   de calibración.
2. prob_fillable_gbm_late (P2, en producción desde 13-Ago) — ¿el bucket
   bajo_reversion (que gana más) tiene también mayor prob_fillable media?
   ¿Y la fill-ability REAL (libro_snapshots.csv, ratio_vs_stake máximo >=5,
   mismo target que entrenó P2) difiere por bucket de Hurst?
3. kelly_precio_gate.json — factor de corrección de sizing por (activo#marco,
   bucket de precio 0.10) para GBM_LATE_15M_FAMILIA, para ver si el efecto
   de Hurst es simplemente un proxy del precio de entrada (ya corregido).

Solo lectura, no toca producción.
"""
import csv
import glob
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DIR = Path(__file__).resolve().parent
PRICES_GLOB = str(DIR / "data" / "prices" / "2026-*.csv")
RESULTS_PATH = DIR / "data" / "shadow" / "results.csv"
SNAPSHOTS_PATH = DIR / "data" / "live" / "libro_snapshots.csv"
KELLY_PRECIO_GATE_PATH = DIR / "data" / "shadow" / "kelly_precio_gate.json"
OUT_PATH = DIR / "data" / "shadow" / "hurst_vs_fillability_p2_analisis.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
VENTANA_MIN = 60
PASO_MIN = 15
FAMILIAS = ("GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR")
RATIO_OBJETIVO = 5.0  # mismo umbral que P2/veto_profundidad


def _hurst_rs(rets):
    n = len(rets)
    if n < 20:
        return None
    media = sum(rets) / n
    acc = 0.0
    desv_acum = []
    for r in rets:
        acc += (r - media)
        desv_acum.append(acc)
    rango = max(desv_acum) - min(desv_acum)
    var = sum((r - media) ** 2 for r in rets) / n
    s = math.sqrt(var)
    if s <= 0 or rango <= 0:
        return None
    try:
        return math.log(rango / s) / math.log(n)
    except (ValueError, ZeroDivisionError):
        return None


def _cargar_klines():
    series = defaultdict(list)
    for fp in sorted(glob.glob(PRICES_GLOB)):
        if "chainlink" in fp:
            continue
        with open(fp, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                activo = row.get("asset")
                if activo not in ACTIVOS:
                    continue
                try:
                    ts = datetime.fromisoformat(row["timestamp_utc"]).timestamp()
                    price = float(row["price_usd"])
                except (ValueError, KeyError, TypeError):
                    continue
                if price > 0:
                    series[activo].append((ts, price))
    for a in series:
        series[a].sort(key=lambda x: x[0])
    return series


def _hurst_rodante(serie, ventana_min):
    if not serie:
        return []
    ts0, ts_fin = serie[0][0], serie[-1][0]
    out = []
    j = 0
    t = ts0 + ventana_min * 60
    while t <= ts_fin:
        t_lo = t - ventana_min * 60
        while j < len(serie) and serie[j][0] < t_lo:
            j += 1
        i_fin = j
        while i_fin < len(serie) and serie[i_fin][0] <= t:
            i_fin += 1
        sub = serie[j:i_fin]
        rets = []
        for k in range(1, len(sub)):
            p0, p1 = sub[k - 1][1], sub[k][1]
            if p0 > 0 and p1 > 0:
                rets.append(math.log(p1 / p0))
        h = _hurst_rs(rets)
        if h is not None:
            out.append((t, h))
        t += PASO_MIN * 60
    return out


def _bucket_h(h):
    if h >= 0.58:
        return "alto_tendencial"
    if h <= 0.42:
        return "bajo_reversion"
    return "medio_paseo_aleatorio"


def _lookup_h(h_rodante, ts, tol_s=1800):
    if not h_rodante:
        return None
    lo, hi = 0, len(h_rodante) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if h_rodante[mid][0] < ts:
            lo = mid + 1
        else:
            hi = mid - 1
    best = None
    for idx in (hi, lo):
        if 0 <= idx < len(h_rodante) and abs(h_rodante[idx][0] - ts) <= tol_s:
            if best is None or abs(h_rodante[idx][0] - ts) < abs(best[0] - ts):
                best = h_rodante[idx]
    return best[1] if best else None


def _fillable_por_senal():
    """(market_id, strategy, direction) -> ratio_vs_stake MÁXIMO visto."""
    out = {}
    with open(SNAPSHOTS_PATH, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("strategy") not in FAMILIAS:
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or "")
            except (ValueError, TypeError):
                continue
            key = (r["market_id"], r["strategy"], r["direction"])
            if key not in out or ratio > out[key]:
                out[key] = ratio
    return out


def _shuffle_test_medias(a, b, n_shuffle=2000):
    import random
    if len(a) < 5 or len(b) < 5:
        return None
    obs = (sum(a) / len(a)) - (sum(b) / len(b))
    todo = list(a) + list(b)
    na = len(a)
    rnd = random.Random(17)
    cnt = 0
    for _ in range(n_shuffle):
        rnd.shuffle(todo)
        aa, bb = todo[:na], todo[na:]
        diff = (sum(aa) / len(aa)) - (sum(bb) / len(bb))
        if abs(diff) >= abs(obs):
            cnt += 1
    return cnt / n_shuffle


def main():
    print("Cargando klines y Hurst rodante...")
    series = _cargar_klines()
    h_rodante = {a: _hurst_rodante(series.get(a, []), VENTANA_MIN) for a in ACTIVOS}

    print("Cargando kelly_precio_gate (referencia de bucket de precio)...")
    kpg = json.loads(KELLY_PRECIO_GATE_PATH.read_text(encoding="utf-8"))
    fam_kpg = kpg.get("familias", {}).get("GBM_LATE_15M_FAMILIA", {})

    print("Cargando fillability real (libro_snapshots.csv, colapsado por señal)...")
    fillable_map = _fillable_por_senal()
    print(f"  {len(fillable_map)} señales únicas GBM_LATE en libro_snapshots.csv")

    print("Cargando results.csv, prediction_timestamp + features (py_entrada, prob_fillable_gbm_late)...")
    filas = []
    with open(RESULTS_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") not in FAMILIAS:
                continue
            subtype = row.get("subtype", "")
            activo = subtype.split("#")[0] if "#" in subtype else None
            if activo not in ACTIVOS:
                continue
            try:
                ts = float(row.get("prediction_timestamp") or 0)
            except (ValueError, TypeError):
                ts = None
            if not ts:
                try:
                    ts = datetime.fromisoformat(row["prediction_timestamp"]).timestamp()
                except Exception:
                    continue
            try:
                feats = json.loads(row.get("features") or "{}")
            except Exception:
                feats = {}
            filas.append({
                "ts": ts, "activo": activo, "familia": row["strategy"],
                "market_id": row.get("market_id"), "direction": row.get("decision"),
                "py_entrada": feats.get("py_entrada"),
                "prob_fillable_gbm_late": feats.get("prob_fillable_gbm_late"),
            })
    print(f"  {len(filas)} filas GBM_LATE en results.csv")

    # asignar H + fillability real
    cruzadas = []
    for f in filas:
        h = _lookup_h(h_rodante.get(f["activo"], []), f["ts"])
        if h is None:
            continue
        key = (f["market_id"], f["familia"], f["direction"])
        ratio = fillable_map.get(key)
        fillable_real = (ratio >= RATIO_OBJETIVO) if ratio is not None else None
        cruzadas.append({**f, "h": h, "h_bucket": _bucket_h(h),
                          "ratio_vs_stake_max": ratio, "fillable_real": fillable_real})

    print(f"  {len(cruzadas)} filas con H asignado")

    # 1. prob_fillable_gbm_late medio por bucket H (solo post-13-Ago, donde existe la feature)
    con_p2 = [c for c in cruzadas if c["prob_fillable_gbm_late"] is not None]
    print(f"  {len(con_p2)} filas con prob_fillable_gbm_late logueado (post-13-Ago)")
    p2_por_bucket = defaultdict(list)
    for c in con_p2:
        p2_por_bucket[c["h_bucket"]].append(c["prob_fillable_gbm_late"])
    resumen_p2 = {b: {"n": len(v), "prob_fillable_medio": round(sum(v) / len(v), 4)}
                  for b, v in p2_por_bucket.items()}

    # 2. fillability REAL (libro_snapshots.csv) por bucket H
    con_real = [c for c in cruzadas if c["fillable_real"] is not None]
    print(f"  {len(con_real)} filas con fillability real (matched en libro_snapshots.csv)")
    real_por_bucket = defaultdict(list)
    for c in con_real:
        real_por_bucket[c["h_bucket"]].append(1 if c["fillable_real"] else 0)
    resumen_real = {b: {"n": len(v), "fillable_rate": round(sum(v) / len(v), 4)}
                     for b, v in real_por_bucket.items()}

    # shuffle test: fillable_rate bajo_reversion vs medio_paseo_aleatorio
    a = real_por_bucket.get("bajo_reversion", [])
    b = real_por_bucket.get("medio_paseo_aleatorio", [])
    p_shuffle_fillable = _shuffle_test_medias(a, b)

    # 3. PnL real SOLO del subconjunto fillable (ratio>=5), por bucket H —
    # el test decisivo: ¿el edge de bajo_reversion sobrevive tras filtrar
    # por profundidad real, o es el mismo espejismo arquetipo A de siempre?
    outcomes = {}
    with open(RESULTS_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") not in FAMILIAS:
                continue
            key = (row.get("market_id"), row.get("strategy"), row.get("decision"))
            try:
                outcomes[key] = (int(row["acierto"]), float(row["pnl_neto"]))
            except (ValueError, KeyError):
                continue

    fillable_pnl_por_bucket = defaultdict(list)
    for c in con_real:
        if not c["fillable_real"]:
            continue
        key = (c["market_id"], c["familia"], c["direction"])
        out = outcomes.get(key)
        if out:
            fillable_pnl_por_bucket[c["h_bucket"]].append(out[1])

    resumen_fillable_pnl = {b: {"n": len(v), "pnl_medio": round(sum(v) / len(v), 4) if v else None}
                              for b, v in fillable_pnl_por_bucket.items()}

    # 4. py_entrada medio por bucket H — ¿el efecto es proxy de precio (ya
    # corregido por kelly_precio_gate)?
    py_por_bucket = defaultdict(list)
    for c in cruzadas:
        if c["py_entrada"] is not None:
            py_por_bucket[c["h_bucket"]].append(c["py_entrada"])
    resumen_py = {b: {"n": len(v), "py_medio": round(sum(v) / len(v), 4)}
                  for b, v in py_por_bucket.items()}

    out = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "1_gate_calibracion_ya_conocido": {
            "GBM_LATE_15M": "mal_calibrado_confirmado, Platt activo",
            "GBM_LATE_15M_ESPACIO_ATR": "mal_calibrado_confirmado, Platt activo",
            "GBM_LATE_15M_TARDIO": "bien_calibrado_confirmado, Platt no aplica",
            "conclusion": "el patron H bajo>H medio aparece en las 3 pese a "
                          "estados de calibracion distintos -> no es artefacto Platt",
        },
        "2_prob_fillable_gbm_late_P2_por_bucket_h": resumen_p2,
        "3_fillability_real_libro_snapshots_por_bucket_h": resumen_real,
        "p_shuffle_fillable_rate_bajo_vs_medio": p_shuffle_fillable,
        "4_pnl_SOLO_subconjunto_fillable_real_por_bucket_h": resumen_fillable_pnl,
        "5_py_entrada_medio_por_bucket_h_kelly_precio_gate_check": resumen_py,
    }
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT_PATH}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
