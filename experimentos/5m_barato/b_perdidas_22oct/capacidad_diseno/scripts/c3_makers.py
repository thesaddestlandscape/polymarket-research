#!/usr/bin/env python3
"""c3: persistencia de makers 5m (todas monedas y bandas) elegidos en DESC (06..13-Oct) y medidos en OOS (14..21). Fuente mapa_escala/datos/niche_maker_dia.csv.gz.
EV pond. por EUR (sum pnl / sum coste), sin y con rebate inferido. Placebo = misma cantidad de makers al azar con volumen DESC comparable (cuartil de volumen). IC90 bootstrap de MAKERS."""
import csv, gzip, collections, numpy as np, sys
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_maker_dia.csv.gz'
rng=np.random.default_rng(20261024)
marco=sys.argv[1] if len(sys.argv)>1 else '5min'
M=collections.defaultdict(lambda: np.zeros(8))  # desc c,p,r ; oos c,p,r ; dias_desc, dias_oos
dd=collections.defaultdict(set); do=collections.defaultdict(set)
coin_ev=collections.defaultdict(lambda: collections.defaultdict(lambda: np.zeros(2)))
for x in csv.DictReader(gzip.open(D,'rt')):
    if x['marco']!=marco: continue
    m=x['maker']; c=float(x['coste']); p=float(x['pnl']); r=float(x['reb']); d=x['dia']
    if d<='2026-10-13': M[m][0:3]+=[c,p,r]; dd[m].add(d)
    else: M[m][3:6]+=[c,p,r]; do[m].add(d)
    coin_ev[m][x['coin']]+=[c,p]
mk=[m for m in M if M[m][0]>=2000]   # >=2000 EUR de coste en DESC
A=np.array([M[m] for m in mk])
print(marco,'makers totales',len(M),'con >=2000 EUR DESC',len(mk))
def evw(S,k=1): 
    c=A[S,3].sum(); return (A[S,4].sum()+(A[S,5].sum() if k else 0))/c if c>0 else np.nan
evd=(A[:,1]+A[:,2])/A[:,0]
for etiqueta,key in (('EV DESC (con rebate)',evd),('PnL DESC absoluto',A[:,1]+A[:,2])):
    for frac in (0.05,0.10,0.25):
        n=max(5,int(len(mk)*frac)); top=np.argsort(-key)[:n]
        pl=[]
        for _ in range(500):
            # placebo: mismo n, mismos cuartiles de volumen (muestreo estratificado)
            q=np.digitize(A[:,0],np.quantile(A[:,0],[.25,.5,.75]))
            sel=[]
            for qi in range(4):
                k_=int((q[top]==qi).sum()); pool=np.where(q==qi)[0]
                if k_: sel+=list(rng.choice(pool,k_,replace=False))
            pl.append(evw(np.array(sel)))
        bs=[evw(top[rng.integers(0,n,n)]) for _ in range(1000)]
        ocup=A[top,3].sum()/len({d for m in mk for d in do[m]}) if mk else 0
        print(f"{etiqueta:22s} top {int(frac*100):2d}% n={n:3d} OOS EV(+reb)={evw(top):+.4f} IC90 makers=({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) placebo med={np.median(pl):+.4f} p(placebo>=)={(np.array(pl)>=evw(top)).mean():.3f} vol OOS/dia top={ocup:,.0f} pnlOOS/dia={ (A[top,4].sum()+A[top,5].sum())/8:,.0f}  pool OOS EV={evw(np.arange(len(mk))):+.4f}")
# top ex-post OOS: rentabilidad por maker (SOLO descriptivo: elegidos viendo OOS)
tot=A[:,1]+A[:,2]+A[:,4]+A[:,5]; vol=A[:,0]+A[:,3]
o=np.argsort(-tot)[:12]
print('TOP 12 ex-post por PnL total 16 d (descriptivo): maker, vol/dia, pnl_DESC, pnl_OOS(+reb), EV_total, dias activos desc/oos, monedas por volumen')
for i in o:
    m=mk[i]; ce=coin_ev[m]; cs=sorted(ce.items(),key=lambda kv:-kv[1][0])[:3]
    print(f"{m[:10]} vol/d={vol[i]/16:>9,.0f} pnlD={A[i,1]+A[i,2]:>9,.0f} pnlO={A[i,4]+A[i,5]:>9,.0f} EV={tot[i]/vol[i]:+.4f} dias={len(dd[m])}/{len(do[m])} "+' '.join(f"{c}:{v[0]/vol[i]*100:.0f}%" for c,v in cs))
print('suma PnL total makers con >=2000 DESC:',round(tot.sum()), ' vol total',round(vol.sum()), ' EV pond',round(tot.sum()/vol.sum(),4))
pos=(tot>0).sum(); print('makers con PnL total>0:',pos,'de',len(mk))
