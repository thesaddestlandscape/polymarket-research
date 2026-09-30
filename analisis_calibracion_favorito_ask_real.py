#!/usr/bin/env python3
"""analisis_calibracion_favorito_ask_real.py -- ¿está el favorito bien puesto de precio? Calibración del MERCADO al
ask real, por marco x tiempo restante x tramo de ask, con 21 días (30-Sep).

Motivo: todas las pistas con edge del 30-Sep caen en 15 minutos y en favoritos caros (precierre 15m ask 0,80-0,95,
cierre 15m ask 0,90-0,97, copia de tomadoras 15m 0,80-0,95) y ninguna en 5 minutos, pero salen de 6 días. Aquí se
comprueba con una fuente independiente y más larga, sin modelo ni señal propia: libro_ambos_lados (foto de ambos
lados de cada up/down de 5/15/60 min cada ~1-2 min, 10-30 Sep) + desenlace oficial. Por cada mercado y tramo de
tiempo restante se toma la PRIMERA foto y se compra el lado más caro (el favorito) a su ask.
Comisión real 7 % x (1 - precio). Sin profundidad (la fuente no la trae): cota optimista de ejecución.
IC90 por días. Solo lectura. Uso: analisis_calibracion_favorito_ask_real.py
"""
import collections
import csv
import glob
import gzip
import json
import random
import sys
from pathlib import Path

import requests

DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE = DATALOGS / "desenlaces_por_market_id_cache.json"
FEE = 0.07
RESTO = ((0, 30), (30, 60), (60, 120), (120, 300), (300, 900), (900, 3600))
ASK = ((0.50, 0.60), (0.60, 0.70), (0.70, 0.80), (0.80, 0.90), (0.90, 0.95), (0.95, 0.99))


def desenlaces(ids) -> dict:
    try:
        c = json.loads(CACHE.read_text())
    except Exception:
        c = {}
    pend = sorted(i for i in set(ids) if i not in c)
    ses = requests.Session()
    for k in range(0, len(pend), 40):
        try:
            for m in ses.get("https://gamma-api.polymarket.com/markets", timeout=25,
                             params=[("id", i) for i in pend[k:k + 40]] + [("closed", "true"), ("limit", "40")]).json() or []:
                pr = m.get("outcomePrices")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999:
                    c[str(m["id"])] = "YES"
                elif pr and float(pr[1]) >= 0.999:
                    c[str(m["id"])] = "NO"
        except Exception as e:
            print(f"lote {k // 40}: {type(e).__name__}", file=sys.stderr)
        if k % 4000 == 0 and k:
            CACHE.write_text(json.dumps(c))
    if pend:
        CACHE.write_text(json.dumps(c))
    return c


def ic90(pd):
    ks = [k for k in pd if pd[k]]
    if len(ks) < 5:
        return None
    rng, ms = random.Random(6), []
    for _ in range(800):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in pd[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return ms[40], ms[759]


def main() -> int:
    obs, vistos = [], set()
    for f in sorted(glob.glob(str(DATALOGS / "libro_ambos_lados_*.csv*"))):
        dia = f.split("libro_ambos_lados_")[1][:10]
        fh = gzip.open(f, "rt", encoding="utf-8", newline="") if f.endswith(".gz") else open(f, encoding="utf-8", newline="")
        with fh:
            for r in csv.DictReader(fh):
                try:
                    resto, ay, an = float(r["restante_s"]), float(r["ask_yes"]), float(r["ask_no"])
                except (ValueError, TypeError):
                    continue
                tr = next((i for i, (lo, hi) in enumerate(RESTO) if lo <= resto < hi), None)
                if tr is None or (r["market_id"], tr) in vistos:
                    continue
                vistos.add((r["market_id"], tr))
                lado, a = ("YES", ay) if ay >= an else ("NO", an)
                if 0.50 <= a < 0.99:
                    obs.append((dia, r["marco"], r["activo"], r["market_id"], tr, lado, a))
    gan = desenlaces(o[3] for o in obs)
    n_m = len({o[3] for o in obs})
    print(f"{len(obs)} observaciones, {n_m} mercados, {sum(1 for m in {o[3] for o in obs} if m in gan)} con desenlace oficial, "
          f"{len({o[0] for o in obs})} días")
    for marco in ("5min", "15min", "60min"):
        print(f"\n===== {marco}: comprar el FAVORITO al ask =====\n restante_s   ask            n    /día  acierto  ask_medio   EV por €   IC90 por días      días+")
        for tr, (lo, hi) in enumerate(RESTO):
            for alo, ahi in ASK:
                v = [(o[0], 1 if gan[o[3]] == o[5] else 0, o[6]) for o in obs if o[1] == marco and o[4] == tr and alo <= o[6] < ahi and o[3] in gan]
                if len(v) < 40:
                    continue
                pd = collections.defaultdict(list)
                for d, ok, a in v:
                    pd[d].append(ok / a - 1 - FEE * (1 - a))
                x = [y for z in pd.values() for y in z]
                i90 = ic90(pd)
                marca = "  <==" if i90 and i90[0] > 0 else ""
                print(f" [{lo:4d},{hi:4d})  [{alo:.2f},{ahi:.2f})  {len(v):5d}  {len(v) / len(pd):5.1f}   {sum(o[1] for o in v) / len(v):.3f}    "
                      f"{sum(o[2] for o in v) / len(v):.3f}    {sum(x) / len(x):+.4f}   {'(%+.3f,%+.3f)' % i90 if i90 else '-':18s} "
                      f"{sum(1 for z in pd.values() if sum(z) > 0)}/{len(pd)}{marca}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
