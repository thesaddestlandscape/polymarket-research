#!/usr/bin/env python3
"""analisis_tomador_60m_binance.py -- TOMADOR de 60 min con la regla FIJADA el 05-Oct (antes de mirar datos).

Los mercados Up/Down de 60 min resuelven con la vela 1H de Binance (cierre >= apertura gana Up). Regla:
en T-5, T-4, T-3, T-2 y T-1 min, z = ln(S/O) / (sigma_1m * sqrt(min restantes)), con S = mid de Binance
(bookTicker del registro ms, hora de recepción), O = apertura oficial de la vela 1H (klines REST de Binance)
y sigma_1m = desviación típica de los log-retornos de 1 min de los 120 min previos. Se compra el lado
favorecido si Phi(|z|) - ask >= 0,05, con el ask del registro ms (filas q, hora de RECEPCIÓN) a la decisión
+ LAT ms. Una entrada por mercado (el primer instante que dispara). PnL por EUR al ask, fee 0,07*(1-p) por
EUR, desenlace OFICIAL (gamma closed=true; cobertura impresa). sigma de 120 min es la única elección libre
y se fija aquí, sin barrer.

Uso: python3 analisis_tomador_60m_binance.py --desde 2026-10-05 [--lat 250]
"""
import argparse
import bisect
import csv
import glob
import gzip
import math
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
FEE = 0.07
OFFSETS_MIN = (5, 4, 3, 2, 1)
UMBRAL = 0.05
SIM = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def klines(sym, interval, t0_ms, t1_ms):
    out, t = [], t0_ms
    while t < t1_ms:
        r = requests.get("https://api.binance.com/api/v3/klines", timeout=20,
                         params={"symbol": sym, "interval": interval, "startTime": int(t), "endTime": int(t1_ms),
                                 "limit": 1000}).json()
        if isinstance(r, dict):
            raise RuntimeError(f"Binance klines {sym} {interval}: {r}")
        if not r:
            break
        out += r
        t = r[-1][0] + 1
        if len(r) < 1000:
            break
    return out


def leer(desde, hasta):
    """-> meta[token]=(moneda, mid, cierre_ms, lado); asks[token]=([t_recv], [ask]); bin[sym]=([t], [mid])"""
    meta, asks, bt = {}, defaultdict(lambda: ([], [])), defaultdict(lambda: ([], []))
    fich = sorted(f for f in glob.glob(str(DL / "maker_ms_*.csv.gz"))
                  if desde <= Path(f).name[9:19] <= hasta)
    for f in fich:
        try:
            with gzip.open(f, "rt") as fh:
                for ln in fh:
                    c = ln.rstrip("\n").split(",")
                    tp = c[0]
                    if tp == "k" and c[4] == "60min":
                        cierre = datetime.fromisoformat(c[6]).timestamp() * 1000
                        meta[c[2]] = (c[3], c[5], cierre, c[7])
                    elif tp == "q" and c[2] in meta and c[4] not in ("", "None"):
                        a = asks[c[2]]
                        a[0].append(int(c[7]) if c[7] else int(c[1]))
                        a[1].append(float(c[4]))
                    elif tp == "b":
                        b = bt[c[2]]
                        b[0].append(int(c[1]))
                        b[1].append((float(c[3]) + float(c[4])) / 2)
        except (EOFError, OSError) as e:
            print(f"  aviso: {Path(f).name} truncado ({type(e).__name__}); se usa lo leído", file=sys.stderr)
    for d in (asks, bt):
        for k, (t, v) in d.items():
            o = sorted(range(len(t)), key=t.__getitem__)
            d[k] = ([t[i] for i in o], [v[i] for i in o])
    return meta, asks, bt


