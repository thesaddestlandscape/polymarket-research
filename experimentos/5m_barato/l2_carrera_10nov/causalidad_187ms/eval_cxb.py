import numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
F = pd.read_pickle('G0_cxbtrue.pkl'); F = F[F.src != 'sin_evento'].copy()
F['sh'] = F.tf_true - F.tf_old
def pc(v, q=(5, 25, 50, 75, 95)): v = np.asarray(v, float); v = v[np.isfinite(v)]; return [round(float(np.percentile(v, x))) for x in q] if len(v) else None
print('n', len(F), 'by src', F.src.value_counts().to_dict(), 'amb', round(F.amb.mean(), 3))
for s, g in F.groupby('src'): print(' shift tf_true-tf_old', s, pc(g.sh), 'ftype', g.ftype.value_counts().to_dict())
print('ftype x src shift p50', F.groupby(['ftype', 'src']).sh.median().to_dict())
F['has_trig'] = F.trig_rx.notna()
print('trig exists', round(F.has_trig.mean(), 3), 'by ftype', F.groupby('ftype').has_trig.mean().round(3).to_dict())
print('trig_rx - tf_true (ms) when trig', pc((F.trig_rx - F.tf_true)[F.has_trig]))
print('TOTAL G0: n', len(F), 'cost', round(F.cost.sum(), 2), 'pnl', round(F.pnl.sum(), 2), 'EV/EUR', round(F.pnl.sum() / F.cost.sum(), 4))
days = sorted(F.dia.unique()); rng = np.random.default_rng(7)
def boot_days(dd):   # dd: DataFrame dia, pnl_delta, cost ; IC90 por dias del Delta total
    g = dd.groupby('dia').agg(p=('dp', 'sum')); v = g.p.reindex(days).fillna(0).values
    bs = [rng.choice(v, len(v)).sum() for _ in range(4000)]; return round(float(v.sum()), 2), [round(float(np.percentile(bs, 5)), 2), round(float(np.percentile(bs, 95)), 2)], int((v > 0).sum()), round(float(np.sort(v)[:-2].sum()), 2)
for clock in ('old', 'true'):
    for l in (60, 100, 150, 300):
        tf = F.tf_old if clock == 'old' else F.tf_true
        av = F.has_trig & (tf > F.trig_rx + l)
        A = F[av]; K = F[~av]
        dp = pd.DataFrame({'dia': F.dia, 'dp': np.where(av, -F.pnl, 0.0)})
        tot, ic, dpos, sin2 = boot_days(dp)
        # placebo igual cobertura estratificado dia x L
        n_by = A.groupby(['dia', 'L']).size()
        pl = []
        grp = {k: g.pnl.values for k, g in F.groupby(['dia', 'L'])}
        for _ in range(2000):
            s = 0.0
            for key, n in n_by.items():
                v = grp[key]; s -= rng.choice(v, n, replace=False).sum()
            pl.append(s)
        pl = np.array(pl); p_perm = float((pl >= tot).mean())
        print(f'{clock:4s} l={l:3d} evitados n={len(A)} ({len(A)/len(F):.1%}) EV/EUR evitados={A.pnl.sum()/max(A.cost.sum(),1e-9):+.4f} acierto={A.gana.mean():.3f} | mantenidos n={len(K)} EV/EUR={K.pnl.sum()/K.cost.sum():+.4f} | Delta={tot:+.2f} EUR IC90dias={ic} dias+={dpos}/15 sin2mejores={sin2:+.2f} | placebo p50={np.median(pl):+.2f} p95={np.percentile(pl,95):+.2f} p={p_perm:.3f}')
# by ftype for true l=100
av = F.has_trig & (F.tf_true > F.trig_rx + 100)
print('true l=100 by ftype', F[av].groupby('ftype').apply(lambda g: (len(g), round(g.pnl.sum() / g.cost.sum(), 3))).to_dict())
print('true l=100 by act', F[av].groupby('act').apply(lambda g: (len(g), round(g.pnl.sum(), 2), round(g.pnl.sum() / g.cost.sum(), 3))).to_dict())
print('true l=100 by L', F[av].groupby('L').apply(lambda g: (len(g), round(g.pnl.sum(), 2), round(g.pnl.sum() / g.cost.sum(), 3))).to_dict())
print('true l=100 by dia', F[av].groupby('dia').apply(lambda g: (len(g), round(g.pnl.sum(), 2))).to_dict())
# por cierre (fin) n efectivo
print('cierres distintos evitados', F[av].fin.nunique(), 'tokens', F[av].groupby(['dia','k']).ngroups)
