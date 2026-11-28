import json,sys,collections,statistics as st
def q(x,p): x=sorted(x); return x[min(len(x)-1,int(p*len(x)))] if x else None
for run in sys.argv[1:]:
    D='/root/polymarket-research-datalogs/paquete_l/'+run
    I={};req=[]
    for l in open(D+'/ledger.jsonl'):
        r=json.loads(l)
        if r.get('k')=='intencion': I[r['oid_local']]=r['coin']
        elif r.get('k')=='post' and r.get('t_ack_ns'): req.append(('P',I.get(r['oid_local']),r['t_send_ns']/1e6,r['t_ack_ns']/1e6))
        elif r.get('k')=='cancel' and r.get('t_ack_ns') and r.get('intento')==1: req.append(('C',I.get(r['oid']),r['t_send_ns']/1e6,r['t_ack_ns']/1e6))
    cnt=collections.Counter((t,c) for t,c,_,_ in req); print(run, dict(cnt))
    by=collections.defaultdict(list)
    for t,c,s,a in req:
        inflight=sum(1 for t2,c2,s2,a2 in req if s2<s<a2)
        by[(t,min(inflight,2))].append(a-s); by[(t,c)].append(a-s)
    for k in sorted(by,key=str): print(' ',k,'n',len(by[k]),'p50 %.0f p90 %.0f'%(q(by[k],.5),q(by[k],.9)))
    # tiempo: primera vs segunda mitad
    req.sort(key=lambda x:x[2]); h=len(req)//2
    print('  1a mitad p50/p90 %.0f/%.0f  2a %.0f/%.0f'%(q([a-s for *_,s,a in req[:h]],.5),q([a-s for *_,s,a in req[:h]],.9),q([a-s for *_,s,a in req[h:]],.5),q([a-s for *_,s,a in req[h:]],.9)))
