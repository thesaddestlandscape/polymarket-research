import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
G = json.load(open(r4.I.CACHE)); days = days_incl(); IS, OOS, DEV = part(days); nd = len(days)
A = {k: [] for k in ('di', 'p', 'sz', 'y', 'dn', 'src', 'ctx')}
for di, d in enumerate(days):
    D = Day(d, 'BTC')
    for u in range(D.n):
        win = G.get(str(D.mks[u]))
        if win not in ('YES', 'NO') or D.qhi[u] <= D.qlo[u]: continue
        y = 1.0 if win == ('YES' if D.side[u] == 0 else 'NO') else 0.0
        st, se, sp, ss, so = stream_src(D, u)
        if len(st) == 0: continue
        cid, starts, ends = clusters(se); tot = np.bincount(cid, weights=ss, minlength=len(starts)); z = (sp >= 0.09) & (sp <= 0.31)
        if not z.any(): continue
        bnow = D.l1(u, st - 5.0)[0]; dn = np.where(np.isfinite(bnow), np.round((sp - bnow) / 0.01), np.nan)
        n = int(z.sum()); A['di'].append(np.full(n, di)); A['p'].append(sp[z]); A['sz'].append(ss[z]); A['y'].append(np.full(n, y)); A['dn'].append(dn[z]); A['src'].append(so[z]); A['ctx'].append((tot[cid] >= 200)[z])
A = {k: np.concatenate(v) for k, v in A.items()}; R = dict(di=A['di'], num=A['sz'] * (A['y'] - A['p']), den=A['sz'] * A['p'])
cl = np.where(~np.isfinite(A['dn']), 4, np.where(A['dn'] >= 1, 0, np.where(A['dn'] == 0, 1, np.where(A['dn'] >= -2, 2, np.where(A['dn'] >= -4, 3, 4)))))
lab = ['>=+1', '0', '-1..-2', '-3..-4', '<=-5/sin libro']
P('== R8 Bloque 1c: origen del print (SELL del token u frente a BUY del complementario mapeado a 1-p) x D_now, dentro de barrido >=200')
for sn, sm in (('SELL del token barato', A['src'] == 0), ('BUY del complementario mapeado', A['src'] == 1)):
    P(' [%s] fraccion de prints %.1f %% ; de los D_now<=−3: %.1f %%' % (sn, 100 * (A['ctx'] & sm).sum() / A['ctx'].sum(), 100 * (A['ctx'] & sm & (A['dn'] <= -3)).sum() / max(1, (A['ctx'] & (A['dn'] <= -3)).sum())))
    for k in range(5):
        m = A['ctx'] & sm & (cl == k); o = []
        for pn, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV)):
            s = summ(R, m, ds, nd); o.append('%s %s' % (pn, ('%+.3f [%+.3f,%+.3f] +%d/%d %.0fEUR/d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['eurd'])) if s else '-'))
        P('   %-16s %s' % (lab[k], ' | '.join(o)))
open(BASE + 'salida_r8x3.txt', 'w').write('\n'.join(r6a.LINES))
