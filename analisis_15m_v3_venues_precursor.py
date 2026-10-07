#!/usr/bin/env python3
"""analisis_15m_v3_venues_precursor.py -- MISIÓN 15M V3 §24-26 (07-Oct): ¿qué VENUE se mueve antes de un barrido en BTC 15m?
Fase previa: solo el 11 % de los barridos traía Binance >=1 bp en 500 ms; cross-moneda no discrimina; Chainlink débil;
35 % sin precursor visible. Lead-lag 14:30Z: Coinbase cruza el umbral antes que Binance en 7/10 eventos (n pequeño).
Entrada (todo con NUESTRO reloj de recepción):
  - captura de leadlag_venues_llegada.py (datalogs/leadlag_venues_*.csv.gz: venue, t_fuente_ms, t_recepcion_ms, precio)
  - registro ms del día (maker_ms_D_*.csv.gz): k (mapa token), q (top del libro, recepción c[7]), t (operaciones, recepción c[6])
  - on-chain del día (onchain_fills_D.csv.gz): órdenes TOMADORAS (taker == contrato) en tokens BTC 15m
Cada orden tomadora on-chain se empareja con su fila t del registro (token, lado, tamaño, ±8 s del bloque) -> hora de
recepción tr. Para cada venue: retorno en [tr−500, tr] y [tr−2000, tr] en la dirección del tomador (YES = Up). Barrido
(descriptivo, usa el futuro): mid YES del registro −1 s → +5 s alrededor de tr >= 4 c a favor del tomador.
Desenlace oficial (gamma) para el EV a resolución. Uso:
  (ulimit -v 4000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_venues_precursor.py datalogs/leadlag_venues_X.csv.gz)
"""
import gzip
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"


