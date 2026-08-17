#!/usr/bin/env python3
"""
backtest_momentum_ibs_15m_17ago.py — backtest histórico de momentum
genuino (drift+ibs) a 15min, mismo día que la versión de 5min (Javi:
"¿y de 15 minutos? ¿por qué no lo has construido?").

Lookback=20min (ratio 1.33x sobre 15min, YA validado dentro de
GBM_LATE_15M como feature -- 10-Jul, _drift_e_ibs_ventana: alineado 65%
hit EV+0.34 vs no-alineado 59% EV+0.27, n=1133/508; extremo fresco a
favor 70% hit EV+0.42 n=398 -- pero NUNCA extraído como estrategia
propia, solo vivía condicionado a que GBM_LATE_15M ya hubiera disparado).
Este backtest mide la señal SOLA, sin esa condición previa -- no asumir
que el resultado de 5min (momentum refutado, fade con edge) transfiere
a 15min sin datos propios.

Mismo método que backtest_momentum_ibs_5m_17ago.py (reutiliza
backfill_history.get_klines_day, mismo fix de look-ahead ya aplicado
desde el diseño inicial: señal en la APERTURA del slot, outcome de
apertura a cierre, nunca al revés).

Uso: python3 backtest_momentum_ibs_15m_17ago.py [--days 35]
"""
import argparse
import bisect
import math
from datetime import datetime, timedelta, timezone

import numpy as np

from backfill_history import get_klines_day, _build_price_series, _build_index, _spot_at

UTC = timezone.utc
ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
WINDOW_MIN = 15
LOOKBACK_MIN = 20  # 1.33x de 15min, mismo ratio ya validado como feature en GBM_LATE_15M
IBS_UMBRAL = 0.7
TWAP_CUTOFF = datetime(2026, 8, 7, tzinfo=UTC)


def wilson_lower(hits, n, z=1.6449):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def drift_ibs_en(series, idx, target_dt, n_min):
    cutoff = target_dt - timedelta(minutes=n_min)
    lo = bisect.bisect_left(idx, cutoff)
    hi = bisect.bisect_right(idx, target_dt)
    sub = series[lo:hi]
    if len(sub) < 5:
        return None, None
    ref_p, now_p = sub[0][1], sub[-1][1]
    if ref_p <= 0:
        return None, None
    drift_pct = (now_p / ref_p - 1) * 100
    closes = [pt[1] for pt in sub]
    loP, hiP = min(closes), max(closes)
    ibs = (now_p - loP) / (hiP - loP) if (hiP - loP) > 1e-9 else 0.5
    return round(drift_pct, 4), round(ibs, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=35)
    args = ap.parse_args()

    hoy = datetime.now(UTC).date()
    dias = [(hoy - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(args.days, 0, -1)]

    filas = []
    for activo in ASSETS:
        print(f"[{activo}] cacheando klines ({len(dias)} días)...")
        klines_all = []
        for d in dias:
            klines_all.extend(get_klines_day(activo, d))
        if not klines_all:
            continue
        series = _build_price_series(klines_all)
        idx = _build_index(series)
        if not series:
            continue
        t0, tN = series[0][0], series[-1][0]
        t = t0.replace(second=0, microsecond=0)
        t += timedelta(minutes=(WINDOW_MIN - t.minute % WINDOW_MIN) % WINDOW_MIN or WINDOW_MIN)
        n_local = 0
        while t <= tN:
            slot_start = t
            slot_end = t + timedelta(minutes=WINDOW_MIN)
            drift, ibs = drift_ibs_en(series, idx, slot_start, LOOKBACK_MIN)
            if drift is not None and ibs is not None:
                p_start = _spot_at(series, slot_start, tol_min=3, _idx=idx)
                p_end = _spot_at(series, slot_end, tol_min=3, _idx=idx)
                if p_start and p_end:
                    outcome_yes = 1 if p_end >= p_start else 0
                    if drift > 0 and ibs >= IBS_UMBRAL:
                        decision = "BUY_YES"
                    elif drift < 0 and ibs <= (1 - IBS_UMBRAL):
                        decision = "BUY_NO"
                    else:
                        decision = None
                    if decision:
                        filas.append((activo, slot_end, drift, ibs, decision, outcome_yes))
                        n_local += 1
            t += timedelta(minutes=WINDOW_MIN)
        print(f"  {n_local} señales")

    filas_twap = [f for f in filas if f[1] >= TWAP_CUTOFF]
    print(f"\nTotal post-TWAP: {len(filas_twap)}\n")

    def acierto(d, o):
        return 1 if ((d == "BUY_YES" and o == 1) or (d == "BUY_NO" and o == 0)) else 0

    def fade(d):
        return "BUY_NO" if d == "BUY_YES" else "BUY_YES"

    rng = np.random.default_rng(42)
    for modo, transform in (("MOMENTUM (puro)", lambda d: d), ("FADE (invertido)", fade)):
        print("=" * 90)
        print(modo)
        print("=" * 90)
        resumen = {}
        for act in ASSETS:
            sub = [f for f in filas_twap if f[0] == act]
            n = len(sub)
            if n < 15:
                print(f"{act}: n={n} insuficiente")
                continue
            hits = sum(acierto(transform(d), o) for _, _, _, _, d, o in sub)
            hit = hits / n
            wl = wilson_lower(hits, n)
            sim = rng.binomial(1, 0.5, size=(2000, n)).mean(axis=1)
            p_shuffle = (sim >= hit).mean()
            subs = sorted(sub, key=lambda x: x[1])
            mid = n // 2
            h1 = sum(acierto(transform(d), o) for _, _, _, _, d, o in subs[:mid]) / mid
            h2 = sum(acierto(transform(d), o) for _, _, _, _, d, o in subs[mid:]) / (n - mid)
            resumen[act] = dict(n=n, hit=hit, wilson90lo=wl, p_shuffle=p_shuffle, h1=h1, h2=h2)
            print(f"{act}: n={n} hit={hit*100:.1f}% wilson90lo={wl*100:.1f}% p_shuffle={p_shuffle:.4f} "
                  f"split_half=[{h1*100:.1f}%,{h2*100:.1f}%]")
        for dec in ("BUY_YES", "BUY_NO"):
            sub = [f for f in filas_twap if transform(f[4]) == dec]
            n = len(sub)
            if n < 15:
                continue
            hits = sum(acierto(dec, o) for _, _, _, _, _, o in sub)
            wl = wilson_lower(hits, n)
            print(f"  {dec}: n={n} hit={hits/n*100:.1f}% wilson90lo={wl*100:.1f}%")
        print()

    import json
    with open("data/shadow/backtest_momentum_ibs_15m_resultado.json", "w") as f:
        json.dump({"generado_utc": datetime.now(UTC).isoformat(), "dias": args.days,
                    "n_total_post_twap": len(filas_twap)}, f, indent=2)


if __name__ == "__main__":
    main()
