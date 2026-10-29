import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
exec(open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez3.py').read().split("rows = isI & v3 & T")[0])
rows = isI & v3 & T; sm = bb + cbb
LEAF = T & (bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28)
P('== G) hoja rentable: T200-286 & bid15<=0.51 & cbb>0.66 & bb>0.28 (bb<=0.35 por construccion de la banda)')
rep(LEAF, 'LEAF'); 
for lo_, hi_ in ((0, .95), (.95, .97), (.97, .99), (.99, 1.001), (1.001, 2)):
    with np.errstate(invalid='ignore'): rep(LEAF & (sm > lo_) & (sm <= hi_), '  LEAF & bb+cbb in (%.3f,%.3f]' % (lo_, hi_))
a, kp = evm(LEAF, 2, OO); f = fl[:, 2] & kp & LEAF & isO
P('  en OOS: ordenes %d rellenos %d; precio medio objetivo %.3f; y medio de rellenos %.3f; y medio de ordenes (hubiera ganado, rellenada o no) %.3f' % ((kp & LEAF & isO).sum(), f.sum(), tg[f, 2].mean(), y[f].mean(), y[kp & LEAF & isO].mean()))
fi = fl[:, 2] & kp & LEAF & isI; P('  en IS: rellenos %d precio %.3f y %.3f; ordenes y %.3f' % (fi.sum(), tg[fi, 2].mean(), y[fi].mean(), y[kp & LEAF & isI].mean()))
P('  bb+cbb mediana rellenos %.3f ; bid15 mediana %.3f ; bb %.3f ; cbb %.3f ; spr %.3f' % tuple(np.nanmedian(x[f]) for x in (sm, bid15, bb, cbb, col('spr'))))
P('  y medio (ganar) de TODAS las filas T200-286 con bid15<=0.51 & bb en [0.28,0.35] por cbb: ' + ' '.join('cbb(%.2f,%.2f]: %.3f n%d' % (a_, b_, y[T & (bid15 <= .51) & (bb > .28) & (cbb > a_) & (cbb <= b_)].mean(), (T & (bid15 <= .51) & (bb > .28) & (cbb > a_) & (cbb <= b_)).sum()) for a_, b_ in ((0, .5), (.5, .6), (.6, .66), (.66, .72), (.72, .8), (.8, 1))))
# origen de relleno y tipo de dia
import collections
srcs = collections.Counter(); 
for dd_ in sorted(set(di[f].tolist())):
    D = Day(days[dd_], 'BTC')
    for r in np.flatnonzero(f & (di == dd_)):
        st, se, sp, ss, so = stream_src(D, int(u[r])); j = fillsrch(st, sp, t[r] + 73.0, tg[r, 2]); srcs[int(so[j]) if j >= 0 else -1] += 1
P('  origen del print que rellena (OOS, 0 propio / 1 complementario / -1 no hallado): %s' % dict(srcs))
open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/salida_robustez4.txt', 'w').write('\n'.join(L))
