import sys, os, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from simlib import *
import pandas as pd
O3 = O + 'r3_out/'
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O3 + 'mk_*.csv'))])
sel = M[(M.clk == 'rx') & (M.lc == 60) & (M.lleno > 0) & (((M['var'] == 'join') & (M.mq == -0.05)) | ((M['var'] == 'mejora') & (M.mq == -0.05)) | ((M['var'] == 'join_nc') & (M.mq == -0.05)))]
out = []
for D, g in sel.groupby('dia'):
    km = kmap(D); LS = lados(D); B = binance(D)
    want = {(int(r.cierre)): r for r in g.itertuples()}
    cs = set(g.cierre.astype(int))
    for C, QS, TS in grupos(D):
        if C not in cs: continue
        lado, m5 = LS[C]; sl = 'YES' if lado == 'Up' else 'NO'; k5 = km[('5min', C, sl)][0]; q5 = QS[k5]
        for r in g[g.cierre == C].itertuples():
            t = int(r.t_relleno)
            def bid(tt):
                j = q5.i(tt); return q5.bid[j] if j >= 0 else np.nan
            sgn = 1 if lado == 'Up' else -1
            out.append(dict(dia=D, cierre=C, var=r.var, p=r.coste / r.lleno, gana=r.gana, lleno=r.lleno, T=r.T_rel,
                            bid_now=bid(t - 100), d1=bid(t - 100) - bid(t - 1600), d3=bid(t - 100) - bid(t - 3100),
                            bin1=float(sgn * bin_ret(B, np.array([t]), 1000)[0])))
pd.DataFrame(out).to_csv(O3 + 'flash_check.csv', index=False)
print(pd.DataFrame(out).round(3).to_string())
