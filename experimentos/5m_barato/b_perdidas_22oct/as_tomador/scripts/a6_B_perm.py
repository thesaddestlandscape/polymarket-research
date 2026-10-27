#!/usr/bin/env python3
"""a6 (descriptivo, post-hoc): permutacion y bootstrap por cierre sobre los rellenos REALES de B (b_real_fills_taker.csv, a5).
EXCESO_B = EV_noflag - EV_total (positivo = saltar los banderados mejora). Permutacion de banderas a igual n_flag sobre los fills (sin estratos: n pequeno)."""
import json, numpy as np, pandas as pd
rng=np.random.default_rng(7)
D='datos/'
J=pd.read_csv(D+'b_real_fills_taker.csv'); S=json.load(open(D+'sets.json'))
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
acc=[]
for d in pd.date_range('2026-10-09','2026-10-18').strftime('%Y-%m-%d'):
    F=pd.read_parquet(CA+f'fills_{d}.parquet',columns=['is_tk','taker','side','act','mkt','lado','maker_amt','taker_amt']); F=F[(F.is_tk==0)&F.act.isin(('ETH','SOL','XRP'))].copy()
    F['des']=F.mkt.astype('int64').astype(str).map(DES); v=F.side.values==1
    F['sh']=np.where(v,F.maker_amt,F.taker_amt); F=F[(F.sh>0)&F.des.notna()].copy(); usd=np.where(F.side.values==1,F.taker_amt,F.maker_amt)
    lc=np.where(F.side.values==1,np.where(F.lado=='YES','NO','YES'),F.lado); pyes=np.where(F.lado.values=='YES',usd/F.sh.values,1-usd/F.sh.values); pc=np.where(lc=='YES',pyes,1-pyes)
    pnl_t=-(np.where(lc==F.des.values,F.sh.values,0)-F.sh.values*pc)-0.07*F.sh.values*pc*(1-pc)
    acc.append(pd.DataFrame({'taker':F.taker.str.lower().values,'p':pnl_t,'c':F.sh.values*(1-pc)}))
A=pd.concat(acc).groupby('taker').agg(p=('p','sum'),c=('c','sum'),n=('p','size')); A['roi']=A.p/A.c
inf=set(A[(A.n>=100)&(A.c>=200)&(A.roi>=0.02)].index)
J['cierre']=J.mercado.str.extract(r'(\d+)$')[0]
c=J.coste.values; p=J.pnl.values
def exc(f):
    return p[~f].sum()/c[~f].sum()-p.sum()/c.sum()
cl=J.cierre.values; uc=np.unique(cl); idx={u:np.where(cl==u)[0] for u in uc}
for nm,st in (('S_A',set(S['S_A'])),('inf_09_18',inf)):
    f=J.taker.isin(st).values; obs=exc(f); k=int(f.sum())
    perm=np.array([exc(rng.permutation(f)) for _ in range(5000)])
    bs=[]
    for _ in range(2000):
        s=np.concatenate([idx[u] for u in rng.choice(uc,len(uc))])
        ff=f[s]
        if ff.sum()==0 or ff.sum()==len(s): continue
        bs.append(p[s][~ff].sum()/c[s][~ff].sum()-p[s].sum()/c[s].sum())
    bs=np.array(bs)
    # sin el mejor cierre/fill banderado
    fi=np.where(f)[0]; w=fi[np.argsort(p[fi])][:1]  # el banderado mas perdedor
    f2=f.copy(); f2[w]=False
    print(nm,{'n_fills':len(J),'n_cierres':len(uc),'n_flag':k,'n_flag_cierres':int(len(set(cl[f]))),'EXCESO_B':round(obs,4),'IC90_cierre':[round(float(np.percentile(bs,5)),4),round(float(np.percentile(bs,95)),4)],'p_perm_unilateral':float((1+(perm>=obs).sum())/5001),'EXCESO_sin_peor_banderado':round(exc(f2),4),'pnl_flag':round(float(p[f].sum()),2),'pnl_noflag':round(float(p[~f].sum()),2),'coste_total':round(float(c.sum()),2)})
