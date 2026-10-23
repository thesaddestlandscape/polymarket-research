# A4: M1 nulo calibrado a poblacion (pob 17-22), M2 gemelo r3shadow, M3 regimen del dia. PREREG_POST2527. Solo lectura.
import pandas as pd, numpy as np, glob, gzip, json
D='/root/polymarket-research-datalogs'; O='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
rng=np.random.default_rng(20261023)
P=pd.read_csv(f'{O}/pos_b.csv',keep_default_na=False,na_values=['']); P['win']=(P.payout>0).astype(int)
pob=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
pob=pob[pob.gana_lado.notna()&pob.pnl.notna()&pob.coin.isin(['ETH','SOL','XRP'])&(pob.precio>=0.10)&(pob.precio<0.30)].copy()
print('poblacion 17-22: unidades',len(pob),'coste %.0f pnl %.0f EV %.4f'%(pob.coste.sum(),pob.pnl.sum(),pob.pnl.sum()/pob.coste.sum()),'hit %.4f'%pob.gana_lado.mean(),'dias',sorted(pob.dia.unique()))
pob['bp']=(pob.precio*20).astype(int)/20
tab=pob.groupby('bp').apply(lambda g:pd.Series(dict(n=len(g),hit=g.gana_lado.mean(),EV=g.pnl.sum()/g.coste.sum(),precio=np.average(g.precio,weights=g.coste))))
print(tab.round(4)); 
print('EV poblacion por dia:'); print(pob.groupby('dia').apply(lambda g:pd.Series(dict(n=len(g),EV=g.pnl.sum()/g.coste.sum(),hit=g.gana_lado.mean()))).round(4))
print('EV poblacion por lado:'); print(pob.groupby('lado').apply(lambda g:pd.Series(dict(n=len(g),EV=g.pnl.sum()/g.coste.sum()))).round(4))
# DEFF por cierre: residuo = pnl - EV_cubo*coste
pob['res']=pob.pnl-pob.bp.map(tab.EV)*pob.coste
deff=(pob.groupby('fin_s').res.sum()**2).sum()/(pob.res**2).sum(); print('DEFF por cierre (varianza de sumas por cierre / suma de varianzas) = %.2f ; n cierres %d'%(deff,pob.fin_s.nunique()))
phit=tab.hit
pob['rw']=pob.gana_lado-pob.bp.map(phit)
pv=pob.groupby(['fin_s','coin']).rw.mean().unstack(); cc=pv.corr(min_periods=300); iu=np.triu_indices(3,1); rho=float(np.nanmean(cc.values[iu]))
print('rho entre monedas dentro del mismo cierre (residuo de acierto):',cc.round(3).values.tolist(),'media %.3f'%rho)
m_cl=float(__import__('pandas').read_csv(f'{O}/pos_b.csv').groupby('fin_s').size().mean()) if False else 1.6
deff=1+(m_cl-1)*rho; print('DEFF_B = 1+(m-1)rho con m=1.6 posiciones/cierre: %.2f'%deff)
def nulo(Q,nm,nsim=100000):
    bp=(Q.precio*20).astype(int)/20; p=bp.map(phit).values; pr=Q.precio.values; acc=Q.acciones.values
    W=rng.random((nsim,len(Q)))<p; sim=(W*acc*(1-pr)-(~W)*acc*pr).sum(1); obs=Q.pnl.sum(); mu=sim.mean(); sd=sim.std()
    # variante cluster: ajustar sd por sqrt(DEFF)
    z=(obs-mu)/(sd*np.sqrt(deff))
    from math import erf,sqrt
    pz=0.5*(1+erf(z/sqrt(2)))
    print(f'M1 {nm}: n {len(Q)} obs PnL {obs:+.2f} | nulo(pop) media {mu:+.2f} sd {sd:.2f} (sd*sqrt(DEFF) {sd*np.sqrt(deff):.2f}) | p(PnL nulo<=obs) indep {np.mean(sim<=obs+1e-9):.4f} ; cluster-ajustado (normal) {pz:.4f} ; hit obs {Q.win.mean():.3f} vs esperado {p.mean():.3f}')
