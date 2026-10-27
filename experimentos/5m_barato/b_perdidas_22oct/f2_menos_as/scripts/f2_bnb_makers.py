# concentracion de PnL por maker en BNB 5m [0.30,0.40) y ETH 15m [0.80,0.99): importa run() de f2_extrae (misma logica) y agrega por maker. Solo lectura.
import sys, json, pandas as pd, numpy as np
sys.argv=['x']; exec(open('f2_extrae.py').read().split("if __name__")[0])
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))); DES.update(json.load(open('../datos/des_extra.json')))
res={}
for marco,coin,a,b,nm in [('5min','BNB',0.30,0.40,'BNB5'),('15min','ETH',0.80,0.99,'ETH15')]:
    parts=[]
    for k in range(6,24):
        d=f'2026-10-{k:02d}'; X,_,_=run(d,marco)
        if X is None: continue
        X=X[(X.coin==coin)&(X.pc>=a)&(X.pc<b)].copy(); X['dia']=d; parts.append(X[['dia','mid','fin','lc','pc','coste','acc','maker']])
    X=pd.concat(parts); X['w']=X.mid.map(DES); X=X[X.w.notna()]; X['pnl']=X.acc*(X.w==X.lc)-X.coste
    mk=X.groupby('maker').agg(coste=('coste','sum'),pnl=('pnl','sum'),n=('coste','size')).sort_values('coste',ascending=False)
    tot=mk.coste.sum(); ev=mk.pnl.sum()/tot
    out=dict(celda=nm,fills=len(X),makers=len(mk),ev=ev,pnl_total=mk.pnl.sum(),top1_coste=mk.coste.iloc[0]/tot,top1_pnl_share=mk.pnl.iloc[0]/mk.pnl.sum(),top1_ev=mk.pnl.iloc[0]/mk.coste.iloc[0])
    for k in (1,3,10):
        r=mk.iloc[k:]; out[f'ev_sin_top{k}_coste']=r.pnl.sum()/r.coste.sum()
    mp=mk.sort_values('pnl',ascending=False); out['pnl_top1_pnl']=mp.pnl.iloc[0]/mp.pnl.sum(); out['ev_sin_top1_pnl']=mp.iloc[1:].pnl.sum()/mp.iloc[1:].coste.sum(); out['ev_sin_top3_pnl']=mp.iloc[3:].pnl.sum()/mp.iloc[3:].coste.sum()
    out['share_makers_pos']=float((mk.pnl>0).mean()); res[nm]=out; print(json.dumps(out,default=float),flush=True)
json.dump(res,open('../datos/makers_concentracion.json','w'),default=float)
