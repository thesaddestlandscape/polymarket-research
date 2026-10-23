# A3: reglas candidatas sobre posiciones reales de B + M1 nulo poblacion + L1 conteo. PREREG_POST2527 (sha 8e220e16). Solo lectura.
import pandas as pd, numpy as np, glob
D='/root/polymarket-research-datalogs'; O='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/post_25_27/datos'
rng=np.random.default_rng(20261023)
P=pd.read_csv(f'{O}/pos_b.csv',keep_default_na=False,na_values=['']); P['R']=P.R.fillna('NA'); P['win']=(P.payout>0).astype(int)
def ev(g): return g.pnl.sum()/g.coste.sum() if len(g) and g.coste.sum()>0 else np.nan
def regla(P,nombre,m,nperm=20000):
    """m = mascara booleana de SALTADAS (NaN=missing, excluidas del conjunto evaluado)."""
    ok=m.notna(); Q=P[ok]; s=m[ok].astype(bool).values; n=len(Q); k=int(s.sum())
    if k==0 or n==0: print(f'{nombre}: n_evaluadas {n} saltadas {k}'); return
    pn=Q.pnl.values; dP=-pn[s].sum(); perd=pn[s][pn[s]>0].sum()
    ret=Q[~s]; 
    r=np.array([-pn[rng.choice(n,k,replace=False)].sum() for _ in range(nperm)])
    # IC90 bootstrap por cierre de dP
    cl=Q.cierre.values; uc=np.unique(cl); idx={c:np.nonzero(cl==c)[0] for c in uc}; ssum=np.array([pn[idx[c]][s[idx[c]]].sum() for c in uc])
    bs=np.array([-ssum[rng.integers(0,len(uc),len(uc))].sum() for _ in range(3000)])
    print(f'{nombre}: evaluadas {n} (pnl {pn.sum():+.2f}, coste {Q.coste.sum():.2f}, EV {ev(Q):+.3f}) | saltadas {k} coste {Q.coste[s].sum():.2f} pnl_saltadas {pn[s].sum():+.2f} -> dPnL {dP:+.2f} ; ganancias perdidas {perd:.2f} ; EV retenido {ev(ret):+.3f} ; p_perm(dP>=obs) {np.mean(r>=dP):.3f} ; IC90 cierre dP ({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f}) ; n_cierres {len(uc)}')
    return dict(n=n,k=k,dP=dP)
S23=P[P.dia=='2026-10-23']; S23r=P[P.run.isin(['r25','r26','r27'])]
print('=== B total 20-23 Oct: n',len(P),'pnl %.3f coste %.3f EV %.4f'%(P.pnl.sum(),P.coste.sum(),ev(P)))
print('Por dia:'); print(P.groupby('dia').apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum(),EV=ev(g),hit=g.win.mean(),precio=np.average(g.precio,weights=g.coste)))).round(3))
print('Por run (r25-r27 + previa):'); print(P.groupby('run').apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum(),EV=ev(g),hit=g.win.mean()))).round(3))
for col in ['coin','lado','clase_rpre','h_w1','R']:
    print(f'--- 23-Oct por {col}'); print(S23.groupby(col).apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum(),EV=ev(g)))).round(3))
    print(f'--- B 20-22 (visto) por {col}'); print(P[P.dia<'2026-10-23'].groupby(col).apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum(),EV=ev(g)))).round(3))
