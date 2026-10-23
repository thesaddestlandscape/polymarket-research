import gc
#!/usr/bin/env python3
"""s4_analisis.py -- PREREG_W2 (sha 7b3c5e4c…). P1 cuota CON, P2 lado contrario/mercado, P4 descomposicion. Salida w2_btc/an_w2.txt
Entradas w2_btc/feats_btc_M.csv.gz (s3) y w2_btc/fills_btc_all.csv.gz (s2). nice/ionice, ulimit -v 3000000, >=09:00Z."""
import os, sys, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); OUT = '/root/polymarket-research-datalogs/w2_btc'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG_W2.md'), 'rb').read()).hexdigest().startswith('7b3c5e4c')
rng = np.random.default_rng(20261023); NPERM = int(os.environ.get('NPERM', 1000)); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
W21 = '0x21f4c1a1'; CTRL = ['0xaa1a4f31', '0x41e2e1cc']
IND = ['r300', 'r60', 'r900', 'rop', 'rpre', 'b15', 'f60']
def ci_ratio(num, den, cl, nb=1000):
    d = pd.DataFrame({'n': num, 'd': den, 'c': cl}).dropna(); g = d.groupby('c')[['n', 'd']].sum(); a, b = g.n.values, g.d.values; m = len(g)
    if m < 5: return (np.nan, np.nan)
    r = np.empty(nb)
    for i in range(nb):
        j = rng.integers(0, m, m); r[i] = a[j].sum() / max(b[j].sum(), 1e-12)
    return tuple(np.percentile(r, [5, 95]))
A = pd.read_csv(os.path.join(OUT, 'fills_btc_all.csv.gz'), dtype={'wallet': str}, usecols=['dia', 'wallet', 'mid', 'rol', 'side', 'lado_ef', 'acc', 'cost_ef', 'fee_usd', 'des', 'fin', 'px_ef', 'T']); A = A[A.des.notna()]; _nm = A.groupby('wallet').mid.nunique(); A = A[A.wallet.map(_nm) >= 30].copy(); P(f'ledger: wallets con >=30 mercados BTC 5m en 17-21: {_nm.ge(30).sum()} de {len(_nm)}; filas {len(A)}')
def ledger(A):
    g = A.groupby(['wallet', 'mid', 'lado_ef']).agg(Q=('acc', 'sum'), C=('cost_ef', 'sum'), fee=('fee_usd', 'sum')).reset_index()
    mkusd = A[A.rol == 'M'].groupby(['wallet', 'mid', 'lado_ef']).cost_ef.sum().rename('mku').reset_index(); g = g.merge(mkusd, on=['wallet', 'mid', 'lado_ef'], how='left').fillna({'mku': 0})
    meta = A.drop_duplicates('mid').set_index('mid')[['fin', 'des', 'dia']]
    W = g.pivot_table(index=['wallet', 'mid'], columns='lado_ef', values=['Q', 'C', 'fee', 'mku'], fill_value=0); W.columns = [f'{a}_{b}' for a, b in W.columns]
    for c in ('Q', 'C', 'fee', 'mku'):
        for l in ('YES', 'NO'):
            if f'{c}_{l}' not in W: W[f'{c}_{l}'] = 0.0
    W = W.reset_index().join(meta, on='mid')
    W['vol'] = W.C_YES + W.C_NO; W['fee'] = W.fee_YES + W.fee_NO; W['pago'] = np.where(W.des == 'YES', W.Q_YES, W.Q_NO); W['pnl'] = W.pago - W.vol - W.fee
    W['Qp'] = np.minimum(W.Q_YES, W.Q_NO); py = np.where(W.Q_YES > 0, W.C_YES / W.Q_YES.where(W.Q_YES > 0, 1), 0); pn = np.where(W.Q_NO > 0, W.C_NO / W.Q_NO.where(W.Q_NO > 0, 1), 0)
    W['pc'] = np.where(W.Qp > 0, py + pn, np.nan); W['par'] = W.Qp * (1 - np.nan_to_num(W.pc)); W['res'] = W.pnl + W.fee - W.par
    W['rf'] = (W.Q_YES - W.Q_NO).abs() / (W.Q_YES + W.Q_NO); W['heavy'] = np.where(W.Q_YES >= W.Q_NO, 'YES', 'NO')
    W['Qres'] = (W.Q_YES - W.Q_NO).abs(); W['pheavy'] = np.where(W.heavy == 'YES', py, pn); W['cres'] = W.Qres * W.pheavy; W['win_res'] = (W.heavy == W.des).astype(float)
    W['ambos'] = (W.Q_YES >= 5) & (W.Q_NO >= 5); W['mkp'] = (W.mku_YES + W.mku_NO) / W.vol; W['per'] = np.where(W.dia <= '2026-10-19', 'DESC', 'TEST'); return W
