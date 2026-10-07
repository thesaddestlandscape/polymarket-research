#!/usr/bin/env python3
"""forense_feed_15m_emparejar.py -- MISIÓN 15M V3 FASE 0: empareja el lector AISLADO (forense_feed_15m_aislado.py) con el
registro de PRODUCCIÓN (maker_ms_*: filas q = top del libro con hora del exchange y de recepción, filas t = operaciones)
para el MISMO mensaje (token + hora del exchange) y descompone el retraso:
   red+servidor = recepción aislada − hora del exchange   |   producción = recepción producción − hora del exchange
   PIPELINE PROPIO = recepción producción − recepción aislada   (lo que añade nuestro proceso: cola del hijo, GIL, CPU)
Uso: python3 forense_feed_15m_emparejar.py <aislado.csv.gz>
"""
import glob
import gzip
import sys

import numpy as np


def pct(v):
    v = np.asarray(v, float)
    v = v[~np.isnan(v)]
    if not len(v):
        return "n=0"
    p = np.percentile(v, [50, 90, 95, 99])
    return f"n={len(v):7} P50 {p[0]:7.1f} P90 {p[1]:7.1f} P95 {p[2]:7.1f} P99 {p[3]:8.1f} máx {v.max():8.1f}"


def main(f_iso):
    iso_q, iso_t, toks = {}, {}, set()
    t_min, t_max = 1e18, 0
    with gzip.open(f_iso, "rt") as fh:
        next(fh)
        for ln in fh:
            c = ln.rstrip("\n").split(",")
            try:
                rec, ts = float(c[0]), int(c[1])
            except ValueError:
                continue
            toks.add(c[3])
            t_min, t_max = min(t_min, rec), max(t_max, rec)
            if c[2] == "pc":
                k = (c[3], ts)
                iso_q[k] = min(iso_q.get(k, 1e18), rec)
            elif c[2] == "t":
                k = (c[3], ts)
                iso_t[k] = min(iso_t.get(k, 1e18), rec)
    prod_q, prod_t = {}, {}
    for f in sorted(glob.glob("/root/polymarket-research-datalogs/maker_ms_2026-10-*_*.csv.gz"))[-3:]:
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    tp = ln[:2]
                    if tp not in ("q,", "t,"):
                        continue
                    c = ln.rstrip("\n").split(",")
                    if c[2] not in toks:
                        continue
                    try:
                        ts = int(c[1])
                        rec = int(c[7]) if tp == "q," else int(c[6])
                    except (ValueError, IndexError):
                        continue
                    if not (t_min - 60_000 <= rec <= t_max + 60_000):
                        continue
                    d = prod_q if tp == "q," else prod_t
                    k = (c[2], ts)
                    d[k] = min(d.get(k, 1e18), rec)
            except (EOFError, OSError):
                pass
    for nom, I, P in (("LIBRO (price_change / q)", iso_q, prod_q), ("OPERACIONES (last_trade_price / t)", iso_t, prod_t)):
        comunes = [k for k in P if k in I]
        print(f"\n== {nom}: aislado {len(I)} mensajes | producción {len(P)} | emparejados {len(comunes)}")
        if not comunes:
            continue
        ri = np.array([I[k] - k[1] for k in comunes])
        rp = np.array([P[k] - k[1] for k in comunes])
        print(f"   red+servidor (aislado − exchange) : {pct(ri)}")
        print(f"   producción   (prod − exchange)    : {pct(rp)}")
        print(f"   PIPELINE PROPIO (prod − aislado)  : {pct(rp - ri)}")
        solo_iso = len([k for k in I if k not in P])
        print(f"   mensajes que el aislado vio y producción NO registró: {solo_iso} ({100 * solo_iso / max(1, len(I)):.1f} %)")
        # ¿el retraso de cola es del servidor? ráfagas: lag aislado alto
        alto = ri > np.percentile(ri, 90)
        print(f"   en el 10 % de mensajes con MÁS lag de red+servidor: pipeline propio {pct((rp - ri)[alto])}")


if __name__ == "__main__":
    main(sys.argv[1])
