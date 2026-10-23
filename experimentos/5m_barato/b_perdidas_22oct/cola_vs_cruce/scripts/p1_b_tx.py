#!/usr/bin/env python3
"""p1_b_tx.py -- clasificacion a nivel de TRANSACCION de los rellenos de B real (solo lectura).
Para cada COMPRA maker de B (contabilidad_wallet_dedicada/movimientos.csv, tanda_B) busca su tx en onchain_fills (datos/b_txs_fills.csv)
y mide: precio equivalente-bid del lado s de TODOS los makers rellenados en esa tx; TX_DEEP = algun maker a precio s-equiv < el nuestro
(la orden tomadora atraveso nuestro nivel); niveles por encima comidos en la misma tx; rango de nuestro log_index entre makers de nuestro precio.
Salida datos/b_tx.csv."""
import csv, collections, os
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
W = '0x659a40ff9920febc5a66836213040924343d297f'; EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
mov = [x for x in csv.DictReader(open(os.path.join(AQ, '../../../contabilidad_wallet_dedicada/movimientos.csv'))) if x['tanda_B'] and x['tipo'] == 'COMPRA']
tx = collections.defaultdict(list)
for c in csv.reader(open(os.path.join(D, 'b_txs_fills.csv'))):
    if c[0] != 'F': continue
    tx[c[3]].append(dict(li=int(c[4]), maker=c[6].lower(), taker=c[7].lower(), side=int(c[8]), tok=c[9], ma=float(c[10]), ta=float(c[11]), fee=float(c[12] or 0)))
out = []; nomatch = 0
for m in mov:
    rows = tx.get(m['tx'], [])
    me = [r for r in rows if r['maker'] == W and r['li'] == int(m['log_index'])] or [r for r in rows if r['maker'] == W]
    if not me: nomatch += 1; out.append(dict(tx=m['tx'], mercado=m['mercado'], outcome=m['outcome'], clase_tx='missing')); continue
    me = me[0]; s = me['tok']; p = me['ma'] / me['ta']   # nuestra BUY: precio = usdc/acciones
    mk = [r for r in rows if r['taker'] != EXCH and r['maker'] != '' ]
    tk = [r for r in rows if r['taker'] == EXCH]
    eq = []
    for r in mk:
        pr = r['ma'] / r['ta'] if r['side'] == 0 else r['ta'] / r['ma']
        acc = r['ta'] if r['side'] == 0 else r['ma']
        if r['tok'] == s and r['side'] == 0: e = pr          # otro bid del mismo token
        elif r['tok'] != s and r['side'] == 1: e = 1 - pr    # ask del token contrario (casado por acunado/quemado)
        else: e = None                                       # contraparte del otro sentido (no deberia)
        eq.append((e, acc, r['li'], r['maker'] == W))
    e_ok = [x for x in eq if x[0] is not None]
    deep = [x for x in e_ok if x[0] < p - 0.005]
    above = [x for x in e_ok if x[0] > p + 0.005]
    same = sorted([x for x in e_ok if abs(x[0] - p) <= 0.005], key=lambda x: x[2])
    rank = [i for i, x in enumerate(same) if x[3]]
    taker_dir = None
    if tk:
        t0 = tk[0]; taker_dir = ('BUY_opp' if t0['tok'] != s else 'BUY_s') if t0['side'] == 0 else ('SELL_s' if t0['tok'] == s else 'SELL_opp')
    out.append(dict(tx=m['tx'], bloque=m['bloque'], fecha=m['fecha_utc'], mercado=m['mercado'], outcome=m['outcome'], p=round(p, 4), acc=me['ta'],
                    n_makers=len(mk), n_tk=len(tk), taker_dir=taker_dir, n_otro=sum(1 for x in eq if x[0] is None),
                    acc_deep=round(sum(x[1] for x in deep), 4), p_min=round(min(x[0] for x in e_ok), 4), n_deep=len(deep),
                    acc_above=round(sum(x[1] for x in above), 4), n_above=len(above), p_max=round(max(x[0] for x in e_ok), 4),
                    n_same=len(same), rank_same=(rank[0] if rank else -1), acc_same_before=round(sum(x[1] for x in same[:rank[0]]) if rank else 0, 4),
                    acc_same_after=round(sum(x[1] for x in same[rank[0] + 1:]) if rank else 0, 4),
                    clase_tx='TX_DEEP' if deep else 'TX_STOP'))
f = os.path.join(D, 'b_tx.csv')
keys = list(max(out, key=len).keys())
with open(f, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); [w.writerow(r) for r in out]
print('rellenos', len(out), 'sin tx en onchain', nomatch, collections.Counter(r['clase_tx'] for r in out),
      collections.Counter(r.get('taker_dir') for r in out), 'otro', sum(r.get('n_otro', 0) for r in out))
