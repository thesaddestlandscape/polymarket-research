import json, numpy as np, pandas as pd
from pathlib import Path
F6=Path("/mnt/HC_Volume_106538179/agentes_datos/f6"); NEW=Path("/mnt/HC_Volume_106538179/agentes_datos/b_sin_flujo"); rng=np.random.default_rng(88)
DES=json.load(open("/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"))
for f in ("/root/polymarket-research-datalogs/mapa_escala/des.json","/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/b_vs_poblacion/datos/des_gamma.json"):
    for k,v in json.load(open(f)).items(): DES.setdefault(k,v)
def win_of(mkt,lado):
    o=pd.Series(mkt).astype(str).map(DES).values; w=np.where(o=="YES",1.0,np.where(o=="NO",0.0,np.nan)); return np.where(np.asarray(lado)=="YES",w,1-w)
def load(d):
    p=F6/f"T_2026-10-{d:02d}.parquet" if d<24 else NEW/"T_2026-10-24.parquet"
    x=pd.read_parquet(p,columns=["ts","w","buy","acc","usd","fee","mkt","lado","cierre","p"]); x["w"]=x.w.astype(str); x["mkt"]=x.mkt.astype(str); x["lado"]=x.lado.astype(str)
    x["win"]=win_of(x.mkt.values,x.lado.values); return x
days={}; agg=[]
for d in range(5,25):
    x=load(d); days[d]=x if d>=12 else None
    ok=~np.isnan(x.win.values); w=np.nan_to_num(x.win.values)
    pnl=np.where(x.buy,x.acc*w-x.usd,x.usd-x.acc*w)-x.fee; var=x.acc**2*x.p*(1-x.p); cost=np.where(x.buy,x.usd,x.acc-x.usd)
    g=pd.DataFrame({"w":x.w,"pnl":np.where(ok,pnl,0),"var":np.where(ok,var,0),"c":np.where(ok,cost,0),"n":1}).groupby("w").sum(); g["d"]=d; agg.append(g.reset_index())
    print("dia",d,"cob",round(ok.mean(),4),flush=True)
agg=pd.concat(agg)
def roster(D):
    h=agg[(agg.d>=D-7)&(agg.d<=D-1)].groupby("w").sum(); z=h.pnl/np.sqrt(h["var"].clip(lower=1e-9)); return set(h.index[(h.n>=30)&(h.c>=200)&(z<=-2)])
res=[]; ctrl_pool=[]
for D in range(12,25):
    x=days[D]; R=roster(D); x=x[~np.isnan(x.win.values)].copy(); x["los"]=x.w.isin(R); x["T0"]=x.ts-(x.cierre-300)
    ev=x[x.los&x.buy&(x.p<=0.35)].sort_values("ts").drop_duplicates(["mkt","lado"]); 
    buys=x[x.buy&~x.los]; gb={k:(g.ts.values,g.acc.values,g.p.values,g.win.values) for k,g in buys.groupby(["mkt","lado"])}
    def sell(k,a,b):
        g=gb.get(k)
        if g is None: return (0.0,0.0,0)
        i0,i1=np.searchsorted(g[0],[a,b]); acc=g[1][i0:i1]; p=g[2][i0:i1]; w=g[3][i0:i1]; m_=p<=0.35; acc=acc[m_]; w=w[m_]; p=p[m_]; return ((acc*(p-w)).sum(),(acc*(1-p)).sum(),int(i1-i0))
    for r in ev.itertuples():
        k=(r.mkt,r.lado); a=sell(k,r.ts+5,r.ts+60); c=sell(k,r.ts+65,r.ts+120)
        res.append((D,r.cierre,r.mkt,r.lado,r.T0,r.w)+a+c)
    print("D",D,"roster",len(R),"eventos",len(ev),flush=True)
    # control sin evento: mercados-lado sin evento, mismo tramo (ventana [T0+5,T0+60] de cada evento no aplica) -> usar ventanas de segundos desde apertura de los eventos del dia
    evk=set(zip(ev.mkt,ev.lado)); 
    if len(ev):
        for (k,g) in gb.items():
            if k in evk: continue
        # muestreo de controles: para cada evento, un mercado-lado sin evento del mismo dia/lado con ventana desde-apertura igual
        pool=[k for k in gb if k not in evk]; ck=pd.DataFrame(pool,columns=["mkt","lado"])
        cl=x.drop_duplicates("mkt").set_index("mkt").cierre
        for r in ev.itertuples():
            cand=ck[ck.lado==r.lado]
            if not len(cand): continue
            for j in rng.choice(len(cand),size=min(3,len(cand)),replace=False):
                k2=(cand.mkt.values[j],cand.lado.values[j]); t_open=cl[k2[0]]-300
                a=sell(k2,t_open+r.T0+5,t_open+r.T0+60); ctrl_pool.append((D,cl[k2[0]],)+a)
R8=pd.DataFrame(res,columns=["D","cierre","mkt","lado","T0","w","pnl_W","cap_W","n_W","pnl_C","cap_C","n_C"])
C=pd.DataFrame(ctrl_pool,columns=["D","cierre","pnl","cap","n"])
R8.to_pickle(NEW/"R8b.pkl"); C.to_pickle(NEW/"R8b_ctrl.pkl")
print("eventos",len(R8),"con flujo en W",int((R8.n_W>0).sum()),"dias",R8.D.nunique())
