import json,requests,sys
S=sys.argv[1]
d=json.load(open(S+'/ledger_extract.json'))
c=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
slugs=sorted(set(k.split('|')[0] for k in d['pujas']))
ids={s:d['mk'][s] for s in slugs}
out={}
pend=[]
for s,i in ids.items():
    if i in c: out[s]=c[i]
    else: pend.append((s,i))
print('cache',len(out),'pend',len(pend))
for k in range(0,len(pend),40):
    lote=pend[k:k+40]
    r=requests.get('https://gamma-api.polymarket.com/markets',timeout=20,params=[('id',i) for s,i in lote]+[('closed','true'),('limit','40')]).json()
    byid={str(m['id']):m for m in r}
    for s,i in lote:
        m=byid.get(str(i))
        if not m: continue
        pr=m.get('outcomePrices'); pr=json.loads(pr) if isinstance(pr,str) else pr
        if pr and float(pr[0])>=0.999: out[s]='YES'
        elif pr and float(pr[1])>=0.999: out[s]='NO'
print('total',len(out),'of',len(slugs))
json.dump(out,open(S+'/des_pujas.json','w'))
