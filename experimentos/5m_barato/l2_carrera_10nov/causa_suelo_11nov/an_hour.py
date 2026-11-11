import pickle, sys, numpy as np
P = pickle.load(open(sys.argv[1], 'rb'))
for d in sys.argv[2:]:
    H = P[d]['q']
    s = []
    for h in range(24):
        n = H[h].sum()
        if n < 5000: continue
        c = np.cumsum(H[h]); p5 = np.searchsorted(c, .05 * n) - 100; p50 = np.searchsorted(c, .5 * n) - 100
        s.append(f"{h:02d}h n={n//1000}k p5={p5} p50={p50}")
    print(d, ' ; '.join(s))
