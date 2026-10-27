#!/usr/bin/env python3
"""f8: rasgos de construccion de pares por wallet (cohorte 48 grandes makers BTC 5m + volumen>300k) en DESCUBRIMIENTO (06..17-Oct) y su relacion con el EV en HOLDOUT (18..23-Oct). Pares FIFO, pata suelta mantenida a resolucion.
EV = (pnl + rebate inferido)/coste. Rasgos (solo descubrimiento): f_emp (acciones emparejadas/acciones), f_par (mercados con par), lock (margen FIFO/EUR), mg_med (mediana ponderada), f_neg (frac acc margen<0), f_m4 (frac acc margen>=4c), ret_med (retardo mediano s), f_suelta50 (mercados con >50% suelta), loose_ev."""
import os,pandas as pd,numpy as np,glob,scipy.stats as ss
pref='datos/c48'; MK=pd.read_pickle(pref+'_mercado.pkl')
D0,D1,H0,H1='2026-10-06','2026-10-17','2026-10-18','2026-10-23'
def wq(x,w,q):
    o=np.argsort(x); x=np.asarray(x)[o]; w=np.asarray(w)[o]; c=np.cumsum(w)/w.sum(); return x[min(np.searchsorted(c,q),len(x)-1)]
rows=[]
for a in sorted(MK.maker.unique()):
    import os
    CPc=['maker','mid','dia','acc','margen','p1','p2','delay','T1','T2','lado1','rol1','rol2']; CLc=['maker','mid','dia','lc','pc','acc','T','pnl']
    pa=pd.read_pickle(f'{pref}_{a}_pares.pkl') if os.path.exists(f'{pref}_{a}_pares.pkl') else pd.DataFrame(columns=CPc)
    lo=pd.read_pickle(f'{pref}_{a}_suelta.pkl') if os.path.exists(f'{pref}_{a}_suelta.pkl') else pd.DataFrame(columns=CLc)
    m=MK[MK.maker==a]
    for per,(x0,x1) in (('D',(D0,D1)),('H',(H0,H1))):
        p=pa[(pa.dia.astype(str)>=x0)&(pa.dia.astype(str)<=x1)]; l=lo[(lo.dia.astype(str)>=x0)&(lo.dia.astype(str)<=x1)]; mm=m[(m.dia>=x0)&(m.dia<=x1)]
        c=mm.coste.sum()
        if c<=0 or len(mm)<100: continue
        r=dict(maker=a,per=per,n=len(mm),coste=c,ev=(mm.pnl.sum()+mm.reb.sum())/c,ev_sinreb=mm.pnl.sum()/c,reb=mm.reb.sum()/c)
        if len(p)>0:
            w=p.acc.values.astype(float); g=p.margen.values.astype(float)
            r.update(lock=(w*g).sum()/c,loose=l.pnl.sum()/c,f_emp=2*w.sum()/mm.acc.sum(),f_par=p.mid.nunique()/len(mm),mg_med=wq(g,w,.5),f_neg=w[g<0].sum()/w.sum(),f_m4=w[g>=.04].sum()/w.sum(),ret_med=wq(p.delay.values.astype(float),w,.5),
                     loose_ev=(l.pnl.sum()/(l.acc*l.pc).sum()) if len(l) else np.nan, f_suelta50=np.nan)
        rows.append(r)
F=pd.DataFrame(rows); F.to_csv('datos/f8_rasgos.csv',index=False)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
D=F[F.per=='D'].set_index('maker'); H=F[F.per=='H'].set_index('maker')
print('wallets D',len(D),'H',len(H)); 
print('EV(+reb)/EUR cohorte D: ponderado %.4f ; mediana %.4f ; H: ponderado %.4f ; mediana %.4f'%((D.ev*D.coste).sum()/D.coste.sum(),D.ev.median(),(H.ev*H.coste).sum()/H.coste.sum(),H.ev.median()))
print('ganadores/controles (D):'); print(D.loc[[i for i in D.index if i[:10] in ('0x21f4c1a1','0xe29042f5','0x86b14772','0x85a186d1','0x9d57c42e')],['n','coste','ev','lock','loose','f_emp','f_par','mg_med','f_neg','f_m4','ret_med','loose_ev']].round(4))
J=D.join(H[['ev','coste']],rsuffix='_H',how='inner'); print('persistencia EV D->H: spearman %.2f n=%d'%(ss.spearmanr(J.ev,J.ev_H)[0],len(J)))
print('Rasgo(D) vs EV_H  (spearman, p); K=9 rasgos -> Bonferroni p<0.0056')
for f in ('lock','loose','f_emp','f_par','mg_med','f_neg','f_m4','ret_med','loose_ev'):
    j=J[[f,'ev_H']].dropna(); r,p=ss.spearmanr(j[f],j.ev_H); r2,p2=ss.spearmanr(j[f],J.loc[j.index,'ev'])
    print(f'  {f:9s} vs EV_H: rho {r:+.2f} p {p:.3f} (n={len(j)}) | vs EV_D (mecanico): {r2:+.2f}')
# cohorte: distribucion margen FIFO global
allw=[];allg=[]
for a in D.index:
    if not os.path.exists(f'{pref}_{a}_pares.pkl'): continue
    pa=pd.read_pickle(f'{pref}_{a}_pares.pkl'); pa=pa[(pa.dia.astype(str)>=D0)&(pa.dia.astype(str)<=D1)]; allw.append(pa.acc.values); allg.append(pa.margen.values)
w=np.concatenate(allw).astype(float); g=np.concatenate(allg).astype(float)
print('cohorte D: margen FIFO por accion ponderado: p10 %.3f p25 %.3f p50 %.3f p75 %.3f p90 %.3f ; frac<0 %.2f ; 0-2c %.2f ; 2-5c %.2f ; 5-10c %.2f ; >=10c %.2f'%(tuple(wq(g,w,q) for q in (.1,.25,.5,.75,.9))+tuple(w[(g>=a_)&(g<b_)].sum()/w.sum() for a_,b_ in ((-9,0),(0,.02),(.02,.05),(.05,.1),(.1,9)))))
