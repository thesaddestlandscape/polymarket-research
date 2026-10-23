#!/usr/bin/env python3
"""an2.py -- PREREG W1 parte 2 (wallets) + extra POST-HOC de rpre en poblacion. Salida ../datos/an2.txt"""
import os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG.md'), 'rb').read()).hexdigest().startswith('303c2090')
rng = np.random.default_rng(20261024); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
IND = ['r300', 'r60', 'r900', 'rop', 'rpre', 'b15', 'd15', 'f60']
W = pd.read_csv(os.path.join(DAT, 'feats_wal.csv.gz')); W = W[W.act == 'ETH'].copy()
W['gana'] = (W.lado_ef == W.des).astype(float); W['coste'] = W.acc * W.px_ef; W['pnl'] = W.acc * (W.gana - W.px_ef); W['pxb'] = (W.px_ef / 0.1).astype(int)
W['T'] = W.fin - W.ts; W['Tb'] = (W['T'] // 60).clip(0, 4)
P(f'Fills maker ETH 5m con px_ef 0,1-0,9, 17-22 Oct: {len(W)}; wallets distintas {W.wallet.nunique()}')
def sg(x): return np.where(np.isnan(x) | (x == 0), np.nan, (x > 0).astype(float))
for c in IND: W['s_' + c] = sg(W[c].values)
def ci(vals, cl, nb=1000):
    d = pd.DataFrame({'v': vals, 'c': cl}).dropna(); g = d.groupby('c').v.agg(['sum', 'count']); s, n = g['sum'].values, g['count'].values; m = len(g); r = []
    for _ in range(nb):
        i = rng.integers(0, m, m); r.append(s[i].sum() / n[i].sum())
    return np.percentile(r, [5, 95])
def evc(d): return d.pnl.sum() / d.coste.sum() if len(d) and d.coste.sum() > 0 else np.nan
for w in ['0xf074dc84', '0x0ab01745']:
    m = W.wallet.str.startswith(w); Wd = W[m]; Od = W[~m]
    P(f'\n===== {w} (n fills {len(Wd)}, mercados {Wd.mid.nunique()}, acc medio {Wd.acc.mean():.2f}, px_ef medio {Wd.px_ef.mean():.3f}, T mediana {Wd["T"].median():.0f}; otros makers ETH n {len(Od)})')
    rows = []
    for c in IND:
        s = 's_' + c
        # esperado: cuota CON de los OTROS en el mismo (mercado, cubo px 0,1)
        g = Od.groupby(['mid', 'pxb'])[s].agg(['sum', 'count']); key = pd.MultiIndex.from_frame(Wd[['mid', 'pxb']])
        gs = g['sum'].reindex(key).values; gc = g['count'].reindex(key).values
        exp = np.where(gc > 0, gs / np.where(gc > 0, gc, 1), np.nan); dif = Wd[s].values - exp
        ok = ~np.isnan(dif); icd = ci(dif[ok], Wd.fin.values[ok]) if ok.sum() > 50 else (np.nan, np.nan)
        # cuota CON del propio wallet vs esperada
        cw = np.nanmean(Wd[s]); ce = np.nanmean(exp[ok])
        # EV por clase
        a = Wd[Wd[s] == 1]; b = Wd[Wd[s] == 0]
        ao = Od[Od[s] == 1]; bo = Od[Od[s] == 0]
        rows.append(dict(ind=c, n=int(ok.sum()), cuotaCON_w=cw, esperada=ce, dif=np.nanmean(dif), ic_lo=icd[0], ic_hi=icd[1],
                         acc_CON=a.acc.mean(), acc_CONTRA=b.acc.mean(), nCON=len(a), nCONTRA=len(b), evCON_w=evc(a), evCONTRA_w=evc(b), evCON_otros=evc(ao), evCONTRA_otros=evc(bo)))
    P(pd.DataFrame(rows).round(3).to_string(index=False))
    # fills por (mercado,lado) segun clase de r300 / rpre al primer fill? descriptivo: nº de fills por mercado-lado y cuota CON por Tb
    P('cuota CON (r300) por tramo de T restante (min): ' + ' '.join(f'{int(t)}: {np.nanmean(Wd[Wd.Tb == t].s_r300):.3f}/{np.nanmean(Od[Od.Tb == t].s_r300):.3f}' for t in sorted(Wd.Tb.unique())) + '  [wallet/otros]')
    # tamano de la tendencia: |r300| terciles -> cuota CON
    Wd2 = Wd.dropna(subset=['r300']); Wd2 = Wd2.assign(ar=Wd2.r300.abs() * np.sign(Wd2.r300)); q = np.nanpercentile(Wd2.r300.abs(), [50, 80])
    P(f'cuota CON(r300) segun |r300| (<=p50 {q[0]:.1f} bps, p50-p80, >p80 {q[1]:.1f}): ' + ' '.join(f'{lab} {np.nanmean(Wd2[sel].s_r300):.3f}(n{int(sel.sum())})' for lab, sel in (('peq', Wd2.r300.abs() <= q[0]), ('med', (Wd2.r300.abs() > q[0]) & (Wd2.r300.abs() <= q[1])), ('grande', Wd2.r300.abs() > q[1]))))
    P(f'EV del wallet {evc(Wd):+.4f} (n {len(Wd)}, coste {Wd.coste.sum():.0f}), otros makers ETH {evc(Od):+.4f}')
# Poblacion rpre: POST-HOC por moneda y magnitud
U = pd.read_csv(os.path.join(DAT, 'feats_pop.csv.gz')); U = U[U.gana.notna()]
def delta(D, c):
    a = D[D[c] > 0]; b = D[D[c] < 0]; return evc(a) - evc(b), len(a), len(b)
P('\n== POST-HOC (NO preregistrado) poblacion: Delta CON-CONTRA de rpre y r900 por moneda y periodo')
for c in ['rpre', 'r900']:
    for per, sel in (('DESC', U.dia <= '2026-10-19'), ('TEST', U.dia >= '2026-10-20')):
        P(f'  {c} {per}: ' + ' | '.join(f'{a} {delta(U[sel & (U.act == a)], c)[0]:+.3f} (n {delta(U[sel & (U.act == a)], c)[1]}/{delta(U[sel & (U.act == a)], c)[2]})' for a in ['ETH', 'SOL', 'XRP']))
P('  rpre por magnitud |rpre| (bps) CON y CONTRA, todo 17-22: ')
U2 = U.dropna(subset=['rpre']); U2 = U2[U2.rpre != 0]; U2['mag'] = pd.qcut(U2.rpre.abs(), 3, labels=['bajo', 'medio', 'alto'])
for mg, D in U2.groupby('mag', observed=True):
    a = D[D.rpre > 0]; b = D[D.rpre < 0]; P(f'    {mg} (|rpre| {D.rpre.abs().min():.1f}-{D.rpre.abs().max():.1f}): CON EV {evc(a):+.3f} (n {len(a)}), CONTRA EV {evc(b):+.3f} (n {len(b)})')
P('  PnL por dia (EUR) si se quita la clase CON de rpre / CON de r900 (frente a mantener):')
for c in ['rpre', 'r900']:
    P('   ' + c + ': ' + ' '.join(f'{d[5:]}: {-U[(U.dia == d) & (U[c] > 0)].pnl.sum():+.0f} (base {U[U.dia == d].pnl.sum():+.0f})' for d in sorted(U.dia.unique())))
open(os.path.join(DAT, 'an2.txt'), 'w').write('\n'.join(out) + '\n')
