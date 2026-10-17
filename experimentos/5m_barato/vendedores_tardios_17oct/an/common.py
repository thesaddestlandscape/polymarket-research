import pandas as pd, numpy as np, pickle
P=pd.read_pickle("/tmp/claude-0/-root-polymarket-research/a0c96fc2-2902-4388-9cab-9cffc412228c/scratchpad/vend/an/P.pkl")
g=P.groupby(["mkt","lado"],sort=False)
cum0=g.acc.cumsum()-P.acc
P["cum0"]=cum0.astype("float32")
tk_=np.clip(P.acc-np.clip(500-P.cum0,0,None),0,None)   # acciones por encima de 500 acumuladas
P["w_late"]=(tk_/P.acc).astype("float32")
P["acc_l"]=(P.acc*P.w_late).astype("float32"); P["c_l"]=(P.coste*P.w_late).astype("float32")
P["pnl"]=(P.acc*P.gana-P.coste).astype("float32"); P["pnl_l"]=(P.pnl*P.w_late).astype("float32")
P["pnl_e"]=P.pnl-P.pnl_l; P["c_e"]=P.coste-P.c_l
def ev(pn,c): 
    c=float(np.sum(c)); return float(np.sum(pn)/c) if c>0 else float("nan")
SEL=["2026-10-05","2026-10-06","2026-10-07","2026-10-08","2026-10-09"]
MEAS=[f"2026-10-{d}" for d in range(10,17)]
P["per"]=np.where(P.dia.isin(SEL),"SEL",np.where(P.dia.isin(MEAS),"MEAS","otro"))
import os
if os.environ.get("SLIM"):
    P=P[["ts","mkt","lado","act","pc","acc","coste","T","mk","tk","cl","tk_acc","cum0","acc_l","c_l","pnl","pnl_l","dia","per","fin","gana","p60","p10","inv_s","inv_ns","nf_prev","nmk"]].copy()
    import gc; gc.collect()
