#!/usr/bin/env python3
"""analisis_escaleras_cierre_fase0.py -- precierre en escaleras cripto "above K" (ronda 2 #8).
Lee data/shadow/escaleras_cierre_ws_fase0.csv (libro por WS en T-60..T+60 s) y el desenlace oficial
(gamma, closed=true). Pregunta: comprando al ASK REAL el lado que el propio libro da por favorito
(mid > 0,5) en cada instante antes del cierre, ¿queda margen? Por instante x tramo de ask, con IC90
por hora de cierre (los strikes de una misma hora comparten el mismo movimiento del spot: la unidad
independiente es la hora, no el strike). Solo lectura.  Uso: analisis_escaleras_cierre_fase0.py
"""
import collections
import csv
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from resolver_mean_reversion_penny_clipper_fase0 import _CACHE, precargar_desenlaces  # noqa: E402

FEE = 0.07
TRAMOS = ((0.50, 0.80), (0.80, 0.90), (0.90, 0.95), (0.95, 0.98), (0.98, 0.995))


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main() -> int:
    random.seed(11)
    rows = list(csv.DictReader(open(REPO / "data/shadow/escaleras_cierre_ws_fase0.csv", encoding="utf-8")))
    precargar_desenlaces([r["condition_id"] for r in rows])
    por = collections.defaultdict(dict)          # (market, offset) -> {YES: fila, NO: fila}
    for r in rows:
        por[(r["market_id"], int(float(r["offset_s"])))][r["token"]] = r
    sin = len({r["condition_id"] for r in rows if r["condition_id"] not in _CACHE})
    print(f"{len(rows)} filas, {len({r['market_id'] for r in rows})} mercados, "
          f"{len({r['end_date'] for r in rows})} horas de cierre; {sin} mercados sin desenlace oficial")
    celdas = collections.defaultdict(list)       # (offset, tramo) -> [(hora, ev, acierto, ask, tamaño_usd)]
    disp = collections.Counter()
    for (mid, off), lados in por.items():
        if off > 0 or "YES" not in lados or "NO" not in lados:
            continue
        y = lados["YES"]
        gan = _CACHE.get(y["condition_id"])       # "Up" = gana el primer outcome (YES)
        if gan is None:
            continue
        by, ay = _f(y["best_bid"]), _f(y["best_ask"])
        bn, an = _f(lados["NO"]["best_bid"]), _f(lados["NO"]["best_ask"])
        # favorito según el libro: mid del YES si hay dos lados; si no, el lado con bid alto
        if by is not None and ay is not None:
            fav_yes = (by + ay) / 2 > 0.5
        elif by is not None or bn is not None:
            fav_yes = (by or 0) > (bn or 0)
        else:
            continue
        fav = lados["YES"] if fav_yes else lados["NO"]
        ask, tam = (ay, _f(y["ask_size"])) if fav_yes else (an, _f(lados["NO"]["ask_size"]))
        disp[(off, "con_ask" if ask is not None and ask < 0.995 else "sin_ask")] += 1
        if ask is None or not 0.5 <= ask < 0.995:
            continue
        acierto = (gan == "Up") == fav_yes
        ev = (1 - ask) / ask * (1 - FEE) if acierto else -1.0
        for lo, hi in TRAMOS:
            if lo <= ask < hi:
                celdas[(off, (lo, hi))].append((y["end_date"], ev, acierto, ask, (tam or 0) * ask, _f(fav["edad_estado_ms"]) or 0))
    print("\nfavoritos con ask comprable (<0,995) por instante:")
    for off in sorted({o for o, _ in disp}):
        c, s = disp[(off, "con_ask")], disp[(off, "sin_ask")]
        print(f"  T{off:+4d} s: {c:4d} de {c + s:4d} ({c / max(1, c + s):.0%})")
    print("\ninstante  tramo_ask        n  horas  acierto  ask_medio  EV/€    IC90 por horas     usd_al_ask(med)  edad_libro_s(med)")
    for (off, (lo, hi)), v in sorted(celdas.items()):
        if len(v) < 15:
            continue
        horas = collections.defaultdict(list)
        for h, ev, *_ in v:
            horas[h].append(ev)
        ks, bs = list(horas), []
        for _ in range(1000):
            m = [x for k in random.choices(ks, k=len(ks)) for x in horas[k]]
            bs.append(sum(m) / len(m))
        bs.sort()
        tams, edades = sorted(x[4] for x in v), sorted(x[5] for x in v)
        print(f"  T{off:+4d}  [{lo:.2f},{hi:.3f})  {len(v):4d}  {len(ks):4d}   {sum(x[2] for x in v) / len(v):.3f}    "
              f"{sum(x[3] for x in v) / len(v):.3f}   {sum(x[1] for x in v) / len(v):+.3f}  ({bs[50]:+.3f},{bs[949]:+.3f})   "
              f"{tams[len(tams) // 2]:8.0f}        {edades[len(edades) // 2] / 1000:6.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
