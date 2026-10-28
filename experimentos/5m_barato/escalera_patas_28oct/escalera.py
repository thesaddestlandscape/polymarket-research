import sys, gzip, csv, json, math, random, datetime
import numpy as np
from array import array
BASEU='/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/units/u_%s.csv.gz'
REG='/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
OUT='/root/polymarket-research/experimentos/5m_barato/escalera_patas_28oct/out/e_%s.csv'
G=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
D=(0.05,0.10,0.15,0.20,0.30,0.45); LX=150.0; LT=250.0; E=1e-9
def fee(p): return 0.07*p*(1-p)
def c2(x): return math.ceil(x*100-1e-6)/100.0
class Tok:
    def __init__(s,cie): s.q=array('d'); s.p=array('d'); s.cie=cie*1000
def prep(t):
    t.qa=np.frombuffer(t.q,dtype=float).reshape(-1,3) if len(t.q) else np.zeros((0,3))
    o=np.argsort(t.qa[:,0],kind='stable'); t.qa=t.qa[o]
    t.pa=np.frombuffer(t.p,dtype=float).reshape(-1,3) if len(t.p) else np.zeros((0,3))  # t,p,side(1=BUY,0=SELL)
    o=np.argsort(t.pa[:,0],kind='stable'); t.pa=t.pa[o]
def quote(t,tau,k):  # k=1 bid, 2 ask, ultimo q <= tau con edad<=30s; descarta cruzados ya al cargar
    a=t.qa[:,0]; i=np.searchsorted(a,tau,side='right')-1
    if i<0 or tau-a[i]>30000: return None
    v=t.qa[i,k]; return None if v!=v else v
def eqprints(A,B):  # compras equivalentes de A: BUY A a p ; SELL B a p -> 1-p
    ta=A.pa; tb=B.pa
    m1=ta[:,2]==1; m2=tb[:,2]==0
    t=np.concatenate([ta[m1,0],tb[m2,0]]); p=np.concatenate([ta[m1,1],1-tb[m2,1]])
    o=np.argsort(t,kind='stable'); return t[o],p[o]
def first(t,p,tp,g,strict=True):
    i=np.searchsorted(t,tp,side='left')
    if i>=len(t): return None
    m=(p[i:]>g+E) if strict else (p[i:]>=g-E)
    j=np.argmax(m)
    return t[i+j] if m[j] else None
def evalleg(A,B,cie,t1,p0,sh,win,entry_cost,entry_reb,kind,row):
    tp=t1+LX; tend=cie*1000-2000; tdump=cie*1000-30000
    te,pe=eqprints(A,B)
    bd=quote(A,tdump+LT,1)   # bid al vender (tomador)
    hold=sh*win
    dump=None if bd is None else sh*bd-sh*fee(bd)
    row['pnl_base_H']=hold-entry_cost+entry_reb
    row['pnl_base_D']=(dump if dump is not None else hold)-entry_cost+entry_reb
    for i,d in enumerate(D):
        g=c2(p0+d)
        if g>0.99+1e-9 or sh<5-1e-9:
            for T in 'HDC': row['pnl_s%d_%s'%(i,T)]=''
            row['tf_s%d'%i]=''; row['tfge_s%d'%i]=''; row['g_s%d'%i]=''; continue
        tf=first(te,pe,tp,g,True); tfge=first(te,pe,tp,g,False)
        row['g_s%d'%i]=g; row['tf_s%d'%i]=1 if (tf is not None and tf<=tend) else 0
        row['tfge_s%d'%i]=1 if (tfge is not None and tfge<=tend) else 0
        sale=sh*g+0.2*sh*fee(g)
        # H
        hH=sale if (tf is not None and tf<=tend) else hold
        # D
        if tf is not None and tf<=tdump: hD=sale
        else: hD=dump if dump is not None else (sale if (tf is not None and tf<=tend) else hold)
        # C
        if tf is not None and tf<=tdump: hC=sale
        elif bd is not None and bd<p0: hC=dump
        else: hC=hH
        for T,v in (('H',hH),('D',hD),('C',hC)): row['pnl_s%d_%s'%(i,T)]=v-entry_cost+entry_reb
