import pandas as pd, numpy as np
O="/root/polymarket-research-datalogs/wallet_pspspsps5/"
C=pd.read_csv(O+"closed.csv.gz"); C["cost"]=C.avgPrice*C.totalBought
C["dia"]=pd.to_datetime(C.timestamp,unit="s").dt.strftime("%Y-%m-%d")
C["act"]=C.slug.str.split("-").str[0]; C["mar"]=C.slug.str.split("-").str[2]
print("posiciones", len(C), "perdedoras %.1f%%" % (100*(C.realizedPnl<0).mean()), "marcos", C.mar.value_counts().to_dict(), "monedas", C.act.value_counts().to_dict())
d=C.groupby("dia").agg(pnl=("realizedPnl","sum"),c=("cost","sum"),n=("slug","size"))
print(d.loc["2026-09-20":].round(0).to_string())
last=d.loc["2026-09-24":"2026-10-23"]   # 30 dias completos
print("\n30 dias 24-Sep..23-Oct: PnL %.0f coste %.0f EV %.4f verdes %d/%d ; sin 2 mejores dias %.0f ; sin 5 mejores %.0f" % (last.pnl.sum(), last.c.sum(), last.pnl.sum()/last.c.sum(), (last.pnl>0).sum(), len(last), last.pnl.sort_values().iloc[:-2].sum(), last.pnl.sort_values().iloc[:-5].sum()))
for a,b in (("2026-09-24","2026-10-04"),("2026-10-05","2026-10-23")):
    s=d.loc[a:b]; print(a,b,"PnL %.0f coste %.0f EV %.4f verdes %d/%d" % (s.pnl.sum(), s.c.sum(), s.pnl.sum()/s.c.sum(), (s.pnl>0).sum(), len(s)))
tot=d.loc[:"2026-10-23"]; print("desde 01-Sep (53d): PnL %.0f verdes %d/%d" % (tot.pnl.sum(), (tot.pnl>0).sum(), len(tot)))
# otros 30 dias: ventanas moviles de 30d, cuantas con >=24 verdes
dd=d.loc["2026-09-01":"2026-10-23"]; k=[ (dd.pnl.iloc[i:i+30]>0).sum() for i in range(len(dd)-29)]; print("ventanas 30d: verdes min/mediana/max", min(k), np.median(k), max(k), "PnL 30d min/med/max", min(dd.pnl.rolling(30).sum().dropna()).round(0), dd.pnl.rolling(30).sum().median().round(0), max(dd.pnl.rolling(30).sum().dropna()).round(0))
# validacion contra mi ledger on-chain (5-23 Oct)
U=pd.read_csv(O+"units.csv.gz",dtype={"mkt":str})
u=U.groupby("dia").pnl.sum(); cmp=pd.concat([u.rename("mi_ledger"), d.pnl.rename("api_closed")],axis=1).loc["2026-10-06":"2026-10-22"]
print("\ncorrelacion diaria ledger vs closed-positions %.3f ; suma %.0f vs %.0f" % (cmp.corr().iloc[0,1], cmp.mi_ledger.sum(), cmp.api_closed.sum()))
# anuncio: +299217 historico?
print("\nTotal closed-positions desde 01-Sep: %.0f (leaderboard all-time 270478, mes 28923)" % C.realizedPnl.sum())
# top win positions
print(C.nlargest(5,"realizedPnl")[["slug","outcome","avgPrice","totalBought","realizedPnl"]].to_string())
