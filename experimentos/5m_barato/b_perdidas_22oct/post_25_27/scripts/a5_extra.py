# A5: escaneo de ventanas (regimen fill-independiente), S1p con margen (POST-HOC), MDE, capacidad. PREREG_POST2527. Solo lectura.
import pandas as pd, numpy as np, glob, gzip, json
D='/root/polymarket-research-datalogs'; O='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
rng=np.random.default_rng(20261023)
# --- M3 escaneo: ventana de 29 cierres contiguos (06:30-08:56Z) frente a todas las ventanas de 29 cierres del 23-Oct (00:00-09:xx) y 22-Oct pm
rows=[]
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_shadow_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        if '"tipo":"smp"' not in l: continue
        d=json.loads(l)
        if 150<=d['T']<=210 and d.get('bb') is not None and 0.10<=d['bb']<0.30: rows.append((d['slug'],d['lado'],d['bb'],d['T']))
M=pd.DataFrame(rows,columns=['slug','lado','bb','T']).sort_values('T').drop_duplicates(['slug','lado'],keep='first')
des={}
for f in sorted(glob.glob(f'{D}/r3_shadow/r3_desenlaces_2026-10-2[23].jsonl.gz')):
    for l in gzip.open(f,'rt'):
        d=json.loads(l)
        if d.get('tipo')=='des' and d.get('ganador'): des[d['slug']]=d['ganador']
M=M[M.slug.isin(des)].copy(); M['gana']=(M.lado==M.slug.map(des)).astype(int); M['cierre']=M.slug.str.split('-').str[-1].astype(int)+300
M=M[M.slug.str.split('-').str[0].isin(['eth','sol','xrp'])]
cl=np.array(sorted(M.cierre.unique())); 
g=M.groupby('cierre').agg(n=('gana','size'),w=('gana','sum'),bb=('bb','sum'))
ini,fin=1792737300+300,1792745700+300   # 06:35..09:00 cierres de los mercados de B (06:30-08:56)
inwin=g[(g.index>=ini)&(g.index<=fin)]; print('Ventana de B: cierres',len(inwin),'n',int(inwin.n.sum()),'hit %.3f bid medio %.3f'%(inwin.w.sum()/inwin.n.sum(),inwin.bb.sum()/inwin.n.sum()))
# todas las ventanas contiguas de la misma duracion (en tiempo) dentro de los datos continuos 23-Oct 00:00-09:00 (sin hueco)
t0=1792713600; res=[]
for s in range(t0,fin-(fin-ini)+1,300):
    w=g[(g.index>s)&(g.index<=s+(fin-ini)+300)]
    if len(w)>=0.8*((fin-ini)/300+1): res.append((s,w.w.sum()/w.n.sum(),w.n.sum()))
r=np.array([x[1] for x in res]); obs=inwin.w.sum()/inwin.n.sum()
print('ventanas candidatas',len(r),'hit medio %.3f min %.3f ; rango de la propia ventana incluida; fraccion de ventanas con hit <= observado (%.3f): %.3f (autocorrelacionadas, ventanas solapadas: orientativo)'%(r.mean(),r.min(),obs,(r<=obs+1e-9).mean()))
fuera=g[~((g.index>=ini)&(g.index<=fin))]; print('fuera de ventana (23-Oct 00:00-09:xx + 22-Oct pm): hit %.3f n %d cierres %d'%(fuera.w.sum()/fuera.n.sum(),int(fuera.n.sum()),len(fuera)))
# permutacion por bloque de cierre: asignar al azar 29 cierres contiguos
# --- S1p con margen (POST-HOC): ventana [t_det-2.5, t_det-0.5]
P=pd.read_csv(f'{O}/pos_b.csv',keep_default_na=False,na_values=['']); P['win']=(P.payout>0).astype(int)
bt={}
for d in ['2026-10-20','2026-10-21','2026-10-22','2026-10-23']:
    x=pd.read_csv(f'{D}/binance_bookticker_{d}.csv',usecols=['ts_recepcion_ms','activo','mid'])
    for c,gg in x.groupby('activo'): bt.setdefault(c,[]).append(gg.sort_values('ts_recepcion_ms'))
