import sys, os, json, pickle, numpy as np
E4 = '/root/polymarket-research/experimentos/5m_barato/'
sys.path.insert(0, E4 + 'formula_r5_28oct'); sys.path.insert(0, E4 + 'formula_r4_28oct'); sys.path.insert(0, E4 + 'formula_r3_28oct')
import r5, r4
G = json.load(open(r4.I.CACHE))
si = [i for i, sp in enumerate(r5.SPECS) if sp == ('S', 800.0, 5.0, 60.0, 1, 1)][0]; v = r5.vid(si, 0, 0)
print('v258 =', r5.vlabel(v), flush=True)
for d in sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_')):
    out = E4 + 'formula_r7_28oct/simc/s_%s.pkl' % d
    if os.path.exists(out): continue
    R, rows, inf = r5.run_day(d, G, only={si}, detail={v}); pickle.dump((R[v], rows), open(out, 'wb')); print(d, 'ok fills', len(rows), flush=True)
