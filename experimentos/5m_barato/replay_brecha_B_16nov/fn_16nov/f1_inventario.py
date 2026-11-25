#!/usr/bin/env python3
"""f1_inventario.py (FN_132, 16-Nov) -- SOLO LECTURA, 0 ordenes, CPU ~s. Inventario de los rellenos reales de B 20-23 Oct (FN y TP) con motor v4
(verif_real/out_v4/V3_<D>.pkl, v3d BASE, es_fill q>=1e-3) y estructura ON-CHAIN COMPLETA del primer tx de relleno (tx_rows.pkl de f0; identidad maker/tomador
por fila on-chain, no firehose). Precio equivalente YES de cada maker: mismo token side0 -> p; token complementario side1 (vende el complementario) -> 1-p.
Salida: inventario.pkl / inventario.json."""
import os, sys, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'
DL = '/root/polymarket-research-datalogs/'; EX = '0xe111180000d2663c0091e4f400237545b87b996b'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
REB = 0.2 * 0.07
def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)
R = pd.concat([pd.read_pickle(L2 + f'verif_real/out_v4/V3_2026-10-2{i}.pkl') for i in range(4)], ignore_index=True)
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 'tok', 'lado', 'bb', 'bs', 'off_c', 'cola', 't_cancel_int', 'n_orden', 'cie'])
R = R.merge(O, on='oid', how='left')
R['q_s'] = R.v3d_BASE_f_q.astype(float); R['q_r'] = R.real_q.astype(float); R['q_opt'] = R.v3d_OPT_f_q.astype(float)
R['cls'] = np.where((R.q_s >= 1e-3) & (R.q_r > 1e-9), 'TP', np.where(R.q_s >= 1e-3, 'FP', np.where(R.q_r > 1e-9, 'FN', 'TN')))
R['cl'] = R.dia + '_' + (R.t_ini // 300000).astype(str)
BF = pd.read_csv(DL + 'calibracion_etiqueta/b_fills_onchain.csv', dtype={'token_id': str, 'tx': str}).drop_duplicates(['tx', 'log_index'])
A = pd.read_pickle(H + 'tx_rows.pkl'); A = A[A.tipo == 'F'].copy(); A['maker'] = A.maker.str.lower(); A['taker'] = A.taker.str.lower()
A['sh'] = np.where(A.side == 0, A.taker_amt, A.maker_amt); A['p'] = np.where(A.side == 0, A.maker_amt / A.taker_amt, A.taker_amt / A.maker_amt)
first = BF.sort_values(['ts_est', 'log_index']).groupby('order_hash').agg(tx=('tx', 'first'), ts=('ts_est', 'first'), ntx=('tx', 'nunique'), sh_tot=('taker_amt', 'sum')).reset_index()
rows = []
for r in R[R.q_r > 1e-9].itertuples():
    f = first[first.order_hash == r.oid]
    if not len(f): rows.append(dict(oid=r.oid, estructura='SIN_TX')); continue
    f = f.iloc[0]; a = A[A.tx == f.tx]; tok = str(r.tok)
    mk = a[a.taker != EX]; tk = a[a.taker == EX]
    own = mk[mk.maker == OWN]; oth = mk[mk.maker != OWN].copy()
    comp_toks = set(a.token_id) - {tok}
    oth['peq'] = np.where((oth.token_id == tok) & (oth.side == 0), oth.p, np.where((oth.token_id != tok) & (oth.side == 1), 1 - oth.p, np.nan))
    oth['tipo_o'] = np.where((oth.token_id == tok) & (oth.side == 0), 'bid_tok', np.where((oth.token_id != tok) & (oth.side == 1), 'ask_comp', 'otro'))
    L = r.L; tol = 1e-6
    n_at = int(((oth.peq - L).abs() <= 0.0051 * 0 + 1e-6).sum()); n_ab = int((oth.peq > L + tol).sum()); n_be = int((oth.peq < L - tol).sum()); n_otro = int((oth.tipo_o == 'otro').sum())
    sh_at = float(oth[(oth.peq - L).abs() <= 1e-6].sh.sum()); sh_be = float(oth[oth.peq < L - tol].sh.sum()); sh_ab = float(oth[oth.peq > L + tol].sh.sum())
    be_tape = int(((oth.peq < L - tol) & (oth.tipo_o == 'bid_tok')).sum()); be_comp = int(((oth.peq < L - tol) & (oth.tipo_o == 'ask_comp')).sum())
    at_tape = int((((oth.peq - L).abs() <= 1e-6) & (oth.tipo_o == 'bid_tok')).sum())
    if len(oth) == 0: est = 'SOLO'
    elif n_be > 0: est = 'DEBAJO'
    elif n_at > 0: est = 'MISMO_NIVEL'
    elif n_ab > 0: est = 'SOLO_ARRIBA'
    else: est = 'OTRO'
    tk_tok = ','.join(sorted(set(np.where(tk.token_id == tok, 'tok', 'comp') + '_s' + tk.side.astype(str))))
    rows.append(dict(oid=r.oid, tx=f.tx, ts_tx=float(f.ts), ntx=int(f.ntx), estructura=est, n_otros=len(oth), n_at=n_at, n_arriba=n_ab, n_debajo=n_be, n_otro=n_otro,
                     sh_at=sh_at, sh_debajo=sh_be, sh_arriba=sh_ab, debajo_en_cinta=be_tape, debajo_solo_comp=be_comp, at_en_cinta=at_tape,
                     own_sh_tx=float(own.sh.sum()), own_p=float(own.p.mean()) if len(own) else np.nan, taker_tipo=tk_tok, taker_sh=float(tk.sh.sum()), n_taker=tk.maker.nunique()))
I = pd.DataFrame(rows); X = R[R.q_r > 1e-9].merge(I, on='oid', how='left')
X['p_r'] = pnl_of(X.q_r, X.L, X.gana); X['c_r'] = X.q_r * X.L
X['opt_ve'] = X.q_opt >= 1e-3; X['parcial'] = X.q_r < X['size'] - 1e-6
X.to_pickle(H + 'inventario.pkl')
def ev(d): return round(float(d.p_r.sum() / d.c_r.sum()), 4) if d.c_r.sum() > 0 else None
out = {}
for c in ('FN', 'TP'):
    d = X[X.cls == c]; out[c] = dict(n=len(d), ev_real=ev(d), coste=round(float(d.c_r.sum()), 2),
        por_estructura={k: dict(n=len(g), ev=ev(g), coste=round(float(g.c_r.sum()), 2), opt_ve=int(g.opt_ve.sum()), gana=int((g.gana == 1).sum()),
                                debajo_en_cinta=int((g.debajo_en_cinta > 0).sum()), debajo_solo_comp=int(((g.debajo_solo_comp > 0) & (g.debajo_en_cinta == 0)).sum()),
                                at_en_cinta=int((g.at_en_cinta > 0).sum()), taker=g.taker_tipo.value_counts().to_dict()) for k, g in d.groupby('estructura')},
        por_dia=d.dia.value_counts().sort_index().to_dict(), por_moneda=d.coin.value_counts().to_dict(), off_c=d.off_c.value_counts().sort_index().to_dict(),
        L=d.L.describe()[['min', '50%', 'max']].round(2).to_dict(), size=d['size'].value_counts().to_dict(), parcial=int(d.parcial.sum()), ntx_gt1=int((d.ntx > 1).sum()),
        n_mk1_T1=None)
T = pd.read_pickle(L2 + 'verif_real/out/T1_tx.pkl'); nm = T.groupby('order_hash').n_mk.min(); X['n_mk_T1'] = X.oid.map(nm)
for c in ('FN', 'TP'):
    d = X[X.cls == c]; out[c]['n_mk1_T1'] = int((d.n_mk_T1 == 1).sum())
    out[c]['cruce_T1_vs_estructura'] = pd.crosstab(d.n_mk_T1 == 1, d.estructura).to_dict()
json.dump(out, open(H + 'inventario.json', 'w'), indent=1, default=str); print(json.dumps(out, indent=1, default=str))
