import sys, os, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from scanlib import *; from sa_common import *
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = pd.concat([pd.read_csv(f) for f in sorted(glob.glob('/root/polymarket-research-datalogs/sa_r1/btc/units2_*.csv.gz'))], ignore_index=True).rename(columns={'p': 'pn'})
U = U[U.b15.notna()].copy(); U['dia'] = U.dia.astype(str); dn = U.dia.str[-2:].astype(int); dis = (dn <= 19).values; U['hb'] = U.hora // 4
print('BTC 5m unidades con bid15:', len(U), 'EUR', round(U.c.sum()), 'unid/dia', round(len(U) / U.dia.nunique()), 'EUR/dia', round(U.c.sum() / U.dia.nunique()), 'EV todas %+.3f' % (U.pn.sum() / U.c.sum()))
for nm, m in (('todas', np.ones(len(U), bool)), ('A lvl15<=0.03', U.A), ('no A', ~U.A), ('R1ws', U.R1ws), ('A & R1ws', U.A & U.R1ws), ('vol30ws>=26', U.vol30ws >= 26)):
    m = np.asarray(m); r = day_boot(U[m], 'pn', 'c', 'dia'); print('%-16s %s | ret %.2f | por dia %s' % (nm, fmt(r), U.c[m].sum() / U.c.sum(), {d[-2:]: round(g.pn.sum() / g.c.sum(), 3) for d, g in U[m].groupby('dia')}))
feats = ['lvl15', 'spread', 'vol30ws', 'vol30', 'bs', 'T', 'pc', 'hora']
rules = build_rules(U, feats, dis, {'hb': [0, 1, 2, 3, 4, 5]}); Td, Th = U[dis].reset_index(drop=True), U[~dis].reset_index(drop=True)
res = maxstat(Td, rules, nperm=200, seed=2); eh = stats(masks(Th, rules), Th.pn.values, Th.c.values)
o = pd.DataFrame(dict(regla=[r[0] for r in rules], evg_d=res['eg'], evb_d=res['eb'], t_d=res['t'], p_fw=res['p_fw'], valid=res['valid'], evg_h=eh[0], evb_h=eh[1], t_h=eh[2]))
pd.set_option('display.width', 200); print(o[o.valid].sort_values('t_d', ascending=False).head(10).round(3).to_string())
