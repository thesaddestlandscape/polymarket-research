#!/usr/bin/env python3
"""c5: umbral de pago del MAKER_REBATE. Por (maker,dia) compara inferido(5m+15m de ese dia) con pagado (activity MAKER_REBATE 00:45Z D+1). Solo GET publicos."""
import csv,gzip,collections,json,urllib.request,datetime,random
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_maker_dia.csv.gz'
inf=collections.defaultdict(lambda: collections.defaultdict(float)); vol=collections.defaultdict(float)
for x in csv.DictReader(gzip.open(D,'rt')):
    inf[x['maker']][x['dia']]+=float(x['reb']); vol[x['maker']]+=float(x['coste'])
random.seed(11)
pool=[m for m in vol if 1500<vol[m]<=60000]
sel=random.sample(pool,70)
filas=[]
for a in sel:
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(f"https://data-api.polymarket.com/activity?user={a}&limit=100&type=MAKER_REBATE",headers={'User-Agent':'x'}),timeout=20))
    except Exception as e: continue
    p=collections.defaultdict(float)
    for r in d:
        t=datetime.datetime.fromtimestamp(r['timestamp'],datetime.UTC); p[(t-datetime.timedelta(days=1)).strftime('%Y-%m-%d')]+=r['usdcSize']
    for dia,v in inf[a].items():
        if '2026-10-06'<=dia<='2026-10-21': filas.append((v,p.get(dia,0.0)))
import numpy as np
F=np.array(filas); print('maker-dias',len(F))
bins=[0,0.1,0.25,0.5,0.75,1.0,1.5,2,4,1e9]
for lo,hi in zip(bins[:-1],bins[1:]):
    s=F[(F[:,0]>=lo)&(F[:,0]<hi)]
    if len(s): print(f"inferido dia [{lo},{hi}): n={len(s):4d} con pago>0: {(s[:,1]>0).mean():.2f}  pagado/inferido (suma)={s[:,1].sum()/s[:,0].sum():.2f}")
