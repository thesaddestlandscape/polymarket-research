#!/usr/bin/env python3
"""an1.py -- PREREG W1 parte 1. Poblacion 17-22 (DESC 17-19 / TEST 20-22) y B real. Salida ../datos/an1.txt"""
import os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG.md'), 'rb').read()).hexdigest().startswith('303c2090')
rng = np.random.default_rng(20261023); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
IND = ['r300', 'r60', 'r900', 'rop', 'rpre', 'b15', 'd15', 'f60']
U = pd.read_csv(os.path.join(DAT, 'feats_pop.csv.gz')); U = U[U.gana.notna()].reset_index(drop=True)
U['pcb'] = (U.pc / 0.05).round().astype(int); U['strat'] = pd.factorize(U.dia + '|' + U.act + '|' + U.lado + '|' + U.pcb.astype(str))[0]
def ev(pnl, c): return pnl.sum() / c.sum() if c.sum() > 0 else np.nan
def contrast(df, col):
    a = df[df[col] > 0]; b = df[df[col] < 0]
    return ev(a.pnl, a.coste) - ev(b.pnl, b.coste), len(a), len(b), ev(a.pnl, a.coste), ev(b.pnl, b.coste), a.coste.sum(), b.coste.sum()
def boot(df, col, key, nb=2000):
    d = df[df[col].notna() & (df[col] != 0)]
    s = d.assign(w=(d[col] > 0)).groupby([key, 'w']).agg(p=('pnl', 'sum'), c=('coste', 'sum')).unstack('w').fillna(0)
    pa, ca, pb, cb = s[('p', True)].values, s[('c', True)].values, s[('p', False)].values, s[('c', False)].values
    n = len(s); v = []
    for _ in range(nb):
        i = rng.integers(0, n, n); A, B = ca[i].sum(), cb[i].sum()
        v.append(pa[i].sum() / A - pb[i].sum() / B if A > 0 and B > 0 else np.nan)
    return np.nanpercentile(v, [5, 95])
def perm_dist(df, cols, nperm=1000):
    """permuta (pnl,coste) dentro de estratos; devuelve matriz nperm x len(cols) de Delta"""
    d = df.sort_values('strat').reset_index(drop=True); codes = d.strat.values; pnl = d.pnl.values; cst = d.coste.values
    M = {c: (np.nan_to_num(d[c].values) > 0, np.nan_to_num(d[c].values) < 0) for c in cols}
    res = np.zeros((nperm, len(cols)))
    for k in range(nperm):
        idx = np.lexsort((rng.random(len(d)), codes)); p = pnl[idx]; c = cst[idx]
        for j, col in enumerate(cols):
            a, b = M[col]; res[k, j] = p[a].sum() / c[a].sum() - p[b].sum() / c[b].sum()
    return res, d
P(f'Poblacion: {len(U)} unidades con desenlace, coste {U.coste.sum():.0f} EUR, EV {ev(U.pnl, U.coste):+.4f}. Cobertura (no missing y !=0) por indicador:')
P(' '.join(f'{c}={((U[c].notna()) & (U[c] != 0)).mean():.3f}' for c in IND))
P('\nCorrelacion de contexto: P(gana) y EV por clase, TODA la poblacion (para ver si el indicador esta ya en el precio)')
rows = []
for per, sel in (('DESC 17-19', U.dia <= '2026-10-19'), ('TEST 20-22', U.dia >= '2026-10-20'), ('TODO 17-22', U.dia > '')):
    D = U[sel]
    for c in IND:
        dl, na, nb_, ea, eb, ca, cb = contrast(D, c)
        icc = boot(D, c, 'fin'); icd = boot(D, c, 'dia', 1000)
        rows.append(dict(per=per, ind=c, nCON=na, nCONTRA=nb_, evCON=ea, evCONTRA=eb, delta=dl, ic_cierre_lo=icc[0], ic_cierre_hi=icc[1], ic_dia_lo=icd[0], ic_dia_hi=icd[1],
                         hitCON=D[D[c] > 0].gana.mean(), hitCONTRA=D[D[c] < 0].gana.mean(), pcCON=D[D[c] > 0].pc.mean(), pcCONTRA=D[D[c] < 0].pc.mean(), costCON=ca, costCONTRA=cb))
R = pd.DataFrame(rows); pd.set_option('display.width', 250); pd.set_option('display.max_columns', 30)
for per in R.per.unique():
    P(f'\n== {per} =='); P(R[R.per == per].drop(columns='per').round(4).to_string(index=False))
# dias
P('\nDelta por dia (CON-CONTRA):'); dd = {}
for c in IND:
    dd[c] = [contrast(U[U.dia == d], c)[0] for d in sorted(U.dia.unique())]
