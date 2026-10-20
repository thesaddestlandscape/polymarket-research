import sys,json,gzip,collections,datetime,bisect,statistics
sys.path.insert(0,'/tmp/claude-0/-root-polymarket-research/06f7b0e2-eafc-4b79-84cd-46f932c672b1/scratchpad')
import analiza as A
L5='/root/polymarket-research-datalogs/experimento_h47_A_ledger.jsonl'
mk={}; orders={}
def ts(s): return int(datetime.datetime.fromisoformat(s).timestamp()*1000)
for l in open(L5):
    try:d=json.loads(l)
    except: continue
    t=d['tipo']
    if t=='mercado_inicio': mk[d['slug']]=(d['coin'].upper(),d['id'])
    elif t=='intencion_post': orders[d['oid']]={'slug':d['slug'],'tok':d['tok'],'lado':d['lado'],'p':d['precio'],'t_int':ts(d['ts'])}
    elif t=='post_ok' and d['oid'] in orders: orders[d['oid']]['cola']=d['cola']; orders[d['oid']]['t_ok']=ts(d['ts'])
    elif t=='fuera_libro' and d['oid'] in orders: orders[d['oid']]['t_out']=ts(d['ts'])
by=collections.defaultdict(list)
for oid,o in orders.items():
    if 'cola' in o and o['slug'] in mk: by[mk[o['slug']]].append(o)
res=[]
for (coin,mid),lst in by.items():
    path=A.C+f'mk/{coin}_{mid}.gz'
    try: ev=A.load(path)
    except Exception: continue
    # replay bids por token(Y/N)
    tokside={}
    for tk,v in A.TOK.items():
        if v[1]==mid: tokside[tk]=v[2][0]
    bids={'Y':{},'N':{}}; valid={'Y':False,'N':False}
    times=[]; snaps=[]
    lst.sort(key=lambda o:o['t_int'])
    oi=0
    for e in ev:
        while oi<len(lst) and e[0]>lst[oi]['t_int']:
            o=lst[oi]; L=tokside.get(o['tok'])
            q=int(round(o['p']*1000))
            if L and valid[L]: res.append((coin,o['p'],o['cola'],bids[L].get(q,0.0),o['t_int']))
            oi+=1
        t=e[1]
        if t=='G': valid['Y' if e[2]=='*' else e[2]]=False; 
        elif t=='B': bids[e[2]]=dict(e[3]); valid[e[2]]=True
        elif t=='d' and e[3]=='B' and valid[e[2]]:
            if e[5]>0: bids[e[2]][e[4]]=e[5]
            else: bids[e[2]].pop(e[4],None)
print('ordenes comparables',len(res))
ok=sum(1 for c,p,cola,mine,t in res if abs(cola-mine)<=max(1.0,0.02*cola))
print('cola ledger == nivel reconstruido (±2% o 1 acc):',ok,len(res),round(ok/len(res),3))
rel=[abs(cola-mine)/max(cola,1) for c,p,cola,mine,t in res]
print('error rel mediana',statistics.median(rel),'p90',statistics.quantiles(rel,n=10)[-1])
# el ledger mide la cola con REST ANTES del envio (~100 ms) -> ver tambien el nivel 150 ms despues
