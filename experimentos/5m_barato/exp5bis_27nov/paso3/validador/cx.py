import json,sys,collections,glob
def q(x,p):
    x=sorted(x); return x[min(len(x)-1,int(p*len(x)))] if x else None
for d in sys.argv[1:]:
    I={};C={};CA={};P={}
    for l in open(d+'/ledger.jsonl'):
        try:r=json.loads(l)
        except: continue
        if r['k']=='intencion': I[r['oid_local']]=r
        if r['k']=='cancel' and r.get('ok') and r.get('intento')==1: C[r['oid']]=r
        if r['k']=='post' and r.get('t_send_ns'): P[r['oid_local']]=r
    for f in glob.glob(d+'/cancel_evid/*.jsonl'):
        for l in open(f):
            try:r=json.loads(l)
            except: continue
            if r['k']=='user_order' and r.get('mine') and r['tipo']=='CANCELLATION': CA[r['oid']]=r
    g=collections.defaultdict(lambda: collections.defaultdict(list))
    for oid,c in C.items():
        if oid not in CA or oid not in I: continue
        co=I[oid]['coin']; ts=c['t_send_ns']/1e6; ta=c['t_ack_ns']/1e6; e=CA[oid]
        for k in ('all',co):
            g[k]['delRTT'].append(ta-ts); g[k]['ex-send'].append(e['ts_ex_ms']-ts); g[k]['ex-ack'].append(e['ts_ex_ms']-ta); g[k]['recv-ex'].append(e['t_recv_ms']-e['ts_ex_ms'])
    print('==',d)
    for k in ('all','BTC','ETH','SOL','XRP'):
        print(k,{m:'%d/%d/%d(n%d)'%(q(v,.1),q(v,.5),q(v,.9),len(v)) for m,v in g[k].items()})
