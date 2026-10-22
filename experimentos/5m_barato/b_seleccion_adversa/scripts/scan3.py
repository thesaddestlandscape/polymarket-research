"""scan3.py -- walk-forward en 3 periodos (A 09-13 descubrimiento, B 14-17 replicacion, C 18-21 test virgen). Poblacion (unidades) -- reglas de scan_units."""
import sys, os, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NP = int(sys.argv[1])
U = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(B + '/datos/units/units_*.pkl'))], ignore_index=True)
U = U.rename(columns={'p': 'pn'}); U['hb'] = U.hora // 4
feats = ['gap_last', 'dp5', 'dp30', 'dp60', 'hi60', 'rng60', 'd_open', 'vol30', 'blk30', 'vol_all', 'flow60', 'inf120', 'fv_gap', 'z', 'sig_bps_s', 'b10', 'T', 'pc', 'nf']
for f in feats: U[f] = U[f].astype(float)
dn = U.dia.str[-2:].astype(int)
A = (dn <= 13).values; Bp = ((dn >= 14) & (dn <= 17)).values; C = (dn >= 18).values
rules = build_rules(U, feats, A, {'act': ['ETH', 'SOL', 'XRP'], 'hb': [0, 1, 2, 3, 4, 5]})
TA, TB, TC = (U[m].reset_index(drop=True) for m in (A, Bp, C))
res = maxstat(TA, rules, nperm=NP, seed=11)
def st(T):
    return stats(masks(T, rules), T.pn.values, T.c.values)
eB = st(TB); eC = st(TC)
out = pd.DataFrame(dict(regla=[r[0] for r in rules], evg_A=res['eg'], evb_A=res['eb'], t_A=res['t'], p_fw_A=res['p_fw'], valid=res['valid'],
                        evg_B=eB[0], evb_B=eB[1], t_B=eB[2], ng_B=eB[3], evg_C=eC[0], evb_C=eC[1], t_C=eC[2], ng_C=eC[3], nb_C=eC[4]))
out.to_csv(B + '/datos/scan3_units_reglas.csv', index=False)
print('base EV A/B/C', TA.pn.sum() / TA.c.sum(), TB.pn.sum() / TB.c.sum(), TC.pn.sum() / TC.c.sum(), 'N', len(TA), len(TB), len(TC), 'max-null q95', np.quantile(res['mx'], .95))
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 30)
o = out[out.valid & (out.p_fw_A < 0.10)].sort_values('t_A', ascending=False)
print(o.round(3).to_string()); print('p_fw_A<0.10:', len(o), ' de ellas t_B>1.645:', int((o.t_B > 1.645).sum()), ' y t_C>1.645:', int(((o.t_B > 1.645) & (o.t_C > 1.645)).sum()))
