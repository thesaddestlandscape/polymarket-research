import pandas as pd, numpy as np, glob, json, sys
O=pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv').sort_values(['puja','t_dec'])
pf=O.groupby('puja').fill.max(); n_pf=O.groupby('puja').size(); O['life_dec']=O.t_cancel_int-O.t_dec
print('REAL (20-23 Oct) ord/puja',round(n_pf.mean(),1),'| sin relleno',round(n_pf[pf==0].mean(),1),'| vida mediana t_dec->cancel',round(O.life_dec.median(),2),'| L medio',round(O.precio.mean(),3),'| cierre-cancel->siguiente mediana',1.73)
for d in sorted(glob.glob('out_sim/*/ordenes_'+(sys.argv[1] if len(sys.argv)>1 else '2026-11-04')+'.pkl')):
    R=pd.read_pickle(d).sort_values(['mid','t_dec']); P=json.load(open(d.replace('ordenes_','manifest_').replace('.pkl','.json')))['params']
    R['life']=(R.t_cancel_dec-R.t_dec)/1000; pq=R.groupby('mid').q.max(); g=R.groupby('mid').size(); R['gap']=(R.t_dec-R.groupby('mid').t_cancel_dec.shift())/1000
    print(d.split('/')[1], {k:P.get(k) for k in ['dec_rx','post_block','canc_block','settle_extra','tick']}, 'ord/mercado',round(g.mean(),1),'sin relleno',round(g[pq==0].mean(),1),'vida med',round(R.life.median(),2),'gap med',round(R.gap.median(),2),'L',round(R.L.mean(),3),'n',len(R),'cierres_tick',int((R.motivo_fin=='tick_cambiado').sum()))