def ultimo(serie, t):
    ts, vs = serie
    i = bisect.bisect_right(ts, t) - 1
    return (ts[i], vs[i]) if i >= 0 else (None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta", default="2099-12-31")
    ap.add_argument("--lat", type=int, default=250)
    a = ap.parse_args()
    meta, asks, bt = leer(a.desde, a.hasta)
    mercados = defaultdict(dict)
    for tok, (mon, mid, cierre, lado) in meta.items():
        mercados[(mon, mid, cierre)][lado] = tok
    if not mercados:
        print("sin mercados de 60 min en el registro")
        return
    t_min = min(k[2] for k in mercados) - 3 * 3600_000
    t_max = max(k[2] for k in mercados)
    k1h, k1m = {}, {}
    for mon in {k[0] for k in mercados}:
        k1h[mon] = {int(r[0]): float(r[1]) for r in klines(SIM[mon], "1h", t_min, t_max)}
        r = klines(SIM[mon], "1m", t_min, t_max)
        k1m[mon] = ([int(x[0]) for x in r], [float(x[4]) for x in r])
    out = desenlaces([k[1] for k in mercados])
    filas, sin_datos, sin_des, mejor = [], 0, 0, []
    ahora = datetime.now(timezone.utc).timestamp() * 1000
    mercados = {k: v for k, v in mercados.items() if k[2] < ahora - 120_000}
    for (mon, mid, cierre), toks in mercados.items():
        if "YES" not in toks or "NO" not in toks:
            continue
        mejor_m = None
        apertura = cierre - 3600_000
        O = k1h[mon].get(int(apertura))
        bins = bt.get(SIM[mon])
        if O is None or not bins:
            sin_datos += 1
            continue
        if mid not in out:
            sin_des += 1
            continue
        for off in OFFSETS_MIN:
            td = cierre - off * 60_000
            tS, S = ultimo(bins, td)
            if S is None or td - tS > 5000:
                continue
            ts1, cl = k1m[mon]
            j = bisect.bisect_right(ts1, td - 60_000)
            seg = cl[max(0, j - 121):j]
            rets = [math.log(seg[i + 1] / seg[i]) for i in range(len(seg) - 1)]
            if len(rets) < 60:
                continue
            sig = st.pstdev(rets)
            if sig <= 0:
                continue
            z = math.log(S / O) / (sig * math.sqrt(off))
            lado = "YES" if z > 0 else "NO"
            tA, ask = ultimo(asks[toks[lado]], td + a.lat)
            if ask is None or td + a.lat - tA > 60_000 or not 0.01 <= ask <= 0.99:
                continue
            valor = phi(abs(z)) - ask
            mejor_m = valor if mejor_m is None else max(mejor_m, valor)
            if valor >= UMBRAL:
                gana = out[mid] == lado
                pnl = ((1 - ask) / ask if gana else -1.0) - FEE * (1 - ask)
                dia = datetime.fromtimestamp(cierre / 1000, timezone.utc).strftime("%Y-%m-%d")
                filas.append(dict(mon=mon, mid=mid, off=off, z=z, ask=ask, valor=valor, gana=gana, pnl=pnl, dia=dia,
                                  hora=datetime.fromtimestamp(cierre / 1000, timezone.utc).hour))
                break
        if mejor_m is not None:
            mejor.append(mejor_m)
    n_m = sum(1 for t in mercados.values() if len(t) == 2)
    print(f"mercados 60 min CERRADOS en el registro: {n_m} | sin vela/Binance: {sin_datos} | sin desenlace oficial: {sin_des} "
          f"(cobertura {1 - sin_des / max(1, n_m):.0%}) | disparos: {len(filas)} | latencia {a.lat} ms")
    if mejor:
        q = sorted(mejor)
        print(f"  mejor valor por mercado (n={len(q)}): p50 {q[len(q) // 2]:+.3f}  p90 {q[int(len(q) * .9)]:+.3f}  "
              f"máx {q[-1]:+.3f}")
    if not filas:
        return
    d = defaultdict(list)
    for f in filas:
        d[f["dia"]].append(f["pnl"])
    random.seed(1)
    g = list(d.values())
    b = sorted(st.mean([v for k in random.choices(g, k=len(g)) for v in k]) for _ in range(2000))
    print(f"EV {st.mean(f['pnl'] for f in filas):+.3f} por EUR | acierto {sum(f['gana'] for f in filas) / len(filas):.0%} "
          f"| ask medio {st.mean(f['ask'] for f in filas):.2f} | IC90 por días [{b[100]:+.3f}, {b[1900]:+.3f}] | días {len(d)}")
    for clave in ("mon", "off", "dia"):
        g2 = defaultdict(list)
        for f in filas:
            g2[f[clave]].append(f["pnl"])
        print(f"  por {clave}: " + "  ".join(f"{k}: n={len(v)} {st.mean(v):+.3f}" for k, v in sorted(g2.items())))
    for lo, hi in ((0.05, 0.10), (0.10, 0.20), (0.20, 1.0)):
        s = [f["pnl"] for f in filas if lo <= f["valor"] < hi]
        if s:
            print(f"  valor [{lo},{hi}): n={len(s)} EV {st.mean(s):+.3f}")


if __name__ == "__main__":
    main()