P['bp']=(P.precio*20).astype(int)/20; S23=P[P.dia=='2026-10-23']
print('--- precio 0,05 23-Oct'); print(S23.groupby('bp').apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum()))).round(3))
print('--- precio 0,05 B 20-22'); print(P[P.dia<'2026-10-23'].groupby('bp').apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum(),EV=ev(g)))).round(3))
print('--- hora 23-Oct'); print(S23.groupby('hora').apply(lambda g:pd.Series(dict(n=len(g),gan=g.win.sum(),coste=g.coste.sum(),pnl=g.pnl.sum()))).round(3))
print('\n##### REGLAS sobre posiciones reales')
for nm,df in [('23-Oct (r25-r27) FORWARD',P[P.dia=='2026-10-23']),('B 20-22 (VISTO por W1, descriptivo)',P[P.dia<'2026-10-23']),('B total 20-23',P)]:
    print('\n##',nm)
    regla(df,'RL0 h_w1==1',df.h_w1.astype(float).where(df.R!='NA').astype(float).where(df.h_w1.notna()))
    regla(df,'RL1 h_w1 & TREND',((df.h_w1==1)&(df.R=='TREND')).astype(float).where(df.R!='NA'))
    regla(df,'RL2 h_w1 & TREND|MIXTO',((df.h_w1==1)&df.R.isin(['TREND','MIXTO'])).astype(float).where(df.R!='NA'))
    regla(df,'S1p Binance>=2bps en contra (2s previos a t_det)',df.S1p_salta)
    # nota: RL0 con 'NA' en R excluye 3 posiciones por simplicidad de conjunto comun
sh=P[P.b15.notna()]
for nm,df in [('shadow-disponible (22-Oct pm + 23-Oct)',sh),('shadow-disponible 23-Oct',sh[sh.dia=='2026-10-23'])]:
    print('\n##',nm)
    regla(df,'RB2 (salta si NO pasa)',1-df.RB2_pasa)
    regla(df,'RB3 (salta si NO pasa)',1-df.RB3_pasa)
    regla(df,'RL0 sobre el mismo conjunto',df.h_w1.astype(float))
# Delta EV h_w1 por cierre (B total)
def dEV(Q): return ev(Q[Q.h_w1==1])-ev(Q[Q.h_w1==0])
for nm,Q in [('23-Oct',P[(P.dia=='2026-10-23')&P.h_w1.notna()]),('B 20-22 visto',P[(P.dia<'2026-10-23')&P.h_w1.notna()]),('B total',P[P.h_w1.notna()])]:
    cl=Q.cierre.values; uc=np.unique(cl); ix=[np.nonzero(cl==c)[0] for c in uc]; bs=[]
    for _ in range(3000):
        j=np.concatenate([ix[i] for i in rng.integers(0,len(uc),len(uc))]); R=Q.iloc[j]; 
        if (R.h_w1==1).sum() and (R.h_w1==0).sum(): bs.append(dEV(R))
    print(f'Delta EV(h_w1=1)-EV(h_w1=0) {nm}: n1={int((Q.h_w1==1).sum())} EV1 {ev(Q[Q.h_w1==1]):+.3f} n0={int((Q.h_w1==0).sum())} EV0 {ev(Q[Q.h_w1==0]):+.3f} Delta {dEV(Q):+.3f} IC90 cierre ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) ; PnL h1 {Q.pnl[Q.h_w1==1].sum():+.2f} PnL h0 {Q.pnl[Q.h_w1==0].sum():+.2f}')
# markouts AS (ponderado por coste)
def wm(g,c): v=g[c]; ok=v.notna(); return np.average(v[ok],weights=g.coste[ok]) if ok.any() else np.nan
print('\n#### markout de rellenos B (rel. al precio, ponderado por coste)'); 
for nm,g in [('23-Oct',P[P.dia=='2026-10-23']),('20-22',P[P.dia<'2026-10-23'])]:
    print(nm,'mk5 %.3f mk30 %.3f mk120 %.3f n_mk %d'%(wm(g,'mk5'),wm(g,'mk30'),wm(g,'mk120'),g.mk5.notna().sum()))
# ritmo L1
print('\n#### L1 conteo'); 
for d,g in P.groupby('dia'): print(d,'posiciones',len(g),'h_w1=1',int((g.h_w1==1).sum()),'h_w1=0',int((g.h_w1==0).sum()))
