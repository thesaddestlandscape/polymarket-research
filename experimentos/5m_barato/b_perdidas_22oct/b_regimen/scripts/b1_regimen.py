#!/usr/bin/env python3
"""b1_regimen.py -- B-REGIMEN (OLA 7). Ejecuta PREREG_BREGIMEN.md (sha 9a59851d...). Solo lectura de tab.pkl y barras Binance. Sin red."""
import sys, os, json
import numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/q_techo/scripts')
from qlib import MapQ, clus, boot, boot_ratio, perm_cierre, tramo, COINS
HERE = os.path.dirname(os.path.abspath(__file__)); OUTD = os.path.join(HERE, '..', 'datos')
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
T = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl'); T = T[T.act.isin(COINS)].sort_values(['dia', 'ts']).reset_index(drop=True)
# ---- MAP walk-forward (E1)
T['q_MAP'] = np.nan
for d in sorted(T.dia.unique()):
    for a in COINS:
        tr = T[(T.dia < d) & (T.act == a)]; mk = ((T.dia == d) & (T.act == a)).values
        if len(tr) > 500: T.loc[mk, 'q_MAP'] = MapQ().fit(tr).predict(T[mk])
T['E1'] = T.q_MAP - T.pc; T['E2'] = T.mid5 - T.pc; T['E3'] = T.fv_gap
# ---- regimen causal desde barras 1m
z = np.load('/root/polymarket-research-datalogs/regimen_5m/barras_bookticker.npz')
T['z240'] = np.nan; T['z1440'] = np.nan; T['rpre_mine'] = np.nan
for a in COINS:
    m0 = int(z[a + '_m0']); Pp = pd.Series(z[a + '_P']).ffill(limit=5).values; lp = np.log(Pp); R = np.diff(lp, prepend=np.nan)
    cq = np.concatenate([[0.0], np.cumsum(np.where(np.isfinite(R), R ** 2, 0.0))]); cn = np.concatenate([[0], np.cumsum(np.isfinite(R).astype(int))])
    mk = (T.act == a).values; io = (T.tmin.values[mk] - m0).astype(int)
    ok = (io - 1440 >= 1) & (io < len(lp)); s = np.full(len(io), np.nan)
    cnt = cn[np.where(ok, io, 0) + 1] - cn[np.where(ok, io - 1439, 1)]; sq = cq[np.where(ok, io, 0) + 1] - cq[np.where(ok, io - 1439, 1)]
    s[ok & (cnt >= 0.8 * 1440)] = np.sqrt(sq / np.maximum(cnt, 1))[ok & (cnt >= 0.8 * 1440)]
    g = lambda k: np.where(ok, lp[np.clip(io - k, 0, len(lp) - 1)], np.nan)
    z240 = (g(0) - g(240)) / (s * np.sqrt(240)); z1440 = (g(0) - g(1440)) / (s * np.sqrt(1440)); rp = (g(0) - g(15)) * 1e4
    T.loc[mk, 'z240'] = z240; T.loc[mk, 'z1440'] = z1440; T.loc[mk, 'rpre_mine'] = rp
