#!/usr/bin/env python3
"""s2: por dia D, tabla de ordenes TOMADORAS (TK) y rellenos MAKER en banda (MK) de mercados 5m BTC/ETH/SOL/XRP desde VOL/m5_onchain.
Mapa token desde filas k de VOL/m5_registro_D (marco 5min/15min). Todo en 'compra del lado L a pc' (venta de s = compra de no-s a 1-p).
Uso: s2_onchain.py D [D...]. Salida datos/tk_D.parquet, mk_D.parquet, tok_D.json. Solo lectura."""
import sys, subprocess, json, numpy as np, pandas as pd
OUT='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'; COINS={'BTC','ETH','SOL','XRP'}
for D in sys.argv[1:]:
    p=subprocess.Popen(f"zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_{D}.csv.gz | grep '^k,'",shell=True,stdout=subprocess.PIPE,text=True)
    tok={}
    for l in p.stdout:
        c=l.rstrip('\n').split(',')
        if len(c)>=8 and c[3] in COINS and c[4] in ('5min','15min'):
            cie=int(pd.Timestamp(c[6]).timestamp()); tok[c[2]]=(c[3],c[4],c[5],cie,c[7])
    p.wait(); json.dump(tok,open(OUT+f'tok_{D}.json','w'))
    t5={k:v for k,v in tok.items() if v[1]=='5min'}
    TK=[];MK=[]
    for ch in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{D}.csv.gz',dtype={'token_id':str},
                          usecols=['tipo','bloque','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt','fee'],chunksize=1_000_000):
        ch=ch[(ch.tipo=='F')&ch.token_id.isin(t5.keys())].copy()
        if not len(ch): continue
        info=ch.token_id.map(t5)
        ch['coin']=info.str[0]; ch['mkt']=info.str[2]; ch['cierre']=info.str[3]; ch['out']=info.str[4]
        buy=ch.side.values==0
        sh=np.where(buy,ch.taker_amt,ch.maker_amt); usd=np.where(buy,ch.maker_amt,ch.taker_amt)
        ok=sh>0; ch=ch[ok]; sh=sh[ok]; usd=usd[ok]; buy=buy[ok]
        p_=usd/sh; ch['L']=np.where(buy,ch.out,np.where(ch.out=='YES','NO','YES')); ch['pc']=np.where(buy,p_,1-p_)
        ch['acc']=sh; ch['maker']=ch.maker.str.lower(); ch['taker']=ch.taker.str.lower()
        ch['venta']=~buy
        cols=['bloque','ts_est','tx','log_index','maker','coin','mkt','cierre','L','pc','acc','venta','fee']
        tk=ch[ch.taker==EXCH][cols].rename(columns={'maker':'wallet'})
        mk=ch[(ch.taker!=EXCH)&(ch.pc>=0.03)&(ch.pc<=0.40)][cols+['taker']]
        TK.append(tk); MK.append(mk)
    TK=pd.concat(TK); MK=pd.concat(MK)
    for X in (TK,MK):
        for c in ('coin','L'): X[c]=X[c].astype('category')
    TK.to_parquet(OUT+f'tk_{D}.parquet'); MK.to_parquet(OUT+f'mk_{D}.parquet')
    print(D,'tokens',len(tok),'TK',len(TK),'MK banda',len(MK),flush=True)
