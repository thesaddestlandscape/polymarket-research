#!/usr/bin/env python3
"""analisis_valor_relativo_anidado_ask_real.py -- evalúa valor_relativo_anidado_v2_*.csv(.gz) (observador del 30-Sep,
asks reales de los dos tramos en el MISMO ms) con la regla fijada en su docstring: evento = margen >= 3c; unidad =
PRIMER evento de cada (par, moneda, cierre, dirección). Dos direcciones (06-Oct: el mes de firehose apunta a la
pata CORTA, no a la larga):
  LARGA  : margen     = bid5(lado)  - ask15(lado)      -> comprar el tramo largo al ask15
  CORTA  : inv_margen = inv_bid15   - inv_ask5 (lado contrario) -> comprar el tramo corto al inv_ask5
PnL por € al ask DETECTADO (optimista: nuestra orden llega ~215 ms después; el registro ms permite medirlo solo desde
el 05-Oct), comisión de tomador 0,07·p·(1-p), desenlace oficial por id. IC90 bootstrap por días.
Uso: python3 analisis_valor_relativo_anidado_ask_real.py [--margen 0.03]
"""
import argparse
import collections
import csv
import glob
import gzip
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402


def fee(p):
    return 0.07 * p * (1 - p)


def ic90(por_dia):
    ks = [k for k in por_dia if por_dia[k]]
    if len(ks) < 3:
        return None
    rng, m = random.Random(9), []
    for _ in range(2000):
        v = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
        m.append(sum(v) / len(v))
    m.sort()
    return m[100], m[1900]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--margen", type=float, default=0.03)
    a = ap.parse_args()
    filas = []
    for f in sorted(glob.glob("/root/polymarket-research-datalogs/valor_relativo_anidado_v2_*.csv*")):
        with (gzip.open(f, "rt") if f.endswith(".gz") else open(f)) as fh:
            filas += list(csv.DictReader(fh))
    des = desenlaces({r[k] for r in filas for k in ("market15", "market5")})
    vistos = set()
    res = collections.defaultdict(list)
    for r in sorted(filas, key=lambda r: int(r["ts_ms"])):
        for dire, mg, ask, mk, lado in (("LARGA", r["margen"], r["ask15"], r["market15"], r["lado"]),
                                        ("CORTA", r["inv_margen"], r["inv_ask5"], r["market5"],
                                         "Down" if r["lado"] == "Up" else "Up")):
            try:
                mg, ask = float(mg), float(ask)
            except (TypeError, ValueError):
                continue
            if mg < a.margen or not 0.01 <= ask <= 0.99:
                continue
            k = (r["par"], r["activo"], r["fin"], dire)
            if k in vistos:
                continue
            vistos.add(k)
            if mk not in des:
                res[(r["par"], dire, "sin_desenlace")].append(None)
                continue
            gana = (des[mk] == "YES") == (lado == "Up")
            pnl = (1 - ask) / ask - fee(ask) / ask if gana else -1 - fee(ask) / ask
            dia = datetime.fromtimestamp(int(r["ts_ms"]) / 1000, timezone.utc).date().isoformat()
            res[(r["par"], dire)].append((dia, pnl, gana, r["activo"], ask))
    for k in sorted(res):
        v = [x for x in res[k] if x is not None]
        if len(k) == 3:
            print(f"  {k}: {len(res[k])}")
            continue
        if not v:
            continue
        pd_ = collections.defaultdict(list)
        for x in v:
            pd_[x[0]].append(x[1])
        i = ic90(pd_)
        top2 = sorted(pd_, key=lambda d: -sum(pd_[d]))[:2]
        sin2 = [x[1] for x in v if x[0] not in top2]
        print(f"{k[0]:7} {k[1]:5} n={len(v):4} días={len(pd_)} acierto={sum(x[2] for x in v) / len(v):.0%} "
              f"ask medio {sum(x[4] for x in v) / len(v):.2f} EV/€ {sum(x[1] for x in v) / len(v):+.3f} "
              f"IC90 {'-' if i is None else f'[{i[0]:+.3f},{i[1]:+.3f}]'} | sin 2 mejores días "
              f"{(sum(sin2) / len(sin2)) if sin2 else 0:+.3f} | días + {sum(1 for d in pd_ if sum(pd_[d]) > 0)}/{len(pd_)}")
        mon = collections.defaultdict(list)
        for x in v:
            mon[x[3]].append(x[1])
        print("        por moneda: " + " ".join(f"{m}:{sum(p) / len(p):+.2f}(n{len(p)})" for m, p in sorted(mon.items())))


if __name__ == "__main__":
    main()
