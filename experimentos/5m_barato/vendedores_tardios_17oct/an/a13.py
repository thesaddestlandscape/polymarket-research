exec(open("common_s.py").read())
rng=np.random.default_rng(9)
P=P[(P.dia!="2026-10-05")&(P.dia!="2026-10-17")&(P.cum0+P.acc>500)][["mkt","lado","fin","dia","per","cum0","acc","coste","pnl","pc","T"]].copy()
off=2000.0
def firstK(K,off=off):
    lo=np.clip(P.cum0-off,0,None); hi=np.clip(P.cum0+P.acc-off,0,None)
    tk=np.clip(np.minimum(K,hi)-np.minimum(K,lo),0,None)   # acciones de este relleno dentro de las primeras K tras cruzar off
    f=(tk/P.acc).values
    return f

for off in (500.0,1000.0,2000.0,3000.0,5000.0,8000.0):
  print("== offset (cum minima antes de empezar a contar)",off)
  for K in (5,50,200,1e12):
    lo=np.clip(P.cum0-off,0,None); hi=np.clip(P.cum0+P.acc-off,0,None)
    tk=np.clip(np.minimum(K,hi)-np.minimum(K,lo),0,None); f=(tk/P.acc).values
    x=P.assign(c=P.coste*f,p=P.pnl*f)
    g=x.groupby(["dia","mkt","lado"],observed=True)[["c","p"]].sum().reset_index(); g=g[g.c>0]
    gd=g.groupby("dia",observed=True)[["c","p"]].sum()
    gp=g.merge(x.drop_duplicates(["dia","mkt","lado"])[["dia","mkt","lado","per","fin"]],on=["dia","mkt","lado"])
    sS=gp[gp.per=="SEL"]; m=gp[gp.per=="MEAS"]
    gc_=gp.groupby("fin")[["c","p"]].sum()
    bs=np.percentile([gc_.p.values[i].sum()/gc_.c.values[i].sum() for i in (rng.integers(0,len(gc_),len(gc_)) for _ in range(800))],[5,95])
    u=g.sort_values("p",ascending=False)
    print(f"  K={K:>6g}: unidades {len(g):5d} coste {g.c.sum():9.0f} EV {g.p.sum()/g.c.sum():+.4f} | SEL {sS.p.sum()/sS.c.sum():+.4f} MEAS {m.p.sum()/m.c.sum():+.4f} | dias+ {((gd.p>0).sum())}/{len(gd)} | IC90 cierres ({bs[0]:+.3f},{bs[1]:+.3f}) | sinTop20u {u.p.iloc[20:].sum()/u.c.iloc[20:].sum():+.4f}")
