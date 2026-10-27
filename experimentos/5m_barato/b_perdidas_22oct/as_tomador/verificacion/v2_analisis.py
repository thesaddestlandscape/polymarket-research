#!/usr/bin/env python3
"""v2_analisis.py -- VERIFICACION INDEPENDIENTE de AS-TOMADOR. Todo desde f_DIA.parquet (crudo) + DES (gamma). No usa datos/*.json ni scripts del autor.
tab.pkl y sets.json solo se abren al final para COMPARAR (no alimentan ningun calculo)."""
import sys, json, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion')
import vlib
from vlib import *
rng = np.random.default_rng(424242)
SEL = ['2026-10-09', '2026-10-10', '2026-10-11']
import os
TEND = int(os.environ.get('TEST_END', '21')); SUF = '' if TEND == 21 else '_sin21'
TEST = ['2026-10-%02d' % d for d in range(12, TEND + 1)]
ALLD = SEL + TEST
OUT = {}
def P(*a):
    print(*a, flush=True)
# ---------- 1) carga + derivados; acumuladores
per_day = {}; units = []; seld = []; cov = []; hist = {}
for d in ALLD:
    X, ok = load_day(d)
    bad = int((~ok).sum()); X = X[ok]
    usc = vlib._codes.get(US, -9); exc = vlib._codes.get(EX, -9)
    res = X.gana.values >= 0
    cov.append(dict(dia=d, n_fills=len(X), fills_invalidos=bad, cob_desenlace=float(res.mean()),
                    cob_cell=float(res[((X.pc > .10) & (X.pc <= .30) & ((X.fin - X.ts) > 60) & ((X.fin - X.ts) <= 300)).values].mean())))
    X['pnl_m'] = np.where(res, pnl_m(X), np.nan)
    # historico por taker (todas las bandas, SIN fee, bruto) para R_W y SEL (con fee) -- tomador = -pnl_m
    R = X[res & (X.tk.values != usc)]
    fee = FEE * R.sh.values * R.pc.values * (1 - R.pc.values)
    ct = R.sh.values * (1 - R.pc.values)
    per_day[d] = pd.DataFrame({'tk': R.tk.values, 'pg': -R.pnl_m.values, 'pn': -R.pnl_m.values - fee, 'c': ct})
    # unidades (celda, resueltas, sin wallet propia)
    T = (X.fin - X.ts).values
    cell = res & (X.pc.values > .10) & (X.pc.values <= .30) & (T > 60) & (T <= 300) & (X.mk.values != usc)
    C = X[cell].copy(); C['T'] = T[cell]
    C = C.sort_values(['mk', 'mid', 'yes', 'ts', 'tx', 'li'], kind='mergesort')
    g = C.groupby(['mk', 'mid', 'yes'], sort=False)
    C['cum'] = g.sh.cumsum(); C['prev'] = C.cum - C.sh
    C = C[C.prev < 5 - 1e-12].copy(); take = np.minimum(C.sh, 5 - C.prev); f = take / C.sh
    C['cm'] = C.coste_m * f; C['pm'] = C.pnl_m * f; C['sh2'] = take
    U = C.groupby(['mk', 'mid', 'yes'], sort=False).agg(c=('cm', 'sum'), p=('pm', 'sum'), sh=('sh2', 'sum'), pc=('pc', 'first'), fin=('fin', 'first'),
                                                      coin=('coin', 'first'), tk=('tk', 'first'), ts=('ts', 'first'), T=('T', 'first')).reset_index()
    U['dia'] = d; units.append(U)
    # SEL: fills por taker (todas las bandas) con fee, dia
    if d in SEL:
        seld.append(pd.DataFrame({'dia': d, 'tk': R.tk.values, 'pc': R.pc.values, 'pn': per_day[d].pn.values, 'c': ct}))
    P(d, 'fills', len(X), 'inval', bad, 'cob', round(float(res.mean()), 5), 'unidades', len(U))
    del X, R, C
