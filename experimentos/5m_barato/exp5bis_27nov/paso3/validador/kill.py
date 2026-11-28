import json,random,collections
random.seed(1)
V=collections.defaultdict(list); DS=collections.defaultdict(list)
for run in ['/root/polymarket-research-datalogs/paquete_l/p1b_real_B_20261128T033520Z','/root/polymarket-research-datalogs/paquete_l/p1b_real_A_20261128T110605Z']:
    I={};P={}
    for l in open(run+'/ledger.jsonl'):
        r=json.loads(l)
        if r.get('k')=='intencion': I[r['oid_local']]=r
        if r.get('k')=='post' and r.get('clase')=='ok': P[r['oid_local']]=r
        if r.get('k')=='cancel' and r.get('ok') and r.get('intento')==1 and r.get('t_ack_ns'):
            V[(('B' if '_B_' in run else 'A'),I[r['oid']]['coin'])].append((r['t_ack_ns']-r['t_send_ns'])/1e6-23)
    for o,p in P.items(): DS[I[o]['coin']].append((p['t_send_ns']-I[o]['t_decision_ns'])/1e6)
U={'ETH':250,'SOL':200,'XRP':200}
def p90(x): x=sorted(x); return x[min(len(x)-1,int(.9*len(x)))]
for c,u in U.items():
    for tag in ['B','A']:
        x=V[(tag,c)]
        fd=sum(p90(random.choices(x,k=20))>u for _ in range(5000))/5000
        print(c,tag,'n',len(x),'P(p90 de 20 > U) =',round(fd,3))
for c,x in DS.items(): x=sorted(x); print('decision->envio',c,len(x),round(x[len(x)//2]),round(x[int(.9*len(x))]))
