import sys,gzip,csv,json,collections,random,datetime as dt
D=sys.argv[1];S=sys.argv[2];EX='0xe111180000d2663c0091e4f400237545b87b996b'
OUT=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
tok={}
for l in open(f'{S}/k{D[-2:]}.csv'):
    c=l.rstrip('\n').split(','); tok[c[2]]=(c[3],c[4],c[5],dt.datetime.fromisoformat(c[6]).timestamp(),c[7])
def tb(e): return '0-30' if e<30 else ('30-120' if e<120 else ('120-240' if e<240 else '240-300'))
def pb(p): return '<=0.20' if p<=0.20 else ('>=0.80' if p>=0.80 else 'mid')
P=collections.defaultdict(lambda:[0.,0.,None])  # (rol,wallet,token,tb) -> sh,usd
with gzip.open(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz','rt') as f:
    r=csv.reader(f);next(r)
    for c in r:
        i=tok.get(c[9])
        if not i or i[1]!='5min' or i[0]!='BTC' or c[8]!='0': continue  # solo COMPRAS BTC 5m
        ma=float(c[10]);ta=float(c[11])
        if ta<=0: continue
        e=float(c[2])-(i[3]-300)
        if c[0]=='M': rol,w='T',c[6]
        elif c[0]=='F' and c[7].lower()!=EX: rol,w='K',c[6]
        else: continue
        x=P[(rol,w,c[9],tb(e))]; x[0]+=ta; x[1]+=ma
        if x[2] is None: x[2]=ma/ta
G=collections.defaultdict(list)
for (rol,w,tk,b),(sh,usd,p0) in P.items():
    i=tok[tk]; o=OUT.get(i[2])
    if o is None: continue
    win=1. if o==i[4] else 0.; p=usd/sh; f=0.07*p*(1-p)*sh
    pn=sh*win-usd+(-f if rol=='T' else 0.2*f)
    G[(rol,b,pb(p))].append((i[2],pn,usd))
def summ(v):
    cl=collections.defaultdict(lambda:[0,0])
    for k,a,b in v: cl[k][0]+=a; cl[k][1]+=b
    z=list(cl.values()); rnd=random.Random(1); o=[]
    for _ in range(500):
        s=[z[rnd.randrange(len(z))] for _ in z]; c=sum(q[1] for q in s); o.append(sum(q[0] for q in s)/c)
    o.sort(); pn=sum(q[0] for q in z); co=sum(q[1] for q in z)
    return (len(v),len(z),round(co),round(pn/co,4),round(o[25],4),round(o[475],4))
for k in sorted(G): print(D,k,summ(G[k]))
