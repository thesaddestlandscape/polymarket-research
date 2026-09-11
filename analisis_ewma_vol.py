#!/usr/bin/env python3
"""Propuesta #11 backlog quant-desk (13-jul): ¿EWMA en vez de ventana plana
en _estimar_vol_h (shadow_predict.py:1085) mejora la estimación de sigma_h?

sigma_h alimenta `d = drift/sigma_h` en GBM_LATE_15M (LIVE, 5 tuplas
whitelisted) y UPDOWN_GBM — se trata con el mismo rigor que código de
dinero real (CLAUDE.md, project_state_2026-07-11): SOLO ANÁLISIS aquí, no
toca shadow_predict.py. Cualquier cambio de fórmula necesita aprobación
explícita + code-review si acaba tocando la ruta de GBM_LATE_15M en vivo.

Metodología: para cada asset y muchos puntos temporales en data/prices/
(desde que hay formato nuevo, 29-jun en adelante), compara dos estimadores
de sigma_h con el MISMO lookback (20min, igual que _s_gbm_late en vivo):
  - sigma_flat: fórmula actual, mean(log_r^2) sin ponderar.
  - sigma_ewma: mismo log_r^2 pero ponderado por decaimiento exponencial
    (más peso a los retornos recientes), para 2 half-lives (5min, 10min).
contra el sigma_h REALIZADO en los siguientes 15min (T_h de GBM_LATE_15M) —
la vol que de verdad ocurrió, no una proxy. Menor error de pronóstico =
mejor estimador. También testea el efecto apalancamiento (Heston): ¿drift
negativo reciente predice más vol futura?

Uso: python3 analisis_ewma_vol.py
"""
import bisect
import csv
import math
import statistics
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_PRICES = Path("data/prices")
SYMS = ["BTC", "ETH", "SOL", "XRP"]
LOOKBACK_MIN = 20   # igual que _s_gbm_late (n_min=20)
FORWARD_MIN = 15    # T_h de GBM_LATE_15M
STEP_MIN = 5         # cadencia de puntos de muestreo del backtest
HALF_LIVES = [2, 3, 5, 7, 10, 15, 20, 30]  # minutos, candidatos a testear


def cargar_precios(desde=None, hasta=None):
    """(ts, {sym: precio}) ordenado, solo ficheros formato nuevo (asset/price_usd)."""
    rows = []
    for path in sorted(DIR_PRICES.glob("*.csv")):
        fecha = path.stem
        if desde and fecha < desde:
            continue
        if hasta and fecha > hasta:
            continue
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if "asset" not in (reader.fieldnames or []):
                continue  # formato viejo, fuera de alcance (antes del live)
            buf, buf_ts = {}, None
            for row in reader:
                try:
                    ts = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)
                except Exception:
                    continue
                asset = (row.get("asset") or "").strip().upper()
                if asset not in SYMS:
                    continue
                try:
                    v = float(row.get("price_usd", ""))
                except (ValueError, TypeError):
                    continue
                if ts != buf_ts:
                    if buf:
                        rows.append((buf_ts, dict(buf)))
                    buf, buf_ts = {}, ts
                buf[asset] = v
            if buf:
                rows.append((buf_ts, dict(buf)))
    rows.sort(key=lambda x: x[0])
    return rows


def _series_por_asset(precios):
    """dict sym -> (lista_ts, lista_precio) ordenada, para bisect O(log n)."""
    por_asset = {sym: ([], []) for sym in SYMS}
    for ts, p in precios:
        for sym in SYMS:
            if sym in p:
                por_asset[sym][0].append(ts)
                por_asset[sym][1].append(p[sym])
    return por_asset


def _ventana(ts_list, precio_list, t0, t1):
    """(ts, precio) con t0 <= ts <= t1, O(log n) vía bisect sobre lista ordenada."""
    i0 = bisect.bisect_left(ts_list, t0)
    i1 = bisect.bisect_right(ts_list, t1)
    return list(zip(ts_list[i0:i1], precio_list[i0:i1]))


def _log_returns(serie):
    prices = [p for _, p in serie]
    ts = [t for t, _ in serie]
    out = []
    for i in range(1, len(prices)):
        if prices[i-1] > 0 and prices[i] > 0:
            out.append((ts[i], math.log(prices[i] / prices[i-1])))
    return out


def sigma_flat(log_r, avg_dur_min):
    if len(log_r) < 2 or avg_dur_min <= 0:
        return None
    var = sum(r * r for _, r in log_r) / len(log_r)
    return math.sqrt(var / avg_dur_min * 60)


