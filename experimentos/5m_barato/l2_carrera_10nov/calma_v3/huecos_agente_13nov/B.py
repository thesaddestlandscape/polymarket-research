import sys,glob,numpy as np,pandas as pd
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov')
import chequeo_libro5tx as CK
O='/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov/out/'
days=[f'2026-11-{d:02d}' for d in range(2,13)]
R=[];allf=[]
for d in days:
    d0=int(pd.Timestamp(d,tz='UTC').timestamp()*1000)
    # holes with exact bounds
    parts=[];
    for dd in (pd.Timestamp(d)+pd.Timedelta(days=i) for i in (-1,0,1)):
        for f in glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dd:%Y-%m-%d}_*.csv.gz'):
            try: parts.append(pd.read_csv(f,header=None,usecols=[0,1],names=['t','tk'],dtype={'t':'int64','tk':str},on_bad_lines='skip'))
            except Exception as e: pass
    x=pd.concat(parts);x=x[(x.t>=d0)&(x.t<d0+86400000)];t=np.unique(x.t.values);toks=set(x.tk)
    e=np.concatenate([[d0],t,[d0+86400000]]);g=np.diff(e);ix=np.where(g>60000)[0];H=[(e[i],e[i+1]) for i in ix]
    try:
        oc=pd.read_csv(f'/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz',usecols=['tipo','ts_est','tx','token_id'],dtype={'token_id':str});oc=oc[oc.tipo=='F'];oc['t']=(oc.ts_est*1000).astype('int64')
        ocn=sum(oc[(oc.t>=a)&(oc.t<b)&oc.token_id.isin(toks)].tx.nunique() for a,b in H);ocr=oc[oc.token_id.isin(toks)].tx.nunique()/1440
        dur=sum(b-a for a,b in H)/60000
    except Exception as ex: ocn=ocr=dur=np.nan
    print(d,'huecos',len(H),'min_en_huecos %.1f'%dur,'| onchain tx 5m EN hueco',ocn,'| esperado por ritmo medio %.0f'%(ocr*dur),flush=True)
    for T in ('G0','T1'):pass
    p=pd.read_pickle(O+f'dec2v3_{d}.pkl');p=p[p['var'].isin(['G0','T1'])].copy()
    fl=np.zeros(len(p),bool);
    for a,b in H: fl|=((p.tf.values>=a)&(p.tf.values<b+60000))
    p['near']=fl;p['d']=d;allf.append(p)
    # market windows overlapping hole (fin seconds)
    print('   fin check: fin%300==0 ->',(p.fin%300==0).mean(),' T=(fin*1000-tf)/1000 ok->',np.allclose((p.fin*1000-p.tf)/1000,p['T'],atol=0.01))
A=pd.concat(allf)
print(A.groupby(['var','near']).agg(n=('pnl','size'),pnl=('pnl','sum'),cost=('cost','sum')).assign(EV=lambda z:z.pnl/z.cost))
tab=A.groupby(['d','var','near']).pnl.sum().unstack([1,2]).fillna(0);print(tab.round(2))
print('near by day n:',A[A.near].groupby('d').size().to_dict())
# hora: share of T1/G0 fills by hour mod 4 ==3 (bad hours absent)
A['h']=((A.tf//3600000)%24);print('fills por hora (G0):',A[A['var']=='G0'].groupby('h').size().to_dict())
