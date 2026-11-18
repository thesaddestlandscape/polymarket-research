import pandas as pd, numpy as np
H='/tmp/claude-0/-root-polymarket-research/e104a83f-d7c6-451f-be5d-620ce299e16c/scratchpad/'
O=pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv',dtype={'tok':str})
T=pd.read_pickle('/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/tomador_202.pkl')[['oid','causa','estructura']]
O=O.merge(T,on='oid',how='left'); O['cl1']=O.causa.fillna('').str.startswith('1_'); O['solo']=O.estructura.eq('SOLO')
O['tdm']=(O.t_dec*1000).round().astype('int64')
out=[]
for d,g in O.groupby('dia'):
    X=pd.read_csv(H+f'x_{d}.csv',header=None,names=['t','T','sym','p','q','m','E','rx'],usecols=[2,3,7],dtype={'sym':str}).rename(columns={})
    X=X[['sym','p','rx']] if 'sym' in X else X
    Q=pd.read_csv(H+f'q_{d}.csv',header=None,names=['t','T','tok','bid','ask','bsz','asz','rx'],dtype={'tok':str}).sort_values('rx')
    px={}
    for s,gg in X.groupby('sym'): gg=gg.sort_values('rx'); px[s[:-4].lower()]=(gg.rx.values,gg.p.values)
    g=g.copy()
    for k,dt in (('p0',0),('p5',5000),('p30',30000)):
        v=np.full(len(g),np.nan)
        for c in g.coin.unique():
            m=(g.coin==c).values; rx,p=px[c]; i=np.searchsorted(rx,g.tdm.values[m]-dt,side='right')-1
            ok=i>=0; vv=np.full(m.sum(),np.nan); vv[ok]=p[i[ok]]; 
            # no usar precio con rx mas de 5s anterior al corte
            stale=np.zeros(m.sum(),bool); stale[ok]=(g.tdm.values[m]-dt-rx[i[ok]])>5000; vv[stale]=np.nan
            v[m]=vv
        g[k]=v
    # apertura de la ventana
    g['ep']=g.slug.str.rsplit('-',n=1).str[1].astype('int64')*1000
    v=np.full(len(g),np.nan)
    for c in g.coin.unique():
        m=(g.coin==c).values; rx,p=px[c]; i=np.searchsorted(rx,g.ep.values[m],side='right')-1; v[m]=p[np.clip(i,0,None)]
    g['popen']=v
    sg=np.where(g.lado=='YES',1.0,-1.0)
    g['r5']=sg*(g.p0/g.p5-1)*1e4; g['r30']=sg*(g.p0/g.p30-1)*1e4; g['dist']=sg*(g.p0/g.popen-1)*1e4
    # verificacion L1: bid vigente en t_dec (rx<=t_dec) vs bb; bid en t_dec+post_ms+1s
    Qd={t:gg for t,gg in Q.groupby('tok')}
    bb0=[];bb1=[];bs0=[]
    for tok,td,pm in zip(g.tok,g.tdm,g.post_ms):
        q=Qd.get(tok)
        if q is None: bb0.append(np.nan);bb1.append(np.nan);bs0.append(np.nan);continue
        rx=q.rx.values; i=np.searchsorted(rx,td,side='right')-1; j=np.searchsorted(rx,td+pm+1500,side='right')-1
        bb0.append(q.bid.values[i] if i>=0 else np.nan); bs0.append(q.bsz.values[i] if i>=0 else np.nan); bb1.append(q.bid.values[j] if j>=0 else np.nan)
    g['bb_L1_tdec']=bb0; g['bb_L1_post']=bb1; g['bs_L1_tdec']=bs0
    out.append(g)
O=pd.concat(out); O.to_pickle(H+'O_feat.pkl')
print('bb==L1(t_dec):',(abs(O.bb-O.bb_L1_tdec)<1e-6).mean(), ' bb==L1(t_dec+post+1.5s):',(abs(O.bb-O.bb_L1_post)<1e-6).mean(),' L1 NaN:',O.bb_L1_tdec.isna().mean())
print('bs==L1 bsz:',(abs(O.bs-O.bs_L1_tdec)<0.01).mean())
print(O[['r5','r30','dist']].describe().T)
print('NaN r5',O.r5.isna().mean())
