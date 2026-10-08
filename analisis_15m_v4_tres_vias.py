#!/usr/bin/env python3
"""analisis_15m_v4_tres_vias.py -- MISIÓN 15M v4 (08-Oct, Javi: "estudiar takers e híbridos siguiendo la misma
tendencia, tener las tres vías cubiertas y generando pasta"). Sobre los rellenos on-chain 15m (caché
v4_quien_gana.parquet; formato y signos en analisis_15m_v4_quien_gana.py):
  1) Clase por wallet (volumen >= VOL_MIN en 05-07 Oct): MAKER puro (< 10 % del volumen como tomador), TOMADOR puro
     (> 90 %), HÍBRIDO (resto).
  2) Por clase: PnL a resolución por día (tomador neto de su comisión; reembolso del maker ESTIMADO aparte),
     persistencia (wallets con PnL > 0 los 3 días; con 3 días el azar da ~1/8 si fuese moneda al aire).
  3) Perfil de las PERSISTENTES de tomador e híbrido: banda de precio, fase del ciclo (T), tamaño, monedas, % de
     mercados con PnL > 0, PnL/mercado, y para híbridos qué rol hace cada pata (¿maker un lado y tomador el otro en el
     mismo mercado? ¿tomador solo cerca del cierre?).
Uso: nice -n 19 python3 analisis_15m_v4_tres_vias.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

DL = Path("/root/polymarket-research-datalogs")
VOL_MIN = 3000.0
INF = Path(__file__).resolve().parent / "informes" / "m15v4_tres_vias_08oct.txt"


def main():
    X = pd.read_parquet(DL / "m15_ms_cache" / "v4_quien_gana.parquet",
                        columns=["wallet", "rol", "side", "dia", "act", "mkt", "lado", "acc", "usdc", "p", "T", "pnl", "rebate_est", "fee"])
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    v = X.pivot_table(index="wallet", columns="rol", values="usdc", aggfunc="sum").fillna(0.0)
    v["vol"] = v.sum(axis=1)
    v = v[v.vol >= VOL_MIN]
    v["frac_tom"] = v.get("tomador", 0) / v.vol
    v["clase"] = np.where(v.frac_tom < 0.10, "MAKER", np.where(v.frac_tom > 0.90, "TOMADOR", "HIBRIDO"))
    X = X[X.wallet.isin(v.index)].copy()
    X["clase"] = X.wallet.map(v.clase)
    dias = sorted(X.dia.unique())
    L(f"Tres vías — rellenos on-chain 15m {dias[0]}..{dias[-1]}, wallets con volumen >= {VOL_MIN:.0f} USDC: {len(v)}")
    d = X.groupby(["clase", "wallet", "dia"]).agg(pnl=("pnl", "sum"), reb=("rebate_est", "sum"), vol=("usdc", "sum")).reset_index()
    for clase in ("MAKER", "TOMADOR", "HIBRIDO"):
        c = d[d.clase == clase]
        piv = c.pivot_table(index="wallet", columns="dia", values="pnl", aggfunc="sum")
        tres = piv.dropna()
        pers = tres[(tres > 0).all(axis=1)]
        porc = c.groupby("dia").agg(pnl=("pnl", "sum"), reb=("reb", "sum"), vol=("vol", "sum"))
        L(f"\n== {clase}: {piv.shape[0]} wallets; PnL por día " + ", ".join(f"{k} {r.pnl:+.0f} (reb {r.reb:.0f}, vol {r.vol / 1e3:.0f}k)" for k, r in porc.iterrows()))
        L(f"   con actividad los 3 días: {len(tres)}; PERSISTENTES (PnL > 0 los 3 días): {len(pers)} ({len(pers) / max(1, len(tres)):.0%}; azar ≈ 12,5 %); "
          f"su PnL/día medio {pers.sum(axis=1).sum() / 3:+.0f}")
        if clase == "MAKER" or len(pers) == 0:
            continue
        L("   persistentes (PnL total, PnL/vol, mercados, % mercados > 0, precio P50, T P50, tamaño P50, monedas):")
        for w in pers.sum(axis=1).sort_values(ascending=False).index[:15]:
            q = X[X.wallet == w]
            pm = q.groupby("mkt").pnl.sum()
            mon = q.groupby("act").usdc.sum()
            mon = (mon / mon.sum()).sort_values(ascending=False)
            extra = ""
            if clase == "HIBRIDO":
                mk, tk = q[q.rol == "maker"], q[q.rol == "tomador"]
                ambos = set(mk.mkt) & set(tk.mkt)
                extra = (f" | maker: vol {mk.usdc.sum():.0f} PnL {mk.pnl.sum():+.0f} p50 {mk.p.median():.2f} T50 {mk['T'].median():.0f}"
                         f" | tomador: vol {tk.usdc.sum():.0f} PnL {tk.pnl.sum():+.0f} p50 {tk.p.median():.2f} T50 {tk['T'].median():.0f}"
                         f" | mercados con ambos roles {len(ambos)}/{q.mkt.nunique()}")
            L(f"   {w[:10]} PnL {q.pnl.sum():+7.0f} PnL/vol {q.pnl.sum() / q.usdc.sum():+.3f} merc {q.mkt.nunique():4d} "
              f"%merc>0 {(pm > 0).mean():.0%} p50 {q.p.median():.2f} T50 {q['T'].median():.0f} acc50 {q.acc.median():.0f} "
              f"{', '.join(f'{k} {x:.0%}' for k, x in mon.head(3).items())}{extra}")
        # perfil agregado de las persistentes vs el resto de la clase
        P = X[(X.clase == clase) & X.wallet.isin(pers.index)]
        R = X[(X.clase == clase) & ~X.wallet.isin(pers.index)]
        for nom, q in (("persistentes", P), ("resto", R)):
            if len(q) == 0:
                continue
            L(f"   [{nom}] vol {q.usdc.sum() / 1e3:.0f}k PnL/vol {q.pnl.sum() / q.usdc.sum():+.4f} | precio: "
              + ", ".join(f"{b} {x:.0%}" for b, x in pd.cut(q.p, [0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.97, 1.0]).value_counts(normalize=True).sort_index().items())
              + " | T: " + ", ".join(f"{b} {x:.0%}" for b, x in pd.cut(q["T"], [-100, 0, 30, 120, 300, 600, 900, 3000]).value_counts(normalize=True).sort_index().items()))
    INF.write_text("\n".join(lin) + "\n")


if __name__ == "__main__":
    main()
