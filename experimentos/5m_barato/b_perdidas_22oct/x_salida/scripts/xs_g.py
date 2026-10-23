# POST-HOC: g (crecimiento log por dia) y parada por regla en E-S, mas 'SIN' (sin regla). E_ini=40 H=12, 12 dias sinteticos.
import pandas as pd, numpy as np, pickle, json, sys
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/x_salida/scripts')
from xs_sim import sim,REGLAS
from scipy.stats import norm
O='/root/polymarket-research-datalogs/x_salida/'
DB=pickle.load(open(O+'datasets.pkl','rb'))['DB']; rng=np.random.default_rng(777)
R=dict(REGLAS); R['SIN']=dict(Bd=1e9,rat=0)
Bg=[(int(f),g.coste.values,g.acciones.values,g.precio_medio.values) for f,g in DB.groupby('fin')]; f0=Bg[0][0]
out={}
for e in (0.0,0.05,0.10):
    th=[norm.ppf(np.clip(p*(1+e),.01,.99)) for (_,_,_,p) in Bg]; rows=[]
    for j in range(800):
        fl=[]
        for r in range(3):
            for (fin,cs,ac,p),t in zip(Bg,th):
                z=np.sqrt(.333)*rng.standard_normal()+np.sqrt(.667)*rng.standard_normal(len(cs)); w=z<t
                fl.append((fin-f0+r*4*86400,(fin-f0)//86400+r*4,tuple(cs),tuple(np.where(w,ac-cs,-cs))))
        for k,rr in R.items():
            m=sim(fl,rr,40.0); rows.append((k,m['pnl'],m['cost'],m['dd'],int(m['halted']),np.log(max(m['Eend'],0.5)/40.0)/12.0,int(m['Eend']<17)))
    df=pd.DataFrame(rows,columns=['regla','pnl','cost','dd','halt','g','bajo17'])
    t=df.groupby('regla').agg(pnl=('pnl','mean'),pnl_sd=('pnl','std'),dd=('dd','mean'),dd_p90=('dd',lambda x:np.percentile(x,90)),g=('g','mean'),halt=('halt','mean'),bajo17=('bajo17','mean'),cost=('cost','mean'))
    out[str(e)]=t.round(4).to_dict('index'); print(e); print(t.round(4).to_string(),flush=True)
json.dump(out,open(O+'parteG.json','w'),indent=1)