cov = pd.DataFrame(cov); P(cov.to_string()); OUT['cobertura'] = cov.to_dict('records')
U = pd.concat(units, ignore_index=True)
U['taker'] = U.tk
inv_ = vlib.inv(); U['cierre'] = U.fin.astype('int64')
UT = U[U.dia.isin(TEST)].reset_index(drop=True)
P('unidades TEST', len(UT), 'EV_total', UT.p.sum() / UT.c.sum(), 'n cierres', UT.cierre.nunique(), 'takers', UT.tk.nunique())
OUT['test_total'] = dict(n=len(UT), EV=float(UT.p.sum() / UT.c.sum()), cierres=int(UT.cierre.nunique()), takers=int(UT.tk.nunique()))
# ---------- 2) SEL (09-11) -> S_A / S_B
A = pd.concat(seld, ignore_index=True)
usc = vlib._codes.get(US, -9); exc = vlib._codes.get(EX, -9)
A = A[(A.tk != usc) & (A.tk != exc)]
def sel(A, nmin, cmin, dmin, band=None, cost_fee=False):
    if band is not None: A = A[(A.pc > band[0]) & (A.pc <= band[1])]
    g = A.groupby('tk').agg(n=('pn', 'size'), pnl=('pn', 'sum'), cost=('c', 'sum'))
    gd = A.groupby(['tk', 'dia']).agg(n=('pn', 'size'), pnl=('pn', 'sum')).reset_index(); gd = gd[gd.n >= dmin]
    g['dpos'] = gd[gd.pnl > 0].groupby('tk').size().reindex(g.index).fillna(0); g['roi'] = g.pnl / g.cost
    return g, g[(g.n >= nmin) & (g.cost >= cmin) & (g.roi >= .02) & (g.dpos >= 2)]
gA, okA = sel(A, 100, 200, 10); gB, okB = sel(A, 30, 50, 5, (.10, .30))
SA = set(okA.index); SB = set(okB.index)
P('SEL fills', len(A), 'takers', A.tk.nunique(), 'S_A', len(SA), 'S_B', len(SB), 'solape', len(SA & SB))
OUT['SEL'] = dict(fills=len(A), takers=int(A.tk.nunique()), S_A=len(SA), S_B=len(SB), solape=len(SA & SB))
# sensibilidades de seleccion: coste incl. fee en denominador; umbral 3/3 dias
def sel_alt(A):
    g = A.groupby('tk').agg(n=('pn', 'size'), pnl=('pn', 'sum'), cost=('c', 'sum')); fee = (A.assign(f=0.0)); 
    return g
# ---------- 3) metricas (EXCESO, IC90 cierre, permutacion, monedas, mitades, top wallet)
pnl = UT.p.values; c = UT.c.values
cl = pd.factorize(UT.cierre)[0]; ncl = cl.max() + 1
dayi = pd.factorize(UT.dia)[0]; nday = dayi.max() + 1
strat = pd.factorize(UT.dia + '|' + UT.coin + '|' + np.floor(UT.pc.values / .05 + 1e-9).astype(int).astype(str))[0]
coin = UT.coin.values; tkv = UT.tk.values
def ev(m): return pnl[m].sum() / c[m].sum() if m.any() else np.nan
def exc_(flag, m=None):
    m = np.ones(len(UT), bool) if m is None else m
    r = m & ~flag
    return pnl[r].sum() / c[r].sum() - pnl[m].sum() / c[m].sum()
def boot_cl(flag, B=2000, idx=cl, nc=ncl):
    Pt = np.bincount(idx, pnl, nc); Ct = np.bincount(idx, c, nc); Pr = np.bincount(idx, pnl * ~flag, nc); Cr = np.bincount(idx, c * ~flag, nc)
    w = rng.multinomial(nc, np.ones(nc) / nc, size=B).astype(float)
    e = (w @ Pr) / (w @ Cr) - (w @ Pt) / (w @ Ct); return [float(x) for x in np.percentile(e, [5, 95])]