L = ledger(A); Lw = L[L.wallet.str.startswith(W21)]
P(f'\n===== P4 ledger: wallet-mercado {len(L)}; 0x21f4 {len(Lw)} mercados, vol {Lw.vol.sum():,.0f}, PnL/vol {Lw.pnl.sum()/Lw.vol.sum():+.4f}, par {Lw.par.sum()/Lw.vol.sum():+.4f}, residuo {Lw.res.sum()/Lw.vol.sum():+.4f}, comision {-Lw.fee.sum()/Lw.vol.sum():+.4f}, maker {Lw.mku_YES.sum()+Lw.mku_NO.sum():.0f}/{Lw.vol.sum():.0f}')
for per in ('DESC', 'TEST'):
    x = Lw[Lw.per == per]; lo, hi = ci_ratio(x.pnl.values, x.vol.values, x.fin.values); P(f'  {per}: n {len(x)} PnL/vol {x.pnl.sum()/x.vol.sum():+.4f} IC90 cierre ({lo:+.4f},{hi:+.4f}) par {x.par.sum()/x.vol.sum():+.4f} residuo {x.res.sum()/x.vol.sum():+.4f}')
P('  por dia (PnL/vol | par | residuo | n mercados): ' + ' ; '.join(f'{d[5:]}: {x.pnl.sum()/x.vol.sum():+.4f}|{x.par.sum()/x.vol.sum():+.4f}|{x.res.sum()/x.vol.sum():+.4f}|{len(x)}' for d, x in Lw.groupby('dia')))
# (a) direccion
x = Lw[Lw.Qres > 0]
lo, hi = ci_ratio(x.res.values, x.cres.values, x.fin.values)
P(f'\n(a) DIRECCION: residuo (lado pesado): EV por € de coste del residuo {x.res.sum()/x.cres.sum():+.4f} IC90 cierre ({lo:+.4f},{hi:+.4f}); acierto del lado pesado ponderado por acciones {np.average(x.win_res, weights=x.Qres):.3f} frente a precio medio pagado {x.cres.sum()/x.Qres.sum():.3f}; n mercados {len(x)}')
x['blk'] = x.fin // 14400; pr = []; Qy = x.Q_YES.values; Qn = x.Q_NO.values; desv = x.des.values.copy(); parv = x.par.values; volv = x.vol.values; feev = x.fee.values
for p in range(2000):
    dp = desv.copy()
    for _, ii in x.groupby(['dia', 'blk']).indices.items(): dp[ii] = rng.permutation(desv[ii])
    pago = np.where(dp == 'YES', Qy, Qn); pr.append((pago - volv - feev + feev - parv).sum())
