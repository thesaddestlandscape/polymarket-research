#!/usr/bin/env python3
"""r9: ancla del simulador de pares/cosechar BTC 5m contra 0x21f4/0xe290 (pares) y 0x86b1 (direccional) con libro5 BTC.
Muestra: 1 de cada 3 mercados BTC 5m (fin//300 %3==0), dias 20,21,22-Oct (toks_sub.json, extraccion awk de libro5_ms, solo tipos T, d(bids), B).
Politica simulada (pre-declarada, SIN ajustar a los ganadores): en cada mercado, un bid de S acciones POR LADO al mejor bid (touch) en T=300-2 s (+85 ms latencia), vivo hasta T=60 s,
solo si el mejor bid esta en la banda. Variantes: SIT (no repone) / TOP (sigue el mejor bid: cancela 65 ms + repone 85 ms, pierde cola);
cola: COLA_T (delante solo se consume con trades) / COLA_TD (ademas cancelaciones proporcionales). Relleno: trade SELL a precio<=bid; a precio<bid llena todo; a ==bid consume cola.
Desenlace oficial (maker_ms_desenlaces_cache). Rebate = 0.014(1-p)*coste. Unidad: mercado+lado."""
import gzip,json,glob,sys,collections,bisect,numpy as np,pandas as pd
DL='/root/polymarket-research-datalogs/'; R='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/'
TOK=json.load(open(DL+'rebate_ganadores_btc/toks_sub.json')); DES=json.load(open(DL+'maker_ms_desenlaces_cache.json'))
S=10.0; LATP,LATC=85,65
import os
DAY=sys.argv[1]; TO=json.load(open(DL+'rebate_ganadores_btc/tok_order.json'))
IXD=set(i for i,t in enumerate(TO) if pd.Timestamp(TOK[t][3],unit='s',tz='UTC').strftime('%Y-%m-%d')==DAY)
parts=[(lambda p:p[p.ix.isin(IXD)])(pd.read_csv(f,header=None,names=['k','t','ix','p','q','x'],dtype={'k':'category','t':np.int64,'ix':np.int32,'p':np.float32,'q':np.float32,'x':np.int8},on_bad_lines='skip')) for f in sorted(glob.glob(DL+'rebate_ganadores_btc/c_*.gz'))]
A=pd.concat(parts,ignore_index=True); del parts
A['kk']=A.k.map({'d':1,'T':2}).astype(np.int8); A=A.drop(columns='k')
n0=len(A); T_=A[A.kk==2].drop_duplicates(['t','ix','p','q']); A=pd.concat([A[A.kk==1],T_],ignore_index=True); del T_
print('filas',n0,'tras dedup trades',len(A),flush=True)
A=A.sort_values(['ix','t','kk'],kind='stable')
BS=collections.defaultdict(dict)
for f in glob.glob(DL+'rebate_ganadores_btc/b_*.txt'):
    for ln in open(f):
        i,t,s_=ln.rstrip('\n').split(',',2)
        if int(i) in IXD: BS[TO[int(i)]][int(t)]=s_
EV={}
for ix,g in A.groupby('ix',sort=False): EV[TO[ix]]=(g.t.values,g.kk.values,g.p.values,g.q.values,g.x.values)
print('tokens con eventos',len(EV),len(A),'eventos',flush=True); del A
_C={}
def events(tok):
    if tok in _C: yield from _C[tok]; return
    yield from _events(tok)
def _events(tok):
    t,k,p,q,x=EV[tok]; t0=TOK[tok][3]*1000-600000
    ev_=[(int(t[i]),int(k[i]),round(float(p[i]),2),float(q[i]),int(x[i]),None) for i in range(len(t))]
    ev_+=[(tb,0,0.0,0.0,0,s_) for tb,s_ in BS[tok].items()]
    ev_.sort(key=lambda e:(e[0],e[1]))
    _C[tok]=[(t0+e[0],)+e[1:] for e in ev_]
    yield from _C[tok]
def parse_b(s):
    d={}
    for x in s.split(';'):
        if ':' in x:
            p,q=x.split(':'); d[round(float(p),2)]=float(q)
    return d
