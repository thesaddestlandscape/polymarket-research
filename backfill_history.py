#!/usr/bin/env python3
"""
backfill_history.py — Calibración histórica completa (todas las estrategias).

Arquitectura simplificada — sin API de Polymarket para outcomes:
  Los mercados Up/Down resuelven según Chainlink ≈ Binance close.
  Outcome = "YES" (Up) si close(slot_end) >= close(slot_start).

Pipeline:
  Fase 1 — Descarga klines 1min de Binance por (par, día) → cache
  Fase 2 — Simula predicciones GBM + ORDER_FLOW en cada slot
  Fase 3 — Calibración: grid search de parámetros + H-hypotheses

Calibra:
  DRIFT_DAMPING, REGIME_THRESHOLD, H-OVERDRIFT (GBM)
  DELTA_MIN/MAX por par (ORDER_FLOW)
  H-REGIMEN confirmación 90d

Uso:
  python3 backfill_history.py [--days 90] [--phase 1|2|3|all] [--pairs BTC,ETH,...]
  python3 backfill_history.py --phase 3   # recalibrar sobre resultados ya descargados
"""

import argparse
import csv
import json
import math
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# ── Importar funciones compartidas con shadow_predict ────────────────────────
import sys
sys.path.insert(0, str(Path(__file__).parent))
from shadow_predict import (
    _gbm_p_up, _norm_cdf, _parse_updown_tipo, identificar_activo,
    BINANCE_SYMBOLS, EDGE_MINIMO, SLIPPAGE_ESTIMADO,
    ORDER_FLOW_PAIR_BLACKLIST, ORDER_FLOW_BLACKLIST_HOURS,
)

# ── Constantes ────────────────────────────────────────────────────────────────
UTC = timezone.utc

DIR_BACKFILL = Path("data/backfill")
DIR_KLINES   = DIR_BACKFILL / "klines"
RESULTS_FILE = DIR_BACKFILL / "backfill_results.csv"
CALIB_FILE   = DIR_BACKFILL / "calibration_results.json"

DIR_BACKFILL.mkdir(parents=True, exist_ok=True)
DIR_KLINES.mkdir(parents=True, exist_ok=True)

RESULTS_HEADER = [
    "slot_start_utc", "slot_end_utc", "activo", "ventana_min",
    "strategy", "decision", "outcome_real", "acierto", "pnl_neto",
    "prob_yes_modelo", "edge_neto",
    "drift_60min", "drift_15min", "sigma_h", "pct_spot_vs_ref",
    "delta_ratio",
]

# Pares a incluir en el backfill (los que tienen mercados Up/Down en Polymarket)
PAIRS_GBM = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
PAIRS_OF  = [p for p in PAIRS_GBM if p not in ORDER_FLOW_PAIR_BLACKLIST]

# Ventanas de slot en minutos → (nombre subtype, tipo interno)
VENTANAS = {
    5:    ("5min",   "slot"),
    15:   ("15min",  "slot"),
    60:   ("60min",  "hourly"),
    240:  ("240min", "slot"),
}


# ── Binance klines históricos ─────────────────────────────────────────────────

def get_klines_day(activo: str, date_str: str) -> list:
    """
    Klines 1min para (activo, 'YYYY-MM-DD').
    Rango: 22:00 UTC día anterior → 24:00 UTC → cubre todos los slots del día
    con 2h de contexto para drift_60min y sigma.
    Cache en data/backfill/klines/YYYY-MM-DD_{ACTIVO}.json
    """
    cache_path = DIR_KLINES / f"{date_str}_{activo}.json"
    if cache_path.exists():
        return json.load(open(cache_path))

    symbol   = BINANCE_SYMBOLS[activo]
    day_dt   = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=UTC)
    start_ms = int((day_dt - timedelta(hours=2)).timestamp() * 1000)
    end_ms   = int((day_dt + timedelta(hours=24)).timestamp() * 1000)

    klines  = []
    cur     = start_ms
    session = requests.Session()

    while cur < end_ms:
        try:
            r = session.get(
                "https://api.binance.com/api/v3/klines",
                params={"symbol": symbol, "interval": "1m",
                        "startTime": cur, "limit": 1000},
                timeout=30,
            )
            r.raise_for_status()
            batch = r.json()
        except Exception as e:
            print(f"  [WARN] {activo} {date_str}: {e}. Reintentando en 3s...")
            time.sleep(3)
            continue

        if not batch:
            break

        klines.extend(batch)
        last_ms = int(batch[-1][0])
        if last_ms >= end_ms - 60000:
            break
        cur = last_ms + 60000
        time.sleep(0.05)

    if klines:
        json.dump(klines, open(cache_path, "w"))
    return klines


