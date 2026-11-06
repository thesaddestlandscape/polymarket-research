#!/usr/bin/env python3
# RE enjambre 5m (read-only). Relojes: t_exch/recv (CLOB WS, ms), ts_est (bloque on-chain, s), x recv (Binance).
import sys, gzip, json, csv, bisect, random, collections, datetime as dt
from array import array
D=sys.argv[1]; S=sys.argv[2]
V='/mnt/HC_Volume_106538179'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
OUT=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
tok={}  # token -> (coin, frame, mid, close_s, side)
for l in open(f'{S}/k{D[-2:]}.csv'):
    c=l.rstrip('\n').split(',')
    cl=dt.datetime.fromisoformat(c[6]).timestamp()
    tok[c[2]]=(c[3],c[4],c[5],cl,c[7])
qtok=set(x.strip() for x in open(f'{S}/tok_q.txt'))
# ---- registro: q (mid por recv) para BTC5/ETH5/BTC15, t para 5m BTC/ETH, x BTCUSDT por segundo
qs=collections.defaultdict(lambda:(array('d'),array('d')))
ts=collections.defaultdict(list)
bn={}
with gzip.open(f'{V}/m5_registro/m5_registro_{D}.csv.gz','rt') as f:
    for l in f:
        t0=l[0]
        if t0=='q':
            c=l.split(',')
            if c[2] in qtok and c[3] and c[4]:
                try: b=float(c[3]); a=float(c[4])
                except: continue
                if b>=a: continue  # libro cruzado/bloqueado fuera
                A=qs[c[2]]; A[0].append(float(c[7])); A[1].append((a+b)/2)
        elif t0=='t':
            c=l.split(',')
            if c[2] in qtok:
                ts[c[2]].append((int(c[1]),int(c[6]),float(c[3]),c[4],float(c[5])))
        elif t0=='x':
            if ',BTCUSDT,' in l:
                c=l.split(','); bn[int(c[7])//1000]=float(c[3])
import os
f15=f'{V}/m15_registro/m15_registro_{D}.csv.gz'
if os.path.exists(f15):
  with gzip.open(f15,'rt') as f:
    for l in f:
        if l[0]=='q':
            c=l.split(',')
            if c[2] in qtok and c[3] and c[4]:
                try: b=float(c[3]); a=float(c[4])
                except: continue
                if b>=a: continue
                A=qs[c[2]]; A[0].append(float(c[7])); A[1].append((a+b)/2)
for k_ in list(qs):
    A=qs[k_]; o=sorted(range(len(A[0])),key=A[0].__getitem__)
    qs[k_]=(array('d',(A[0][j] for j in o)),array('d',(A[1][j] for j in o)))
def mid_at(tk,ms):
    A=qs.get(tk)
    if not A or not len(A[0]): return None
    i=bisect.bisect_right(A[0],ms)-1
    return A[1][i] if i>=0 else None
def bn_at(s):
    for k in range(s,s-6,-1):
        if k in bn: return bn[k]
    return None
# ---- on-chain
aggr=[]   # M rows
mk_fills=[]  # maker fills (F, taker!=EXCH)
with gzip.open(f'{V}/m5_onchain/m5_onchain_{D}.csv.gz','rt') as f:
    r=csv.reader(f); next(r)
    for c in r:
        tk=c[9]; info=tok.get(tk)
        if not info or info[1]!='5min': continue
        ma=float(c[10]); ta=float(c[11]); side=c[8]
        if c[0]=='M':
            if side=='0': usd,sh=ma,ta
            else: usd,sh=ta,ma
            if sh<=0: continue
            aggr.append((float(c[2]),c[6].lower(),tk,side,sh,usd/sh,usd,c[3]))
        elif c[0]=='F' and c[7].lower()!=EXCH:
            if side=='0': usd,sh=ma,ta
            else: usd,sh=ta,ma
            if sh<=0: continue
            mk_fills.append((float(c[2]),c[6].lower(),c[7].lower(),tk,side,sh,usd/sh,usd))
print('aggr',len(aggr),'makerfills',len(mk_fills),file=sys.stderr)
def outcome(tk):
    i=tok[tk]; o=OUT.get(i[2])
    if o is None: return None
    return 1.0 if o==i[4] else 0.0
fee=lambda p,sh:0.07*p*(1-p)*sh
# ---- rasgos por wallet agresora (sin desenlaces)
W=collections.defaultdict(lambda:collections.Counter())
mk_cnt=collections.Counter()
bought=collections.defaultdict(set)
for (te,w,tk,side,sh,p,usd,tx) in aggr:
    i=tok[tk]; trem=i[3]-te; tel=te-(i[3]-300)
    X=W[w]; X['n']+=1; X['usd']+=usd
    if trem<60: X['late']+=usd
    if tel<30: X['open']+=usd
    if side=='1': X['sell']+=usd
    else:
        X['buy']+=usd
        if p<=0.20: X['cheap']+=usd
        if p>=0.80: X['fav']+=usd
        bought[(w,i[2])].add(i[4])
    X['coin_'+i[0]]+=1
for (te,mw,aw,tk,side,sh,p,usd) in mk_fills: mk_cnt[mw]+=1
both=collections.Counter(); mkts=collections.Counter()
for (w,m),s in bought.items():
    mkts[w]+=1
    if len(s)==2: both[w]+=1
def arquetipo(w):
    X=W[w]
    if X['n']<10: return 'COLA_<10'
    u=X['usd'] or 1e-9; b=X['buy'] or 1e-9
    mr=mk_cnt[w]/(mk_cnt[w]+X['n'])
    if mkts[w] and both[w]/mkts[w]>=0.5: return 'PARES'
    if X['late']/u>=0.5 and X['fav']/b>=0.5: return 'SNIPER_TARDIO_FAV'
    if X['cheap']/b>=0.5: return 'LONGSHOT_BARATO'
    if X['open']/u>=0.5: return 'APERTURA'
    if mr>=0.5: return 'HIBRIDO_MAKER'
    if X['sell']/u>=0.5: return 'VENDEDOR'
    return 'MIXTO'
arq={w:arquetipo(w) for w in W}
res={'dia':D,'n_aggr_orders':len(aggr),'n_wallets_aggr':len(W)}
tot=sum(X['usd'] for X in W.values()); top=sorted(((X['usd'],w) for w,X in W.items()),reverse=True)[:5]
res['top5_share_usd']=[(w[:10],round(u/tot,4)) for u,w in top]
# ---- PnL por posicion (wallet, mercado, token)
P=collections.defaultdict(lambda:[0,0,0,0,0,None,None])  # buy_sh,buy_usd,sell_sh,sell_usd,fee,first_te,first_p
for (te,w,tk,side,sh,p,usd,tx) in aggr:
    x=P[(w,tk)]
    if side=='0': x[0]+=sh; x[1]+=usd
    else: x[2]+=sh; x[3]+=usd
    x[4]+=fee(p,sh)
    if x[5] is None: x[5]=te; x[6]=p
def boot(rows,key,B=1000):  # rows: (cluster,pnl,cost); IC90 de sum pnl/sum cost por cluster de mercado
    cl=collections.defaultdict(lambda:[0,0])
    for k,pn,co in rows: cl[k][0]+=pn; cl[k][1]+=co
    v=list(cl.values()); 
    if len(v)<5: return None
    rnd=random.Random(1); out=[]
    for _ in range(B):
        s=[v[rnd.randrange(len(v))] for _ in v]; c=sum(z[1] for z in s)
        if c>0: out.append(sum(z[0] for z in s)/c)
    out.sort(); return (round(out[int(.05*len(out))],4),round(out[int(.95*len(out))],4),len(v))
grp=collections.defaultdict(list); miss=0; shorts=0
grp_coin=collections.defaultdict(list)
for (w,tk),x in P.items():
    o=outcome(tk)
    if o is None: miss+=1; continue
    if x[0]<=0 or x[2]>x[0]+1e-6: shorts+=1; continue
    pn=(x[0]-x[2])*o+x[3]-x[1]-x[4]
    i=tok[tk]; a=arq[w]
    pb='<=0.20' if x[6]<=0.20 else ('>=0.80' if x[6]>=0.80 else 'mid')
    grp[(a,)].append((i[2],pn,x[1])); grp[(a,i[0],pb)].append((i[2],pn,x[1]))
    grp[('ALL',i[0],pb)].append((i[2],pn,x[1]))
res['pos_sin_desenlace']=miss; res['pos_netas_vendedoras_excluidas']=shorts
def summ(rows):
    pn=sum(r[1] for r in rows); co=sum(r[2] for r in rows)
    return {'n_pos':len(rows),'coste':round(co,1),'pnl':round(pn,1),'ev_eur':round(pn/co,4) if co else None,'ic90_mercado':boot(rows,None)}
res['arquetipos_wallets']=collections.Counter(arq.values())
res['arq_usd']={a:round(sum(W[w]['usd'] for w in W if arq[w]==a)/tot,4) for a in set(arq.values())}
res['ev']={'|'.join(k):summ(v) for k,v in grp.items() if len(v)>=15 and (k[0]!='ALL' or True) and (len(k)==1 or k[1] in('BTC','ETH'))}
# ---- maker fills baratos BTC por arquetipo del agresor (donde nos pisan)
mg=collections.defaultdict(list)
for (te,mw,aw,tk,side,sh,p,usd) in mk_fills:
    i=tok[tk]
    if i[0]!='BTC' or side!='0' or p>0.20: continue
    o=outcome(tk)
    if o is None: continue
    mg[arq.get(aw,'NO_AGRESOR_M')].append((i[2],sh*o-usd+0.2*fee(p,sh),usd))
res['maker_bid_barato_BTC_por_arq_agresor']={k:summ(v) for k,v in mg.items()}
# ---- retraso on-chain y señal para hermanos (BTC 5m, ordenes grandes)
btc=[a for a in aggr if tok[a[2]][0]=='BTC']
thr=sorted(a[6] for a in btc)[int(.95*len(btc))] if btc else 0
res['umbral_grande_usd_p95_btc']=round(thr,2)
seen=set(); lags=[]; ev2=collections.defaultdict(list); nmatch=0; nbig=0
tk15={}  # close15 -> YES token
for t,i in tok.items():
    if i[0]=='BTC' and i[1]=='15min' and i[4]=='YES': tk15[i[3]]=t
eth5={}
for t,i in tok.items():
    if i[0]=='ETH' and i[1]=='5min' and i[4]=='YES': eth5[i[3]]=t
yes5={}
for t,i in tok.items():
    if i[0]=='BTC' and i[1]=='5min' and i[4]=='YES': yes5[i[3]]=t
for (te,w,tk,side,sh,p,usd,tx) in sorted(btc):
    big=usd>=thr; isseen=w in seen
    if big: seen.add(w)
    if not big: continue
    nbig+=1; i=tok[tk]
    # match con print WS: mismo token, tamaño igual, exch en [te-8, te+2] s
    best=None
    for (ex,rc,pp,sd,sz) in ts.get(tk,()):
        if abs(sz-sh)<0.01 and te*1000-8000<=ex<=te*1000+2000:
            if best is None or abs(te*1000-ex)<abs(te*1000-best[0]): best=(ex,rc)
    if best is None: continue
    nmatch+=1; lags.append(te*1000-best[1])
    dirn=(1 if i[4]=='YES' else -1)*(1 if side=='0' else -1)
    c15=i[3]-i[3]%900+(900 if i[3]%900 else 0)
    t_ws=best[1]; t_oc=te*1000+1000  # supuesto: log recibido 1 s tras ts_est
    for nombre,tkk in (('BTC15',tk15.get(c15)),('BTC5_mismo',yes5.get(i[3])),('ETH5',eth5.get(i[3]))):
        if not tkk: continue
        m0=mid_at(tkk,t_ws+300); m1=mid_at(tkk,t_oc); m2=mid_at(tkk,t_oc+30000)
        if None in (m0,m1,m2): continue
        ev2[(nombre,'WS+0.3s->oc')].append((i[2],dirn*(m1-m0)))
        ev2[(nombre,'oc->oc+30s','visto' if isseen else 'nuevo')].append((i[2],dirn*(m2-m1)))
        ev2[(nombre,'oc->oc+30s',arq[w])].append((i[2],dirn*(m2-m1)))
        ev2[(nombre,'oc->oc+30s','ALL')].append((i[2],dirn*(m2-m1)))
    b0=bn_at(int(best[1]//1000)-5); b1=bn_at(int(best[1]//1000))
    if b0 and b1: ev2[('BN_ret_5s_previo_signed_bps',)].append((i[2],dirn*(b1/b0-1)*1e4))
def mstat(rows):
    cl=collections.defaultdict(list)
    for k,v in rows: cl[k].append(v)
    v=[sum(z)/len(z) for z in cl.values()]
    if len(v)<5: return {'n':len(rows),'n_merc':len(v)}
    rnd=random.Random(2); o=sorted(sum(v[rnd.randrange(len(v))] for _ in v)/len(v) for _ in range(1000))
    return {'n':len(rows),'n_merc':len(v),'media':round(sum(v)/len(v),4),'ic90':(round(o[50],4),round(o[950],4))}
lags.sort()
res['big_btc']=nbig; res['big_match_ws']=nmatch
res['lag_onchain_ms_(ts_est-recvWS)']={q:round(lags[int(q*len(lags))]) for q in (0.1,0.5,0.9)} if lags else None
res['hermanos']={'|'.join(k):mstat(v) for k,v in ev2.items()}
json.dump(res,open(f'{S}/re_{D}.json','w'),indent=1,default=str)
print(json.dumps(res,indent=1,default=str))