v = T.z240.notna() & T.rpre.notna(); P('sanity: cobertura z240', round(float(T.z240.notna().mean()), 4), '| corr(rpre_mine, rpre tab)', round(float(np.corrcoef(T.rpre_mine[v], T.rpre[v])[0, 1]), 4))
T['reg'] = np.where(T.z240 >= 1, 'ALC', np.where(T.z240 <= -1, 'BAJ', np.where(T.z240.isna(), 'NA', 'LAT')))
sg = np.where(T.lado_c == 'YES', 1.0, -1.0); T['zs'] = sg * T.z240
T['aln'] = np.where(T.zs >= 1, 'ALIGN', np.where(T.zs <= -1, 'COUNTER', np.where(T.zs.isna(), 'NA', 'FLAT')))
T['cls'] = np.where(T.CON == 1, 'CON', np.where(T.rpre_s <= -7.7, 'CONTRA', np.where(T.rpre_s.isna(), 'NA', 'NEU')))
# ---- AR2h
fin = T.fin.values.astype(float); o = np.argsort(fin, kind='stable'); fs = fin[o]; cp = np.concatenate([[0], np.cumsum(T.p.values[o])]); cc = np.concatenate([[0], np.cumsum(T.c.values[o])])
hi = np.searchsorted(fs, T.ts.values - 60, 'right'); lo = np.searchsorted(fs, T.ts.values - 7200, 'right'); n = hi - lo
T['AR2h'] = np.where(n >= 200, (cp[hi] - cp[lo]) / np.maximum(cc[hi] - cc[lo], 1e-9), np.nan)
T['hb'] = (T.hora // 6).astype(int); T['tr'] = tramo(T.pc.values); T['Tt'] = pd.cut(T['T'], [0, 120, 200, 301], labels=['T<120', 'T120-200', 'T200-300'])
P1 = T[T.dia <= '2026-10-16'].reset_index(drop=True); P2 = T[T.dia >= '2026-10-17'].reset_index(drop=True); PER = {'P1 09-16': P1, 'P2 17-21': P2}
for k, X in PER.items(): P(f'{k}: n={len(X)} EUR={X.c.sum():.0f} EV={X.p.sum()/X.c.sum():+.4f} dias={X.dia.nunique()} cierres={X.cierre.nunique()}')
def evs(X, m): return float(X.p.values[m].sum() / X.c.values[m].sum()) if m.sum() and X.c.values[m].sum() > 0 else np.nan
# ---- H-D descriptiva
P('\n#### H-D: EV/EUR por clase de regimen x CON/NEU/CONTRA (n, EUR) por periodo')
for k, X in PER.items():
    for key in ('reg', 'aln'):
        t = X[X.cls != 'NA'].groupby([key, 'cls']).agg(n=('c', 'size'), eur=('c', 'sum'), pnl=('p', 'sum')); t['EV'] = t.pnl / t.eur
        P(f'--- {k} por {key}\n' + t[['n', 'eur', 'EV']].round(3).to_string())
    t = X[X.reg != 'NA'].groupby(['act', 'reg', 'cls']).agg(eur=('c', 'sum'), pnl=('p', 'sum')); t['EV'] = t.pnl / t.eur; P(f'--- {k} por moneda x reg x cls (EV)\n' + t.EV.unstack().round(3).to_string())
P('\n#### Delta_dir = EV(COUNTER) - EV(ALIGN) (z240 respecto al lado), IC90 por cierre')
rng = np.random.default_rng(20261024)
def boot_diff(X, ma, mb, nb=2000):
    cl = clus(X); k = cl.max() + 1; A = [np.bincount(cl, weights=v * m, minlength=k) for v, m in ((X.p.values, ma), (X.c.values, ma), (X.p.values, mb), (X.c.values, mb))]
    idx = rng.integers(0, k, (nb, k)); d = A[0][idx].sum(1) / np.maximum(A[1][idx].sum(1), 1e-9) - A[2][idx].sum(1) / np.maximum(A[3][idx].sum(1), 1e-9)
    return float(np.percentile(d, 5)), float(np.percentile(d, 95))
for k, X in PER.items():
    a = (X.aln == 'COUNTER').values; b = (X.aln == 'ALIGN').values; lo_, hi_ = boot_diff(X, a, b)
    P(f'{k}: EV COUNTER {evs(X, a):+.3f} (EUR {X.c.values[a].sum():.0f}) | EV ALIGN {evs(X, b):+.3f} (EUR {X.c.values[b].sum():.0f}) | FLAT {evs(X, (X.aln=="FLAT").values):+.3f} | Delta_dir {evs(X,a)-evs(X,b):+.3f} IC90 [{lo_:+.3f},{hi_:+.3f}]')
    for ac in COINS:
        ma = a & (X.act == ac).values; mb = b & (X.act == ac).values; P(f'    {ac}: COUNTER {evs(X, ma):+.3f} ALIGN {evs(X, mb):+.3f}')
# ---- evaluacion de una regla
def rep(nom, X, skip, perm=True):
    cl = clus(X); c, p = X.c.values, X.p.values; r = ~skip
    ret = c[r].sum() / c.sum(); evr = p[r].sum() / c[r].sum() if c[r].sum() > 0 else np.nan; evs_ = p[skip].sum() / c[skip].sum() if c[skip].sum() > 0 else np.nan
    dp = -p[skip].sum(); lo, hi = boot(-p * skip, cl); pp = perm_cierre(X, skip)[0] if perm and skip.sum() > 0 else np.nan
    dd = pd.Series(-p * skip).groupby(X.dia.values).sum(); sin2 = dd.drop(dd.sort_values(ascending=False).index[:2]).sum() if len(dd) > 2 else np.nan
    pm = {a: round(float(-p[skip & (X.act.values == a)].sum()), 1) for a in COINS}
    gate = bool(dp > 0 and lo > 0 and pp < 0.0036 and (dd > 0).mean() >= 0.6 and sin2 > 0 and ret >= 0.4)
    P(f'{nom}: skip {int(skip.sum())}/{len(X)} ret {ret:.3f} | EV_all {p.sum()/c.sum():+.4f} EV_ret {evr:+.4f} EV_skip {evs_:+.4f} | dPnL {dp:+.1f} IC90 [{lo:+.1f},{hi:+.1f}] p_perm {pp:.4f} | dias+ {(dd>0).sum()}/{len(dd)} sin2 {sin2:+.1f} haircut50 {dp/2:+.1f} | moneda {pm} | GATE_FORMAL {gate}')
    return dict(dp=float(dp), ic=(lo, hi), p=float(pp), ret=float(ret), ev_ret=float(evr), sin2=float(sin2), gate=gate)
# ---- ajuste y reglas
def fit_R(Xf, key):
    ev_contra = evs(Xf, (Xf.cls == 'CONTRA').values); S = []
    for cel in sorted(Xf[key].unique()):
        if cel == 'NA': continue
        m = ((Xf[key] == cel) & (Xf.cls == 'CON')).values
        if Xf.c.values[m].sum() >= 1000 and evs(Xf, m) - ev_contra < -0.05: S.append(cel)
    return S
def fit_N(Xf):
    S = []
    for a in COINS:
        for r in ('ALC', 'LAT', 'BAJ'):
            m = ((Xf.act == a) & (Xf.reg == r)).values
            if Xf.c.values[m].sum() >= 1000 and evs(Xf, m) < -0.05: S.append((a, r))
    return S
def fit_V(Xf, k):
    cuts = {a: Xf[Xf.act == a][k].quantile(0.70) for a in COINS}; lowc = {a: Xf[Xf.act == a][k].quantile(0.30) for a in COINS}
    top = np.zeros(len(Xf), bool)
    for a in COINS: top |= ((Xf.act == a) & (Xf[k] >= cuts[a])).values
    cand = bool(evs(Xf, top) < evs(Xf, ~top) - 0.03)
    return dict(cuts=cuts, low=lowc, cand=cand, ev_top=evs(Xf, top), ev_rest=evs(Xf, ~top))
def apply_V(X, k, f, inv=False):
    s = np.zeros(len(X), bool)
    for a in COINS: s |= ((X.act == a) & ((X[k] <= f['low'][a]) if inv else (X[k] >= f['cuts'][a]))).values
    return s
def apply_R(X, key, S): return ((X.cls == 'CON') & X[key].isin(S)).values
def apply_N(X, S):
    s = np.zeros(len(X), bool)
    for (a, r) in S: s |= ((X.act == a) & (X.reg == r)).values
    return s
RES = {}
for nom, (Xf, Xe) in {'F_A (ajuste P1 -> eval P2)': (P1, P2), 'F_B (ajuste P2 -> eval P1; OOS GENUINO)': (P2, P1)}.items():
    P(f'\n######## {nom}'); R = {}
    S_aln = fit_R(Xf, 'aln'); S_reg = fit_R(Xf, 'reg'); S_N = fit_N(Xf); P(f'ajuste: S_R(aln)={S_aln}  S_R2(reg)={S_reg}  S_N={S_N}')
    P('CONTROL R0 (CONTRA-only incondicional, saltar todos CON)'); R['R0'] = rep('R0', Xe, (Xe.cls == 'CON').values)
    if S_aln: R['H-R'] = rep('H-R (CON x aln)', Xe, apply_R(Xe, 'aln', S_aln))
    if S_reg: R['H-R2'] = rep('H-R2 (CON x reg)', Xe, apply_R(Xe, 'reg', S_reg))
    if S_N: R['H-N'] = rep('H-N (celdas moneda x reg no pujar)', Xe, apply_N(Xe, S_N))
    for k in ('E1', 'E2', 'E3'):
        f = fit_V(Xf, k); P(f'V({k}) ajuste: EV top30 {f["ev_top"]:+.3f} vs resto {f["ev_rest"]:+.3f} candidato={f["cand"]} cortes={ {a: round(v,3) for a,v in f["cuts"].items()} }')
        sk = apply_V(Xe, k, f); R['V_' + k] = rep(f'V_{k} (cand={f["cand"]})', Xe, sk)
        R['Vinv_' + k] = rep(f'   control inversion V_{k} (cola baja)', Xe, apply_V(Xe, k, f, inv=True))
        RES[(nom, k)] = f
    R['H-N2'] = rep('H-N2 (AR2h<=-0,10, sin ajuste)', Xe, (Xe.AR2h <= -0.10).values)
    P(f'(AR2h cobertura en eval: {float(Xe.AR2h.notna().mean()):.3f}; fraccion con AR2h<=-0,10: {float((Xe.AR2h<=-0.10).mean()):.3f})')
    RES[nom] = (R, S_aln, S_reg, S_N)
# ---- perfil por decil de E por periodo
P('\n#### Perfil EV por decil de cada medida de edge aparente (EUR-ponderado), por periodo')
for k in ('E1', 'E2', 'E3'):
    for pn, X in PER.items():
        v = X[X[k].notna()].copy(); v['dec'] = pd.qcut(v[k].rank(method='first'), 10, labels=False)
        t = v.groupby('dec').agg(eur=('c', 'sum'), pnl=('p', 'sum'), pc=('pc', 'mean'), E=(k, 'mean')); t['EV'] = t.pnl / t.eur
        P(f'{k} {pn}: EV por decil (bajo->alto) ' + ' '.join(f'{x:+.3f}' for x in t.EV.values) + ' | E medio ' + ' '.join(f'{x:+.3f}' for x in t.E.values))
# ---- H-C combinada (programatica)
P('\n######## H-C combinada (reglas con dPnL>0 y menor p en F_B, union; mismas reglas ajustadas en cada pliegue)')
Rb = RES['F_B (ajuste P2 -> eval P1; OOS GENUINO)'][0]
cand = [(v['p'], k) for k, v in Rb.items() if k not in ('R0',) and not k.startswith('Vinv') and v['dp'] > 0 and v['p'] == v['p']]
cand.sort(); passing = [k for p, k in cand if Rb[k]['gate']]; elegidas = passing if passing else [k for p, k in cand[:2]]
P(f'reglas elegidas para H-C: {elegidas} (pasan gate formal en F_B: {passing}) -> {"FORMAL" if passing else "EXPLORATORIA"}')
def build(X, nomF, Xf):
    s = np.zeros(len(X), bool); R_, S_aln, S_reg, S_N = RES[nomF]
    for k in elegidas:
        if k == 'H-R': s |= apply_R(X, 'aln', S_aln)
        elif k == 'H-R2': s |= apply_R(X, 'reg', S_reg)
        elif k == 'H-N': s |= apply_N(X, S_N)
        elif k == 'H-N2': s |= (X.AR2h <= -0.10).values
        elif k.startswith('V_'): s |= apply_V(X, k[2:], RES[(nomF, k[2:])])
    return s
for nomF, (Xf, Xe) in {'F_A (ajuste P1 -> eval P2)': (P1, P2), 'F_B (ajuste P2 -> eval P1; OOS GENUINO)': (P2, P1)}.items():
    P(nomF); rep('  H-C', Xe, build(Xe, nomF, Xf))
json.dump({'elegidas': elegidas, 'passing': passing}, open(OUTD + '/b1_resumen.json', 'w'))
T.drop(columns=['maker', 'taker']).to_pickle('/mnt/HC_Volume_106538179/agentes_datos/b_regimen/tab_reg.pkl')
open(OUTD + '/b1_resultados.txt', 'w').write('\n'.join(OUT))