nulo(P[P.dia=='2026-10-23'],'r25-r27 (23-Oct)')
for r in ['r25','r26','r27']: nulo(P[P.run==r],r)
nulo(P[P.dia=='2026-10-22'],'22-Oct'); nulo(P[(P.dia<'2026-10-23')],'B 20-22 (visto)'); nulo(P,'B total 20-23')
# B vs poblacion por celda (n>=40 solo si existe)
for col in ['lado','coin']:
    for k,g in P[P.dia<'2026-10-23'].groupby(col):
        q=pob[pob[col]==k]; print(f'M4 B20-22 {col}={k}: n {len(g)} EV B {g.pnl.sum()/g.coste.sum():+.3f} vs pob {q.pnl.sum()/q.coste.sum():+.3f} (n {len(q)})')
# M2 gemelo
des={}
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_desenlaces_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        d=json.loads(l)
        if d.get('tipo')=='des' and d.get('ganador'): des[d['slug']]=d['ganador']
comp={}; fills=[]
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_shadow_2026-10-23.jsonl.gz')):
    for l in gzip.open(f,'rt'):
        if '"tipo":"mkt_fin"' in l: d=json.loads(l); comp[d['slug']]=d['completo']
        elif '"tipo":"fill"' in l:
            d=json.loads(l)
            if d['pol']=='BASE': fills.append(d)
F=pd.DataFrame(fills); print('\nM2 gemelo BASE 23-Oct: fills',len(F),'mercados completos',sum(comp.values()),'de',len(comp),'con desenlace',len(des))
F=F[F.slug.map(comp).fillna(False)&F.slug.isin(des)].copy()
F=F.sort_values('r').drop_duplicates(['slug','esc','lado'],keep='first')   # un relleno por puja
F['gana']=(F.lado==F.slug.map(des)).astype(int); F['pnl']=np.where(F.gana==1,F.acc*(1-F.precio),-F.acc*F.precio); F['coste']=F.acc*F.precio
F['cierre']=F.slug.str.split('-').str[-1].astype(int)+300; F['coin']=F.slug.str.split('-').str[0].str.upper()
F['hora']=pd.to_datetime(F.r,unit='ms',utc=True).dt.hour+pd.to_datetime(F.r,unit='ms',utc=True).dt.minute/60
F.to_csv(f'{O}/gemelo_fills_23oct.csv',index=False)
for esc,g in F.groupby('esc'):
    w=g[(g.hora>=6.5)&(g.hora<8.95)]
    def ci(q):
        uc=q.cierre.unique(); ix={c:np.nonzero(q.cierre.values==c)[0] for c in uc}; s=[]
        for _ in range(2000):
            j=np.concatenate([ix[c] for c in rng.choice(uc,len(uc))]); s.append(q.pnl.values[j].sum()/q.coste.values[j].sum())
        return np.percentile(s,5),np.percentile(s,95)
    a=ci(g);b=ci(w)
    print(f'gemelo {esc}: dia n {len(g)} hit {g.gana.mean():.3f} precio {np.average(g.precio,weights=g.coste):.3f} EV {g.pnl.sum()/g.coste.sum():+.3f} IC90 cierre ({a[0]:+.3f},{a[1]:+.3f}) pnl {g.pnl.sum():+.1f} | ventana B 06:30-08:56 n {len(w)} hit {w.gana.mean():.3f} EV {w.pnl.sum()/w.coste.sum():+.3f} IC90 ({b[0]:+.3f},{b[1]:+.3f}) pnl {w.pnl.sum():+.1f}')
