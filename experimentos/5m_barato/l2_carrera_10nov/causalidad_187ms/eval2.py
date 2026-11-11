import numpy as np, pandas as pd, glob
pd.set_option('future.infer_string', False)
F = pd.read_pickle('G0_cxbtrue.pkl'); F = F[F.src != 'sin_evento'].copy(); F['has_trig'] = F.trig_rx.notna()
rng = np.random.default_rng(11); days = sorted(F.dia.unique())
for l in (60, 100, 150, 300):
    ao = F.has_trig & (F.tf_old > F.trig_rx + l); at = F.has_trig & (F.tf_true > F.trig_rx + l)
    inc = F[at & ~ao]; dec = F[ao & ~at]
    v = inc.groupby('dia').pnl.sum().reindex(days).fillna(0).values
    bs = [rng.choice(v, len(v)).sum() for _ in range(4000)]
    print(f'l={l}: nuevos evitados (true no old) n={len(inc)} cost={inc.cost.sum():.1f} pnl={inc.pnl.sum():+.2f} EV/EUR={inc.pnl.sum()/max(inc.cost.sum(),1e-9):+.3f} acierto={inc.gana.mean():.3f} IC90 dias pnl=[{np.percentile(bs,5):+.1f},{np.percentile(bs,95):+.1f}] dias_pnl<0={int((v<0).sum())}/15 | dejan de evitarse n={len(dec)} pnl={dec.pnl.sum():+.2f}; ftype nuevos {inc.ftype.value_counts().to_dict()} src {inc.src.value_counts().to_dict()}')
# trig - tf distribucion para fills con tf_true-trig in (-1000, 1000)
x = (F.tf_true - F.trig_rx)[F.has_trig]; print('tf_true - trig_rx: frac <0', round(float((x<0).mean()),3), 'frac 0-60', round(float(((x>=0)&(x<60)).mean()),3), '60-150', round(float(((x>=60)&(x<150)).mean()),3), '150-400', round(float(((x>=150)&(x<400)).mean()),3), '>=400', round(float((x>=400).mean()),3))
y = (F.tf_old - F.trig_rx)[F.has_trig]; print('tf_old  - trig_rx: frac <0', round(float((y<0).mean()),3), 'frac 0-60', round(float(((y>=0)&(y<60)).mean()),3), '60-150', round(float(((y>=60)&(y<150)).mean()),3), '150-400', round(float(((y>=150)&(y<400)).mean()),3), '>=400', round(float((y>=400).mean()),3))
# passT CXB (reloj old) para validar la aproximacion
R = []
for f in sorted(glob.glob('/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/out_v2/RT_causal_2026-1*.pkl')):
    r = pd.read_pickle(f); r = r[r['var'].isin(['G0', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000', 'PCXB300_1', 'PCXB300_2'])][['var', 'dia', 'pnl', 'cost', 'gana']]
    R.append(r.astype({'var': object, 'dia': object}))
R = pd.concat(R); print(R.groupby('var').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), cost=('cost', 'sum')).assign(ev=lambda t: t.pnl / t.cost).round(3).to_string())
