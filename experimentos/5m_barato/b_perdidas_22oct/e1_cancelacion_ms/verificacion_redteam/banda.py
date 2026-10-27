import sys, pandas as pd, numpy as np
EX='0xe111180000d2663c0091e4f400237545b87b996b'
def run(f):
    rows=[]
    for x in pd.read_csv(f,usecols=['tipo','ts_est','tx','log_index','taker','side','token_id','maker_amt','taker_amt'],dtype={'token_id':str,'tx':str,'taker':str},chunksize=500000):
        x=x[(x.tipo=='F')&(x.taker!=EX)]
        v=x.side.values==1
        acc=np.where(v,x.maker_amt.values,x.taker_amt.values).astype(float); usdc=np.where(v,x.taker_amt.values,x.maker_amt.values).astype(float)
        with np.errstate(all='ignore'): pc=np.where(v,1-usdc/acc,usdc/acc)
        rows.append(pd.DataFrame(dict(tx=x.tx.values,li=x.log_index.values,tok=x.token_id.values,pc=pc,usd=np.where(v,acc-usdc,usdc))))
    X=pd.concat(rows).drop_duplicates(['tx','li'])
    b=X[(X.pc>=0)&(X.pc<0.10)]; b1=b[b.pc<0.05]
    return dict(fills=len(X),tok=X.tok.nunique(),b010=len(b),b010_tok=b.tok.nunique(),b010_usd=round(b.usd.sum(),0),b005=len(b1),b0510=len(b)-len(b1),pc_nan=int(X.pc.isna().sum()),pc_out=int(((X.pc<0)|(X.pc>1)).sum()))
for a in sys.argv[1:]:
    m,f=a.split('=',1); print(m,run(f),flush=True)