pr = np.array(pr); obs = x.res.sum(); P(f'    placebo (des permutado entre mercados del mismo dia x 4 h, 2000): obs Σres {obs:+.1f} $, placebo medio {pr.mean():+.1f} (sd {pr.std():.1f}), p una cola {(pr >= obs).mean():.4f}')
P('    residuo por dia (EV/€ residuo | acierto vs precio): ' + ' ; '.join(f'{d[5:]}: {z.res.sum()/z.cres.sum():+.3f}|{np.average(z.win_res, weights=z.Qres):.3f} vs {z.cres.sum()/z.Qres.sum():.3f}' for d, z in x.groupby('dia')))
# (c) inventario
P('\n(c) INVENTARIO: dosis-respuesta de res_frac -> PnL/vol del mercado (0x21f4)')
for lab, lo_, hi_ in (('<0,1', 0, .1), ('0,1-0,3', .1, .3), ('0,3-0,6', .3, .6), ('>0,6', .6, 1.01)):
    z = Lw[(Lw.rf >= lo_) & (Lw.rf < hi_)]
    if len(z) > 10: l1, h1 = ci_ratio(z.pnl.values, z.vol.values, z.fin.values); P(f'   res_frac {lab}: n {len(z)} PnL/vol {z.pnl.sum()/z.vol.sum():+.4f} IC90 ({l1:+.4f},{h1:+.4f}) par {z.par.sum()/z.vol.sum():+.4f} residuo {z.res.sum()/z.vol.sum():+.4f}')
# pareadoras poblacion (conducta en DESC), medidas en TEST
cd = L[L.per == 'DESC'].groupby('wallet').agg(nm=('mid', 'size'), amb=('ambos', 'mean')); par = cd[(cd.nm >= 30) & (cd.amb >= 0.6)].index
T = L[(L.per == 'TEST') & L.wallet.isin(par)]; Tn = L[(L.per == 'TEST') & ~L.wallet.isin(par)]
def resumen(x, nm):
    l1, h1 = ci_ratio(x.pnl.values, x.vol.values, x.fin.values); return f'{nm}: wallets {x.wallet.nunique()} merc {len(x)} vol {x.vol.sum():,.0f} PnL/vol {x.pnl.sum()/x.vol.sum():+.4f} IC90 cierre ({l1:+.4f},{h1:+.4f}) par {x.par.sum()/x.vol.sum():+.4f} residuo {x.res.sum()/x.vol.sum():+.4f} comision {-x.fee.sum()/x.vol.sum():+.4f} coste_par med {np.nanmedian(x.pc):.3f} res_frac med {x.rf.median():.2f} maker {x.mkp.mean():.2f}'
P(f'\n== pareadoras BTC (conducta en 17-19: >=30 mercados, >=60 % con ambos lados >=5 acc): {len(par)} wallets; MEDIDAS en TEST 20-21')
P('  ' + resumen(T[~T.wallet.str.startswith(W21)], 'pareadoras sin 0x21f4')); P('  ' + resumen(T[T.wallet.str.startswith(W21)], '0x21f4 (TEST)') if len(T[T.wallet.str.startswith(W21)]) else '  0x21f4 no entra en el grupo por conducta')
P('  ' + resumen(Tn, 'resto (direccionales/otros)')); P('  ' + resumen(L[(L.per == 'TEST') & L.wallet.str.startswith(W21)], '0x21f4 siempre (TEST)'))
pw = T.groupby('wallet').apply(lambda z: pd.Series({'nm': len(z), 'vol': z.vol.sum(), 'ev': z.pnl.sum() / z.vol.sum(), 'par': z.par.sum() / z.vol.sum(), 'res': z.res.sum() / z.vol.sum(), 'pc': np.nanmedian(z.pc), 'rf': z.rf.median()})).sort_values('vol', ascending=False)
P('  top pareadoras por volumen TEST:'); P(pw.head(10).round(4).to_string())
# (b) precio / cola
# forma (P3)
P('\n== P3 forma (todas las filas, 17-21): wallet / controles / pareadoras')
for nm, pref in (('0x21f4', W21), ('0xaa1a', CTRL[0]), ('0x41e2', CTRL[1])):
    z = A[A.wallet.str.startswith(pref)]; zm = z[z.rol == 'M']
    P(f'  {nm}: fills {len(z)} maker {len(zm)/len(z):.2f} ventas {(z.side==1).mean():.3f} acc/fill med {z.acc.median():.1f} px_ef med {z.px_ef.median():.3f} T p10/50/90 {np.percentile(z["T"],[10,50,90]).round(0).tolist()}')
open(os.path.join(OUT, 'an_w2b.txt'), 'w').write('\n'.join(out) + '\n')
