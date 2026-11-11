#!/usr/bin/env python3
"""regresion_extractor.py DIA -- el extractor v2 reproduce EXACTAMENTE el npz v1 (sa_ms/ms_D.npz) en todo salvo las columnas nuevas de recepcion. Un dia; solo lectura. Salida: out_v2/regresion_extractor_<D>.json."""
import sys, os, json, numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'; d = sys.argv[1]
a = np.load(f'/root/polymarket-research-datalogs/sa_ms/ms_{d}.npz', allow_pickle=True); b = np.load(f'/root/polymarket-research-datalogs/sa_ms2/ms2_{d}.npz', allow_pickle=True)
R = dict(dia=d, igual={})
R['igual']['tokens'] = bool((a['tokens'] == b['tokens']).all()); R['igual']['tmap'] = bool((a['tmap'] == b['tmap']).all()); R['igual']['t0'] = bool(int(a['t0']) == int(b['t0']))
for ka, kb in (('q_t', 'q_t_ex'), ('q_k', 'q_k'), ('t_t', 't_t_ex'), ('t_k', 't_k'), ('t_pr', 't_pr'), ('t_sd', 't_sd'), ('t_sz', 't_sz')) + tuple((f'q_v{j}', f'q_v{j}') for j in range(4)):
    x, y = a[ka], b[kb]
    R['igual'][ka] = bool(x.shape == y.shape and np.array_equal(x, y, equal_nan=x.dtype.kind == 'f'))
R['filas'] = dict(q_v1=int(len(a['q_t'])), q_v2=int(len(b['q_t_ex'])), t_v1=int(len(a['t_t'])), t_v2=int(len(b['t_t_ex'])), q_sin_rx=int((b['q_t_rx'] < 0).sum()), t_sin_rx=int((b['t_t_rx'] < 0).sum()))
R['identico'] = all(R['igual'].values())
os.makedirs(H + 'out_v2', exist_ok=True); json.dump(R, open(H + f'out_v2/regresion_extractor_{d}.json', 'w'), indent=1); print(json.dumps(R))
