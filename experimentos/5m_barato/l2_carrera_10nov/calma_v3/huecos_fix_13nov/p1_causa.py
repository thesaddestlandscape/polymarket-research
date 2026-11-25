"""P1: huecos de libro5_tx (>60 s sin ninguna fila) vs q/t de libro5_ms (npz sa_ms) vs onchain F. Solo lectura."""
import glob,json,numpy as np,pandas as pd,sys
N='/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_fix_13nov/'
res={}
for di in range(5,13):
    d=f'2026-11-{di:02d}'; d0=int(pd.Timestamp(d,tz='UTC').timestamp()*1000); d1=d0+86400000
    P=[]
    for dd in (pd.Timestamp(d)+pd.Timedelta(days=i) for i in (-1,0,1)):
        for f in glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dd:%Y-%m-%d}_*.csv.gz'):
            try: P.append(pd.read_csv(f,header=None,usecols=[0,1,3],names=['t','tk','rx'],dtype={'t':'int64','tk':str,'rx':'int64'},on_bad_lines='skip'))
            except Exception as e: print('err',f,e)
    x=pd.concat(P); x=x[(x.rx>=d0)&(x.rx<d1)]; t=np.unique(x.rx.values); toks=set(x.tk)
    e=np.concatenate([[d0],t,[d1]]); g=np.diff(e); ix=np.where(g>60000)[0]; H=[(int(e[i]),int(e[i+1])) for i in ix]
    z=np.load(f'/root/polymarket-research-datalogs/sa_ms/ms_{d}.npz',allow_pickle=True); T0=int(z['t0']); qt=z['q_t'].astype('int64')+T0; tt=z['t_t'].astype('int64')+T0; tok=z['tokens']; tmap=z['tmap']
    fs=sorted(glob.glob(f'/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_{d}*.csv.gz'))
    st=set(tok); ch=[]
    for f in fs:
        for c in pd.read_csv(f,usecols=['tipo','ts_est','tx','token_id','log_index'],dtype={'token_id':str},chunksize=300000):
            ch.append(c[(c.tipo=='F')&c.token_id.isin(st)])
    oc=pd.concat(ch).drop_duplicates(['tx','log_index']); oc['t']=(oc.ts_est*1000).astype('int64'); del ch
    oc5=oc[oc.token_id.isin(set(tok))]
    out=[]
    for a,b in H:
        dur=(b-a)/60000
        nq=int(((qt>=a)&(qt<b)).sum()); nqb=int(((qt>=a-300000)&(qt<a)).sum()); nt=int(((tt>=a)&(tt<b)).sum()); ntb=int(((tt>=a-300000)&(tt<a)).sum())
        # bloque ts es ~2.25 s posterior al casado: desplazar ventana onchain
        o=oc5[(oc5.t>=a+2250)&(oc5.t<b+2250)].tx.nunique()
        out.append(dict(ini=pd.Timestamp(a,unit='ms').strftime('%H:%M:%S'),dur_min=round(dur,2),q_por_min_hueco=round(nq/dur),q_por_min_antes=round(nqb/5),t_por_min_hueco=round(nt/dur,1),t_por_min_antes=round(ntb/5,1),onchain_tx5m_hueco=int(o),onchain_tx5m_por_min=round(o/dur,1)))
    rate=oc5.tx.nunique()/1440
    res[d]=dict(n=len(H),min_total=round(sum(h['dur_min'] for h in out),1),rate_oc_min=round(rate,1),huecos=out)
    print(d,len(H),'huecos',res[d]['min_total'],'min; oc/min medio',round(rate,1),flush=True)
    print('   hueco ini/dur_min/q_min_hueco/q_min_antes/t_min_hueco/t_min_antes/oc_tx5m_min:',[(h['ini'][:5],h['dur_min'],h['q_por_min_hueco'],h['q_por_min_antes'],h['t_por_min_hueco'],h['t_por_min_antes'],h['onchain_tx5m_por_min']) for h in out],flush=True)
json.dump(res,open(N+'out/p1_huecos.json','w'))
