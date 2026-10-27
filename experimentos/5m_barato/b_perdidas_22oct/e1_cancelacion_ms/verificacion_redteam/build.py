# red team: construir rellenos y ventanas desde la extraccion propia del crudo
import gzip, json, glob, os, sys, numpy as np, pandas as pd
S='/tmp/claude-0/-root-polymarket-research/f534e0ad-d7ec-4661-9bed-0375a481e712/scratchpad'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
for f in ['/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/salida/datos/desenlaces_extra.json','/root/polymarket-research-datalogs/e1_cancelacion_ms/desenlaces_e1d.json']:
    if os.path.exists(f): DES.update(json.load(open(f)))
K={}; T=[]; X={}; NBAD=0
for fn in sorted(glob.glob(S+'/raw/2026-10-*.txt.gz')):
    for line in gzip.open(fn,'rt'):
        c=line.rstrip('\n').split(',')
        if c[0]=="t":
            if c[5]=="": NBAD+=1; continue
            T.append((c[1],float(c[2]),c[3],float(c[4]),int(c[5]),int(c[6])))
        elif c[0]=='k': K[c[1]]=(c[2],c[3],int(pd.Timestamp(c[4]).timestamp()),c[5])
        elif c[0]=='x':
            k=(c[1][:3],int(c[2])); r=int(float(c[4]))
            if k not in X or r>X[k][1]: X[k]=(float(c[3]),r)
print('NBAD',NBAD); print('K',len(K),'T',len(T),'X',len(X))
T=pd.DataFrame(T,columns=['tok','p','side','sz','r','te']); n0=len(T); T=T.drop_duplicates(); print('dup',n0-len(T))
T=T[T.tok.isin(K)]
OPP={(v[1],v[3]):t for t,v in K.items()}
T['coin']=T.tok.map(lambda t:K[t][0]); T['mid']=T.tok.map(lambda t:K[t][1]); T['fin']=T.tok.map(lambda t:K[t][2]); lab=T.tok.map(lambda t:K[t][3])
T['lado']=np.where(T.side=='SELL',lab,np.where(lab=='YES','NO','YES'))
T['q']=np.where(T.side=='SELL',T.p,1-T.p).round(4)
# comprobar que fin es el cierre: actividad relativa
rel=(T.r/1000-T.fin); print('r-fin percentiles',np.percentile(rel,[1,5,50,95,99]).round(1))
F=T[(T.r/1000>=T.fin-300)&(T.r/1000<T.fin)].copy()
F['out']=F.mid.map(DES); print('fills ventana',len(F),'sin desenlace',F.out.isna().sum(), 'mids sin des',F[F.out.isna()].mid.nunique())
F=F[F.out.notna()]
F['gana']=(F.out==F.lado).astype(float); F['pnl']=F.sz*(F.gana-F.q); F['coste']=F.sz*F.q
F['dia']=pd.to_datetime(F.fin,unit='s').dt.strftime('%Y-%m-%d')
F.to_pickle(S+'/F.pkl')
# grid Binance
G={}
for (co,b),(p,r) in X.items(): G.setdefault(co,{})[b]=p
pd.to_pickle(G,S+'/G.pkl')
W=F.groupby(['coin','mid']).agg(fin=('fin','first'),pnl=('pnl','sum'),coste=('coste','sum'),n=('pnl','size')).reset_index()
# ventanas sin rellenos tambien (con desenlace)
allm={(v[0],v[1]):v[2] for v in K.values()}
W2=pd.DataFrame([(c,m,f) for (c,m),f in allm.items() if m in DES],columns=['coin','mid','fin'])
W=W2.merge(W.drop(columns='fin'),on=['coin','mid'],how='left').fillna({'pnl':0,'coste':0,'n':0})
W['dia']=pd.to_datetime(W.fin,unit='s').dt.strftime('%Y-%m-%d')
W.to_pickle(S+'/W.pkl'); print('ventanas',len(W)); print(F.groupby('dia').agg(n=('pnl','size'),pnl=('pnl','sum'),coste=('coste','sum')).round(0).to_string())
