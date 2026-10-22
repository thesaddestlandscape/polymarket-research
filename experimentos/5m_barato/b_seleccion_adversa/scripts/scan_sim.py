import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NP = int(sys.argv[1]) if len(sys.argv) > 1 else 200
FT = pd.read_pickle(B + '/datos/ft_base.pkl')
dis = FT.dia.isin(['2026-10-%02d' % d for d in range(9, 16)]).values
FT['hb'] = FT.hora // 4
feats = ['dp10', 'dp30', 'dp60', 'dopen', 'hi60', 'v30', 'sh30', 'flow60', 'z', 'ret10', 'sig', 'lastage', 'T', 'p']
for f in feats: FT[f] = FT[f].astype(float)
Td = FT[dis].reset_index(drop=True); Th = FT[~dis].reset_index(drop=True)
rules = build_rules(FT, feats, dis, {'act': ['ETH', 'SOL', 'XRP'], 'hb': [0, 1, 2, 3, 4, 5]})
res = maxstat(Td, rules, nperm=NP)
Mh = masks(Th, rules); eg_h, eb_h, t_h, ng_h, nb_h, _ = stats(Mh, Th.pn.values, Th.c.values)
out = pd.DataFrame(dict(regla=[r[0] for r in rules], ev_bueno_d=res['eg'], ev_malo_d=res['eb'], t_d=res['t'], n_bueno_d=res['ng'], n_malo_d=res['nb'], p_fw_d=res['p_fw'], valid=res['valid'],
                        ev_bueno_h=eg_h, ev_malo_h=eb_h, t_h=t_h, n_bueno_h=ng_h, n_malo_h=nb_h))
out.to_csv(B + '/datos/scan_sim_reglas.csv', index=False)
o = out[out.valid].sort_values('t_d', ascending=False)
pd.set_option('display.width', 250); pd.set_option('display.max_columns', 30)
print('base descubrimiento EV', Td.pn.sum() / Td.c.sum(), 'holdout', Th.pn.sum() / Th.c.sum(), 'N', len(Td), len(Th), 'perms', NP, 'max-null t cuantil95', np.quantile(res['mx'], .95))
print(o.head(25).round(3).to_string())
print('reglas con p_fw<0.10:', int((o.p_fw_d < 0.10).sum()), 'de', len(o))
