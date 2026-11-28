import json,sys,collections
def q(x,p):
    x=sorted(x); return x[min(len(x)-1,int(p*len(x)))] if x else None
for d in sys.argv[1:]:
    I={};P={};PL={};CA={}
    for l in open(d+'/ledger.jsonl'):
        try:r=json.loads(l)
        except: continue
        if r['k']=='intencion': I[r.get('oid_local')]=r
        if r['k']=='post' and r.get('t_send_ns'): P[r['oid_local']]=r
    import glob
    for f in glob.glob(d+'/cancel_evid/*.jsonl'):
        for l in open(f):
            try:r=json.loads(l)
            except: continue
            if r['k']=='user_order' and r.get('mine'):
                (PL if r['tipo']=='PLACEMENT' else CA)[r['oid']]=r
    g=collections.defaultdict(lambda: collections.defaultdict(list))
    for oid,p in P.items():
        if oid not in PL: continue
        c=I[oid]['coin']; ts=p['t_send_ns']/1e6; ta=p['t_ack_ns']/1e6; pl=PL[oid]
        for key in ('all',c):
            g[key]['ack-send'].append(ta-ts); g[key]['ex-send'].append(pl['ts_ex_ms']-ts); g[key]['recv-send'].append(pl['t_recv_ms']-ts); g[key]['recv-ack'].append(pl['t_recv_ms']-ta)
            g[key]['ex-ack'].append(pl['ts_ex_ms']-ta)
    print('==',d)
    for key in ('all','BTC','ETH','SOL','XRP'):
        print(key,{m:'%d/%d/%d(n%d)'%(q(v,.1),q(v,.5),q(v,.9),len(v)) for m,v in g[key].items()})