order0 = np.argsort(strat, kind='stable'); st0 = strat[order0]
def perm_strat(flag, Bp=2000):
    base = exc_(flag); f0 = flag[order0]; p0 = pnl[order0]; c0 = c[order0]; tot = p0.sum() / c0.sum(); null = np.empty(Bp)
    for b in range(Bp):
        idx = np.argsort(st0 + rng.random(len(st0))); g = f0[idx]
        null[b] = p0[~g].sum() / c0[~g].sum() - tot
    return base, float((1 + (null >= base).sum()) / (Bp + 1)), float(np.percentile(null, 95))
def full(name, flag, pool_for_placebo=None, Bp=2000):
    r = dict(n_flag=int(flag.sum()), takers_flag=int(len(np.unique(tkv[flag]))), frac_eur=float(c[flag].sum() / c.sum()), EV_total=float(ev(np.ones(len(UT), bool))),
             EV_IN=float(ev(flag)) if flag.any() else None, EV_OUT=float(ev(~flag)))
    base, p, p95 = perm_strat(flag, Bp); r.update(EXCESO=float(base), p_perm_unit=p, null_p95=p95, IC90_cierre=boot_cl(flag), IC90_dia=boot_cl(flag, 2000, dayi, nday))
    r['monedas'] = {k: float(exc_(flag, coin == k)) for k in ('ETH', 'SOL', 'XRP')}
    r['EV_IN_moneda'] = {k: (float(ev(flag & (coin == k))) if (flag & (coin == k)).any() else None) for k in ('ETH', 'SOL', 'XRP')}
    mit = {'12-14': ('2026-10-12', '2026-10-14'), '15-18': ('2026-10-15', '2026-10-18'), '19-21': ('2026-10-19', '2026-10-21')}
    r['mitades'] = {k: float(exc_(flag, ((UT.dia >= a) & (UT.dia <= b)).values)) for k, (a, b) in mit.items()}
    sh = pd.Series(c[flag]).groupby(tkv[flag]).sum().sort_values(ascending=False); r['top_wallet'] = float(sh.iloc[0] / sh.sum()) if len(sh) else None
    r['top3_wallet'] = float(sh.head(3).sum() / sh.sum()) if len(sh) else None
    # por dia y sin 2 mejores dias
    ed = {d: float(exc_(flag, (UT.dia == d).values)) for d in TEST}; r['por_dia'] = ed
    best = sorted(ed, key=ed.get, reverse=True)[:2]; r['sin_2_mejores_dias'] = float(exc_(flag, ~UT.dia.isin(best).values)); r['dias_exc_pos'] = int(sum(v > 0 for v in ed.values()))
    # leave-one-taker-out del top-3 banderado en EUR
    r['EXC_sin_top1_taker_flag'] = float(exc_(flag & (tkv != sh.index[0]))) if len(sh) else None
    # placebo de seleccion a nivel TOMADOR: conjuntos aleatorios de takers activos en SEL con n>=100,c>=200 (sin el criterio de ROI), mismo numero que los banderados
    if pool_for_placebo is not None:
        k = r['takers_flag']; pool = np.array(sorted(set(pool_for_placebo) & set(np.unique(tkv)))); ex = []
        for _ in range(2000):
            pick = rng.choice(pool, min(k, len(pool)), replace=False); ex.append(exc_(np.isin(tkv, pick)))
        ex = np.array(ex); r['placebo_pool'] = dict(n_pool=len(pool), media=float(ex.mean()), p95=float(np.percentile(ex, 95)), p_emp=float((1 + (ex >= base).sum()) / (len(ex) + 1)))
    P(name, json.dumps({k: r[k] for k in ('n_flag', 'takers_flag', 'frac_eur', 'EV_IN', 'EV_OUT', 'EXCESO', 'IC90_cierre', 'IC90_dia', 'p_perm_unit', 'monedas', 'mitades', 'top_wallet', 'sin_2_mejores_dias', 'dias_exc_pos')}, default=float))
    if 'placebo_pool' in r: P('   placebo', r['placebo_pool'])
    return r
