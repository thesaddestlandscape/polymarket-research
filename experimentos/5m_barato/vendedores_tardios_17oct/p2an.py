import pandas as pd, numpy as np, glob
W=[l.strip() for l in open("w6.txt")]
X=pd.concat([pd.read_csv(f).assign(dia=f[-6:-4]) for f in sorted(glob.glob("p2/p2_*.csv"))])
B=X[X.act=="BTC"].copy(); B["six"]=B.wallet.isin(W)
print("BTC 5m, volumen MAKER (acciones, miles) por lado y dia; share de las 6")
t=B.groupby(["dia","side"]).apply(lambda x: pd.Series({"acc_k":x.acc.sum()/1e3,"share6":x[x.six].acc.sum()/x.acc.sum(),"wallets":x.wallet.nunique()}),include_groups=False).unstack("side").round(3)
print(t.to_string())
cheap=B[(B.side==1)&(B.pb<=1)]   # venta maker a precio token <0.10  (pb 0,1 = <0.05, <0.10)
print("\nVENTAS maker de tokens BARATOS (<0,10): acc miles, share de las 6, wallets, top1/top5/top10 share")
rows=[]
for d,x in cheap.groupby("dia"):
    g=x.groupby("wallet").acc.sum().sort_values(ascending=False); tot=g.sum()
    rows.append((d,tot/1e3,x[x.six].acc.sum()/tot,len(g),g.iloc[0]/tot,g.head(5).sum()/tot,g.head(10).sum()/tot))
print(pd.DataFrame(rows,columns=["dia","acc_k","share6","wallets","top1","top5","top10"]).round(3).to_string(index=False))
# perfil "vendedor puro" : side1 >=90% del volumen maker BTC 5m y precios en >=5 tramos
S=B.groupby(["wallet","side"]).acc.sum().unstack(fill_value=0); S.columns=["buy","sell"]
S["fr_sell"]=S.sell/(S.sell+S.buy)
sel=S[(S.fr_sell>0.9)&(S.sell>20000)].index
print("\nvendedores puros BTC 5m (>=90% ventas, >20k acc en 11 dias):",len(sel))
D=B[B.wallet.isin(sel)&(B.side==1)].groupby(["wallet","dia"]).agg(acc=("acc","sum"),n=("n","sum")).acc.unstack(fill_value=0)
D["six"]=D.index.isin(W); D["tot"]=D.drop(columns="six").sum(axis=1)
D=D.sort_values("tot",ascending=False)
D.index=[i[:10]+("*" if s else "") for i,s in zip(D.index,D.six)]
print((D.drop(columns=["six","tot"])/1e3).round(0).head(25).to_string())
print("suma de TODOS los vendedores puros por dia (k):",(D.drop(columns=["six","tot"]).sum()/1e3).round(0).to_dict())
six=D[D.six].drop(columns=["six","tot"]).sum()
print("suma de las 6 (k):",(six/1e3).round(0).to_dict())
oth=D[~D.six].drop(columns=["six","tot"]).sum()
print("suma otros vendedores puros (k):",(oth/1e3).round(0).to_dict())
