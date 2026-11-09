#!/usr/bin/env python3
"""s3: por dia D extrae de VOL/m5_registro_D (solo lectura) series compactas para rasgos, POR MONEDA (memoria acotada):
 q (top: tok, ex, rx=RECEPCION, bid, ask, bsz, asz) de tokens 5m/15m; t (prints WS: tok, ex, rx, p, buy, sz); x (aggTrade Binance: sym, ex, rx=c[7], p, qty, m).
 Tiempos int32 ms relativos a BASE = D-1 00:00Z. Escribe temporales binarios por moneda y luego reg_D_<COIN>.npz ordenado por (tok, rx)."""
import sys, os, json, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
OUT='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
SYM={'BTCUSDT':0,'ETHUSDT':1,'SOLUSDT':2,'XRPUSDT':3}; COINS=['BTC','ETH','SOL','XRP']
QF=[('tok',np.int16),('ex',np.int32),('rx',np.int32),('bid',np.float32),('ask',np.float32),('bsz',np.float32),('asz',np.float32)]
def num(v):
    try: return np.asarray(v,dtype=np.float64)
    except (ValueError,TypeError):
        o=np.empty(len(v))
        for i,z in enumerate(v):
            try: o[i]=float(z)
            except (ValueError,TypeError): o[i]=np.nan
        return o
for D in sys.argv[1:]:
    BASE=int(pd.Timestamp(D,tz='UTC').timestamp()*1000)-86400000
    tok=json.load(open(OUT+f'tok_{D}.json')); tl=sorted(tok); ti={k:i for i,k in enumerate(tl)}
    coin_of=np.array([COINS.index(tok[k][0]) for k in tl],dtype=np.int8)
    tmp=OUT+f'tmp_{D}/'; os.makedirs(tmp,exist_ok=True)
    fh={(c,f):open(tmp+f'q_{c}_{f}.bin','wb') for c in COINS for f,_ in QF}
    T=[];X=[]
    rel=lambda v: np.nan_to_num(num(v)-BASE,nan=-1).astype(np.int32)
    for ch in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{D}.csv.gz',header=0,names=['tipo','t','id','c1','c2','c3','c4','c5'],
                          dtype=object,chunksize=1_000_000,on_bad_lines='skip'):
        tp=ch.tipo.values; idv=ch.id.values
        m=(tp=='q'); q=ch[m]; ids=q.id.values; tki=np.array([ti.get(z,-1) for z in ids],dtype=np.int32); k=tki>=0
        if k.any():
            q=q[k]; tki=tki[k].astype(np.int16)
            cols={'tok':tki,'ex':rel(q.t.values),'rx':rel(q.c5.values),'bid':num(q.c1.values).astype(np.float32),'ask':num(q.c2.values).astype(np.float32),
                  'bsz':num(q.c3.values).astype(np.float32),'asz':num(q.c4.values).astype(np.float32)}
            co=coin_of[tki]
            for ci,c in enumerate(COINS):
                if c=='BTC': continue
                mm=co==ci
                if mm.any():
                    for f,dt in QF: cols[f][mm].astype(dt).tofile(fh[(c,f)])
        t=ch[tp=='t']; tki=np.array([ti.get(z,-1) for z in t.id.values],dtype=np.int32); k=tki>=0
        if k.any():
            t=t[k]; T.append((tki[k].astype(np.int16),rel(t.t.values),rel(t.c4.values),num(t.c1.values).astype(np.float32),(t.c2.values=='BUY').astype(np.int8),num(t.c3.values).astype(np.float32)))
        x=ch[tp=='x']; sy=np.array([SYM.get(z,-1) for z in x.id.values],dtype=np.int8); k=sy>=0
        if k.any():
            x=x[k]; X.append((sy[k],rel(x.t.values),rel(x.c5.values),num(x.c1.values),num(x.c2.values).astype(np.float32),np.isin(x.c3.astype(str).str.lower().values,['1','true']).astype(np.int8)))
        del ch
    for f in fh.values(): f.close()
    out={'BASE':np.array([BASE]),'tok':np.array(tl)}
    for k,cols,L in (('t',['tok','ex','rx','p','buy','sz'],T),('x',['sym','ex','rx','p','qty','m'],X)):
        arrs=[np.concatenate([a[i] for a in L]) for i in range(len(cols))]; o=np.lexsort((arrs[2],arrs[0]))
        for nm,a in zip(cols,arrs): out[f'{k}_{nm}']=a[o]
    np.savez(OUT+f'reg_{D}_tx.npz',**out); nq={}
    for c in COINS:
        if c=='BTC':
            for f,_ in QF: os.remove(tmp+f'q_{c}_{f}.bin')
            continue
        a={f:np.fromfile(tmp+f'q_{c}_{f}.bin',dtype=dt) for f,dt in QF}
        o=np.lexsort((a['rx'],a['tok'])); np.savez(OUT+f'reg_{D}_{c}.npz',**{f'q_{f}':a[f][o] for f,_ in QF}); nq[c]=len(o); del a,o
        for f,_ in QF: os.remove(tmp+f'q_{c}_{f}.bin')
    os.rmdir(tmp)
    print(D,'q',nq,'t',len(out['t_tok']),'x',len(out['x_sym']),flush=True)