def main(f_ven):
    V = pd.read_csv(f_ven)
    V = V[pd.to_numeric(V.t_recepcion_ms, errors="coerce").notna()]
    V["tr"] = V.t_recepcion_ms.astype(float).astype(np.int64)
    V["precio"] = V.precio.astype(float)
    a, b = int(V.tr.min()) + 5000, int(V.tr.max()) - 10_000
    dia = pd.Timestamp(a, unit="ms").strftime("%Y-%m-%d")
    print(f"ventana {pd.Timestamp(a, unit='ms')} .. {pd.Timestamp(b, unit='ms')} ({(b - a) / 60000:.0f} min)", file=sys.stderr)
    ven = {v: (g.tr.values[np.argsort(g.tr.values, kind='stable')], g.precio.values[np.argsort(g.tr.values, kind='stable')])
           for v, g in V.groupby("venue")}
    # registro ms: k + q/t en la ventana (awk sobre la hora de la columna 2)
    regs = sorted(DL.glob(f"maker_ms_{dia}_*.csv.gz"))
    # un zcat POR fichero: con varios a la vez, un gzip truncado (corte brusco del hijo) detiene la lectura del resto
    cmd = (f"for f in {' '.join(map(str, regs))}; do zcat $f 2>/dev/null; done | awk -F, '$1==\"k\" || (($1==\"q\"||$1==\"t\") && $2>={a - 20000} && $2<={b + 40000})'")
    k, q, t = {}, [], []
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True)
    for ln in p.stdout:
        c = ln.rstrip("\n").split(",")
        if c[0] == "k" and len(c) >= 8 and c[3] == "BTC" and c[4] == "15min":
            k[c[2]] = (c[5], c[7], c[6])
        elif c[0] == "q" and len(c) >= 8:
            q.append((c[2], int(c[7]), c[3], c[4]))
        elif c[0] == "t" and len(c) >= 7:
            t.append((c[2], int(c[1]), int(c[6]), c[4], float(c[5] or 0)))
    p.wait()
    Q = pd.DataFrame(q, columns=["tok", "tr", "bb", "ba"])
    Q = Q[Q.tok.isin(k)]
    Q["mid"] = (pd.to_numeric(Q.bb, errors="coerce") + pd.to_numeric(Q.ba, errors="coerce")) / 2
    Q = Q.dropna().sort_values(["tok", "tr"], kind="stable")
    mids = {tk: (g.tr.values, g.mid.values) for tk, g in Q.groupby("tok")}
    T = pd.DataFrame(t, columns=["tok", "te", "tr", "side", "sz"])
    T = T[T.tok.isin(k)].sort_values(["tok", "te"], kind="stable")
    tidx = {tk: g for tk, g in T.groupby("tok")}
    # on-chain del día, órdenes tomadoras en tokens BTC 15m
    rows = []
    with gzip.open(DL / f"onchain_fills_{dia}.csv.gz", "rt", errors="replace") as fh:
        next(fh)
        for ln in fh:
            c = ln.split(",")
            if len(c) < 13 or c[0] != "F" or c[7] != EXCH or c[9] not in k:
                continue
            try:
                ts = float(c[2]) * 1000
            except ValueError:
                continue
            if a - 10_000 <= ts <= b + 10_000:
                rows.append((c[6], c[9], int(c[8]), float(c[10]), float(c[11]), float(c[12]), ts))
    O = pd.DataFrame(rows, columns=["wallet", "tok", "side", "maker_amt", "taker_amt", "fee", "ts"])
    buy = O.side == 0
    O["acc"] = np.where(buy, O.taker_amt, O.maker_amt)
    O["usdc"] = np.where(buy, O.maker_amt, O.taker_amt)
    O = O[O.acc > 0]
    print(f"tokens BTC15m {len(k)}, q {len(Q)}, t {len(T)}, tomadoras on-chain {len(O)}", file=sys.stderr)
    des = desenlaces({v[0] for v in k.values()})
    filas = []
    for r in O.itertuples(index=False):
        g = tidx.get(r.tok)
        if g is None:
            continue
        lado_ws = "BUY" if r.side == 0 else "SELL"
        m = g[(g.side == lado_ws) & ((g.sz - r.acc).abs() < 0.02) & (g.te >= r.ts - 8000) & (g.te <= r.ts + 3000)]
        if m.empty:
            continue
        tr = int(m.iloc[(m.te - r.ts).abs().argmin()].tr)
        if not (a <= tr <= b):
            continue
        mkt, lado, _fin = k[r.tok]
        d = (1 if r.side == 0 else -1) * (1 if lado == "YES" else -1)       # dirección en términos YES (= Up)
        tm, vm = mids.get(r.tok, (None, None))
        if tm is None:
            continue

        def mid(tt):
            j = np.searchsorted(tm, tt, side="right") - 1
            return vm[j] if j >= 0 else np.nan
        sgn_tok = 1 if lado == "YES" else -1
        salto = d * sgn_tok * (mid(tr + 5000) - mid(tr - 1000))
        p_yes = r.usdc / r.acc if lado == "YES" else 1 - r.usdc / r.acc
        win = (1.0 if des.get(mkt) == "YES" else 0.0) if mkt in des else np.nan
        f = dict(tr=tr, d=d, salto=salto, usdc=r.usdc, wallet=r.wallet,
                 res=d * (win - p_yes) - r.fee / r.acc if np.isfinite(win) else np.nan)
        for v, (vt, vp) in ven.items():
            for h in (500, 2000):
                j1 = np.searchsorted(vt, tr, side="right") - 1
                j0 = np.searchsorted(vt, tr - h, side="right") - 1
                f[f"{v}_{h}"] = d * (vp[j1] / vp[j0] - 1) * 1e4 if j0 >= 0 and j1 >= 0 else np.nan
        filas.append(f)
    R = pd.DataFrame(filas)
    R["barrido"] = R.salto >= 0.04
    L = []
    P = lambda *x: L.append(" ".join(str(y) for y in x))
    P(f"MISIÓN 15M V3 — venue precursor de barridos BTC 15m. Captura {Path(f_ven).name}; ventana {(b - a) / 60000:.0f} min; "
      f"órdenes tomadoras emparejadas {len(R)} de {len(O)}; barridos {R.barrido.sum()} ({R.barrido.mean():.1%}); "
      f"con desenlace {R.res.notna().sum()}")
    vs = sorted(ven)
    for h in (500, 2000):
        P(f"\n{h} ms previos (recepción), retorno a favor del tomador >= 1 bp: % en barridos / no barridos / EV res|cond")
        for v in vs:
            c = R[f"{v}_{h}"]
            P(f"  {v:9} barr {(c[R.barrido] >= 1).mean():5.1%}  no {(c[~R.barrido] >= 1).mean():5.1%}  "
              f"EV res {R[c >= 1].res.mean():+.4f} (n={(c >= 1).sum()})")
        alg = np.zeros(len(R), bool)
        for v in vs:
            alg |= (R[f"{v}_{h}"] >= 1).values
        P(f"  ALGUNO   barr {alg[R.barrido.values].mean():5.1%}  no {alg[~R.barrido.values].mean():5.1%}")
        if "binance" in vs:
            sinb = R.barrido & ~(R[f"binance_{h}"] >= 1)
            P(f"  barridos SIN Binance >=1 bp ({sinb.sum()}): " + "  ".join(
                f"{v} {(R.loc[sinb, f'{v}_{h}'] >= 1).mean():.1%}" for v in vs if v != "binance"))
    INF = Path(__file__).resolve().parent / "informes" / f"m15v3_venues_precursor_{Path(f_ven).stem.split('_')[-1].replace('.csv', '')}.txt"
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1])
