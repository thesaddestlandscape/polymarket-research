#!/usr/bin/env python3
"""analisis_kalshi_curva_vol_gap_sigma_27ago.py -- propuesta #2, ver
docstring version anterior. Fix: procesar TODAS las filas de cada
minuto muestreado (bug v1: el dedup descartaba todos los strikes menos
uno). Ahora bufferiza por (event_ticker, minuto) y funde en cuanto
cambia el minuto, sin guardar todo el CSV en memoria.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import numpy as np
from scipy.stats import norm

REPO = Path(__file__).resolve().parent
csv.field_size_limit(sys.maxsize)

FILES = sorted(REPO.glob("data/prices/kalshi_btchourly_2026-08-*.csv"))
print(f"Archivos kalshi_btchourly: {len(FILES)}", file=sys.stderr)


def norm_cdf(x):
    return norm.cdf(x)


def fit_sigma(spot, T_h, strikes_prices):
    if len(strikes_prices) < 6 or T_h <= 0:
        return None, None
    grid = np.linspace(0.0005, 0.06, 300)

    def sse(sigma):
        s = 0.0
        for k, p in strikes_prices:
            d2 = math.log(spot / k) / (sigma * math.sqrt(T_h))
            s += (norm_cdf(d2) - p) ** 2
        return s

    vals = [sse(g) for g in grid]
    best = grid[int(np.argmin(vals))]
    lo, hi = max(best * 0.6, 1e-5), best * 1.4
    grid2 = np.linspace(lo, hi, 150)
    vals2 = [sse(g) for g in grid2]
    best2 = grid2[int(np.argmin(vals2))]
    obs = np.array([p for _, p in strikes_prices])
    pred = np.array([norm_cdf(math.log(spot / k) / (best2 * math.sqrt(T_h))) for k, _ in strikes_prices])
    ss_res = np.sum((obs - pred) ** 2)
    ss_tot = np.sum((obs - obs.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else None
    return best2, r2


def procesar_snapshot(et, minute_rows):
    if len(minute_rows) < 6:
        return None
    strikes_prices = []
    for x in minute_rows:
        try:
            yb, ya = float(x["yes_bid"]), float(x["yes_ask"])
            k = float(x["floor_strike"])
        except (ValueError, TypeError):
            return None
        if yb <= 0.02 or ya >= 0.98 or ya < yb:
            continue
        strikes_prices.append((k, (yb + ya) / 2))
    if len(strikes_prices) < 6:
        return None
    strikes_prices = sorted(set(strikes_prices))
    try:
        t_close = datetime.fromisoformat(minute_rows[0]["close_time"].replace("Z", "+00:00"))
        t_now = datetime.fromisoformat(minute_rows[0]["timestamp_utc"].replace("Z", "+00:00"))
        T_h = (t_close - t_now).total_seconds() / 3600.0
    except Exception:
        return None
    if not (0.02 < T_h <= 1.05):
        return None
    spot = None
    for i in range(len(strikes_prices) - 1):
        k1, p1 = strikes_prices[i]
        k2, p2 = strikes_prices[i + 1]
        if (p1 - 0.5) * (p2 - 0.5) <= 0 and p1 != p2:
            spot = k1 + (k2 - k1) * (0.5 - p1) / (p2 - p1)
            break
    if spot is None:
        return None
    sigma_fit, r2 = fit_sigma(spot, T_h, strikes_prices)
    if sigma_fit is None:
        return None
    return {"event_ticker": et, "ts": minute_rows[0]["timestamp_utc"], "T_h": round(T_h, 4),
            "spot": round(spot, 2), "sigma_kalshi": round(sigma_fit, 6),
            "r2": round(r2, 4) if r2 is not None else None, "n_strikes": len(strikes_prices)}


resultados = []
for fp in FILES:
    print(f"procesando {fp.name} ...", file=sys.stderr)
    buffers = {}  # et -> (minute, [rows])
    n_finalized = 0
    with open(fp) as f:
        r = csv.DictReader(f)
        for row in r:
            et = row["event_ticker"]
            minute = row["timestamp_utc"][:16]
            cur = buffers.get(et)
            if cur is None:
                buffers[et] = (minute, [row])
            elif cur[0] == minute:
                cur[1].append(row)
            else:
                # SAMPLEO: solo procesamos si el minuto termina en :00,:20,:40 (cada ~20min)
                mm = int(cur[0][-2:])
                if mm % 20 == 0:
                    res = procesar_snapshot(et, cur[1])
                    if res:
                        resultados.append(res)
                        n_finalized += 1
                buffers[et] = (minute, [row])
    print(f"  snapshots validos acumulados: {n_finalized}", file=sys.stderr)

print(f"\nTotal snapshots con fit valido: {len(resultados)}")
if resultados:
    r2s = [r["r2"] for r in resultados if r["r2"] is not None]
    sigmas = [r["sigma_kalshi"] for r in resultados]
    ns = [r["n_strikes"] for r in resultados]
    print(f"n_strikes por snapshot: media={np.mean(ns):.1f} mediana={np.median(ns):.0f}")
    print(f"R2 fit: media={np.mean(r2s):.4f} mediana={np.median(r2s):.4f} p10={np.percentile(r2s,10):.4f}")
    print(f"sigma_kalshi (por-sqrt-hora): media={np.mean(sigmas):.5f} mediana={np.median(sigmas):.5f} std={np.std(sigmas):.5f}")
    with open(REPO / "data/shadow/kalshi_sigma_curva_27ago.json", "w") as f:
        json.dump(resultados, f)
    print("Guardado data/shadow/kalshi_sigma_curva_27ago.json")
else:
    print("SIN resultados -- revisar filtros")
