#!/usr/bin/env python3
"""analisis_5m_v1_politica_bots_pares.py -- MISIÓN 5M v1, paso 2 (09-Oct, Javi: "ve con el punto 2"): ingeniería
inversa de la política de los COSECHADORES DE PARES de 5m a partir de sus rellenos MAKER on-chain (caché
m5_cache/v1_quien_gana_makers.parquet de analisis_5m_v1_quien_gana.py --solo-makers). Réplica en 5m de
analisis_15m_v4_politica_bots_pares.py (misma función emparejar FIFO, importada, no copiada).

Bots (top 15 maker por PnL 06-08 Oct, >= 98 % de sus mercados con ambos lados): 0x21f4c1a1 (par mediano 0,938),
0xaa1a4f31 (0,939), 0x41e2e1cc (0,989). Tiempo = cierre - T (T = segundos al cierre; resolución de bloque ~2 s).
Por bot, TODOS los activos y por día (estabilidad): inventario, emparejado FIFO (retraso entre patas, coste del par),
% de mercados con par, reacción al desequilibrio, fase del ciclo (T), precio de entrada por pata, PnL y reembolso.
Uso: nice -n 19 python3 analisis_5m_v1_politica_bots_pares.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

from analisis_15m_v4_politica_bots_pares import emparejar

CACHE = Path("/root/polymarket-research-datalogs/m5_cache/v1_quien_gana_makers.parquet")
SALIDA = Path(__file__).resolve().parent / "informes" / "m5v1_politica_bots_pares_09oct.txt"
BOTS = {"0x21f4c1a1be34a39a7bc20985df4b7e5a39fb691d": "21f4", "0xaa1a4f31c010d4a63fc49770d4ca2d69ea370602": "aa1a",
        "0x41e2e1ccf1e4940029af02259a31c6b89b9fa354": "41e2"}


def main():
    X = pd.read_parquet(CACHE, columns=["dia", "mkt", "lado", "side", "acc", "usdc", "pnl", "rebate_est", "p", "T", "act",
                                        "wallet_hex"])
    X = X[X.wallet_hex.isin(BOTS)].copy()
    X["ts"] = -X["T"]                                     # orden temporal dentro del mercado (mismo cierre)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L("Política de cosechadores de pares 5m — rellenos MAKER on-chain 06-08 Oct (todos los activos)")
    for w, nom in BOTS.items():
        A = X[X.wallet_hex == w]
        if A.empty:
            L(f"\n== {nom}: sin rellenos")
            continue
        ventas = (A.side == 1).mean()
        B = A[A.side == 0].sort_values(["mkt", "ts"], kind="stable")
        L(f"\n== {nom}: {A.mkt.nunique()} mercados, {len(A)} rellenos ({ventas:.1%} VENTAS como maker), "
          f"PnL {A.pnl.sum():+.0f} $, reembolso est. {A.rebate_est.sum():.0f} $, vol {A.usdc.sum():.0f} $, "
          f"activos {A.act.value_counts(normalize=True).round(2).to_dict()}")
        for dia, D in [("TODOS", B)] + list(B.groupby("dia")):
            P, filas, merc = [], [], []
            for mkt, g in D.groupby("mkt", sort=False):
                fs = list(zip(g.ts, g.lado, g.acc, g.p))
                pares, Iantes = emparejar(fs)
                P += pares
                tot = g.acc.sum()
                ay, an = g.acc[g.lado == "YES"].sum(), g.acc[g.lado == "NO"].sum()
                absI = np.abs(Iantes)
                merc.append({"n": len(g), "acc": tot, "maxI": absI.max(), "Ifin": abs(ay - an) / tot, "ambos": ay > 0 and an > 0,
                             "t1": g["T"].max(), "t2": g["T"].min(), "pnl": g.pnl.sum(), "usdc": g.usdc.sum()})
                for (ts, lado, acc, p), I0, T in zip(fs, Iantes, g["T"]):
                    filas.append({"absI": abs(I0), "emp": (lado == "NO" and I0 > 0) or (lado == "YES" and I0 < 0),
                                  "acc": acc, "T": T, "p": p})
            M, F = pd.DataFrame(merc), pd.DataFrame(filas)
            Pq = pd.DataFrame(P, columns=["lag", "coste", "acc"])
            L(f"  [{dia}] mercados {len(M)} | con ambos lados {M.ambos.mean():.0%} | rellenos/merc P50 {M.n.median():.0f} | "
              f"acciones/merc P50 {M.acc.median():.0f} | tamaño/relleno P50 {F.acc.median():.1f} P90 {F.acc.quantile(.9):.0f} | "
              f"max|I| P50 {M.maxI.median():.0f} P90 {M.maxI.quantile(.9):.0f} | |I| final/acc P50 {M.Ifin.median():.2f} | "
              f"1er relleno T P50 {M.t1.median():.0f} s, último T P50 {M.t2.median():.0f} s | PnL/vol {M.pnl.sum() / M.usdc.sum():+.4f}")
            if len(Pq) and dia == "TODOS":
                wq = Pq.acc
                o = np.argsort(Pq.lag.values)
                cum = np.cumsum(wq.values[o]) / wq.sum()
                lp = lambda x: Pq.lag.values[o][min(len(o) - 1, np.searchsorted(cum, x))]
                L(f"     emparejado FIFO: retraso entre patas P25 {lp(.25):.0f} s, P50 {lp(.5):.0f} s, P75 {lp(.75):.0f} s, "
                  f"P90 {lp(.9):.0f} s; acciones emparejadas en <=2 s {wq[Pq.lag <= 2].sum() / wq.sum():.1%}, <=10 s "
                  f"{wq[Pq.lag <= 10].sum() / wq.sum():.1%}")
                L(f"     coste del par: media {np.average(Pq.coste, weights=wq):.4f}, P10 {Pq.coste.quantile(.1):.3f}, "
                  f"P50 {Pq.coste.quantile(.5):.3f}, P90 {Pq.coste.quantile(.9):.3f}; % acciones con par > 1,00 "
                  f"{wq[Pq.coste > 1].sum() / wq.sum():.1%}")
                for lo, hi in ((0, 2), (2, 10), (10, 60), (60, 1e9)):
                    s = Pq[(Pq.lag >= lo) & (Pq.lag <= hi)] if lo == 0 else Pq[(Pq.lag > lo) & (Pq.lag <= hi)]
                    if len(s):
                        L(f"       retraso ({lo},{hi if hi < 1e9 else '∞'}] s: {s.acc.sum() / wq.sum():.1%} de acciones, coste medio "
                          f"{np.average(s.coste, weights=s.acc):.4f}")
                F["bin"] = pd.cut(F.absI, [-1, 0.5, 10, 30, 100, 300, 1e9])
                t = F.groupby("bin", observed=True).agg(n=("emp", "size"), pe=("emp", "mean"), acc=("acc", "median"))
                L("     reacción al desequilibrio (|I| antes del relleno -> P(relleno que empareja), tamaño mediano): " +
                  "; ".join(f"{b}: n={int(r.n)} P={r.pe:.2f} t={r.acc:.0f}" for b, r in t.iterrows()))
                tf = F.groupby(pd.cut(F["T"], [-60, 0, 30, 60, 120, 200, 300, 2000]), observed=True).agg(
                    n=("acc", "size"), p=("p", "median"), absI=("absI", "median"))
                L("     por fase (T s): " + "; ".join(f"{b} n={int(r.n)} p_med={r.p:.2f} |I|med={r.absI:.0f}" for b, r in tf.iterrows()))
                tp = F.groupby(pd.cut(F.p, [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1]), observed=True).acc.sum()
                L("     acciones por banda de precio: " + "; ".join(f"{b} {v / tp.sum():.0%}" for b, v in tp.items()))
    SALIDA.write_text("\n".join(lin) + "\n")
    print(f"informe: {SALIDA}")


if __name__ == "__main__":
    main()
