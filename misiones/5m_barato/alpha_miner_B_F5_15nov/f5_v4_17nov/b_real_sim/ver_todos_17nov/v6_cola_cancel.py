#!/usr/bin/env python3
"""v6_cola_cancel.py -- diagnostico de los FN clase 8 (cola no agotada) y 4 (relleno real tras cancelacion simulada). SOLO LECTURA.
Cola: posicion de NUESTRA orden en makerOrders del calldata frente a otros makers al MISMO precio (orden del operador = prioridad), cola delante del motor (bk_bsz
si bid==L) y suma de prints en L en la ventana. Cancelacion: rt - t_end, rt - t_cancel_int, firma del tomador vs envio de la cancelacion."""
import json, numpy as np, pandas as pd, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
CD = {}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', H + 'calldata_extra.jsonl'):
    for l in open(f): j = json.loads(l); CD[j['tx']] = j['input']
def makers(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big'); om = w(64); n = w(om); out = []
    for i in range(n):
        s = om + 32 + w(om + 32 * (1 + i)); f = [w(s + 32 * k) for k in range(12)]
        mk = '0x' + f[1].to_bytes(32, 'big')[12:].hex(); side = f[6]; p = f[4] / f[5] if side == 0 else f[5] / f[4]
        out.append(dict(i=i, maker=mk, tok=str(f[3]), side=side, p=round(p, 4), ts=f[8]))
    return out
T = pd.read_pickle(H + 'tomador_202.pkl'); T['cl'] = T.causa.str.split('(').str[0]
rows = []
for r in T[T.cl.isin(['8_cola_no_agotada', 'TP'])].itertuples():
    m = makers(CD[r.tx]); own = [x for x in m if x['maker'] == OWN and x['tok'] == str(r.tok)]
    if not own: continue
    o = own[0]; sameL = [x for x in m if x['maker'] != OWN and x['tok'] == str(r.tok) and x['side'] == 0 and abs(x['p'] - r.L) < 0.005]
    rows.append(dict(oid=r.oid, cl=r.cl, n_mismoL=len(sameL), delante=sum(x['i'] < o['i'] for x in sameL), detras=sum(x['i'] > o['i'] for x in sameL),
                     detras_firmo_antes=sum(x['i'] > o['i'] and x['ts'] < o['ts'] for x in sameL), bk_bid=r.bk_bid, bk_bsz=r.bk_bsz, L=r.L, sz_eqL=r.sz_pr_eqL, size=r.size))
C = pd.DataFrame(rows); C['ahead_motor'] = np.where((C.bk_bid - C.L).abs() < 0.005, C.bk_bsz, 0.0)
print(C[C.cl == '8_cola_no_agotada'][['n_mismoL', 'delante', 'detras', 'detras_firmo_antes', 'ahead_motor', 'sz_eqL', 'size']].to_string())
print('TP con mismoL:', C[(C.cl == 'TP') & (C.n_mismoL > 0)][['delante', 'detras', 'detras_firmo_antes']].sum().to_dict())
K = T[T.cl == '4_relleno_real_tras_cancel_sim'].copy()
K['rt_menos_tend'] = K.real_tm3 - K.t_end; K['rt_menos_tci'] = K.real_tm3 - K.t_cancel_int; K['tk_firma_menos_tci'] = K.tk_ts - K.t_cancel_int
print(K[['oid', 'rt_menos_tend', 'rt_menos_tci', 'tk_firma_menos_tci', 'estructura', 'real_q', 'gana', 'L']].to_string())
C.to_pickle(H + 'cola_diag.pkl'); K.to_pickle(H + 'cancel_diag.pkl')