bt={c:pd.concat(v).sort_values('ts_recepcion_ms') for c,v in bt.items()}
def mid_at(c,t):
    gg=bt[c]; i=np.searchsorted(gg.ts_recepcion_ms.values,t,side='right')-1
    return gg.mid.values[i] if i>=0 and t-gg.ts_recepcion_ms.values[i]<60000 else np.nan
def mov(r,a,b):
    if not np.isfinite(r.t_det): return np.nan
    x=mid_at(r.coin,(r.t_det-a)*1000); y=mid_at(r.coin,(r.t_det-b)*1000); sg=1 if r.lado=='YES' else -1
    return (y/x-1)*1e4*sg
for nm,(a,b) in {'S1p [t-2.0,t]':(2.0,0.0),'S1p-lag [t-2.5,t-0.5] (post-hoc)':(2.5,0.5),'S1p-lag2 [t-3.0,t-1.0] (post-hoc)':(3.0,1.0)}.items():
    P['m']=[mov(r,a,b) for r in P.itertuples()]; ok=P.m.notna(); Q=P[ok]; s=(Q.m<=-2.0).values; pn=Q.pnl.values; k=int(s.sum())
    pr=np.array([-pn[rng.choice(len(Q),k,replace=False)].sum() for _ in range(20000)]); dP=-pn[s].sum()
    q23=Q[Q.dia=='2026-10-23']; s23=(q23.m<=-2.0).values
    print(f'{nm}: evaluadas {len(Q)} saltadas {k} (hit saltadas {Q.win[s].mean():.3f} vs resto {Q.win[~s].mean():.3f}) dPnL {dP:+.2f} ganancias perdidas {pn[s][pn[s]>0].sum():.2f} p_perm {np.mean(pr>=dP):.3f} | 23-Oct: saltadas {int(s23.sum())} dPnL {-q23.pnl.values[s23].sum():+.2f}')
# --- MDE y potencia (pnl/coste por posicion, B total)
P['u']=P.pnl/P.coste; s0=P.u[P.h_w1==0].std(); s1=P.u[P.h_w1==1].std()
print('\nSD de pnl/coste por posicion: h_w1=0 %.2f h_w1=1 %.2f (pago asimetrico)'%(s0,s1))
for n1 in (40,60,100):
    mde=1.645*np.sqrt(s1**2/n1+s0**2/(2*n1)); print(f'MDE (IC90 una cola) del Delta EV con n1={n1}, n0={2*n1}: {mde:.3f} (sin DEFF por cierre)')
# --- capacidad poblacion
pob=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(f'{D}/etiquetado_pasivo_B/poblacion/pob_*.csv.gz'))])
pob=pob[pob.gana_lado.notna()&pob.coin.isin(['ETH','SOL','XRP'])&(pob.precio>=0.10)&(pob.precio<0.30)]
cd=pob.groupby('dia').agg(n=('coste','size'),coste=('coste','sum'),pnl=('pnl','sum')); print('\nPoblacion makers ETH/SOL/XRP 5m banda 0,10-0,30: coste por dia (EUR)'); print(cd.round(0).T.to_string())
full=cd.loc['2026-10-17':'2026-10-21']; print('coste medio dias completos 17-21: %.0f EUR/dia (TODOS los makers juntos)'%full.coste.mean())
print('B: coste por dia B (20,21,22): ',P.groupby('dia').coste.sum().round(1).to_dict(),'; cuota de B sobre poblacion 21-Oct: %.3f'%(P[P.dia=='2026-10-21'].coste.sum()/cd.loc['2026-10-21','coste']))
for ev_ in (0.05,0.10,0.20): print(f'Para 200.000 EUR/anio con EV {ev_:.2f}/EUR: coste anual {200000/ev_:,.0f} = {200000/ev_/365:,.0f} EUR/dia = {200000/ev_/365/full.coste.mean():.1f}x el coste diario de TODA la poblacion de makers en la banda')
