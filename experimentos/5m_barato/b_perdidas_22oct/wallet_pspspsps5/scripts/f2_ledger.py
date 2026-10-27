#!/usr/bin/env python3
"""f2: ledger de pspspsps5 (0xb0f85baa...) 5m on-chain 5-23 Oct. Unidad mercado+lado; desenlace oficial; fee real on-chain.
Salida: units.csv.gz, fills.csv.gz (con desenlace) en datalogs/wallet_pspspsps5/."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
from pathlib import Path
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
OUT = Path("/root/polymarket-research-datalogs/wallet_pspspsps5")
fs = sorted(glob.glob(str(OUT / "rellenos_2026-*.csv.gz")))
R = pd.concat([pd.read_csv(f, dtype={"mkt": str}).assign(dia=Path(f).name[10:20]) for f in fs], ignore_index=True)
des = desenlaces(set(R.mkt))
R["des"] = R.mkt.map(des).fillna("")
print("fills", len(R), "mercados", R.mkt.nunique(), "con desenlace", (R.des != "").mean())
R["win"] = np.where(R.des == "", np.nan, (R.lado == R.des).astype(float))
R["sg"] = np.where(R.compra, 1.0, -1.0)
# pnl por fill: compra: acc*win - usdc - fee ; venta: usdc - acc*win - fee
R["pnl"] = R.sg * (R.acc * R.win - R.usdc) - R.fee
# cierre en dia UTC del cierre
R["dia_cierre"] = pd.to_datetime(R.cierre, unit="s").dt.strftime("%Y-%m-%d")
R.to_csv(OUT / "fills.csv.gz", index=False, compression="gzip")
B = R[R.compra]
U = B.groupby(["mkt", "lado"]).agg(dia=("dia_cierre", "first"), act=("act", "first"), cierre=("cierre", "first"),
        acc=("acc", "sum"), cost=("usdc", "sum"), fee=("fee", "sum"), n=("acc", "size"), pM=("rol", lambda s: (s == "M").mean()),
        T1=("T", "max"), Tmin=("T", "min"), des=("des", "first")).reset_index()
V = R[~R.compra].groupby(["mkt", "lado"]).agg(vac=("acc", "sum"), vus=("usdc", "sum"), vfee=("fee", "sum")).reset_index()
U = U.merge(V, on=["mkt", "lado"], how="left").fillna({"vac": 0, "vus": 0, "vfee": 0})
U["p"] = U.cost / U.acc
U["win"] = np.where(U.des == "", np.nan, (U.lado == U.des).astype(float))
U["pnl"] = (U.acc - U.vac) * U.win - U.cost + U.vus - U.fee - U.vfee
U.to_csv(OUT / "units.csv.gz", index=False, compression="gzip")
print("unidades", len(U), "ventas fills", (~R.compra).sum())
