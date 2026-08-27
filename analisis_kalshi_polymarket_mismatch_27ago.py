#!/usr/bin/env python3
"""Exploratorio 27-Ago: comparacion de nivel de precio Kalshi vs Polymarket
en el mismo instante (propuesta #1 de la lista de 10 ideas alfa 27-Ago).
V2: controla por staleness conocido de precio_yes_mercado (bug documentado
CLAUDE.md, ts calculado una vez por ciclo ~100-130s) usando drift de
Chainlink en la ventana previa a la prediccion.
Solo lectura, no toca produccion."""
import csv
import glob
from datetime import datetime, timedelta


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def cargar_kalshi15m():
    filas = []
    for f in sorted(glob.glob("data/prices/kalshi_btc15m_*.csv")):
        with open(f) as fh:
            for r in csv.DictReader(fh):
                filas.append(r)
    return filas


def cargar_chainlink():
    out = {}
    for f in sorted(glob.glob("data/prices/chainlink_*.csv")):
        with open(f) as fh:
            for r in csv.DictReader(fh):
                if r.get("asset") != "BTC":
                    continue
                try:
                    ts = parse_ts(r["timestamp_utc"])
                    px = float(r["price_usd"])
                except Exception:
                    continue
                out.setdefault(ts.date(), []).append((ts, px))
    for d in out:
        out[d].sort()
    return out


def cl_near(chainlink, ts, tol_s=20):
    dia = chainlink.get(ts.date(), [])
    mejor = None
    mejor_dist = None
    for t, p in dia:
        dist = abs((t - ts).total_seconds())
        if dist > tol_s:
            continue
        if mejor_dist is None or dist < mejor_dist:
            mejor_dist = dist
            mejor = (t, p)
    return mejor


def main():
    filas = cargar_kalshi15m()
    por_ticker = {}
    for r in filas:
        por_ticker.setdefault(r["ticker"], []).append(r)

    chainlink = cargar_chainlink()

    idx = {}
    for ticker, rs in por_ticker.items():
        rs2 = []
        close_time = None
        for r in rs:
            try:
                ts = parse_ts(r["timestamp_utc"])
                ask = float(r["yes_ask"])
                bid = float(r["yes_bid"])
                close_time = r["close_time"]
            except Exception:
                continue
            rs2.append((ts, ask, bid))
        rs2.sort()
        if rs2 and close_time:
            idx.setdefault(close_time, []).extend(rs2)
    for k in idx:
        idx[k].sort()

    rows = []
    with open("data/shadow/results.csv") as fh:
        for r in csv.DictReader(fh):
            if r.get("subtype") != "BTC#15min":
                continue
            if r.get("strategy") not in ("GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "UPDOWN_GBM_15M_TARDIO"):
                continue
            try:
                pt = parse_ts(r["prediction_timestamp"])
            except Exception:
                continue
            if pt.date() < datetime(2026, 8, 19).date():
                continue
            rows.append((pt, r))

    matches = []
    for pt, r in rows:
        end_date = r.get("end_date", "")
        candidatos_close = [end_date, end_date + ":00", end_date.replace(" ", "T")]
        serie = None
        for c in candidatos_close:
            for k in idx:
                if k.startswith(c[:16]):
                    serie = idx[k]
                    break
            if serie:
                break
        if not serie:
            continue
        mejor = None
        mejor_dist = None
        for ts, ask, bid in serie:
            dist = abs((ts - pt).total_seconds())
            if dist > 20:
                continue
            if mejor_dist is None or dist < mejor_dist:
                mejor_dist = dist
                mejor = (ts, ask, bid)
        if mejor is None:
            continue
        ts_k, ask_k, bid_k = mejor
        mid_k = (ask_k + bid_k) / 2
        try:
            px_poly = float(r["precio_yes_mercado"])
        except Exception:
            continue

        # control de staleness: drift chainlink en los ~120s previos a pt
        cl_now = cl_near(chainlink, pt, tol_s=20)
        cl_antes = cl_near(chainlink, pt - timedelta(seconds=120), tol_s=20)
        drift_pct = None
        if cl_now and cl_antes:
            drift_pct = 100 * (cl_now[1] - cl_antes[1]) / cl_antes[1]

        matches.append({
            "market_id": r["market_id"], "pt": pt,
            "px_poly": px_poly, "mid_kalshi": mid_k,
            "diff": px_poly - mid_k, "drift_pct_120s": drift_pct,
        })

    print(f"Total emparejados: {len(matches)}")
    con_drift = [m for m in matches if m["drift_pct_120s"] is not None]
    print(f"Con dato de drift Chainlink (rango 22-27 Ago): {len(con_drift)}")

    if con_drift:
        diffs_all = [m["diff"] for m in con_drift]
        n = len(diffs_all)
        media = sum(diffs_all) / n
        print(f"  [sin control] diff media={media:+.4f}  |diff|>0.04: "
              f"{sum(1 for d in diffs_all if abs(d) > 0.04)}/{n}")

        quietos = [m for m in con_drift if abs(m["drift_pct_120s"]) < 0.03]
        print(f"\n  Subconjunto con drift Chainlink <0.03% en los 120s previos (mercado 'quieto'): n={len(quietos)}")
        if quietos:
            diffs_q = [m["diff"] for m in quietos]
            nq = len(diffs_q)
            media_q = sum(diffs_q) / nq
            grandes_q = sum(1 for d in diffs_q if abs(d) > 0.04)
            print(f"    diff media={media_q:+.4f}  |diff|>0.04: {grandes_q}/{nq} ({100*grandes_q/nq:.1f}%)")
            pos = sum(1 for d in diffs_q if d > 0.04)
            neg = sum(1 for d in diffs_q if d < -0.04)
            print(f"    Polymarket mas caro: {pos}  Polymarket mas barato: {neg}")

        movidos = [m for m in con_drift if abs(m["drift_pct_120s"]) >= 0.03]
        print(f"\n  Subconjunto con drift Chainlink >=0.03% en los 120s previos (mercado 'moviendose'): n={len(movidos)}")
        if movidos:
            diffs_m = [m["diff"] for m in movidos]
            nm = len(diffs_m)
            media_m = sum(diffs_m) / nm
            grandes_m = sum(1 for d in diffs_m if abs(d) > 0.04)
            print(f"    diff media={media_m:+.4f}  |diff|>0.04: {grandes_m}/{nm} ({100*grandes_m/nm:.1f}%)")


if __name__ == "__main__":
    main()
