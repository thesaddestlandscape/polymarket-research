import sys, gzip, csv, math, datetime, random
import numpy as np
from array import array
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/escalera_patas_28oct')
import escalera as E
E.D=(0.02,0.05,0.10,0.20,0.30,0.45)
REG=E.REG; OUT='/root/polymarket-research/experimentos/5m_barato/entradas_bajo_010_28oct/outD/d_%s.csv'
G=E.G; fee=E.fee; LX=150.0; LT=250.0; EPS=1e-9
LV=[round(0.01*i,2) for i in range(1,10)]; SS=(30,120,210)
class Tok:
    def __init__(s,cie): s.qt=array('i'); s.qb=array('h'); s.qa_=array('h'); s.qs=array('f'); s.p=array('d'); s.cie=cie*1000
def prep(t):
    n=len(t.qt)
    if n:
        tt=np.frombuffer(t.qt,dtype=np.int32).astype(np.float64)+t.cie
        bb=np.frombuffer(t.qb,dtype=np.int16).astype(np.float64); ba=np.frombuffer(t.qa_,dtype=np.int16).astype(np.float64)
        bb=np.where(bb<0,np.nan,bb/10000.0); ba=np.where(ba<0,np.nan,ba/10000.0)
        t.qa=np.stack([tt,bb,ba,np.frombuffer(t.qs,dtype=np.float32).astype(np.float64)],axis=1)
        if not np.all(np.diff(tt)>=0): t.qa=t.qa[np.argsort(tt,kind='stable')]
    else: t.qa=np.zeros((0,4))
    t.pa=np.frombuffer(t.p,dtype=float).reshape(-1,4) if len(t.p) else np.zeros((0,4))
    t.pa=t.pa[np.argsort(t.pa[:,0],kind='stable')]
    t.pa=np.frombuffer(t.p,dtype=float).reshape(-1,4) if len(t.p) else np.zeros((0,4))
    t.pa=t.pa[np.argsort(t.pa[:,0],kind='stable')]
cache={}
def eqprints(A,B):  # compras equivalentes de A (para ventas) cacheado
    k=(id(A),id(B))
    if k in cache: return cache[k]
    ta=A.pa; tb=B.pa; m1=ta[:,2]==1; m2=tb[:,2]==0
    t=np.concatenate([ta[m1,0],tb[m2,0]]); p=np.concatenate([ta[m1,1],1-tb[m2,1]])
    o=np.argsort(t,kind='stable'); cache[k]=(t[o],p[o]); return cache[k]
E.eqprints=eqprints
def eqsell(A,B):  # ventas equivalentes sobre A: SELL A a p ; BUY B a pb -> 1-pb ; con tamano
    ta=A.pa; tb=B.pa; m1=ta[:,2]==0; m2=tb[:,2]==1
    t=np.concatenate([ta[m1,0],tb[m2,0]]); p=np.concatenate([ta[m1,1],1-tb[m2,1]]); s=np.concatenate([ta[m1,3],tb[m2,3]])
    o=np.argsort(t,kind='stable'); return t[o],p[o],s[o]
def qrow(t,tau):
    a=t.qa[:,0]; i=np.searchsorted(a,tau,side='right')-1
    if i<0 or tau-a[i]>30000: return None
    return t.qa[i]
def dumpD(A,sh,win,cost,reb,L,tfill,B):
    tdump=A.cie-30000; tau=tdump+LT; hold=sh*win
    a=A.qa[:,0]; i=np.searchsorted(a,tau,side='right')-1
    st='ok'; dv=None; bs0=float('nan'); bd=float('nan')
    if i<0 or tau-a[i]>2000: st='stale'
    else:
        bb,ba,bs=A.qa[i,1],A.qa[i,2],A.qa[i,3]; bs0=bs; bd=bb
        if bb!=bb or bb<=0: st='nobid'
        elif ba==ba and bb>=ba-1e-9: st='crossed'
        elif bs!=bs or bs<=0: st='nodepth'
        else:
            q=min(sh,bs); dv=q*bb-q*fee(bb)+(sh-q)*win
            if bs<sh: st='partial'
    dump=dv if dv is not None else hold
    g=E.c2(L+0.45); te,pe=eqprints(A,B)
    if g>0.99+1e-9: s5=float('nan')
    else:
        tf=E.first(te,pe,tfill+E.LX,g,True); sale=sh*g+0.2*sh*fee(g)
        s5=(sale if (tf is not None and tf<=tdump) else dump)-cost+reb
    return dump-cost+reb,s5,st,bs0,bd
