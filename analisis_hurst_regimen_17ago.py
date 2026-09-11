#!/usr/bin/env python3
"""
analisis_hurst_regimen_17ago.py — punto 5 de project_calibracion_vs_mercado_5puntos_17ago.

Prueba barata, shadow puro, SOLO LECTURA: exponente de Hurst (R/S) rodante
por activo, calculado sobre klines ya almacenados (data/prices/*.csv), y
cruzado contra results.csv para ver si el régimen (tendencial H>0.6 / paseo
aleatorio H~0.5 / reversión H<0.4) separa qué FAMILIA de estrategia (GBM_LATE
= paseo aleatorio con drift, STREAK_FADE = reversión, FAVORITO_CONFIRMADO =
consenso/momentum) rinde mejor.

Memoria origen: idea_hurst_exponent_regimen_mercado_15ago (Javi, 15-Ago,
pegó un post viral sobre Hurst/Nilo). Riesgo ya identificado ahí, sin
mencionar en el post: el estimador R/S es inestable en series CORTAS y
ruidosas (velas 1min en ventanas 5/15/60min) — este script verifica
ESTABILIDAD (split-half + ventana alternativa) ANTES de sacar ninguna
conclusión, no solo el resultado puntual. NO implementar ningún router de
régimen si el estimador no es estable.

No implementa nada operativo. Solo analiza y reporta.
"""
import glob
import json
import math
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).resolve().parent
PRICES_GLOB = str(DIR / "data" / "prices" / "2026-*.csv")
RESULTS_PATH = DIR / "data" / "shadow" / "results.csv"
OUT_PATH = DIR / "data" / "shadow" / "hurst_regimen_analisis.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
VENTANA_MIN_PRINCIPAL = 60   # minutos de klines por estimación de H
VENTANA_MIN_ALT = 30         # ventana alternativa para chequeo de estabilidad
PASO_MIN = 15                # recalcular H cada 15min (no cada minuto, barato)

# Familias representativas de cada supuesto de régimen (subtype con #15min
# como referencia común, ya que es el marco con más volumen en results.csv).
FAMILIAS_INTERES = {
    "GBM_LATE_15M": "paseo_aleatorio_con_drift",
    "GBM_LATE_15M_TARDIO": "paseo_aleatorio_con_drift",
    "GBM_LATE_15M_ESPACIO_ATR": "paseo_aleatorio_con_drift",
    "STREAK_FADE_15M": "reversion",
    "STREAK_FADE_5M": "reversion",
    "FAVORITO_CONFIRMADO": "consenso_momentum",
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION": "consenso_momentum",
}


def _hurst_rs(serie_log_ret: list[float]) -> float | None:
    """Estimador R/S clásico sobre una serie de log-retornos. Devuelve H o
    None si la serie es demasiado corta/plana para estimar con sentido."""
    n = len(serie_log_ret)
    if n < 20:
        return None
    media = sum(serie_log_ret) / n
    desv_acum = []
    acc = 0.0
    for r in serie_log_ret:
        acc += (r - media)
        desv_acum.append(acc)
    rango = max(desv_acum) - min(desv_acum)
    var = sum((r - media) ** 2 for r in serie_log_ret) / n
    s = math.sqrt(var)
    if s <= 0 or rango <= 0:
        return None
    rs = rango / s
    try:
        return math.log(rs) / math.log(n)
    except (ValueError, ZeroDivisionError):
        return None


def _cargar_klines() -> dict[str, list[tuple[float, float]]]:
    """{activo: [(ts_epoch, price), ...]} ordenado por tiempo, fuente
    consenso (misma columna que usa _cargar_spot en shadow_predict.py)."""
    import csv
    from datetime import datetime, timezone

    series = defaultdict(list)
    archivos = sorted(glob.glob(PRICES_GLOB))
    for fp in archivos:
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
    for activo in series:
        series[activo].sort(key=lambda x: x[0])
    return series


