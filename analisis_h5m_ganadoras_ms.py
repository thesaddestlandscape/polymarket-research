#!/usr/bin/env python3
"""analisis_h5m_ganadoras_ms.py -- H5M (b) (Javi 14-Oct): ¿qué hacen DISTINTO, al milisegundo, las 54 wallets GANADORAS de
la banda 0,10-0,30 de 5m frente a las 158 PERDEDORAS, si on-chain se comportan igual (5 acc, 1 orden por unidad, mismo
precio/T)? Se empareja cada relleno on-chain (caché de analisis_h5m_quien_gana_banda.py) con su operación del registro
ms (m5_registro_D, fila t, hora del exchange) y se mira el libro en ese instante.

Emparejamiento: relleno maker que compra el lado s a pc. Su operación es una fila t en el token s con side SELL a pc, o en
el token contrario con side BUY a 1-pc (acuñación / venta del favorito), con hora del exchange en [ts_bloque - 8 s,
ts_bloque + 2 s]; se toma la MÁS CERCANA a ts_bloque - 2 s. Se informa la tasa de emparejamiento.
Rasgos en el instante de la operación (estado del libro del token s por recepción):
  - posición: pc == mejor bid de s (top), < bid (nivel más profundo: barrido), > bid (el libro aún no reflejaba la orden);
  - edad del nivel: ms desde que el mejor bid de s tomó ese precio (¿se ponen en niveles RECIÉN creados?);
  - spread de s; Binance en contra en el segundo previo (bps, recepción);
  - MARKOUT: mid de s a +5 s y +30 s menos pc (selección adversa sin depender del desenlace).
Grupos de quien_gana_wallets.csv (fijados en la parte 2). Días por defecto 11-13 Oct.
Uso: nice -n 19 ionice -c3 python3 analisis_h5m_ganadoras_ms.py [--dias 2026-10-11,2026-10-12,2026-10-13]
Salida: datalogs/h5m_cola_sim/ganadoras_ms_D.csv.gz + ganadoras_ms_informe.txt
"""
import argparse
import bisect
import gzip
import sys
from collections import deque
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_h5m_cola_simulada import OUT  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

VENT_ANTES_MS, VENT_DESPUES_MS, OBJ_MS = 8000, 2000, 2000
MARKOUTS_MS = (5000, 30000)


