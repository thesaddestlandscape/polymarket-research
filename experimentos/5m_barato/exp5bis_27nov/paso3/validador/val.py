import json,glob,collections,sys
def q(x,p):
    x=sorted(x); return None if not x else round(x[min(len(x)-1,int(p*len(x)))],1)
def rs(x): return dict(n=len(x),p10=q(x,.1),p50=q(x,.5),p90=q(x,.9)) if x else None
run,dfile,order=sys.argv[1],sys.argv[2],sys.argv[3]  # order: seq | tms
I,P,C,E={}, {}, {}, {}
for l in open(run+'/ledger.jsonl'):
    r=json.loads(l);k=r.get('k')
    if k=='intencion': I[r['oid_local']]=r
    elif k=='post' and r.get('clase')=='ok' and r.get('t_send_ns'): P[r['oid_local']]=r
    elif k=='cancel' and r.get('ok') and r.get('intento')==1 and r.get('t_ack_ns'): C[r['oid']]=r
for f in glob.glob(run+'/cancel_evid/*.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r.get('k')=='user_order' and r.get('mine'): E[(r['tipo'],r['oid'])]=r
lv=collections.defaultdict(list)
for l in open(dfile):
    c=l.strip().split(',')
    if c[3]!='B': continue
    lv[c[2]].append((int(c[1]),float(c[5]),int(c[6]),int(c[7])))
ev=collections.defaultdict(list) # tok -> (t_ms, delta, rx)
for tok,a in lv.items():
    a.sort(key=(lambda z:(z[3])) if order=='seq' else (lambda z:(z[0],z[1],z[2])))
    for i in range(1,len(a)):
        d=a[i][1]-a[i-1][1]
        if abs(abs(d)-5)<0.006: ev[tok].append((a[i][0],round(d),a[i][2]))
own_t=collections.defaultdict(list)
for oid,p in P.items():
    tok=I[oid]['tok']; own_t[tok].append(p['t_send_ns']/1e6)
    if oid in C: own_t[tok].append(C[oid]['t_send_ns']/1e6)
# background rate: +-5 events farther than 3 s from any own send
bg=collections.Counter(); dur=collections.Counter()
coin_of={I[o]['tok']:I[o]['coin'] for o in I}
for tok,a in lv.items():
    if not a: continue
    T=sorted(own_t[tok]); span=(max(z[0] for z in a)-min(z[0] for z in a))/1000
    dur[coin_of.get(tok)]+=span
    for t,d,rx in ev[tok]:
        if all(abs(t-s)>3000 for s in T): bg[coin_of.get(tok)]+=1
R=collections.defaultdict(lambda:collections.defaultdict(list)); X=collections.defaultdict(collections.Counter)
for oid,p in P.items():
    i=I[oid]; c=i['coin']; tok=i['tok']
    for kind,sgn,ts,ta,ue in [('alta',5,p['t_send_ns']/1e6,p['t_ack_ns']/1e6,E.get(('PLACEMENT',oid)))]+([('cancel',-5,C[oid]['t_send_ns']/1e6,C[oid]['t_ack_ns']/1e6,E.get(('CANCELLATION',oid)))] if oid in C else []):
        m=[e for e in ev[tok] if e[1]==sgn and ts-50<=e[0]<=ts+2000]
        for k in (c,'TODAS'):
            X[k][kind+'_n']+=1
            if len(m)==0: X[k][kind+'_0']+=1
            elif len(m)>1: X[k][kind+'_multi']+=1
            elif m[0][0]<ts-5: X[k][kind+'_neg']+=1
            else:
                t,d,rx=m[0]
                R[k][kind+'_ex_envio'].append(t-ts); R[k][kind+'_rx_envio'].append(rx-ts)
                R[k][kind+'_ex_ack'].append(t-ta)
                if ue: R[k][kind+'_ex_menos_userex'].append(t-ue['ts_ex_ms'])
                if t>ta: X[k][kind+'_post_ack']+=1
            # first-match (engineer style window -20..3500)
            m2=[e for e in ev[tok] if e[1]==sgn and ts-20<=e[0]<=ts+3500]
            if m2: R[k][kind+'_first_ex_envio_eng'].append(min(m2)[0]-ts)
out={}
for k in ('ETH','SOL','XRP','BTC','TODAS'):
    out[k]=dict(excl=dict(X[k]),**{n:rs(v) for n,v in R[k].items()})
    if k!='TODAS': out[k]['bg_ev_por_s']=round(bg[k]/max(dur[k],1),3); out[k]['bg_n']=bg[k]; out[k]['dur_s']=round(dur[k])
print(json.dumps(out,indent=0))
