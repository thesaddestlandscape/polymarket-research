#!/usr/bin/env python3
"""r12: sim v2 (PREREG_V2.md) + fills reales de la muestra con markout 30 s y clasificacion pata suelta/emparejada. Uso: r12_v2.py DIA VARIANTES(A,B)
DIA en construccion (20,21,22): c_*.gz + tok_order.json ; en evaluacion (18,19,23): cev_*.gz/bev_* + tok_order_ev.json."""
import gzip,json,glob,sys,collections,heapq,numpy as np,pandas as pd
DL='/root/polymarket-research-datalogs/'; R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; RG=R+'rebate_ganadores/'
DAY=sys.argv[1]; VARS=sys.argv[2].split(',')
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
LATP,LATC=85,65; NLEV,SZ,CAP=4,50.0,150.0
def sim(d,fin,follow):
    toks={'YES':d['YES'],'NO':d['NO']}
    st={}
    for l,tk in toks.items(): st[l]=dict(tok=tk,bids={},pend=collections.defaultdict(float),orders=[],posted=False,anchor=None,last=-1e18,blocked=False,inv=0.0,sawbook=False)
    t_post=(fin-300)*1000+2000+LATP; t_end=(fin-60)*1000; fills=[]
    def lab(l,tk):
        for e in events(tk): yield (e[0],e[1],l,e)
    mg=heapq.merge(*[lab(l,tk) for l,tk in toks.items()],key=lambda x:(x[0],x[1]))
    valid=True; chk=False
    def post(S,t,best):
        S['orders']=[o for o in S['orders'] if o['rem']>0 and o['cancel']>t]  # vivos
        for k in range(NLEV):
            pr=round(best-0.01*k,2)
            if pr<0.02: break
            S['orders'].append(dict(price=pr,rem=SZ,ahead=S['bids'].get(pr,0.0),live=t+LATP,cancel=1e18))
        S['posted']=True; S['anchor']=best; S['last']=t
    for t,kk,l,e in mg:
        if t>=t_end: break
        S=st[l]; _,_,p,q,sl,bs=e
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
                        if f>0: o['rem']-=f; S['inv']+=f; fills.append((t,l,o['price'],f))
        if t>=t_post and not chk:
            chk=True; valid=all(st[x]['sawbook'] and st[x]['bids'] for x in st)
            if not valid: return [],False
            for S2 in st.values():
                b2=max(S2['bids']); 
                if 0.05<=b2<0.95: post(S2,t,b2)
        best=max(S['bids']) if S['bids'] else None
        if chk and best is not None and not S['blocked']:
            O=st['NO' if l=='YES' else 'YES']
            if not S['posted'] and t>=t_post and 0.05<=best<0.95: post(S,t,best)
            elif S['posted'] and follow and best!=S['anchor'] and t-S['last']>=1000 and any(o['rem']>0 for o in S['orders']) and 0.05<=best<0.95:
                for o in S['orders']:
                    if o['rem']>0 and o['cancel']>t+LATC: o['cancel']=t+LATC
                post(S,t+LATC,best)
            if S['posted'] and S['inv']-O['inv']>CAP:
                S['blocked']=True
                for o in S['orders']:
                    if o['rem']>0 and o['cancel']>t+LATC: o['cancel']=t+LATC
    return fills,valid
mk=collections.defaultdict(dict)
for tok in EV: mk[TOK[tok][2]][TOK[tok][4]]=tok
rows=[]; validm=set()
for mid,d in mk.items():
    _C.clear()
    if 'YES' not in d or 'NO' not in d or mid not in DES: continue
    fin=TOK[d['YES']][3]
    for vn in VARS:
        fl,ok=sim(d,fin,vn=='B')
        if vn==VARS[0] and ok: validm.add(mid)
        if not ok: continue
        for t,l,p,a in fl: rows.append((DAY,mid,l,'V2'+vn,t,p,a,p*a,a*(DES[mid]==l)-p*a,0.014*(1-p)*p*a))
X=pd.DataFrame(rows,columns=['dia','mid','lc','var','t','pc','acc','coste','pnl','reb']); X.to_csv(RG+f'datos/r12_sim_{DAY}.csv.gz',index=False)
print(DAY,'mercados validos',len(validm),'fills sim',len(X),flush=True)
# ---- real
GAN=('0x21f4c1a1','0xe29042f5','0x86b14772')
cols=['dia','maker','rol','coin','mid','lc','pc','coste','acc','T','ts_est']
Rl=pd.concat([pd.read_csv(RG+f'datos/{n}',usecols=cols,dtype={'mid':str,'maker':str,'rol':str,'coin':str,'lc':str,'dia':str}) for n in ('r4_fills.csv.gz','r4b_fills.csv.gz','r4c_fills.csv.gz')])
Rl=Rl[(Rl.coin=='BTC')&(Rl.rol=='M')&Rl.maker.str[:10].isin(GAN)&Rl.mid.isin(validm)&(Rl.dia==DAY)&(Rl['T']>60)&(Rl['T']<=300)&(Rl.pc>=0.01)&(Rl.pc<0.99)].copy()
Rl['pnl']=Rl.acc*(Rl.lc==Rl.mid.map(DES))-Rl.coste; Rl['reb']=0.014*(1-Rl.pc)*Rl.coste
# pata suelta: por (wallet,mercado) lado con mas acc = suelta
g=Rl.groupby(['maker','mid','lc']).acc.sum().unstack(fill_value=0)
for l in ('YES','NO'):
    if l not in g: g[l]=0.0
g['suelta']=np.where(g.YES>=g.NO,'YES','NO'); g['mn']=np.minimum(g.YES,g.NO)
Rl=Rl.merge(g[['suelta']].reset_index(),on=['maker','mid'],how='left'); Rl['rol_pata']=np.where(Rl.lc==Rl.suelta,'suelta','emparejada')
# markout 30 s con libro5
mo=[]
for (mid,lc),gg in Rl.groupby(['mid','lc']):
    _C.clear(); tok=mk[mid].get(lc)
    if tok is None or tok not in EV: continue
    Eo=events(tok); q=sorted([(int(r.ts_est*1000-2400+30000),r.Index) for r in gg.itertuples()]); i=0; bids={}
    for tq,ix in q:
        while i<len(Eo) and Eo[i][0]<=tq:
            _,kk,pp,qq,_,bs=Eo[i]; i+=1
            if kk==0 and bs: bids=parse_b(bs)
            elif kk==1:
                if qq<=0: bids.pop(pp,None)
                else: bids[pp]=qq
        mo.append((ix,max(bids) if bids else np.nan))
M=pd.DataFrame(mo,columns=['ix','bid30']).drop_duplicates('ix').set_index('ix'); Rl=Rl.join(M)
Rl.to_csv(RG+f'datos/r12_real_{DAY}.csv.gz',index=False); print(DAY,'fills reales',len(Rl),flush=True)
