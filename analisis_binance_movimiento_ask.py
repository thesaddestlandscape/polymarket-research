#!/usr/bin/env python3
"""analisis_binance_movimiento_ask.py -- lee binance_movimiento_ask_fase0 (movimientos de Binance >=1 bps en 1 s) y mide
el EV por € de COMPRAR el lado del movimiento al ask REAL del libro (histórico ms de libro_estado_ws) en cada offset,
reteniendo a resolución, con DESENLACE OFICIAL (gamma, closed=true; se informa la cobertura). Fee 0,07·p·(1-p)/share.

Offset 0 = libro ANTES de poder reaccionar (referencia, no ejecutable); 0,15/0,3 = tomador perfecto; 0,6 = nuestra
latencia realista (Binance→Helsinki ~130 ms + proceso + orden + taker delay 150 ms). Edad del libro alta = libro
quieto o hueco del WebSocket (no distinguibles): se informa con y sin filtro EDAD_MAX_MS.

Uso: python3 analisis_binance_movimiento_ask.py [--offset 0.6] [--desde YYYY-MM-DD]
Solo lectura. Gate de cualquier celda (no se mira aquí): n>=40 mercados, >=5 días, EV>=+0,10, IC90 por días >0.
"""
import argparse
import csv
import glob
import gzip
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_precierre_rejilla_ask_real import desenlaces  # noqa: E402

DATALOGS = "/root/polymarket-research-datalogs"
FEE = 0.07
EDAD_MAX_MS = 5000
ESCALA = {"BTC": 1.0, "ETH": 1.2, "SOL": 1.6, "XRP": 1.6, "DOGE": 2.0, "BNB": 1.2}   # umbral en bps de cada moneda


def ev(win, a):
    return (1.0 / a if win else 0.0) - 1.0 - FEE * (1 - a)


def ic90_dias(por_dia):
    ks = [k for k in por_dia if por_dia[k]]
    if len(ks) < 3:
        return None
    rng, ms = random.Random(7), []
    for _ in range(1000):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return round(ms[50], 3), round(ms[950], 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offset", default="0.6")
    ap.add_argument("--desde", default="")
    a = ap.parse_args()
    s_off = a.offset.replace(".", "")
    filas = []
    for f in sorted(glob.glob(f"{DATALOGS}/binance_movimiento_ask_*.csv*")):
        if a.desde and f.split("_")[-1][:10] < a.desde:
            continue
        op = gzip.open if f.endswith(".gz") else open
        with op(f, "rt") as fh:
            filas += list(csv.DictReader(fh))
    if not filas:
        print("sin datos")
        return
    des = desenlaces({r["slug"] for r in filas})
    res = [r for r in filas if r["slug"] in des]
    print(f"filas {len(filas)}, con desenlace oficial {len(res)} ({len(res) / len(filas) * 100:.1f} %; el resto, mercados aún abiertos)")
    cel = defaultdict(lambda: defaultdict(list))
    deriva = defaultdict(list)
    for r in res:
        try:
            ask = float(r[f"ask_{s_off}"])
            edad = float(r[f"edad_ms_{s_off}"])
            a0 = float(r["ask_00"])
        except (ValueError, KeyError):
            continue
        if not (0.02 <= ask <= 0.98):
            continue
        win = des[r["slug"]] == r["direccion"]
        bps = abs(float(r["ret_1s"])) * 1e4 / ESCALA.get(r["activo"], 1.0)
        tam = "1-1.5" if bps < 1.5 else "1.5-2.5" if bps < 2.5 else ">=2.5"
        banda = f"{int(ask * 10) / 10:.1f}"
        dia = datetime.fromtimestamp(int(r["ts_ms"]) / 1000, timezone.utc).strftime("%m-%d")
        v = ev(win, ask)
        for clave in [("TOTAL",), (r["marco"],), (r["activo"], r["marco"]), (r["activo"], r["marco"], tam),
                      (r["marco"], tam, "ask" + banda)]:
            cel[clave + (("todas",))][dia].append(v)
            if edad <= EDAD_MAX_MS:
                cel[clave + (("edad<5s",))][dia].append(v)
        deriva[(r["activo"], r["marco"])].append(ask - a0)
    print(f"\nEV por € al ask a +{a.offset} s (retener a resolución, neto de fee). n = eventos (dedup 3 s por moneda)")
    print(f"{'celda':52s} {'n':>6s} {'días':>4s} {'EV':>7s}  IC90 por días")
    for k in sorted(cel, key=lambda k: (len(k), k)):
        pd = cel[k]
        xs = [x for d in pd.values() for x in d]
        if len(xs) < 15:
            continue
        print(f"{' | '.join(k):52s} {len(xs):6d} {len(pd):4d} {sum(xs) / len(xs):+7.3f}  {ic90_dias(pd)}")
    print(f"\nDeriva media del ask entre 0 y +{a.offset} s (c):")
    for k in sorted(deriva):
        xs = deriva[k]
        print(f"  {k[0]:5s} {k[1]:4s} n={len(xs):5d}  {sum(xs) / len(xs) * 100:+.2f}c")


if __name__ == "__main__":
    main()
