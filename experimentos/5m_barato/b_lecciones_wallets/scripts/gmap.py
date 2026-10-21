import json,requests,sys,time
from datetime import datetime,timezone
S=sys.argv[1]
t0=int(datetime(2026,10,20,tzinfo=timezone.utc).timestamp()); t1=int(datetime(2026,10,21,10,0,tzinfo=timezone.utc).timestamp())
slugs=[f'{c}-updown-5m-{s}' for c in ('eth','sol','xrp') for s in range(t0-300,t1,300)]
out={}
ses=requests.Session()
for closed in ('true','false'):
    pend=[s for s in slugs if s not in out]
    for k in range(0,len(pend),40):
        try:
            r=ses.get('https://gamma-api.polymarket.com/markets',timeout=25,params=[('slug',s) for s in pend[k:k+40]]+[('closed',closed),('limit','40')]).json()
        except Exception as e:
            print('err',e); continue
        for m in r:
            toks=json.loads(m['clobTokenIds']) if isinstance(m.get('clobTokenIds'),str) else m.get('clobTokenIds')
            outs=json.loads(m['outcomes']) if isinstance(m.get('outcomes'),str) else m.get('outcomes')
            pr=m.get('outcomePrices'); pr=json.loads(pr) if isinstance(pr,str) else pr
            des=None
            if m.get('closed') and pr:
                if float(pr[0])>=0.999: des='YES'
                elif float(pr[1])>=0.999: des='NO'
            out[m['slug']]=dict(id=str(m['id']),toks=toks,outs=outs,des=des,end=m.get('endDate'),closed=m.get('closed'))
        time.sleep(0.2)
print(len(slugs),len(out),sum(1 for v in out.values() if v['des']), set(tuple(v['outs']) for v in out.values()))
json.dump(out,open(S+'/gmap.json','w'))
