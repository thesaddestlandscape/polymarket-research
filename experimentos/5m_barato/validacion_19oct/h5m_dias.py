import pandas as pd,numpy as np,glob,sys
SP='/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/'
cols=['mkt','lado_c','ts','T','acc','pc','coste','pnl','act','dia']
parts=[]
for d in range(9,14):
    f=f'/root/polymarket-research-datalogs/h5m_cola_sim/quien_gana_rellenos_v2_2026-10-{d:02d}.csv.gz'
    parts.append(pd.read_csv(f,usecols=cols,dtype={'mkt':str}))
for d in range(14,19):
    parts.append(pd.read_csv(SP+f'fills_2026-10-{d}.csv.gz',usecols=cols,dtype={'mkt':str}))
F=pd.concat(parts,ignore_index=True)
F=F[(F.pc>0.10)&(F.pc<=0.30)&(F['T']>60)&(F['T']<=300)].sort_values(['dia','ts'],kind='stable').reset_index(drop=True)
F['fin']=(np.round((F.ts+F['T'])/300)*300).astype('int64')
F['hora']=pd.to_datetime(F.fin,unit='s').dt.hour
F['key']=F.dia+'|'+F.mkt+'|'+F.lado_c
g=F.groupby('key',sort=False)
F['cum']=g.acc.cumsum();F['prev']=F.cum-F.acc
F['f5']=(np.clip(5-F.prev,0,None).clip(upper=F.acc))/F.acc
F['c5']=F.coste*F.f5;F['p5']=F.pnl*F.f5
F.to_pickle(SP+'F_all.pkl')
print(len(F),F.dia.nunique())
U=F.groupby('key').agg(dia=('dia','first'),act=('act','first'),mkt=('mkt','first'),lado=('lado_c','first'),p=('pnl','sum'),c=('coste','sum'),acc=('acc','sum'),fin=('fin','first'),hora=('hora','first'),p5=('p5','sum'),c5=('c5','sum'))
U['ev']=U.p/U.c;U['gan']=U.p>0
U5=U[U.c5>0].copy();U5['ev5']=U5.p5/U5.c5
rows=[]
for d,x in U.groupby('dia'):
    y=U5[U5.dia==d]
    rows.append(dict(dia=d,n=len(x),ev_media=x.ev.mean(),ev_pond=x.p.sum()/x.c.sum(),n5=len(y),ev5_media=y.ev5.mean(),ev5_pond=y.p5.sum()/y.c5.sum(),acierto=x.gan.mean(),
        c_gan=x.c[x.gan].mean(),c_per=x.c[~x.gan].mean(),px_pond=x.c.sum()/x.acc.sum()))
R=pd.DataFrame(rows).set_index('dia');pd.set_option('display.width',250);pd.set_option('display.max_columns',30)
print(R.round(4))
rng=np.random.default_rng(1)
def icd(v,n=10000):
    v=np.asarray(v);return np.quantile(v[rng.integers(0,len(v),(n,len(v)))].mean(1),[.05,.95]).round(4)
for k in ['ev_media','ev_pond','ev5_media','ev5_pond']:
    print(k,'media de días',R[k].mean().round(4),'IC90 días',icd(R[k]),'| sin 18:',R[k].drop('2026-10-18').mean().round(4),icd(R[k].drop('2026-10-18')))
print('agregado pond Σp/Σc',U.p.sum()/U.c.sum(),' first5 agregado',U5.p5.sum()/U5.c5.sum())
# agregado pond: IC por días
d=U.groupby('dia')[['p','c']].sum();bb=[]
for _ in range(10000):
    i=rng.integers(0,len(d),len(d));bb.append(d.p.values[i].sum()/d.c.values[i].sum())
print('IC90 agregado pond (boot días)',np.quantile(bb,[.05,.95]).round(4))
d5=U5.groupby('dia')[['p5','c5']].sum();bb=[]
for _ in range(10000):
    i=rng.integers(0,len(d5),len(d5));bb.append(d5.p5.values[i].sum()/d5.c5.values[i].sum())
print('IC90 first5 agregado pond (boot días)',np.quantile(bb,[.05,.95]).round(4))
# por cierre
cl=U.groupby('fin')[['p','c']].sum();bb=[]
for _ in range(4000):
    i=rng.integers(0,len(cl),len(cl));bb.append(cl.p.values[i].sum()/cl.c.values[i].sum())
