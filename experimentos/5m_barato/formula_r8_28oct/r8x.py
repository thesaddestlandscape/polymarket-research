#!/usr/bin/env python3
"""r8x: Bloque 1 (auditoria del reloj de bb). Manda PREREG_FORMULA_R8.md."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
G = json.load(open(r4.I.CACHE)); days = days_incl(); nd = len(days); IS, OOS, DEV = part(days)
A = {k: [] for k in ('di', 'ctx2', 'ctx8', 'p', 'sz', 'y', 'dR6', 'dnow', 'dpre', 'cbef')}; T = {'di': [], 'ask': [], 'y': [], 'p0': [], 'pk': []}
for di, d in enumerate(days):
    D = Day(d, 'BTC')
    for u in range(D.n):
        win = G.get(str(D.mks[u]))
        if win not in ('YES', 'NO') or D.qhi[u] <= D.qlo[u]: continue
        y = 1.0 if win == ('YES' if D.side[u] == 0 else 'NO') else 0.0
        st, se, sp, ss = D.stream(u)
        if len(st) == 0: continue
        cid, starts, ends = clusters(se); K = len(starts); tot = np.bincount(cid, weights=ss, minlength=K); cst = st[starts]
        bR6 = D.l1(u, st - 300.0)[0]; bnow = D.l1(u, st - 5.0)[0]; bpre = D.l1(u, cst - 50.0)[0][cid]
        cum = np.cumsum(ss); cb = cum - ss - (cum[starts] - ss[starts])[cid]
        z = (sp >= 0.09 - 1e-9) & (sp <= 0.31 + 1e-9)
        if z.any():
            f = lambda b: np.where(np.isfinite(b), np.round((sp - b) / 0.01), np.nan)
            n = int(z.sum()); A['di'].append(np.full(n, di)); A['ctx2'].append((tot[cid] >= 200)[z]); A['ctx8'].append((tot[cid] >= 800)[z]); A['p'].append(sp[z]); A['sz'].append(ss[z]); A['y'].append(np.full(n, y))
            A['dR6'].append(f(bR6)[z]); A['dnow'].append(f(bnow)[z]); A['dpre'].append(f(bpre)[z]); A['cbef'].append(cb[z])
        # tomador tras armar (>=100 acc en <=2 s, primer precio en [0,10,0,35]) con ask de L1 a t_d+215 ms
        for c in range(K):
            s0, e0 = starts[c], ends[c]
            if not (0.10 <= sp[s0] <= 0.35): continue
            cu = np.cumsum(ss[s0:e0]); dur = se[s0:e0] - se[s0]; k = int(np.searchsorted(cu, 100.0, 'left'))
            if k >= len(cu) or dur[k] > 2000.0: continue
            td = st[s0 + k] + 5.0; ask = float(D.l1(u, [td + 215.0])[1][0])
            if np.isfinite(ask) and 0.05 <= ask <= 0.45: T['di'].append(di); T['ask'].append(ask); T['y'].append(y); T['p0'].append(sp[s0]); T['pk'].append(sp[s0 + k])
    print(d, len(np.concatenate(A['di'])), flush=True)
A = {k: np.concatenate(v) for k, v in A.items()}; T = {k: np.array(v) for k, v in T.items()}
R = dict(di=A['di'], num=A['sz'] * (A['y'] - A['p']), den=A['sz'] * A['p'])
def cls(d):
    return np.where(~np.isfinite(d), 4, np.where(d >= 1, 0, np.where(d == 0, 1, np.where(d >= -2, 2, np.where(d >= -4, 3, 4)))))
lab = ['>=+1', '0 (en bb)', '-1..-2', '-3..-4', '<=-5/sin libro']
P('== R8 Bloque 1: auditoria reloj bb (prints con reloj de recepcion exacto; BTC 5m; zona .09-.31). EV/E por profundidad segun referencia')
for cn, cm in (('DENTRO barrido (cluster>=200 acc)', A['ctx2']), ('DENTRO barrido>=800', A['ctx8']), ('FUERA de barrido', ~A['ctx2'])):
    for rn, rk in (('D_R6 = p-bb(t-300ms)', 'dR6'), ('D_now = p-bb(t-5ms)', 'dnow'), ('D_pre = p-bb(inicio cluster-50ms)', 'dpre')):
        c = cls(A[rk]); P(' [%s | %s]' % (cn, rn))
        for k in range(5):
            m = cm & (c == k); o = []
            for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
                s = summ(R, m, ds, nd); o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d %.0fEUR/d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['eurd'])) if s else '-'))
            P('   %-16s %s' % (lab[k], ' | '.join(o)))
P(' [quien llega al nivel: dentro>=200, D_pre, por acc ya barridas antes del print en el cluster]')
for lo_, hi_ in ((0, 1), (1, 100), (100, 400), (400, 1e9)):
    m = A['ctx2'] & (A['cbef'] >= lo_) & (A['cbef'] < hi_); o = []
    for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
        s = summ(R, m, ds, nd); o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'])) if s else '-'))
    P('   acc previas [%g,%g): %s' % (lo_, hi_, ' | '.join(o)))
fee = 0.07 * T['ask'] * (1 - T['ask']); Rt = dict(di=T['di'], num=(T['y'] - T['ask'] - fee), den=T['ask'])
P(' [TOMADOR tras armar (>=100 acc/2 s) al ask L1 a t_d+215 ms, comision 0,07*p*(1-p); 1 acc]')
for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
    P('   %s: %s | eventos/d %.0f' % (pn, F(summ(Rt, np.ones(len(T['di']), bool), ds, nd)), np.isin(T['di'], ds).sum() / len(ds)))
open(BASE + 'salida_r8x.txt', 'w').write('\n'.join(r6a.LINES))