act = A.groupby('tk').agg(n=('pn', 'size'), cost=('c', 'sum')); pool = list(act[(act.n >= 100) & (act.cost >= 200)].index)
OUT['S_A'] = full('S_A', np.isin(tkv, list(SA)), pool)
OUT['S_B'] = full('S_B', np.isin(tkv, list(SB)), pool)
# ---------- 4) R_W walk-forward (tk_score = ROI BRUTO acumulado dias previos, n>=30, c>=50)
N = max(vlib._codes.values()) + 1
cum_p = np.zeros(N); cum_c = np.zeros(N); cum_n = np.zeros(N)
score = np.full(len(UT), np.nan)
dayidx = {d: np.where(UT.dia.values == d)[0] for d in TEST}
for d in ALLD:
    if d in TEST:
        ii = dayidx[d]; t = tkv[ii]; ok = (cum_n[t] >= 30) & (cum_c[t] >= 50)
        s = np.full(len(ii), np.nan); s[ok] = cum_p[t[ok]] / cum_c[t[ok]]; score[ii] = s
    D = per_day[d]; np.add.at(cum_p, D.tk.values, D.pg.values); np.add.at(cum_c, D.tk.values, D.c.values); np.add.at(cum_n, D.tk.values, 1)
P('cobertura tk_score', float(np.isfinite(score).mean()))
fW = np.nan_to_num(score, nan=-9) >= .02
OUT['cobertura_tk_score'] = float(np.isfinite(score).mean())
OUT['R_W'] = full('R_W', fW, None)
bins = [-9, -.02, 0, .02, .05, 9]; lab = ['<-0.02', '[-0.02,0)', '[0,0.02)', '[0.02,0.05)', '>=0.05']
ib = pd.cut(pd.Series(score), bins, labels=lab, right=False)
dose = {l: dict(n=int((ib == l).sum()), frac_eur=float(c[(ib == l).values].sum() / c.sum()), EV=float(ev((ib == l).values))) for l in lab}
dose['sin_hist'] = dict(n=int(np.isnan(score).sum()), EV=float(ev(np.isnan(score)))); OUT['dosis'] = dose; P(dose)
b = (score < -.02); OUT['bin_lt_m02'] = dict(EV_por_moneda={k: float(ev(b & (coin == k))) for k in ('ETH', 'SOL', 'XRP')}, EV_por_dia={d: float(ev(b & (UT.dia == d).values)) for d in TEST if (b & (UT.dia == d).values).any()})
P(OUT['bin_lt_m02'])
# ---------- 5) persistencia
def persist(sel_u, test_u, nm):
    a = sel_u.groupby('tk').agg(p=('p', 'sum'), c=('c', 'sum')); bb = test_u.groupby('tk').agg(p=('p', 'sum'), c=('c', 'sum'))
    J = a.join(bb, lsuffix='_a', rsuffix='_b', how='inner'); J = J[(J.c_a >= 100) & (J.c_b >= 100)]
    from scipy import stats
    ra = -J.p_a / J.c_a; rb = -J.p_b / J.c_b
    r = dict(n=len(J), spearman=[float(x) for x in stats.spearmanr(ra, rb)], pearson=[float(x) for x in stats.pearsonr(ra, rb)])
    P('persistencia', nm, r); return r
