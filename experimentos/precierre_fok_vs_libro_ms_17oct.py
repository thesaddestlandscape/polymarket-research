import csv, gzip, json, sys, bisect, requests
from datetime import datetime
sys.path.insert(0, "/root/polymarket-research")
from comision_cripto import pnl_por_euro
R="/root/polymarket-research"; DL="/root/polymarket-research-datalogs"
cache=json.load(open(R+"/data/live/precierre_variantes_outcomes.json"))
sends=[]
for r in csv.DictReader(open(R+"/data/shadow/resolution_sniper_precierre_executor_v2.csv")):
    if r["timestamp_utc"]<"2026-09-29T10" or r.get("disparado")!="True" or r.get("dry_run")=="True": continue
    sends.append(r)
miss=[s["market_id"] for s in sends if s["market_id"] not in cache]
for i in range(0,len(miss),20):
    js=requests.get("https://gamma-api.polymarket.com/markets",params=[("id",m) for m in miss[i:i+20]]+[("closed","true")],timeout=20).json()
    for m in js:
        o=json.loads(m["outcomes"]); p=[float(x) for x in json.loads(m["outcomePrices"])]
        if max(p)>=0.99: cache[str(m["id"])]=o[p.index(max(p))]
books={}
def libro(day):
    if day in books: return books[day]
    d={}
    try:
        with gzip.open(f"{DL}/precierre_libro_ms_{day}.csv.gz","rt") as f:
            for r in csv.DictReader(f):
                if r["tipo"]!="book" or r["token"]!="YES": continue
                d.setdefault(r["market_id"],[]).append((int(r["rel_fin_ms"]),float(r["best_bid"] or 0),float(r["best_ask"] or 1)))
    except FileNotFoundError: pass
    for k in d: d[k].sort()
    books[day]=d; return d
def ask_at(ser,rel,up):
    i=bisect.bisect_right([x[0] for x in ser],rel)-1
    if i<0: return None
    _,b,a=ser[i]; return a if up else round(1-b,4)
print("fecha mk marco act dir ask_dec | ask+0 +300 +600 +1000 | out ok/muerta EV€/€@+600")
agg={"ok":[], "muerta":[]}
for s in sends:
    day=s["timestamp_utc"][:10]; ser=libro(day).get(s["market_id"])
    rel=float(s["t_envio_rel_cierre_s"] or 0)*1000; up=s["direccion_implicita"]=="Up"
    est="muerta" if "fully filled" in (s["order_error"] or "") else ("ok" if s["order_ok"]=="True" else "otro:"+(s["order_error"] or "")[:30])
    out=cache.get(s["market_id"]); gana=None if out is None else int(out==s["direccion_implicita"])
    asks=[ask_at(ser,rel+d,up) if ser else None for d in (0,300,600,1000)]
    ev=None
    if gana is not None and asks[2]: ev=round(pnl_por_euro(asks[2],gana),3)
    evdec=round(pnl_por_euro(float(s["ask_implicita"]),gana),3) if gana is not None else None
    if est in agg: agg[est].append((gana,ev,evdec,asks))
    print(day,s["market_id"],s["marco"],s["activo"],s["direccion_implicita"],s["ask_implicita"],"|",*asks,"|",out,est,ev)
for k,v in agg.items():
    g=[x[0] for x in v if x[0] is not None]; e=[x[1] for x in v if x[1] is not None]; e0=[x[2] for x in v if x[2] is not None]
    print(k,"n",len(v),"acierto",sum(g),"/",len(g),"EV@ask+600ms",round(sum(e)/len(e),3) if e else None,"n",len(e),"EV@ask_decision",round(sum(e0)/len(e0),3) if e0 else None)
