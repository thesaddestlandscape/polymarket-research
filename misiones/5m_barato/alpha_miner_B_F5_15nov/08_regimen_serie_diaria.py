#!/usr/bin/env python3
"""Paso 8 (DESCRIPTIVO, FASE 1; NO es test de ninguna regla): serie diaria del EV de poblacion (ETH/SOL/XRP, banda, T_rem>60 s)
09-Oct..14-Nov (37 dias): todas las filas vs tipo B. Autocorrelacion lag-1 (Pearson/Spearman, p por permutacion de dias), n efectivo por dias,
persistencia de signo y correlacion con la media de los k dias previos; gradiente F5 bajo-alto por periodo (de poblacion_por_tercil.json).
Mismos dias de los que salio la historia de regimenes: solo diagnostico de viabilidad de un detector causal, NO confirma nada."""
import os, sys, glob, json, numpy as np, pandas as pd
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; FW = DL + 'forward/'
rows = []
def red(d, F):
    F = F[F.coin.isin(('ETH', 'SOL', 'XRP'))]
    T = F.fin.values - F.r.values / 1000.0; m = T > 60
    tb = ((F.bid.values - F.q.values) >= 0.0099) & np.isfinite(F.bid.values)
    p = F.pnl.values; c = F.coste.values
    rows.append(dict(dia=d, pA=p[m].sum(), cA=c[m].sum(), pB=p[m & tb].sum(), cB=c[m & tb].sum(), nA=int(m.sum()), nB=int((m & tb).sum())))
for d in pd.date_range('2026-10-09', '2026-10-23').strftime('%F'): red(d, pd.read_pickle(DL + f'r_{d}.pkl'))
for p in sorted(glob.glob(FW + 'prints_2026-*.pkl')):
    d = os.path.basename(p)[7:17]
    if '2026-10-24' <= d <= '2026-11-14': red(d, pd.read_pickle(p))
D = pd.DataFrame(rows).sort_values('dia').reset_index(drop=True)
D['evA'] = D.pA / D.cA; D['evB'] = D.pB / D.cB
out = ['# Serie diaria EV poblacion (ETH/SOL/XRP, banda, T_rem>60 s), EV pond. por EUR de cada dia. DESCRIPTIVO (dias ya vistos); n dias = %d' % len(D),
       'dia        evTodas  evTipoB  costeTipoB(EUR)  nTipoB']
for r in D.itertuples(): out.append(f'{r.dia}  {r.evA:+.3f}   {r.evB:+.3f}   {r.cB:8.1f}   {r.nB:5d}')
rng = np.random.default_rng(20261115)
def acf(x, nperm=10000):
    x = np.asarray(x, float); r1 = np.corrcoef(x[:-1], x[1:])[0, 1]; sp = stats.spearmanr(x[:-1], x[1:])[0]
    perm = np.array([np.corrcoef(*(lambda y: (y[:-1], y[1:]))(rng.permutation(x)))[0, 1] for _ in range(nperm)])
    p = (1 + np.sum(perm >= r1)) / (1 + nperm); neff = len(x) * (1 - r1) / (1 + r1) if r1 > 0 else float(len(x))
    s = x > 0; pp = int(np.sum(s[:-1] & s[1:])); pn = int(np.sum(s[:-1] & ~s[1:])); np_ = int(np.sum(~s[:-1] & s[1:])); nn = int(np.sum(~s[:-1] & ~s[1:]))
    return r1, sp, p, neff, (pp, pn, np_, nn)
for nm, col in (('todas', 'evA'), ('tipo B', 'evB')):
    x = D[col].values; r1, sp, p, neff, tr = acf(x)
    out.append(f'[{nm}] media diaria {x.mean():+.3f} sd {x.std(ddof=1):.3f} | lag-1 Pearson {r1:+.3f} Spearman {sp:+.3f} p_perm(unilateral) {p:.4f} | n_eff por dias {neff:.1f} de {len(x)} | transiciones signo (++ +- -+ --) {tr}')
    for k in (3, 5, 7):
        a = np.array([x[i - k:i].mean() for i in range(k, len(x))]); b = x[k:]
        out.append(f'   corr(dia t, media k={k} dias previos) = {np.corrcoef(a, b)[0, 1]:+.3f} (n={len(b)}; descriptivo)')
    # sin los dias de B real 20-23 Oct (para no depender del bloque negativo)
    m = ~D.dia.between('2026-10-20', '2026-10-23').values; xs = D[col].values[m]
    out.append(f'   sin 20-23 Oct (nota: serie con salto, lag-1 sobre contiguos): media {xs.mean():+.3f}, dias+ {(xs>0).sum()}/{len(xs)}')
# gradiente F5 bajo-alto por periodo (P_DER vs P_OOS), de poblacion_por_tercil.json (todos los T, no solo T>60)
J = json.load(open(HERE + '/poblacion_por_tercil.json'))
out.append('# Gradiente F5 poblacion por periodo (bajo_alto_dia del JSON; todos los T_rem):')
for k, v in J.items(): out.append(f'  {k}: bajo_alto_dia={json.dumps(v["bajo_alto_dia"])[:140]} | todo={v["todo"]:+.3f} G1={json.dumps(v["G1"])[:80]}')
open(HERE + '/regimen_serie_diaria.txt', 'w').write('\n'.join(out)); print('\n'.join(out))
