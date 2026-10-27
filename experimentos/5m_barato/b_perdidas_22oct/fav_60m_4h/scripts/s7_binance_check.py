# s7: coincidencia desenlace gamma 60m vs vela 1H Binance (cierre >= apertura -> Up) para BTC/ETH/SOL/XRP/DOGE/BNB.
import json, urllib.request
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/fav_60m_4h/datos/'
G=json.load(open(D+'tokmap_gamma.json'))['mercados']; res={}
for c in ['BTC','ETH','SOL','XRP','DOGE','BNB']:
    u=f'https://api.binance.com/api/v3/klines?symbol={c}USDT&interval=1h&startTime=1791676800000&limit=1000'
    k={int(r[0])//1000:(float(r[1]),float(r[4])) for r in json.load(urllib.request.urlopen(u,timeout=30))}
    ok=n=0; mal=[]
    for m in G.values():
        if m['coin']!=c or m['marco']!='60min' or not m['win']: continue
        o=k.get(m['fin']-3600)
        if not o: continue
        n+=1; up='Up' if o[1]>=o[0] else 'Down'; ok+=up==m['win']
        if up!=m['win']: mal.append(m['slug'])
    res[c]=dict(n=n,coinciden=ok,discrepan=mal[:5]); print(c,n,ok,mal[:3])
json.dump(res,open(D+'binance_check.json','w'),indent=1)