# ── Helpers GBM con tiempo explícito ─────────────────────────────────────────

def _build_price_series(klines: list) -> list:
    """(datetime, close, taker_buy_vol, vol) ordenado por tiempo."""
    out = []
    for k in klines:
        try:
            dt    = datetime.fromtimestamp(int(k[0]) / 1000, tz=UTC)
            close = float(k[4])
            vol   = float(k[5])
            tb    = float(k[9]) if len(k) >= 10 else vol / 2  # k[9]=taker_buy_base (full Binance format)
        except Exception:
            continue
        out.append((dt, close, tb, vol))
    return sorted(out, key=lambda x: x[0])


import bisect

def _build_index(series):
    """Pre-computa timestamps como lista ordenada para lookups O(log n)."""
    return [pt[0] for pt in series]


def _spot_at(series, target_dt, tol_min=3, _idx=None):
    """Precio close más cercano a target_dt (tolerancia ±tol_min)."""
    if not series:
        return None
    idx = _idx if _idx is not None else _build_index(series)
    pos = bisect.bisect_left(idx, target_dt)
    best_p, best_d = None, float("inf")
    for i in range(max(0, pos - 1), min(len(series), pos + 2)):
        d = abs((series[i][0] - target_dt).total_seconds())
        if d < best_d:
            best_d, best_p = d, series[i][1]
    return best_p if best_d <= tol_min * 60 else None


def _sigma_at(series, signal_dt, n_min=120, _idx=None) -> float | None:
    """Volatilidad por hora usando series hasta signal_dt."""
    idx    = _idx if _idx is not None else _build_index(series)
    cutoff = signal_dt - timedelta(minutes=n_min)
    lo     = bisect.bisect_left(idx, cutoff)
    hi     = bisect.bisect_right(idx, signal_dt)
    sub    = series[lo:hi]
    if len(sub) < 5:
        hi2 = bisect.bisect_right(idx, signal_dt)
        sub = series[max(0, hi2 - 60):hi2]
    if len(sub) < 2:
        return None
    ps    = [pt[1] for pt in sub]
    log_r = [math.log(ps[i] / ps[i-1]) for i in range(1, len(ps)) if ps[i-1] > 0]
    if len(log_r) < 2:
        return None
    var   = sum(r * r for r in log_r) / len(log_r)
    durs  = [(sub[i][0] - sub[i-1][0]).total_seconds() / 60 for i in range(1, len(sub))]
    avg_d = sum(durs) / len(durs) if durs else 1.0
    return math.sqrt(var / avg_d * 60) if avg_d > 0 else None


def _drift_at(series, signal_dt, n_min, _idx=None) -> float | None:
    """Drift en fracción/hora observado en las últimas n_min hasta signal_dt."""
    idx    = _idx if _idx is not None else _build_index(series)
    cutoff = signal_dt - timedelta(minutes=n_min)
    lo     = bisect.bisect_left(idx, cutoff)
    hi     = bisect.bisect_right(idx, signal_dt)
    sub    = series[lo:hi]
    if len(sub) < 5:
        return None
    p0, p1 = sub[0][1], sub[-1][1]
    return (p1 / p0 - 1) / (n_min / 60) if p0 > 0 else None


