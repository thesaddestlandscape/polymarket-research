#!/usr/bin/env python3
"""analisis_precierre_rejilla_ask_real.py -- ¿dónde hay edge REAL en el precierre? (30-Sep, Javi: "solucionar
sniper precierre y naive").

Fuente: /root/polymarket-research-datalogs/precierre_multioffset_fase0.csv (todas las ventanas up/down, 7 instantes
T-120..T-10 s, con z del TWAP proyectado, dirección implícita y ASK REAL del lado implícito con profundidad) +
desenlace oficial por slug (gamma closed=true, caché). Comisión real: 7 % x (1 - precio) por euro, gane o pierda
(comprobado contra data/live/trades.csv).

Por marco x instante: (1) en qué % de ventanas hay ask comprable del lado que marca el TWAP; (2) acierto y EV por
€ por tramo de z x tramo de ask, con IC90 por días; (3) lo mismo por moneda en las celdas con muestra.
Solo lectura.  Uso: analisis_precierre_rejilla_ask_real.py [--desde YYYY-MM-DD]
"""
import collections
import csv
import json
import random
import sys
from pathlib import Path

import requests

SRC = Path("/root/polymarket-research-datalogs/precierre_multioffset_fase0.csv")
CACHE = Path("/root/polymarket-research-datalogs/precierre_desenlaces_cache.json")
FEE, RATIO_MIN = 0.07, 5.0
ZB = ((0, 0.5), (0.5, 1.0), (1.0, 1.8), (1.8, 3.0), (3.0, 99))
AB = ((0.05, 0.25), (0.25, 0.65), (0.65, 0.80), (0.80, 0.90), (0.90, 0.95), (0.95, 0.99))


def desenlaces(slugs) -> dict:
    try:
        c = json.loads(CACHE.read_text())
    except Exception:
        c = {}
    pend = sorted(s for s in set(slugs) if s not in c)
    ses = requests.Session()
    for k in range(0, len(pend), 40):
        try:
            for m in ses.get("https://gamma-api.polymarket.com/markets", timeout=20,
                             params=[("slug", s) for s in pend[k:k + 40]] + [("closed", "true"), ("limit", "40")]).json() or []:
                pr = m.get("outcomePrices")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999:
                    c[m["slug"]] = "Up"
                elif pr and float(pr[1]) >= 0.999:
                    c[m["slug"]] = "Down"
        except Exception as e:
            print(f"lote {k // 40}: {type(e).__name__}", file=sys.stderr)
    if pend:
        CACHE.write_text(json.dumps(c))
    return c


def ic90(por_dia: dict):
    ks = [k for k in por_dia if por_dia[k]]
    if len(ks) < 3:
        return None
    rng, ms = random.Random(3), []
    for _ in range(800):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return ms[40], ms[759]


def fila(nombre, v):
    """v: [(dia, acierto, ask, pnl)]"""
    if len(v) < 15:
        return None
    pd = collections.defaultdict(list)
    for d, _, _, p in v:
        pd[d].append(p)
    ic = ic90(pd)
    return (f"{nombre:34s} n={len(v):5d} acierto={sum(x[1] for x in v) / len(v):.3f} ask={sum(x[2] for x in v) / len(v):.3f} "
            f"EV={sum(x[3] for x in v) / len(v):+.4f} IC90={'(%+.3f,%+.3f)' % ic if ic else '   -   '} "
            f"días+={sum(1 for d in pd.values() if sum(d) > 0)}/{len(pd)} por_día={len(v) / len(pd):.1f}")


def main() -> int:
    desde = sys.argv[sys.argv.index("--desde") + 1] if "--desde" in sys.argv else "0"
    filas = [r for r in csv.DictReader(open(SRC, encoding="utf-8", errors="replace")) if r["ts_utc"][:10] >= desde]
    gan = desenlaces(r["slug"] for r in filas)
    n_slug = len({r["slug"] for r in filas})
    print(f"{len(filas)} lecturas, {n_slug} mercados, {sum(1 for s in {r['slug'] for r in filas} if s in gan)} con desenlace oficial, "
          f"días {sorted({r['ts_utc'][:10] for r in filas})}")
    datos = collections.defaultdict(list)       # (marco, offset) -> [(dia, activo, z, ask|None, ratio, acierto)]
    for r in filas:
        g = gan.get(r["slug"])
        if g is None or not r["direccion"]:
            continue
        try:
            z = abs(float(r["z"]))
        except ValueError:
            continue
        try:
            a = float(r["ask"])
        except ValueError:
            a = None
        try:
            ratio = float(r["ratio_vs_stake"] or 0)
        except ValueError:
            ratio = 0.0
        datos[(r["marco"], int(float(r["offset_s"])))].append((r["ts_utc"][:10], r["activo"], z, a, ratio, 1 if r["direccion"] == g else 0))
    for marco in ("5m", "15m"):
        print(f"\n================ {marco} ================")
        print("instante  ventanas  acierto_TWAP  con_ask<0,99  ask_comprable(>=5x)   acierto_TWAP por z: " + "  ".join(f"[{lo},{hi})" for lo, hi in ZB))
        for off in sorted(o for m, o in datos if m == marco):
            v = datos[(marco, off)]
            por_z = []
            for lo, hi in ZB:
                s = [x[5] for x in v if lo <= x[2] < hi]
                por_z.append(f"{sum(s) / len(s):.2f}({len(s)})" if s else "-")
            print(f"  T{off:+4d}   {len(v):6d}     {sum(x[5] for x in v) / len(v):.3f}        "
                  f"{sum(1 for x in v if x[3] is not None and x[3] < 0.99) / len(v):5.1%}         "
                  f"{sum(1 for x in v if x[3] is not None and x[3] < 0.99 and x[4] >= RATIO_MIN) / len(v):5.1%}            " + "  ".join(por_z))
        for off in (-120, -90, -60, -45, -30, -20, -10):
            v = [x for x in datos.get((marco, off), []) if x[3] is not None and 0.05 <= x[3] < 0.99 and x[4] >= RATIO_MIN]
            print(f"\n--- {marco} T{off:+d} s: comprar el lado del TWAP al ask real (profundidad >=5x)")
            for zlo, zhi in ZB:
                for alo, ahi in AB:
                    s = [(x[0], x[5], x[3], x[5] / x[3] - 1 - FEE * (1 - x[3])) for x in v if zlo <= x[2] < zhi and alo <= x[3] < ahi]
                    t = fila(f"  z[{zlo},{zhi}) ask[{alo:.2f},{ahi:.2f})", s)
                    if t:
                        print(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
