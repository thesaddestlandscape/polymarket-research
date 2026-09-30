#!/usr/bin/env python3
"""analisis_colas_escaleras_fase0.py -- colas de escaleras cripto horarias "above K" (ronda 2 #6).
La idea: los strikes lejanos (YES a 0,01-0,10) casi nunca ganan; vender ese YES (= comprar el NO a 1-bid).
Dos mediciones, de menos a más fiable:
  A) RETROSPECTIVO con precio de la historia del CLOB (precio MEDIO por minuto, NO ejecutable: optimista)
     -> /root/polymarket-research-datalogs/analisis_persistente_29sep/colas.pkl (colas_collect.py).
  B) LIBRO REAL por WS (colas_escaleras_ws_fase0.py): BID real del YES y su tamaño en T-30/-15/-5/-1 min.
     Lo que decide es B: sin bid en el YES no hay a quién vendérselo.
La unidad independiente es la HORA de cierre (todos los strikes de una hora caen juntos): IC90 por horas.
Solo lectura. Uso: analisis_colas_escaleras_fase0.py
"""
import collections
import csv
import glob
import gzip
import pickle
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolver_mean_reversion_penny_clipper_fase0 import _CACHE, precargar_desenlaces  # noqa: E402

DATALOGS = Path("/root/polymarket-research-datalogs")
FEE = 0.07
TRAMOS = ((0.005, 0.02), (0.02, 0.05), (0.05, 0.10), (0.10, 0.20))


def _ic(por_hora: dict) -> tuple:
    ks, bs = list(por_hora), []
    for _ in range(1000):
        m = [x for k in random.choices(ks, k=len(ks)) for x in por_hora[k]]
        bs.append(sum(m) / len(m))
    bs.sort()
    return bs[50], bs[949]


def _tabla(celdas: dict, etiqueta: str) -> None:
    print(f"\n{etiqueta}\n minutos_antes  tramo_YES       n  horas  YES_gana   EV/€ de comprar NO   IC90 por horas     peor_hora")
    for (mins, (lo, hi)), v in sorted(celdas.items(), key=lambda kv: (-kv[0][0], kv[0][1])):
        if len(v) < 15:
            continue
        horas = collections.defaultdict(list)
        for h, ev, _ in v:
            horas[h].append(ev)
        lo_ic, hi_ic = _ic(horas)
        peor = min(sum(x) / len(x) for x in horas.values())
        print(f"   T-{mins:3d} min   [{lo:.3f},{hi:.2f})  {len(v):5d}  {len(horas):4d}   {sum(x[2] for x in v) / len(v):6.2%}      "
              f"{sum(x[1] for x in v) / len(v):+.4f}        ({lo_ic:+.4f},{hi_ic:+.4f})   {peor:+.3f}")


def _ev_no(p_yes: float, gana_yes: bool) -> float:
    # comprar NO a (1 - p_yes): gana p_yes/(1-p_yes) menos fee, o pierde 1
    return -1.0 if gana_yes else p_yes / (1 - p_yes) * (1 - FEE)


def retrospectivo() -> None:
    f = DATALOGS / "analisis_persistente_29sep" / "colas.pkl"
    if not f.exists():
        print("sin colas.pkl")
        return
    ms = pickle.load(open(f, "rb"))
    celdas = collections.defaultdict(list)
    for m in ms:
        for mins in (30, 15, 5, 1):
            obj = m["end"] - mins * 60
            prev = [p for t, p in m["h"] if t <= obj]
            if not prev:
                continue
            p = prev[-1]
            for lo, hi in TRAMOS:
                if lo <= p < hi:
                    celdas[(mins, (lo, hi))].append((m["end"], _ev_no(p, bool(m["yes"])), bool(m["yes"])))
    print(f"A) RETROSPECTIVO: {len(ms)} mercados, {len({m['end'] for m in ms})} horas de cierre")
    _tabla(celdas, "A) precio medio de la historia (OPTIMISTA, no es el bid)")


def libro_real() -> None:
    filas = []
    for f in sorted(glob.glob(str(DATALOGS / "colas_escaleras_ws_*.csv.gz"))):
        with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
            filas += [r for r in csv.DictReader(fh) if r["token"] == "YES"]
    precargar_desenlaces([r["condition_id"] for r in filas])
    celdas, disp, tam = collections.defaultdict(list), collections.Counter(), collections.defaultdict(list)
    for r in filas:
        off = int(float(r["offset_s"]))
        if off >= 0 or r["condition_id"] not in _CACHE:
            continue
        mins = -off // 60
        gana_yes = _CACHE[r["condition_id"]] == "Up"
        try:
            ask = float(r["best_ask"])
        except ValueError:
            ask = None
        if ask is None or ask >= 0.20:          # solo colas: YES ofrecido por debajo de 0,20
            continue
        try:
            bid, sz = float(r["best_bid"]), float(r["bid_size"] or 0)
        except ValueError:
            bid, sz = None, 0.0
        disp[(mins, "con_bid" if bid and bid >= 0.005 else "sin_bid")] += 1
        if not bid or bid < 0.005:
            continue
        for lo, hi in TRAMOS:
            if lo <= bid < hi:
                celdas[(mins, (lo, hi))].append((r["end_date"], _ev_no(bid, gana_yes), gana_yes))
                tam[(mins, (lo, hi))].append(bid * sz)
    print(f"\nB) LIBRO REAL: {len(filas)} filas YES, {len({r['market_id'] for r in filas})} mercados, "
          f"{len({r['end_date'] for r in filas})} horas de cierre")
    for mins in sorted({m for m, _ in disp}, reverse=True):
        c, s = disp[(mins, "con_bid")], disp[(mins, "sin_bid")]
        print(f"   T-{mins:3d} min: colas (ask YES <0,20) con BID en el YES: {c} de {c + s} ({c / max(1, c + s):.0%})")
    _tabla(celdas, "B) vender el YES a su BID real (= comprar NO a 1-bid)")
    for k, v in sorted(tam.items(), key=lambda kv: (-kv[0][0], kv[0][1])):
        v.sort()
        print(f"   T-{k[0]:3d} min [{k[1][0]:.3f},{k[1][1]:.2f}): USD en el mejor bid del YES, mediana {v[len(v) // 2]:.1f} (n={len(v)})")


if __name__ == "__main__":
    random.seed(13)
    retrospectivo()
    libro_real()
