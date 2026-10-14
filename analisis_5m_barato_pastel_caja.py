#!/usr/bin/env python3
"""analisis_5m_barato_pastel_caja.py -- MISIÓN 5m barato (Javi 14-Oct: "¿200 k€ solo de esta estrategia?"): TAMAÑO DEL
PASTEL de la CAJA 5m/15m entre TODAS las wallets (sin filtro de especialista). SOLO LECTURA sobre las cachés on-chain de
analisis_5m_barato_quien_gana.py (quien_gana_fills_D.csv.gz: 5m que cierran con un 15m + su 15m).

Por (wallet, activo, cierre): exposición neta Up (acciones) en el 5m (toda su vida) y en el 15m SOLO últimos 300 s;
PnL a resolución oficial con comisión. CAJA = signos opuestos y min(|e5|,|e15|)/max(|e5|,|e15|) >= 0,5 (tamaños
comparables). Se informa: nº de cajas, wallets, PnL total/día, PnL por caja, % positivas, concentración (top 1/5/10
wallets), por activo y por día, y PnL de la parte cubierta vs pata sobrante.
Uso: nice -n 19 python3 analisis_5m_barato_pastel_caja.py
Salida: datalogs/m5barato_mision/pastel_caja_informe.txt, pastel_caja_cierres.csv.gz
"""
import glob
from pathlib import Path

import numpy as np
import pandas as pd

D = Path("/root/polymarket-research-datalogs/m5barato_mision")


def main():
    partes = []
    for f in sorted(glob.glob(str(D / "quien_gana_fills_2026-10-*.csv.gz"))):
        dia = Path(f).name[17:27]
        for x in pd.read_csv(f, chunksize=400_000, usecols=["marco", "wallet", "act", "cierre", "lado", "compra", "acc", "T", "pnl"]):
            x = x[(x.marco == "5m") | (x["T"] <= 300)]
            x = x.assign(e=np.where(x.compra, 1, -1) * x.acc * np.where(x.lado == "YES", 1, -1), dia=dia)
            partes.append(x.groupby(["dia", "wallet", "act", "cierre", "marco"]).agg(e=("e", "sum"), pnl=("pnl", "sum")))
        print(dia, flush=True)
    G = pd.concat(partes).groupby(level=[0, 1, 2, 3, 4]).sum().unstack("marco").dropna()
    G.columns = [f"{a}_{b}" for a, b in G.columns]
    e5, e15 = G["e_5m"], G["e_15m"]
    ratio = np.minimum(e5.abs(), e15.abs()) / np.maximum(e5.abs(), e15.abs()).replace(0, np.nan)
    G["caja"] = (np.sign(e5) == -np.sign(e15)) & (ratio >= 0.5)
    G["pnl"] = G.pnl_5m + G.pnl_15m
    C = G[G.caja].reset_index()
    nd = C.dia.nunique()
    L = [f"PASTEL DE LA CAJA 5m/15m (todas las wallets, {nd} días): cierres-wallet con 5m y 15m-últ5: {len(G)}; CAJAS {len(C)} "
         f"({len(C) / max(1, len(G)):.0%}) de {C.wallet.nunique()} wallets"]
    L.append(f"PnL cajas {C.pnl.sum():+,.0f} $ = {C.pnl.sum() / nd:+,.0f} $/día (5m {C.pnl_5m.sum():+,.0f}, 15m {C.pnl_15m.sum():+,.0f}) | "
             f"por caja media {C.pnl.mean():+.2f} mediana {C.pnl.median():+.2f} | positivas {(C.pnl > 0).mean():.0%}")
    pw = C.groupby("wallet").pnl.sum().sort_values(ascending=False)
    pos = pw[pw > 0].sum()
    L.append(f"wallets con PnL de caja > 0: {(pw > 0).sum()} (+{pos:,.0f} $) / < 0: {(pw < 0).sum()} ({pw[pw < 0].sum():+,.0f} $); "
             f"top1 {pw.iloc[0] / pos:.0%}, top5 {pw.iloc[:5].sum() / pos:.0%}, top10 {pw.iloc[:10].sum() / pos:.0%} del PnL positivo")
    L.append("top 10 wallets de caja: " + ", ".join(f"{w[:10]} {v:+,.0f}" for w, v in pw.head(10).items()))
    L.append("por activo: " + ", ".join(f"{a} {v:+,.0f} (n={n})" for a, v, n in
                                         C.groupby("act").agg(v=("pnl", "sum"), n=("pnl", "size")).itertuples()))
    L.append("por día: " + " ".join(f"{d[5:]} {v:+,.0f}" for d, v in C.groupby("dia").pnl.sum().items()))
    pg = C[C.pnl > 0].pnl.sum()
    L.append(f"PnL de las ganadoras persistentes de caja (>= 4 días con caja y PnL de caja > 0 en >= 75 % de esos días): "
             + (lambda P: f"{P.sum():+,.0f} $ en {len(P)} wallets")(
                 C.groupby(["wallet", "dia"]).pnl.sum().groupby("wallet").agg(lambda v: v.sum() if (len(v) >= 4 and (v > 0).mean() >= 0.75) else np.nan).dropna()))
    txt = "\n".join(L)
    print(txt)
    (D / "pastel_caja_informe.txt").write_text(txt + "\n")
    C.to_csv(D / "pastel_caja_cierres.csv.gz", index=False, compression="gzip")


if __name__ == "__main__":
    main()
