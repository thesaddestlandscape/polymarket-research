#!/usr/bin/env python3
"""x0: desenlace oficial (gamma closed=true, lectura pública) de los mids sin desenlace -> datos/des_gamma.json. Ganador solo si outcomePrices es inequívoco (1/0)."""
import json,requests,time
miss=json.load(open('datos/mids_sin_des.json')); out={}
for k in range(0,len(miss),40):
    r=requests.get('https://gamma-api.polymarket.com/markets',params=[('id',x) for x in miss[k:k+40]]+[('closed','true'),('limit','40')],timeout=30).json() or []
    for m in r:
        pr=m.get('outcomePrices'); oc=m.get('outcomes')
        pr=json.loads(pr) if isinstance(pr,str) else pr; oc=json.loads(oc) if isinstance(oc,str) else oc
        if not pr or not oc: continue
        p=[float(x) for x in pr]
        if sorted(p)==[0.0,1.0]: out[str(m['id'])]='YES' if p[oc.index('Up') if 'Up' in oc else 0]==1.0 else 'NO'
    time.sleep(0.3)
json.dump(out,open('datos/des_gamma.json','w')); print('pedidos',len(miss),'resueltos',len(out))
