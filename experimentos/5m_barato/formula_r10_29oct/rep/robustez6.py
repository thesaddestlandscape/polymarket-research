import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
exec(open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez3.py').read().split("rows = isI & v3 & T")[0])
LEAF = T & (bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28); REST = T & (bid15 <= 0.51) & (cbb <= 0.66) & (bb > 0.28)
for dd_ in (1, 5, 14):
    D = Day(days[dd_], 'BTC')
    for nm, M_ in (('LEAF', LEAF), ('REST(cbb<=.66)', REST)):
        w = np.flatnonzero(M_ & (di == dd_)); w = w[::max(1, len(w) // 400)]; rec = []
        for r in w:
            c = int(D.comp[int(u[r])]); 
            if c < 0: continue
            cb, ca, _ = D.l1(c, [t[r]]); b_, a_, _ = D.l1(int(u[r]), [t[r]])
            same = (D.mks[int(u[r])] == D.mks[c]); rec.append((same, D.side[int(u[r])] != D.side[c], cb[0], ca[0], b_[0], a_[0], t[r] - 0, y[r]))
        A = np.array(rec, float); print(days[dd_], nm, 'n', len(A), 'mismo mercado %.2f lado distinto %.2f | med cb %.3f ca %.3f bb %.3f ba %.3f | 1-ca %.3f 1-cb %.3f | incoherencia mediana (bb-(1-ca)) %.3f | y %.2f' % (A[:, 0].mean(), A[:, 1].mean(), *np.nanmedian(A[:, 2:6], 0), np.nanmedian(1 - A[:, 3]), np.nanmedian(1 - A[:, 2]), np.nanmedian(A[:, 4] - (1 - A[:, 3])), A[:, 7].mean()))
