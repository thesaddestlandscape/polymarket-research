#!/usr/bin/env python3
"""r1: descarga TODO el historial MAKER_REBATE (data-api activity, GET publico) de una muestra de makers del mapa 5m+15m. Guarda pagos crudos."""
import csv,gzip,collections,json,urllib.request,time,random,sys
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_maker_dia.csv.gz'
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/rebate_ganadores/datos/r1_pagos.csv'
vol=collections.defaultdict(float)
for x in csv.DictReader(gzip.open(D,'rt')): vol[x['maker']]+=float(x['coste'])
random.seed(23)
mk=sorted(vol,key=lambda m:-vol[m])
sel=set(mk[:60])  # top 60 por volumen
for lo,hi,n in ((5e4,5e5,40),(5e3,5e4,50),(1e3,5e3,50),(1,1e3,40)):
    pool=[m for m in mk if lo<vol[m]<=hi]; sel|=set(random.sample(pool,min(n,len(pool))))
# anadir los 3 ganadores
for p in ('0x21f4c1a1','0xe29042f5','0x86b1'):
    sel|={m for m in mk if m.startswith(p)}
sel=sorted(sel); print(len(sel),'makers',flush=True)
def get(a):
    rows=[];off=0
    while True:
        u=f"https://data-api.polymarket.com/activity?user={a}&limit=100&offset={off}&type=MAKER_REBATE"
        for k in range(3):
            try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=25)); break
            except Exception as e: d=None; time.sleep(2)
        if d is None: return rows,False
        rows+=d
        if len(d)<100 or off>=500: return rows,True
        off+=100
with open(OUT,'w') as f:
    w=csv.writer(f); w.writerow(['maker','ts','usdc','vol16d'])
    for i,a in enumerate(sel):
        r,ok=get(a)
        for x in r: w.writerow([a,x['timestamp'],x['usdcSize'],round(vol[a],2)])
        if i%20==0: print(i,len(r),ok,flush=True)
        time.sleep(0.12)
