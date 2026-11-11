import sys, glob, collections, re
import numpy as np
suf = sys.argv[1] if len(sys.argv) > 1 else 'pre'
rows = []
def pct(h, qs=(1, 5, 50, 90, 99)):
    n = h.sum()
    if n == 0: return None
    c = np.cumsum(h); return [int(np.searchsorted(c, q / 100 * n)) - 100 for q in qs], int(n)
per_hour = {}
for f in sorted(glob.glob(f'lag_*_{suf}.txt')):
    d = re.search(r'lag_(.*?)_', f).group(1)
    H = {'q': np.zeros((24, 2101), np.int64), 'x': np.zeros((24, 2101), np.int64)}
    for ln in open(f):
        k, h, b, c = ln.strip().split(','); H[k][int(h), int(b)] += int(c)
    out = [d]
    for k in 'qx':
        p = pct(H[k].sum(0))
        if p is None: out.append(f"{k}: n=0"); continue
        hrs = [h for h in range(24) if H[k][h].sum() > 1000]
        out.append(f"{k}: n={p[1]:>9} p1/5/50/90/99={p[0]} horas={hrs[0] if hrs else '-'}-{hrs[-1] if hrs else '-'}")
    print(' | '.join(out))
    per_hour[d] = H
import pickle; pickle.dump(per_hour, open(f'perhour_{suf}.pkl', 'wb'))
