#!/usr/bin/env python3
"""c2_barrido_b.py -- PREREG_COLA (sha a72007c5...). Para cada fila de relleno de B (hash on-chain = oid del ledger): posicion de B dentro de la rafaga (tx)
entre makers del MISMO nivel (precio equivalente BUY c a x / SELL c' a 1-x) ordenados por (bloque, li). Salida datos/b_barridos.csv (una fila por fila de relleno)."""
import json, hashlib, os, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
W = '0x659a40ff9920febc5a66836213040924343d297f'; EX = '0xe111180000d2663c0091e4f400237545b87b996b'; EPS = 0.0005
O = {o['oid']: o for o in json.load(open(DL + 'ordenes_b.json'))}
TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
TM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
T = pd.read_csv(DL + 'b_tx_all.csv', dtype={'tok': str, 'tx': str, 'hash': str, 'maker': str, 'taker': str})
T['rol'] = np.where(T.taker == EX, 'T', 'M')
T['acc'] = np.where(T.side == 0, T.ta, T.ma); T['usd'] = np.where(T.side == 0, T.ma, T.ta); T['px'] = T.usd / T.acc
rows = []
for h, g in T[(T.maker == W)].groupby('hash'):
    o = O[h]; c = TOK[h]
    g = g.sort_values(['bloque', 'li'])
    for k, (_, b) in enumerate(g.iterrows()):
        tx = T[(T.tx == b.tx)]
        mk = tx[tx.rol == 'M'].sort_values(['bloque', 'li']).copy()
        eq = np.where((mk.tok == c) & (mk.side == 0), mk.px, np.where((mk.tok != c) & (mk.side == 1), 1 - mk.px, np.nan))
        mk['pe'] = eq
        pc = b.px
        same = mk[np.abs(mk.pe - pc) < EPS]
        li_b = b.li
        ahead = same[same.li < li_b]; after = same[same.li > li_b]
        better = mk[(mk.pe > pc + EPS)]; worse = mk[(mk.pe < pc - EPS)]
        anom_before_worse = int(((mk.pe < pc - EPS) & (mk.li < li_b)).sum()); anom_after_better = int(((mk.pe > pc + EPS) & (mk.li > li_b)).sum())
        tk = tx[tx.rol == 'T']
        q = (len(ahead) / (len(same) - 1)) if len(same) >= 2 else np.nan
        rows.append(dict(oid=h, fila=k, es_primera=int(k == 0), tx=b.tx, bloque=b.bloque, li=li_b, ts_chain=b.ts, coin=o['coin'], pc=round(pc, 4), acc=b.acc,
                         n_mk=len(mk), n_same=len(same), rank_same=len(ahead), q=q, n_ahead_same=len(ahead), sh_ahead_same=ahead.acc.sum(), n_after_same=len(after), sh_after_same=after.acc.sum(),
                         n_better=len(better), sh_better=better.acc.sum(), n_worse=len(worse), sh_worse=worse.acc.sum(), n_mal_mirror=int(mk.pe.isna().sum()),
                         anom_before_worse=anom_before_worse, anom_after_better=anom_after_better, taker_acc=tk.acc.sum(),
                         ult_maker=int(li_b == mk.li.max()), w_ahead=';'.join(a[:10] for a in ahead.maker), w_better=';'.join(a[:10] for a in better.maker),
                         px_ahead=';'.join(f'{x:.3f}' for x in ahead.pe)))
R = pd.DataFrame(rows); R.to_csv(os.path.join(D, 'b_barridos.csv'), index=False)
P = R[R.es_primera == 1]
print('filas', len(R), 'ordenes', len(P), '| n_same dist (primeras):', P.n_same.value_counts().sort_index().to_dict(), '| anomalias precio:', int(P.anom_before_worse.sum()), int(P.anom_after_better.sum()), '| mal mirror:', int(P.n_mal_mirror.sum()))
