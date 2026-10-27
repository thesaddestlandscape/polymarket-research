import sys, numpy as np, pandas as pd
sys.path.insert(0, '.'); from v2lib import *
B = pd.read_parquet(DL + 'ordenes_b.parquet'); X = pd.read_parquet(DL + 'v2/diag_tune.parquet')
d = Dia('2026-10-20'); g = B[B.dia == '2026-10-20']
print('tokens B', g.tok.nunique(), 'con comp', sum(t in d.comp for t in g.tok.unique()), 'con prints', sum(t in d.tr for t in g.tok.unique()), 'comp con prints', sum((d.comp.get(t) in d.tr) for t in g.tok.unique()))
miss = X[(X.fill == 1) & (X.n_cons5 == 0) & (X.dia == '2026-10-20')]
for r in miss.head(4).itertuples():
    b = B[B.oid == r.oid].iloc[0]; print(b.slug, b.lado, b.tok[:8], 'comp', (d.comp.get(b.tok) or 'NONE')[:8], 'n prints tok', len(d.tr.get(b.tok, [])), 'n prints comp', len(d.tr.get(d.comp.get(b.tok), [])), 'n q tok', len(d.q.get(b.tok, [])))
    a = d.tr.get(b.tok); 
    if a is not None: print('   rango prints rel a ti (s):', (a[0, 0] - b.t_ini * 1000) / 1000, (a[-1, 0] - b.t_ini * 1000) / 1000)