def main(day):
    units=[]
    with gzip.open(BASEU%day,'rt') as f:
        for r in csv.DictReader(f):
            if r['P_sh'] and float(r['P_sh'])>=5-1e-9 and r['P_t1'] not in ('','None'):
                units.append(r)
    mk={}
    for r in units: mk[r['mercado']]=1
    toks={}; byk={}
    with gzip.open(REG%day,'rt') as f:
        next(f)
        for ln in f:
            ty=ln[0]
            if ty=='k':
                c=ln.rstrip('\n').split(',')
                if c[4]=='5min' and c[5] in mk and c[7] in ('YES','NO'):
                    toks[c[2]]=Tok(datetime.datetime.fromisoformat(c[6]).timestamp()); byk[(c[5],c[7])]=c[2]
            elif ty=='q' or ty=='t':
                c0=ln.split(',',3); t=toks.get(c0[2])
                if t is None: continue
                c=ln.rstrip('\n').split(',')
                if ty=='q':
                    rv=c[7].strip(); tm=float(rv) if rv else float(c[1])
                    try: bb=float(c[3]) if c[3].strip() not in('','None') else float('nan'); ba=float(c[4]) if c[4].strip() not in('','None') else float('nan')
                    except: continue
                    if bb==bb and ba==ba and bb>ba+E: continue
                    if t.cie-320000<=tm<=t.cie+10000: t.q.extend((tm,bb,ba))
                else:
                    rv=c[6].strip(); tm=float(rv) if rv else float(c[1])
                    if t.cie-320000<=tm<=t.cie+10000: t.p.extend((tm,float(c[3]),1.0 if c[4]=='BUY' else 0.0))
    for t in toks.values(): prep(t)
    rows=[]; rng=random.Random(2811)
    for r in units:
        m=r['mercado']; side=r['lado']; oth='NO' if side=='YES' else 'YES'
        w=G.get(str(m))
        if w not in('YES','NO'): continue
        A=toks.get(byk.get((m,side))); B=toks.get(byk.get((m,oth)))
        if A is None or B is None: continue
        cie=float(r['cierre']); sh=float(r['P_sh']); cost=float(r['P_cost']); p0=cost/sh; t1=float(r['P_t1'])
        win=1.0 if w==side else 0.0
        base=dict(dia=day,coin=r['coin'],mercado=m,lado=side,p0=p0,cost=cost,sh=sh,win=win)
        row=dict(base,kind='real'); evalleg(A,B,cie,t1,p0,sh,win,cost,0.2*sh*fee(p0),'real',row); rows.append(row)
        # inversion: complemento al ask en t1+LT
        ak=quote(B,t1+LT,2)
        if ak is not None and 0.01<=ak<0.99:
            c=sh*ak+sh*fee(ak); row=dict(base,kind='inv',p0=ak,cost=c,win=1.0-win); evalleg(B,A,cie,t1+LT,ak,sh,1.0-win,c,0,'inv',row); rows.append(row)
        # placebo: tomador a tiempo aleatorio
        for _ in range(2):
            tau=(cie-rng.uniform(60,290))*1000
            ak=quote(A,tau+LT,2)
            if ak is not None and 0.10<=ak<0.30:
                c=sh*ak+sh*fee(ak); row=dict(base,kind='pla',p0=ak,cost=c); evalleg(A,B,cie,tau+LT,ak,sh,win,c,0,'pla',row); rows.append(row)
    cols=['kind','dia','coin','mercado','lado','p0','cost','sh','win','pnl_base_H','pnl_base_D']
    for i in range(len(D)):
        cols+=['g_s%d'%i,'tf_s%d'%i,'tfge_s%d'%i]+['pnl_s%d_%s'%(i,T) for T in 'HDC']
    with open(OUT%day,'w',newline='') as f:
        w_=csv.DictWriter(f,cols); w_.writeheader()
        for r in rows: w_.writerow({k:r.get(k,'') for k in cols})
    print(day,'unidades',len(units),'filas',len(rows),flush=True)
if __name__=='__main__': main(sys.argv[1])
