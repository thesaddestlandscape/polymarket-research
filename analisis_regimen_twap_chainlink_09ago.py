#!/usr/bin/env python3
"""analisis_regimen_twap_chainlink_09ago.py -- ¿cambió de verdad la
resolución de los mercados Chainlink (5min/15min) el 07-Ago (TWAP) vs
antes (snapshot)?

Origen (09-Ago, aviso externo de Javi, verificado contra la API real):
el mercado BTC 5min activo ahora mismo resuelve por
"TWAP de Bitcoin generado por Chainlink" (resolutionSource apunta a
btc-usd-twap-30s-streams para 5min, twap-60s-streams para 15min) --
CONFIRMADO también que los mercados de 60min/weekly resuelven distinto:
vela 1h de BINANCE (open/close), NO Chainlink, NO afectados por este
cambio (verificado BTC y SOL#60min vía gamma-api).

No tenemos acceso al stream TWAP real de Chainlink (Data Streams es de
pago, la página pública de data.chain.link está detrás de un challenge
Vercel). Aproximamos el TWAP nosotros mismos con los ticks brutos que YA
capturamos en data/prices/chainlink_YYYY-MM-DD.csv (topic
crypto_prices_chainlink, ~1 tick/s por activo) -- promedio ponderado por
tiempo de los ticks dentro de la ventana [end-w, end], w=30s (5min) /
60s (15min). Comparamos esa aproximación contra el snapshot puro (último
tick antes de end) para medir cuánto habría cambiado el resultado bajo
el mecanismo viejo -- y contra outcome_real (ya oficial, vía API) para
validar que la aproximación TWAP es fiel después del 07-Ago.

Puramente análisis, solo lectura, no toca ningún dato ni decisión.
"""
import csv
import gzip
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
PRICES_DIR = REPO / "data" / "prices"

VENTANA_TWAP_S = {"5min": 30, "15min": 60}
FECHA_CAMBIO = datetime(2026, 8, 7, tzinfo=timezone.utc)


def _parse_dt(s):
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def _abrir_precios(fecha_str):
    plano = PRICES_DIR / f"chainlink_{fecha_str}.csv"
    gz = PRICES_DIR / f"chainlink_{fecha_str}.csv.gz"
    if plano.exists():
        return open(plano, "r", newline="", encoding="utf-8")
    if gz.exists():
        return gzip.open(gz, "rt", newline="", encoding="utf-8")
    return None


def _cargar_ticks_dia(fecha_str):
    """asset -> (lista timestamps epoch ordenada, lista precios paralela)"""
    f = _abrir_precios(fecha_str)
    if f is None:
        return {}
    ts_por_activo = defaultdict(list)
    px_por_activo = defaultdict(list)
    with f:
        r = csv.DictReader(f)
        for row in r:
            try:
                dt = datetime.fromisoformat(row["timestamp_utc"])
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                ts_por_activo[row["asset"]].append(dt.timestamp())
                px_por_activo[row["asset"]].append(float(row["price_usd"]))
            except (ValueError, KeyError):
                continue
    return {a: (ts_por_activo[a], px_por_activo[a]) for a in ts_por_activo}


def _twap_y_snapshot(ts_list, px_list, start_epoch, end_epoch, ventana_s):
    """Devuelve (proxy_twap, proxy_snapshot, referencia) o (None,None,None)
    si no hay ticks suficientes."""
    if not ts_list:
        return None, None, None
    # referencia: primer tick >= start_epoch (aprox precio al inicio del rango)
    i0 = bisect_left(ts_list, start_epoch)
    if i0 >= len(ts_list):
        return None, None, None
    referencia = px_list[i0]

    # snapshot: último tick <= end_epoch
    j = bisect_right(ts_list, end_epoch) - 1
    if j < 0:
        return None, None, None
    proxy_snapshot = px_list[j]

    # twap: media ponderada por tiempo de los ticks en [end-ventana, end]
    lo = end_epoch - ventana_s
    k0 = bisect_left(ts_list, lo)
    k1 = bisect_right(ts_list, end_epoch)
    if k1 - k0 < 2:
        return None, proxy_snapshot, referencia
    ts_v = ts_list[k0:k1]
    px_v = px_list[k0:k1]
    acumulado = 0.0
    peso_total = 0.0
    for idx in range(len(ts_v) - 1):
        dt_peso = ts_v[idx + 1] - ts_v[idx]
        acumulado += px_v[idx] * dt_peso
        peso_total += dt_peso
    if peso_total <= 0:
        return None, proxy_snapshot, referencia
    proxy_twap = acumulado / peso_total
    return proxy_twap, proxy_snapshot, referencia


