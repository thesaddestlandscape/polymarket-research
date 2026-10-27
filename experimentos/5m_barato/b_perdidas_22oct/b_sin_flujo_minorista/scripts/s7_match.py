"""s7: empareja rellenos de B (U isB) con ordenes del ledger; offset de reloj; guarda UB (U 20-24 ETH/SOL/XRP, columnas minimas)."""
import numpy as np, pandas as pd
NEW="/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"
U = pd.read_pickle("/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado/U.pkl")
U = U[U.act.astype(str).isin(["ETH","SOL","XRP"]) & U.dia.astype(str).isin(["2026-10-%d"%d for d in (20,21,22,23)])]
cols = ["ts","mkt","act","cierre","lado","acc","usd","p","maker","taker","cl","cob","pnl","c","dia","T","isB","tk_roi"]
U = U[cols].copy()
U24 = pd.read_pickle(NEW+"/U24.pkl"); U24 = U24[U24.act.astype(str).isin(["ETH","SOL","XRP"])][cols].copy()
for c in ("maker","taker","mkt","act","lado","cl","dia"):
    U[c]=U[c].astype(str); U24[c]=U24[c].astype(str)
U = pd.concat([U,U24], ignore_index=True)
U["p"]=U.p.round(4)
U.to_pickle(NEW+"/UB.pkl"); print("UB", len(U), U.groupby("dia").size().to_dict(), "B", int(U.isB.sum()))
O = pd.read_pickle(NEW+"/ordenes_B.pkl"); O["act"]=O.coin.str.upper()
F = O[O.filled].copy()
Bf = U[U.isB].copy().reset_index(drop=True)
# emparejar: (act, cierre, lado, precio) y acc ~ f ; el ledger puede tener varias lecturas por orden; usamos greedy por tiempo
Bf["k"]=Bf.act+"|"+Bf.cierre.astype(int).astype(str)+"|"+Bf.lado+"|"+Bf.p.round(2).astype(str)
F["k"]=F.act+"|"+F.cierre.astype(int).astype(str)+"|"+F.lado+"|"+F.precio.round(2).astype(str)
F["t_det"]=F.t_arm+F.espera_s
m = F.merge(Bf.reset_index().rename(columns={"index":"bi"}), on="k", suffixes=("","_u"))
m["dt"]=m.ts - m.t_det
print("pares candidatos", len(m), "ordenes con fill", len(F), "B rellenos", len(Bf))
print(m.dt.describe(percentiles=[.1,.5,.9]))
off = m[(m.dt>-5)&(m.dt<15)].dt.median(); print("offset ts_onchain - t_deteccion ledger (s):", off)
m["dt2"]=m.dt-off
mm = m[m.dt2.abs()<6].sort_values("dt2",key=abs).drop_duplicates("oid").drop_duplicates("bi")
print("emparejados", len(mm), "de", len(F), "ordenes y", len(Bf), "rellenos B; |dt2| p50/p90", mm.dt2.abs().quantile([.5,.9]).round(2).tolist())
mm.to_pickle(NEW+"/match_B.pkl"); open(NEW+"/offset.txt","w").write(str(off))
