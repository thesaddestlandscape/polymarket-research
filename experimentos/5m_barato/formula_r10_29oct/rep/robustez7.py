import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
for d in ('2026-10-07', '2026-10-20'):
    D = Day(d, 'BTC'); bad = 0; tot = 0; nb = 0
    for uu in range(D.n):
        a, b = int(D.qlo[uu]), int(D.qhi[uu])
        if b - a < 2: continue
        tot += 1; dq = np.diff(D.qt[a:b]); 
        if (dq < 0).any(): bad += 1; nb += int((dq < 0).sum())
    print(d, 'tokens con qt no monotono', bad, 'de', tot, 'retrocesos', nb, 'filas q', len(D.qt), 'qt global monotono', bool((np.diff(D.qt) >= 0).all()), 'unidades de t: min %.0f max %.0f' % (D.qt.min(), D.qt.max()))
