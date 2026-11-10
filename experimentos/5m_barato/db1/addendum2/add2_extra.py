#!/usr/bin/env python3
"""ADDENDUM2 extras (descriptivo): cobertura R0 vs R2/R3 por tick de precio (S_real, S_sim, S_pop) y R0 sin los 2 mejores dias. Solo lectura."""
import glob, numpy as np
Z = {f[-14:-4]: np.load(f) for f in sorted(glob.glob(__file__.rsplit('/', 1)[0] + '/out/d_2026-*.npz'))}
def cat(p, k): return np.concatenate([z[f'{p}_{k}'] for z in Z.values() if f'{p}_{k}' in z.files])
for p in ('real', 'sim', 'pop'):
    tk = cat(p, 'tick'); g = cat(p, 'guard').astype(bool); pn = cat(p, 'pnl').astype(float); c = cat(p, 'cost').astype(float)
    m = g & np.isfinite(pn)
    print(f'\n{p}: n={int(m.sum())}  tick: n | cob R0 R2 R3 | EV R0-raf R0-suelto | EV R2-raf R2-suelto')
    r0, r2, r3 = (cat(p, r) == 1 for r in ('R0', 'R2', 'R3'))
    for lo, hi in ((0, 9), (10, 14), (15, 17), (18, 21)):
        s = m & (tk >= lo) & (tk <= hi)
        if s.sum() == 0: continue
        ev = lambda q: pn[q].sum() / c[q].sum() if c[q].sum() > 0 else float('nan')
        print(f'  [{lo:02d}-{hi:02d}] {int(s.sum()):7d} | {r0[s].mean():.2f} {r2[s].mean():.2f} {r3[s].mean():.2f} | {ev(s & r0):+.3f} {ev(s & ~r0):+.3f} | {ev(s & r2):+.3f} {ev(s & ~r2):+.3f}')
# R0 sin los 2 mejores dias (mayor Delta diario) en S_sim y S_pop
for p, minn in (('sim', 5), ('pop', 30)):
    rows = []
    for d, z in Z.items():
        if f'{p}_pnl' not in z.files: continue
        g = z[f'{p}_guard'].astype(bool) & np.isfinite(z[f'{p}_pnl']); pn = z[f'{p}_pnl'][g].astype(float); c = z[f'{p}_cost'][g].astype(float); b = z[f'{p}_R0'][g] == 1
        if b.sum() < minn or (~b).sum() < minn: continue
        rows.append((d, pn[b].sum(), c[b].sum(), pn[~b].sum(), c[~b].sum()))
    A = np.array([r[1:] for r in rows]); dd = (A[:, 2] / A[:, 3]) - (A[:, 0] / A[:, 1]); o = np.argsort(-dd)
    for nm, keep in (('todos', np.arange(len(A))), ('sin 2 mejores', o[2:])):
        S = A[keep].sum(0); print(f'{p} R0 {nm}: dias={len(keep)} EV_raf {S[0]/S[1]:+.3f} EV_suelto {S[2]/S[3]:+.3f} Delta {S[2]/S[3]-S[0]/S[1]:+.3f}  (quitados: {[rows[i][0] for i in o[:2]] if nm != "todos" else "-"})')
