"""msdata.py -- acceso a datos/ms_DIA.npz (ordenado por token y RECEPCION). Tiempos en ms absolutos de epoch."""
import os, numpy as np
DD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
class Dia:
    def __init__(self, d):
        z = np.load(os.path.join(DD, f'ms_{d}.npz'), allow_pickle=False)
        self.D0 = int(z['D0']); self.tokens = z['tokens']; self.tmap = z['tmap']
        self.qr = z['qr'].astype(np.int64) + self.D0; self.qk = z['qk']; self.qv = z['qv']
        self.tr = z['tr'].astype(np.int64) + self.D0; self.tk = z['tk']; self.tv = z['tv']
        self.xr = z['xr'].astype(np.int64) + self.D0; self.xk = z['xk']; self.xv = z['xv']
        n = len(self.tokens)
        self.qs = np.searchsorted(self.qk, np.arange(n + 1)); self.ts = np.searchsorted(self.tk, np.arange(n + 1)); self.xs = np.searchsorted(self.xk, np.arange(4))
        self.idx = {}
        for i, (act, marco, mid, fin, lado) in enumerate(self.tmap):
            import pandas as pd
            fe = int(pd.Timestamp(str(fin)).timestamp())
            self.idx[(str(act), str(marco), fe, str(lado))] = i
        self.mid = {i: self.tmap[i][2] for i in range(n)}
    def tok(self, act, marco, fin_s, lado):
        return self.idx.get((act, marco, int(fin_s), lado))
    def top(self, k, t):
        """ultimo top con recepcion <= t: (bid, ask, bsz, asz, recv) o None"""
        a, b = self.qs[k], self.qs[k + 1]
        j = np.searchsorted(self.qr[a:b], t, 'right') - 1
        if j < 0: return None
        v = self.qv[a + j]; return (float(v[0]), float(v[1]), float(v[2]), float(v[3]), int(self.qr[a + j]))
    def trades(self, k, t0, t1):
        a, b = self.ts[k], self.ts[k + 1]; r = self.tr[a:b]
        i0, i1 = np.searchsorted(r, t0, 'right'), np.searchsorted(r, t1, 'right')
        return r[i0:i1], self.tv[a + i0:a + i1]
    def bn(self, sym, t):
        a, b = self.xs[sym], self.xs[sym + 1]
        j = np.searchsorted(self.xr[a:b], t, 'right') - 1
        if j < 0: return None, None
        return float(self.xv[a + j]), int(self.xr[a + j])
SYM = {'ETH': 0, 'SOL': 1, 'XRP': 2}