def main(day):
    toks={}; byk={}; coin={}
    with gzip.open(REG%day,'rt') as f:
        next(f)
        for ln in f:
            ty=ln[0]
            if ty=='k':
                c=ln.rstrip('\n').split(',')
                if c[4]=='5min' and G.get(c[5]) in ('YES','NO') and c[7] in ('YES','NO'):
                    toks[c[2]]=Tok(datetime.datetime.fromisoformat(c[6]).timestamp()); byk[(c[5],c[7])]=c[2]; coin[c[5]]=c[3]
            elif ty=='q' or ty=='t':
                c0=ln.split(',',3); t=toks.get(c0[2])
                if t is None: continue
                c=ln.rstrip('\n').split(',')
                if ty=='q':
                    rv=c[7].strip(); tm=float(rv) if rv else float(c[1])
                    try:
                        bb=float(c[3]) if c[3].strip() not in('','None') else float('nan'); ba=float(c[4]) if c[4].strip() not in('','None') else float('nan')
                        bs=float(c[5]) if c[5].strip() not in('','None') else float('nan')
                    except: continue
                    if bb==bb and ba==ba and bb>ba+EPS: continue
                    if t.cie-320000<=tm<=t.cie+10000:
                        t.qt.append(int(tm-t.cie)); t.qb.append(-1 if bb!=bb else int(round(bb*10000))); t.qa_.append(-1 if ba!=ba else int(round(ba*10000))); t.qs.append(bs)
                else:
                    rv=c[6].strip(); tm=float(rv) if rv else float(c[1])
                    if t.cie-320000<=tm<=t.cie+10000: t.p.extend((tm,float(c[3]),1.0 if c[4]=='BUY' else 0.0,float(c[5])))
    for t in toks.values(): t.pa=None
    rows=[]; rng=random.Random(2811)
    cols=['kind','dia','coin','mercado','lado','L','s','sh','win','cost','pnl_hold','pnl_oldD','pnl_oldS5D','pnl_newD','pnl_newS5D','dstat','bs','bd']
    mk=sorted({m for (m,s) in byk})
    for m in mk:
        w=G[m]
        for side in ('YES','NO'):
            oth='NO' if side=='YES' else 'YES'
            A=toks.get(byk.get((m,side))); B=toks.get(byk.get((m,oth)))
            if A is None or B is None: continue
            prep(A); prep(B); cache.clear()
            cie=A.cie/1000.0; win=1.0 if w==side else 0.0
            ts,ps,ss=eqsell(A,B); tend=A.cie-2000
            cum=np.cumsum(ss) if len(ss) else ss
            for s in SS:
                tp=(cie-300+s)*1000; q=qrow(A,tp)
                if q is None: continue
                bb,ask,bs=q[1],q[2],q[3]
                if ask!=ask: continue
                i0=np.searchsorted(ts,tp+LX,side='left')
                for L in LV:
                    if ask<L+0.01-1e-9: continue
                    sh=float(max(5,math.ceil(1.0/L-1e-9))); cost=sh*L; reb=0.2*sh*fee(L)
                    hyp=sh*win-cost+reb
                    tfill=None
                    if i0<len(ts):
                        mk_=ps[i0:]<L-EPS
                        j=np.argmax(mk_)
                        if mk_[j] and ts[i0+j]<=tend: tfill=ts[i0+j]
                    touch=0
                    if tfill is not None: touch=1
                    elif i0<len(ts):
                        if bb==bb and abs(L-bb)<1e-6: qa=bs if bs==bs else None
                        elif bb==bb and L>bb+1e-6: qa=0.0
                        elif bb!=bb: qa=0.0   # sin bid visible: delante 0
                        else: qa=None
                        if qa is not None:
                            sel=ps[i0:]<=L+EPS
                            if sel.any():
                                cs=np.cumsum(np.where(sel,ss[i0:],0.0)); jj=np.argmax(cs>=qa+sh)
                                if cs[jj]>=qa+sh and ts[i0+jj]<=tend: touch=1
                    base=dict(kind='real',dia=day,coin=coin[m],mercado=m,lado=side,L=L,s=s,sh=sh,win=win,ask0=ask,bb0=bb,bs0=bs,
                              filled=0 if tfill is None else 1,tfill='' if tfill is None else tfill,touch=touch,hold_hyp=hyp)
                    if tfill is not None:
                        row=dict(base,pnl_hold=hyp,cost=cost)
                        E.evalleg(A,B,cie,tfill,L,sh,win,cost,reb,'real',row)
                        nd_,n5_,st_,bs_,bd_=dumpD(A,sh,win,cost,reb,L,tfill,B)
                        rows.append(dict(kind='real',dia=day,coin=coin[m],mercado=m,lado=side,L=L,s=s,sh=sh,win=win,cost=cost,pnl_hold=hyp,pnl_oldD=row['pnl_base_D'],pnl_oldS5D=row['pnl_s5_D'],pnl_newD=nd_,pnl_newS5D=n5_,dstat=st_,bs=bs_,bd=bd_))
                        ak=E.quote(B,tfill+LT,2)
                        if False:
                            c=sh*ak+sh*fee(ak); r2=dict(base,kind='inv',L=ak,cost=c,win=1.0-win,pnl_hold=sh*(1-win)-c)
                            E.evalleg(B,A,cie,tfill+LT,ak,sh,1.0-win,c,0,'inv',r2); rows.append(r2)
                    else: pass
            # placebo
            for _ in range(0):
                tau=(cie-rng.uniform(10,290))*1000
                ak=E.quote(A,tau+LT,2)
                if ak is not None and 0.01<=ak<0.10:
                    sh=float(max(5,math.ceil(1.0/ak-1e-9))); c=sh*ak+sh*fee(ak)
                    row=dict(kind='pla',dia=day,coin=coin[m],mercado=m,lado=side,L=ak,s=-1,sh=sh,win=win,filled=1,cost=c,pnl_hold=sh*win-c)
                    E.evalleg(A,B,cie,tau+LT,ak,sh,win,c,0,'pla',row); rows.append(row)
    with open(OUT%day,'w',newline='') as f:
        wr=csv.DictWriter(f,cols,extrasaction='ignore'); wr.writeheader()
        for r in rows:
            if r['kind']=='real': wr.writerow({k:r.get(k,'') for k in cols})
    print(day,'mercados',len(mk),'filas',len(rows),'rellenos',sum(1 for r in rows if r['kind']=='real' and r['filled']==1),flush=True)
if __name__=='__main__': main(sys.argv[1])
