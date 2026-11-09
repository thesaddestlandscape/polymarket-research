#!/usr/bin/env python3
"""s7: para cada relleno real de B: edad de la orden al rellenarse (post_ok del ledger -> bloque/ts_est on-chain), cola al postear, T restante,
nº de repegas previas. Une ledger (oid) con m5_onchain (order_hash de la fila maker de B). Solo lectura."""
import json, pandas as pd, numpy as np
pd.set_option('future.infer_string', False)
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
W='0x659a40ff9920febc5a66836213040924343d297f'
J=pd.read_csv(DD+'b_fills_tomador.csv'); txs=set(J.tx)
oh=[]
for d in sorted(set(J.fecha_utc.str[:10])):
    for ch in pd.read_csv(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz',usecols=['tx','maker','order_hash'],chunksize=1_000_000):
        ch=ch[ch.tx.isin(txs)&(ch.maker.str.lower()==W)]
        if len(ch): oh.append(ch[['tx','order_hash']])
J=J.merge(pd.concat(oh).drop_duplicates('tx'),on='tx',how='left')
post={};puja={}
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    try: e=json.loads(l)
    except Exception: continue
    if e.get('tipo')=='post_ok': post[e['oid'].lower()]=pd.Timestamp(e['ts']).timestamp()
    if e.get('tipo')=='puja_post': puja[e['oid'].lower()]=(e.get('cola'),e.get('T'),e.get('n_orden'),e.get('precio'))
J['oid']=J.order_hash.str.lower(); J['t_post']=J.oid.map(post)
J['edad_s']=J.ts_est-J.t_post-2.4   # aprox: bloque - 2,4 s = casado
J['cola']=J.oid.map(lambda o:puja.get(o,(None,)*4)[0]); J['T_post']=J.oid.map(lambda o:puja.get(o,(None,)*4)[1]); J['n_orden']=J.oid.map(lambda o:puja.get(o,(None,)*4)[2])
J['seg_a_cierre']=J.mercado.str.split('-').str[-1].astype(float)+300-J.ts_est
J.to_csv(DD+'b_fills_vida.csv',index=False)
m=J.t_post.notna(); print('con post en ledger',int(m.sum()),'/',len(J))
for nm,S in (('pierde',J[m&~J.gana]),('gana',J[m&J.gana])):
    print(nm,len(S),'edad p10/50/90',np.round(np.nanpercentile(S.edad_s,[10,50,90]),2),'cola p50',np.nanmedian(S.cola.astype(float)),'T_post p50',np.nanmedian(S.T_post.astype(float)),'s2c p50',np.nanmedian(S.seg_a_cierre),'n_orden p50',np.nanmedian(S.n_orden.astype(float)))
J2=J[m].copy(); J2['edad_b']=pd.cut(J2.edad_s,[-99,1,3,10,30,999])
print(J2.groupby('edad_b',observed=True).agg(n=('gana','size'),gana=('gana','mean'),precio=('precio','mean'),pnl=('pnl','sum'),coste=('coste','sum')).assign(ev=lambda d:d.pnl/d.coste).round(3))