P(pd.DataFrame(dd, index=sorted(U.dia.unique())).round(3).T.to_string())
# direcciones de DESC
dirs = {c: np.sign(R[(R.per == 'DESC 17-19') & (R.ind == c)].delta.iloc[0]) for c in IND}
# placebo en TEST, max-estadistico
T = U[U.dia >= '2026-10-20']; res, Td = perm_dist(T, IND, 1000)
obs = np.array([contrast(Td, c)[0] for c in IND]); dr = np.array([dirs[c] for c in IND])
mx_obs = (obs * dr).max(); mx_perm = (res * dr).max(1)
P('\nPLACEBO estratos (dia,act,lado,pc 0,05) en TEST (1000 perms): una cola en el sentido de DESC; p max-estadistico entre 8 indicadores')
for j, c in enumerate(IND):
    pone = ((res[:, j] * dr[j]) >= obs[j] * dr[j]).mean(); P(f'  {c}: Delta TEST {obs[j]:+.4f} dir DESC {int(dr[j]):+d} media placebo {res[:, j].mean():+.4f} p una cola {pone:.3f}')
P(f'  max-estadistico: obs {mx_obs:+.4f}; p = {(mx_perm >= mx_obs).mean():.3f}')
# ALL period placebo too
res2, Ad = perm_dist(U, IND, 1000); obs2 = np.array([contrast(Ad, c)[0] for c in IND])
P('PLACEBO en TODO 17-22 (dos colas): ' + ' '.join(f'{c}: {obs2[j]:+.4f} p={(np.abs(res2[:, j] - res2[:, j].mean()) >= abs(obs2[j] - res2[:, j].mean())).mean():.3f}' for j, c in enumerate(IND)))
# regla skip en TEST
P('\nREGLA SKIP en TEST: quitar la clase de peor EV en DESC (por indicador); PnL total, coste quitado y placebo (quitar misma fraccion de coste al azar en estratos)')
base = T.pnl.sum(); P(f'  base TEST: n {len(T)} coste {T.coste.sum():.0f} PnL {base:+.1f} EUR EV {ev(T.pnl, T.coste):+.4f}')
Dd = U[U.dia <= '2026-10-19']
for c in IND:
    clases = {'CON': lambda D: D[c] > 0, 'CONTRA': lambda D: D[c] < 0}
    evd = {k: ev(Dd[f(Dd)].pnl, Dd[f(Dd)].coste) for k, f in clases.items()}; worst = min(evd, key=evd.get)
    rm = clases[worst](T); kept = T[~rm]; frac = T[rm].coste.sum() / T.coste.sum()
    # placebo: dentro de estrato, quitar al azar la misma fraccion de unidades (aprox por prob = frac por estrato = share de rm en el estrato)
    sh = T.assign(rm=rm).groupby('strat').rm.transform('mean').values; pl = []
    for _ in range(1000):
        r = rng.random(len(T)) < sh; pl.append(T.pnl[~r].sum() - base)
    gain = kept.pnl.sum() - base
    P(f'  {c}: quita {worst} (EV DESC {evd[worst]:+.3f} vs {evd["CON" if worst == "CONTRA" else "CONTRA"]:+.3f}); n quitadas {int(rm.sum())} ({frac*100:.0f} % del coste); EV TEST retenido {ev(kept.pnl, kept.coste):+.4f}; dPnL {gain:+.1f} EUR (placebo media {np.mean(pl):+.1f}, p {(np.array(pl) >= gain).mean():.3f})')
# B real
Bf = pd.read_csv(os.path.join(DAT, 'feats_b.csv.gz')); Bf = Bf[Bf.gana.notna()].copy(); Bf['fin'] = Bf.fin_s
P(f'\n== B real: {len(Bf)} posiciones, coste {Bf.coste.sum():.1f} PnL {Bf.pnl.sum():+.2f} EV {ev(Bf.pnl, Bf.coste):+.3f}; t0 con flag (sin t_det): {int(Bf.t0_flag.sum())}')
rows = []
for c in IND:
    dl, na, nb_, ea, eb, ca, cb = contrast(Bf, c); icc = boot(Bf, c, 'fin', 2000) if min(na, nb_) > 3 else (np.nan, np.nan)
    rows.append(dict(ind=c, nCON=na, nCONTRA=nb_, evCON=ea, evCONTRA=eb, delta=dl, ic_cierre_lo=icc[0], ic_cierre_hi=icc[1], hitCON=Bf[Bf[c] > 0].gana.mean(), hitCONTRA=Bf[Bf[c] < 0].gana.mean(), pnlCON=Bf[Bf[c] > 0].pnl.sum(), pnlCONTRA=Bf[Bf[c] < 0].pnl.sum()))
P(pd.DataFrame(rows).round(3).to_string(index=False))
open(os.path.join(DAT, 'an1.txt'), 'w').write('\n'.join(out) + '\n')