def _hurst_rodante(serie: list[tuple[float, float]], ventana_min: float) -> list[tuple[float, float]]:
    """[(ts, H), ...] recalculando cada PASO_MIN minutos con una ventana de
    ventana_min minutos de retornos 1min anteriores."""
    if not serie:
        return []
    ts0 = serie[0][0]
    ts_fin = serie[-1][0]
    idx_by_ts = serie
    out = []
    i_ventana_inicio = 0
    t = ts0 + ventana_min * 60
    # avance con doble puntero para O(n) total en vez de O(n*ventana)
    j = 0
    while t <= ts_fin:
        t_lo = t - ventana_min * 60
        while j < len(idx_by_ts) and idx_by_ts[j][0] < t_lo:
            j += 1
        i_ventana_inicio = j
        i_fin = i_ventana_inicio
        while i_fin < len(idx_by_ts) and idx_by_ts[i_fin][0] <= t:
            i_fin += 1
        sub = idx_by_ts[i_ventana_inicio:i_fin]
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


def _bucket_h(h: float) -> str:
    if h >= 0.58:
        return "alto_tendencial"
    if h <= 0.42:
        return "bajo_reversion"
    return "medio_paseo_aleatorio"


def _cargar_results_familias() -> list[dict]:
    import csv
    filas = []
    with open(RESULTS_PATH, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            fam = row.get("strategy")
            if fam not in FAMILIAS_INTERES:
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
                # prediction_timestamp puede venir como ISO en algunos casos
                try:
                    from datetime import datetime
                    ts = datetime.fromisoformat(row["prediction_timestamp"]).timestamp()
                except Exception:
                    continue
            acierto = row.get("acierto")
            pnl = row.get("pnl_neto")
            if acierto in (None, "") or pnl in (None, ""):
                continue
            try:
                filas.append({
                    "ts": ts, "activo": activo, "familia": fam,
                    "supuesto": FAMILIAS_INTERES[fam],
                    "acierto": int(float(acierto)), "pnl_neto": float(pnl),
                })
            except (ValueError, TypeError):
                continue
    return filas


def _lookup_h_mas_cercano(h_rodante: list[tuple[float, float]], ts: float, tol_s: float = 1800) -> float | None:
    if not h_rodante:
        return None
    # búsqueda binaria simple (h_rodante ordenado por ts)
    lo, hi = 0, len(h_rodante) - 1
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if h_rodante[mid][0] < ts:
            lo = mid + 1
        else:
            hi = mid - 1
    for idx in (hi, lo):
        if 0 <= idx < len(h_rodante) and abs(h_rodante[idx][0] - ts) <= tol_s:
            if best is None or abs(h_rodante[idx][0] - ts) < abs(best[0] - ts):
                best = h_rodante[idx]
    return best[1] if best else None


def _shuffle_test(grupo_bueno: list[float], grupo_resto: list[float], n_shuffle: int = 2000) -> float:
    """p-valor de permutación sobre la diferencia de medias (pnl_neto)."""
    import random
    obs = (sum(grupo_bueno) / len(grupo_bueno) if grupo_bueno else 0) - \
          (sum(grupo_resto) / len(grupo_resto) if grupo_resto else 0)
    todo = grupo_bueno + grupo_resto
    n_a = len(grupo_bueno)
    if n_a == 0 or len(grupo_resto) == 0:
        return 1.0
    cnt = 0
    rnd = random.Random(17)
    for _ in range(n_shuffle):
        rnd.shuffle(todo)
        a = todo[:n_a]
        b = todo[n_a:]
        diff = (sum(a) / len(a)) - (sum(b) / len(b))
        if abs(diff) >= abs(obs):
            cnt += 1
    return cnt / n_shuffle


def main():
    print("Cargando klines...")
    series = _cargar_klines()
    for activo in ACTIVOS:
        print(f"  {activo}: {len(series.get(activo, []))} puntos")

    print("Calculando Hurst rodante (ventana principal 60min)...")
    h_principal = {a: _hurst_rodante(series.get(a, []), VENTANA_MIN_PRINCIPAL) for a in ACTIVOS}
    print("Calculando Hurst rodante (ventana alternativa 30min, chequeo estabilidad)...")
    h_alt = {a: _hurst_rodante(series.get(a, []), VENTANA_MIN_ALT) for a in ACTIVOS}

    for a in ACTIVOS:
        print(f"  {a}: {len(h_principal[a])} estimaciones H(60min), {len(h_alt[a])} H(30min)")

    print("Cargando results.csv (familias de interés)...")
    filas = _cargar_results_familias()
    print(f"  {len(filas)} filas cruzables")

    # Cruce ventana principal
    cruzadas = []
    for f in filas:
        h = _lookup_h_mas_cercano(h_principal.get(f["activo"], []), f["ts"])
        h_alt_v = _lookup_h_mas_cercano(h_alt.get(f["activo"], []), f["ts"])
        if h is None:
            continue
        cruzadas.append({**f, "h": h, "h_bucket": _bucket_h(h),
                          "h_alt": h_alt_v, "h_alt_bucket": _bucket_h(h_alt_v) if h_alt_v is not None else None})

    print(f"  {len(cruzadas)} filas con H asignado (tolerancia 30min)")

    # Estabilidad del estimador: ¿coincide el bucket de H(60min) con H(30min)?
    con_ambos = [c for c in cruzadas if c["h_alt_bucket"] is not None]
    coincide = sum(1 for c in con_ambos if c["h_bucket"] == c["h_alt_bucket"])
    pct_estable = round(100 * coincide / len(con_ambos), 1) if con_ambos else None
    print(f"Estabilidad estimador: {pct_estable}% de coincidencia de bucket entre ventana 60min y 30min (n={len(con_ambos)})")

    # split-half temporal
    cruzadas_ts_sorted = sorted(cruzadas, key=lambda c: c["ts"])
    mitad = len(cruzadas_ts_sorted) // 2
    primera_mitad = cruzadas_ts_sorted[:mitad]
    segunda_mitad = cruzadas_ts_sorted[mitad:]

    def _resumen(subset, etiqueta):
        por_familia_bucket = defaultdict(list)
        for c in subset:
            por_familia_bucket[(c["familia"], c["h_bucket"])].append(c)
        out = {}
        for (fam, bucket), items in por_familia_bucket.items():
            n = len(items)
            if n < 8:
                continue
            hit = sum(c["acierto"] for c in items) / n
            pnl_medio = sum(c["pnl_neto"] for c in items) / n
            out[f"{fam}#{bucket}"] = {"n": n, "hit": round(hit, 3), "pnl_medio": round(pnl_medio, 4)}
        return out

    resumen_global = _resumen(cruzadas, "global")
    resumen_1a = _resumen(primera_mitad, "1a_mitad")
    resumen_2a = _resumen(segunda_mitad, "2a_mitad")

    # shuffle test por supuesto (no por familia individual, para tener n):
    # ¿el bucket "afín" al supuesto de la familia (reversion->bajo_reversion,
    # paseo_aleatorio_con_drift->medio_paseo_aleatorio, consenso_momentum->alto_tendencial)
    # gana significativamente más que el resto de buckets, dentro de esa familia?
    afin = {
        "reversion": "bajo_reversion",
        "paseo_aleatorio_con_drift": "medio_paseo_aleatorio",
        "consenso_momentum": "alto_tendencial",
    }
    shuffle_resultados = {}
    por_supuesto = defaultdict(list)
    for c in cruzadas:
        por_supuesto[c["supuesto"]].append(c)
    for supuesto, items in por_supuesto.items():
        bucket_afin = afin[supuesto]
        grupo_afin = [c["pnl_neto"] for c in items if c["h_bucket"] == bucket_afin]
        grupo_resto = [c["pnl_neto"] for c in items if c["h_bucket"] != bucket_afin]
        if len(grupo_afin) < 15 or len(grupo_resto) < 15:
            shuffle_resultados[supuesto] = {"n_afin": len(grupo_afin), "n_resto": len(grupo_resto), "motivo": "n insuficiente"}
            continue
        p = _shuffle_test(grupo_afin, grupo_resto)
        shuffle_resultados[supuesto] = {
            "bucket_afin": bucket_afin,
            "n_afin": len(grupo_afin), "pnl_medio_afin": round(sum(grupo_afin) / len(grupo_afin), 4),
            "n_resto": len(grupo_resto), "pnl_medio_resto": round(sum(grupo_resto) / len(grupo_resto), 4),
            "p_shuffle": round(p, 4),
        }

    out = {
        "generado_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(timespec="seconds"),
        "estabilidad_estimador_pct_coincidencia_60_vs_30min": pct_estable,
        "n_cruzadas_total": len(cruzadas),
        "resumen_global": resumen_global,
        "resumen_1a_mitad": resumen_1a,
        "resumen_2a_mitad": resumen_2a,
        "shuffle_por_supuesto_regimen": shuffle_resultados,
    }
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT_PATH}")
    print(json.dumps(shuffle_resultados, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
