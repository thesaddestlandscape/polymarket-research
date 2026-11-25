#!/usr/bin/env python3
"""F8 28-Oct: contribucion RETENIDA (EV ponderado por EUR = sum y / sum c) de las politicas F8 congeladas (scores walk-forward P0/P1/P2 de f8_scores.parquet,
entrenados con etiqueta pesimista), evaluadas sobre dos etiquetas: ORIG (pesimista f=1, tabla.parquet) y CAL0 (variante 0 f=0, la elegida por TUNE; tabla_cal_off0).
Solo lectura. Controles: IC90 por dias (bootstrap), sin 2 mejores dias, placebo (flags aleatorios mismo n por dia x moneda x hora, 300), inversion (30% inferior)."""
import numpy as np, pandas as pd, json
rng=np.random.default_rng(28102026)
D1='/root/polymarket-research-datalogs/f8_estructura/'; D2='/root/polymarket-research-datalogs/calibracion_etiqueta/'
cols=['dia','mercado','lado','t0_recv_ms','coin','bl','relleno_pes','pnl_5acc_si_relleno','censurada','gana']
S=pd.read_parquet(D1+'f8_scores.parquet')
T0=pd.read_parquet(D1+'tabla.parquet'); T1=pd.read_parquet(D2+'tabla_cal_off0.parquet')
print(T0.shape,T1.shape, 'index igual:',T0.index.equals(T1.index))
def prep(V):
    V=V.copy(); V['c']=5.0*(V.bl if 'bl' in V.columns else V.b)
    V['y']=np.where(V.relleno_pes==1,V.pnl_5acc_si_relleno.astype(float),0.0)
    V['hora']=pd.to_datetime(V.t0_recv_ms,unit='ms',utc=True).dt.hour
    return V
res={}
for etq,V in (('ORIG',T0),('CAL0',T1)):
    V=prep(V[[c for c in cols if c in V.columns]]) if False else prep(V)
    V=V[V.censurada==0]; V=V[~((V.relleno_pes==1)&V.gana.isna())]
    for m in ('P0','P1','P2'):
        s=S[S.modelo==m].set_index('idx'); idx=s.index.intersection(V.index)
        df=V.loc[idx].join(s.loc[idx,['score','cut30','cutlow30']])
        df=df[df.coin.isin(['ETH','SOL','XRP'])]
        for ven,(a,b) in {'16_24':('2026-10-16','2026-10-24'),'22_24':('2026-10-22','2026-10-24'),'08_24':('2026-10-08','2026-10-24')}.items():
            g=df[(df.dia>=a)&(df.dia<=b)]
            flag=(g.score>=g.cut30).values; inv=(g.score<=g.cutlow30).values
            def per_day(fl):
                r={}
                for d,x in g.assign(f=fl).groupby('dia'):
                    k=x.f.values; r[d]=(x.y.values[k].sum(),x.c.values[k].sum())
                return r
            pd_=per_day(flag); y=sum(v[0] for v in pd_.values()); c=sum(v[1] for v in pd_.values())
            todas=g.y.sum()/g.c.sum()
            ev_d=np.array([v[0]/v[1] if v[1]>0 else np.nan for v in pd_.values()]); days=list(pd_.keys())
            bs=[np.mean(rng.choice(ev_d,len(ev_d))) for _ in range(4000)]
            # pooled sin 2 mejores dias (por pnl dia)
            order=np.argsort([-v[0] for v in pd_.values()]); keep=[days[i] for i in order[2:]]
            y2=sum(pd_[d][0] for d in keep); c2=sum(pd_[d][1] for d in keep)
            # placebo
            g2=g.reset_index(drop=True); key=g2.dia+g2.coin+g2.hora.astype(str); grp=g2.groupby(key).indices
            nf={k:int(flag[ix].sum()) for k,ix in grp.items()}
            pl=[]
            for _ in range(300):
                fl=np.zeros(len(g2),bool)
                for k,ix in grp.items():
                    if nf[k]: fl[rng.choice(ix,nf[k],replace=False)]=True
                pl.append(g2.y.values[fl].sum()/g2.c.values[fl].sum())
            pl=np.array(pl)
            yi=g.y.values[inv].sum()/g.c.values[inv].sum()
            res[f'{etq}|{m}|{ven}']=dict(n=int(len(g)),n_ret=int(flag.sum()),dias=len(days),ev_ret=y/c,ev_todas=todas,ic90_dias=[float(np.percentile(bs,5)),float(np.percentile(bs,95))],
              ev_sin2mejores=y2/c2,dias_pos=int((ev_d>0).sum()),placebo_media=float(pl.mean()),placebo_p=float((pl>=y/c).mean()),inversion=yi,
              p_relleno_ret=float(g.relleno_pes.values[flag].mean()),ev_dia={d:float(e) for d,e in zip(days,ev_d)})
            print(etq,m,ven,{k:(round(v,3) if isinstance(v,float) else v) for k,v in res[f'{etq}|{m}|{ven}'].items() if k!='ev_dia'},flush=True)
json.dump(res,open('/root/polymarket-research/experimentos/5m_barato/f8_28oct/contrib_f8.json','w'),indent=1)
