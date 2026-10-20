#!/usr/bin/env python3
"""Calibracion de colas A6 con libro5 (cancelaciones por delante). Solo lectura. Por mercado: replay del libro de bids,
explicacion de bajadas por trades, muestras virtuales (1 por token x tramo T) y replay de la cola con 3 reparto de cancelaciones."""
import sys, os, json, gzip, glob, bisect, collections, heapq, math
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/'
TOK=json.load(open(C+'tokens.json'))
CIE={}   # (coin,mkt)->cierre
for t,(a,m,lado,fin) in TOK.items(): CIE[(a,m)]=fin
TAM=50.0; LALTA=int(os.environ.get('LALTA','85'))
GRID=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.25,1.5,2.0]
WB=int(os.environ.get('WB','300')); WA=int(os.environ.get('WA','150'))          # una bajada de nivel se explica por un trade si su recepcion cae en [r_trade-WB, r_trade+WA] ms (la bajada llega ~100 ms ANTES que el T)
TRAMOS=[(60,140),(140,220),(220,270)]   # tramo = rango de T en que se POSTEA la puja virtual (1a ocasion elegible); A6 no entra por encima de T=270
WS=[1,2,3,5,10,20,30,60,120,180]   # segundos desde t0
BAND_LO,BAND_HI=100,300   # milesimas; (lo,hi]
OPP={'Y':'N','N':'Y'}
def mills(p): return int(round(float(p)*1000))
def pbook(s):
    d={}
    if s:
        for x in s.split(';'):
            if ':' in x:
                p,z=x.split(':'); z=float(z)
                if z>0: d[mills(p)]=z
    return d
GALL=[]
if os.path.exists(C+'g_all.txt'):
    for l in open(C+'g_all.txt'):
        try: r,m=l.strip().split(',',1); GALL.append((int(r),m))
        except: pass
GALL.sort()
def load(path):
    ev=[]
    with gzip.open(path,'rt',errors='replace') as f:
        try:
            for ln in f:
                c=ln.rstrip('\n').split(',')
                t=c[1]
                try:
                    if t=='d': ev.append((int(c[2]),'d',c[0],c[3],mills(c[4]),float(c[5])))
                    elif t=='T': ev.append((int(c[2]),'T',c[0],c[3],mills(c[4]),float(c[5])))   # side='BUY'|'SELL' (c[3]), price
                    elif t=='B': ev.append((int(c[2]),'B',c[0],pbook(c[3]),pbook(c[4])))
                    elif t=='G': ev.append((int(c[2]),'G',c[0],c[3]))
                except (ValueError,IndexError): continue
        except (EOFError,OSError): pass
    return ev
def tramo(T):
    for i,(a,b) in enumerate(TRAMOS):
        if a<T<=b: return i
    return None
def bucket(q):
    if q<=150: return '0.10-0.15'
    if q<=200: return '0.15-0.20'
    if q<=250: return '0.20-0.25'
    return '0.25-0.30'

