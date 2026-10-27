#!/usr/bin/env python3
"""c2: diseno 'ventana de T al cierre' sobre mapa_escala/datos/s7_tiempo_dia.csv (dia,marco,tb,banda,grp[ALT3|OTRAS],coste,pnl,reb).
tb: 0 <=60 s, 1 (60,150], 2 (150,300], 3 (300,900], 4 (900,3600], 5 >3600. IC90 por DIAS (bootstrap 2000). EXPLORATORIO (146 celdas miradas en el mapa)."""
import csv, collections, numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/s7_tiempo_dia.csv'
rng=np.random.default_rng(20261024)
cel=collections.defaultdict(lambda: np.zeros(3))
for x in csv.DictReader(open(D)):
    cel[(x['dia'],x['marco'],int(x['tb']),int(x['banda']),x['grp'])]+=np.array([float(x['coste']),float(x['pnl']),float(x['reb'])])
def ev(marco,tbs,bandas,grps):
    por=collections.defaultdict(lambda: np.zeros(3))
    for (d,m,t,b,g),v in cel.items():
        if m==marco and t in tbs and b in bandas and g in grps: por[d]+=v
    ds=sorted(por); A=np.array([por[d] for d in ds]); 
    r=lambda M: M[:,1].sum()/M[:,0].sum()
    bs=[r(A[rng.integers(0,len(A),len(A))]) for _ in range(2000)]
    lo,hi=np.percentile(bs,[5,95])
    desc=[i for i,d in enumerate(ds) if d<='2026-10-13']; oos=[i for i,d in enumerate(ds) if d>'2026-10-13']
    k=np.setdiff1d(np.arange(len(A)),np.argsort(-A[:,1])[:2])
    return dict(vol=A[:,0].sum()/len(A),ev=r(A),lo=lo,hi=hi,dpos=int((A[:,1]>0).sum()),n=len(A),desc=r(A[desc]),oos=r(A[oos]),s2d=r(A[k]),evreb=(A[:,1].sum()+A[:,2].sum())/A[:,0].sum(),
                dias_oos=[round(float(A[i,1]/A[i,0]),3) for i in oos])
ALL=['ALT3','OTRAS']; ALT=['ALT3']
casos=[('5m ALL 0,10-0,30 T(60,150]','5min',[1],[2,3],ALL),('5m ALL 0,10-0,30 T(150,300]','5min',[2],[2,3],ALL),('5m ALL 0,10-0,30 T(60,300]','5min',[1,2],[2,3],ALL),
 ('5m ALT3 0,10-0,30 T(60,150]','5min',[1],[2,3],ALT),('5m ALT3 0,10-0,30 T(150,300] (donde opera B)','5min',[2],[2,3],ALT),('5m ALL 0,10-0,30 T<=60','5min',[0],[2,3],ALL),
 ('5m ALL 0,10-0,30 T(60,150] sin ALT3','5min',[1],[2,3],['OTRAS']),
 ('5m ALL 0,20-0,30 T(60,150]','5min',[1],[3],ALL),('5m ALL 0,10-0,20 T(60,150]','5min',[1],[2],ALL)]
for n,m,t,b,g in casos:
    r=ev(m,t,b,g)
    print(f"{n:44s} vol/d={r['vol']:>9,.0f} EV={r['ev']:+.3f} ICd=({r['lo']:+.3f},{r['hi']:+.3f}) d+={r['dpos']}/{r['n']} s2d={r['s2d']:+.3f} DESC={r['desc']:+.3f} OOS={r['oos']:+.3f} +reb={r['evreb']:+.3f} OOSdias={r['dias_oos']}")
