import json, collections, pandas as pd, numpy as np
rows=[json.loads(l) for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl')]
df=pd.DataFrame(rows); df['t']=pd.to_datetime(df.ts, utc=True); df['dia']=df.t.dt.strftime('%Y-%m-%d'); df['h']=df.t.dt.hour
O=pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok':str})
print('ordenes_b', len(O), 'dias', O.dia.value_counts().sort_index().to_dict(), 'ledger dias', df.dia.min(), df.dia.max())
ip=df[df.tipo=='intencion_post']; pok=df[df.tipo=='post_ok']; pr=df[df.tipo=='post_rechazada']; pp=df[df.tipo=='puja_post']
print('intencion', len(ip), 'post_ok', len(pok), 'post_rechazada', len(pr), 'oid intencion-sin-post_ok == rechazadas:', set(ip.oid)-set(pok.oid)==set(pr.oid), len(set(ip.oid)-set(pok.oid)), 'ordenes_b oids == post_ok:', set(O.oid)==set(pok.oid), 'oids unicos intencion', ip.oid.nunique())
# =================== 37 rechazadas
x=pr[['oid','status','e','dia','h']].merge(ip[['oid','slug','lado','precio','ts']].rename(columns={'ts':'ts_int'}), on='oid', how='left'); x['coin']=x.slug.str.split('-').str[0]; x['L']=x.precio.astype(float)
x['status']=x.status; x['err']=x.e.str.extract(r"'error': '([^']*)'")[0].fillna(x.e.str[:60])
print('--- 37 rechazadas: motivo', x.err.value_counts().to_dict(), '| status', x.status.value_counts().to_dict())
print('por dia', x.dia.value_counts().sort_index().to_dict(), '| por moneda', x.coin.value_counts().to_dict(), '| por hora', x.h.value_counts().sort_index().to_dict())
print('L dist', x.L.round(2).value_counts().sort_index().to_dict(), '| lado', x.lado.value_counts().to_dict())
ipc=ip.copy(); ipc['coin']=ipc.slug.str.split('-').str[0]; ipc['rech']=ipc.oid.isin(pr.oid)
g=ipc.groupby('coin').rech.agg(['sum','size']); g['tasa']=(g['sum']/g['size']).round(4); print(g.to_string())
g=ipc.groupby('dia').rech.agg(['sum','size']); g['tasa']=(g['sum']/g['size']).round(4); print(g.to_string())
ipc['L']=ipc.precio.astype(float); g=ipc.groupby(ipc.L.round(2)).rech.agg(['sum','size']); g['tasa']=(g['sum']/g['size']).round(4); print(g.to_string())
# =================== bloqueo_suelo_saldo
b=df[df.tipo=='bloqueo_suelo_saldo'].copy(); 
for c in ('saldo','comprometido','coste','minimo'): b[c]=b[c].astype(float)
b['L']=(b.coste/5).round(2); print('--- bloqueo_suelo_saldo n', len(b), 'por dia', b.dia.value_counts().sort_index().to_dict(), '| por hora', b.h.value_counts().sort_index().to_dict())
print('coste (=size*L, size 5) -> L dist', b.L.value_counts().sort_index().to_dict()); print('comprometido dist', b.comprometido.round(1).describe().round(2).to_dict())
print('saldo-minimo', (b.saldo-b.minimo).describe().round(2).to_dict())
print('L bloqueados media', round(b.L.mean(),3), 'L posteadas media', round(O.precio.mean(),3))
# bloqueos como fraccion de intentos (bloqueos + intenciones) por dia/hora
inh=ip.groupby(['dia','h']).size().rename('post').reset_index(); bh=b.groupby(['dia','h']).size().rename('blq').reset_index(); m=inh.merge(bh,on=['dia','h'],how='outer').fillna(0); m['frac']=m.blq/(m.blq+m.post)
print('frac bloqueo por dia', (m.groupby('dia').blq.sum()/(m.groupby('dia').blq.sum()+m.groupby('dia').post.sum())).round(3).to_dict())
mh=m.groupby('h')[['blq','post']].sum(); mh['frac']=(mh.blq/(mh.blq+mh.post)).round(3); print('por hora (blq,post,frac)'); print(mh.T.to_string())
# racha: tiempo entre bloqueos consecutivos (se concentran?)
bb=b.sort_values('t'); gap=bb.t.diff().dt.total_seconds(); print('bloqueos: gap p50/p90 s', gap.median(), gap.quantile(.9), '| distintos minutos', bb.t.dt.floor('min').nunique())
# ¿que coin/mercado? asignar al mercado_inicio mas reciente por tiempo (no hay slug en el evento): solo cuenta de mercados activos
# =================== cancela_banda
c=df[df.tipo=='cancela_banda'].copy(); c['coin']=c.slug.str.split('-').str[0]
for k in ('de','bid','ask','T'): c[k]=pd.to_numeric(c[k], errors='coerce')
print('--- cancela_banda n', len(c), 'por dia', c.dia.value_counts().sort_index().to_dict(), '| moneda', c.coin.value_counts().to_dict(), '| hora', c.h.value_counts().sort_index().to_dict())
print('L de (nivel cancelado)', c.de.round(2).value_counts().sort_index().to_dict(), '| objetivo None', int((c.objetivo.astype(str)=='None').sum()))
print('bid-de en ticks', ((c.bid-c.de)*100).round().value_counts().sort_index().to_dict(), '| T med', c['T'].median())
gp=ipc.groupby('coin').size(); print('cancela_banda por 100 post por moneda', (c.coin.value_counts()/gp*100).round(1).to_dict())
print('post-intenciones por dia', ip.dia.value_counts().sort_index().to_dict())
# =================== soporte del ledger (ordenes_b)
O['coin']=O.coin.str.lower(); O['vida']=O.t_fuera-O.t_ini; O['h']=pd.to_datetime(O.t_ini, unit='s', utc=True).dt.hour
O['off_ticks']=O.off_c if 'off_c' in O else np.nan; O['L']=O.precio.round(2)
print('--- SOPORTE ordenes_b n', len(O))
print('L:', O.L.value_counts().sort_index().to_dict()); print('off_c (ticks bajo bid):', O.off_c.value_counts().sort_index().to_dict())
print('moneda:', O.coin.value_counts().to_dict(), '| lado', O.lado.value_counts().to_dict(), '| size', O['size'].value_counts().to_dict())
print('vida s cuantiles 5/25/50/75/95/99:', O.vida.quantile([.05,.25,.5,.75,.95,.99]).round(2).to_dict(), '| bins vida', pd.cut(O.vida,[0,.3,1,1.5,3,10,400]).value_counts().sort_index().to_dict())
print('horas UTC:', O.h.value_counts().sort_index().to_dict()); print('dias:', O.dia.value_counts().sort_index().to_dict(), '| T(s restantes) q', O['T'].quantile([.05,.5,.95]).round(0).to_dict())
print('cola(prof al armar) q', O.cola.quantile([.05,.25,.5,.75,.95]).round(1).to_dict(), '| precio bid: bb q', O.bb.quantile([.05,.5,.95]).to_dict())
print('moneda x L'); print(pd.crosstab(O.coin, O.L).to_string())
print('moneda x dia'); print(pd.crosstab(O.coin, O.dia).to_string())
print('fills por L:', O.groupby('L').fill.agg(['sum','size']).T.to_string())
# max vivas / k config
pass
O.to_pickle('out/ordenes_soporte.pkl'); b.to_pickle('out/bloqueos.pkl'); c.to_pickle('out/cancela_banda.pkl')
