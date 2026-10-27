#!/usr/bin/env python3
"""e1d_eval.py -- PREREG_E1D. H1 (BN_W300_X2 en poblacion, dias != 20-22 Oct) y H2 (cuando operar, walk-forward por dia). Salida datos/e1d_resultados.txt"""
import os, sys, hashlib, warnings, numpy as np, pandas as pd
warnings.filterwarnings('ignore')
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); BASE = os.path.join(AQ, '..', '..')
H = open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1D.sha256')).read().split()[0]
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1D.md'), 'rb').read()).hexdigest() == H
OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'; rng = np.random.default_rng(11); out = []
def P(*a): out.append(' '.join(map(str, a))); print(*a, flush=True)
F = pd.read_csv(OUT + 'e1d_rellenos.csv.gz', dtype={'mid': str}); W = pd.read_csv(OUT + 'e1d_ventanas.csv.gz', dtype={'mid': str})
ev = lambda d: d.pnl.sum() / d.coste.sum() if d.coste.sum() > 0 else np.nan
P('POBLACION rellenos bid 0,10-0,30 5m ETH/SOL/XRP con desenlace oficial:', len(F), '| por dia n / pnl / EV€ / Σcoste:')
for d, g in F.groupby('dia'): P(f'  {d}: {len(g)} / {g.pnl.sum():+.0f} / {ev(g):+.3f} / {g.coste.sum():.0f} | flag {g.flag.mean():.3f} | bn_age p90 {g.bn_age.quantile(.9):.0f} ms')
# ---------------- H1
P('\n=== H1 BN_W300_X2 en la poblacion (dias != 20-22 Oct) ===')
A = F[~F.dia.isin(['2026-10-20', '2026-10-21', '2026-10-22']) & (F.flag >= 0)].copy()
U = A.assign(pf=np.where(A.flag == 1, A.pnl, 0), cf=np.where(A.flag == 1, A.coste, 0), pn=np.where(A.flag == 0, A.pnl, 0), cn=np.where(A.flag == 0, A.coste, 0)).groupby(['dia', 'fin', 'mid', 'lado_m'])[['pf', 'cf', 'pn', 'cn']].sum().reset_index()
def dif(u): return u.pf.sum() / u.cf.sum() - u.pn.sum() / u.cn.sum()
gi = {c: g.index.values for c, g in U.groupby('fin')}; cl = np.array(list(gi))
bs = [dif(U.loc[np.concatenate([gi[c] for c in rng.choice(cl, len(cl))])]) for _ in range(2000)]
lo, hi = np.quantile(bs, [0.05, 0.95]); obs = dif(U)
P(f'unidades mercado+lado {len(U)}, cierres {len(cl)}, dias {A.dia.nunique()}; rellenos con bandera {int((A.flag==1).sum())} ({(A.flag==1).mean():.3f})')
P(f'EV€ con bandera {U.pf.sum()/U.cf.sum():+.4f} (coste {U.cf.sum():.0f}) | sin bandera {U.pn.sum()/U.cn.sum():+.4f} (coste {U.cn.sum():.0f}) | dif {obs:+.4f} IC90 cierre ({lo:+.4f},{hi:+.4f})')
dPnL = -A[A.flag == 1].pnl.sum(); sims = np.zeros(2000)
for d, g in A.groupby('dia'):
    v = g.pnl.values; k = int((g.flag == 1).sum())
    if k: sims -= np.array([v[rng.choice(len(v), k, replace=False)].sum() for _ in range(2000)])
