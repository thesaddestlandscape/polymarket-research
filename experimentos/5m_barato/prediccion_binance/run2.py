from model import *
import sys
# AUC por moneda y baseline solo-moneda, para ver cuánto es información real de Binance
for H in (150, 250, 400):
    d = load(H); tr = d[d.dia.isin(DIAS[:2])].reset_index(drop=True); te = d[d.dia.isin(DIAS[2:])].reset_index(drop=True)
    print(f"\n=== H={H}")
    for tgt in ("Y1", "Y3"):
        s_c, _ = fit_score(tr, te, CODE, tgt, "lin", oof_on=False)
        s_b, _ = fit_score(tr, te, BIN + CODE, tgt, "lin", oof_on=False)
        s_h, _ = fit_score(tr, te, BIN + CODE, tgt, "hgb", oof_on=False)
        print(tgt, "solo-moneda+lado AUC", round(auc(te[tgt].values, s_c), 3), "| BIN lin", round(auc(te[tgt].values, s_b), 3), "hgb", round(auc(te[tgt].values, s_h), 3))
        for c in COINS:
            m = (te.act == c).values
            print("   ", c, "n", m.sum(), "pos", te[tgt].values[m].sum(), "lin", round(auc(te[tgt].values[m], s_b[m]), 3), "hgb", round(auc(te[tgt].values[m], s_h[m]), 3))
