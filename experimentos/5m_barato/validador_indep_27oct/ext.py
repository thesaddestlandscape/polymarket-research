# Extraccion independiente (validador 27-Oct). Lee m5_registro crudo. No reutiliza codigo del medidor.
import gzip, sys, pickle, subprocess, json, time
from array import array
from collections import defaultdict
REG='/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
OUT=sys.argv[1]
SYMS={'BTCUSDT','ETHUSDT','SOLUSDT','XRPUSDT','DOGEUSDT','BNBUSDT'}
res={}
t0=time.time()
# x de 24 y 25 via grep
for D in ('2026-10-24','2026-10-25'):
    xs=defaultdict(lambda:(array('d'),array('d')))
    p=subprocess.Popen("zcat %s | grep '^x,'"%(REG%D),shell=True,stdout=subprocess.PIPE,text=True)
    for ln in p.stdout:
        c=ln.rstrip('\n').split(',')
        if c[2] in SYMS:
            a=xs[c[2]]; a[0].append(float(c[7])); a[1].append(float(c[3]))
    res['x_'+D]={k:v for k,v in xs.items()}
    print(D,'x',{k:len(v[0]) for k,v in xs.items()},round(time.time()-t0),flush=True)
# 26 completo
D='2026-10-26'
xs=defaultdict(lambda:(array('d'),array('d')))
tok={}            # token -> (market, coin, side, cierre_s)
other={}          # (market,side)->token
lastq={}          # token -> (recv, ba, as)
pend=defaultdict(list)  # token -> list of [unit dict]
seenS=set(); seenP=set(); units=[]
tsample=[]        # t rows 5min para cruce on-chain (primeras 3 h)
ini=None
def fl(x):
    return None if x in ('None','') else float(x)
def tb_of(T):
    for lo in (20,60,120,180,240):
        if lo<=T<lo+60: return lo
    return None
with gzip.open(REG%D,'rt') as f:
    next(f)
    for ln in f:
        ty=ln[0]
        if ty=='x':
            c=ln.rstrip('\n').split(',')
            if c[2] in SYMS:
                a=xs[c[2]]; a[0].append(float(c[7])); a[1].append(float(c[3]))
            continue
        c=ln.rstrip('\n').split(',')
        if ty=='k':
            if c[4]!='5min' or c[2] in tok: continue
            # c[6] inicio ventana; cierre = inicio+300
            import datetime
            st=datetime.datetime.fromisoformat(c[6]).timestamp()
            tok[c[2]]=(c[5],c[3],c[7],int(st))  # c[6]=FIN de ventana (verificado)
            other[(c[5],c[7])]=c[2]
        elif ty=='q':
            k=c[2]
            if k not in tok: continue
            recv=float(c[7]); bb=fl(c[3]); ba=fl(c[4]); as_=fl(c[6]) or 0.0
            val=(bb is not None and ba is not None and bb<ba)
            if ini is None: ini=recv
            # actualizar pendientes de este token (estado <= deadline)
            pl=pend.get(k)
            if pl:
                keep=[]
                for u in pl:
                    if recv<=u['dl']:
                        if val: u['snap']=(recv,ba,as_)
                        keep.append(u)
                pend[k]=keep
            if val:
                lastq[k]=(recv,ba,as_)
                m,coin,side,cie=tok[k]
                T=(cie*1000-recv)/1000.0
                tb=tb_of(T)
                if tb is not None and 0.70<=ba<=0.90 and (m,side,tb) not in seenP:
                    seenP.add((m,side,tb))
                    u={'tipo':'P','m':m,'coin':coin,'lado':side,'cie':cie,'td':recv,'tb':tb,'dl':recv+250,'snap':(recv,ba,as_)}
                    units.append(u); pend[k].append(u)
        elif ty=='t':
            k=c[2]
            if k not in tok: continue
            recv=float(c[6]); p=float(c[3]); sd=c[4]
            if ini is not None and recv<ini+3*3600*1000: tsample.append((k,p,sd,float(c[5]),recv))
            if sd!='BUY' or not (0.70<=p<=0.90): continue
            m,coin,side,cie=tok[k]
            T=(cie*1000-recv)/1000.0
            tb=tb_of(T)
            if tb is None or (m,side,tb) in seenS: continue
            seenS.add((m,side,tb))
            u={'tipo':'S','m':m,'coin':coin,'lado':side,'cie':cie,'td':recv,'tb':tb,'dl':recv+250,'snap':lastq.get(k),'p':p}
            units.append(u); pend[k].append(u)
for u in units: u.pop('dl',None)
res['x_'+D]={k:v for k,v in xs.items()}
res['units26']=units; res['ini26']=ini
print(D,'units',len(units),'x',{k:len(v[0]) for k,v in xs.items()},round(time.time()-t0),flush=True)
# cruce on-chain primeras 3 h del 26: lado de la fila t vs lado del tomador on-chain
tokset=set(tok)
oc=defaultdict(list)
cnt=defaultdict(int)
with gzip.open('/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_2026-10-26.csv.gz','rt') as f:
    next(f)
    rows=[]
    for ln in f:
        c=ln.rstrip('\n').split(',')
        ts=float(c[2])*1000
        if ts>ini+3*3600*1000+20000: break
        rows.append(c); cnt[c[7]]+=1
EXC=max(cnt,key=cnt.get)
for c in rows:
    if c[7]!=EXC or c[9] not in tokset: continue
    side='BUY' if c[8]=='0' else 'SELL'
    ma,ta=float(c[10]),float(c[11])
    if ta<=0 or ma<=0: continue
    if side=='BUY': px=ma/ta; sz=ta
    else: px=ta/ma; sz=ma
    oc[c[9]].append((float(c[2])*1000,px,sz,side))
agree=dis=nomatch=amb=0
for k,p,sd,sz,recv in tsample:
    cands={s for (ts,px,szo,s) in oc.get(k,()) if abs(ts-recv)<15000 and abs(px-p)<0.006 and abs(szo-sz)<0.02}
    if not cands: nomatch+=1
    elif len(cands)>1: amb+=1
    elif sd in cands: agree+=1
    else: dis+=1
res['onchain']={'EXC':EXC,'t_filas':len(tsample),'acuerdo':agree,'desacuerdo':dis,'sin_match':nomatch,'ambiguo':amb}
print(res['onchain'],round(time.time()-t0),flush=True)
pickle.dump(res,open(OUT,'wb'))
print('FIN',flush=True)
