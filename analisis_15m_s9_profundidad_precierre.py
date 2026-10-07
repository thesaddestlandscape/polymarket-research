#!/usr/bin/env python3
"""analisis_15m_s9_profundidad_precierre.py -- MISIÓN DEFINITIVA 15m §9 paso 2 (07-Oct, Javi: "¿no lo puedes hacer con el
histórico?"). La profundidad multinivel de los 15m solo existe en disco en precierre_libro_ms_*.csv.gz: últimos 70 s de cada
mercado, desequilibrio a 1 y 5 niveles (imb1, imb5) en cada cambio del libro, 29-Sep → 07-Oct (retención 5 d en origen).
Pregunta: ¿la profundidad (imb5) predice algo EJECUTABLE por encima del nivel 1 (imb1) y del propio precio?
DISEÑO (fijado antes de mirar): momentos T−60/−45/−30 s; estado = última fila 'book' del token anterior al momento.
  H9a_imb5 : comprar el token si imb5 >= P80 de DISC (por marco)        H9a_imb1: idem con imb1 (control de nivel 1)
  BASE     : comprar todo token con ask en el mismo rango de precio, sin filtro (control de precio)
Ejecución: ask de la primera fila 'book' del token con t >= momento + 215 ms (sin ella = no ejecutable). PnL por € con
comision_cripto.pnl_por_euro, desenlace oficial. DISC 29-Sep..02-Oct | TEST 03..07-Oct. IC90 bootstrap por CIERRES.
Uso: (ulimit -v 2500000; nice -n 10 python3 analisis_15m_s9_profundidad_precierre.py)
"""
import glob
import gzip
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comision_cripto import pnl_por_euro  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = "/root/polymarket-research-datalogs"
OFFS = (60_000, 45_000, 30_000)
LAT = 215
DISC_HASTA = "2026-10-02"


def cargar():
    libros = defaultdict(list)             # (mid, token) -> [(t_ms, ask, imb1, imb5)]
    meta = {}
    for f in sorted(glob.glob(f"{DL}/precierre_libro_ms_*.csv.gz")):
        with gzip.open(f, "rt", errors="replace") as fh:
            next(fh, None)
            try:
                for ln in fh:
                    c = ln.rstrip("\n").split(",")
                    if len(c) < 12 or c[5] != "book" or c[2] != "15min":
                        continue
                    try:
                        t, ask, i1, i5 = int(c[6]), float(c[9]), float(c[10]), float(c[11])
                    except ValueError:
                        continue
                    k = (c[0], c[4])
                    libros[k].append((t, ask, i1, i5))
                    meta[c[0]] = (c[1], float(c[3]))
            except EOFError:
                pass
    for v in libros.values():
        v.sort()
    return libros, meta


def main():
    libros, meta = cargar()
    des = desenlaces(set(meta))
    obs = []                               # (dia, cierre, mid, lado, off, ask_ejec, imb1, imb5, gana)
    for (mid, lado), filas in libros.items():
        if mid not in des:
            continue
        fin = int(meta[mid][1] * 1000)
        ts = np.array([x[0] for x in filas])
        for off in OFFS:
            t = fin - off
            k = np.searchsorted(ts, t, side="right") - 1
            j = np.searchsorted(ts, t + LAT, side="left")
            if k < 0 or j >= len(filas) or filas[j][0] > t + 5000:
                continue
            ask = filas[j][1]
            if not 0.02 <= ask <= 0.98:
                continue
            from datetime import datetime, timezone
            dia = datetime.fromtimestamp(fin / 1000, timezone.utc).strftime("%Y-%m-%d")
            gana = 1 if str(des[mid]).upper() in (lado.upper(), "UP" if lado == "YES" else "DOWN") else 0
            obs.append((dia, fin, mid, lado, off, ask, filas[k][2], filas[k][3], gana))
    print(f"observaciones: {len(obs)} | mercados {len({o[2] for o in obs})} | días {sorted({o[0] for o in obs})}")
    O = np.array([(o[5], o[6], o[7], o[8], o[1], o[0] <= DISC_HASTA, o[4]) for o in obs], dtype=float)
    ask, i1, i5, gana, cie, disc, off = O.T
    disc = disc.astype(bool)
    pnl = np.array([pnl_por_euro(a, int(g)) for a, g in zip(ask, gana)])
    rng = np.random.default_rng(9)

    def ic(m):
        u, inv = np.unique(cie[m], return_inverse=True)
        S, N = np.bincount(inv, pnl[m]), np.bincount(inv)
        bs = [S[k].sum() / N[k].sum() for k in (rng.integers(0, len(u), len(u)) for _ in range(2000))]
        return np.percentile(bs, 5), np.percentile(bs, 95), len(u)
    for nom, x in (("H9a_imb5", i5), ("H9a_imb1", i1)):
        thr = np.quantile(x[disc], 0.8)
        print(f"\n{nom}: umbral P80 DISC = {thr:+.3f}")
        for per, mp in (("DISC", disc), ("TEST", ~disc)):
            m = mp & (x >= thr)
            lo, hi, nc = ic(m)
            base = mp & (ask >= np.quantile(ask[m], 0.1)) & (ask <= np.quantile(ask[m], 0.9))
            print(f"   {per}: n={m.sum():5} cierres={nc:4} ask medio {ask[m].mean():.3f} acierto {gana[m].mean():.3f} | "
                  f"PnL/€ {pnl[m].mean():+.4f} IC90 ({lo:+.4f},{hi:+.4f}) | BASE mismo rango de precio "
                  f"n={base.sum()} PnL/€ {pnl[base].mean():+.4f}")
            for o in OFFS:
                mo = m & (off == o)
                if mo.sum() >= 30:
                    print(f"      T-{o // 1000}s n={mo.sum():4} PnL/€ {pnl[mo].mean():+.4f}")
    # información incremental: imb5 dentro de cuantiles de imb1 (¿la profundidad añade algo a nivel 1?)
    print("\nINCREMENTAL (TEST): PnL/€ por tercil de imb5 DENTRO de cada tercil de imb1")
    t1 = np.quantile(i1[disc], [1 / 3, 2 / 3]); t5 = np.quantile(i5[disc], [1 / 3, 2 / 3])
    for a in range(3):
        m1 = (~disc) & (np.digitize(i1, t1) == a)
        fila = []
        for b in range(3):
            mm = m1 & (np.digitize(i5, t5) == b)
            fila.append(f"imb5 t{b}: n={mm.sum():4} {pnl[mm].mean() if mm.sum() else float('nan'):+.3f} (acierto-ask {(gana[mm] - ask[mm]).mean() if mm.sum() else float('nan'):+.3f})")
        print(f"   imb1 tercil {a}: " + " | ".join(fila))


if __name__ == "__main__":
    main()
