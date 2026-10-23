#!/usr/bin/env python3
"""an_wallets.py -- Parte B: seleccion por CONDUCTA en 17-19 (sin PnL), medida 20-22; casos; diseccion de la mejor pareadora."""
import os, sys, numpy as np, pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
W = pd.read_csv(os.path.join(D, 'wm_ledger.csv.gz')); rng = np.random.default_rng(20261022)
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
def ic_dias(x):
    g = x.groupby('dia'); num = g.pnl.sum().values; den = g.vol.sum().values; k = len(num)
    if k < 2: return (np.nan, np.nan)
    ix = rng.integers(0, k, (2000, k)); v = num[ix].sum(1) / den[ix].sum(1); return tuple(np.round(np.percentile(v, [5, 95]), 4))
def resumen(x, nom):
    v = x.vol.sum()
    if v == 0: P(nom, 'vacio'); return
    byd = (x.groupby('dia').pnl.sum() / x.groupby('dia').vol.sum()).round(4).to_dict()
    P(f"{nom}: wallets {x.wallet.nunique()} merc {len(x)} vol {v:,.0f} $ | PnL/vol {x.pnl.sum()/v:+.4f} IC90dias {ic_dias(x)} | par {x.pnl_par.sum()/v:+.4f} residuo {x.pnl_res.sum()/v:+.4f} comision {-x.fee.sum()/v:+.4f} | ambos {x.ambos.mean():.2f} maker {(x.maker_pct*x.vol).sum()/v:.2f} | por dia {byd}")
DESC = W[W.dia <= '2026-10-19']; TEST = W[W.dia >= '2026-10-20']
s = DESC.groupby('wallet').agg(n=('mid', 'size'), ambos=('ambos', 'mean'), vol=('vol', 'sum'))
par = s[(s.n >= 30) & (s.ambos >= 0.60)].index; dirc = s[(s.n >= 30) & (s.ambos < 0.20)].index; mid_ = s[(s.n >= 30) & (s.ambos >= 0.20) & (s.ambos < 0.60)].index
P('== SELECCION POR CONDUCTA en 17-19 (sin mirar PnL): pareadoras', len(par), '| direccionales', len(dirc), '| mixtas', len(mid_))
for nom, grp in (('PAREADORAS', par), ('DIRECCIONALES (placebo)', dirc), ('MIXTAS', mid_)):
    resumen(DESC[DESC.wallet.isin(grp)], f'{nom} DESC 17-19'); resumen(TEST[TEST.wallet.isin(grp)], f'{nom} TEST 20-22')
resumen(TEST, 'TODAS las wallets TEST 20-22')
# por wallet en TEST, pareadoras
t = TEST[TEST.wallet.isin(par)].groupby('wallet').agg(n=('mid', 'size'), vol=('vol', 'sum'), pnl=('pnl', 'sum'), par=('pnl_par', 'sum'), res=('pnl_res', 'sum'), fee=('fee', 'sum'), ambos=('ambos', 'mean'))
t['ev'] = t.pnl / t.vol
P('\n== PAREADORAS por wallet en TEST (ordenadas por vol):'); P(t.sort_values('vol', ascending=False).round(3).head(25).to_string())
P('pareadoras con PnL TEST > 0:', int((t.pnl > 0).sum()), 'de', len(t))
# persistencia dentro de pareadoras: mitad mejor DESC por pnl/vol
sd = DESC[DESC.wallet.isin(par)].groupby('wallet').apply(lambda z: z.pnl.sum() / z.vol.sum(), include_groups=False)
best = sd[sd >= sd.median()].index; worst = sd[sd < sd.median()].index
resumen(TEST[TEST.wallet.isin(best)], 'PAREADORAS mitad MEJOR en DESC -> TEST'); resumen(TEST[TEST.wallet.isin(worst)], 'PAREADORAS mitad PEOR en DESC -> TEST')
# casos
casos = {'0x41e2e1cc': '0x41e2e1ccf1e4940029af02259a31c6b89b9fa354', 'mo-money 0x32ed2e54': '0x32ed2e546b187ca15e2841edc82b22c713cf8ec3'}
P('\n== CASOS')
for nom, w in casos.items():
    x = W[W.wallet == w]
    if not len(x): P(nom, 'sin actividad en alts 5m 17-22'); continue
    for dd, z in [('17-19', x[x.dia <= '2026-10-19']), ('20-22', x[x.dia >= '2026-10-20'])]: resumen(z, f'{nom} {dd}')
    P(f"  {nom}: monedas {x.act.value_counts().to_dict()} | merc/dia {len(x)/x.dia.nunique():.0f} | rellenos/merc mediana {(x.nfill_YES+x.nfill_NO).median():.0f} | acc/merc mediana {(x.Q_YES+x.Q_NO).median():.0f} | coste par mediana {x.par_coste.median():.3f} (p25 {x.par_coste.quantile(.25):.3f} p75 {x.par_coste.quantile(.75):.3f}) % par>1 {(x.par_coste>1).mean():.2f} | residuo frac mediana {x.res_frac.median():.2f}")
    # residuo: gana el lado sobrante?
    x = x.assign(lado_res=np.where(x.Q_YES > x.Q_NO, 'YES', 'NO'))
    xr = x[x.res_frac > 0.05]
    P(f"  residuo: lado sobrante gana {(xr.lado_res == xr.des).mean():.3f} (n={len(xr)}); precio medio pagado del lado sobrante {np.average(np.where(xr.lado_res=='YES', xr.C_YES/xr.Q_YES.where(xr.Q_YES>0,1), xr.C_NO/xr.Q_NO.where(xr.Q_NO>0,1)), weights=np.abs(xr.Q_YES-xr.Q_NO)):.3f}")
txt = '\n'.join(out); print(txt); open(os.path.join(D, 'an_wallets.txt'), 'w').write(txt + '\n')
