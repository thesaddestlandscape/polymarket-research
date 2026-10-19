import csv, sys, random
from collections import defaultdict
def load(v):
    return [dict(dia=r["dia"],mkt=r["mkt"],lado=r["lado"],fin=int(r["fin"]),act=r["act"],c=float(r["c"]),p=float(r["p"]),acc=float(r["acc"])) for r in csv.DictReader(open(f"units_{v}.csv"))]
def ic(units,key,B=2000,seed=11):
    g=defaultdict(lambda:[0.0,0.0])
    for u in units: x=g[u[key]]; x[0]+=u["c"]; x[1]+=u["p"]
    g=list(g.values())
    if len(g)<3: return None
    rng=random.Random(seed); bs=[]
    for _ in range(B):
        m=[rng.choice(g) for _ in g]; c=sum(x[0] for x in m); bs.append(sum(x[1] for x in m)/c if c else 0)
    bs.sort(); return (round(bs[int(B*.05)],3),round(bs[int(B*.95)-1],3))
def resumen(units,nom):
    if not units: print(nom,"vacio"); return
    c=sum(u["c"] for u in units); p=sum(u["p"] for u in units)
    pd_=defaultdict(lambda:[0.0,0.0,0])
    for u in units: x=pd_[u["dia"]]; x[0]+=u["c"]; x[1]+=u["p"]; x[2]+=1
    top=sorted(units,key=lambda u:u["p"],reverse=True)[20:]
    s20=sum(u["p"] for u in top)/sum(u["c"] for u in top) if top else None
    mej=sorted(pd_,key=lambda d:pd_[d][1],reverse=True)[:2]
    r=[v for d,v in pd_.items() if d not in mej]
    s2=sum(v[1] for v in r)/sum(v[0] for v in r) if r and sum(v[0] for v in r) else None
    pu=sum(u["p"]/u["c"] for u in units if u["c"])/len(units)
    acc=sum(u["acc"] for u in units)
    print(f"{nom}: n={len(units)} dias={len(pd_)} coste={c:.0f} EV_pond={p/c:+.4f} EV_unidad={pu:+.4f} IC90cierre={ic(units,'fin')} IC90dias={ic(units,'dia')} sin2mejoresdias={None if s2 is None else round(s2,4)} sinTop20={None if s20 is None else round(s20,4)} px_medio={c/acc:.3f} dias+={sum(1 for v in pd_.values() if v[1]>0)}/{len(pd_)}")
    return pd_
if __name__=="__main__":
    lo,hi=sys.argv[1],sys.argv[2]
    for v in sys.argv[3:]:
        U=[u for u in load(v) if lo<=u["dia"]<=hi]
        pd_=resumen(U,f"{v} {lo}..{hi}")
        if pd_: print("   por dia:"," ".join(f"{d[5:]}:{x[1]/x[0]:+.2f}({x[2]})" for d,x in sorted(pd_.items())))
