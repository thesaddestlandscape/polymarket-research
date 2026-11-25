# Q4 fantasma (PREREG_Q4.md). Solo lectura. Uso: nice -n 19 ionice -c3 python3 q4.py
import gzip, csv, json, bisect, random, subprocess, os, sys
from array import array
from collections import defaultdict
EXP='/root/polymarket-research/experimentos/5m_barato/'
REG='/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
ONC='/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz'
KEEP27='/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_2026-10-27_parcial_1434Z.csv.gz'
OUT=EXP+'q4_fantasma_27oct/'
G=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
SYM={'BTC':'BTCUSDT','ETH':'ETHUSDT','SOL':'SOLUSDT','XRP':'XRPUSDT','DOGE':'DOGEUSDT','BNB':'BNBUSDT'}
DAYS=['2026-10-24','2026-10-25','2026-10-26']
NEXT={'2026-10-24':ONC%'2026-10-25','2026-10-25':ONC%'2026-10-26','2026-10-26':KEEP27}
LP=85
def gana(m,lado):
    w=G.get(str(m)); 
    return None if w not in ('YES','NO') else (1 if w==lado else 0)
def ev(U):
    P=sum(u[2] for u in U); C=sum(u[3] for u in U); return P/C if C else float('nan')
def boot(U,key=1,B=2000,seed=2711):
    g=defaultdict(lambda:[0.0,0.0])
    for u in U: g[u[key]][0]+=u[2]; g[u[key]][1]+=u[3]
    L=list(g.values()); r=random.Random(seed); out=[]
    if not L: return float('nan'),float('nan'),0
    for _ in range(B):
        P=C=0.0
        for _ in range(len(L)):
            a=L[r.randrange(len(L))]; P+=a[0]; C+=a[1]
        out.append(P/C if C else 0.0)
    out.sort(); return out[int(.05*B)],out[int(.95*B)-1],len(L)
def rep(lab,U,dias=True):
    if not U: print('%-44s n=0'%lab); return
    lo,hi,nc=boot(U); s='%-44s n=%5d cierres=%4d coste=%8.1f EVw=%+.4f IC90c=(%+.3f,%+.3f)'%(lab,len(U),nc,sum(u[3] for u in U),ev(U),lo,hi)
    if dias:
        byd=defaultdict(list)
        for u in U: byd[u[0]].append(u)
        dv={d:ev(v) for d,v in sorted(byd.items())}
        s+=' | '+' '.join('%s:%+.3f(n%d)'%(d[-2:],v,len(byd[d])) for d,v in dv.items())
        if len(dv)>=3:
            top=sorted(dv,key=dv.get)[-2:]; R=[u for u in U if u[0] not in top]
            if R: s+=' | sin2mejoresdias=%+.4f'%ev(R)
    print(s,flush=True)
def saltos(xd,k=2.0,W=300.0):
    out={}
    for s,(tr,pr) in xd.items():
        idx=sorted(range(len(tr)),key=tr.__getitem__) if any(tr[i]>tr[i+1] for i in range(len(tr)-1)) else None
        if idx: tr=array('d',(tr[i] for i in idx)); pr=array('d',(pr[i] for i in idx))
        dn=array('d'); up=array('d'); j=-1; n=len(tr)
        for i in range(n):
            if i+1<n and tr[i+1]==tr[i]: continue
            lim=tr[i]-W
            while j+1<n and tr[j+1]<=lim: j+=1
            if j<0: continue
            r=(pr[i]/pr[j]-1)*1e4
            if r<=-k: dn.append(tr[i])
            elif r>=k: up.append(tr[i])
        out[s]=(dn,up)
    return out
def first_adv(S,coin,lado,a,b):
    s=SYM.get(coin)
    if s is None or s not in S: return None
    arr=S[s][0] if lado=='YES' else S[s][1]
    i=bisect.bisect_left(arr,a)
    return arr[i] if i<len(arr) and arr[i]<=b else None
def rd(p):
    with gzip.open(p,'rt') as f: return list(csv.DictReader(f))
def load_day(D):
    K={}; tok_ml={}; T={}; xs=defaultdict(lambda:(array('d'),array('d')))
    p=subprocess.Popen("zcat %s | grep -E '^(t|k|x),'"%(REG%D),shell=True,stdout=subprocess.PIPE,text=True)
    for ln in p.stdout:
        c=ln.rstrip('\n').split(',')
        if c[0]=='k':
            tok_ml[(c[5],c[7])]=c[2]; K[c[2]]=(c[3],c[4],c[5],c[7])
        elif c[0]=='t':
            T.setdefault((c[2],int(c[6]),round(float(c[5]),4)),[]).append((int(c[1]),float(c[3]),c[4]))
        elif c[0]=='x' and c[2] in SYM.values():
            a=xs[c[2]]; a[0].append(float(c[7])); a[1].append(float(c[3]))
    return K,tok_ml,T,dict(xs)