def sigma_ewma(log_r, avg_dur_min, half_life_min, ahora):
    if len(log_r) < 2 or avg_dur_min <= 0:
        return None
    decay = math.log(2) / half_life_min
    pesos = [math.exp(-decay * (ahora - t).total_seconds() / 60) for t, _ in log_r]
    sw = sum(pesos)
    if sw <= 0:
        return None
    var = sum(w * r * r for w, (_, r) in zip(pesos, log_r)) / sw
    return math.sqrt(var / avg_dur_min * 60)


def main():
    precios = cargar_precios()
    print(f"Puntos de precio cargados: {len(precios)} | "
          f"rango: {precios[0][0].isoformat() if precios else 'n/a'} → "
          f"{precios[-1][0].isoformat() if precios else 'n/a'}")

    resultados = {sym: {"flat": [], **{f"ewma_hl{hl}": [] for hl in HALF_LIVES},
                         "drift_vs_realized": []} for sym in SYMS}

    if not precios:
        print("Sin datos.")
        return
    series = _series_por_asset(precios)
    t_min, t_max = precios[0][0], precios[-1][0]
    t = t_min + timedelta(minutes=LOOKBACK_MIN)
    n_puntos = 0
    while t + timedelta(minutes=FORWARD_MIN) <= t_max:
        for sym in SYMS:
            ts_list, precio_list = series[sym]
            lookback = _ventana(ts_list, precio_list, t - timedelta(minutes=LOOKBACK_MIN), t)
            forward = _ventana(ts_list, precio_list, t, t + timedelta(minutes=FORWARD_MIN))
            if len(lookback) < 5 or len(forward) < 5:
                continue
            log_r_lb = _log_returns(lookback)
            log_r_fwd = _log_returns(forward)
            if len(log_r_lb) < 3 or len(log_r_fwd) < 3:
                continue
            durs_lb = [(lookback[i][0] - lookback[i-1][0]).total_seconds() / 60
                       for i in range(1, len(lookback))]
            avg_dur_lb = sum(durs_lb) / len(durs_lb)
            durs_fwd = [(forward[i][0] - forward[i-1][0]).total_seconds() / 60
                        for i in range(1, len(forward))]
            avg_dur_fwd = sum(durs_fwd) / len(durs_fwd)

            s_flat = sigma_flat(log_r_lb, avg_dur_lb)
            s_real = sigma_flat(log_r_fwd, avg_dur_fwd)  # mismo estimador, ventana futura = "verdad"
            if s_flat is None or s_real is None:
                continue
            resultados[sym]["flat"].append((s_flat, s_real))
            for hl in HALF_LIVES:
                s_e = sigma_ewma(log_r_lb, avg_dur_lb, hl, t)
                if s_e is not None:
                    resultados[sym][f"ewma_hl{hl}"].append((s_e, s_real))
            drift_lb = (lookback[-1][1] / lookback[0][1] - 1) * 100
            resultados[sym]["drift_vs_realized"].append((drift_lb, s_real))
            n_puntos += 1
        t += timedelta(minutes=STEP_MIN)

    print(f"Puntos de backtest evaluados (asset-instante): {n_puntos}")
    print()

    def mae_corr(pairs):
        if len(pairs) < 15:
            return None
        errs = [abs(a - b) for a, b in pairs]
        mae = statistics.mean(errs)
        try:
            corr = statistics.correlation([a for a, _ in pairs], [b for _, b in pairs])
        except Exception:
            corr = float("nan")
        return mae, corr, len(pairs)

    for sym in SYMS:
        print(f"--- {sym} ---")
        r = mae_corr(resultados[sym]["flat"])
        if r:
            print(f"  flat (actual):      MAE={r[0]:.5f}  corr={r[1]:+.3f}  n={r[2]}")
        else:
            print("  flat: n insuficiente")
        for hl in HALF_LIVES:
            r = mae_corr(resultados[sym][f"ewma_hl{hl}"])
            if r:
                print(f"  ewma half_life={hl:2d}min: MAE={r[0]:.5f}  corr={r[1]:+.3f}  n={r[2]}")
            else:
                print(f"  ewma half_life={hl}min: n insuficiente")
        r = mae_corr(resultados[sym]["drift_vs_realized"])
        if r:
            print(f"  drift_lookback vs vol_realizada_forward: corr={r[1]:+.3f}  n={r[2]}  "
                  f"(negativo y fuerte = efecto apalancamiento tipo Heston)")
        print()

    print("=" * 70)
    print("Lectura: menor MAE / mayor corr(+) contra sigma_h REALIZADO forward = mejor "
          "estimador. Si ewma no mejora claramente sobre flat en ninguna moneda, no hay "
          "caso para tocar _estimar_vol_h (que alimenta GBM_LATE_15M en vivo).")


if __name__ == "__main__":
    main()
