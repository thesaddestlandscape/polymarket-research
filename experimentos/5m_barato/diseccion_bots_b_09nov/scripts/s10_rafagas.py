#!/usr/bin/env python3
"""s10: anatomia de las RAFAGAS (varios tomadores distintos en el mismo bloque y mercado contra bids de banda):
 rango dentro de la rafaga (1º vs siguientes), hueco desde el 1er print, y regla ex ante candidata 'print contrario reciente'
 (prints WS en el mercado contra L recibidos en [c-W, c], c = tau-100 ms) con W = 0,25/0,5/1/2 s. EXCESO = EV(no marcadas) - EV(todas).
 IC90 bootstrap por dia y por cierre. DISC 20-29 Oct / HOLD 30 Oct-08 Nov (ambos exploratorios)."""
import json, glob, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
rng=np.random.default_rng(5)
cols=['tx','dia','tw','esB','y_loss','pnl_mk','c','pc_u','tau_abs','mkt','bloque','L','cierre','coin']
out=[]
for f in sorted(glob.glob(DD+'feat_2026-*.parquet')):
    D=f[-18:-8]; U=pd.read_parquet(f,columns=cols); R=np.load(DD+f'reg_{D}_tx.npz'); BASE=float(R['BASE'][0])
    tok=json.load(open(DD+f'tok_{D}.json')); tl=list(R['tok']); ti={k:i for i,k in enumerate(tl)}
    m5={(v[2],v[4]):k for k,v in tok.items() if v[1]=='5min'}
    Tt=R['t_tok'].astype(np.float64); Tr=R['t_rx'].astype(np.float64); Tb=R['t_buy']; Tsz=R['t_sz'].astype(np.float64)
    key=Tt*1e10+Tr
    c=U.tau_abs.values-BASE-100
    opp={'YES':'NO','NO':'YES'}
    tL=np.array([ti.get(m5.get((str(m),l)),-1) for m,l in zip(U.mkt,U.L)],dtype=np.float64)
    tC=np.array([ti.get(m5.get((str(m),opp[l])),-1) for m,l in zip(U.mkt,U.L)],dtype=np.float64)
    # contra L = vender L o comprar C
    against_L=np.cumsum(np.where(Tb==0,Tsz,0.0)); against_C=np.cumsum(np.where(Tb==1,Tsz,0.0)); nall=np.arange(1,len(Tt)+1,dtype=np.float64)
    def win(tt,cum,a,b):
        i=np.searchsorted(key,tt*1e10+b,'right')-1; j=np.searchsorted(key,tt*1e10+a,'right')-1
        okI=(i>=0)&(Tt[np.maximum(i,0)]==tt); okJ=(j>=0)&(Tt[np.maximum(j,0)]==tt)
        vi=np.where(okI,cum[np.maximum(i,0)],np.nan); vj=np.where(okJ,cum[np.maximum(j,0)],0.0)
        return np.where(okI,vi-vj,0.0)
    for W in (250,500,1000,2000):
        U[f'contra{W}']=win(tL,against_L,c-W,c)+win(tC,against_C,c-W,c)
        U[f'nprint{W}']=win(tL,nall,c-W,c)+win(tC,nall,c-W,c)
    out.append(U)
F=pd.concat(out,ignore_index=True); F=F[F.y_loss.notna()]
F['per']=np.where(F.dia<='2026-10-29','DISC','HOLD')
g=F.groupby(['bloque','mkt']); F['ntk']=g.tw.transform('nunique'); F['tau1']=g.tau_abs.transform('min'); F['gap']=F.tau_abs-F.tau1
F['rank']=g.tau_abs.rank(method='first')-1
ev=lambda S: S.pnl_mk.sum()/S.c.sum()
def ic(S,by,B=1000):
    gg=S.groupby(by).agg(p=('pnl_mk','sum'),c=('c','sum')); p=gg.p.values; cc=gg.c.values; i=rng.integers(0,len(gg),(B,len(gg))); return tuple(np.round(np.quantile(p[i].sum(1)/cc[i].sum(1),[.05,.95]),3))
F['grupo']=np.where(F.ntk<2,'solo',np.where(F['rank']==0,'rafaga_1o','rafaga_sig'))
print('EV maker por posicion en rafaga:')
for per in ('DISC','HOLD'):
    for gname in ('solo','rafaga_1o','rafaga_sig'):
        S=F[(F.per==per)&(F.grupo==gname)]; print(per,gname,len(S),round(ev(S),4),'IC90dia',ic(S,'dia'),'IC90cierre',ic(S,'cierre'))
S=F[F.grupo=='rafaga_sig']; print('hueco desde 1er print de la rafaga (ms) p10/25/50/75/90',np.percentile(S.gap,[10,25,50,75,90]).round())
B=F[F.esB]; print('B:',len(B),'grupo',B.grupo.value_counts().to_dict()); print('B hueco (ms) en rafaga_sig',np.percentile(B[B.grupo=='rafaga_sig'].gap,[10,25,50,75,90]).round() if (B.grupo=='rafaga_sig').sum() else '-')
V=pd.read_csv(DD+'b_fills_vida.csv')[['tx','gana','pnl','coste']]; BB=B.merge(V,on='tx')
print(BB.groupby('grupo').apply(lambda X: pd.Series({'n':len(X),'gana':X.gana.mean(),'EV_B':X.pnl.sum()/X.coste.sum(),'pnl':X.pnl.sum()}),include_groups=False).round(3))
print('Regla ex ante candidata: marcar si hubo prints contra L en [c-W,c] (c=tau-100 ms). EXCESO = EV(no marcadas) - EV(todas):')
for W in (250,500,1000,2000):
    for per in ('DISC','HOLD'):
        S=F[F.per==per]; m=S[f'contra{W}']>0
        e_all=ev(S); e_no=ev(S[~m]); e_si=ev(S[m])
        bs=[]; dias=S.dia.unique()
        for _ in range(500):
            dd=rng.choice(dias,len(dias)); X=pd.concat([S[S.dia==d] for d in dd]); mm=X[f'contra{W}']>0; bs.append(ev(X[~mm])-ev(X))
        print(f' W={W} {per} marcadas {m.mean():.3f} EV_marcadas {e_si:.4f} EV_no {e_no:.4f} EV_todas {e_all:.4f} EXCESO {e_no-e_all:+.4f} IC90dia {tuple(np.round(np.quantile(bs,[.05,.95]),4))}')
    mB=BB[f'contra{W}']>0 if f'contra{W}' in BB else None
for W in (250,500,1000,2000):
    m=BB[f'contra{W}']>0; print(f' B W={W}: marcadas {int(m.sum())}/{len(BB)} EV_B marcadas {BB[m].pnl.sum()/max(BB[m].coste.sum(),1e-9):.3f} no marcadas {BB[~m].pnl.sum()/BB[~m].coste.sum():.3f}')
# ¿la rafaga se ve venir? fraccion de rafaga_sig con print contrario previo (W=500) vs solo
for gname in ('solo','rafaga_1o','rafaga_sig'): print(gname,'contra500>0: %.3f'%(F[F.grupo==gname].contra500>0).mean())
F[['tx','grupo','ntk','gap','rank']+[f'contra{W}' for W in (250,500,1000,2000)]].to_parquet(DD+'s10_rafagas.parquet')
