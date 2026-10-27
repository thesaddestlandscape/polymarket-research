#!/usr/bin/env python3
"""c4: ¿se paga el rebate maker (MAKER_REBATE en data-api activity) y cuanto frente al INFERIDO (0,014*(1-pc)*coste)? Solo GET publicos de lectura.
Compara por maker y por dia (pago del dia D+1 00:45Z a las wallets, vs inferido de fills del dia D en 5m+15m del mapa)."""
import csv,gzip,collections,json,urllib.request,datetime,sys,random
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos/niche_maker_dia.csv.gz'
inf=collections.defaultdict(lambda: collections.defaultdict(float)); vol=collections.defaultdict(float)
for x in csv.DictReader(gzip.open(D,'rt')):
    inf[x['maker']][x['dia']]+=float(x['reb']); vol[x['maker']]+=float(x['coste'])
random.seed(7)
def pagos(a):
    u=f"https://data-api.polymarket.com/activity?user={a}&limit=100&type=MAKER_REBATE"
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'x'}),timeout=20))
    out={}
    for r in d:
        t=datetime.datetime.fromtimestamp(r['timestamp'],datetime.UTC)
        dia_fills=(t-datetime.timedelta(days=1)).strftime('%Y-%m-%d')   # pago 00:45 D+1 por fills de D
        out[dia_fills]=out.get(dia_fills,0)+r['usdcSize']
    return out
# muestra estratificada por volumen total 16 d (todos los marcos del fichero 5m+15m)
mk=sorted(vol,key=lambda m:-vol[m])
estratos={'>500k':[m for m in mk if vol[m]>5e5],'50k-500k':[m for m in mk if 5e4<vol[m]<=5e5],'5k-50k':[m for m in mk if 5e3<vol[m]<=5e4],'0.5k-5k':[m for m in mk if 5e2<vol[m]<=5e3],'<500':[m for m in mk if vol[m]<=5e2]}
res=[]
for e,l in estratos.items():
    s=random.sample(l,min(8,len(l)))
    for a in s:
        try: p=pagos(a)
        except Exception as ex: print('err',a,ex); continue
        dias=[d for d in inf[a] if '2026-10-06'<=d<='2026-10-21']
        i=sum(inf[a][d] for d in dias); r=sum(p.get(d,0) for d in dias)
        nd_pag=sum(1 for d in dias if p.get(d,0)>0)
        res.append((e,a[:10],len(l),vol[a],i,r,nd_pag,len(dias)))
        print(f"{e:9s} {a[:10]} vol16d={vol[a]:>10,.0f} inferido={i:>8.2f} pagado={r:>8.2f} ratio={r/i if i else float('nan'):.2f} dias_con_pago={nd_pag}/{len(dias)}", flush=True)
