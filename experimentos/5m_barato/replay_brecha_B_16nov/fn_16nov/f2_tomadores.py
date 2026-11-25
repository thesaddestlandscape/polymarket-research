#!/usr/bin/env python3
"""f2_tomadores.py (FN_132, 16-Nov) -- SOLO LECTURA, 0 ordenes. Para cada relleno real de B (FN/TP, inventario.pkl) identifica la ORDEN TOMADORA del tx (fila resumen
taker==exchange: order_hash y direccion, on-chain) y busca en todo el on-chain del dia (keep_onchain_re_as_b) las demas casaciones de ESE tomador sobre el mismo mercado
(token propio side0 = bids; complementario side1 = asks del complementario, precio equivalente YES 1-p) en [-5, +5] s de bloque. Pregunta (H1, continuacion del tomador):
tras consumir nuestra orden, el mismo tomador sigue casando por DEBAJO de L (=> sin nosotros habria impreso por debajo de L: el simulador lo veria como barrido)?
Orden temporal por (bloque, log_index). Salida: tomadores.pkl / tomadores.json."""
import os, json, glob, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
X = pd.read_pickle(H + 'inventario2.pkl'); A = pd.read_pickle(H + 'tx_rows.pkl'); A['maker'] = A.maker.str.lower(); A['taker'] = A.taker.str.lower()
S = A[(A.tipo == 'F') & (A.taker == EX)][['tx', 'maker', 'order_hash', 'bloque', 'log_index']].rename(columns={'maker': 'tk_addr', 'order_hash': 'tk_hash', 'bloque': 'blk', 'log_index': 'li'})
X = X.merge(S, on='tx', how='left'); addrs = set(X.tk_addr.dropna())
TS = np.sort(X.ts_tx.dropna().values)
def cerca(ts): i = np.searchsorted(TS, ts); lo = np.abs(ts - TS[np.clip(i - 1, 0, len(TS) - 1)]); hi = np.abs(ts - TS[np.clip(i, 0, len(TS) - 1)]); return np.minimum(lo, hi) <= 5.5
if os.path.exists(H + 'tomadores_rows.pkl'):
    T = pd.read_pickle(H + 'tomadores_rows.pkl'); T = T[cerca(T.ts_est.values)]
else:
    parts = []
    for f in sorted(glob.glob('/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_2026-10-2[0-3].csv.gz')):
        for c in pd.read_csv(f, dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str, 'order_hash': str}, chunksize=200000):
            c = c[(c.tipo == 'F') & cerca(c.ts_est.values)]; c['maker'] = c.maker.str.lower(); c['taker'] = c.taker.str.lower()
            parts.append(c[c.taker.isin(addrs) | ((c.taker == EX) & c.maker.isin(addrs))])
    T = pd.concat(parts).drop_duplicates(['tx', 'log_index'])
T = T.drop_duplicates(['tx', 'log_index']); T.to_pickle(H + 'tomadores_rows.pkl'); print('filas tomador en ventanas', len(T), flush=True)
MK = T[T.taker != EX].copy(); MK['p'] = np.where(MK.side == 0, MK.maker_amt / MK.taker_amt, MK.taker_amt / MK.maker_amt); MK['sh'] = np.where(MK.side == 0, MK.taker_amt, MK.maker_amt)
SM = T[T.taker == EX]
out_rows = []
for r in X.itertuples():
    if not isinstance(r.tk_addr, str): continue
    tok = str(r.tok); m = MK[(MK.taker == r.tk_addr) & (MK.ts_est.between(r.ts_tx - 5, r.ts_tx + 5)) & (MK.tx != r.tx)]
    comp = m[(m.token_id != tok) & (m.side == 1)]; own_tok = m[(m.token_id == tok) & (m.side == 0)]
    # solo el MISMO mercado: complementario = cualquier token con ventana coincidente que aparezca en el tx propio como token del tomador
    ctoks = set(A[(A.tx == r.tx)].token_id) - {tok}
    comp = comp[comp.token_id.isin(ctoks)] if ctoks else comp.iloc[0:0]
    ev = pd.concat([own_tok.assign(peq=own_tok.p), comp.assign(peq=1 - comp.p)])
    key = ev.bloque * 100000 + ev.log_index; k0 = r.blk * 100000 + r.li
    aft = ev[key > k0]; bef = ev[key < k0]
    same_hash_other_tx = int(SM[(SM.order_hash == r.tk_hash) & (SM.tx != r.tx)].tx.nunique())
    out_rows.append(dict(oid=r.oid, n_tx_tomador_misma_orden=same_hash_other_tx,
                         desp_n=len(aft), desp_debajo=int((aft.peq < r.L - 1e-6).sum()), desp_en_L=int(((aft.peq - r.L).abs() <= 1e-6).sum()), desp_arriba=int((aft.peq > r.L + 1e-6).sum()),
                         desp_debajo_sh=float(aft[aft.peq < r.L - 1e-6].sh.sum()), desp_debajo_dt=float((aft[aft.peq < r.L - 1e-6].ts_est - r.ts_tx).min()) if (aft.peq < r.L - 1e-6).any() else np.nan,
                         antes_n=len(bef), antes_arriba=int((bef.peq > r.L + 1e-6).sum())))
Z = X.merge(pd.DataFrame(out_rows), on='oid', how='left'); Z.to_pickle(H + 'tomadores.pkl')
REB = 0.2 * 0.07
def ev_(d): return round(float(d.p_r.sum() / d.c_r.sum()), 4) if len(d) and d.c_r.sum() > 0 else None
res = {}
for (c, e), g in Z.groupby(['cls', 'estructura']):
    res[f'{c}|{e}'] = dict(n=len(g), tomadores_distintos=int(g.tk_addr.nunique()), top_tomador_frac=round(float(g.tk_addr.value_counts(normalize=True).iloc[0]), 3),
                         misma_orden_en_otro_tx=int((g.n_tx_tomador_misma_orden > 0).sum()), sigue_debajo_L=int((g.desp_debajo > 0).sum()),
                         sigue_en_L=int((g.desp_en_L > 0).sum()), barrio_antes_arriba=int((g.antes_arriba > 0).sum()),
                         ev_sigue_debajo=ev_(g[g.desp_debajo > 0]), ev_no_sigue=ev_(g[~(g.desp_debajo > 0)]), dt_sigue_debajo_p50=(round(float(g.desp_debajo_dt.median()), 2) if g.desp_debajo_dt.notna().any() else None))
json.dump(res, open(H + 'tomadores.json', 'w'), indent=1); print(json.dumps(res, indent=1))