print('IC90 agregado pond (boot cierres, n=%d)'%len(cl),np.quantile(bb,[.05,.95]).round(4))
cl5=U5.groupby('fin')[['p5','c5']].sum();bb=[]
for _ in range(4000):
    i=rng.integers(0,len(cl5),len(cl5));bb.append(cl5.p5.values[i].sum()/cl5.c5.values[i].sum())
print('IC90 first5 pond (boot cierres)',np.quantile(bb,[.05,.95]).round(4))
# ¿18-Oct ruptura? diferencia de ev_media de unidades 18 vs resto, bootstrap por cierre (clusters) 
def cl_diff(col='ev',n=3000):
    a=U[U.dia=='2026-10-18'];b=U[U.dia!='2026-10-18']
    ga=a.groupby('fin')[col].agg(['sum','count']);gb=b.groupby('fin')[col].agg(['sum','count']);out=[]
    for _ in range(n):
        ia=rng.integers(0,len(ga),len(ga));ib=rng.integers(0,len(gb),len(gb))
        out.append(ga['sum'].values[ia].sum()/ga['count'].values[ia].sum()-gb['sum'].values[ib].sum()/gb['count'].values[ib].sum())
    return np.quantile(out,[.05,.5,.95]).round(4),np.mean(np.array(out)>=0)
print('18 vs resto, ev_media unidades, boot cierre: IC90 y P(dif>=0):',cl_diff())
# Mismo para ev_pond: usar p,c agregados por cierre
def cl_diff_pond(n=3000,excl=('2026-10-18',)):
    a=U[U.dia=='2026-10-18'];b=U[~U.dia.isin(excl)]
    ga=a.groupby('fin')[['p','c']].sum();gb=b.groupby('fin')[['p','c']].sum();out=[]
    for _ in range(n):
        ia=rng.integers(0,len(ga),len(ga));ib=rng.integers(0,len(gb),len(gb))
        out.append(ga.p.values[ia].sum()/ga.c.values[ia].sum()-gb.p.values[ib].sum()/gb.c.values[ib].sum())
    return np.quantile(out,[.05,.5,.95]).round(4),np.mean(np.array(out)>=0)
print('18 vs resto, ev_pond, boot cierre:',cl_diff_pond())
# permutación de días: ¿cuántos de los 10 días ocupa el 18 por ev_media? z de residuo con SE por cierres
# por moneda y hora (18 vs resto)
print('\n18-Oct vs resto POR MONEDA: n, ev_media, ev_pond | resto')
for m in sorted(U.act.unique()):
    a=U[(U.dia=='2026-10-18')&(U.act==m)];b=U[(U.dia!='2026-10-18')&(U.act==m)]
    print(m,len(a),round(a.ev.mean(),3),round(a.p.sum()/a.c.sum(),3),'|',len(b),round(b.ev.mean(),3),round(b.p.sum()/b.c.sum(),3))
print('\nPOR HORA UTC (bloques de 4 h) 18 vs resto: n, ev_media, ev_pond')
U['hb']=U.hora//4*4
for h,x in U.groupby('hb'):
    a=x[x.dia=='2026-10-18'];b=x[x.dia!='2026-10-18']
    print(h,len(a),round(a.ev.mean(),3),round(a.p.sum()/a.c.sum(),3),'|',len(b),round(b.ev.mean(),3),round(b.p.sum()/b.c.sum(),3))
print('\nPOR HORA 18-Oct (h exacta) ev_media n')
a=U[U.dia=='2026-10-18'];print(a.groupby('hora').ev.agg(['mean','size']).round(2).T.to_string())
# régimen: precio medio y acierto por lado (YES/NO)
print('\nPOR LADO comprado 18 vs resto')
for l,x in U.groupby('lado'):
    a=x[x.dia=='2026-10-18'];b=x[x.dia!='2026-10-18']
    print(l,len(a),round(a.ev.mean(),3),round(a.gan.mean(),3),'|',len(b),round(b.ev.mean(),3),round(b.gan.mean(),3))
# autocorrelación entre días de ev_media (para saber si el 18 es continuación)
print('ev_media diaria',R.ev_media.round(3).tolist())
# first5 por moneda 18 vs resto
print('\nFIRST-5 por moneda: 18 vs resto (ev5 media, pond; n)')
for m in sorted(U5.act.unique()):
    a=U5[(U5.dia=='2026-10-18')&(U5.act==m)];b=U5[(U5.dia!='2026-10-18')&(U5.act==m)]
    print(m,len(a),round(a.ev5.mean(),3),round(a.p5.sum()/a.c5.sum(),3),'|',len(b),round(b.ev5.mean(),3),round(b.p5.sum()/b.c5.sum(),3))
U.to_pickle(SP+'U_all.pkl')
