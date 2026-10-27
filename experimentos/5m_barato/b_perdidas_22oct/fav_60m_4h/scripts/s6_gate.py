# s6_gate.py: PREREG_FAV60 gate y desgloses sobre datos/vpv_unidades.csv. Semilla fija.
import pandas as pd, numpy as np, json
from datetime import datetime, timezone
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos/'
rng=np.random.default_rng(20261025)
U=pd.read_csv(D+'vpv_unidades.csv',dtype={'mid':str})
U['dia']=pd.to_datetime(U.fin-1,unit='s',utc=True).dt.strftime('%Y-%m-%d')
U=U[U.fin<=int(datetime(2026,10,25,tzinfo=timezone.utc).timestamp())]
cob=U.win.notna().mean(); print('cobertura desenlace',round(cob,4),'unidades',len(U)); U=U[U.win.notna()].copy()
U['coste']=5*U.P; U['pnl']=5*(U.win-U.P); U['reb']=5*0.014*U.P*(1-U.P)
# placebo: desenlace del mismo lado, misma moneda, mercado con fin 24 h antes
key=U.drop_duplicates(['coin','fin','lado']).set_index(['coin','fin','lado']).win
W=pd.read_json(D+'tokmap_gamma.json').loc['mercados'] if False else None
G=json.load(open(D+'tokmap_gamma.json'))['mercados']
wl={}
for m in G.values():
    if m['marco']=='60min' and m['win']: wl[(m['coin'],m['fin'],'Up')]=int(m['win']=='Up'); wl[(m['coin'],m['fin'],'Down')]=int(m['win']=='Down')
U['win_pl']=[wl.get((c,f-86400,s),np.nan) for c,f,s in zip(U.coin,U.fin,U.lado)]
def boot(Dd,col='p',B=4000):
    i=rng.integers(0,len(Dd),(B,len(Dd))); bs=Dd[col].values[i].sum(1)/Dd.c.values[i].sum(1); return round(np.percentile(bs,5),4),round(np.percentile(bs,95),4)
def st(df,pn='pnl'):
    if len(df)==0: return dict(n=0)
    Dd=df.groupby('dia').agg(c=('coste','sum'),p=(pn,'sum'),r=('reb','sum'))
    ev=Dd.p.sum()/Dd.c.sum(); s2=Dd.sort_values('p',ascending=False).iloc[2:]
    o=dict(n=len(df),dias=len(Dd),dias_pos=int((Dd.p>0).sum()),ev=round(ev,4),ev_unid=round((df[pn]/df.coste).mean(),4),hit=round(df.win.mean(),4),pmed=round(df.P.mean(),4),
           ic90_dias=boot(Dd) if len(Dd)>=3 else None,ev_sin2=round(s2.p.sum()/s2.c.sum(),4) if len(s2) else None,ev_reb=round((Dd.p.sum()+Dd.r.sum())/Dd.c.sum(),4))
    return o
R={}
def rep(nombre,df,fill='fill_pes'):
    f=df[df[fill]==1]; nf=df[df[fill]==0]; r=dict(todas=st(df),rellenas=st(f),no_rellenas=st(nf))
    if len(f) and len(nf):
        # AS: acierto rellenas - no rellenas, IC por dias (bootstrap de dias)
        dd=sorted(df.dia.unique()); A=[]
        g=df.groupby(['dia',fill]).win.agg(['sum','count']).unstack(fill).fillna(0)
        for _ in range(4000):
            s=g.iloc[rng.integers(0,len(g),len(g))].sum()
            if s[('count',1)]>0 and s[('count',0)]>0: A.append(s[('sum',1)]/s[('count',1)]-s[('sum',0)]/s[('count',0)])
        r['AS_pp']=round(f.win.mean()-nf.win.mean(),4); r['AS_ic90']=(round(np.percentile(A,5),4),round(np.percentile(A,95),4))
        r['tasa_relleno']=round(len(f)/len(df),4)
    R[nombre]=r; print(nombre,json.dumps(r,default=str)); return r
base=U[U.coin.isin(['BTC','ETH','SOL'])]
g=rep('GATE_BTCETHSOL_070_090_PES',base[base.banda==0.70])
gf=base[(base.banda==0.70)&(base.fill_pes==1)]
pl=gf[gf.win_pl.notna()].copy(); pl['pnl_pl']=5*(pl.win_pl-pl.P); pl['dif']=pl.pnl-pl.pnl_pl
Dd=pl.groupby('dia').agg(c=('coste','sum'),p=('dif','sum'))
R['placebo']=dict(n=len(pl),ev_real=round(pl.pnl.sum()/pl.coste.sum(),4),ev_placebo=round(pl.pnl_pl.sum()/pl.coste.sum(),4),dif_ic90_dias=boot(Dd) if len(Dd)>=3 else None); print('placebo',R['placebo'])
rep('INVERSION_010_030_PES',base[base.banda==0.10])
rep('BTCETHSOL_070_090_OPT',base[base.banda==0.70],'fill_opt')
for b in (0.50,0.90): rep(f'BTCETHSOL_{b:.2f}_PES',base[base.banda==b])
for c in sorted(U.coin.unique()): rep(f'{c}_070_090_PES',U[(U.coin==c)&(U.banda==0.70)])
for lo in (0.70,0.75,0.80,0.85):
    rep(f'BTCETHSOL_P{lo:.2f}_PES',base[(base.banda==0.70)&(base.P>=lo-1e-9)&(base.P<lo+0.05-1e-9)])
vis=base[(base.banda==0.70)]; rep('VISTOS_F2_18a23',vis[(vis.dia>='2026-10-18')&(vis.dia<='2026-10-23')]); rep('NO_VISTOS_12a17_24',vis[(vis.dia<'2026-10-18')|(vis.dia>'2026-10-23')])
R['n_dia_rellenas_gate']=round(len(gf)/max(1,gf.dia.nunique()),2); R['dias_lista']=sorted(gf.dia.unique())
R['coste_rellenado_dia_5acc']=round(gf.coste.sum()/max(1,base.dia.nunique()),3)
json.dump(R,open(D+'gate.json','w'),indent=1,default=str)
# EXPLORATORIO (post-prereg, K extra declarado): vida de la puja limitada a L s (relleno PES solo si t_fill<=L)
for L in (60,300,900):
    b2=base[base.banda==0.70].copy(); b2['fill_L']=((b2.fill_pes==1)&(pd.to_numeric(b2.t_fill_pes,errors='coerce')<=L)).astype(int)
    rep(f'EXPLOR_vida_{L}s_070_090',b2,'fill_L')
json.dump(R,open(D+'gate.json','w'),indent=1,default=str)
