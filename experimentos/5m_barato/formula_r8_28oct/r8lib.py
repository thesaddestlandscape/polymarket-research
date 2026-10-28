import sys, os, json, io, contextlib, numpy as np
E4 = '/root/polymarket-research/experimentos/5m_barato/'
for d in ('formula_r7_28oct', 'formula_r6_28oct', 'formula_r5_28oct', 'formula_r4_28oct', 'formula_r3_28oct'): sys.path.insert(0, E4 + d)
import r4, r5f, r6a
from r6a import summ, F, P, signflip_max
BASE = E4 + 'formula_r8_28oct/'
EXTD = {'BTC': E4 + 'formula_r5_28oct/ext/', 'ETH': BASE + 'ext_eth/'}
def days_incl():
    d0 = sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_'))
    with contextlib.redirect_stdout(io.StringIO()): return r5f.inclusion(d0)
def part(days):
    dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
    return dd(6, 15), dd(16, 25), dd(26, 27)
class Day:
    def __init__(self, day, coin='BTC'):
        z = np.load(EXTD[coin] + 'b_%s.npz' % day); Z = {k: z[k] for k in z.files}; self.Z = Z
        self.cie = Z['tok_cie']; self.side = Z['tok_side']; self.comp = Z['tok_comp']; self.mks = Z['tok_mk']; self.n = len(self.cie)
        self.qt, self.qtok, self.qbb, self.qba, self.qbs = Z['qt'], Z['qtok'], Z['qbb'], Z['qba'], Z['qbs']
        self.pt, self.ptok, self.pex, self.ppx, self.psz, self.psd = Z['pt'], Z['ptok'], Z['pex'], Z['ppx'], Z['psz'], Z['psd']
        ids = np.arange(self.n); self.qlo = np.searchsorted(self.qtok, ids, 'left'); self.qhi = np.searchsorted(self.qtok, ids, 'right')
        self.plo = np.searchsorted(self.ptok, ids, 'left'); self.phi = np.searchsorted(self.ptok, ids, 'right')
        self.jd = np.sort(Z['jd']); self.ju = np.sort(Z['ju'])
    def stream(self, u):
        a, b = int(self.plo[u]), int(self.phi[u]); m = self.psd[a:b] == 0
        t = [self.pt[a:b][m]]; e = [self.pex[a:b][m]]; p = [np.round(self.ppx[a:b][m], 2)]; s = [self.psz[a:b][m]]; c = int(self.comp[u])
        if c >= 0:
            a2, b2 = int(self.plo[c]), int(self.phi[c]); m2 = self.psd[a2:b2] == 1
            t.append(self.pt[a2:b2][m2]); e.append(self.pex[a2:b2][m2]); p.append(np.round(1.0 - self.ppx[a2:b2][m2], 2)); s.append(self.psz[a2:b2][m2])
        t = np.concatenate(t); o = np.argsort(t, kind='stable')
        return t[o], np.concatenate(e)[o], np.concatenate(p)[o], np.concatenate(s)[o]
    def l1(self, u, times):
        """L1 (bb, ba, bs) del token u en los instantes 'times' (ultima fila q <= t). NaN si no hay."""
        a, b = int(self.qlo[u]), int(self.qhi[u]); times = np.asarray(times, float); nan = np.full(len(times), np.nan)
        if b <= a: return nan, nan.copy(), nan.copy()
        j = np.searchsorted(self.qt[a:b], times, 'right') - 1; ok = j >= 0; jj = np.clip(j, 0, None) + a
        return np.where(ok, self.qbb[jj], np.nan), np.where(ok, self.qba[jj], np.nan), np.where(ok, self.qbs[jj], np.nan)
def clusters(se, gap=300.0):
    newc = np.r_[True, np.diff(se) > gap]; cid = np.cumsum(newc) - 1; starts = np.flatnonzero(newc); ends = np.r_[starts[1:], len(se)]
    return cid, starts, ends
def fillsrch(st, sp, ta, tgt, life=10000.0, clk=26.0):
    i0 = int(np.searchsorted(st, ta + clk, 'left')); i1 = int(np.searchsorted(st, ta + clk + life, 'left'))
    if i1 <= i0: return -1
    hit = np.flatnonzero(sp[i0:i1] < tgt - 1e-9)
    return (i0 + int(hit[0])) if len(hit) else -1
def stream_src(D, u):
    a, b = int(D.plo[u]), int(D.phi[u]); m = D.psd[a:b] == 0
    t = [D.pt[a:b][m]]; e = [D.pex[a:b][m]]; p = [np.round(D.ppx[a:b][m], 2)]; s = [D.psz[a:b][m]]; o = [np.zeros(int(m.sum()), np.int8)]; c = int(D.comp[u])
    if c >= 0:
        a2, b2 = int(D.plo[c]), int(D.phi[c]); m2 = D.psd[a2:b2] == 1
        t.append(D.pt[a2:b2][m2]); e.append(D.pex[a2:b2][m2]); p.append(np.round(1.0 - D.ppx[a2:b2][m2], 2)); s.append(D.psz[a2:b2][m2]); o.append(np.ones(int(m2.sum()), np.int8))
    t = np.concatenate(t); k = np.argsort(t, kind='stable')
    return t[k], np.concatenate(e)[k], np.concatenate(p)[k], np.concatenate(s)[k], np.concatenate(o)[k]
