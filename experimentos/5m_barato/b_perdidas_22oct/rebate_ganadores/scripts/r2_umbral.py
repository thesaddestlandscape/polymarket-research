#!/usr/bin/env python3
"""r2: umbral del MAKER_REBATE con r1_pagos (pagos crudos) y niche_maker_dia (inferido 5m+15m por maker-dia, 06..21-Oct).
Salida: datos/r2_umbral.txt"""
import csv,gzip,collections,numpy as np,pandas as pd,datetime as dt,sys
R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'
out=open(R+'rebate_ganadores/datos/r2_umbral.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
pg=pd.read_csv(R+'rebate_ganadores/datos/r1_pagos.csv'); pg['t']=pd.to_datetime(pg.ts,unit='s',utc=True)
# --- A. suelo duro del pago
pm=pg[pg.t>='2026-03-01']
P('A. pagos desde 2026-03-01: n=',len(pm),'minimo=',pm.usdc.min(),'n<1.0:',(pm.usdc<1).sum())
P('   [1.00,1.05):',((pm.usdc>=1)&(pm.usdc<1.05)).sum(),' [1.05,1.10):',((pm.usdc>=1.05)&(pm.usdc<1.10)).sum(),' [0.90,1.00):',((pm.usdc>=.9)&(pm.usdc<1)).sum())
pf=pg[pg.t<'2026-03-01']; P('   antes de marzo: n=',len(pf),'n<1:',(pf.usdc<1).sum(),'min',pf.usdc.min(),'(sin suelo)')
last_sub=pg[pg.usdc<1].t.max(); first_ge=pg[(pg.t>last_sub)].t.min(); P('   ultimo pago <1:',last_sub,' ; cambio de regimen entre',last_sub.date(),'y marzo')
P('   cota 95% (regla de 3) de P(pago<1 | regimen actual) <',round(3/len(pm),5))
# --- B. inferido por dia
inf=collections.defaultdict(float); coste=collections.defaultdict(float)
for x in csv.DictReader(gzip.open(R+'mapa_escala/datos/niche_maker_dia.csv.gz','rt')):
    inf[(x['maker'],x['dia'])]+=float(x['reb']); coste[(x['maker'],x['dia'])]+=float(x['coste'])
pg['dia_fill']=(pg.t-pd.Timedelta(days=1)).dt.strftime('%Y-%m-%d')
paid=pg.groupby(['maker','dia_fill']).usdc.sum().to_dict()
makers=sorted(set(pg.maker))
# lag check
for lag in (0,1,2):
    xs=[];ys=[]
    for m in makers:
        for d in pd.date_range('2026-10-06','2026-10-21'):
            ds=d.strftime('%Y-%m-%d'); dp=(d+pd.Timedelta(days=lag-1)).strftime('%Y-%m-%d')
            xs.append(inf.get((m,ds),0)); ys.append(paid.get((m,dp),0))
    P('B. lag pago-relleno',lag,'corr(inferido_dia, pagado)=',round(np.corrcoef(xs,ys)[0,1],3))
# maker-dias
rows=[]
for m in makers:
    ds=[d for d in pd.date_range('2026-10-06','2026-10-21').strftime('%Y-%m-%d')]
    for d in ds:
        if (m,d) in inf or (m,d) in paid: rows.append((m,d,inf.get((m,d),0.0),paid.get((m,d),0.0),coste.get((m,d),0.0)))
df=pd.DataFrame(rows,columns=['m','d','inf','paid','coste'])
P('C. maker-dias con relleno 5m/15m ese dia:',(df.inf>0).sum())
b=[0,0.25,0.5,0.75,0.9,1.0,1.1,1.25,1.5,2,4,1e9]
df['bin']=pd.cut(df.inf,b,right=False)
g=df[df.inf>0].groupby('bin',observed=True).agg(n=('inf','size'),p_pago=('paid',lambda s:(s>0).mean()),mediana_pag_si=('paid',lambda s:s[s>0].median()))
P(g.to_string())
# D. ratio pagado/inferido por maker (solo makers cuyo total pagado oct06-21 >=1 y pasa el suelo): estimar k = otros marcos
mk=df.groupby('m').agg(inf=('inf','sum'),paid=('paid','sum'),nd=('inf',lambda s:(s>0).sum()),np_=('paid',lambda s:(s>0).sum()))
mk=mk[mk.inf>50]; mk['ratio']=mk.paid/mk.inf
P('D. makers con inferido 16d>50 (n=%d): ratio pagado/inferido mediana %.2f p10 %.2f p90 %.2f'%(len(mk),mk.ratio.median(),mk.ratio.quantile(.1),mk.ratio.quantile(.9)))
# E. umbral efectivo: logit P(pago | log inf) solo makers 'puros' (ratio global 0.9..1.5)
pur=set(mk[(mk.ratio>=.9)&(mk.ratio<=1.5)].index)
d2=df[df.m.isin(pur)&(df.inf>0)].copy(); d2['pay']=(d2.paid>0).astype(int)
P('E. makers "puros" (ratio 0.9-1.5, n=%d makers, %d maker-dias)'%(len(pur),len(d2)))
# estimar I* tal que pago iff k*inf >= 1 ; k=1.2 central: ratio por dia pagada
dp=d2[d2.pay==1]; k=(dp.paid.sum()/dp.inf.sum()); P('   k (pagado/inferido en dias pagados)=',round(k,3))
P('   dias pagados con inf*k<1.0 (contradicen suelo):',int((dp.inf*k<1).sum()),'de',len(dp),'; dias NO pagados con inf*k>=1.0:',int(((d2.pay==0)&(d2.inf*k>=1)).sum()),'de',int((d2.pay==0).sum()))
for lo,hi in ((0,.5),(.5,.7),(.7,.85),(.85,1.0),(1.0,1.2),(1.2,2),(2,99)):
    s=d2[(d2.inf*k>=lo)&(d2.inf*k<hi)]
    if len(s):
        pp=(s.pay.mean()); n=len(s); se=(pp*(1-pp)/n)**.5
        P(f'   k*inf en [{lo},{hi}): n={n:4d} P(pago)={pp:.2f} +-{1.645*se:.2f} (IC90 normal)')
# F. acumulacion: dia pagado precedido de dias sin pago: pago vs inf_d (+inf_u)
mm=[]
for m in pur:
    s=df[df.m==m].set_index('d')
    ds=sorted(s.index)
    prev_unpaid=0.0
    for d in ds:
        r=s.loc[d]
        if r.paid>0:
            if prev_unpaid>0: mm.append((m,d,r.paid,r.inf,prev_unpaid))
            prev_unpaid=0.0
        else: prev_unpaid+=r.inf
mm=pd.DataFrame(mm,columns=['m','d','paid','inf','unpaid_prev'])
P('F. dias pagados precedidos de dias sin pago (makers puros): n=',len(mm))
if len(mm)>3:
    P('   mediana paid/(inf*k)=%.2f ; paid/((inf+unpaid_prev)*k)=%.2f ; (acumulacion implicaria el segundo ~1 y el primero >1)'%((mm.paid/(mm.inf*k)).median(),(mm.paid/((mm.inf+mm.unpaid_prev)*k)).median()))
    P('   media unpaid_prev*k=%.2f ; media (paid-inf*k)=%.2f'%((mm.unpaid_prev*k).mean(),(mm.paid-mm.inf*k).mean()))
df.to_csv(R+'rebate_ganadores/datos/r2_maker_dia.csv',index=False)