def procesa(coin,mkt,path,diag):
    cierre=CIE.get((coin,mkt))
    if cierre is None: return []
    ev=load(path)
    if not ev: return []
    r0,r1=ev[0][0],ev[-1][0]
    i0=bisect.bisect_left(GALL,(r0,'')); i1=bisect.bisect_right(GALL,(r1,'~'))
    g=[(r,'G','*',m) for r,m in GALL[i0:i1]]
    if g: ev=list(heapq.merge(ev,g,key=lambda e:e[0]))
    # --- pasada 1: trades por nivel
    own=collections.defaultdict(list)   # (L,q)->[r,rem]  T SELL en L a q
    mint=collections.defaultdict(list)  # (L,q)->[r,rem]  T BUY en opp a p -> q=1000-p en L
    NT={'Y':[],'N':[]}                  # trades normalizados (r,q,acc,tipo) por lado adquirido
    for e in ev:
        if e[1]=='T':
            r,_,L,side,q,sz=e
            if side=='SELL': own[(L,q)].append([r,sz]); NT[L].append((r,q,sz,'own'))
            elif side=='BUY':
                Lc=OPP[L]; qc=1000-q; mint[(Lc,qc)].append([r,sz]); NT[Lc].append((r,qc,sz,'mint'))
    for k in NT: NT[k].sort(key=lambda x:x[0])
    diag['tot_own']+=sum(x[1] for l in own.values() for x in l); diag['tot_mint']+=sum(x[1] for l in mint.values() for x in l)
    CUMT={}; CUMV={}
    for L_ in 'YN':
        tt=[];vv=[];acc_=0.0
        for (r_,q_,a_,tp_) in NT[L_]:
            T_=cierre-r_/1000.0
            if 100<q_<=300 and 60<T_<=300: acc_+=a_
            tt.append(r_); vv.append(acc_)
        CUMT[L_]=tt; CUMV[L_]=vv
    def cum_at(L_,r_):
        i_=bisect.bisect_right(CUMT[L_],r_)
        return CUMV[L_][i_-1] if i_>0 else 0.0
    # --- pasada 2: replay del libro, eventos de nivel, muestras
    bids={'Y':{},'N':{}}; asks={'Y':{},'N':{}}; valid={'Y':False,'N':False}
    lev=collections.defaultdict(list)   # (L,q)-> [r,delta,e_own,e_mint,kind]
    ptr_o=collections.defaultdict(int); ptr_m=collections.defaultdict(int)
    muestras=[]; hecho=set(); last_eval={}
    sync_abs=0.0; sync_n=0; dec_total=0.0; dec_own=0.0; dec_mint=0.0; nB=0
    for e in ev:
        r,t=e[0],e[1]
        if t=='G':
            L=e[2]
            if L=='*': valid['Y']=valid['N']=False
            else: valid[L]=False
            continue
        if t=='B':
            L=e[2]; nB+=1
            nb,na=e[3],e[4]
            if valid[L]:
                ob=bids[L]
                for q in set(ob)|set(nb):
                    dl=nb.get(q,0.0)-ob.get(q,0.0)
                    if abs(dl)>1e-6:
                        sync_abs+=abs(dl); sync_n+=1
                        lev[(L,q)].append([r,dl,0.0,'sync'])
            bids[L]=dict(nb); asks[L]=dict(na); valid[L]=True
            continue
        if t=='d':
            _,_,L,side,q,sz=e
            if not valid[L]: continue
            if side=='B':
                old=bids[L].get(q,0.0); dl=sz-old
                if sz>0: bids[L][q]=sz
                else: bids[L].pop(q,None)
                if abs(dl)>1e-9:
                    ent=[r,dl,0.0,'d']
                    lev[(L,q)].append(ent)
                    if dl<0: dec_total+=-dl
            else:
                if sz>0: asks[L][q]=sz
                else: asks[L].pop(q,None)
        # --- muestreo
        if t in('d',) and valid['Y'] and valid['N']:
            T=cierre-r/1000.0
            k=tramo(T)
            if k is None: continue
            L=e[2]
            for LL in ('Y','N'):
                bb=max(bids[LL],default=None)
                if bb is None or not(BAND_LO<bb<=BAND_HI): continue
                ba=min(asks[LL],default=None)
                bbo=max(bids[OPP[LL]],default=None)
                cum=cum_at(LL,r)
                for kind in ('g','a'):
                    key=(LL,k,kind)
                    if key in hecho: continue
                    if kind=='a' and cum<5000.0: continue
                    if r-last_eval.get(key,0)<1000: continue
                    last_eval[key]=r
                    if (ba is not None and bb>=ba) or (bbo is not None and bb+bbo>1000):
                        diag['cruzado']+=1; continue
                    hecho.add(key)
                    muestras.append({'L':LL,'k':k,'kind':kind,'cum':cum,'t0':r,'T0':T,'q0':bb,'D0':bids[LL][bb],'cierre':cierre,'ba':ba,'bbo':bbo,'n_niv':len(bids[LL])})
    # emparejado centrado en el trade: cada trade reclama bajadas del mismo nivel en [r-WB, r+WA]
    for tp,dic in (('own',own),('mint',mint)):
        for (L,q),trs in dic.items():
            lst=[x for x in lev.get((L,q),()) if x[1]<0 and x[3]=='d']
            if not lst: continue
            times=[x[0] for x in lst]
            for tr in trs:
                rt=tr[0]; rem=tr[1]
                i=bisect.bisect_left(times,rt-WB); j=bisect.bisect_right(times,rt+WA)
                for k in sorted(range(i,j),key=lambda k:abs(lst[k][0]-rt)):
                    if rem<=1e-9: break
                    libre=-lst[k][1]-lst[k][2]
                    u=min(rem,libre)
                    if u>1e-9:
                        lst[k][2]+=u; rem-=u; diag['match_'+tp]+=u
                        if len(diag['lag_'+tp])<20000: diag['lag_'+tp].append(lst[k][0]-rt)
                tr.append(rem)   # no emparejado
    diag['dec_total']+=dec_total
    diag['sync_abs']+=sync_abs; diag['sync_n']+=sync_n; diag['nB']+=nB
    # --- pasada 3: replay de cada muestra
    out=[]
    for s_ in muestras:
        L,q0,t0,D0=s_['L'],s_['q0'],s_['t0'],s_['D0']
        te=int((s_['cierre']-60)*1000)
        evs=[]
        for x in lev.get((L,q0),()):
            if t0<x[0]<=te: evs.append((x[0],0,x))
        for (r,q,acc,tp) in NT[L]:
            if t0<r<=te and q<=q0: evs.append((r,1,(q,acc,tp)))
        evs.sort(key=lambda z:(z[0],z[1]))
        gi=bisect.bisect_right(GALL,(t0,'~'))
        s_['roto']=bool(gi<len(GALL) and GALL[gi][0]<=te)
        tready=t0+LALTA
        res={}
        # colas del shadow: copia exacta de Orden.aplicar (trades normalizados, recv >= t_ready, barrido si pc < puja)
        for nm,f in [('f%03d'%int(round(g*100)),g) for g in GRID]:
            ah=f*D0; rest=TAM; fills=[]
            for (r,pri,x) in evs:
                if pri!=1 or r<tready: continue
                pc,acc,tp=x
                if rest<=1e-9: break
                if pc<q0: ah=0.0; fl=rest
                else:
                    u=min(acc,ah); ah-=u; fl=min(acc-u,rest)
                if fl>1e-9: fills.append((r,fl)); rest-=fl
            res['sh_'+nm]=fills
        # replays fisicos con 3 repartos de las cancelaciones no explicadas
        for alloc in ('lo','prop','hi'):
            ah=D0; bh=0.0; rest=TAM; ca=0.0; ct=0.0; ctp=0.0; apre=0.0; fills=[]; snaps={}; wi=0; ah_ready=None; f1=None
            for (r,pri,x) in evs+[(10**15,9,None)]:
                while wi<len(WS) and t0+WS[wi]*1000<=r:
                    snaps[WS[wi]]=(ca,TAM-rest,ah,apre); wi+=1
                if pri==9: break
                if ah_ready is None and r>=tready: ah_ready=ah
                if pri==0:
                    rr,dl,e_,kind=x
                    if dl>0:
                        if r<tready: ah+=dl; apre+=dl
                        else: bh+=dl
                    else:
                        xx=-dl
                        u=max(0.0,xx-e_) if kind!='sync' else xx
                        if u>0:
                            tot=ah+bh
                            if tot<=1e-9: continue
                            if alloc=='prop': c=u*ah/tot
                            elif alloc=='hi': c=min(u,ah)
                            else: c=max(0.0,u-bh)
                            c=min(c,ah); ah-=c; bh=max(0.0,bh-(u-c)); ca+=c
                else:
                    pc,acc,tp=x
                    if pc<q0:
                        ct+=ah; ctp+=(ah if r>=tready else 0.0); ah=0.0
                        if r>=tready and rest>1e-9:
                            if f1 is None: f1=(r,ca,ct,ctp,apre,D0)
                            fills.append((r,rest)); rest=0.0
                    else:
                        u=min(acc,ah); ah-=u; ct+=u; ctp+=(u if r>=tready else 0.0); left=acc-u
                        if r>=tready and left>1e-9 and rest>1e-9:
                            if f1 is None: f1=(r,ca,ct,ctp,apre,D0)
                            fl=min(left,rest); fills.append((r,fl)); rest-=fl
            while wi<len(WS):
                snaps[WS[wi]]=(ca,TAM-rest,ah,apre); wi+=1
            res['rp_'+alloc]={'ca_end':ca,'ct_end':ct,'ah_end':ah,'ctp_end':ctp,'apre':apre,'ah_ready':ah_ready,'fills':fills,'snaps':snaps,'f1':f1}
        s_['res']=res
        out.append(s_)
    return out
