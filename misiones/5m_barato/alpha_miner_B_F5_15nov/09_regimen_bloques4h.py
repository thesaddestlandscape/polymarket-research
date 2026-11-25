#!/usr/bin/env python3
"""Paso 9 (DESCRIPTIVO, FASE 1; NO es test de ninguna regla): persistencia del EV de poblacion a escala de BLOQUE DE 4 h UTC (cierre del mercado),
ETH/SOL/XRP, banda, T_rem>60 s; todas vs tipo B; 09-Oct..14-Nov. Se resta la media del tramo horario (hora-del-dia) para no confundir
estacionalidad intradia con persistencia de regimen. lag-1 Spearman entre bloques consecutivos (permutacion global, 10000), y correlacion del bloque t
con la media de los 2 bloques previos. Dias ya vistos: diagnostico de viabilidad, no confirma nada."""
import os, sys, glob, numpy as np, pandas as pd
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__))
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; FW = DL + 'forward/'
acc = []
def red(F):
    F = F[F.coin.isin(('ETH', 'SOL', 'XRP'))]
    T = F.fin.values - F.r.values / 1000.0; m = T > 60
    tb = ((F.bid.values - F.q.values) >= 0.0099) & np.isfinite(F.bid.values)
    blk = (F.fin.values // (4 * 3600)).astype(np.int64)
    for nm, mm in (('todas', m), ('tipoB', m & tb)):
        g = pd.DataFrame({'blk': blk[mm], 'p': F.pnl.values[mm], 'c': F.coste.values[mm]}).groupby('blk').sum()
        g['nm'] = nm; acc.append(g.reset_index())
for d in pd.date_range('2026-10-09', '2026-10-23').strftime('%F'): red(pd.read_pickle(DL + f'r_{d}.pkl'))
for p in sorted(glob.glob(FW + 'prints_2026-*.pkl')):
    d = os.path.basename(p)[7:17]
    if '2026-10-24' <= d <= '2026-11-14': red(pd.read_pickle(p))
A = pd.concat(acc, ignore_index=True).groupby(['nm', 'blk'], as_index=False).sum()
rng = np.random.default_rng(20261115); out = ['# Persistencia a bloques de 4 h UTC (cierre del mercado); EV pond. por bloque, menos media del tramo horario. DESCRIPTIVO (dias vistos)']
for nm in ('todas', 'tipoB'):
    X = A[A.nm == nm].sort_values('blk').copy(); X = X[(X.blk >= X.blk.min()) & (X.blk <= X.blk.max())]
    # solo bloques con coste suficiente (>= 300 EUR) y consecutivos
    full = pd.DataFrame({'blk': np.arange(X.blk.min(), X.blk.max() + 1)}).merge(X, how='left', on='blk')
    full['slot'] = (full.blk % 6).astype(int); full['ev'] = full.p / full.c
    ok = full.c >= 300; full.loc[~ok, 'ev'] = np.nan
    full['res'] = full.ev - full.groupby('slot').ev.transform('mean')
    x = full.res.values; a, b = x[:-1], x[1:]; m = np.isfinite(a) & np.isfinite(b)
    r_obs = stats.spearmanr(a[m], b[m])[0]; pe = np.corrcoef(a[m], b[m])[0, 1]
    v = x[np.isfinite(x)]; perm = np.empty(10000)
    for i in range(10000):
        y = x.copy(); y[np.isfinite(y)] = rng.permutation(v); aa, bb = y[:-1], y[1:]; mm = np.isfinite(aa) & np.isfinite(bb); perm[i] = stats.spearmanr(aa[mm], bb[mm])[0]
    p = (1 + np.sum(perm >= r_obs)) / (1 + len(perm))
    # media de 2 bloques previos -> bloque actual
    prev = pd.Series(x).shift(1).rolling(2, min_periods=2).mean().values; mk = np.isfinite(prev) & np.isfinite(x)
    out.append(f'[{nm}] bloques {len(full)} (validos {int(ok.sum())}, coste>=300 EUR) | lag-1 Spearman {r_obs:+.3f} (Pearson {pe:+.3f}) p_perm unilateral {p:.4f} (pares {int(m.sum())}) | corr(bloque t, media 2 previos) = {np.corrcoef(prev[mk], x[mk])[0, 1]:+.3f} (n={int(mk.sum())}) | sd EV bloque {np.nanstd(full.ev.values):.3f}')
open(HERE + '/regimen_bloques4h.txt', 'w').write('\n'.join(out)); print('\n'.join(out))
