import pandas as pd, numpy as np
for D in ["2026-10-10","2026-10-11","2026-10-12","2026-10-13"]:
    X=pd.read_csv(f"xq_{D}.csv.gz",names=["mon","T","p","q","m","E","rx"],dtype={"mon":str})
    print(D,len(X)); print(X.groupby("mon").size().to_dict())
    d=X.duplicated(["mon","T","p","q","m"]).sum(); print(" dup(mon,T,p,q,m)",d)
    X=X.sort_values("rx"); b=X[X.mon=="BTC"]
    g=np.diff(b.rx.values); print(" BTC gaps>5s:",(g>5000).sum()," >60s:",(g>60000).sum(), "median dt",np.median(g), "n/hour", len(b)/24)
    print(" rx-T p10/50/90", np.percentile(X.rx-X["T"],[10,50,90]))
