exec(open("common_s.py").read())
rng=np.random.default_rng(13)
P=P[(P.dia!="2026-10-05")&(P.dia!="2026-10-17")&(P.cum0+P.acc>500)][["mkt","lado","fin","dia","per","cum0","acc","coste","pnl","pc","T","gana"]].copy()
P["hora"]=pd.to_datetime(P.fin,unit="s").dt.hour
def sel(off,K):
    lo=np.clip(P.cum0-off,0,None); hi=np.clip(P.cum0+P.acc-off,0,None)
    tk=np.clip(np.minimum(K,hi)-np.minimum(K,lo),0,None); f=(tk/P.acc).values
    return P.assign(f=f,c=P.coste*f,p=P.pnl*f,a=P.acc*f,w=P.acc*f*P.gana)
for off,K in [(5000.0,50),(5000.0,200),(3000.0,50)]:
    x=sel(off,K); x=x[x.f>0]
    print(f"\n=== offset {off:g} K {K}: fills {len(x)} unidades {x.groupby(['dia','mkt','lado'],observed=True).ngroups} px medio {x.c.sum()/x.a.sum():.3f} acierto (acc ponderado) {x.w.sum()/x.a.sum():.3f}")
    d=x.groupby("dia",observed=True)[["c","p"]].sum(); d["ev"]=d.p/d.c; d["n"]=x.groupby("dia",observed=True).apply(lambda y:y.groupby(['mkt','lado']).ngroups,include_groups=False)
    print("por dia:",{k[8:]:(round(v.ev,2),int(v.n)) for k,v in d.iterrows()})
    dd=d.sort_values("ev",ascending=False).iloc[2:]; print("sin 2 mejores dias: %.3f"%(dd.p.sum()/dd.c.sum()))
    print("por bloque horario:",{h:(round(y.p.sum()/y.c.sum(),2),y.groupby(['dia','mkt','lado'],observed=True).ngroups) for h,y in x.groupby(x.hora//6*6)})
    print("por T (restante):",{str(b):(round(y.p.sum()/y.c.sum(),2),len(y)) for b,y in x.groupby(pd.cut(x['T'],[60,120,180,240,300]),observed=True)})
    print("por pc:",{str(b):(round(y.p.sum()/y.c.sum(),2),len(y)) for b,y in x.groupby(pd.cut(x.pc,[0.1,0.15,0.2,0.25,0.3]),observed=True)})
    # bootstrap de unidades por dia-bloque (cluster por dia)
