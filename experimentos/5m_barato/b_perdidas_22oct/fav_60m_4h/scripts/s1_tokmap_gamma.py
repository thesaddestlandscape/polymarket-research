# s1_tokmap_gamma.py: mapa token->mercado y desenlace OFICIAL desde gamma (series hourly y 4h), fin entre 11-Oct y 26-Oct. Solo GET publico.
import json, urllib.request, time, sys
OUT='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos/tokmap_gamma.json'
SER={'60min':{'BTC':'btc-up-or-down-hourly','ETH':'eth-up-or-down-hourly','SOL':'solana-up-or-down-hourly','XRP':'xrp-up-or-down-hourly','DOGE':'doge-up-or-down-hourly','BNB':'bnb-up-or-down-hourly'},
     '240min':{c:f'{c.lower()}-up-or-down-4h' for c in ['BTC','ETH','SOL','XRP','DOGE','BNB']}}
from datetime import datetime
def get(u):
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as r: return json.load(r)
        except Exception as e: time.sleep(2+k*3); err=e
    raise err
tok={}; mk={}; stats={}
for marco,d in SER.items():
    for coin,s in d.items():
        n=0; off=0
        while True:
            ev=get(f'https://gamma-api.polymarket.com/events?series_slug={s}&end_date_min=2026-10-11T00:00:00Z&end_date_max=2026-10-26T01:00:00Z&limit=100&offset={off}')
            if not ev: break
            for e in ev:
                for m in e.get('markets',[]):
                    ids=json.loads(m.get('clobTokenIds') or '[]'); outs=json.loads(m.get('outcomes') or '[]'); pr=json.loads(m.get('outcomePrices') or '[]')
                    if len(ids)!=2: continue
                    fin=int(datetime.fromisoformat(m['endDate'].replace('Z','+00:00')).timestamp())
                    w=None
                    if m.get('closed') and pr and sorted(pr)==['0','1']: w=outs[pr.index('1')]
                    mk[m['id']]=dict(coin=coin,marco=marco,fin=fin,slug=m['slug'],win=w,vol=float(m.get('volume') or 0),closed=m.get('closed'),fee=m.get('feeSchedule'))
                    for t,o in zip(ids,outs): tok[t]=[coin,marco,m['id'],fin,o]
                    n+=1
            off+=100
            if len(ev)<100: break
        stats[f'{coin}#{marco}']=n; print(coin,marco,n,flush=True)
json.dump(dict(tokens=tok,mercados=mk,stats=stats,generado=time.strftime('%FT%TZ',time.gmtime())),open(OUT,'w'))
