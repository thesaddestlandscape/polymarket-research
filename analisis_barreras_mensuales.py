#!/usr/bin/env python3
"""analisis_barreras_mensuales.py -- mercados mensuales "¿qué precio tocará BTC/ETH/SOL/XRP?" (ronda 2 #5).
Son los mercados cripto más profundos de Polymarket (decenas de millones de USD por mes). Pregunta: ¿el precio del
mercado está bien calibrado, y un modelo de barrera con volatilidad realizada lo mejora?

Datos (recogidos por /root/polymarket-research-datalogs/analisis_persistente_30sep/barreras_collect.py): cada strike
con su desenlace oficial y su historia de precio cada 6 h, más velas de 1 h de Binance. OJO: la historia del CLOB es
precio MEDIO/último, no ask; aquí el spread es de 0,1-2c, así que se cobra 1c de cruce + la comisión 7 % x (1-precio).

Por cada mercado y cada punto de la historia en que la barrera AÚN no se ha tocado:
  modelo = P(tocar K antes de fin de mes) con movimiento browniano geométrico sin deriva real (mu = -sigma²/2) y
  sigma = volatilidad realizada de las 336 h previas.
A) Calibración del mercado por tramo de precio.  B) Brier mercado vs modelo.  C) Estrategia: PRIMERA vez que
modelo - mercado supera el umbral se entra (una sola entrada por mercado) y se lleva a resolución.
La unidad independiente es el activo-mes (todos los strikes de un mes caen juntos): IC90 por activo-mes.
Solo lectura. Uso: analisis_barreras_mensuales.py
"""
import bisect
import collections
import math
import pickle
import random
import sys
from datetime import datetime

DIR = "/root/polymarket-research-datalogs/analisis_persistente_30sep"
SYM = {"bitcoin": "BTCUSDT", "ethereum": "ETHUSDT", "solana": "SOLUSDT", "xrp": "XRPUSDT"}
FEE, CRUCE = 0.07, 0.01


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def p_tocar(s, k, sig_h, horas, arriba):
    """P(máx >= K) (o mín <= K) en `horas` para GBM con mu = -sig²/2 por hora."""
    if horas <= 0 or sig_h <= 0:
        return 0.0
    b = math.log(k / s) if arriba else math.log(s / k)
    if b <= 0:
        return 1.0
    mu = (-0.5 * sig_h ** 2) * (1 if arriba else -1)
    sd = sig_h * math.sqrt(horas)
    return min(1.0, phi((-b + mu * horas) / sd) + math.exp(2 * mu * b / sig_h ** 2) * phi((-b - mu * horas) / sd))


