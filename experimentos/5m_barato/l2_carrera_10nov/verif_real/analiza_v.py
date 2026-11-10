import pandas as pd, numpy as np, glob
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(__file__.rsplit('/',1)[0] + '/out/V_*.pkl'))], ignore_index=True)
R['vida'] = (R.t_fuera - R.t_ini) / 1000.0
def conf(df, col, tag):
    s = df[col] > 1e-9; r = df.real_fill == 1; tp = int((s & r).sum()); fp = int((s & ~r).sum()); fn = int((~s & r).sum())
    return dict(tag=tag, n=len(df), real=int(r.sum()), sim=int(s.sum()), tp=tp, prec=round(tp / max(tp + fp, 1), 3), rec=round(tp / max(tp + fn, 1), 3))
print('cov', R['cov'].value_counts().to_dict())
Rk = R[R['cov'] == 'ok']
for col in ('BASE_f_q', 'OPT_f_q', 'CONS_f_q', 'BASE_n_q'):
    print(conf(Rk, col, col + ' todas'))
    print(conf(Rk[Rk.vida >= 1.5], col, col + ' vida>=1.5'))
for c, g in Rk.groupby('coin'): print(conf(g, 'BASE_f_q', 'BASE por moneda ' + c))
for d, g in Rk.groupby('dia'): print(conf(g, 'BASE_f_q', 'BASE dia ' + d))
print('vida mediana', Rk.vida.median(), 'n vida>=1.5', int((Rk.vida >= 1.5).sum()), 'reales con vida>=1.5', int(Rk[(Rk.vida>=1.5)].real_fill.sum()))
print('mercados distintos (slug? por t_fuera//300)', Rk.groupby(['dia','coin']).size().shape)
# tamano y precio de relleno
tp = Rk[(Rk.BASE_f_q > 1e-9) & (Rk.real_fill == 1)]
print('TP: n', len(tp), 'q sim==real', float((np.isclose(tp.BASE_f_q, tp.real_q, atol=1e-6)).mean()), 'q sim/real med', float((tp.BASE_f_q / tp.real_q).median()), 'real_q mean', tp.real_q.mean(), 'sim q mean', tp.BASE_f_q.mean())
print('sim total acc', Rk.BASE_f_q.sum(), 'real total acc', Rk.real_q.sum())
# precio: motor llena a L o por debajo (barrido): compare 
# tiempo
a = tp[tp.t_own_print > 0].copy(); a['d_print'] = a.BASE_f_tf - (a.t_own_print - 63)
print('dt tf_sim - (print propio-63) n', len(a), a.d_print.describe(percentiles=[.05,.25,.5,.75,.95]).round(0).to_dict())
a['dentro'] = (a.BASE_f_tf >= a.t_ini) & (a.BASE_f_tf <= a.t_fuera)
print('tf sim dentro de vida real', float(a.dentro.mean()))
a2 = tp[tp.ts_oc.notna()].copy(); a2['d_blk'] = a2.BASE_f_tf - (a2.ts_oc * 1000 - 2250); print('dt tf_sim - bloque(-2.25s) mediana', a2.d_blk.median(), 'p5/p95', a2.d_blk.quantile([.05,.95]).tolist())
# EV: pnl por orden real y simulado (gana lado, fee maker rebate 0.2*0.07*L*(1-L) como passT)
def pnl(q, L, gana): return q * (gana - L) + q * 0.2 * 0.07 * L * (1 - L)
Rk = Rk.assign(pnl_real=pnl(Rk.real_q, Rk.L, Rk.gana), pnl_sim=pnl(Rk.BASE_f_q, Rk.L, Rk.gana), cost_real=Rk.real_q * Rk.L, cost_sim=Rk.BASE_f_q * Rk.L)
print('EV real: pnl', round(Rk.pnl_real.sum(), 2), 'coste', round(Rk.cost_real.sum(), 2), 'EV/E', round(Rk.pnl_real.sum() / Rk.cost_real.sum(), 3), 'n fills', int((Rk.real_q > 0).sum()))
print('EV sim BASE: pnl', round(Rk.pnl_sim.sum(), 2), 'coste', round(Rk.cost_sim.sum(), 2), 'EV/E', round(Rk.pnl_sim.sum() / Rk.cost_sim.sum(), 3), 'n fills', int((Rk.BASE_f_q > 0).sum()))
m = Rk[(Rk.BASE_f_q > 1e-9) & (Rk.real_q > 0)]; print('comunes (ambos rellenan) n', len(m), 'pnl_real', round(m.pnl_real.sum(), 2), 'pnl_sim', round(m.pnl_sim.sum(), 2))
fnm = Rk[(Rk.BASE_f_q <= 1e-9) & (Rk.real_q > 0)]; fpm = Rk[(Rk.BASE_f_q > 1e-9) & (Rk.real_q == 0)]
print('solo real (FN) n', len(fnm), 'EV/E', round(fnm.pnl_real.sum() / fnm.cost_real.sum(), 3), 'pnl', round(fnm.pnl_real.sum(), 2), '| solo sim (FP) n', len(fpm), 'EV/E', round(fpm.pnl_sim.sum() / fpm.cost_sim.sum(), 3), 'pnl', round(fpm.pnl_sim.sum(), 2))
print('FN: eventos en vida: print comp', int((fnm.t_comp > 0).sum()), 'self', int((fnm.t_self > 0).sum()), 'cualquiera', int((fnm.t_prn_any > 0).sum()), 'de', len(fnm))
print('L de FN', fnm.L.round(2).value_counts().sort_index().to_dict(), 'FN vida med', fnm.vida.median(), 'FP vida med', fpm.vida.median())
# por L bucket
Rk['Lb'] = (Rk.L * 100 // 5 * 5 / 100)
print(Rk.groupby('Lb').apply(lambda g: pd.Series(dict(n=len(g), real=int(g.real_fill.sum()), sim=int((g.BASE_f_q > 1e-9).sum()), tp=int(((g.BASE_f_q > 1e-9) & (g.real_fill == 1)).sum())))).to_string())