def load_onchain(D,toks):
    idx=defaultdict(list)
    for path in (ONC%D,NEXT[D]):
        if not os.path.exists(path): continue
        p=subprocess.Popen("zcat %s"%path,shell=True,stdout=subprocess.PIPE,text=True)
        for ln in p.stdout:
            if not ln.startswith('F,'): continue
            c=ln.split(',')
            tk=c[9]
            if tk not in toks: continue
            side=c[8]; ma=float(c[10]); ta=float(c[11])
            sh,us=(ta,ma) if side=='0' else (ma,ta)
            if sh<=0: continue
            idx[(tk,int(round(sh*1e4)))].append((float(c[2])*1000,us/sh,c[3]))
    return idx
def match(idx,tk,e,recv,price,size):
    cands=idx.get((tk,int(round(size*1e4))))
    if not cands: return 'none',None
    lo=e-2000; hi=recv+15000; tx={}
    for ts,p,t in cands:
        if lo<=ts<=hi and abs(p-price)<=0.006: tx[t]=ts
    if not tx: return 'none',None
    if len(tx)>1: return 'amb',list(tx.values())
    return 'ok',next(iter(tx.values()))
rec=[]; NZ={}   # registros por unidad baseline y resim
pr_out=gzip.open(OUT+'prints_vidas.csv.gz','wt'); pr_out.write('dia,mercado,lado,tipo,t0,recv,dt,size,t_exch,estado_chain,ts_chain,casado_est,FX,FC\n')
UB=[]; UR=[]; cov=defaultdict(int); noise={}
for D in DAYS:
    K,tok_ml,T,xs=load_day(D)
    toks={k for k,v in K.items() if v[1]=='5min'}
    idx=load_onchain(D,toks)
    SJ=saltos(xs)
    print(D,'k',len(K),'t keys',len(T),'onchain keys',len(idx),flush=True)
    # calibracion OFF con prints frescos casados
    d=[]
    for (tk,recv,sz),L in T.items():
        if tk not in toks: continue
        for (e,pc,sd) in L:
            if recv-e<=200:
                st,ts=match(idx,tk,e,recv,pc,sz)
                if st=='ok': d.append(ts-e)
    d.sort(); NZ[D]=d[:]; n=len(d); q=lambda f:d[int(f*(n-1))] if n else float('nan')
    OFF=q(.5); noise[D]=(n,q(.05),q(.25),q(.5),q(.75),q(.95)); print(D,'frescos casados n=%d p5=%.0f p25=%.0f p50=%.0f p75=%.0f p95=%.0f IQR=%.0f ms'%(n,q(.05),q(.25),q(.5),q(.75),q(.95),q(.75)-q(.25)),flush=True)
    nrej=0
    for r in rd(EXP+'re_as_b_frente/fr_%s.csv.gz'%D):
        g=gana(r['mercado'],r['lado'])
        if g is None: continue
        bb=float(r['bb']); ba=float(r['ba']); bp=round(bb+0.01,2)
        if ba-bb<0.02-1e-9: continue
        if r['ba85']=='' or float(r['ba85'])<=bp+1e-9: continue
        t0=float(r['t0']); fin=float(r['fin'])
        c=first_adv(SJ,r['coin'],r['lado'],t0,fin); cut=fin if c is None else min(fin,c+100-1e-6)
        fd=(r['bb85']!='' and float(r['bb85'])>=bp-1e-9)
        comp='NO' if r['lado']=='YES' else 'YES'
        plist=[]
        for pr in (r['prints'] or '').split(';'):
            if not pr: continue
            t,sz,ty=pr.split(':'); t=float(t); sz=float(sz)
            if t<t0+LP or t>fin or t>=cut: continue
            tk=tok_ml.get((r['mercado'],r['lado'] if ty=='A' else comp))
            info=dict(t=t,sz=sz,ty=ty,e=None,fx=None,fc=None,st='sin_fila_t',cas=None)
            if tk:
                L=T.get((tk,int(t),round(sz,4)))
                if L:
                    e,pc,sd=L[0]; info['e']=e; info['fx']=e<t0+LP
                    st,ts=match(idx,tk,e,t,pc,sz); info['st']=st
                    if st=='amb': info['cands']=ts
                    if st=='ok': info['cas']=ts-OFF; info['fc']=(ts-OFF)<t0+LP
            plist.append(info)
            pr_out.write('%s,%s,%s,%s,%d,%d,%d,%g,%s,%s,%s,%s,%s,%s\n'%(D,r['mercado'],r['lado'],ty,t0,t,t-t0,sz,info['e'],info['st'],'' if info['cas'] is None else int(info['cas']+OFF),'' if info['cas'] is None else int(info['cas']),info['fx'],info['fc']))
        def sim(drop):
            acc=0.0; first=None
            for i in plist:
                if drop(i): continue
                if first is None: first=i
                acc=min(5.0,acc+i['sz'])
                if acc>=5: break
            return first,acc
        key=(D,r['mercado'],r['lado'])
        f,acc=sim(lambda i:False)
        if f is not None:
            u=(D,int(r['cierre']),acc*(g-bp),acc*bp); dt=f['t']-t0
            row=dict(key=key,t0=t0,u=u,dt=dt,e=f['e'],recv=f['t'],cas=f['cas'],cands=f.get('cands'),coin=r['coin'],OFF=OFF,fx=bool(f['fx']),fc=bool(f['fc']),st=f['st'],fd=fd,both=bool(f['fx'] and f['fc']))
            row['prim']=row['fx'] or row['fc']; UB.append(row)
        f2,acc2=sim(lambda i:bool(i['fx'] or i['fc']))
        if f2 is not None: UR.append(dict(key=key,t0=t0,u=(D,int(r['cierre']),acc2*(g-bp),acc2*bp),dt=f2['t']-t0))
    print(D,'listo',flush=True)