def ic(por_cl):
    ks = [k for k in por_cl if por_cl[k]]
    if len(ks) < 5:
        return None
    rng, ms = random.Random(4), []
    for _ in range(1000):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in por_cl[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return ms[50], ms[949]


def main() -> int:
    mk = pickle.load(open(f"{DIR}/barreras.pkl", "rb"))
    kl = pickle.load(open(f"{DIR}/barreras_klines.pkl", "rb"))
    idx = {s: ([r[0] for r in v], v) for s, v in kl.items()}
    pts, n_mk = [], 0
    for m in mk:
        if m["yes"] is None or not m["h"] or m["K"] <= 0:
            continue
        ts, v = idx[SYM[m["asset"]]]
        t_ini = datetime.fromisoformat(m["start"].replace("Z", "+00:00")).timestamp()
        t_fin = datetime.fromisoformat(m["end"].replace("Z", "+00:00")).timestamp()
        arriba = m["dir"] == "up"
        n_mk += 1
        cl = f"{m['asset']}|{m['slug']}"
        for t, p in m["h"]:
            if t < t_ini + 3600 or t > t_fin - 6 * 3600:
                continue
            i = bisect.bisect_right(ts, t) - 1
            i0 = bisect.bisect_left(ts, t_ini)
            if i < 340 or i <= i0:
                continue
            tramo = v[i0:i + 1]
            if (arriba and max(r[2] for r in tramo) >= m["K"]) or (not arriba and min(r[3] for r in tramo) <= m["K"]):
                break                                   # ya tocada: el mercado está decidido
            s = v[i][4]
            rets = [math.log(v[j][4] / v[j - 1][4]) for j in range(i - 335, i + 1)]
            sig = math.sqrt(sum(r * r for r in rets) / len(rets))
            pts.append(dict(cl=cl, id=m["q"] + m["slug"], t=t, p=p, mod=p_tocar(s, m["K"], sig, (t_fin - t) / 3600, arriba),
                            yes=m["yes"], arriba=arriba, dias=(t_fin - t) / 86400, asset=m["asset"]))
    cls = {x["cl"] for x in pts}
    print(f"{n_mk} mercados con desenlace, {len(pts)} puntos (barrera aún sin tocar), {len(cls)} activo-mes")

    print("\nA) CALIBRACIÓN DEL MERCADO (todos los puntos)\n tramo_precio      n   precio_medio  frec_YES  modelo_medio   diferencia(frec-precio) IC90 por activo-mes")
    for lo, hi in ((0.02, 0.05), (0.05, 0.10), (0.10, 0.20), (0.20, 0.35), (0.35, 0.50), (0.50, 0.65), (0.65, 0.80), (0.80, 0.95)):
        s = [x for x in pts if lo <= x["p"] < hi]
        if len(s) < 30:
            continue
        pc = collections.defaultdict(list)
        for x in s:
            pc[x["cl"]].append(x["yes"] - x["p"])
        i90 = ic(pc)
        print(f" [{lo:.2f},{hi:.2f})  {len(s):6d}     {sum(x['p'] for x in s) / len(s):.3f}      {sum(x['yes'] for x in s) / len(s):.3f}      "
              f"{sum(x['mod'] for x in s) / len(s):.3f}        {sum(x['yes'] - x['p'] for x in s) / len(s):+.3f}  {'(%+.3f,%+.3f)' % i90 if i90 else '-'}  [{len(pc)} act-mes]")
    for nombre, f in (("sube ↑", lambda x: x["arriba"]), ("baja ↓", lambda x: not x["arriba"])):
        s = [x for x in pts if f(x) and 0.05 <= x["p"] < 0.95]
        pc = collections.defaultdict(list)
        for x in s:
            pc[x["cl"]].append(x["yes"] - x["p"])
        print(f" {nombre}: n={len(s)} frec-precio {sum(x['yes'] - x['p'] for x in s) / len(s):+.4f} IC90 {ic(pc)}")

    s = [x for x in pts if 0.03 <= x["p"] <= 0.97]
    print(f"\nB) BRIER (menor es mejor), {len(s)} puntos: mercado {sum((x['p'] - x['yes']) ** 2 for x in s) / len(s):.4f} | "
          f"modelo {sum((x['mod'] - x['yes']) ** 2 for x in s) / len(s):.4f} | media 50/50 {sum(((x['p'] + x['mod']) / 2 - x['yes']) ** 2 for x in s) / len(s):.4f}")

    print("\nC) ESTRATEGIA: primera vez que |modelo - mercado| >= umbral, una entrada por mercado, a resolución (1c de cruce + fee)")
    print(" umbral  lado            n   act-mes  acierto  precio  EV por €   IC90 por activo-mes      act-mes en positivo")
    for thr in (0.05, 0.10, 0.15, 0.25):
        for lado in ("YES", "NO", "ambos"):
            visto, pc, res = set(), collections.defaultdict(list), []
            for x in sorted(pts, key=lambda z: z["t"]):
                if x["id"] in visto or not 0.05 <= x["p"] <= 0.95:
                    continue
                d = x["mod"] - x["p"]
                if d >= thr and lado in ("YES", "ambos"):
                    px, gana = min(0.99, x["p"] + CRUCE), x["yes"] == 1
                elif d <= -thr and lado in ("NO", "ambos"):
                    px, gana = min(0.99, 1 - x["p"] + CRUCE), x["yes"] == 0
                else:
                    continue
                visto.add(x["id"])
                pnl = (1 / px - 1 if gana else -1.0) - FEE * (1 - px)
                pc[x["cl"]].append(pnl)
                res.append((gana, px, pnl))
            if len(res) < 20:
                continue
            i90 = ic(pc)
            print(f"  {thr:.2f}   {lado:6s}     {len(res):5d}   {len(pc):4d}     {sum(r[0] for r in res) / len(res):.3f}   {sum(r[1] for r in res) / len(res):.3f}   "
                  f"{sum(r[2] for r in res) / len(res):+.4f}   {'(%+.3f,%+.3f)' % i90 if i90 else '-':20s}   {sum(1 for v in pc.values() if sum(v) > 0)}/{len(pc)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
