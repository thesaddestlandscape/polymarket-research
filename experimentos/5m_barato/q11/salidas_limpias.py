#!/usr/bin/env python3
"""Q11-SALIDAS paso 1 (extraccion, por DIA, idempotente): markouts post-relleno SIN supervivencia sobre los rellenos dec2 (T1,G0,PLA_T1).
Para cada relleno (dec2_D.pkl) lee el libro del token a tf+h (+250 ms de llegada de una venta tomadora): bid, bid_size; y a T-60/-30/-10 s.
bid ausente/NaN/0 o llegada >= cierre => NO se vende (se mantiene; valor = desenlace oficial 'gana'). Reloj: sa_ms (el mismo de dec2).
Uso: nice -n 19 ionice -c3 python3 -I salidas_limpias.py DIA   (ulimit -v 3000000; fuera de 06:00-09:30Z; ver salidas_limpias_noche.sh)
Salida: out_salidas/sal_DIA.pkl (escritura atomica; si existe -> 'ya hecho')."""
import sys, os, numpy as np, pandas as pd
DESC='/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/'
P2='/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
H=os.path.dirname(os.path.abspath(__file__))+'/'; OUT=H+'out_salidas/'; os.makedirs(OUT,exist_ok=True)
d=sys.argv[1]; LLEG=250
if os.path.exists(OUT+f'sal_{d}.pkl'): print('ya hecho',d); sys.exit(0)
R=pd.read_pickle(DESC+f'out/dec2_{d}.pkl'); R=R[R['var'].isin(['T1','G0','PLA_T1'])].reset_index(drop=True)
sys.path.insert(0,P2+'escalera_B'); import engine as G
import json
PB=P2+'precursores_barrido/out/'
tape=pd.read_pickle(PB+f'tape_{d}.pkl'); bad={tuple(x) for x in json.load(open(PB+f'bad_{d}.json'))['bad']}
E=G.DayEng(d,'chain',tape,bad); D=E.D
HS=[0,1000,5000,15000,30000,60000]; cols={}
def libro(k,t):
    b=D.book(int(k),int(t)); return (np.nan,0.0) if b is None else (b[0],b[2])
for h in HS:
    bd=[];ba=[];sz=[]
    for k,tf in zip(R.k.values,R.tf.values):
        x0=libro(k,tf+h); x1=libro(k,tf+h+LLEG); bd.append(x0[0]); ba.append(x1[0]); sz.append(x1[1])
    cols[f'bd_{h}']=bd; cols[f'ba_{h}']=ba; cols[f'sz_{h}']=sz
for s in (60,30,10):
    bd=[];ba=[];sz=[]
    for k,tf,fin in zip(R.k.values,R.tf.values,R.fin.values):
        t=int(fin)*1000-s*1000
        if t<=tf: bd.append(np.nan);ba.append(np.nan);sz.append(0.0); continue
        x0=libro(k,t); x1=libro(k,t+LLEG); bd.append(x0[0]); ba.append(x1[0]); sz.append(x1[1])
    cols[f'bd_T{s}']=bd; cols[f'ba_T{s}']=ba; cols[f'sz_T{s}']=sz
R=pd.concat([R,pd.DataFrame(cols)],axis=1); R.to_pickle(OUT+f'sal_{d}.pkl.tmp'); os.replace(OUT+f'sal_{d}.pkl.tmp',OUT+f'sal_{d}.pkl'); print('ok',d,len(R))
