#!/usr/bin/env python3
"""diag_print_vs_caida.py DIA -- trampa 03-Nov (print de libro5_tx llega DESPUES de la cotizacion que ya muestra el libro consumido): medida en AMBOS relojes sobre la cinta chain de DIA.
Para cada (token, tx) con caida L1 localizable (misma regla que passT: primera transicion de bid>pmin a bid<=pmin en [recv-400, recv] por RECEPCION):
  d_rx = recv_print - rx_caida ; d_ex = t_ev_print - ex_caida (mismo mensaje WS de cada lado, sellos del exchange) ; lag_print = recv_print - t_ev_print ; lag_caida = rx_caida - ex_caida.
d_rx = d_ex + lag_print - lag_caida: si d_ex ~ 0, el retraso del print es de TRANSPORTE/orden de llegada (rx), no del exchange. Solo lectura; salida out_v2/diag_print_vs_caida_<DIA>.json."""
import sys, os, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, H)
import relojes as R
d = sys.argv[1]; P2 = R.P2; PB = P2 + 'precursores_barrido/out/'
tape = pd.read_pickle(PB + f'tape_{d}.pkl'); K = R.Day2(d, 'rx', light=True, with_otro=True)
fr = []
for dd in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f in sorted(glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dd}_*.csv.gz')): fr.append(pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
T = pd.concat(fr).drop_duplicates(['token', 'tx']); TX = T.groupby('tx').agg(t_ev=('t_ev', 'min'), recv=('recv', 'min'))
tp = tape[tape.src == 'tx_ws'].assign(k=tape.token_id.map(K.tokidx)); tp = tp[tp.k.notna()]; tp['k'] = tp.k.astype(int)
ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min')).reset_index().join(TX, on='tx')
out = []
for r in ev.itertuples():
    a, b = K.qb[r.k], K.qb[r.k + 1]; qt = K.qt[a:b]; v0 = K.v0[a:b]
    i0 = np.searchsorted(qt, r.t - 400, side='left'); i1 = np.searchsorted(qt, r.t, side='right')
    if i1 > i0 and i0 > 0:
        lo = v0[i0 - 1:i1] <= r.pmin + 0.0049; w = np.where(lo[1:] & ~lo[:-1])[0]
        if len(w):
            j = a + i0 + w[0]; out.append((r.recv - K.qt[j], r.t_ev - K.otro(j), r.recv - r.t_ev, K.qt[j] - K.otro(j)))
x = np.array(out, float)
def p(v): q = np.percentile(v, [5, 25, 50, 75, 95]); return dict(zip(['p5', 'p25', 'p50', 'p75', 'p95'], map(float, q)))
Rr = dict(dia=d, n_eventos=int(len(ev)), n_con_caida=int(len(x)), d_rx=p(x[:, 0]), d_ex=p(x[:, 1]), lag_print=p(x[:, 2]), lag_caida=p(x[:, 3]), frac_d_ex_abs_le_20=float((np.abs(x[:, 1]) <= 20).mean()), frac_d_ex_pos=float((x[:, 1] > 0).mean()))
json.dump(Rr, open(H + f'out_v2/diag_print_vs_caida_{d}.json', 'w'), indent=1); print(json.dumps(Rr))
