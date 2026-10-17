exec(open("common_s.py").read())
rng=np.random.default_rng(3)
Pd=P[(P.dia!="2026-10-05")&(P.dia!="2026-10-17")].copy()
Pd["hora"]=pd.to_datetime(Pd.fin,unit="s").dt.hour
def rep(x,tag):
    s=x[x.per=="SEL"]; m=x[x.per=="MEAS"]
    g=x.groupby("fin")[["pnl","coste"]].sum(); pn,c=g.pnl.values,g.coste.values
    bs=np.percentile([pn[i].sum()/c[i].sum() for i in (rng.integers(0,len(g),len(g)) for _ in range(1500))],[5,95])
    u=x.groupby(["mkt","lado"]).agg(pn=("pnl","sum"),c=("coste","sum")).sort_values("pn",ascending=False)
    dd=x.groupby("dia",observed=True).apply(lambda y: ev(y.pnl,y.coste),include_groups=False)
    d2=x.groupby("dia",observed=True)[["pnl","coste"]].sum().assign(e=lambda z:z.pnl/z.coste).sort_values("e",ascending=False).iloc[2:]
    print(f"{tag}: n {len(x)} coste {x.coste.sum():.0f} unidades {len(u)} cierres {len(g)} | EV {ev(x.pnl,x.coste):+.3f} SEL {ev(s.pnl,s.coste):+.3f} (coste {s.coste.sum():.0f}) MEAS {ev(m.pnl,m.coste):+.3f} (coste {m.coste.sum():.0f}) | dias+ {(dd>0).sum()}/{len(dd)} | IC90 cierres ({bs[0]:+.3f},{bs[1]:+.3f}) | sin2mejoresdias {d2.pnl.sum()/d2.coste.sum():+.3f} sinTop5u {u.pn.iloc[5:].sum()/u.c.iloc[5:].sum():+.3f} sinTop20u {u.pn.iloc[20:].sum()/u.c.iloc[20:].sum():+.3f}")
    return dd
late=Pd[Pd.cum0>=500]
rep(late,"BASE: todo volumen cum0>=500")
r1=late[late.cum0>=2000]; rep(r1,"R1 cum0>=2000")
rep(late[late.cum0>=1000],"   cum0>=1000")
rep(r1[(r1.hora>=8)&(r1.hora<16)],"R2 = R1 & 08-16Z")
rep(r1[(r1.hora>=8)&(r1.hora<20)],"   R1 & 08-20Z")
rep(r1[(r1.hora<8)|(r1.hora>=20)],"   R1 & noche (20-08Z)")
rep(late[(late.cum0<2000)],"   NO-R1 (cum0 500-2000)")
# placebo horas: bloque de 8 h aleatorio sobre R1, 24 posibles inicios
base=[]
for h0 in range(24):
    hs=[(h0+i)%24 for i in range(8)]
    x=r1[r1.hora.isin(hs)]; base.append((h0,ev(x.pnl,x.coste),ev(x[x.per=="SEL"].pnl,x[x.per=="SEL"].coste),ev(x[x.per=="MEAS"].pnl,x[x.per=="MEAS"].coste)))
print("placebo/rejilla: EV de R1 en cada bloque de 8 h (inicio h0): ",[(a,round(b,3)) for a,b,_,_ in base])
# R1 por moneda y dia
print("R1 por moneda:",{a:(len(x),round(x.coste.sum()),round(ev(x.pnl,x.coste),3)) for a,x in r1.groupby("act",observed=True)})
print("R1 por dia:",{d:round(ev(x.pnl,x.coste),3) for d,x in r1.groupby("dia",observed=True)})
# capacidad: coste R1 por dia y por mercado
print("R1 coste/dia medio %.0f  unidades/dia %.0f"%(r1.coste.sum()/11, r1.groupby(['mkt','lado']).ngroups/11))
