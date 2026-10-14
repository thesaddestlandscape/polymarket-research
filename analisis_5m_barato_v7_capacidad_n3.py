#!/usr/bin/env python3
"""analisis_5m_barato_v7_capacidad_n3.py -- CAPACIDAD MULTINIVEL de V7_DISPARO15M_BTC (descubrimiento, solo lectura): para cada
ejecución simulada (caché disparo15m_D, BTC, DELTA 0, L355) lee del ARCHIVO registro_5m_barato las filas `l` (ask niveles 1-3
del 5m: l,t_ex,token,p1,s1,p2,s2,p3,s3,t_rx) y toma la última con recepción <= t+355 ms. Por stake objetivo S compra
barriendo los niveles con precio <= p_lim (límite de la regla) hasta S € -> VWAP, acciones (mínimo 5 o no opera),
mismo desenlace y comisión por nivel. Sigue siendo una cota (sin niveles > 3 ni competencia por el mismo nivel).
Uso: nice -n 19 python3 analisis_5m_barato_v7_capacidad_n3.py
"""
import bisect
import csv
import glob
import gzip
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
ARCH = Path("/mnt/HC_Volume_106538179/registro_5m_barato")
STAKES = (2, 5, 10, 25, 50, 100, 250, 500)


def main():
    ej = defaultdict(list)
    for f in sorted(OUT.glob("disparo15m_2026-10-*.csv.gz")):
        for r in csv.DictReader(gzip.open(f, "rt")):
            if r["moneda"] == "BTC" and r.get("pnl") and float(r["delta"]) == 0.0 and r["L"] == "355":
                ej[r["dia"]].append(r)
    filas = []
    for dia, rs in sorted(ej.items()):
        objetivo = {}                                          # token -> lista de t+355
        meta = {}
        fich = sorted(glob.glob(str(ARCH / f"maker_ms_{dia}_*.csv.gz")))
        # 1ª pasada: mapa k (mercado, lado) -> token
        for fn in fich:
            with gzip.open(fn, "rt", errors="replace") as fh:
                try:
                    for ln in fh:
                        if ln.startswith("k,"):
                            c = ln.rstrip("\n").split(",")
                            if len(c) >= 8 and c[4] == "5min" and c[3] == "BTC":
                                meta[(c[5], c[7])] = c[2]
                except (EOFError, OSError):
                    pass
        for r in rs:
            tk = meta.get((r["mercado"], "YES" if r["lado"] == "Up" else "NO"))
            if tk:
                objetivo.setdefault(tk, []).append(r)
        ls = defaultdict(list)                                  # token -> [(t_rx, niveles)]
        for fn in fich:
            with gzip.open(fn, "rt", errors="replace") as fh:
                try:
                    for ln in fh:
                        if not ln.startswith("l,"):
                            continue
                        c = ln.rstrip("\n").split(",")
                        if c[2] not in objetivo:
                            continue
                        try:
                            nv = tuple((float(c[i]), float(c[i + 1])) for i in (3, 5, 7) if c[i] not in ("", "None"))
                            ls[c[2]].append((int(c[9]), nv))
                        except (ValueError, IndexError):
                            continue
                except (EOFError, OSError):
                    pass
        for tk, lst in objetivo.items():
            L = sorted(ls.get(tk, []), key=lambda x: x[0])
            ts = [x[0] for x in L]
            for r in lst:
                i = bisect.bisect_right(ts, int(r["t"]) + 355) - 1
                nv = L[i][1] if i >= 0 and int(r["t"]) + 355 - ts[i] <= 60_000 else ()
                filas.append({**r, "niveles": nv})
        print(f"{dia}: {len(rs)} ejecuciones, con niveles {sum(1 for f in filas if f['dia'] == dia and f['niveles'])}", flush=True)
    dias = len({f["dia"] for f in filas}) or 1
    prof = sorted(sum(p * s for p, s in f["niveles"] if p <= float(f["p_lim"]) + 1e-9) for f in filas if f["niveles"])
    if prof:
        print(f"\nV7 BTC DELTA 0 L355 — € disponibles en niveles 1-3 a <= p_lim al llegar: P25/P50/P75/máx "
              f"{prof[len(prof) // 4]:.0f}/{prof[len(prof) // 2]:.0f}/{prof[3 * len(prof) // 4]:.0f}/{prof[-1]:.0f}")
    for S in STAKES:
        pnl = cost = 0.0
        n = 0
        top = []
        for f in filas:
            g = f["gana"] == "True"
            plim = float(f["p_lim"])
            falta, acc, coste_f, pnl_f = S, 0.0, 0.0, 0.0
            for p, s in f["niveles"]:
                if p > plim + 1e-9 or falta <= 0:
                    break
                x = min(s, falta / (p + V.fee(p)))
                acc += x
                coste_f += x * (p + V.fee(p))
                pnl_f += x * ((1.0 if g else 0.0) - p - V.fee(p))
                falta -= x * (p + V.fee(p))
            if acc < 5:
                continue
            n += 1
            pnl += pnl_f
            cost += coste_f
            top.append(pnl_f)
        top.sort(reverse=True)
        print(f"  stake {S:4d} €: ops {n:2d} | invertido {cost:8.1f} € | PnL {pnl:+8.2f} € | EV/€ {pnl / cost if cost else 0:+.3f} | "
              f"sin top3 {pnl - sum(top[:3]):+8.2f} € | {pnl / dias:+.2f} €/día -> x365 {pnl / dias * 365:+,.0f} €/año (techo descubrimiento)")


if __name__ == "__main__":
    main()
