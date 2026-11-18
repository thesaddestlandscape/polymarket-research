import pickle,numpy as np,pandas as pd,collections
H='/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/pista_cola_18nov/out/verif_adenda01/p1_btc_2026-11-12_fxB.pkl'
d=pickle.load(open(H,'rb')); E=d['EV']; P=d['PL']; E=E[~E.own.astype(bool)].copy()
def cuts(x): return np.nanquantile(x,[1/3,2/3])
for c in ('q150','absr5','act'):
    q=cuts(E[c].astype(float).values)
    for X in (E,P):
        v=X[c].astype(float).values; X['s_'+c]=np.where(np.isnan(v),-1,np.searchsorted(q,np.nan_to_num(v),'right'))
for X in (E,P): X['s_ttc']=(X.ttc//60000).clip(-1,10)
print('n E',len(E),'P',len(P))
def has(keys):
    S=set(map(tuple,P[keys].values.tolist())); return np.array([tuple(r) in S for r in E[keys].values.tolist()])
for k in (['p'],['p','s_q150'],['p','s_ttc'],['p','s_absr5'],['p','s_act'],['p','s_q150','s_ttc'],['p','s_q150','s_absr5'],['p','s_q150','s_act'],['p','s_ttc','s_act'],['p','s_q150','s_ttc','s_absr5','s_act'],['X','p'],['X','p','s_q150','s_ttc','s_absr5','s_act']):
    print(k,'eventos con >=1 placebo: %.3f'%has(k).mean())
print('placebos por nivel (X,p) eventos:',len(set(zip(E.X,E.p))),'niveles placebo:',len(set(zip(P.X,P.p))))
print('q150 E pcts',np.percentile(E.q150,[10,50,90]),'P',np.percentile(P.q150,[10,50,90]))
print('ttc min E',np.percentile(E.ttc/60000,[10,50,90]),'P',np.percentile(P.ttc/60000,[10,50,90]))
print('act E',np.percentile(E.act,[10,50,90]),'P',np.percentile(P.act,[10,50,90]))
print('absr5 nan E',E.absr5.isna().mean(),'P',P.absr5.isna().mean())
