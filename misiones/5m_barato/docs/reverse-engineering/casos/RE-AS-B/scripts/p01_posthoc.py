#!/usr/bin/env python3
"""POST-HOC (no preregistrado): vpv 24-25 Oct, margen gana-b por (relleno_pes, relleno_opt, barrido) con IC90 por cierre; + conciliación etiquetado B orden vs posición."""
import pandas as pd,numpy as np,json
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
X=pd.concat([pd.read_csv(f'/root/polymarket-research-datalogs/vida_puja_virtual/vpv_2026-10-{d}.csv.gz') for d in ('24','25')])
g=X.mercado.astype(str).map(DES.get); X['gana']=np.where(g.isna(),np.nan,(g==X.lado).astype(float)); X=X[X.gana.notna()].reset_index(drop=True); X['m']=X.gana-X.b
rng=np.random.default_rng(1); cl=X.cierre.unique(); ix={c:np.where(X.cierre.values==c)[0] for c in cl}
B=[np.concatenate([ix[c] for c in rng.choice(cl,len(cl))]) for _ in range(1000)]
for k,gq in X.groupby(['relleno_pes','relleno_opt','barrido']):
    msk=np.zeros(len(X),bool); msk[gq.index]=True
    v=[X.m.values[s][msk[s]].mean() for s in B]
    print('pes,opt,barrido',k,'n=%d m=%+.4f IC90 (%+.4f,%+.4f) por dia %s'%(len(gq),gq.m.mean(),*np.nanpercentile(v,[5,95]),gq.groupby('dia').m.mean().round(4).to_dict()))
E=pd.concat([pd.read_csv(f'/root/polymarket-research-datalogs/etiquetado_pasivo_B/etiquetado_B_2026-10-2{d}.csv.gz') for d in '0123'])
o=E[(E.unidad=='orden')&(E.acc_llena>0)]; p=E[E.unidad=='posicion']
a=o.groupby(['mercado','lado']).agg(acc_o=('acc_llena','sum'),g=('gana_lado','first'),pr=('precio','mean')); b=p.groupby(['mercado','lado']).agg(acc_p=('acc_llena','sum'),pnl_p=('pnl','sum'),c_p=('coste','sum'))
k=a.join(b,how='outer'); print('unidades orden-rellena',a.shape[0],'posiciones',b.shape[0],'solo posicion',int(k.acc_o.isna().sum()),'acc_o=2*acc_p',int((abs(k.acc_o-2*k.acc_p)<1e-6).sum()))
print('PnL orden %.2f vs posicion %.2f (€) ; acc %.1f vs %.1f'%((o.acc_llena*(o.gana_lado-o.precio)).sum(),p.pnl.sum(),o.acc_llena.sum(),p.acc_llena.sum()))
