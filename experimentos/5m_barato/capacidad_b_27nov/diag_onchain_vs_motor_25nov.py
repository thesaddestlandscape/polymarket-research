import sys, gzip, glob, pickle
sys.dont_write_bytecode=True
import pandas as pd, numpy as np
dia='2026-11-25'
O='/root/polymarket-research-datalogs/capacidad_b_27nov/'
R=pd.read_pickle(O+f'ordenes_K6_base_{dia}_enriquecido.pkl').reset_index(drop=True)
sel=R[(R.q>0)|(R.qc0_5>0)].copy()
toks=set(sel.token)
rec={}
for f in sorted(glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dia}_*.csv.gz')):
    for ln in gzip.open(f,'rt'):
        c=ln.rstrip('\n').split(',')
        if len(c)>=4:
            t=int(c[3]); 
            if c[2] not in rec or t<rec[c[2]]: rec[c[2]]=t
ev=[]
for ch in pd.read_csv(f'/root/polymarket-research-datalogs/onchain_fills_{dia}.csv.gz',usecols=['tipo','tx','log_index','token_id','maker','side','maker_amt','taker_amt'],dtype=object,chunksize=500000):
    ch=ch[(ch.tipo=='F')&ch.token_id.isin(toks)&(ch.side=='0')]
    for r in ch.itertuples():
        ma,ta=float(r.maker_amt),float(r.taker_amt)
        if ta>0: ev.append((r.token_id,rec.get(r.tx),ma/ta,ta,r.tx[:8],int(r.log_index)))
E=pd.DataFrame(ev,columns=['token','rx','price','qty','tx','li']); E['rx']=E.rx.astype(float)
print('chain maker-BUY rows en tokens sel:',len(E),'sin reloj',E.rx.isna().sum())
for i,r in sel.iterrows():
    e=E[(E.token==r.token)&(E.rx>=r.t_arr-300)&(E.rx<=r.t_end+300)&(E.price<=r.L+0.0006)]
    print(f"#{i} {r.coin} {r.lado} L={r.L} ahead={r.ahead_0} bid0={r.bid_0} win=[{r.t_end-r.t_arr}ms] motor_q={r.q} fifoT_q5={r.qc0_5} flujoSELL={r.flujo_L_misma_ficha_SELL:.1f} espBUY={r.flujo_L_espejo_BUY:.1f} bajo={r.flujo_debajo:.1f}")
    for x in e.itertuples(): print(f"     chain rx-t_arr={int(x.rx-r.t_arr):+d}ms (t_end {int(x.rx-r.t_end):+d}) price={x.price:.3f} qty={x.qty:.1f} tx={x.tx} li={x.li}")
