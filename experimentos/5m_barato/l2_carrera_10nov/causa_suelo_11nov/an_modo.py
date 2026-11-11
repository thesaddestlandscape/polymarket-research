import pickle, glob, re, numpy as np
P = pickle.load(open('perhour_pre.pkl', 'rb'))
print('dia | n_q | horas | p5 p50 | %lag<=28 (modo rapido) | %29-60 (modo lento) | x p5 p50')
for d in sorted(P):
    q = P[d]['q'].sum(0); n = q.sum()
    if n == 0: continue
    c = np.cumsum(q); pc = lambda p: int(np.searchsorted(c, p * n)) - 100
    rap = q[100 + 10:100 + 29].sum() / n * 100; len_ = q[100 + 29:100 + 61].sum() / n * 100
    x = P[d]['x'].sum(0); nx = x.sum(); cx = np.cumsum(x)
    hrs = [h for h in range(24) if P[d]['q'][h].sum() > 20000]
    print(f"{d} | {n/1e6:.1f}M | {hrs[0]:02d}-{hrs[-1]:02d} | {pc(.05)} {pc(.5)} | {rap:5.1f} | {len_:5.1f} | x {int(np.searchsorted(cx,.05*nx))-100} {int(np.searchsorted(cx,.5*nx))-100}" if nx else f"{d} | n={n} sin x")