def procesar_dia(d, grupos):
    R = pd.read_csv(OUT / f"quien_gana_rellenos_v2_{d}.csv.gz", dtype={"wallet": str, "mkt": str})
    R["grupo"] = R.wallet.map(grupos)
    R = R[R.grupo.isin(["GANADORA", "PERDEDORA"])].reset_index(drop=True)
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    # 1ª pasada: mapa k (mercado, lado) -> token (los k van al principio de cada fichero)
    tok = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                if ln.startswith("k,"):
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[4] == "5min":
                        tok[(c[5], c[7])] = c[2]
        except (EOFError, OSError):
            pass
    R["tok_s"] = [tok.get((m, l)) for m, l in zip(R.mkt, R.lado_c)]
    R["tok_o"] = [tok.get((m, "NO" if l == "YES" else "YES")) for m, l in zip(R.mkt, R.lado_c)]
    R = R[R.tok_s.notna() & R.tok_o.notna()].reset_index(drop=True)
    # índice de búsqueda: (token de la operación, side, precio) -> lista ordenada de (t_obj_ms, idx)
    idx = {}
    tobj = (R.ts.values * 1000 - OBJ_MS).astype(np.int64)
    for i, (ts_, ss, so, pc) in enumerate(zip(tobj, R.tok_s, R.tok_o, R.pc.round(2))):
        idx.setdefault((ss, "SELL", round(pc, 2)), []).append((ts_, i))
        idx.setdefault((so, "BUY", round(1 - pc, 2)), []).append((ts_, i))
    for v in idx.values():
        v.sort()
    claves_t = {k: [x[0] for x in v] for k, v in idx.items()}
    n = len(R)
    mejor = np.full(n, np.iinfo(np.int64).max)       # |t_ex - t_obj| del mejor emparejamiento
    t_match = np.full(n, -1, dtype=np.int64)
    estado = {}                                      # token -> [bid, ask, t_bid_desde, t_rx]
    rasgos = {}                                      # i -> dict (se reescribe si aparece un emparejamiento mejor)
    pend_mk = []                                     # (t_rx_objetivo, i, k, token)
    bn = {}
    mon_tok = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "x,":
                    c = ln.split(",")
                    try:
                        dq = bn.setdefault(c[2][:-4], deque())
                        t_rx, p = int(c[7]), float(c[3])
                    except (ValueError, IndexError):
                        continue
                    if dq and t_rx < dq[-1][0] - 1000:
                        dq.clear()
                    dq.append((t_rx, p))
                    while dq and dq[0][0] < t_rx - 1000:
                        dq.popleft()
                    continue
                if tp == "q,":
                    c = ln.rstrip("\n").split(",")
                    try:
                        b, a, t_rx = float(c[3]), float(c[4]), int(c[7])
                    except (ValueError, IndexError):
                        continue
                    e = estado.get(c[2])
                    if e is None or abs(e[0] - b) > 1e-9:
                        estado[c[2]] = [b, a, t_rx, t_rx]
                    else:
                        e[1], e[3] = a, t_rx
                    continue
                if tp != "t,":
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8:
                            mon_tok[c[2]] = c[3]
                    continue
                c = ln.rstrip("\n").split(",")
                try:
                    p, side, t_ex, t_rx = round(float(c[3]), 2), c[4], int(c[1]), int(c[6])
                except (ValueError, IndexError):
                    continue
                k = (c[2], side, p)
                lst = claves_t.get(k)
                if not lst:
                    continue
                lo = bisect.bisect_left(lst, t_ex - OBJ_MS - VENT_DESPUES_MS)      # t_o >= t_ex - 4 s
                hi = bisect.bisect_right(lst, t_ex + VENT_ANTES_MS - OBJ_MS)       # t_o <= t_ex + 6 s
                for j in range(max(0, lo), hi):
                    t_o, i = idx[k][j]
                    # ventana: ts_bloque - 8 s <= t_ex <= ts_bloque + 2 s  (t_o = ts_bloque - 2 s)
                    if not (t_o + OBJ_MS - VENT_ANTES_MS <= t_ex <= t_o + OBJ_MS + VENT_DESPUES_MS):
                        continue
                    dist = abs(t_ex - t_o)
                    if dist >= mejor[i]:
                        continue
                    mejor[i], t_match[i] = dist, t_ex
                    s = R.tok_s.iat[i]
                    e = estado.get(s)
                    pc = R.pc.iat[i]
                    mon = mon_tok.get(s)
                    dq = bn.get(mon)
                    contra = np.nan
                    if dq:
                        p0 = dq[0][1]
                        contra = ((p0 - min(x[1] for x in dq)) if R.lado_c.iat[i] == "YES" else
                                  (max(x[1] for x in dq) - p0)) / p0 * 1e4
                    if e is None:
                        rasgos[i] = {"bn_ms": contra}
                    else:
                        pos = "top" if abs(pc - e[0]) < 0.005 else ("debajo" if pc < e[0] else "encima")
                        rasgos[i] = {"pos": pos, "edad_ms": t_rx - e[2], "spread": round(e[1] - e[0], 3),
                                     "bid": e[0], "bn_ms": contra}
                    for mk in MARKOUTS_MS:
                        pend_mk.append((t_rx + mk, i, mk, s, t_ex))
        except (EOFError, OSError) as e:
            print(f"  {d}: fichero truncado ({type(e).__name__})", file=sys.stderr)
    # markouts: segunda pasada solo por q de los tokens pendientes (mid por recepción)
    pend_mk.sort()
    por_tok = {}
    for t_o, i, mk, s, tm in pend_mk:
        if tm == t_match[i]:                         # solo el emparejamiento definitivo
            por_tok.setdefault(s, []).append((t_o, i, mk))
    ptr = {s: 0 for s in por_tok}
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                if ln[:2] != "q,":
                    continue
                c = ln.rstrip("\n").split(",")
                lst = por_tok.get(c[2])
                if lst is None:
                    continue
                try:
                    t_rx, mid = int(c[7]), (float(c[3]) + float(c[4])) / 2
                except (ValueError, IndexError):
                    continue
                j = ptr[c[2]]
                while j < len(lst) and lst[j][0] <= t_rx:
                    _, i, mk = lst[j]
                    if i in rasgos and t_match[i] >= 0:
                        rasgos[i][f"mk{mk // 1000}"] = mid - R.pc.iat[i]
                    j += 1
                ptr[c[2]] = j
        except (EOFError, OSError):
            pass
    F = pd.DataFrame.from_dict(rasgos, orient="index")
    R = R.join(F)
    R["emparejado"] = t_match >= 0
    R["dt_bloque_ms"] = np.where(t_match >= 0, R.ts.values * 1000 - t_match, np.nan)
    return R


