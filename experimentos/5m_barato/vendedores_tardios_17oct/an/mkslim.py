import pandas as pd, numpy as np
P=pd.read_pickle("P.pkl")
P=P.drop(columns=[c for c in ["first_ts","p30","plast","cash","des","file","tk_px"] if c in P])
g=P.groupby(["mkt","lado"],sort=False)
P["cum0"]=(g.acc.cumsum()-P.acc).astype("float32")
w=(np.clip(P.acc-np.clip(500-P.cum0,0,None),0,None)/P.acc).astype("float32")
P["acc_l"]=(P.acc*w).astype("float32"); P["c_l"]=(P.coste*w).astype("float32")
P["pnl"]=(P.acc*P.gana-P.coste).astype("float32"); P["pnl_l"]=(P.pnl*w).astype("float32")
del w
SEL=["2026-10-05","2026-10-06","2026-10-07","2026-10-08","2026-10-09"]
MEAS=[f"2026-10-{d}" for d in range(10,17)]
P["per"]=pd.Categorical(np.where(P.dia.isin(SEL),"SEL",np.where(P.dia.isin(MEAS),"MEAS","otro")))
print(P.memory_usage(deep=True).sum()/1e6, list(P.columns))
P.to_pickle("S.pkl")
