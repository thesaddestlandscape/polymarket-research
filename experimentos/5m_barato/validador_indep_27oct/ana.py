import gzip, csv, pickle, json, random, bisect, sys
from collections import defaultdict
from array import array
EXP='/root/polymarket-research/experimentos/5m_barato/'
VPV='/root/polymarket-research-datalogs/vida_puja_virtual/vpv_%s.csv.gz'
G=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
res=pickle.load(open(sys.argv[1],'rb'))
SYM={'BTC':'BTCUSDT','ETH':'ETHUSDT','SOL':'SOLUSDT','XRP':'XRPUSDT','DOGE':'DOGEUSDT','BNB':'BNBUSDT'}
def rd(p):
    with gzip.open(p,'rt') as f: return list(csv.DictReader(f))
def gana(m,lado):
    w=G.get(str(m))
    if w not in ('YES','NO'): return None
    return 1 if w==lado else 0
def ev(U):  # U: list of (dia,cierre,pnl,coste)
    P=sum(u[2] for u in U); C=sum(u[3] for u in U); return P/C if C else float('nan')
def boot(U,key=1,B=2000,seed=97):
    g=defaultdict(lambda:[0.0,0.0])
    for u in U: g[u[key]][0]+=u[2]; g[u[key]][1]+=u[3]
    L=list(g.values()); r=random.Random(seed); out=[]
    for _ in range(B):
        P=C=0.0
        for _ in range(len(L)):
            a=L[r.randrange(len(L))]; P+=a[0]; C+=a[1]
        out.append(P/C)
    out.sort(); return out[int(.05*B)],out[int(.95*B)-1],len(L)
def rep(lab,U,dias=True):
    if not U: print(lab,'n=0'); return
    lo,hi,nc=boot(U); s='%-34s n=%5d cierres=%4d coste=%8.1f EVw=%+.4f IC90c=(%+.3f,%+.3f)'%(lab,len(U),nc,sum(u[3] for u in U),ev(U),lo,hi)
    if dias:
        byd=defaultdict(list)
        for u in U: byd[u[0]].append(u)
        dv={d:ev(v) for d,v in sorted(byd.items())}
        s+=' | '+' '.join('%s:%+.3f'%(d[-2:],v) for d,v in dv.items())
        if len(dv)>=3:
            top=sorted(dv,key=dv.get)[-2:]; R=[u for u in U if u[0] not in top]
            lo2,hi2,_=boot(R); s+=' | sin2mejores=%+.4f (%+.3f,%+.3f) dias>0=%d/%d'%(ev(R),lo2,hi2,sum(v>0 for v in dv.values()),len(dv))
            ld,hd,_=boot(U,key=0); s+=' IC90dias=(%+.3f,%+.3f)'%(ld,hd)
    print(s,flush=True)
# ---------- Binance: tiempos de salto adverso (ret 300 ms >=2 bps) ----------
def saltos(xd,k=2.0,W=300.0,shift=0.0):
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
            if r<=-k: dn.append(tr[i]+shift)
            elif r>=k: up.append(tr[i]+shift)
        out[s]=(dn,up)
    return out
def first_adv(S,coin,lado,a,b):
    s=SYM.get(coin)
    if s is None or s not in S: return None
    arr=S[s][0] if lado=='YES' else S[s][1]
    i=bisect.bisect_left(arr,a)
    if i<len(arr) and arr[i]<=b: return arr[i]
    return None
