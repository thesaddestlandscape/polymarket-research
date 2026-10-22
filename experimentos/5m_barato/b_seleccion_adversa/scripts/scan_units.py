import sys, os, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 200
U = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(B + '/datos/units/units_*.pkl'))], ignore_index=True)
U = U.rename(columns={'p': 'pn'}); U['hb'] = U.hora // 4
feats = ['gap_last', 'dp5', 'dp30', 'dp60', 'hi60', 'rng60', 'd_open', 'vol30', 'blk30', 'vol_all', 'flow60', 'inf120', 'fv_gap', 'z', 'sig_bps_s', 'b10', 'T', 'pc', 'nf']
for f in feats: U[f] = U[f].astype(float)
dis = U.dia.isin(['2026-10-%02d' % d for d in range(9, 16)]).values
Td = U[dis].reset_index(drop=True); Th = U[~dis].reset_index(drop=True)
rules = build_rules(U, feats, dis, {'act': ['ETH', 'SOL', 'XRP'], 'hb': [0, 1, 2, 3, 4, 5]})
res = maxstat(Td, rules, nperm=NP)
Mh = masks(Th, rules); eg_h, eb_h, t_h, ng_h, nb_h, _ = stats(Mh, Th.pn.values, Th.c.values)
out = pd.DataFrame(dict(regla=[r[0] for r in rules], ev_bueno_d=res['eg'], ev_malo_d=res['eb'], t_d=res['t'], n_bueno_d=res['ng'], n_malo_d=res['nb'], p_fw_d=res['p_fw'], valid=res['valid'],
                        ev_bueno_h=eg_h, ev_malo_h=eb_h, t_h=t_h, n_bueno_h=ng_h, n_malo_h=nb_h))
out.to_csv(B + '/datos/scan_units_reglas.csv', index=False)
o = out[out.valid].sort_values('t_d', ascending=False)
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 30)
print('UNIDADES base descubrimiento EV', Td.pn.sum() / Td.c.sum(), 'holdout', Th.pn.sum() / Th.c.sum(), 'N', len(Td), len(Th), 'perms', NP, 'max-null t q95', np.quantile(res['mx'], .95))
print(o.head(22).round(3).to_string()); print('reglas p_fw<0.10:', int((o.p_fw_d < 0.10).sum()), 'de', len(o))