US_ = U[U.dia.isin(SEL)]
OUT['persist_autor_def'] = persist(US_, UT, 'unidades celda, denominador coste maker (def. autor)')
# persistencia all-band taker ROI SEL -> TEST (fills de todas las bandas, tomador, bruto) con n takers mayor
from scipy import stats
sa = pd.concat([per_day[d] for d in SEL]).groupby('tk').agg(p=('pg', 'sum'), c=('c', 'sum'), n=('pg', 'size'))
sb = pd.concat([per_day[d] for d in TEST]).groupby('tk').agg(p=('pg', 'sum'), c=('c', 'sum'), n=('pg', 'size'))
J = sa.join(sb, lsuffix='_a', rsuffix='_b', how='inner'); J = J[(J.n_a >= 100) & (J.n_b >= 100) & (J.c_a >= 100) & (J.c_b >= 100)]
ra = J.p_a / J.c_a; rb = J.p_b / J.c_b
OUT['persist_allband'] = dict(n=len(J), spearman=[float(x) for x in stats.spearmanr(ra, rb)], pearson=[float(x) for x in stats.pearsonr(ra, rb)]); P('persist all-band SEL->TEST', OUT['persist_allband'])
q = pd.qcut(ra, 5, labels=False, duplicates='drop'); OUT['persist_quintiles_allband'] = {int(k): dict(n=int((q == k).sum()), roi_sel=float(J.p_a[q == k].sum() / J.c_a[q == k].sum()), roi_test=float(J.p_b[q == k].sum() / J.c_b[q == k].sum())) for k in sorted(q.unique())}
P(OUT['persist_quintiles_allband'])
# tomadores de S_A: su ROI bruto en TEST all-band (persisten?)
mA = J.index.isin(list(SA)); OUT['SA_roi_sel_vs_test_allband'] = dict(n=int(mA.sum()), roi_sel=float(J.p_a[mA].sum() / J.c_a[mA].sum()) if mA.any() else None, roi_test=float(J.p_b[mA].sum() / J.c_b[mA].sum()) if mA.any() else None); P(OUT['SA_roi_sel_vs_test_allband'])
# ---------- 6) comparacion con el autor (solo al final)
try:
    S = json.load(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/datos/sets.json'))
    ia = {v: k for k, v in vlib._codes.items()}; mine = {k: set(ia[x] for x in v) for k, v in (('S_A', SA), ('S_B', SB))}
    for k in ('S_A', 'S_B'):
        a = set(S[k]); b = mine[k]; OUT['cmp_set_' + k] = dict(autor=len(a), mio=len(b), inter=len(a & b), solo_autor=len(a - b), solo_mio=len(b - a)); P('cmp set', k, OUT['cmp_set_' + k])
    T0 = pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl'); T0 = T0[T0.dia >= '2026-10-12']
    OUT['cmp_tab'] = dict(n_autor=len(T0), n_mio=len(UT), EV_autor=float(T0.pnl.sum() / T0.c.sum()), EV_mio=float(UT.p.sum() / UT.c.sum()), c_autor=float(T0.c.sum()), c_mio=float(UT.c.sum()))
    k1 = set(zip(T0.dia, T0.maker.str.lower(), T0.mkt.astype('int64'), T0.lado_c)); k2 = set(zip(UT.dia, [ia[x] for x in UT.mk], UT.mid, np.where(UT.yes, 'YES', 'NO')))
    OUT['cmp_tab']['claves_inter'] = len(k1 & k2); OUT['cmp_tab']['solo_autor'] = len(k1 - k2); OUT['cmp_tab']['solo_mio'] = len(k2 - k1); P(OUT['cmp_tab'])
    st = T0.groupby('dia').agg(n=('c', 'size'), c=('c', 'sum'), p=('pnl', 'sum')); mt = UT.groupby('dia').agg(n=('c', 'size'), c=('c', 'sum'), p=('p', 'sum')); P(pd.concat([st, mt], axis=1, keys=['autor', 'mio']).round(2).to_string())
except Exception as e:
    P('cmp error', repr(e))
json.dump(OUT, open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion/v2_resultados%s.json' % SUF, 'w'), indent=1, default=float)
UT.to_pickle('/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/UT%s.pkl' % SUF); pd.to_pickle(dict(codes=vlib._codes, SA=SA, SB=SB), '/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/sets_codes%s.pkl' % SUF)
