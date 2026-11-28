import json,sys,collections,statistics as S
def q(x,p):
    x=sorted(x); 
    return x[min(len(x)-1,int(p*len(x)))] if x else None
for d in sys.argv[1:]:
    intent={};posts=[]
    for l in open(d+'/ledger.jsonl'):
        try:r=json.loads(l)
        except: continue
        if r['k']=='intencion': intent[r['clave']]=r
        if r['k']=='post' and r.get('ack_ms') is not None: posts.append(r)
    print('==',d,len(posts))
    g=collections.defaultdict(list)
    for p in posts:
        i=intent.get(p['clave'],{})
        g['all'].append(p['ack_ms']); g['coin:'+i.get('coin','?')].append(p['ack_ms']); g['v:'+str(i.get('clob_v'))].append(p['ack_ms'])
        g['v+coin:%s/%s'%(i.get('clob_v'),i.get('coin'))].append(p['ack_ms'])
        # lag intent->send (ms): local firma
        g['loc_dec_send'].append((p['t_send_ns']-i['t_decision_ns'])/1e6 if i else 0)
    for k,v in sorted(g.items()): print(k,len(v),'p50 %.0f p90 %.0f max %.0f'%(q(v,.5),q(v,.9),max(v)))
