"""Complemento post-resultado (NO prerregistrado): CXJ150 vs CXJ1000 pareado, CXJ150 por moneda/lado, sin 2 mejores dias de la Delta."""
import glob, numpy as np, pandas as pd
O = 'out/'; R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(O + 'RT_*.pkl'))]); rng = np.random.default_rng(11)
FD = R.groupby('fin').dia.first()
def dl(a, b, m=None):
    x = R[R['var'] == a]; y = R[R['var'] == b]
    if m is not None: x = x[m(x)]; y = y[m(y)]
    fins = sorted(set(x.fin) | set(y.fin)); v = x.groupby('fin').pnl.sum().reindex(fins, fill_value=0) - y.groupby('fin').pnl.sum().reindex(fins, fill_value=0)
    bs = v.values[rng.integers(0, len(v), (4000, len(v)))].sum(1); dd = v.groupby(FD.reindex(v.index).values).sum(); s2 = dd.drop(dd.sort_values().index[-2:]).sum()
    return f'{v.sum():+7.1f} IC90cie ({np.percentile(bs, 5):+.1f},{np.percentile(bs, 95):+.1f}) dias>0 {int((dd > 0).sum())}/{len(dd)} sin2mejores {s2:+.1f}'
print('CXJ150-CXJ1000', dl('CXJ150', 'CXJ1000')); print('CXB150-CXB3000', dl('CXB150', 'CXB3000')); print('CXJ150-G0 OOS', dl('CXJ150', 'G0', lambda z: z.dia >= '2026-11-01'))
for c in ('ETH', 'SOL', 'XRP'): print('CXJ150-G0', c, dl('CXJ150', 'G0', lambda z, c=c: z.act == c))
for s in ('YES', 'NO'): print('CXJ150-G0', s, dl('CXJ150', 'G0', lambda z, s=s: z.lado == s))
for s in ('YES', 'NO'): print('GEO6-G0', s, dl('GEO6', 'G0', lambda z, s=s: z.lado == s))
g = R[R['var'] == 'G0']; c = R[R['var'] == 'CXJ150']; k = set(zip(c.k, c.L, c.tf)); q = g[[t not in k for t in zip(g.k, g.L, g.tf)]]
print('rellenos G0 que CXJ150 quita:', len(q), 'EV', round(q.pnl.sum() / q.cost.sum(), 3), q.ftype.value_counts().to_dict(), '| G0 thru1 EV', round(g[g.ftype == 'thru1'].pnl.sum() / g[g.ftype == 'thru1'].cost.sum(), 3), 'n', int((g.ftype == 'thru1').sum()))
