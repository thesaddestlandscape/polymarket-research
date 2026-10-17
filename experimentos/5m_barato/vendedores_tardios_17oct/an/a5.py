exec(open("common.py").read())
rng=np.random.default_rng(7)
L=P[(P.dia!="2026-10-05")&(P.dia!="2026-10-17")&(P.cum0>=500)].copy()
# subconjunto estricto "fills con cum0>=500" (sin prorrata)
def cl_boot(x,col_c,col_p,key,nb=2000):
    g=x.groupby(key,observed=True)[[col_p,col_c]].sum()
    pn=g[col_p].values; c=g[col_c].values; n=len(g)
    out=[]
    for _ in range(nb):
        i=rng.integers(0,n,n); out.append(pn[i].sum()/c[i].sum())
    return np.percentile(out,[5,50,95])
for th in [500,1000,2000,5000,10000]:
    x=L[L.cum0>=th]
    print(f"\n=== regla cum0>={th}: n {len(x)}  coste {x.coste.sum():.0f}  EV {ev(x.pnl,x.coste):+.4f}  px {x.coste.sum()/x.acc.sum():.3f}")
    for per in ["SEL","MEAS"]:
        y=x[x.per==per]; print(f"  {per}: n {len(y)} coste {y.coste.sum():.0f} EV {ev(y.pnl,y.coste):+.4f} mkts {y.mkt.nunique()} unidades {y.groupby(['mkt','lado']).ngroups}")
    d=x.groupby("dia",observed=True).apply(lambda y: pd.Series({"ev":ev(y.pnl,y.coste),"c":y.coste.sum(),"pn":y.pnl.sum()}),include_groups=False)
    print("  por dia:", d.ev.round(3).to_dict())
    print("  IC90 bootstrap por dia: ",np.percentile([ (lambda i: d.pn.values[i].sum()/d.c.values[i].sum())(rng.integers(0,len(d),len(d))) for _ in range(3000)],[5,95]).round(3))
    print("  IC90 bootstrap por cierre(fin): ",cl_boot(x,"coste","pnl","fin").round(3))
    # sin 2 mejores dias
    dd=d.sort_values("ev",ascending=False).iloc[2:]
    print("  EV sin 2 mejores dias: %.4f"%(dd.pn.sum()/dd.c.sum()))
    # sin top5 unidades por pnl
    u=x.groupby(["mkt","lado"]).agg(pn=("pnl","sum"),c=("coste","sum")).sort_values("pn",ascending=False)
    print("  EV sin top5 unidades: %.4f ; sin top20: %.4f ; unidades %d"%(u.pn.iloc[5:].sum()/u.c.iloc[5:].sum(),u.pn.iloc[20:].sum()/u.c.iloc[20:].sum(),len(u)))
    # MEAS only con selección en SEL
