#!/usr/bin/env python3
"""H5M BTC: EV/€ de los rellenos maker de la banda barata 5m por pares_antes (otro lado ya comprado ANTES), día y banda (14-Oct, exploratorio)."""
import pandas as pd, numpy as np
O="/root/polymarket-research-datalogs/h5m_cola_sim/"
C=pd.concat([pd.read_csv(O+f"quien_gana_rellenos_v2_2026-10-{d}.csv.gz",usecols=["wallet","act","mkt","acc","lado_c","pc","coste","pares_antes","des","pnl","dia"],dtype={"mkt":str}) for d in ("09","10","11","12","13")])
C=C[C.act=="BTC"]
C["pb"]=(C.pc//0.05*0.05).round(2)
ev=lambda x: x.pnl.sum()/x.coste.sum()
print("BTC por día y pares_antes (EV/€ por relleno; unidades mercado-lado-wallet aparte)")
print(C.groupby(["dia","pares_antes"]).apply(ev).unstack().round(4).to_string())
U=C.groupby(["wallet","mkt","lado_c","pares_antes"]).agg(pnl=("pnl","sum"),coste=("coste","sum"),dia=("dia","first"),pb=("pb","first")).reset_index()
print("\nunidades (wallet,mercado,lado): EV/€ por pares_antes y banda de precio")
print(U.groupby(["pb","pares_antes"]).apply(lambda x: pd.Series({"n":len(x),"ev":ev(x)})).unstack().round(4).to_string())
rng=np.random.default_rng(1)
for pa in (False,True):
  d=U[U.pares_antes==pa].groupby("dia").agg(p=("pnl","sum"),c=("coste","sum"))
  print(pa, "EV por día", (d.p/d.c).round(4).tolist())