def main():
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            subtype = row["subtype"]
            dur = None
            for d in ("15min", "5min"):
                if subtype.endswith(d):
                    dur = d
                    break
            if dur is None:
                continue
            end_dt = _parse_dt(row["end_date"])
            res_dt = _parse_dt(row["resolution_timestamp"])
            if end_dt is None or res_dt is None:
                continue
            if res_dt < datetime(2026, 8, 1, tzinfo=timezone.utc):
                continue  # solo ventana reciente: 1-Ago en adelante
            asset = subtype.split("#")[0]
            filas.append((res_dt, end_dt, asset, dur, row["outcome_real"], row["market_id"]))

    print(f"[analisis_regimen_twap] {len(filas)} resoluciones 5min/15min desde 01-Ago candidatas")

    por_dia = defaultdict(list)
    for f_ in filas:
        fecha_str = f_[1].strftime("%Y-%m-%d")
        por_dia[fecha_str].append(f_)

    resultados = []
    for fecha_str in sorted(por_dia.keys()):
        ticks = _cargar_ticks_dia(fecha_str)
        if not ticks:
            print(f"[analisis_regimen_twap] SIN ticks chainlink para {fecha_str}, saltado ({len(por_dia[fecha_str])} filas perdidas)")
            continue
        for res_dt, end_dt, asset, dur, outcome_real, market_id in por_dia[fecha_str]:
            par = ticks.get(asset)
            if par is None:
                continue
            ts_list, px_list = par
            ventana_s = VENTANA_TWAP_S[dur]
            start_epoch = (end_dt - timedelta(minutes=int(dur.replace("min", "")))).timestamp()
            end_epoch = end_dt.timestamp()
            twap, snap, ref = _twap_y_snapshot(ts_list, px_list, start_epoch, end_epoch, ventana_s)
            if twap is None or snap is None or ref is None:
                continue
            dir_twap = "YES" if twap >= ref else "NO"
            dir_snap = "YES" if snap >= ref else "NO"
            resultados.append({
                "fecha": fecha_str, "res_dt": res_dt, "asset": asset, "dur": dur,
                "outcome_real": outcome_real, "dir_twap": dir_twap, "dir_snap": dir_snap,
                "flip": dir_twap != dir_snap,
            })

    print(f"[analisis_regimen_twap] {len(resultados)} filas con ticks suficientes para aproximar\n")

    pre = [r for r in resultados if r["res_dt"] < FECHA_CAMBIO]
    post = [r for r in resultados if r["res_dt"] >= FECHA_CAMBIO]

    def _resumen(nombre, subset):
        if not subset:
            print(f"  {nombre}: sin datos")
            return
        n = len(subset)
        acc_twap = sum(1 for r in subset if r["dir_twap"] == r["outcome_real"]) / n
        acc_snap = sum(1 for r in subset if r["dir_snap"] == r["outcome_real"]) / n
        flip_rate = sum(1 for r in subset if r["flip"]) / n
        print(f"  {nombre}: n={n} | acc_proxy_TWAP_vs_outcome_real={acc_twap:.1%} | "
              f"acc_proxy_SNAPSHOT_vs_outcome_real={acc_snap:.1%} | flip_rate(TWAP!=snapshot)={flip_rate:.1%}")

    print("=== ANTES del 07-Ago (mecanismo viejo, se asume snapshot) ===")
    _resumen("TOTAL", pre)
    for dur in ("5min", "15min"):
        _resumen(f"  {dur}", [r for r in pre if r["dur"] == dur])

    print("\n=== DESDE el 07-Ago (mecanismo nuevo, TWAP) ===")
    _resumen("TOTAL", post)
    for dur in ("5min", "15min"):
        _resumen(f"  {dur}", [r for r in post if r["dur"] == dur])

    print("\n=== Por activo, DESDE el 07-Ago ===")
    activos = sorted(set(r["asset"] for r in post))
    for a in activos:
        _resumen(f"  {a}", [r for r in post if r["asset"] == a])

    return 0


if __name__ == "__main__":
    sys.exit(main())
