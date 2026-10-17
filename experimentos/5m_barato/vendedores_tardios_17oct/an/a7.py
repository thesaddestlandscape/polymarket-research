exec(open("common.py").read())
wid=pickle.load(open("wid.pkl","rb")); inv={v:k for k,v in wid.items()}
L=P[(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")].copy()
T=L.groupby("tk").agg(pn=("pnl_l","sum"),c=("c_l","sum")).sort_values("pn")
pos=T.sort_values("pn",ascending=False).head(12).index.tolist(); neg=T.head(8).index.tolist()
def perfil(t):
    x=L[L.tk==t]
    u=x.groupby(["mkt","lado"]).agg(a=("acc_l","sum"),pn=("pnl_l","sum"),c=("c_l","sum"))
    st=lambda f: ((x.inv_s>0.5)&(x.cl=="VENDE_s")).mean()
    return dict(w=inv[t][:10],n=len(x),unid=len(u),dias=x.dia.nunique(),acc_u=round(u.a.mean()),pxm=round(x.c_l.sum()/x.acc_l.sum(),3),pxtk=round(1-x.c_l.sum()/x.acc_l.sum(),3),Tm=round(x["T"].mean()),
      vende=round((x.cl=="VENDE_s").mean(),2),dueno_ns=round((x.inv_ns>0.5).mean(),2),dueno_s=round((x.inv_s>0.5).mean(),2),btc=round((x.act=="BTC").mean(),2),
      winrate_unid=round((u.pn>0).mean(),2),ev=round(x.pnl_l.sum()/x.c_l.sum(),2),hora_med=int(pd.to_datetime(x.fin,unit="s").dt.hour.median()),
      dias_lista=",".join(sorted(set(d[8:] for d in x.dia.astype(str).unique()))))
print("POSITIVOS (pierden contra los bids)"); print(pd.DataFrame([perfil(t) for t in pos]).to_string())
print("NEGATIVOS (ganan contra los bids)"); print(pd.DataFrame([perfil(t) for t in neg]).to_string())
