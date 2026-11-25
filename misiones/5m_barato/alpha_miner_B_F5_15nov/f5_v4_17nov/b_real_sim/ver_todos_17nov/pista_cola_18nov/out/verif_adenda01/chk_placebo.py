import sys, gzip, pickle, bisect, collections, numpy as np, pandas as pd
H='/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/pista_cola_18nov/out/'
FX='/tmp/claude-0/-root-polymarket-research/5055698c-f1c6-493f-8e00-51095bf98a56/scratchpad/fx/fx30m.csv.gz'
new=pickle.load(open(H+sys.argv[1],'rb')); old=pickle.load(open(H+'obsoletos_preD1/p1_btc_2026-11-12.pkl','rb'))
t0=1794453646660; t1=t0+1800000
def sel(d):
    P=d['PL']; P=P[(P.t>=t0)&(P.t<=t1)]; return P
Pn,Po=sel(new),sel(old)
keys=set(zip(Pn.X,Pn.p))|set(zip(Po.X,Po.p)); toks={k[0] for k in keys}
ch=collections.defaultdict(list)
with gzip.open(FX,'rt') as f:
    for l in f:
        if l[0]!='d': continue
        c=l.split(',')
        if len(c)<8 or c[2] not in toks or c[3]!='B': continue
        k=(c[2],round(float(c[4]),2))
        if k in keys: ch[k].append(int(c[6]))
for k in ch: ch[k].sort()
def dist(P):
    out=[]
    for x,p,t in zip(P.X,P.p,P.t):
        L=ch.get((x,p),[]); i=bisect.bisect_right(L,t)-1
        out.append(t-L[i] if i>=0 else np.nan)
    return np.array(out)
for nm,P in (('nuevo',Pn),('viejo',Po)):
    d=dist(P); v=d[~np.isnan(d)]
    print(nm,'n placebos en ventana',len(P),'con cambio previo',len(v),'frac t-ultimo_cambio<=50ms: %.3f'%np.mean(v<=50),'<=250ms: %.3f'%np.mean(v<=250),'mediana ms',np.median(v))
