#!/usr/bin/env python3
"""E02-real paso A (PREREG_E02REAL.md): une movimientos H47-B (215 fills maker) con onchain_fills y saca la huella del tomador. python3 -I."""
import csv,gzip,json,collections,sys
R='/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/'
OUT=sys.argv[1]
B='0x659a40ff9920febc5a66836213040924343d297f'
mov=[x for x in csv.DictReader(open(R+'movimientos.csv')) if x['experimento'].startswith('H47-B') and x['tipo']=='COMPRA']
pos={(x['mercado'],x['outcome']):x for x in csv.DictReader(open(R+'posiciones.csv')) if x['experimento'].startswith('H47-B')}
txs={x['tx'] for x in mov}
rows=collections.defaultdict(list)
for d in ('20','21','22','23'):
    with gzip.open(f'/root/polymarket-research-datalogs/onchain_fills_2026-10-{d}.csv.gz','rt') as f:
        for l in f:
            p=l.split(',')
            if len(p)>=13 and p[3] in txs and p[0]=='F': rows[p[3]].append(p)
EXCH='0xe111180000d2663c0091e4f400237545b87b996b'
res=[];stats=collections.Counter()
for m in mov:
    sz=float(m['size']);cand=[p for p in rows[m['tx']] if p[6]==B and abs((float(p[11]) if p[8]=='0' else float(p[10]))-sz)<=1e-4]
    if len(cand)!=1:
        stats['fill_F_%d'%len(cand)]+=1
        if len(cand)==0: res.append(dict(m,ok=0)); continue
        cand=[min(cand,key=lambda p:abs((float(p[10])/float(p[11]))-float(m['precio'])))]
    p=cand[0]; stats['F_ok']+=1
    tk=[q for q in rows[m['tx']] if q[6]==p[7] and q[7]==EXCH]
    h=None
    if tk:
        q=tk[0]; usdc,acc=(float(q[10]),float(q[11])) if q[8]=='0' else (float(q[11]),float(q[10]))
        h=dict(tok_t=q[9],side_t='BUY' if q[8]=='0' else 'SELL',pr_t=usdc/acc,acc_t=acc)
        stats['huella']+=1
    ps=pos.get((m['mercado'],m['outcome']))
    res.append(dict(mercado=m['mercado'],outcome=m['outcome'],tx=m['tx'],bloque=int(m['bloque']),logidx_mov=int(m['log_index']),logidx_fill=int(p[4]),
        ts_est=float(p[2]),oid=p[5],tok_x=p[9],precio=float(m['precio']),size=sz,pr_fill=float(p[10])/float(p[11]) if p[8]=='0' else None,
        gana=(None if not ps else (1 if ps['estado']=='liquidada_ganada' else 0 if ps['estado']=='liquidada_perdida' else None)),huella=h,ok=1,fecha=m['fecha_utc']))
json.dump(res,open(OUT,'w'))
print(len(mov),dict(stats),'sin gana:',sum(1 for r in res if r['ok'] and r['gana'] is None),'lado maker side0 todos:',collections.Counter(r['ok'] for r in res))
