exec(open("common.py").read())
rng=np.random.default_rng(5)
L=P[(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")].copy()
L["hora"]=pd.to_datetime(L.fin,unit="s").dt.hour
print("cobertura p60 notna: %.3f ; p10 notna %.3f"%(L.p60.notna().mean(),L.p10.notna().mean()))
L["d60"]=L.p60-L.pc
def estrato(x):
    return pd.cut(x.d60,[-1,0.0,0.03,0.06,0.10,1.0],right=True)
L["e60"]=estrato(L); 
def res(x,tag):
    s=x[x.per=="SEL"]; m=x[x.per=="MEAS"]
    dd=x.groupby("dia",observed=True).apply(lambda y: pd.Series({"ev":ev(y.pnl_l,y.c_l),"pn":y.pnl_l.sum(),"c":y.c_l.sum()}),include_groups=False)
    ci=np.percentile([ (lambda i: dd.pn.values[i].sum()/dd.c.values[i].sum())(rng.integers(0,len(dd),len(dd))) for _ in range(3000)],[5,95])
    print(f"{tag:42} n {len(x):7d} coste {x.c_l.sum():9.0f} EV {ev(x.pnl_l,x.c_l):+.4f} | SEL {ev(s.pnl_l,s.c_l):+.4f} MEAS {ev(m.pnl_l,m.c_l):+.4f} | dias+ {(dd.ev>0).sum()}/{len(dd)} IC90dias ({ci[0]:+.3f},{ci[1]:+.3f})")
print("Por caida del precio de s en los 60 s previos (p60-pc): ")
for k,x in L.groupby("e60",observed=True): res(x,f"d60 {k}")
res(L[L.p60.isna()],"p60 missing (sin trade >=60 s)")
res(L,"TODO tardio")
res(L[(L.cum0>=2000)],"cum0>=2000")
res(L[(L.cum0>=2000)&(L.d60<=0.03)],"cum0>=2000 & caida<=3c")
res(L[(L.cum0>=2000)&(L.d60>0.03)],"cum0>=2000 & caida>3c")
res(L[(L.d60<=0.03)],"caida<=3c")
res(L[(L.d60<=0.03)&L.hora.between(8,19)],"caida<=3c & 08-19Z")
res(L[(L.cum0>=2000)&L.hora.between(8,19)],"cum0>=2000 & 08-19Z")
res(L[(L.cum0>=2000)&(L.d60<=0.03)&L.hora.between(8,19)],"cum0>=2000 & caida<=3c & 08-19Z")
res(L[(L.cum0>=1000)&(L.d60<=0.03)&L.hora.between(8,19)],"cum0>=1000 & caida<=3c & 08-19Z")
# tamano de tomador
res(L[L.tk_acc>200],"tomador fill>200 acc")
res(L[(L.tk_acc>200)&(L.d60<=0.03)],"tomador>200 & caida<=3c")