DAYS=['2026-10-24','2026-10-25','2026-10-26']
SJ={D:saltos(res['x_'+D]) for D in DAYS}
print('saltos',{D:{s:(len(v[0]),len(v[1])) for s,v in SJ[D].items()} for D in DAYS},flush=True)
# ================= (1) E-TD sobre vpv =================
print('\n===== E-TD (vpv 24-26, k=2 W=300 Lc=100)')
for modo in ('pes','opt'):
    ret=defaultdict(list); apa=defaultdict(list); noapa=defaultdict(list); todas=defaultdict(list); ncanc=nv=0
    for D in DAYS:
        S=SJ[D]
        for r in rd(VPV%D):
            g=gana(r['mercado'],r['lado'])
            if g is None or SYM.get(r['coin']) is None: continue
            nv+=1
            b=float(r['b']); t0=float(r['t0_recv_ms']); fill=r['relleno_'+modo]=='1'
            tf=float(r['t_relleno_%s_ms'%modo]) if fill else None
            # cancelacion primaria: primer salto adverso en [t0, tf-100] (vidas sin relleno: hasta fin, solo para frecuencia)
            if fill: c=first_adv(S,r['coin'],r['lado'],t0,tf-100)
            else: c=first_adv(S,r['coin'],r['lado'],t0,t0+60000)
            if c is not None: ncanc+=1
            if not fill: continue
            key=(D,r['mercado'],r['lado']); u=(tf,(D,int(r['cierre']),5*(g-b),5*b))
            todas[key].append(u)
            if c is None: ret[key].append(u)
            j=first_adv(S,r['coin'],r['lado'],tf-2000,tf-100)
            (apa if j is not None else noapa)[key].append(u)
    def unit(dd): return [min(v)[1] for v in dd.values()]
    print(modo,'vidas',nv,'frac vidas con salto adverso (primaria)',round(ncanc/nv,3))
    for lab,dd in (('todas',todas),('RETENIDOS primaria',ret),('apartados justa',apa),('no apartados',noapa)):
        U=unit(dd)
        for sub,f in (('TODO',lambda d:True),('DESC24+25',lambda d:d!='2026-10-26'),('OOS26',lambda d:d=='2026-10-26')):
            rep('%s %s %s'%(modo,lab,sub),[u for u in U if f(u[0])],dias=(sub=='TODO'))
    # diferencia apartados - no apartados (bootstrap conjunto por cierre)
    A=unit(apa); N=unit(noapa)
    gA=defaultdict(lambda:[0,0]); gN=defaultdict(lambda:[0,0])
    for u in A: gA[u[1]][0]+=u[2]; gA[u[1]][1]+=u[3]
    for u in N: gN[u[1]][0]+=u[2]; gN[u[1]][1]+=u[3]
    cs=list(set(gA)|set(gN)); r_=random.Random(5); out=[]
    for _ in range(2000):
        pa=ca=pn=cn=0.0
        for _ in range(len(cs)):
            c=cs[r_.randrange(len(cs))]
            a=gA.get(c); n=gN.get(c)
            if a: pa+=a[0]; ca+=a[1]
            if n: pn+=n[0]; cn+=n[1]
        if ca and cn: out.append(pa/ca-pn/cn)
    out.sort(); print('  %s DIF apartados-no_apartados TODO = %+.4f IC90c=(%+.3f,%+.3f)'%(modo,ev(A)-ev(N),out[int(.05*len(out))],out[int(.95*len(out))-1]))
# ================= (2) FRENTE-TD =================
print('\n===== FRENTE-TD (fr 24-26) y FRENTE-FAV-TD')
for nombre,base in (('FRENTE',EXP+'re_as_b_frente/fr_%s.csv.gz'),('FAV',EXP+'re_as_b_frente/fav/fr_%s.csv.gz')):
  for td in (True,False):
    best={}; nviv=nrej=0
    for D in DAYS:
        S=SJ[D]
        for r in rd(base%D):
            g=gana(r['mercado'],r['lado'])
            if g is None: continue
            bb=float(r['bb']); ba=float(r['ba']); bp=round(bb+0.01,2)
            if ba-bb<0.02-1e-9: continue
            nviv+=1
            if r['ba85']=='' or float(r['ba85'])<=bp+1e-9: nrej+=1; continue
            t0=float(r['t0']); fin=float(r['fin'])
            cut=fin
            if td:
                c=first_adv(S,r['coin'],r['lado'],t0,fin)
                if c is not None: cut=min(cut,c+100-1e-6)
            acc=0.0; tfirst=None
            for pr in (r['prints'] or '').split(';'):
                if not pr: continue
                t,sz,_=pr.split(':'); t=float(t); sz=float(sz)
                if t<t0+85 or t>fin or t>=cut and td: continue
                if tfirst is None: tfirst=t
                acc=min(5.0,acc+sz)
                if acc>=5: break
            if tfirst is None: continue
            key=(D,r['mercado'],r['lado']); cand=(tfirst,t0,(D,int(r['cierre']),acc*(g-bp),acc*bp))
            if key not in best or cand[:2]<best[key][:2]: best[key]=cand
    U=[v[2] for v in best.values()]
    print(nombre,'TD' if td else 'sinTD','vidas colocables',nviv,'rechazadas',nrej)
    rep('%s %s TODO'%(nombre,'TD' if td else 'sinTD'),U)
    rep('  DESC24+25',[u for u in U if u[0]!='2026-10-26'],dias=False); rep('  OOS26',[u for u in U if u[0]=='2026-10-26'],dias=False)
