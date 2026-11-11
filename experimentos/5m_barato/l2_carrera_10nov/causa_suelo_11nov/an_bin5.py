import sys, numpy as np
f = sys.argv[1]; off = int(sys.argv[2]) if len(sys.argv) > 2 else 50
H = np.zeros((288, 351), np.int64)
for ln in open(f):
    b, l, c = ln.strip().split(','); H[int(b), int(l)] += int(c)
for b in range(288):
    n = H[b].sum()
    if n < 3000: continue
    c = np.cumsum(H[b]); q = lambda p: int(np.searchsorted(c, p * n)) - off
    lo = (H[b][:off + 28].sum() / n * 100)       # % con lag <=28
    print(f"{b*5//60:02d}:{b*5%60:02d} n={n:>7} p5={q(.05)} p25={q(.25)} p50={q(.5)} p90={q(.9)} %lag<=28={lo:5.1f}")