# ── Simulación GBM histórica ──────────────────────────────────────────────────

def simulate_gbm(series, slot_start_dt, slot_end_dt, ventana_min,
                 drift_damping=0.25, regime_threshold=0.55, precio_yes=0.50,
                 _idx=None):
    """
    Simula s_updown_gbm en modo histórico.
    signal_dt = slot_start + 1min (señal justo al abrir el slot).
    Devuelve dict de resultados o None si no hay señal.
    _idx: índice precalculado de timestamps para lookups O(log n).
    """
    signal_dt = slot_start_dt + timedelta(minutes=1)

    T_h = (slot_end_dt - signal_dt).total_seconds() / 3600
    if T_h <= 2 / 60:
        return None

    idx = _idx if _idx is not None else _build_index(series)

    # Ventana de vol según tipo de slot
    if ventana_min is None:       # daily
        vol_win = 240
        tol_min = 15
    elif ventana_min >= 60:
        vol_win = 120
        tol_min = 8
    else:
        vol_win = min(60, max(15, ventana_min * 4))
        tol_min = max(2, ventana_min // 2)

    spot = _spot_at(series, signal_dt, tol_min=3, _idx=idx)
    ref  = _spot_at(series, slot_start_dt, tol_min=tol_min, _idx=idx)
    if spot is None or ref is None or ref <= 0:
        return None

    sigma_h = _sigma_at(series, signal_dt, n_min=vol_win, _idx=idx)
    if not sigma_h or sigma_h <= 0:
        return None

    drift_60 = _drift_at(series, signal_dt, n_min=60, _idx=idx)
    drift_15 = _drift_at(series, signal_dt, n_min=15, _idx=idx)
    mu_h     = (drift_60 or 0.0) * drift_damping
    pct      = (spot / ref - 1) * 100

    p_up = _gbm_p_up(spot, ref, sigma_h, T_h, mu_h=mu_h)
    if p_up is None:
        return None

    # Filtro 5min mean-reversion
    if ventana_min == 5 and abs(pct) > 0.05:
        return None

    # Filtro H-REGIMEN (solo #15min)
    if ventana_min == 15 and drift_60 is not None:
        dp = drift_60 * 100
        bullish = p_up > precio_yes
        if dp > regime_threshold and not bullish:
            return None
        if dp < -regime_threshold and bullish:
            return None

    edge_bruto = p_up - precio_yes
    edge_neto  = abs(edge_bruto) - EDGE_MINIMO - SLIPPAGE_ESTIMADO
    if edge_neto <= 0:
        return None

    return {
        "decision":    "BUY_YES" if edge_bruto > 0 else "BUY_NO",
        "p_up":        p_up,
        "edge_neto":   edge_neto,
        "sigma_h":     sigma_h,
        "drift_60min": round((drift_60 or 0) * 100, 4),
        "drift_15min": round((drift_15 or 0) * 100, 4),
        "pct":         round(pct, 4),
    }


# ── Simulación ORDER_FLOW histórica ───────────────────────────────────────────

def simulate_order_flow(klines, slot_start_dt, slot_end_dt,
                        delta_min=0.38, delta_max=0.46, precio_yes=0.50):
    """
    Simula ORDER_FLOW_5M en modo histórico.
    signal_dt = slot_start + 2min (cumple el mínimo de 1.5min vividos).
    Devuelve dict o None.
    """
    signal_dt = slot_start_dt + timedelta(minutes=2)

    hora_utc = signal_dt.hour
    if hora_utc in ORDER_FLOW_BLACKLIST_HOURS:
        return None

    signal_ms = int(signal_dt.timestamp() * 1000)
    last5     = [k for k in klines if int(k[0]) <= signal_ms][-5:]
    if len(last5) < 5:
        return None

    cum_delta = 0.0
    total_vol  = 0.0
    for k in last5:
        try:
            vol = float(k[5])
            tb  = float(k[9]) if len(k) >= 10 else vol / 2  # k[9]=taker_buy_base (full Binance format)
        except Exception:
            return None
        total_vol  += vol
        cum_delta  += 2 * tb - vol

    if total_vol <= 0:
        return None

    delta_ratio = cum_delta / total_vol
    if not (delta_min <= abs(delta_ratio) <= delta_max):
        return None

    p_yes = max(0.10, min(0.90, 0.5 + delta_ratio * 0.5))
    edge_neto = abs(p_yes - precio_yes) - EDGE_MINIMO - SLIPPAGE_ESTIMADO
    if edge_neto <= 0:
        return None

    return {
        "decision":    "BUY_YES" if p_yes > precio_yes else "BUY_NO",
        "p_up":        p_yes,
        "edge_neto":   edge_neto,
        "delta_ratio": round(delta_ratio, 4),
    }


def _pnl(decision, outcome, apuesta=0.50):
    """PNL neto. Win → +apuesta×0.96; Loss → -apuesta."""
    win = (decision == "BUY_YES" and outcome == "YES") or \
          (decision == "BUY_NO"  and outcome == "NO")
    return round(apuesta * 0.96, 4) if win else round(-apuesta, 4)


# ── FASE 1: Descarga de klines ────────────────────────────────────────────────

def phase1_klines(lookback_days: int, pairs: list[str]):
    print(f"\n=== FASE 1: Klines Binance ({lookback_days} días × {len(pairs)} pares) ===")
    today    = datetime.now(UTC).date()
    dates    = [(today - timedelta(days=d)).strftime("%Y-%m-%d")
                for d in range(lookback_days + 2)]  # +2 para contexto nocturno

    needed = [(a, d) for a in pairs for d in dates]
    cached = sum(1 for a, d in needed if (DIR_KLINES / f"{d}_{a}.json").exists())
    print(f"  Necesarios: {len(needed)}  Ya en cache: {cached}  A descargar: {len(needed)-cached}")

    done = 0
    for activo, date_str in sorted(needed):
        if (DIR_KLINES / f"{date_str}_{activo}.json").exists():
            done += 1
            continue
        klines = get_klines_day(activo, date_str)
        done += 1
        if done % 30 == 0:
            print(f"    [{done}/{len(needed)}] {activo} {date_str}  {'✓' if klines else '✗ vacío'}")
        time.sleep(0.08)

    print(f"  ✓ Klines listos ({done} combinaciones)")


# ── FASE 2: Simulación ────────────────────────────────────────────────────────

def phase2_simulate(lookback_days: int, pairs_gbm: list[str], pairs_of: list[str],
                    drift_damping=0.25, regime_threshold=0.55,
                    delta_min=0.38, delta_max=0.46):
    print(f"\n=== FASE 2: Simulación de predicciones ===")

    today   = datetime.now(UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    cutoff  = today - timedelta(days=lookback_days)

    rows     = []
    n_gbm    = 0
    n_of     = 0
    n_skip   = 0
    total_slots = 0

    # Iterar (par, ventana) → iterar slots
    for ventana_min, (subtype_label, tipo_str) in VENTANAS.items():
        step_min  = ventana_min  # slots contiguos sin overlap
        slot_dt   = cutoff
        _series_day_cache: dict = {}  # (activo, date_str) → (series, idx, klines_raw)

        while slot_dt < today:
            slot_start = slot_dt
            slot_end   = slot_dt + timedelta(minutes=ventana_min)
            slot_dt   += timedelta(minutes=step_min)

            date_str   = slot_start.strftime("%Y-%m-%d")
            prev_date  = (slot_start - timedelta(days=1)).strftime("%Y-%m-%d")

            for activo in pairs_gbm:
                total_slots += 1
                cache_key = (activo, date_str)
                if cache_key not in _series_day_cache:
                    klines_raw = _load_cache(activo, prev_date) + _load_cache(activo, date_str)
                    if not klines_raw:
                        _series_day_cache[cache_key] = ([], [], [])
                    else:
                        s = _build_price_series(klines_raw)
                        _series_day_cache[cache_key] = (s, _build_index(s), klines_raw)
                series, idx, klines_raw = _series_day_cache[cache_key]

                if not series:
                    n_skip += 1
                    continue

                # Outcome real: close(end) >= close(start) → YES/Up
                close_start = _spot_at(series, slot_start, tol_min=2, _idx=idx)
                close_end   = _spot_at(series, slot_end,   tol_min=2, _idx=idx)
                if close_start is None or close_end is None:
                    n_skip += 1
                    continue
                outcome = "YES" if close_end >= close_start else "NO"

                # ── GBM ──────────────────────────────────────────────────
                gbm = simulate_gbm(
                    series, slot_start, slot_end, ventana_min,
                    drift_damping=drift_damping,
                    regime_threshold=regime_threshold,
                    _idx=idx,
                )
                if gbm:
                    acierto = int(
                        (gbm["decision"] == "BUY_YES" and outcome == "YES") or
                        (gbm["decision"] == "BUY_NO"  and outcome == "NO")
                    )
                    rows.append({
                        "slot_start_utc":  slot_start.isoformat(),
                        "slot_end_utc":    slot_end.isoformat(),
                        "activo":          activo,
                        "ventana_min":     ventana_min,
                        "strategy":        "UPDOWN_GBM",
                        "decision":        gbm["decision"],
                        "outcome_real":    outcome,
                        "acierto":         acierto,
                        "pnl_neto":        _pnl(gbm["decision"], outcome),
                        "prob_yes_modelo": round(gbm["p_up"], 4),
                        "edge_neto":       round(gbm["edge_neto"], 4),
                        "drift_60min":     gbm["drift_60min"],
                        "drift_15min":     gbm["drift_15min"],
                        "sigma_h":         round(gbm["sigma_h"], 6),
                        "pct_spot_vs_ref": gbm["pct"],
                        "delta_ratio":     "",
                    })
                    n_gbm += 1

                # ── ORDER_FLOW (solo 5min, pares no blacklisted) ──────────
                if ventana_min == 5 and activo in pairs_of:
                    of = simulate_order_flow(
                        klines_raw, slot_start, slot_end,
                        delta_min=delta_min, delta_max=delta_max,
                    )
                    if of:
                        acierto = int(
                            (of["decision"] == "BUY_YES" and outcome == "YES") or
                            (of["decision"] == "BUY_NO"  and outcome == "NO")
                        )
                        rows.append({
                            "slot_start_utc":  slot_start.isoformat(),
                            "slot_end_utc":    slot_end.isoformat(),
                            "activo":          activo,
                            "ventana_min":     ventana_min,
                            "strategy":        "ORDER_FLOW_5M",
                            "decision":        of["decision"],
                            "outcome_real":    outcome,
                            "acierto":         acierto,
                            "pnl_neto":        _pnl(of["decision"], outcome),
                            "prob_yes_modelo": round(of["p_up"], 4),
                            "edge_neto":       round(of["edge_neto"], 4),
                            "drift_60min":     "",
                            "drift_15min":     "",
                            "sigma_h":         "",
                            "pct_spot_vs_ref": "",
                            "delta_ratio":     of["delta_ratio"],
                        })
                        n_of += 1

            if total_slots % 10000 == 0 and total_slots > 0:
                print(f"    Slots procesados: {total_slots}  GBM={n_gbm}  OF={n_of}  skip={n_skip}", flush=True)

    # Guardar
    with open(RESULTS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=RESULTS_HEADER)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n  ✓ {len(rows)} predicciones → {RESULTS_FILE}")
    print(f"    GBM: {n_gbm}  ORDER_FLOW: {n_of}  slots_sin_datos: {n_skip}")
    return rows


_klines_mem: dict = {}

def _load_cache(activo, date_str):
    key = f"{date_str}_{activo}"
    if key not in _klines_mem:
        p = DIR_KLINES / f"{key}.json"
        _klines_mem[key] = json.load(open(p)) if p.exists() else []
    return _klines_mem[key]


# ── FASE 3: Calibración ───────────────────────────────────────────────────────

def _ic(wins, n, n_ref=50):
    return ((wins + 1) / (n + 2) - 0.5) * min(1.0, n / n_ref)


def phase3_calibrate(rows=None):
    print("\n=== FASE 3: Calibración ===")

    if rows is None:
        if not RESULTS_FILE.exists():
            print("  ERROR: ejecuta fase 2 primero.")
            return {}
        rows = list(csv.DictReader(open(RESULTS_FILE)))

    rows = [r for r in rows if r.get("decision") not in ("", "SKIP", None)]
    print(f"  Filas con decisión: {len(rows)}")

    gbm_rows = [r for r in rows if r["strategy"] == "UPDOWN_GBM"]
    of_rows  = [r for r in rows if r["strategy"] == "ORDER_FLOW_5M"]

    # ── 3a. IC por subtipo ────────────────────────────────────────────────
    print("\n── IC por subtipo GBM ──")
    by_st = defaultdict(lambda: {"n": 0, "w": 0, "pnl": 0.0})
    for r in gbm_rows:
        k = f"{r['activo']}#{r['ventana_min']}min"
        by_st[k]["n"] += 1
        by_st[k]["w"] += int(r["acierto"])
        by_st[k]["pnl"] += float(r["pnl_neto"])
    for k, d in sorted(by_st.items(), key=lambda x: -x[1]["pnl"]):
        ic = _ic(d["w"], d["n"])
        print(f"    {k:20s}  {d['w']:5d}/{d['n']:5d} ({d['w']/d['n']*100:.0f}%)  IC={ic:+.3f}  PNL={d['pnl']:+.1f}€")

    # ── 3b. Grid search DRIFT_DAMPING ─────────────────────────────────────
    print("\n── Grid search DRIFT_DAMPING (GBM, todos los subtypes) ──")
    gbm15 = [r for r in gbm_rows
             if str(r["ventana_min"]) == "15"
             and r["drift_60min"] not in ("", None)
             and r["sigma_h"]     not in ("", None)
             and r["pct_spot_vs_ref"] not in ("", None)]
    print(f"  GBM #15min con features completas: {len(gbm15)}")

    best_dd = (0.25, -999)
    for dd in [x * 0.05 for x in range(0, 21)]:
        wins = n = 0
        for r in gbm15:
            try:
                drift_60 = float(r["drift_60min"]) / 100
                sigma_h  = float(r["sigma_h"])
                pct      = float(r["pct_spot_vs_ref"])
                T_h      = float(r["ventana_min"]) / 60
                mu_h     = drift_60 * dd
                sot_ref  = 1 + pct / 100
                sigma_T  = sigma_h * math.sqrt(T_h)
                if sigma_T < 1e-9:
                    continue
                d2       = (math.log(sot_ref) + mu_h * T_h) / sigma_T
                p_new    = _norm_cdf(d2)
                dec_new  = "BUY_YES" if p_new > 0.5 else "BUY_NO"
                if abs(p_new - 0.5) - EDGE_MINIMO - SLIPPAGE_ESTIMADO <= 0:
                    continue
                wins += int((dec_new == "BUY_YES" and r["outcome_real"] == "YES") or
                            (dec_new == "BUY_NO"  and r["outcome_real"] == "NO"))
                n += 1
            except Exception:
                continue
        if n > 20:
            ic = _ic(wins, n)
            if ic > best_dd[1]:
                best_dd = (dd, ic)
            print(f"    dd={dd:.2f}  n={n:6d}  {wins}/{n} ({wins/n*100:.0f}%)  IC={ic:+.4f}"
                  + (" ← ✅ MEJOR" if dd == best_dd[0] else ""))

    print(f"\n  → DRIFT_DAMPING óptimo: {best_dd[0]:.2f}  IC={best_dd[1]:+.4f}")

    # ── 3c. Grid search ORDER_FLOW delta por par ──────────────────────────
    print("\n── Grid search ORDER_FLOW DELTA por par ──")
    best_of = {}
    for activo in [p for p in PAIRS_GBM if p not in ORDER_FLOW_PAIR_BLACKLIST]:
        subset = [r for r in of_rows if r["activo"] == activo and r["delta_ratio"] not in ("", None)]
        if len(subset) < 30:
            print(f"    {activo}: insuficiente (n={len(subset)})")
            continue

        best = (0.38, 0.46, -999, 0)
        for dmin in [x * 0.02 for x in range(15, 30)]:      # 0.30→0.58
            for dmax in [dmin + 0.02 * k for k in range(1, 12)]:  # +0.02→+0.22
                if dmax > 0.70:
                    break
                wins = n = 0
                for r in subset:
                    delta = abs(float(r["delta_ratio"]))
                    if dmin <= delta <= dmax:
                        wins += int(r["acierto"])
                        n += 1
                if n < 30:
                    continue
                ic = _ic(wins, n)
                if ic > best[2]:
                    best = (dmin, dmax, ic, n)

        best_of[activo] = best
        print(f"    {activo:6s}  [{best[0]:.2f},{best[1]:.2f}]  n={best[3]:5d}  IC={best[2]:+.3f}")

    # ── 3d. H-REGIMEN 90 días ─────────────────────────────────────────────
    print("\n── H-REGIMEN 90 días (GBM #15min) ──")
    g15 = [r for r in gbm_rows if str(r["ventana_min"]) == "15"]
    for side in ["BUY_YES", "BUY_NO"]:
        sub = [r for r in g15 if r["decision"] == side]
        if sub:
            w = sum(int(r["acierto"]) for r in sub)
            ic = _ic(w, len(sub))
            print(f"    {side}: {w}/{len(sub)} ({w/len(sub)*100:.0f}%)  IC={ic:+.3f}")

    print("\n  BUY_YES #15min por cuartil de drift_60min:")
    yes15 = sorted(
        [(float(r["drift_60min"]), int(r["acierto"])) for r in g15
         if r["decision"] == "BUY_YES" and r["drift_60min"] not in ("", None)],
        key=lambda x: x[0]
    )
    if yes15:
        q = len(yes15) // 4
        for i in range(4):
            chunk = yes15[i*q:(i+1)*q] if i < 3 else yes15[i*q:]
            w2 = sum(a for d, a in chunk)
            n2 = len(chunk)
            print(f"    Q{i+1} drift=[{chunk[0][0]:+.2f},{chunk[-1][0]:+.2f}]"
                  f"  {w2}/{n2} ({w2/n2*100:.0f}%)")

    # ── 3e. H-OVERDRIFT: BUY_YES drift > 0.55%/h ─────────────────────────
    print("\n── H-OVERDRIFT ──")
    overdrift = [(float(r["drift_60min"]), int(r["acierto"])) for r in g15
                 if r["decision"] == "BUY_YES" and r["drift_60min"] not in ("", None)
                 and float(r["drift_60min"]) > 0.55]
    if overdrift:
        w = sum(a for _, a in overdrift)
        n = len(overdrift)
        ic = _ic(w, n)
        print(f"  drift>0.55, BUY_YES: {w}/{n} ({w/n*100:.0f}%)  IC={ic:+.3f}")
        if n >= 30:
            verdict = "CONFIRMADA ✅" if w / n < 0.45 else "NO confirmada"
            print(f"  → H-OVERDRIFT {verdict}")
        else:
            print(f"  → Insuficiente (n={n}<30), pendiente más datos")

    # ── 3f. H-60MIN: ¿persiste IC positivo en 60min con más datos? ────────
    print("\n── H-60MIN (60min global) ──")
    g60 = [r for r in gbm_rows if str(r["ventana_min"]) == "60"]
    if g60:
        w = sum(int(r["acierto"]) for r in g60)
        ic = _ic(w, len(g60))
        print(f"  GBM #60min global: {w}/{len(g60)} ({w/len(g60)*100:.0f}%)  IC={ic:+.3f}")
        by_pair = defaultdict(lambda: {"n": 0, "w": 0})
        for r in g60:
            by_pair[r["activo"]]["n"] += 1
            by_pair[r["activo"]]["w"] += int(r["acierto"])
        for a, d in sorted(by_pair.items()):
            ic_p = _ic(d["w"], d["n"])
            print(f"    {a}: {d['w']}/{d['n']} ({d['w']/d['n']*100:.0f}%)  IC={ic_p:+.3f}")

    # ── 3g. REGIME_THRESHOLD óptimo ───────────────────────────────────────
    print("\n── Grid search REGIME_THRESHOLD (GBM #15min) ──")
    best_rt = (0.55, -999)
    for rt in [x * 0.1 for x in range(3, 20)]:
        wins = n = 0
        for r in g15:
            try:
                drift = float(r["drift_60min"])
                dec   = r["decision"]
                bullish = (dec == "BUY_YES")
                if (drift >  rt and not bullish) or (drift < -rt and bullish):
                    continue  # filtrado por regime
                wins += int(r["acierto"])
                n += 1
            except Exception:
                continue
        if n > 20:
            ic = _ic(wins, n)
            if ic > best_rt[1]:
                best_rt = (rt, ic)
            if rt in [0.3, 0.5, 0.55, 0.7, 1.0, 1.5]:
                print(f"    rt={rt:.1f}  n={n:6d}  {wins}/{n} ({wins/n*100:.0f}%)  IC={ic:+.4f}")

    print(f"\n  → REGIME_THRESHOLD óptimo: {best_rt[0]:.1f}  IC={best_rt[1]:+.4f}")

    # ── Guardar ───────────────────────────────────────────────────────────
    result = {
        "timestamp":              datetime.now(UTC).isoformat(),
        "n_total":                len(rows),
        "drift_damping_optimo":   best_dd[0],
        "drift_damping_ic":       best_dd[1],
        "regime_threshold_optimo": best_rt[0],
        "regime_threshold_ic":    best_rt[1],
        "order_flow_por_par": {
            a: {"delta_min": v[0], "delta_max": v[1], "ic": v[2], "n": v[3]}
            for a, v in best_of.items()
        },
    }
    json.dump(result, open(CALIB_FILE, "w"), indent=2)
    print(f"\n  ✓ Guardado en {CALIB_FILE}")
    return result


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days",  type=int, default=90)
    parser.add_argument("--phase", default="all", help="1=klines, 2=simulacion, 3=calibracion, all")
    parser.add_argument("--pairs", default=",".join(PAIRS_GBM))
    parser.add_argument("--drift-damping", type=float, default=0.00)
    parser.add_argument("--regime-threshold", type=float, default=999.0)
    args = parser.parse_args()

    pairs = [p.strip().upper() for p in args.pairs.split(",")]
    pairs_of = [p for p in pairs if p not in ORDER_FLOW_PAIR_BLACKLIST]
    phase = args.phase.lower()

    print(f"[backfill] days={args.days} phase={phase} pairs={pairs} dd={args.drift_damping} rt={args.regime_threshold}")
    t0 = time.time()
    rows = None

    if phase in ("1", "all"):
        phase1_klines(args.days, pairs)

    if phase in ("2", "all"):
        rows = phase2_simulate(args.days, pairs, pairs_of,
                               drift_damping=args.drift_damping,
                               regime_threshold=args.regime_threshold)

    if phase in ("3", "all"):
        phase3_calibrate(rows)

    print(f"\n[backfill] Completado en {time.time()-t0:.0f}s ({(time.time()-t0)/60:.1f}min)")


if __name__ == "__main__":
    main()
