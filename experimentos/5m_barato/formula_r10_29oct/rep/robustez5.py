import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
exec(open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez3.py').read().split("rows = isI & v3 & T")[0])
print('y unique', np.unique(y)[:5], 'mean', y.mean())
for nm, ds in (('IS', isI), ('OOS', isO)):
    print(nm)
    for lo_, hi_ in ((.10, .16), (.16, .22), (.22, .28), (.28, .32), (.32, .36)):
        m1 = T & ds & (bb >= lo_) & (bb < hi_); m2 = m1 & (bid15 <= .51); m3 = m2 & (cbb > .66); m4 = m1 & (bid15 > .51)
        print('  bb[%.2f,%.2f) y all %.3f n%d | bid15<=.51 %.3f n%d | & cbb>.66 %.3f n%d | bid15>.51 %.3f n%d | mean bid15 %.3f cbb %.3f' % (lo_, hi_, y[m1].mean(), m1.sum(), y[m2].mean() if m2.sum() else np.nan, m2.sum(), y[m3].mean() if m3.sum() else np.nan, m3.sum(), y[m4].mean() if m4.sum() else np.nan, m4.sum(), np.nanmean(bid15[m1]), np.nanmean(cbb[m1])))
# distinct markets/(dia,token) in leaf
LEAF = T & (bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28); k = np.unique(np.c_[di[LEAF], u[LEAF]], axis=0); print('LEAF filas', LEAF.sum(), '(dia,token) distintos', len(k), 'y medio por (dia,token):', np.mean([y[LEAF & (di == a) & (u == b)].mean() for a, b in k[:3000]]))
# bid15 vs bb: relacion en leaf, y por dia
for d in range(nd):
    m = LEAF & (di == d); print(days[d][-2:], m.sum(), '%.2f' % y[m].mean() if m.sum() else '-', end=' | ')
print()
print('tg[:,2] vs bb - 0.03 check', np.nanmedian(tg[LEAF, 2] - (bb[LEAF] - 0.03)))
