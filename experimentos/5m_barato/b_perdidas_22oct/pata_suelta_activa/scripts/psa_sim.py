#!/usr/bin/env python3
"""f6 (F7 precio del par): sim v2 + tope de precio de la 2a pata. ORIGEN r12. sim v2 (PREREG_V2.md) + fills reales de la muestra con markout 30 s y clasificacion pata suelta/emparejada. Uso: r12_v2.py DIA VARIANTES(A,B)
DIA en construccion (20,21,22): c_*.gz + tok_order.json ; en evaluacion (18,19,23): cev_*.gz/bev_* + tok_order_ev.json."""
import gzip,json,glob,sys,collections,heapq,numpy as np,pandas as pd
DL='/root/polymarket-research-datalogs/'; R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'; RG=R+'rebate_ganadores/'; OUTD=R+'pata_suelta_activa/datos/'
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


# ===================== PSA v1: maquina de estados "pata suelta activa" (PREREG.md) =====================
import math
LATP,LATC,REARM=85,65,250            # ms: alta (F1/E2), cancelacion, re-armado de clip tras relleno
CLIP=5.0; ICAP=15.0; BAND=(0.30,0.70); M0=0.02; TD0,TD1=150.0,90.0
MODES=('BASE','PES','OPT')
def Mt(t,fin):
    left=fin-t/1000.0
    if left>TD0: return M0
    if left<=TD1: return 0.0
    return M0*(left-TD1)/(TD0-TD1)
def sim(d,fin,var,mode):
    toks={'YES':d['YES'],'NO':d['NO']}; st={}
    for l,tk in toks.items(): st[l]=dict(bids={},pend=collections.defaultdict(float),orders=[],last=-1e18,lastfill=-1e18,inv=0.0,cost=0.0,sawbook=False,hist=collections.deque())
    t_post=(fin-300)*1000+2000+LATP; t_end=(fin-60)*1000; fills=[]; flag=[None]
    def lab(l,tk):
        for e in events(tk): yield (e[0],e[1],l,e)
    mg=heapq.merge(*[lab(l,tk) for l,tk in toks.items()],key=lambda x:(x[0],x[1]))
    chk=False
    other=lambda l:'NO' if l=='YES' else 'YES'
    def live_order(S,t): return [o for o in S['orders'] if o['rem']>0 and o['cancel']>t]
    def cancel_all(S,t):
        for o in S['orders']:
            if o['rem']>0 and o['cancel']>t+LATC: o['cancel']=t+LATC
    def desired(l,t):
        S=st[l]; O=st[other(l)]
        best=max(S['bids']) if S['bids'] else None
        if best is None: return None,False
        I=S['inv']-O['inv']
        if var=='C0': return (best if BAND[0]<=best<=BAND[1] else None),False
        if I<=-CLIP+1e-9:                       # pata rezagada: COMPLETAR/PERSEGUIR con tope (M decae a 0 = salir a coste)
            cap=math.floor((1-O['cost']/O['inv']-Mt(t,fin))*100+1e-9)/100
            pr=round(min(best,cap),2)
            return (pr if pr>=0.01 else None),(cap<best)
        if not (BAND[0]<=best<=BAND[1]): return None,False
        if I>=ICAP-1e-9: return None,False      # TOPE de inventario: retirar el lado que sobra
        if I>=CLIP-1e-9 and fin-t/1000.0<=TD0: return None,False   # fase de persecucion: no anadir al lado sobrante
        return best,False
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
                        elif mode=='BASE': f=max(0.0,q-o['ahead']); o['ahead']=max(0.0,o['ahead']-q)
                        elif mode=='OPT': f=q
                        else: f=0.0
                        f=min(f,o['rem'])
                        if f>0:
                            O=st[other(l)]; rol='lag' if O['inv']-S['inv']>=CLIP-1e-9 else 'flat_exc'
                            o['rem']-=f; S['inv']+=f; S['cost']+=f*o['price']; S['lastfill']=t
                            fills.append((t,l,o['price'],f,rol,round(Mt(t,fin),4))); filled=True
        if S['bids']:
            S['hist'].append((t,max(S['bids'])))
            while S['hist'] and S['hist'][0][0]<t-6000: S['hist'].popleft()
        if t>=t_post and not chk:
            chk=True
            if not all(st[x]['sawbook'] and st[x]['bids'] for x in st): return [],False,None
        if not chk: continue
        if flag[0] is None:                      # senal ex ante (secundaria): al entrar en desequilibrio, barrido en contra del lado sobrante en los 5 s previos
            for l2 in st:
                if st[l2]['inv']-st[other(l2)]['inv']>=CLIP-1e-9:
                    h=[b for tt,b in st[l2]['hist'] if tt<=t-5000]
                    b0=h[-1] if h else (st[l2]['hist'][0][1] if st[l2]['hist'] else None)
                    bn=max(st[l2]['bids']) if st[l2]['bids'] else None
                    flag[0]=int(b0 is not None and bn is not None and bn-b0<=-0.02)
        for l2 in (('YES','NO') if filled else (l,)):
            S2=st[l2]; top,urg=desired(l2,t); lv=live_order(S2,t)
            if top is None:
                if lv: cancel_all(S2,t)
                continue
            if not lv:
                if t-S2['lastfill']>=REARM and t-S2['last']>=REARM:
                    S2['orders']=[o for o in S2['orders'] if o['rem']>0 and o['cancel']>t]
                    S2['orders'].append(dict(price=top,rem=CLIP,ahead=S2['bids'].get(top,0.0),live=t+LATP,cancel=1e18)); S2['last']=t
            elif lv[0]['price']!=top and ((urg and t-S2['last']>=250) or t-S2['last']>=1000):
                cancel_all(S2,t); S2['orders'].append(dict(price=top,rem=CLIP,ahead=S2['bids'].get(top,0.0),live=t+LATC+LATP,cancel=1e18)); S2['last']=t
    return fills,True,flag[0]
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
        for md in MODES:
            fl,ok,fg=sim(d,fin,vn,md)
            if not ok: break
            validm.add(mid)
            for t,l,p,a,rol,m in fl: rows.append((DAY,mid,l,vn,md,t,p,a,p*a,a*(DES[mid]==l)-p*a,0.014*(1-p)*p*a,rol,m,fg))
X=pd.DataFrame(rows,columns=['dia','mid','lc','var','mode','t','pc','acc','coste','pnl','reb','rol','M','flag'])
pd.DataFrame({'mid':sorted(validm)}).assign(dia=DAY).to_csv(OUTD+f'validos_{DAY}.csv' if not LIM else '/dev/null',index=False)
if not LIM: X.to_csv(OUTD+f'psa_sim_{DAY}.csv.gz',index=False)
print(DAY,'mercados validos',len(validm),'fills sim',len(X),flush=True)
if LIM: print(X.groupby(['var','mode']).agg(n=('acc','size'),acc=('acc','sum'),coste=('coste','sum'),pnl=('pnl','sum')))
