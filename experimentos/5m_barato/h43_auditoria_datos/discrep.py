import csv, sys
from stats import load
A={ (u["mkt"],u["lado"]):u for u in load("DISC_BTC_T")}   # dia = cierre, cum global
B={}
Bl=load("VIG")
from collections import defaultdict
Bm=defaultdict(list)
for u in Bl: Bm[(u["mkt"],u["lado"])].append(u)
def fmt(u): return f'{u["dia"][5:]} c={u["c"]:.2f} p={u["p"]:+.2f}'
causas=defaultdict(lambda:[0,0.0,0.0])
rows=[]
keys=set(A)|set(Bm)
for k in keys:
    a=A.get(k); b=Bm.get(k,[])
    if a and len(b)==1 and abs(a["c"]-b[0]["c"])<0.005 and a["dia"]==b[0]["dia"]:
        continue
    cb=sum(x["c"] for x in b); pb=sum(x["p"] for x in b)
    ca=a["c"] if a else 0; pa=a["p"] if a else 0
    if a and not b: cz="solo DISC (cum global/otra fecha)"
    elif b and not a: cz="solo VIG (fuera de rango de dias DISC o cum reiniciado)"
    elif len(b)>1: cz="VIG parte la unidad en 2 ficheros (medianoche)"
    elif a["dia"]!=b[0]["dia"]: cz="misma unidad, distinto dia (dia fichero vs cierre)"
    else: cz="mismo dia, distinto importe (cum reiniciado en medianoche)"
    x=causas[cz]; x[0]+=1; x[1]+=ca-cb; x[2]+=pa-pb
    rows.append((k,cz,a and fmt(a),[fmt(x) for x in b]))
print("DISC_BTC_T (dias 05-17) vs VIG: unidades distintas",len(rows),"de",len(keys))
for cz,x in causas.items(): print(f"  {cz}: n={x[0]} dCoste={x[1]:+.1f} dPnL={x[2]:+.1f}")
