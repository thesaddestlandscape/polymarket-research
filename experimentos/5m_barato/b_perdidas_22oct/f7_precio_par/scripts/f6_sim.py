#!/usr/bin/env python3
"""f6 (F7 precio del par): sim v2 + tope de precio de la 2a pata. ORIGEN r12. sim v2 (PREREG_V2.md) + fills reales de la muestra con markout 30 s y clasificacion pata suelta/emparejada. Uso: r12_v2.py DIA VARIANTES(A,B)
DIA en construccion (20,21,22): c_*.gz + tok_order.json ; en evaluacion (18,19,23): cev_*.gz/bev_* + tok_order_ev.json."""
import gzip,json,glob,sys,collections,heapq,numpy as np,pandas as pd
DL='/root/polymarket-research-datalogs/'; R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; RG=R+'rebate_ganadores/'; OUTD=R+'f7_precio_par/datos/'
DAY=sys.argv[1]; VARS=sys.argv[2].split(','); LIM=int(sys.argv[3]) if len(sys.argv)>3 else 0  # LIM>0: smoke test, no escribe
EVAL=DAY in ('2026-10-18','2026-10-19','2026-10-23')
if EVAL: TOK=json.load(open(DL+'rebate_ganadores_btc/toks_ev.json')); TO=json.load(open(DL+'rebate_ganadores_btc/tok_order_ev.json')); CF=DL+'rebate_ganadores_btc/cev_*.gz'; BF=DL+'rebate_ganadores_btc/bev_*.txt'
else: TOK=json.load(open(DL+'rebate_ganadores_btc/toks_sub.json')); TO=json.load(open(DL+'rebate_ganadores_btc/tok_order.json')); CF=DL+'rebate_ganadores_btc/c_*.gz'; BF=DL+'rebate_ganadores_btc/b_*.txt'
DES=json.load(open(DL+'maker_ms_desenlaces_cache.json')); DES.update(json.load(open(DL+'rebate_ganadores_btc/des_23.json')))
dayof=lambda tok: pd.Timestamp(TOK[tok][3],unit='s',tz='UTC').strftime('%Y-%m-%d')
IXD={i for i,t in enumerate(TO) if dayof(t)==DAY}
parts=[]
LISTO=set(l.split()[1] for l in open(DL+'rebate_ganadores_btc/progreso_ev.txt')) if EVAL else None
for f in sorted(glob.glob(CF)):
    if EVAL and f.split('cev_')[1][:-3] not in LISTO: continue
    p=pd.read_csv(f,header=None,names=['k','t','ix','p','q','x'],dtype={'k':'category','t':np.int64,'ix':np.int32,'p':np.float32,'q':np.float32,'x':np.int8},on_bad_lines='skip'); parts.append(p[p.ix.isin(IXD)])
A=pd.concat(parts,ignore_index=True); del parts
A['kk']=A.k.map({'d':1,'T':2}).astype(np.int8); A=A.drop(columns='k')
T_=A[A.kk==2].drop_duplicates(['t','ix','p','q']); A=pd.concat([A[A.kk==1],T_],ignore_index=True); del T_
A=A.sort_values(['ix','t','kk'],kind='stable'); BS=collections.defaultdict(dict)
for f in glob.glob(BF):
    for ln in open(f):
        i,t,s_=ln.rstrip('\n').split(',',2)
        if int(i) in IXD: BS[TO[int(i)]][int(t)]=s_
EV={ TO[ix]:(g.t.values,g.kk.values,g.p.values,g.q.values,g.x.values) for ix,g in A.groupby('ix',sort=False)}; del A
print(DAY,'tokens',len(EV),flush=True)
def parse_b(s):
    d={}
    for x in s.split(';'):
        if ':' in x:
            p,q=x.split(':'); d[round(float(p),2)]=float(q)
    return d
_C={}
def events(tok):
    if tok in _C: return _C[tok]
    t,k,p,q,x=EV[tok]; t0=TOK[tok][3]*1000-600000
    ev_=[(t0+int(t[i]),int(k[i]),round(float(p[i]),2),float(q[i]),int(x[i]),None) for i in range(len(t))]
    ev_+=[(t0+tb,0,0.0,0.0,0,s_) for tb,s_ in BS[tok].items()]
    ev_.sort(key=lambda e:(e[0],e[1])); _C[tok]=ev_; return ev_

