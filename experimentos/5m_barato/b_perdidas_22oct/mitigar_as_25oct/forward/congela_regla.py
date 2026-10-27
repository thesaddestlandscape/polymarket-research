#!/usr/bin/env python3
"""congela_regla.py -- congela la regla F5 de A1 (PREREG_A1) con el TRAIN ORIGINAL 06-08 Oct (r_2026-10-0{6,7,8}.pkl, solo ETH/SOL/XRP).
Equivale a la regla del dia de test 09-Oct del walk-forward original (sel=2, tercil ALTO, en los 15 dias). No lee ningun dato >= 24-Oct.
Salida regla_congelada.json. Solo lectura."""
import os, json, hashlib, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; AQ = os.path.dirname(os.path.abspath(__file__))
fs = [DL + f'r_2026-10-0{d}.pkl' for d in (6, 7, 8)]
X = pd.concat([pd.read_pickle(f) for f in fs], ignore_index=True)
tr = X[np.isfinite(X.F5)]
c = [float(v) for v in np.quantile(tr.F5.values, [1/3, 2/3])]
tt = np.where(tr.F5.values <= c[0], 0, np.where(tr.F5.values <= c[1], 1, 2))
ev = [float(tr.pnl.values[tt == k].sum() / tr.coste.values[tt == k].sum()) for k in range(3)]
t2 = X[np.isfinite(X.F2)]
f2_edges = [float(v) for v in np.quantile(t2.F2.values, np.linspace(0.1, 0.9, 9))]
reg = dict(rasgo='F5 = log1p(tamano del ask del token del maker) a tau = recepcion_print - 100 ms (estado = ultima fila q con recepcion <= tau, max 30 s)',
           cortes_F5_terciles_train=c, tercil_marcado=int(np.argmin(ev)), tercil_inversion=int(np.argmax(ev)), ev_train_por_tercil=ev,
           marcar='F5 > cortes[1] si tercil_marcado==2', F2_deciles_train=f2_edges, n_train=int(len(X)), n_train_F5=int(len(tr)), dias_train=['2026-10-06', '2026-10-07', '2026-10-08'],
           train_sha256={os.path.basename(f): hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in fs})
assert reg['tercil_marcado'] == 2, reg
json.dump(reg, open(os.path.join(AQ, 'regla_congelada.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in reg.items() if k != 'train_sha256'}, indent=1))