P(f'dPnL quitar marcados {dPnL:+.1f} | placebo media {sims.mean():+.1f} se {sims.std():.1f} | EXCESO {dPnL - sims.mean():+.1f} p={float((sims >= dPnL).mean()):.4f}')
pd_ = U.groupby('dia').apply(lambda u: pd.Series(dict(nf=u.cf.gt(0).sum(), dif=dif(u)))); P('por dia (dif EV€ marcado − no marcado):', {k: round(v, 3) for k, v in pd_.dif.items()})
v = pd_[pd_.nf >= 30]; P(f'dias con >=30 unidades marcadas: {len(v)}, con dif<0: {int((v.dif<0).sum())} ({(v.dif<0).mean():.2f})')
best2 = pd_.dif.sort_values().index[:2]; P(f'sin los 2 dias mas favorables {list(best2)}: dif {dif(U[~U.dia.isin(best2)]):+.4f}')
for c, g in A.groupby('coin'):
    u = U[U.mid.isin(g.mid.unique())]; P(f'  {c}: dif {dif(u):+.4f} (marcados coste {u.cf.sum():.0f})')
# latencia real
L = A[A.lead.notna()]
P(f'\nLATENCIA: rellenos con disparo en [t-1000,t]: {len(L)} ({len(L)/len(A):.3f}); lead p10/p25/p50/p75 = {np.round(L.lead.quantile([.1,.25,.5,.75]).values,0)} ms')
for thr in (90, 150, 250):
    P(f'  lead >= {thr} ms (capturable): {(L.lead>=thr).mean():.3f}  | EV€ lead>={thr}: {ev(L[L.lead>=thr]):+.4f}  lead<{thr}: {ev(L[L.lead<thr]):+.4f}')
P(f'  EV€ sin disparo en 1 s: {ev(A[A.lead.isna()]):+.4f}')
# ---------------- H2
P('\n=== H2 cuando operar (walk-forward por dia) ===')
M = F.groupby(['coin', 'mid']).agg(pnl=('pnl', 'sum'), coste=('coste', 'sum'), n=('pnl', 'size')).reset_index()
W = W.merge(M, on=['coin', 'mid'], how='left'); W['tiene_des'] = W.mid.isin(set(F.mid))
for c in ('pnl', 'coste', 'n'): W[c] = W[c].fillna(0.0)
W = W.sort_values(['coin', 'fin']).reset_index(drop=True); W['R6'] = np.nan; W['R7'] = np.nan
for c, g in W.groupby('coin'):
    f = g.fin.values; cp = np.r_[0, np.cumsum(g.pnl.values)]; cc = np.r_[0, np.cumsum(g.coste.values)]; cn = np.r_[0, np.cumsum(g.n.values)]
    i1 = np.searchsorted(f, f - 600, 'right'); i0 = np.searchsorted(f, f - 2100, 'left')
    W.loc[g.index, 'R6'] = np.where(cc[i1] - cc[i0] > 0, (cp[i1] - cp[i0]) / np.maximum(cc[i1] - cc[i0], 1e-9), np.nan); W.loc[g.index, 'R7'] = cn[i1] - cn[i0]
# ventanas sin desenlace oficial (missing) fuera
dias_des = F.groupby('dia').size(); W = W[W.dia.isin(dias_des.index)]
miss = W.groupby('dia').apply(lambda x: (~x.tiene_des & (x.n == 0)).mean()); P('ventanas por dia sin rellenos en banda (o sin desenlace):', miss.round(2).to_dict())
dias = sorted(W.dia.unique()); P('dias', dias)
def regla(tr, te, feat, peor=True):
    if feat in ('R4', 'R5'):
        e = tr.groupby(feat).apply(ev).dropna(); lvl = e.idxmin() if peor else e.idxmax(); return te[feat] == lvl, str(lvl)
    x = tr[feat].dropna()
    if len(x) < 30: return pd.Series(False, index=te.index), 'na'
    c1, c2 = np.quantile(x, [1 / 3, 2 / 3]); tt = lambda s: np.where(s.isna(), -1, np.where(s <= c1, 0, np.where(s <= c2, 1, 2)))
    e = tr.assign(t=tt(tr[feat])).query('t>=0').groupby('t').apply(ev); lvl = e.idxmin() if peor else e.idxmax()
    return pd.Series(tt(te[feat]) == lvl, index=te.index), f'T{lvl}'
