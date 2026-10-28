import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
G = json.load(open(r4.I.CACHE)); days = days_incl(); IS, OOS, DEV = part(days); nd = len(days)
rows = []
for di, d in enumerate(days):
    D = Day(d, 'BTC')
    for u in range(D.n):
        win = G.get(str(D.mks[u]))
        if win not in ('YES', 'NO') or D.qhi[u] <= D.qlo[u]: continue
        st, se, sp, ss = D.stream(u)
        if len(st) == 0: continue
        cid, starts, ends = clusters(se); tot = np.bincount(cid, weights=ss, minlength=len(starts))
        z = (sp >= 0.09) & (sp <= 0.31) & (tot[cid] >= 200)
        if not z.any(): continue
        bnow = D.l1(u, st - 5.0)[0]; b50 = D.l1(u, st + 50.0)[0]; b300 = D.l1(u, st + 300.0)[0]
        # latencia de la primera fila q posterior al print
        a, b = int(D.qlo[u]), int(D.qhi[u]); qq = D.qt[a:b]; j = np.searchsorted(qq, st, 'right'); lagq = np.where(j < len(qq), qq[np.clip(j, 0, len(qq) - 1)] - st, np.nan)
        dn = np.round((sp - bnow) / 0.01)
        rows.append(np.vstack([np.full(z.sum(), di), dn[z], ((b50 - sp) / 0.01)[z], ((b300 - sp) / 0.01)[z], lagq[z]]).T)
M = np.vstack(rows); P('== R8 Bloque 1b: ¿el deficit de L1 es retraso de la actualizacion? (prints dentro de barrido >=200)')
for lab, m in (('D_now>=−2 (L1 coherente)', M[:, 1] >= -2), ('D_now −3..−4', (M[:, 1] <= -3) & (M[:, 1] >= -4)), ('D_now<=−5', M[:, 1] <= -5)):
    P('  %-26s n=%d | bb(t+50ms)−p en ticks: mediana %.1f | bb(t+300ms)−p: mediana %.1f, %% con bb(t+300)<=p: %.1f %% | retardo de la 1a fila q tras el print: p50 %.0f ms p90 %.0f ms' % (lab, m.sum(), np.nanmedian(M[m, 2]), np.nanmedian(M[m, 3]), 100 * np.nanmean(M[m, 3] <= 0), np.nanmedian(M[m, 4]), np.nanpercentile(M[m, 4], 90)))
open(BASE + 'salida_r8x2.txt', 'w').write('\n'.join(r6a.LINES))