# ================= (3) SEGFAV =================
print('\n===== SEGFAV desde sf_D (agregacion propia)')
DS=['2026-10-%02d'%d for d in range(19,27)]
S_=[];P_=[]
for D in DS:
    for r in rd(EXP+'re_as_b_segfav/sf_%s.csv.gz'%D):
        if r['askF250']=='': continue
        a=float(r['askF250']); s=float(r['asF250'] or 0); age=float(r['ageF250'] or 1e9)
        if not(s>=5 and age<=30000 and 0<a<1): continue
        g=gana(r['mercado'],r['lado'])
        if g is None: continue
        T=float(r['T_s']); tb=int(r['tb'])
        cost=5*a+5*0.07*a*(1-a); u=(D,int(r['cierre']),5*g-cost,cost,r['coin'],tb,a,r['mercado'],r['lado'])
        if r['tipo']=='S' and tb in (20,60,120): S_.append(u)
        if r['tipo']=='P' and tb in (20,60,120): P_.append(u)
rep('S primaria TODO 19-26',S_); rep('  DESC 19-25',[u for u in S_ if u[0]!='2026-10-26'],dias=False); rep('  OOS 26',[u for u in S_ if u[0]=='2026-10-26'],dias=False)
rep('PLACEBO T<180',P_)
def cell(u): return (u[4],u[5],int(u[6]*20))
def delta(S,P):
    cs=defaultdict(float); pp=defaultdict(lambda:[0,0])
    for u in S: cs[cell(u)]+=u[3]
    for u in P: pp[cell(u)][0]+=u[2]; pp[cell(u)][1]+=u[3]
    num=den=0
    for c,w in cs.items():
        if pp[c][1]>0: num+=w*pp[c][0]/pp[c][1]; den+=w
    Sc=[u for u in S if pp[cell(u)][1]>0]
    return ev(Sc)-num/den, num/den
d0,pr=delta(S_,P_)
byc=defaultdict(lambda:([],[]))
for u in S_: byc[u[1]][0].append(u)
for u in P_: byc[u[1]][1].append(u)
cl=list(byc); r_=random.Random(11); out=[]
for _ in range(500):
    SS=[];PP=[]
    for _ in range(len(cl)):
        a,b=byc[cl[r_.randrange(len(cl))]]; SS+=a; PP+=b
    out.append(delta(SS,PP)[0])
out.sort(); print('DELTA S-P estratificado moneda x Tb x ask0,05 = %+.4f (placebo reponderado %+.4f) IC90c(500)=(%+.4f,%+.4f)'%(d0,pr,out[25],out[474]))
# ---- extraccion propia 26-Oct ----
print('\n===== SEGFAV 26-Oct extraccion PROPIA desde m5_registro crudo')
mine=[];mineP=[];cmp_=[]
sf26={(r['tipo'],r['mercado'],r['lado'],int(r['tb'])):r for r in rd(EXP+'re_as_b_segfav/sf_2026-10-26.csv.gz')}
for u in res['units26']:
    if u['tb'] not in (20,60,120): continue
    sn=u['snap']
    if sn is None: continue
    rcv,a,s=sn; age=u['td']+250-rcv
    ok= s>=5 and age<=30000 and 0<a<1
    o=sf26.get((u['tipo'],u['m'],u['lado'],u['tb']))
    cmp_.append((u['tipo'],o is not None, o is not None and o['askF250']!='' and abs(float(o['askF250'])-a)<1e-9, o is not None and abs(float(o['td'])-u['td'])<1))
    if not ok: continue
    g=gana(u['m'],u['lado'])
    if g is None: continue
    cost=5*a+5*0.07*a*(1-a); x=('2026-10-26',u['cie'],5*g-cost,cost)
    (mine if u['tipo']=='S' else mineP).append(x)
rep('S propia OOS26',mine,dias=False); rep('P propia OOS26',mineP,dias=False)
for t in 'SP':
    c=[x for x in cmp_ if x[0]==t]
    print(t,'unidades propias',len(c),'en sf',sum(x[1] for x in c),'mismo td',sum(x[3] for x in c),'mismo askF250',sum(x[2] for x in c), 'sf tiene',sum(1 for k in sf26 if k[0]==t and k[3] in (20,60,120)))
print('ONCHAIN',res['onchain'])
