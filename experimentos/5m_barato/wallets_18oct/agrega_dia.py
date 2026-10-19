#!/usr/bin/env python3
"""agrega_dia.py DIA -- tablas pequeñas por día desde fills_D.parquet (celda H5M, desenlace oficial). Salida: agg_D.pkl en CACHE.
Reproduce la contabilidad del validador (PnL/coste maker de la celda por día) para comprobar."""
import sys, pickle
import numpy as np, pandas as pd
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib import *
d = sys.argv[1]
src = sys.argv[2] if len(sys.argv) > 2 else CACHE + f"fills_{d}.parquet"
F = pd.read_parquet(src)
Mk = F[F.is_tk == 0]
Sm = F[F.is_tk == 1]
X = en_celda(deriva(Mk))
X, cob = con_resultado(X)
X["dia"] = d
X["via_compra_fav"] = X.venta          # el maker VENDE el token -> el tomador COMPRA el token (favorito) directamente
X["unidad_m"] = X.mkt.astype(str) + "_" + X.lado_c
print(d, "fills celda", len(X), "cobertura desenlace", round(cob, 4), "coste_m", round(X.coste_m.sum(), 2), "pnl_m", round(X.pnl_m.sum(), 2),
      "EV pond", round(X.pnl_m.sum() / X.coste_m.sum(), 4), "| pnl_t", round(X.pnl_t.sum(), 2), "coste_t", round(X.coste_t.sum(), 2))
A = {"dia": d, "cobertura": cob, "n": len(X), "coste_m": X.coste_m.sum(), "pnl_m": X.pnl_m.sum(), "coste_t": X.coste_t.sum(), "pnl_t": X.pnl_t.sum()}
# por tomador
X["q"] = 1 - X.pc
X["w_q"] = X.q * X.sh; X["w_T"] = X["T"] * X.coste_t; X["win_t"] = np.where(X.lado_c != X.des, X.sh, 0.0)
X["tk_unit"] = X.taker + "_" + X.mkt.astype(str) + "_" + X.lado_c
g = X.groupby(["taker", "act"])
TK = g.agg(n=("sh", "size"), sh=("sh", "sum"), coste_t=("coste_t", "sum"), pnl_t=("pnl_t", "sum"), w_q=("w_q", "sum"), win_t=("win_t", "sum"),
           w_T=("w_T", "sum"), n_tx=("tx", "nunique"), n_mkt=("mkt", "nunique"), fav_directo=("via_compra_fav", "mean")).reset_index()
TK["dia"] = d
A["TK"] = TK
# por maker
g = X.groupby(["maker", "act"])
MK = g.agg(n=("sh", "size"), sh=("sh", "sum"), coste_m=("coste_m", "sum"), pnl_m=("pnl_m", "sum"), n_mkt=("mkt", "nunique"), n_oh=("tx", "nunique")).reset_index()
MK["dia"] = d
A["MK"] = MK
# por cierre y moneda
CI = X.groupby(["fin", "act"]).agg(n=("sh", "size"), coste_m=("coste_m", "sum"), pnl_m=("pnl_m", "sum"), n_tk=("taker", "nunique"), n_mk=("maker", "nunique"),
                                   win_c=("pnl_m", lambda s: 0)).drop(columns="win_c").reset_index()
CI["dia"] = d
A["CI"] = CI
# por hora UTC y moneda
X["hora"] = pd.to_datetime(X.ts, unit="s").dt.hour
A["HR"] = X.groupby(["hora", "act"]).agg(n=("sh", "size"), coste_m=("coste_m", "sum"), pnl_m=("pnl_m", "sum")).reset_index().assign(dia=d)
# pares tomador x maker (top por coste para ver relaciones): agregado
PM = X.groupby(["taker", "maker"]).agg(coste_m=("coste_m", "sum"), pnl_m=("pnl_m", "sum"), n=("sh", "size")).reset_index()
A["PM"] = PM[PM.coste_m > 50].assign(dia=d)
# unidad tomador x cierre x moneda (para bootstrap por cierre de cualquier grupo de tomadores)
A["UN"] = X.groupby(["taker", "fin", "act"]).agg(sh=("sh", "sum"), w_q=("w_q", "sum"), win_t=("win_t", "sum"), coste_t=("coste_t", "sum"), pnl_t=("pnl_t", "sum"),
                                                  coste_m=("coste_m", "sum"), pnl_m=("pnl_m", "sum")).reset_index().assign(dia=d)
# resumen de las ordenes tomadoras (todas las bandas): numero de ordenes y cuantas tocan la celda
Sm = Sm.copy(); Sm["dia"] = d
A["n_resumenes_tomador"] = len(Sm)
# tamano por orden tomadora y niveles barridos (celda)
O = X.groupby("tx").agg(taker=("taker", "first"), act=("act", "first"), sh=("sh", "sum"), niveles=("pc", "nunique"), n_mk=("maker", "nunique"),
                        coste_t=("coste_t", "sum"), pnl_t=("pnl_t", "sum"), T=("T", "mean"), ts=("ts", "min")).reset_index().assign(dia=d)
A["ORD"] = O
out = sys.argv[3] if len(sys.argv) > 3 else CACHE + f"agg_{d}.pkl"
pickle.dump(A, open(out, "wb"))
print("->", out)
