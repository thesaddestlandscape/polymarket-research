#!/usr/bin/env python3
"""a4 POST-HOC: nivel de fill, BTC, dias 16 y 20-Oct: (i) identidad suma cero M+T (sin fee), (ii) EV maker por banda x segundo desde apertura x orden de llegada en el token. nice 19."""
import pandas as pd,numpy as np,json,sys
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f1_huella_cohorte/datos/'
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
TOK={t:v for t,v in json.load(open('/root/polymarket-research-datalogs/mapa_escala/tokens.json')).items() if v[1]=='5min' and v[0]=='BTC'}
DES=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json'))
out=open(D+'a4_resultados.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n')
pd.set_option('display.width',250)
EDG=[0,0.05,0.10,0.20,0.30,0.50,0.70,0.90,1.0]; BN=['<.05','.05-.10','.10-.20','.20-.30','.30-.50','.50-.70','.70-.90','>=.90']
for d in sys.argv[1:]:
    parts=[]
    for x in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',usecols=['tipo','ts_est','tx','log_index','maker','taker','side','token_id','maker_amt','taker_amt','fee'],dtype={'token_id':str,'tx':str,'maker':str,'taker':str},chunksize=500000):
        x=x[(x.tipo=='F')&x.token_id.isin(TOK)]
        if len(x)==0: continue
        tk=x.token_id.values; mid=np.array([TOK[t][2] for t in tk]); fin=np.array([TOK[t][3] for t in tk]); lado=np.array([TOK[t][4] for t in tk])
        v=x.side.values==1; acc=np.where(v,x.maker_amt.values,x.taker_amt.values).astype(float); us=np.where(v,x.taker_amt.values,x.maker_amt.values).astype(float)
        lc=np.where(v,np.where(lado=='YES','NO','YES'),lado)
        with np.errstate(all='ignore'): pc=np.where(v,1-us/acc,us/acc); co=np.where(v,acc-us,us)
        parts.append(pd.DataFrame(dict(mid=mid,lc=lc,pc=pc,co=co,acc=acc,ts=x.ts_est.values.astype(float),fin=fin,M=(x.taker.values!=EXCH),fee=x.fee.fillna(0).values,tx=x.tx.values,li=x.log_index.values,mk=x.maker.values)))
    X=pd.concat(parts,ignore_index=True).drop_duplicates(['tx','li']); X=X[(X.acc>0)&(X.co>0)&(X.pc>=0.01)&(X.pc<0.99)]
    X['des']=X.mid.map(DES); X=X[X.des.notna()].copy(); X['pnl']=X.acc*(X.lc==X.des)-X.co
    P(d,'fills',len(X),'| identidad: Σpnl(sin fee) M %.1f  T %.1f  total %.1f  (coste M %.0f T %.0f)'%(X[X.M].pnl.sum(),X[~X.M].pnl.sum(),X.pnl.sum(),X[X.M].co.sum(),X[~X.M].co.sum()))
    Tb=X[~X.M].copy(); Tb['b']=np.clip(np.digitize(Tb.pc,EDG)-1,0,7); P('  TOMADOR por banda (sin fee): ',{BN[k]:(round(g.pnl.sum()/g.co.sum(),3),int(g.co.sum())) for k,g in Tb.groupby('b')})
    M=X[X.M].copy(); M['b']=np.clip(np.digitize(M.pc,EDG)-1,0,7); M['sec']=300-(M.fin-M.ts); M['sb']=np.digitize(M.sec,[0,10,30,60,120,200,250,300.1])-1
    M=M.sort_values('ts'); M['orden']=M.groupby(['mid','lc']).cumcount()+1; M['ob']=np.digitize(M.orden,[1,2,4,11,31])-1
    P('  MAKER EV (Σpnl/Σco) por banda x segundo desde apertura [0-10,10-30,30-60,60-120,120-200,200-250,250-300]:')
    t=M.groupby(['b','sb']).apply(lambda g: pd.Series(dict(EV=g.pnl.sum()/g.co.sum(),co=g.co.sum()))).unstack('sb'); t.index=[BN[i] for i in t.index]; P(t['EV'].round(3).to_string()); P(' coste (miles €):'); P((t['co']/1000).round(0).to_string())
    P('  MAKER EV banda .70-.90 y .05-.30 por orden de llegada al token-lado (1,2-3,4-10,11-30,31+):')
    for bs_,lab in [([6],'.70-.90'),([1,2,3],'.05-.30'),([5],'.50-.70')]:
        g=M[M.b.isin(bs_)].groupby('ob').apply(lambda z: pd.Series(dict(EV=z.pnl.sum()/z.co.sum(),co=z.co.sum(),n=len(z)))); P(lab); P(g.round(3).to_string())
    g=M[M.b==6].copy(); g['tam']=np.digitize(g.acc,[5,10,20,50,100]); r=g.groupby('tam').apply(lambda z: pd.Series(dict(EV=z.pnl.sum()/z.co.sum(),co=z.co.sum()))); P('  .70-.90 por tamano de fill (acc <5,5-10,10-20,20-50,50-100,100+):'); P(r.round(3).to_string())
