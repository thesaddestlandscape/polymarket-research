import numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
F = pd.read_pickle('G0_cxbtrue.pkl'); F = F[F.src != 'sin_evento'].copy(); F['has_trig'] = F.trig_rx.notna()
rng = np.random.default_rng(5); days = sorted(F.dia.unique())
for clock in ('old', 'true'):
  for l in (60, 100, 150):
    tf = F.tf_old if clock == 'old' else F.tf_true
    K = F[~(F.has_trig & (tf > F.trig_rx + l))]
    g = K.groupby('dia').agg(p=('pnl', 'sum'), c=('cost', 'sum')).reindex(days).fillna(0)
    bs = []
    for _ in range(4000):
        s = g.iloc[rng.integers(0, len(g), len(g))]; bs.append(s.p.sum() / max(s.c.sum(), 1e-9))
    top2 = g.sort_values('p').iloc[:-2]
    gc = K.groupby(['dia', 'fin']).pnl.sum()
    print(f'{clock} l={l}: mantenidos n={len(K)} cierres={K.groupby(["dia","fin"]).ngroups} coste={K.cost.sum():.1f} pnl={K.pnl.sum():+.2f} EV/EUR={K.pnl.sum()/K.cost.sum():+.4f} IC90dias=[{np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}] dias+={int((g.p>0).sum())}/15 sin2mejores EV={top2.p.sum()/top2.c.sum():+.4f} acierto={K.gana.mean():.3f} precio_medio={K.L.mean():.3f}')
