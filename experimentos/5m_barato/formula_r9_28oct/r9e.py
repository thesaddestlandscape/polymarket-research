#!/usr/bin/env python3
"""r9e: E6 exploratorio (A2). Reutiliza fills_r9_BTC.npz."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
Z = np.load(BASE + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days)
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; C = list(Z['cols']); F_ = Z['F'].astype(float); bb = F_[:, C.index('bb')]; tr = F_[:, C.index('trem')]; bs = F_[:, C.index('bs')]
MN = np.load(E4 + 'formula_r9_28oct/fills_r9_BTC.npz')['MN'][:, 1]; isI = np.isin(di, IS); b1, b2 = np.nanquantile(bs[isI], [1 / 3, 2 / 3])
def ded(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
P('== R9 E6 (exploratorio, A2) toque vs estricto, vida 10 s, SIEMPRE; IS elige, OOS solo lectura')
for m in range(1, 7):
    g = np.round(bb - m * 0.01, 2); v = (g >= 0.09 - 1e-9) & (g <= 0.29 + 1e-9); k = ded(v); ft = k & (MN <= g + 1e-9); fs = k & (MN < g - 1e-9); fo = ft & ~fs
    R = dict(di=di, num=np.where(ft, 10 * (y - g), 0.0), den=np.where(ft, 10 * g, 0.0))
    red = np.abs(np.round(g * 20) - g * 20) < 1e-6
    cells = {'redondo': red, 'no-redondo': ~red, 'T<60': tr < 60, 'T60-120': (tr >= 60) & (tr < 120), 'T>=120': tr >= 120, 'bs-bajo': bs < b1, 'bs-medio': (bs >= b1) & (bs < b2), 'bs-alto': bs >= b2}
    o = []
    for nm, c in cells.items():
        sI = summ(R, ft & c, IS, nd); sO = summ(R, ft & c, OOS, nd); fr = (fo & c & isI).sum() / max(1, (ft & c & isI).sum())
        o.append('%s solo/toque %.2f IS %+.3f OOS %+.3f' % (nm, fr, sI['pool'] if sI else np.nan, sO['pool'] if sO else np.nan))
    P('  m=%d: %s' % (m, ' ; '.join(o)))
open(E4 + 'formula_r9_28oct/salida_r9e.txt', 'w').write('\n'.join(r6a.LINES))
