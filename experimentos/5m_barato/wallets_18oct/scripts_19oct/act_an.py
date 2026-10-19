import json, glob, pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/act/'
pd.set_option('display.width',250)
for f in sorted(glob.glob(SP+'act_*.json')):
    d=f[-15:-5]; A=pd.DataFrame(json.load(open(f)))
    A['tipo_m']=A.slug.str.extract(r'^([a-z]+)-updown-(\w+?)-')[0]+'-'+A.slug.str.extract(r'^([a-z]+)-updown-(\w+?)-')[1]
    A.loc[A.tipo_m.isna(),'tipo_m']='otro:'+A.slug.str[:20]
    T=A[A.type=='TRADE']
    vol=T.groupby('tipo_m').usdcSize.sum()
    print(f'\n===== {d}  filas {len(A)}  TRADE {len(T)}  tipos {A.type.value_counts().to_dict()}')
    print('  volumen TRADE por mercado:',(vol/vol.sum()).round(3).to_dict(),' total $',round(vol.sum()))
    print('  BUY/SELL $:',T.groupby('side').usdcSize.sum().round(0).to_dict(),'| MERGE $',round(A[A.type=='MERGE'].usdcSize.sum()),'| REDEEM $',round(A[A.type=='REDEEM'].usdcSize.sum()))
    # por mercado
    T=T.assign(up=(T.outcomeIndex==0))
    g=T[T.side=='BUY'].groupby(['conditionId','up']).agg(q=('size','sum'),c=('usdcSize','sum')).unstack(fill_value=0)
    g.columns=[f'{a}_{"up" if b else "dn"}' for a,b in g.columns]
    for k in ['q_up','q_dn','c_up','c_dn']:
        if k not in g: g[k]=0.0
    par=np.minimum(g.q_up,g.q_dn); res=(g.q_up-g.q_dn).abs()
    cp=(g.c_up/g.q_up.replace(0,np.nan)+g.c_dn/g.q_dn.replace(0,np.nan))
    print(f'  mercados {len(g)} | con ambos lados {(par>0).mean():.3f} | acc par {par.sum():.0f} vs residuales {res.sum():.0f} (ratio res/par {res.sum()/max(par.sum(),1):.2f}) | coste medio del par {np.nansum(cp*par)/par[cp.notna()].sum():.4f} | mediana equilibrio {(par/np.maximum(g.q_up,g.q_dn)).median():.3f}')
    b=T[T.side=='BUY']; print('  precio de compra (pond $): p10/p50/p90', np.round(np.quantile(np.repeat(b.price.values, np.maximum(1,(b.usdcSize.values).astype(int))) ,[.1,.5,.9]),3), ' tamaño mediano acc',b['size'].median())
    # PnL de caja del dia por mercado (merge+redeem+sell-buy); solo mercados con REDEEM o MERGE dentro del dia
    cf=A.assign(s=np.where(A.type=='TRADE',np.where(A.side=='BUY',-A.usdcSize,A.usdcSize),np.where(A.type.isin(['MERGE','REDEEM']),A.usdcSize,0)))
    print('  caja neta del dia (merge+redeem+ventas-compras) $',round(cf.s.sum()),' (aprox. del PnL del dia, sin cruzar medianoche)')
