# s4b: tabla de nichos (PREREG_MAPA + ADENDA1). Solo lectura de celdas/desenlaces. Salida datos/niches.csv, datos/maker_sel.csv, datos/s4b_resumen.txt
import pandas as pd, numpy as np, json, glob, sys, os
OUT='/root/polymarket-research-datalogs/mapa_escala'; D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
rng=np.random.default_rng(20261023)
des=json.load(open(OUT+'/des.json'))
WIN={'5min':(1,2),'15min':(1,3),'60min':(1,4),'240min':(1,5),'24h':(1,5)}
BAND=['0.01-0.05','0.05-0.10','0.10-0.20','0.20-0.30','0.30-0.50','0.50-0.70','0.70-0.90','0.90-0.99']
DESC_DAYS=[f'2026-10-{i:02d}' for i in range(6,14)]
cov=[]; PD=[]; PF=[]; PM=[]
for f in sorted(glob.glob(OUT+'/cells_*.csv.gz')+glob.glob(OUT+'/cellsx_*.csv.gz')):
    x=pd.read_csv(f,dtype={'mid':str,'maker':'category','coin':'category','marco':'category','lc':'category'})
    x['des']=x.mid.map(des); tot=x.groupby('marco',observed=True).coste.sum()
    ok=x[x.des.notna()].copy()
    cc=ok.groupby('marco',observed=True).coste.sum()
    for m in tot.index: cov.append((x.dia.iloc[0],m,float(tot[m]),float(cc.get(m,0))))
    ok['gana']=(ok.lc.astype(str)==ok.des).astype(float); ok['pnl']=ok.acc*ok.gana-ok.coste
    lo=ok.marco.astype(str).map(lambda m:WIN[m][0]); hi=ok.marco.astype(str).map(lambda m:WIN[m][1])
    ok=ok[(ok.tb>=lo)&(ok.tb<=hi)]
    ok['u']=1
    k=['marco','coin','banda']
    PD.append(ok.groupby(k+['dia'],observed=True).agg(coste=('coste','sum'),pnl=('pnl','sum'),reb=('reb','sum'),acc=('acc','sum')).reset_index())
    PF.append(ok.groupby(k+['fin'],observed=True).agg(coste=('coste','sum'),pnl=('pnl','sum')).reset_index().assign(dia=ok.dia.iloc[0]))
    g=ok.groupby(k+['maker','dia'],observed=True).agg(coste=('coste','sum'),pnl=('pnl','sum'),reb=('reb','sum'),nu=('mid','nunique'),nl=('lc','size')).reset_index()
    PM.append(g)
    # n unidades (mid,lc) por nicho-dia
    u=ok.drop_duplicates(['marco','coin','banda','mid','lc']).groupby(k,observed=True).size().rename('nu_dia').reset_index().assign(dia=ok.dia.iloc[0])
    PD[-1]=PD[-1].merge(u,on=k+['dia'],how='left')
    print(f.split('/')[-1],len(x),flush=True)
PD=pd.concat(PD,ignore_index=True); PF=pd.concat(PF,ignore_index=True); PM=pd.concat(PM,ignore_index=True)
for c in ['marco','coin']: 
    for T in (PD,PF,PM): T[c]=T[c].astype(str)
cv=pd.DataFrame(cov,columns=['dia','marco','coste','coste_con_des']); cv.to_csv(D+'/cobertura.csv',index=False)
print(cv.groupby('marco')[['coste','coste_con_des']].sum().assign(cob=lambda d:d.coste_con_des/d.coste).round(4).to_string())
PD.to_csv(D+'/niche_dia.csv',index=False); PM.to_csv(D+'/niche_maker_dia.csv.gz',index=False); PF.to_csv(D+'/niche_fin.csv.gz',index=False)
