#!/usr/bin/env python3
"""
backtest_momentum_ibs_5m_17ago.py — backtest histórico de MOMENTUM_IBS_5M
sobre klines reales de Binance (17-Ago, petición Javi: "cárgale todo el
histórico").

Por qué esto y no conectar de golpe gate_bucket_propio/calibración/
micro-buckets: la estrategia nació hoy (n=0 resuelto). Esos mecanismos
exigen results.csv con outcome_real/pnl_neto reales (n>=15-40) -- no se
pueden "conectar" sin datos, sería fabricar un veredicto. Este script
SÍ es aplicable sin esperar: reconstruye la señal (drift_7min + ibs_7min,
misma fórmula exacta que _drift_e_ibs_ventana en shadow_predict.py) sobre
klines históricos reales y resuelve el outcome real (Up si
close(slot_end)>=close(slot_start), mismo criterio que backfill_history.py
usa para GBM/ORDER_FLOW) -- da n en miles en vez de esperar semanas de
shadow forward.

Caveat explícito: el outcome se resuelve con el tick de Binance en el
cierre del slot, no con el mecanismo real de Polymarket (Chainlink +
TWAP desde 07-Ago sobre los últimos ~60s). Puede diferir en el margen en
fotos-finish exactas, pero es la misma aproximación que ya usa
backfill_history.py para TODAS las demás estrategias del proyecto --
no es una debilidad nueva de este script.

Solo mide si la SEÑAL (drift+ibs) predice la dirección -- no fill-ability
ni precio de entrada real (eso no existe retroactivamente, requiere
libro_snapshots.csv que solo se genera en vivo). Ver protocolo:
1) este backtest confirma o refuta si hay señal real
2) si confirma, se deja acumular forward con datos propios
   (predictions_*.csv/results.csv) para calibración/micro-bucket real
3) fill-ability se mide SIEMPRE forward, nunca retroactivo (no hay libro
   histórico)

Uso: python3 backtest_momentum_ibs_5m_17ago.py [--days 35]
"""
import argparse
import bisect
import math
from collections import defaultdict
from datetime import datetime, timedelta, timezone

import numpy as np

from backfill_history import get_klines_day, _build_price_series, _build_index, _spot_at

UTC = timezone.utc
ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
LOOKBACK_MIN = 7
IBS_UMBRAL = 0.7
FEE = 0.07
TWAP_CUTOFF = datetime(2026, 8, 7, tzinfo=UTC)  # mismo corte que shadow_postmortem.es_pre_twap para 5min


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

    filas = []  # (activo, slot_end_dt, drift, ibs, decision, outcome_yes)
    for activo in ASSETS:
        print(f"[{activo}] descargando/cacheando klines ({len(dias)} días)...")
        klines_all = []
        for d in dias:
            klines_all.extend(get_klines_day(activo, d))
        if not klines_all:
            print(f"  sin datos para {activo}")
            continue
        series = _build_price_series(klines_all)
        idx = _build_index(series)
        if not series:
            continue
        t0 = series[0][0]
        tN = series[-1][0]
        # alinear al primer slot de 5min completo
        t = t0.replace(second=0, microsecond=0)
        t += timedelta(minutes=(5 - t.minute % 5) % 5 or 5)
        n_local = 0
        while t <= tN:
            # FIX look-ahead (17-Ago, autodetectado): la señal se calcula
            # ANTES de que abra la ventana que se intenta predecir --
            # slot_start = t (apertura), slot_end = t+5 (cierre, futuro
            # desconocido en el momento de la señal). El lookback de
            # drift/ibs mira HACIA ATRÁS desde slot_start (nunca toca datos
            # de la propia ventana [slot_start, slot_end]).
            slot_start = t
            slot_end = t + timedelta(minutes=5)
            drift, ibs = drift_ibs_en(series, idx, slot_start, LOOKBACK_MIN)
            if drift is not None and ibs is not None:
                p_start = _spot_at(series, slot_start, tol_min=2, _idx=idx)
                p_end = _spot_at(series, slot_end, tol_min=2, _idx=idx)
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
            t += timedelta(minutes=5)
        print(f"  {n_local} señales (todo el periodo)")

    print(f"\nTotal señales (todos los periodos): {len(filas)}")

    # post-TWAP only
    filas_twap = [f for f in filas if f[1] >= TWAP_CUTOFF]
    print(f"Post-TWAP (>=07-Ago): {len(filas_twap)}\n")

    def acierto(decision, outcome_yes):
        return 1 if ((decision == "BUY_YES" and outcome_yes == 1) or
                     (decision == "BUY_NO" and outcome_yes == 0)) else 0

    print("=" * 90)
    print("RESULTADOS POST-TWAP, por activo (rigor: Wilson90lo vs 50%, shuffle, split-half)")
    print("=" * 90)
    rng = np.random.default_rng(42)
    resumen = {}
    for act in ASSETS:
        sub = [f for f in filas_twap if f[0] == act]
        n = len(sub)
        if n < 15:
            print(f"{act}: n={n} insuficiente")
            continue
        hits = sum(acierto(d, o) for _, _, _, _, d, o in sub)
        hit = hits / n
        wl = wilson_lower(hits, n)
        # shuffle vs 50%
        aciertos = np.array([acierto(d, o) for _, _, _, _, d, o in sub])
        sim = rng.binomial(1, 0.5, size=(2000, n)).mean(axis=1)
        p_shuffle = (sim >= hit).mean()
        subs = sorted(sub, key=lambda x: x[1])
        mid = n // 2
        h1 = sum(acierto(d, o) for _, _, _, _, d, o in subs[:mid]) / mid
        h2 = sum(acierto(d, o) for _, _, _, _, d, o in subs[mid:]) / (n - mid)
        resumen[act] = dict(n=n, hit=hit, wilson90lo=wl, p_shuffle=p_shuffle, h1=h1, h2=h2)
        print(f"{act}: n={n} hit={hit*100:.1f}% wilson90lo={wl*100:.1f}% p_shuffle={p_shuffle:.4f} "
              f"split_half=[{h1*100:.1f}%,{h2*100:.1f}%]")

    # BUY_YES vs BUY_NO por separado (payout asimétrico posible)
    print("\n" + "=" * 90)
    print("Por dirección (BUY_YES=sigue arriba / BUY_NO=sigue abajo), agregado 6 monedas")
    print("=" * 90)
    for dec in ("BUY_YES", "BUY_NO"):
        sub = [f for f in filas_twap if f[4] == dec]
        n = len(sub)
        if n < 15:
            continue
        hits = sum(acierto(d, o) for _, _, _, _, d, o in sub)
        wl = wilson_lower(hits, n)
        print(f"{dec}: n={n} hit={hits/n*100:.1f}% wilson90lo={wl*100:.1f}%")

    import json
    with open("data/shadow/backtest_momentum_ibs_5m_resultado.json", "w") as f:
        json.dump({"generado_utc": datetime.now(UTC).isoformat(), "dias": args.days,
                    "n_total_post_twap": len(filas_twap), "por_activo": resumen}, f, indent=2)
    print("\nGuardado en data/shadow/backtest_momentum_ibs_5m_resultado.json")


if __name__ == "__main__":
    main()
