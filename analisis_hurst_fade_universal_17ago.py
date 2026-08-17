#!/usr/bin/env python3
"""
analisis_hurst_fade_universal_17ago.py — segundo cruce obligatorio pedido
por Javi ("ya tenemos la solución a la profundidad de libro, revisa bien,
no des nada por cerrado sin revisar todo lo que hemos avanzado"): la
solución REAL al problema de profundidad de libro para la familia GBM_LATE
no es solo P2 (clasificador de fillability del lado propio) — es el
mecanismo de FADE (`fade_depth_universal_fase0.py`, generalización 14-Ago
de `gbmlate_fade_depth_fase0.py`): cuando el lado propio se vacía por
flujo informado, el lado CONTRARIO puede tener profundidad y ser el que
realmente se pueda cobrar.

El fade agregado de GBM_LATE ya se cerró refutado el 16-Ago
(idea_gbmlate_fade_refutado_datos_frescos_16ago: BTC/ETH/SOL coinflip+fee
negativo). Este script repite ESE MISMO gate pero segmentado por régimen
de Hurst (bajo_reversion/medio_paseo_aleatorio/alto_tendencial) sobre los
datos ya acumulados en fade_depth_universal_fase0.csv (11508 filas,
creciendo desde 14-Ago) -- por si el régimen rescata un subconjunto que el
agregado no mostraba, antes de dar el hallazgo de Hurst por cerrado del
todo.

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
FADE_PATH = DIR / "data" / "shadow" / "fade_depth_universal_fase0.csv"
OUT_PATH = DIR / "data" / "shadow" / "hurst_fade_universal_analisis.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
VENTANA_MIN = 60
PASO_MIN = 15
FAMILIAS = ("GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR")
RATIO_OBJETIVO = 5.0
FEE = 0.07


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


def _shuffle_test_binaria(hits_a, n_a, hits_b, n_b, n_shuffle=3000):
    """p-valor de permutación sobre diferencia de tasas de acierto."""
    import random
    if n_a < 5 or n_b < 5:
        return None
    obs = (hits_a / n_a) - (hits_b / n_b)
    pool = [1] * hits_a + [0] * (n_a - hits_a) + [1] * hits_b + [0] * (n_b - hits_b)
    rnd = random.Random(17)
    cnt = 0
    for _ in range(n_shuffle):
        rnd.shuffle(pool)
        aa = pool[:n_a]
        bb = pool[n_a:]
        diff = (sum(aa) / n_a) - (sum(bb) / n_b)
        if abs(diff) >= abs(obs):
            cnt += 1
    return cnt / n_shuffle


def main():
    print("Cargando klines y Hurst rodante...")
    series = _cargar_klines()
    h_rodante = {a: _hurst_rodante(series.get(a, []), VENTANA_MIN) for a in ACTIVOS}

    print("Cargando outcomes reales (results.csv)...")
    outcomes = {}
    with open(RESULTS_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") not in FAMILIAS:
                continue
            key = (row.get("market_id"), row.get("strategy"), row.get("decision"))
            try:
                outcomes[key] = int(row["acierto"])
            except (ValueError, KeyError, TypeError):
                continue
    print(f"  {len(outcomes)} outcomes GBM_LATE")

    print("Cargando fade_depth_universal_fase0.csv (eventos con lado original fillable)...")
    eventos = []
    with open(FADE_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") not in FAMILIAS:
                continue
            subtype = row.get("subtype", "")
            activo = subtype.split("#")[0] if "#" in subtype else None
            if activo not in ACTIVOS:
                continue
            try:
                ts = datetime.fromisoformat(row["evento_timestamp_utc"]).timestamp()
                ratio_contrario_max = float(row.get("ratio_contrario_max") or 0.0)
                precio_contrario = float(row.get("precio_contrario") or 0.0)
            except (ValueError, KeyError, TypeError):
                continue
            eventos.append({
                "ts": ts, "activo": activo, "familia": row["strategy"],
                "market_id": row.get("market_id"), "direction_original": row.get("direction"),
                "ratio_contrario_max": ratio_contrario_max,
                "precio_contrario": precio_contrario,
            })
    print(f"  {len(eventos)} eventos GBM_LATE en fade_depth_universal_fase0.csv")

    # asignar H, fade_fillable, outcome del fade
    cruzados = []
    for e in eventos:
        h = _lookup_h(h_rodante.get(e["activo"], []), e["ts"])
        if h is None:
            continue
        key = (e["market_id"], e["familia"], e["direction_original"])
        acierto_original = outcomes.get(key)
        if acierto_original is None:
            continue
        fade_fillable = e["ratio_contrario_max"] >= RATIO_OBJETIVO
        acierto_fade = 1 - acierto_original  # binario: si el original pierde, el fade gana
        pnl_fade = None
        if e["precio_contrario"] > 0:
            if acierto_fade:
                gross_win = (1 - e["precio_contrario"]) / e["precio_contrario"]
                pnl_fade = gross_win * (1 - FEE)
            else:
                pnl_fade = -1.0
        cruzados.append({**e, "h": h, "h_bucket": _bucket_h(h),
                          "fade_fillable": fade_fillable, "acierto_fade": acierto_fade,
                          "pnl_fade": pnl_fade})

    print(f"  {len(cruzados)} eventos con H + outcome cruzados")

    con_fillable = [c for c in cruzados if c["fade_fillable"]]
    print(f"  {len(con_fillable)} con fade REALMENTE fillable (ratio_contrario_max>=5)")

    por_bucket = defaultdict(list)
    for c in con_fillable:
        por_bucket[c["h_bucket"]].append(c)

    resumen = {}
    for bucket, items in por_bucket.items():
        n = len(items)
        hits = sum(c["acierto_fade"] for c in items)
        pnls = [c["pnl_fade"] for c in items if c["pnl_fade"] is not None]
        resumen[bucket] = {
            "n": n, "hit_fade": round(hits / n, 4) if n else None,
            "pnl_fade_medio": round(sum(pnls) / len(pnls), 4) if pnls else None,
        }

    # shuffle test bajo_reversion vs medio_paseo_aleatorio (hit rate)
    a = por_bucket.get("bajo_reversion", [])
    b = por_bucket.get("medio_paseo_aleatorio", [])
    p_shuffle = None
    if len(a) >= 5 and len(b) >= 5:
        hits_a = sum(c["acierto_fade"] for c in a)
        hits_b = sum(c["acierto_fade"] for c in b)
        p_shuffle = _shuffle_test_binaria(hits_a, len(a), hits_b, len(b))

    # split-half temporal dentro de bajo_reversion (si tiene volumen) para
    # verificar estabilidad antes de creer nada
    a_sorted = sorted(a, key=lambda c: c["ts"])
    mitad = len(a_sorted) // 2
    split_half_bajo = None
    if mitad >= 5:
        m1, m2 = a_sorted[:mitad], a_sorted[mitad:]
        split_half_bajo = {
            "1a_mitad": {"n": len(m1), "hit_fade": round(sum(c["acierto_fade"] for c in m1) / len(m1), 4)},
            "2a_mitad": {"n": len(m2), "hit_fade": round(sum(c["acierto_fade"] for c in m2) / len(m2), 4)},
        }

    out = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_eventos_totales_gbm_late": len(cruzados),
        "n_fade_fillable": len(con_fillable),
        "resumen_fade_fillable_por_bucket_h": resumen,
        "p_shuffle_hit_fade_bajo_vs_medio": p_shuffle,
        "split_half_bajo_reversion": split_half_bajo,
    }
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT_PATH}")
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