import math
LATP,LATC=85,65; NLEV,SZ,CAP=4,50.0,150.0
MARG={'B':None,'P2':0.02,'P4':0.04,'P6':0.06}
def sim(d,fin,var):
    M=MARG[var]; follow=True
    toks={'YES':d['YES'],'NO':d['NO']}
    st={}
    for l,tk in toks.items(): st[l]=dict(tok=tk,bids={},pend=collections.defaultdict(float),orders=[],posted=False,anchor=None,last=-1e18,blocked=False,inv=0.0,cost=0.0,sawbook=False,capped=False)
    t_post=(fin-300)*1000+2000+LATP; t_end=(fin-60)*1000; fills=[]
    def lab(l,tk):
        for e in events(tk): yield (e[0],e[1],l,e)
    mg=heapq.merge(*[lab(l,tk) for l,tk in toks.items()],key=lambda x:(x[0],x[1]))
    valid=True; chk=False
    def post(S,t,top):
        S['orders']=[o for o in S['orders'] if o['rem']>0 and o['cancel']>t]
        for k in range(NLEV):
            pr=round(top-0.01*k,2)
            if pr<0.02: break
            S['orders'].append(dict(price=pr,rem=SZ,ahead=S['bids'].get(pr,0.0),live=t+LATP,cancel=1e18))
        S['posted']=True; S['anchor']=top; S['last']=t
    def desired(l):
        S=st[l]; O=st['NO' if l=='YES' else 'YES']
        best=max(S['bids']) if S['bids'] else None
        if best is None or not (0.05<=best<0.95): return None,False
        if M is not None and O['inv']-S['inv']>1e-9:
            cap=math.floor((1-O['cost']/O['inv']-M)*100+1e-9)/100
            if cap<best: return round(cap,2),True
        return best,False
    def cancel_live(S,t):
        for o in S['orders']:
            if o['rem']>0 and o['cancel']>t+LATC: o['cancel']=t+LATC
    for t,kk,l,e in mg:
        if t>=t_end: break
        S=st[l]; _,_,p,q,sl,bs=e; filled=False
        if kk==0:
            if bs: S['bids']=parse_b(bs); S['sawbook']=True
        elif kk==1:
            old=S['bids'].get(p,0.0)
            if q<=0: S['bids'].pop(p,None)
            else: S['bids'][p]=q; S['sawbook']=True
            if q<old:
                cx=max(0.0,(old-q)-S['pend'][p]); S['pend'][p]=max(0.0,S['pend'][p]-(old-q))
                if cx>0:
                    for o in S['orders']:
                        if o['price']==p and o['live']<=t: o['ahead']*=(1-cx/old)
        else:
            S['pend'][p]+=q
            if sl==1:
                for o in S['orders']:
                    if o['live']<=t<o['cancel'] and o['rem']>0 and p<=o['price']+1e-9:
                        if p<o['price']-1e-9: f=o['rem']
                        else: f=max(0.0,q-o['ahead']); o['ahead']=max(0.0,o['ahead']-q)
                        f=min(f,o['rem'])
                        if f>0: o['rem']-=f; S['inv']+=f; S['cost']+=f*o['price']; fills.append((t,l,o['price'],f)); filled=True
        if t>=t_post and not chk:
            chk=True; valid=all(st[x]['sawbook'] and st[x]['bids'] for x in st)
            if not valid: return [],False
            for l2,S2 in st.items():
                b2=max(S2['bids'])
                if 0.05<=b2<0.95: post(S2,t,b2)
        if not chk: continue
        for l2 in (('YES','NO') if filled else (l,)):
            S2=st[l2]
            if S2['blocked']: continue
            top,capd=desired(l2)
            if top is None: continue
            if not S2['posted']:
                if t>=t_post: post(S2,t,top); S2['capped']=capd
            elif follow and top!=S2['anchor'] and any(o['rem']>0 for o in S2['orders']):
                urgent=capd or S2['capped']
                if (urgent and t-S2['last']>=250) or (t-S2['last']>=1000):
                    cancel_live(S2,t); post(S2,t+LATC,top); S2['capped']=capd
        for l2 in st:
            S2=st[l2]; O2=st['NO' if l2=='YES' else 'YES']
            if S2['posted'] and not S2['blocked'] and S2['inv']-O2['inv']>CAP:
                S2['blocked']=True; cancel_live(S2,t)
    return fills,valid
mk=collections.defaultdict(dict)
for tok in EV: mk[TOK[tok][2]][TOK[tok][4]]=tok
rows=[]; validm=set(); nm=0
for mid,d in mk.items():
    _C.clear()
    if 'YES' not in d or 'NO' not in d or mid not in DES: continue
    fin=TOK[d['YES']][3]
    if LIM and nm>=LIM: break
    nm+=1
    for vn in VARS:
        fl,ok=sim(d,fin,vn)
        if vn==VARS[0] and ok: validm.add(mid)
        if not ok: continue
        for t,l,p,a in fl: rows.append((DAY,mid,l,vn,t,p,a,p*a,a*(DES[mid]==l)-p*a,0.014*(1-p)*p*a))
X=pd.DataFrame(rows,columns=['dia','mid','lc','var','t','pc','acc','coste','pnl','reb'])
if not LIM: X.to_csv(OUTD+f'f6_sim_{DAY}.csv.gz',index=False)
print(DAY,'mercados validos',len(validm),'fills sim',len(X),flush=True)
if LIM:
    # control de construccion: en P*, acciones emparejadas (AVG) con margen >= M ?
    for vn in VARS:
        x=X[X['var']==vn]
        for mid,g in x.groupby('mid'):
            y=g[g.lc=='YES']; n=g[g.lc=='NO']; m=min(y.acc.sum(),n.acc.sum())
            if m>0:
                mm=1-(y.pc*y.acc).sum()/y.acc.sum()-(n.pc*n.acc).sum()/n.acc.sum()
                print(vn,mid,'par',round(m,1),'margen medio',round(mm,3),'accY',y.acc.sum(),'accN',n.acc.sum())
