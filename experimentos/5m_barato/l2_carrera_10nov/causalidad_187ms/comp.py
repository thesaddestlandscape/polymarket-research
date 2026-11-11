import numpy as np, pandas as pd, glob
pd.set_option('future.infer_string', False)
tot = {}
for f in sorted(glob.glob('EMP_*.pkl')):
    E = pd.read_pickle(f)
    E['t_true'] = np.where(E.n_exact >= 1, E.tev - E.d_ex_near, np.nan)
    o = E[(E.npr == 1) & E.d_ex_old.notna()].copy(); o['tm_old'] = o.tev - o.d_ex_old
    fills = {}
    for k, t in zip(E.k.values, E.t_true.values):
        if np.isfinite(t): fills.setdefault(int(k), []).append(int(t))
    fills = {k: np.sort(np.array(v)) for k, v in fills.items()}
    lab = []
    for k, t in zip(o.k.values, o.tm_old.values):
        a = fills.get(int(k))
        if a is None: lab.append('cancel_u_otro'); continue
        i = np.searchsorted(a, t - 1); lab.append('relleno_previo' if i < len(a) and a[i] <= t + 1 else 'cancel_u_otro')
    o['lab'] = lab
    for l, g in o.groupby('lab'):
        x = tot.setdefault(l, []); x.append(g.d_ex_old.values)
    print(f[4:14], o.lab.value_counts(normalize=True).round(3).to_dict())
for l, x in tot.items():
    v = np.concatenate(x); print(l, len(v), [round(float(np.percentile(v, q))) for q in (5, 25, 50, 75, 95)])
