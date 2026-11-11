#!/usr/bin/env python3
"""Primer orden (NO motor): G0 causal (out_v2/g0_fills_causal_ALL.pkl, TRAIN 26-Oct..09-Nov) con tf corregido por el emparejado exacto.
Regla CXB-true(l): cancelar cuando el bid VISTO por RECEPCION baja de L (o ya esta por debajo en t_arr); la cancelacion vale en EX = t_trig_rx + l.
Relleno evitado si tf (EX) > t_trig_rx + l. Se compara tf_old (passT causal) vs tf_true. Solo lectura."""
import sys, numpy as np, pandas as pd
pd.set_option('future.infer_string', False); F = pd.read_csv('F_g0.csv', dtype={c: object for c in ('var', 'dia', 'act', 'lado', 'ftype')})
F = F[F['var'] == 'G0'].copy(); TOLP = 0.0049; LS = (60, 100, 150, 300)
out = []; import gc
for d, g in F.groupby('dia'):
    E = pd.read_pickle(f'EMP_{d}.pkl')
    z = np.load(f'/root/polymarket-research-datalogs/sa_ms2/ms2_{d}.npz', allow_pickle=True); t0 = int(z['t0'])
    qk = z['q_k']; qb = np.searchsorted(qk, np.arange(len(z['tokens']) + 1, dtype=np.int16)); del qk
    RX = z['q_t_rx']; B = z['q_v0']
    E['tm_old'] = np.where(E.d_ex_old.notna(), E.tev - E.d_ex_old.fillna(0), E.tev).astype(np.int64) + t0
    E['t_true'] = (E.tev - np.where(E.n_exact >= 1, E.d_ex_near.fillna(20), 20)).astype(np.int64) + t0
    E['amb'] = E.n_exact != 1
    idx = {}
    for r in E[['k', 'tm_old', 't_true', 'amb', 'npr', 'tev', 'rcv']].itertuples(index=False): idx.setdefault((int(r.k), int(r.tm_old)), []).append(r)
    cache = {}; gc.collect()
    for r in g.itertuples():
        k = int(r.k); c = idx.get((k, int(r.tf)))
        if c is None: out.append((d, r.Index, 'sin_evento') + (None,) * 6); continue
        if len(c) > 1: c.sort(key=lambda x: x.t_true)
        e = c[0]; t_true = int(e.t_true); src = 'drop' if r.tf_rxb != -1 else 'tev'
        if k not in cache:
            a, b = qb[k], qb[k + 1]; o = np.argsort(RX[a:b], kind='stable'); cache[k] = (RX[a:b][o].astype(np.int64) + t0, B[a:b][o])
        rx, bb = cache[k]; t_arr = int(r.t_dec) + 68
        i = np.searchsorted(rx, t_arr, 'right') - 1
        if i >= 0 and bb[i] < r.L - TOLP: trig = t_arr
        else:
            j = np.searchsorted(rx, t_arr, 'right'); w = np.where(bb[j:] < r.L - TOLP)[0]
            trig = int(rx[j + w[0]]) if len(w) else None
        out.append((d, r.Index, src, int(r.tf), t_true, trig, bool(e.amb), int(e.npr), int(e.rcv) + t0))
    del RX, B, z, cache, idx, E; gc.collect(); print(d, len(out), int(open('/proc/self/status').read().split('VmSize:')[1].split()[0])//1024, flush=True)
O = pd.DataFrame(out, columns=['dia', 'ix', 'src', 'tf_old', 'tf_true', 'trig_rx', 'amb', 'npr', 'rcv']).set_index('ix')
F = F.join(O.drop(columns=['dia']))
F.to_pickle('G0_cxbtrue.pkl'); print(F.src.value_counts(dropna=False).to_dict())