def ev(df):
    return df.pnl.sum() / df.coste.sum() if len(df) and df.coste.sum() > 0 else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default="2026-10-11,2026-10-12,2026-10-13")
    a = ap.parse_args()
    grupos = pd.read_csv(OUT / "quien_gana_wallets.csv", index_col=0).grupo.to_dict()
    partes = []
    for d in a.dias.split(","):
        cache = OUT / f"ganadoras_ms_{d}.csv.gz"
        if cache.exists():
            partes.append(pd.read_csv(cache))
            continue
        R = procesar_dia(d, grupos)
        R.to_csv(cache, index=False, compression="gzip")
        print(f"{d}: {len(R)} rellenos, emparejados {R.emparejado.mean():.1%}", flush=True)
        partes.append(R)
    R = pd.concat(partes, ignore_index=True)
    lin = [f"H5M ganadoras vs perdedoras al ms ({a.dias}); rasgos en el instante de la operación emparejada"]
    for g in ("GANADORA", "PERDEDORA"):
        G = R[(R.grupo == g)]
        E = G[G.emparejado]
        lin.append(f"\n{g}: rellenos {len(G)} | emparejados {len(E) / max(1, len(G)):.1%} | EV/€ todos {ev(G):+.4f} "
                   f"emparejados {ev(E):+.4f} | dt bloque-operación med {E.dt_bloque_ms.median():.0f} ms")
        for pos in ("top", "debajo", "encima"):
            S = E[E.pos == pos]
            lin.append(f"    posición {pos:7s} {len(S) / max(1, len(E)):6.1%} [{ev(S):+.3f}] markout5 {S.mk5.mean():+.4f} "
                       f"markout30 {S.mk30.mean():+.4f}")
        lin.append(f"    edad del nivel (ms) p25/p50/p75: {E.edad_ms.quantile(.25):.0f}/{E.edad_ms.median():.0f}/"
                   f"{E.edad_ms.quantile(.75):.0f}")
        for lo_, hi_ in ((0, 500), (500, 2000), (2000, 10000), (10000, 1e12)):
            S = E[(E.edad_ms >= lo_) & (E.edad_ms < hi_)]
            lin.append(f"      nivel con edad [{lo_:g},{hi_:g}) ms {len(S) / max(1, len(E)):6.1%} [{ev(S):+.3f}] "
                       f"markout30 {S.mk30.mean():+.4f}")
        lin.append(f"    spread med {E.spread.median():.3f} | markout5 {E.mk5.mean():+.4f} | markout30 {E.mk30.mean():+.4f}")
        for u in (1, 2, 3):
            S = E[E.bn_ms >= u]
            lin.append(f"    Binance en contra >= {u} bps en el 1 s previo (ms) {len(S) / max(1, E.bn_ms.notna().sum()):6.1%} "
                       f"[{ev(S):+.3f}] vs resto [{ev(E[E.bn_ms < u]):+.3f}]")
    txt = "\n".join(lin)
    print(txt)
    (OUT / "ganadoras_ms_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
