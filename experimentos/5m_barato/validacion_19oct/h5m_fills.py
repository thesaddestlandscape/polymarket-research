# Extrae fills maker de la celda H5M (misma lógica que vigia_5m_barato_maker_forward.unidades_dia) conservando ts. Solo lectura.
import sys,gzip,json
import numpy as np,pandas as pd
from datetime import datetime,date,timedelta
SP='/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/'
EXCH="0xe111180000d2663c0091e4f400237545b87b996b"
des=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
def tokmap(d):
    m={}
    for k in (-1,0,1):
        dd=(date.fromisoformat(d)+timedelta(days=k)).isoformat()
        try: fh=open(SP+f'kmap_{dd}.txt')
        except FileNotFoundError: continue
        for ln in fh:
            c=ln.rstrip('\n').split(',')
            if len(c)>=8 and c[4]=='5min': m[c[2]]=(c[3],c[5],int(datetime.fromisoformat(c[6]).timestamp()),c[7])
    return m
d=sys.argv[1]
tok=tokmap(d)
ta={t:v[0] for t,v in tok.items()};tm={t:v[1] for t,v in tok.items()};tf={t:v[2] for t,v in tok.items()};tl={t:v[3] for t,v in tok.items()}
parts=[]
with gzip.open(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz','rt') as fh:
    for x in pd.read_csv(fh,chunksize=150000,dtype={"token_id":str,"tx":str,"maker":str,"taker":str},
        usecols=["tipo","ts_est","tx","log_index","maker","taker","side","token_id","maker_amt","taker_amt"]):
        x=x[(x.tipo=="F")&(x.taker!=EXCH)&x.token_id.isin(tok.keys())]
        if not len(x): continue
        tk=x.token_id;venta=x.side.values==1
        acc=np.where(venta,x.maker_amt.values,x.taker_amt.values).astype(float)
        usdc=np.where(venta,x.taker_amt.values,x.maker_amt.values).astype(float)
        parts.append(pd.DataFrame({"tx":x.tx.values,"li":x.log_index.astype(int).values,"act":tk.map(ta).values,"mkt":tk.map(tm).values,
          "ts":x.ts_est.astype(float).values,"T":tk.map(tf).astype(float).values-x.ts_est.astype(float).values,"lado":tk.map(tl).values,"venta":venta,"acc":acc,"usdc":usdc,"fin":tk.map(tf).astype(float).values}))
X=pd.concat(parts,ignore_index=True);X=X[X.acc>0]
X["lado_c"]=np.where(X.venta,np.where(X.lado=="YES","NO","YES"),X.lado)
X["pc"]=np.where(X.venta,1-X.usdc/X.acc,X.usdc/X.acc)
X["coste"]=np.where(X.venta,X.acc-X.usdc,X.usdc)
X=X[X.coste>0]
C=X[(X.pc>0.10)&(X.pc<=0.30)&(X["T"]>60)&(X["T"]<=300)].copy()
C["des"]=C.mkt.map(des);print(d,'fills',len(C),'cobertura desenlace',C.des.notna().mean())
C=C[C.des.notna()]
C["pnl"]=np.where(C.lado_c==C.des,C.acc,0.0)-C.coste
C["dia"]=d
C.drop(columns=['tx','li','venta','usdc']).to_csv(SP+f'fills_{d}.csv.gz',index=False,compression='gzip')
u=pd.read_csv(f'/root/polymarket-research-datalogs/vigia_5m_barato_maker/unidades_{d}.csv.gz')
print('PNL fills',C.pnl.sum(),'coste',C.coste.sum(),'| cache unidades',u.pnl.sum(),u.coste.sum())
