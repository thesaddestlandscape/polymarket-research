#!/usr/bin/env python3
"""incremental.py -- la senal post-relleno, ?anade informacion sobre el BID del momento? Logit gana ~ logit(bid_salida) + senal estandarizada,
por periodo (pob 17-19 / pob 20-22 / B 20-22). Si el coef. de logit(bid) ~1 y el de la senal ~0, el precio ya lo descuenta."""
import sys, os, numpy as np, pandas as pd
sys.argv = ['x']; import reglas as R
def logit_fit(X, y, it=50):
    b = np.zeros(X.shape[1])
    for _ in range(it):
        p = 1 / (1 + np.exp(-X @ b)); W = p * (1 - p); H = X.T @ (X * W[:, None]) + 1e-8 * np.eye(X.shape[1])
        b = b + np.linalg.solve(H, X.T @ (y - p))
    se = np.sqrt(np.diag(np.linalg.inv(H))); return b, se
for modo, dias in (('pop', ['2026-10-17', '2026-10-18', '2026-10-19']), ('pop', ['2026-10-20', '2026-10-21', '2026-10-22']), ('b', ['2026-10-20', '2026-10-21', '2026-10-22'])):
    L = R.cargar(modo, dias); L['imb'] = np.where((L.fav + L.con) > 0, (L.fav - L.con) / (L.fav + L.con).clip(lower=1e-9), 0)
    print(f'\n## {modo} {dias[0][5:]}..{dias[-1][5:]}')
    for tau in (15, 30):
        d = L[(L.tau == tau) & (L.aplic == 1)].copy()
        b = d.bid_exec.clip(0.01, 0.99); lb = np.log(b / (1 - b))
        out = []
        for s in ('dbid', 'bnret', 'd15', 'imb'):
            x = d[s].fillna(0).values; x = (x - x.mean()) / (x.std() + 1e-12)
            X = np.column_stack([np.ones(len(d)), lb, x]); bb, se = logit_fit(X, d.gana.values.astype(float))
            out.append(f'{s}: coef {bb[2]:+.3f} (z {bb[2]/se[2]:+.1f}) logit(bid) {bb[1]:.2f}')
        print(f'  tau={tau} n={len(d)} | ' + ' | '.join(out))
