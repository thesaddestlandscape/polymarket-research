import sys, bisect, glob, json, collections
from array import array
S = sys.argv[1]
tot_ep = 0; ndias = 0; per = []
for f in sorted(glob.glob(f'{S}/x_*.txt')):
    dia = f[-14:-4]
    v = []
    for ln in open(f):
        if ',BTCUSDT,' not in ln: continue
        c = ln.split(',')
        try: v.append((int(c[6]), float(c[3])))
        except Exception: pass
    if len(v) < 1000: continue
    v.sort(); E = array('q', [a for a, _ in v]); P = [b for _, b in v]
    # ventanas vivas de pares 5m alineados con 15m: cierre %900==0 del día
    d0 = int(__import__('datetime').datetime.fromisoformat(dia + 'T00:00:00+00:00').timestamp())
    ep = {1: 0, -1: 0}
    for sg in (1, -1):
        last = -10**15
        for k in range(len(v)):
            t = E[k]
            cie = ((t // 1000) // 900 + 1) * 900
            if not ((cie - 300) * 1000 + 2000 <= t <= cie * 1000 - 10000): continue
            if t - last < 3000: continue
            j = bisect.bisect_right(E, t - 3000) - 1
            if j < 0: continue
            if sg * (P[k] / P[j] - 1) * 1e4 >= 1.0:
                ep[sg] += 1; last = t
    per.append((dia, ep[1] + ep[-1]))
print(per)
print('episodios/día (BTC, ambos sentidos, refractario 3 s, ventanas vivas del 5m alineado):', sum(x for _, x in per) / max(1, len(per)), 'en', len(per), 'días con datos BTC')