g=F[F.esc=='cons_x']
print('gemelo cons_x por moneda (dia):'); print(g.groupby('coin').apply(lambda q:pd.Series(dict(n=len(q),hit=q.gana.mean(),EV=q.pnl.sum()/q.coste.sum()))).round(3))
print('gemelo cons_x por lado (dia):'); print(g.groupby('lado').apply(lambda q:pd.Series(dict(n=len(q),hit=q.gana.mean(),EV=q.pnl.sum()/q.coste.sum()))).round(3))
print('gemelo cons_x por hora UTC (dia):'); print(g.assign(h=g.hora.astype(int)).groupby('h').apply(lambda q:pd.Series(dict(n=len(q),hit=q.gana.mean(),EV=q.pnl.sum()/q.coste.sum()))).round(3).T.to_string())
# emparejado con B en mercados donde B tuvo posicion
bm=P[P.dia=='2026-10-23'][['mercado','lado','pnl','coste','precio']]
m=bm.merge(g[['slug','lado','pnl','coste','precio','gana']],left_on=['mercado','lado'],right_on=['slug','lado'],how='left',suffixes=('_B','_G'))
print('\nEmparejado B vs gemelo cons_x (misma mercado-lado):'); print(m[['mercado','lado','precio_B','pnl_B','precio_G','pnl_G','gana']].to_string())
print('B posiciones con gemelo relleno:',m.pnl_G.notna().sum(),'de',len(m),'; PnL B en esas %.2f vs gemelo %.2f'%(m[m.pnl_G.notna()].pnl_B.sum(),m.pnl_G.sum()))
# M3: tasa de acierto del gemelo hoy vs poblacion y vs B ventana
print('\nM3 hit gemelo cons_x dia %.3f (n %d) ; pob 17-22 hit %.3f ; B 20-22 hit %.3f ; B 23-Oct %.3f'%(g.gana.mean(),len(g),pob.gana_lado.mean(),P[P.dia<'2026-10-23'].win.mean(),P[P.dia=='2026-10-23'].win.mean()))

# M3': regimen independiente del relleno: lado con bid en banda a T~180 s en TODOS los mercados completos (muestras smp del gemelo)
rows=[]
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_shadow_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        if '"tipo":"smp"' not in l: continue
        d=json.loads(l)
        if 150<=d['T']<=210 and d.get('bb') is not None and 0.10<=d['bb']<0.30: rows.append((d['slug'],d['lado'],d['bb'],d['r'],d['T']))
M=pd.DataFrame(rows,columns=['slug','lado','bb','r','T']).sort_values('T').drop_duplicates(['slug','lado'],keep='first')
des2={}
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_desenlaces_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        d=json.loads(l)
        if d.get('tipo')=='des' and d.get('ganador'): des2[d['slug']]=d['ganador']
M=M[M.slug.isin(des2)].copy(); M['gana']=(M.lado==M.slug.map(des2)).astype(int); M['t']=pd.to_datetime(M.r,unit='ms',utc=True); M['dia']=M.t.dt.strftime('%Y-%m-%d'); M['h']=M.t.dt.hour+M.t.dt.minute/60
M['cierre']=M.slug.str.split('-').str[-1].astype(int)+300
def sec(q): return f'n {len(q)} hit {q.gana.mean():.3f} bid medio {q.bb.mean():.3f} EV@bid {q.gana.mean()/q.bb.mean()-1:+.3f}'
print('\nM3 (fill-independiente) longshots con bid 0,10-0,30 a T 150-210 s, TODOS los mercados con desenlace oficial:')
print(' 22-Oct (desde 12:07Z):',sec(M[M.dia=='2026-10-22']))
d3=M[M.dia=='2026-10-23']; print(' 23-Oct dia completo  :',sec(d3))
print(' 23-Oct ventana B 06:30-08:56:',sec(d3[(d3.h>=6.5)&(d3.h<8.95)]))
print(' 23-Oct fuera de ventana  :',sec(d3[~((d3.h>=6.5)&(d3.h<8.95))]))
w=d3[(d3.h>=6.5)&(d3.h<8.95)]
print(' ventana por lado:'); print(w.groupby('lado').apply(lambda q:pd.Series(dict(n=len(q),hit=q.gana.mean(),bid=q.bb.mean()))).round(3))
print(' ventana por moneda:'); print(w.assign(c=w.slug.str.split('-').str[0]).groupby('c').apply(lambda q:pd.Series(dict(n=len(q),hit=q.gana.mean(),bid=q.bb.mean()))).round(3))
# ganador Up/Down en la ventana (direccion del mercado)
ww=pd.Series({s:g for s,g in des2.items() if s.split('-')[0] in('eth','sol','xrp')}); ts=ww.index.str.split('-').str[-1].astype(int); sel=ww[(ts>=1792737000)&(ts<=1792745700)]
print(' ventana: mercados con desenlace',len(sel),'ganador YES(Up) %.2f'%((sel=='YES').mean()))
from math import comb
print(' binomial P(<=1 acierto de 16 | p=0.20)= %.3f ; P(0 de 4) %.3f'%(sum(comb(16,k)*0.2**k*0.8**(16-k) for k in range(2)),0.8**4))