ALF = 0.10 / 7; resB = {}
Bc = pd.read_csv(os.path.join(BASE, 'cola_posicion', 'datos', 'b_cola.csv'))
Bc['coin'] = Bc.coin.str.upper()
for feat in ('R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7'):
    rows = []; Bskip = []
    for i, d in enumerate(dias):
        if i < 3: continue
        tr = W[W.dia < d]; te = W[W.dia == d]
        for peor in (True, False):
            sk, lvl = regla(tr, te, feat, peor)
            rows.append(dict(dia=d, peor=peor, lvl=lvl, k=int(sk.sum()), n=len(te), dP=-te[sk].pnl.sum(), tot=te.pnl.sum(), cret=te[~sk].coste.sum(), ctot=te.coste.sum(), idx=te.index[sk.values]))
        if d in ('2026-10-20', '2026-10-21', '2026-10-22'):
            sk, _ = regla(tr, te, feat, True); mk = set(zip(te[sk].coin, te[sk].fin.astype(int)))
            b = Bc[(Bc.dia == d) & Bc.fin.notna()]; Bskip.append((b.pnl.sum(), b.coste.sum(), b[[(c, int(f)) in mk for c, f in zip(b.coin, b.fin)]].pnl.sum(), len(b)))
    R = pd.DataFrame(rows); Rp = R[R.peor]; Ri = R[~R.peor]
    exp_ = -(Rp.k / Rp.n * Rp.tot); exc = (Rp.dP - exp_).sum(); exc_inv = (Ri.dP - (-(Ri.k / Ri.n * Ri.tot))).sum()
    sims = np.zeros(2000)
    for _, r in Rp.iterrows():
        v = W[W.dia == r.dia].pnl.values
        if r.k: sims += np.array([-v[rng.choice(len(v), r.k, replace=False)].sum() for _ in range(2000)]) - (-(r.k / r.n * r.tot))
    p = float((sims >= exc).mean())
    # IC por cierre
    X = []
    for _, r in Rp.iterrows():
        te = W[W.dia == r.dia]; s = te.index.isin(r.idx); X.append(pd.DataFrame(dict(fin=te.fin.values, x=np.where(s, -te.pnl.values, 0) + (r.k / r.n) * te.pnl.values)))
    X = pd.concat(X).groupby('fin').x.sum().values; lo, hi = np.quantile([rng.choice(X, len(X)).sum() for _ in range(2000)], [0.05, 0.95])
    exd = (Rp.dP - exp_).values; sin2 = np.sort(exd)[:-2].sum(); ret = Rp.cret.sum() / Rp.ctot.sum()
    ok = exc > 0 and p < ALF and lo > 0 and sin2 > 0 and exc_inv < 0 and ret >= 0.40
    P(f'{feat}: dias test {len(Rp)} | saltadas {Rp.k.sum()}/{Rp.n.sum()} | dPnL {Rp.dP.sum():+.0f} | EXCESO {exc:+.0f} (p={p:.4f}, IC90 cierre {lo:+.0f},{hi:+.0f}) | sin2dias {sin2:+.0f} | INVERSION {exc_inv:+.0f} | ret€ {ret:.2f} | niveles {list(Rp.lvl)} | {"PASA" if ok else "FALLA"}')
    if Bskip:
        bp = sum(x[0] for x in Bskip); bc = sum(x[1] for x in Bskip); bs_ = sum(x[2] for x in Bskip)
        P(f'      transferencia a B 20-22 Oct: base pnl {bp:+.2f} sobre {bc:.1f} € ({sum(x[3] for x in Bskip)} rellenos) | dPnL B si salta {-bs_:+.2f}')
    resB[feat] = (exc, len(Rp))
tc = F.groupby('dia').coste.sum().mean(); P(f'\nEscala poblacion: Σcoste/dia medio en banda {tc:.0f} $ (todas las makers); EXCESO/dia por rasgo:', {k: round(v[0] / max(v[1], 1), 1) for k, v in resB.items()})
open(os.path.join(D, 'e1d_resultados.txt'), 'w').write('\n'.join(out) + '\n')
