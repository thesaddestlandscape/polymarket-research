#!/usr/bin/env python3
"""RE-AS-B r1: reproduce desde el crudo etiquetado_pasivo_B (órdenes reales de B) P(fill) y la brecha de acierto rellenas vs no rellenas."""
import pandas as pd, numpy as np, glob
D='/root/polymarket-research-datalogs/etiquetado_pasivo_B/'
X=pd.concat([pd.read_csv(f) for f in sorted(glob.glob(D+'etiquetado_B_2026-10-2[0-3].csv.gz'))],ignore_index=True)
print('filas',len(X),'unidad',X.unidad.value_counts().to_dict(),'dias',X.dia.value_counts().sort_index().to_dict())
o=X[X.unidad=='orden'].copy()
print('ordenes',len(o),'duplicados id',o.id.duplicated().sum(),'resuelto',o.resuelto.value_counts(dropna=False).to_dict())
o['fill']=(o.acc_llena>0).astype(int)
print('P(fill) por orden %.4f (n=%d, rellenas %d)'%(o.fill.mean(),len(o),o.fill.sum()))
print('P(fill) por dia',o.groupby('dia').fill.agg(['mean','sum','size']).round(4).to_dict('index'))
print('P(fill) ponderada por acc %.4f'%(o.acc_llena.sum()/o.acc.sum()))
r=o[o.gana_lado.notna()].copy(); print('con desenlace',len(r),'de',len(o))
r['pb']=(r.precio*100).round().astype(int)
r['hp']=r.gana_lado-r.precio
for k,g in r.groupby('fill'): print('fill=%d n=%d hit=%.4f precio=%.4f hit-p=%+.4f'%(k,len(g),g.gana_lado.mean(),g.precio.mean(),g.hp.mean()))
# brecha emparejada por estrato dia x moneda x precio(1c): media ponderada por nº rellenas
s=r.groupby(['dia','coin','pb','fill']).gana_lado.mean().unstack('fill').dropna()
w=r[r.fill==1].groupby(['dia','coin','pb']).size().reindex(s.index)
print('estratos con ambos',len(s),'rellenas cubiertas',int(w.sum()))
print('brecha emparejada (rellena-no) %+.4f'%(((s[1]-s[0])*w).sum()/w.sum()))
# misma por mercado-lado (unidad): una obs por (mercado,lado,fill)
u=r.groupby(['mercado','lado','fill']).agg(g=('gana_lado','first'),p=('precio','mean'),dia=('dia','first'),coin=('coin','first'),fin=('fin_s','first')).reset_index()
for k,g in u.groupby('fill'): print('unidad mercado-lado fill=%d n=%d hit=%.4f p=%.4f hit-p=%+.4f'%(k,len(g),g.g.mean(),g.p.mean(),(g.g-g.p).mean()))
# bootstrap por cierre de la brecha de unidades (hit-p rellenas menos hit-p no rellenas)
rng=np.random.default_rng(26); cl=u.fin.unique(); idx={c:np.where(u.fin.values==c)[0] for c in cl}; bs=[]
for i in range(2000):
    q=u.iloc[np.concatenate([idx[c] for c in rng.choice(cl,len(cl))])]
    a=q[q.fill==1]; b=q[q.fill==0]
    if len(a) and len(b): bs.append((a.g-a.p).mean()-(b.g-b.p).mean())
print('brecha hit-p unidad rellena-no %+.4f IC90 (%+.4f,%+.4f) cierres %d'%((u[u.fill==1].g-u[u.fill==1].p).mean()-(u[u.fill==0].g-u[u.fill==0].p).mean(),*np.percentile(bs,[5,95]),len(cl)))
# EV de rellenas al precio de la orden, desde el crudo
f=o[(o.fill==1)&o.gana_lado.notna()]
print('EV rellenas (acc_llena*gana - acc_llena*precio)/coste: %+.4f n=%d coste=%.2f'%(((f.acc_llena*f.gana_lado-f.acc_llena*f.precio).sum()/(f.acc_llena*f.precio).sum()),len(f),(f.acc_llena*f.precio).sum()))