def run(tok,band,top,tdq,fin):
    """devuelve lista de rellenos [(t_ms,precio,acc)]"""
    bids={}; pend=collections.defaultdict(float)
    t_post=(fin-300)*1000+2000+LATP; t_end=(fin-60)*1000
    live=False; price=None; ahead=0.0; rem=S; fills=[]; sched=None
    for t,kk,pp,qq,sl,bs in events(tok):
        k='BdT'[kk]
        if k=='B': bids=parse_b(bs) if bs else bids
        elif k=='d':
            p=round(pp,2); q=qq; old=bids.get(p,0.0)
            if q<=0: bids.pop(p,None)
            else: bids[p]=q
            if live and tdq and p==price and q<old:
                cx=max(0.0,(old-q)-pend[p]); pend[p]=max(0.0,pend[p]-(old-q))
                if cx>0 and old>0: ahead*=(1-cx/old)
        elif k=='T':
            p=round(pp,2); sz=qq
            pend[p]+=sz
            if live and sl==1 and rem>0 and p<=price+1e-9:
                if p<price-1e-9: f=rem
                else:
                    f=max(0.0,sz-ahead); ahead=max(0.0,ahead-sz)
                f=min(f,rem)
                if f>0: fills.append((t,price,f)); rem-=f
        if t>=t_end:
            break
        best=max(bids) if bids else None
        if not live and sched is None and t>=t_post and best is not None and rem>0 and not fills:
            if band[0]<=best<band[1]: live=True; price=best; ahead=bids.get(best,0.0); 
            elif t>t_post+3000 and False: pass
        elif live and top and rem>0 and best is not None and best!=price:
            if sched is None: sched=(t+LATC+LATP,best)
        if sched is not None and t>=sched[0] and live:
            nb=sched[1]; sched=None
            if band[0]<=nb<band[1]: price=nb; ahead=bids.get(nb,0.0)
            else: live=False
    return fills
mk=collections.defaultdict(dict)
for tok,v in TOK.items():
    if TO.index(tok) in IXD if False else tok in EV: mk[v[2]][v[4]]=tok
rows=[]
VAR={'SIT_ALL':(False,(0.05,0.95)),'SIT_BARATO':(False,(0.05,0.30)),'TOP_ALL':(True,(0.05,0.95)),'TOP_BARATO':(True,(0.05,0.30))}
for mid,d in []:
    _C.clear()
    if 'YES' not in d or 'NO' not in d or mid not in DES: continue
    fin=TOK[d['YES']][3]; dia=pd.Timestamp(fin,unit='s',tz='UTC').strftime('%Y-%m-%d')
    for vn,(top,band) in VAR.items():
        for tdq in ((0,1) if vn=='SIT_ALL' else (1,)):
            for lado,tok in d.items():
                if tok not in EV: continue
                for t,p,a in run(tok,band,top,tdq,fin):
                    rows.append((dia,mid,lado,vn,tdq,t,p,a,p*a,a*(DES[mid]==lado)-p*a,0.014*(1-p)*p*a))
X=pd.DataFrame(rows,columns=['dia','mid','lc','var','tdq','t','pc','acc','coste','pnl','reb'])

print(len(X),'fills simulados')
# ---- fills reales de los 3 ganadores (maker) en los mercados de la muestra, con estado del libro 3 s antes del bloque
GAN={'0x21f4c1a1':'21f4','0xe29042f5':'e290','0x86b14772':'86b1'}
cols=['dia','maker','rol','coin','mid','lc','pc','coste','acc','T','ts_est']
Rl=pd.concat([pd.read_csv(R+f'rebate_ganadores/datos/{n}',usecols=cols,dtype={'mid':str,'maker':str,'rol':str,'coin':str,'lc':str,'dia':str}) for n in ('r4_fills.csv.gz','r4b_fills.csv.gz')])
Rl=Rl[(Rl.coin=='BTC')&(Rl.rol=='M')&Rl.maker.str[:10].isin(GAN)&Rl.mid.isin(set(mk))&(Rl.dia==DAY)&(Rl['T']>60)&(Rl['T']<=300)&(Rl.pc>=0.01)&(Rl.pc<0.99)].copy()
Rl=Rl[Rl.mid.isin(DES)]; Rl['pnl']=Rl.acc*(Rl.lc==Rl.mid.map(DES))-Rl.coste; Rl['reb']=0.014*(1-Rl.pc)*Rl.coste
bk=[];lv=[]
for (mid,lc),g in Rl.groupby(['mid','lc']):
    _C.clear(); tok=mk[mid].get(lc)
    if tok not in EV: continue
    Eo=list(events(tok)); fl=sorted(zip((g.ts_est*1000-3000).astype(np.int64),g.pc,g.index)); i=0; bids={}
    for t,p,ix in fl:
        while i<len(Eo) and Eo[i][0]<=t:
            _,kk,pp,q,_,bs=Eo[i]; i+=1
            if kk==0: bids=parse_b(bs) if bs else bids
            elif kk==1:
                pp=round(pp,2)
                if q<=0: bids.pop(pp,None)
                else: bids[pp]=q
        bk.append((ix,(max(bids)-round(p,2)) if bids else np.nan,bids.get(round(p,2),np.nan)))
D=pd.DataFrame(bk,columns=['ix','dist','nivel']).drop_duplicates('ix').set_index('ix'); Rl=Rl.join(D)
Rl.to_csv(R+'rebate_ganadores/datos/r9_real_fills_muestra_'+DAY+'.csv.gz',index=False)
print(len(Rl),'fills reales maker en la muestra')
