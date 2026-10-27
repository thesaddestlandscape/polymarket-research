# resuelve por gamma (closed=true) los mid de las unidades F3 sin desenlace en caches; escribe SOLO datos/des_extra.json (YES si outcomePrices[0]>=0.999, NO si [1]>=0.999)
import pandas as pd, glob, json, requests, os
V='/mnt/HC_Volume_106538179/agentes_datos/f3_carry/'; D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f3_carry/datos/des_extra.json'
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json')); DES.update(json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json')))
DES.update(json.load(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/datos/des_extra.json')))
ex=json.load(open(D)) if os.path.exists(D) else {}
mids=set()
for f in glob.glob(V+'u_*.csv.gz'): mids|=set(pd.read_csv(f,usecols=['mid'],dtype={'mid':str}).mid)
for f in glob.glob(V+'vpv_*.csv.gz'): mids|=set(pd.read_csv(f,usecols=['mercado'],dtype={'mercado':str}).mercado)
pend=sorted(m for m in mids if m not in DES and m not in ex); print('pendientes',len(pend),'de',len(mids))
S=requests.Session(); nres=0
for k in range(0,len(pend),40):
    try:
        for m in S.get('https://gamma-api.polymarket.com/markets',timeout=25,params=[('id',x) for x in pend[k:k+40]]+[('closed','true'),('limit','40')]).json() or []:
            pr=m.get('outcomePrices'); pr=json.loads(pr) if isinstance(pr,str) else pr
            if pr and float(pr[0])>=0.999: ex[str(m['id'])]='YES'; nres+=1
            elif pr and float(pr[1])>=0.999: ex[str(m['id'])]='NO'; nres+=1
    except Exception as e: print('lote',k//40,type(e).__name__)
json.dump(ex,open(D,'w')); print('resueltos',nres,'quedan sin resolver',len([m for m in pend if m not in ex]))
