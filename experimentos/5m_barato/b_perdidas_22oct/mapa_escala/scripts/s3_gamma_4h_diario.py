# s3: tokens y desenlaces de mercados 4h (slug {coin}-updown-4h-{ts}) y diarios ({nombre}-up-or-down-on-{mes}-{d}-{a}) de 17..21-Oct via gamma (solo metadata). Salida datalogs/mapa_escala/tokens_extra.json
import requests, json, time, datetime as dt
G='https://gamma-api.polymarket.com/markets'; S=requests.Session()
COIN={'btc':'BTC','eth':'ETH','sol':'SOL','xrp':'XRP','doge':'DOGE','bnb':'BNB'}
NOM={'bitcoin':'BTC','ethereum':'ETH','solana':'SOL','xrp':'XRP','dogecoin':'DOGE','bnb':'BNB'}
MES=['january','february','march','april','may','june','july','august','september','october','november','december']
out={}; vol={}; miss=[]
def parse(m,coin,marco):
    tk=json.loads(m['clobTokenIds']) if isinstance(m['clobTokenIds'],str) else m['clobTokenIds']
    oc=json.loads(m['outcomes']) if isinstance(m['outcomes'],str) else m['outcomes']
    pr=json.loads(m['outcomePrices']) if isinstance(m['outcomePrices'],str) else m['outcomePrices']
    fin=int(dt.datetime.fromisoformat(m['endDate'].replace('Z','+00:00')).timestamp())
    up=[i for i,o in enumerate(oc) if str(o).lower() in ('up','yes')]; ui=up[0] if up else 0
    win='YES' if float(pr[ui])>=0.999 else ('NO' if float(pr[1-ui])>=0.999 else None)
    for i,t in enumerate(tk): out[t]=[coin,marco,str(m['id']),fin,'YES' if i==ui else 'NO',win]
    vol[str(m['id'])]=[coin,marco,fin,float(m.get('volume') or 0),win]
t0=int(dt.datetime(2026,10,17,20,tzinfo=dt.timezone.utc).timestamp()); t1=int(dt.datetime(2026,10,22,4,tzinfo=dt.timezone.utc).timestamp())
for c,C in COIN.items():
    for te in range(t0-t0%14400+14400,t1+1,14400):
        ok=False
        for ts in (te,te-14400):
            j=S.get(G,params={'slug':f'{c}-updown-4h-{ts}','closed':'true'},timeout=15).json()
            if isinstance(j,list) and j and int(dt.datetime.fromisoformat(j[0]['endDate'].replace('Z','+00:00')).timestamp())==te: parse(j[0],C,'240min'); ok=True; break
        if not ok: miss.append((c,te))
for n,C in NOM.items():
    for dd in range(17,23):
        d=dt.date(2026,10,dd); j=S.get(G,params={'slug':f'{n}-up-or-down-on-{MES[d.month-1]}-{d.day}-{d.year}','closed':'true'},timeout=15).json()
        if isinstance(j,list) and j: parse(j[0],C,'24h')
        else: miss.append((n,dd))
json.dump(out,open('/root/polymarket-research-datalogs/mapa_escala/tokens_extra.json','w')); json.dump(vol,open('/root/polymarket-research-datalogs/mapa_escala/mercados_extra_vol.json','w'))
print(len(out)//2,'mercados',len(miss),'faltan',miss[:10])
import collections; print(collections.Counter((v[1],v[5] is not None) for v in out.values()))