pr_out.close()
def best(L):
    b={}
    for x in L:
        k=x['key']; c=((x['dt']+x['t0']),x['t0'])
        if k not in b or c<b[k][0]: b[k]=(c,x)
    return [v[1] for v in b.values()]
UB=best(UB); UR=best(UR)
import pickle; pickle.dump({'UB':UB,'NZ':{k:v[::3] for k,v in NZ.items()}},open(OUT+'q4_unidades.pkl','wb'))
TR=[('<1 s',0,1000),('1-5 s',1000,5000),('5-20 s',5000,20000),('>=20 s',20000,1e12)]
def tr(x,a,b): return a<=x['dt']<b
print('\n===== RUIDO RELOJ ON-CHAIN (ts_chain - t_exch, prints frescos casados):'); 
for D,v in noise.items(): print(D,'n=%d p5=%.0f p25=%.0f p50=%.0f p75=%.0f p95=%.0f IQR=%.0f'%(v[0],v[1],v[2],v[3],v[4],v[5],v[4]-v[2]))
print('\n===== FRACCION FANTASMA POR TRAMO (unidades; entre parentesis por EUR de coste)')
print('%-8s %6s %6s %6s %6s %6s %6s %6s %6s %6s'%('tramo','n','okchn','amb','none','sinT','FX','FC','FXyFC','PRIM'),'  FD  PRIM|FD')
for nm,a,b in TR:
    S=[x for x in UB if tr(x,a,b)]; n=len(S)
    if not n: print(nm,'n=0'); continue
    C=sum(x['u'][3] for x in S)
    f=lambda fn:'%d/%.0f%%/%.0f%%'%(sum(fn(x) for x in S),100*sum(fn(x) for x in S)/n,100*sum(x['u'][3] for x in S if fn(x))/C)
    cnt=lambda s:sum(x['st']==s for x in S)
    print('%-8s %6d %6d %6d %6d %6d  FX %s | FC %s | FXyFC %s | PRIM %s | FD %s | PRIM|FD %s'%(nm,n,cnt('ok'),cnt('amb'),cnt('none'),cnt('sin_fila_t'),f(lambda x:x['fx']),f(lambda x:x['fc']),f(lambda x:x['both']),f(lambda x:x['prim']),f(lambda x:x['fd']),f(lambda x:x['prim'] or x['fd'])))
print('\n===== EVw (1 obs por mercado-lado; IC90 por cierre) =====')
rep('TODO baseline (control vs -0,217)',[x['u'] for x in UB])
for nm,a,b in TR:
    S=[x for x in UB if tr(x,a,b)]
    rep('ANTES   '+nm,[x['u'] for x in S])
    rep('  sin PRIM (FX|FC)  '+nm,[x['u'] for x in S if not x['prim']])
    rep('  sin FXyFC         '+nm,[x['u'] for x in S if not x['both']])
    rep('  sin PRIM|FD       '+nm,[x['u'] for x in S if not (x['prim'] or x['fd'])])
    rep('  solo PRIM (los fantasma) '+nm,[x['u'] for x in S if x['prim']],dias=False)
print('\n===== RE-SIMULACION quitando prints fantasma (FX|FC) de cada vida; unidad re-asignada al siguiente print')
rep('TODO re-sim',[x['u'] for x in UR])
for nm,a,b in TR:
    rep('RESIM '+nm,[x['u'] for x in UR if tr(x,a,b)])
