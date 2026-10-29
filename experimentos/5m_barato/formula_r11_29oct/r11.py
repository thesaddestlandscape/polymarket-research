#!/usr/bin/env python3
"""r11: rellenos REALES de B vs simulador estricto (travesia), sin auto-print; modelo de relleno (logit) TUNE 20-21 -> TEST 22-23;
brecha real-sim de la politica vigente de B; EV real por posicion de cola. Manda PREREG_R11.md (sha 6e3170e0...). Solo lectura."""
import sys, collections, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/calibracion_etiqueta/v2')
import v2lib
DL = '/root/polymarket-research-datalogs/calibracion_etiqueta/'
OUT = '/root/polymarket-research/experimentos/5m_barato/formula_r11_29oct/'
L = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); L.append(s)
O = pd.read_csv(DL + 'ordenes_b.csv'); FO = pd.read_csv(DL + 'b_fills_onchain.csv')
FO = FO[FO['tipo'] == 'F'] if 'tipo' in FO else FO
own = collections.defaultdict(list)
for r in FO.itertuples(): own[r.order_hash.lower()].append(float(r.taker_amt))
EPS = [0, 250, 1000]; PLAC = 90000
rows = []; nmatch = collections.Counter()
for dia in sorted(O['dia'].unique()):
    D = v2lib.Dia(dia); used = collections.defaultdict(dict)   # tk -> {idx: size_restante}
    Od = O[O['dia'] == dia].sort_values('t_ini')
    for o in Od.itertuples():
        tk = str(o.tok); cp = D.comp.get(tk); p = float(o.precio); ti = o.t_ini * 1000; tf = o.t_fin * 1000
        def prints(t0, t1):
            res = []   # (t, size_restante, worse, at, tk, idx)
            for tt, side_ok, f_at, f_w in ((tk, 0, lambda x: abs(x - p) < 1e-9, lambda x: x < p - 1e-9),
                                           (cp, 1, lambda x: abs(x - (1 - p)) < 1e-9, lambda x: x > 1 - p + 1e-9)):
                a = D.tr.get(tt) if tt else None
                if a is None: continue
                lo, hi = np.searchsorted(a[:, 0], [t0, t1 + 1e-9])
                for j in range(lo, hi):
                    if D.dup[tt][j] or a[j, 2] != side_ok: continue
                    pr = a[j, 1]; at = f_at(pr); w = f_w(pr)
                    if not (at or w): continue
                    sz = used[tt].get(j, a[j, 3])
                    res.append((a[j, 0], sz, w, at, tt, j))
            res.sort(); return res
        # ---- casado de prints propios (auto-print)
        fills = own.get(o.oid.lower(), []); own_t = []
        for sf in fills:
            cand = [x for x in prints(ti - 2000, tf + 5000) if x[3] and x[1] > 1e-9]
            dist = lambda x: 0 if ti <= x[0] <= tf + 250 else min(abs(x[0] - ti), abs(x[0] - tf - 250))
            ex = [x for x in cand if abs(x[1] - sf) < 0.011]
            if ex:
                x = min(ex, key=dist); used[x[4]][x[5]] = 0.0; own_t.append(x[0]); nmatch['exacto'] += 1
            else:
                ge = [x for x in cand if x[1] >= sf - 0.011]
                if ge:
                    x = min(ge, key=dist); used[x[4]][x[5]] = max(0.0, x[1] - sf); own_t.append(x[0]); nmatch['resta'] += 1
                else: nmatch['sin_casar'] += 1
        rec = dict(oid=o.oid, dia=dia, puja=o.puja, coin=o.coin, p=p, size=float(o.size), cola=float(o.cola), off=float(o.off_c), bs=float(o.bs),
                   vida=max(0.0, tf - ti), fill=int(o.fill), acc=float(o.acc_llena), coste=float(o.coste), pnl=float(o.pnl), gana=float(o.gana_lado),
                   T=float(o.T), n_own=len(fills), own_casado=len(own_t))
        for e in EPS:
            pr = prints(ti, tf + e); rec['Vt%d' % e] = sum(x[1] for x in pr if x[2]); rec['Va%d' % e] = sum(x[1] for x in pr if x[3])
        # con propios (para Capa1-v2 contaminada y M_incl): tamaños originales
        a_all = v2lib.lleno(D.consumos(tk, p, ti, tf + 250), ti, tf, 250, 0.0, 0.5, float(o.size), 0.0)
        rec['capa1_incl'] = int(a_all is not None)
        cons = D.consumos(tk, p, ti, tf + 250); rec['Vt_incl'] = sum(c[1] for c in cons if c[2]); rec['Va_incl'] = sum(c[1] for c in cons if not c[2])
        pr = prints(ti + PLAC, tf + 250 + PLAC); rec['Vt_pl'] = sum(x[1] for x in pr if x[2]); rec['Va_pl'] = sum(x[1] for x in pr if x[3])
        rows.append(rec)
    P('dia %s: %d ordenes procesadas' % (dia, len(Od)))
R = pd.DataFrame(rows); R.to_csv(OUT + 'ordenes_r11.csv.gz', index=False)
P('casado auto-print: %s (rellenos on-chain de ordenes %d)' % (dict(nmatch), sum(len(v) for v in own.values())))
# ---------------- categorias
def cat(vt, va, oc): return np.where(vt > 0, 'A', np.where(va > 0, 'B', np.where(oc > 0, 'C', 'D')))
R['cat'] = cat(R['Vt250'], R['Va250'], R['own_casado'] * (R['fill'] > 0))
rng = np.random.default_rng(1129)
def ev_ic(df, B=2000):
    if df['coste'].sum() <= 0: return (np.nan, np.nan, np.nan)
    g = df.groupby('puja')[['pnl', 'coste']].sum().values; e = g[:, 0].sum() / g[:, 1].sum(); bs = []
    for _ in range(B):
        i = rng.integers(0, len(g), len(g)); bs.append(g[i, 0].sum() / max(g[i, 1].sum(), 1e-9))
    return e, *np.percentile(bs, [5, 95])
def porday(df):
    g = df.groupby('dia')[['pnl', 'coste']].sum(); return ' '.join('%s:%+.3f' % (d[5:], r.pnl / r.coste) if r.coste > 0 else '%s:nan' % d[5:] for d, r in g.iterrows())
P('\n== (1) Rellenos REALES por categoria (orden; prints ajenos en [t_ini, t_fin+250 ms])')
F = R[R['fill'] == 1]
for c in 'ABCD':
    s = F[F['cat'] == c]; a = R[R['cat'] == c]; e, lo, hi = ev_ic(s)
    P('  %s  rellenos %3d (%.1f %%) | ordenes en cat %4d P(relleno) %.3f | coste %6.2f EUR pnl %+7.2f EV %+.3f IC90puja [%+.3f,%+.3f] | por dia %s' % (
        c, len(s), 100 * len(s) / len(F), len(a), len(s) / max(1, len(a)), s['coste'].sum(), s['pnl'].sum(), e, lo, hi, porday(s)))
e, lo, hi = ev_ic(F); P('  TOTAL rellenos %d coste %.2f pnl %+.2f EV %+.3f [%+.3f,%+.3f]' % (len(F), F['coste'].sum(), F['pnl'].sum(), e, lo, hi))
P('  ESTRICTO marca NO-relleno a %d de %d rellenos reales (%.1f %%); de ellos B solo-toque %d, C solo-propio %d, D sin print %d' % (
    (F['cat'] != 'A').sum(), len(F), 100 * (F['cat'] != 'A').mean(), (F['cat'] == 'B').sum(), (F['cat'] == 'C').sum(), (F['cat'] == 'D').sum()))
s = F[F['cat'] != 'A']; e, lo, hi = ev_ic(s); P('  EV de los descartados por el estricto: %+.3f [%+.3f,%+.3f] coste %.2f' % (e, lo, hi, s['coste'].sum()))
for e_ in (0, 1000):
    cc = cat(F['Vt%d' % e_], F['Va%d' % e_], F['own_casado']); P('  sensibilidad e=%d ms: A %d B %d C %d D %d' % (e_, *(int((cc == k).sum()) for k in 'ABCD')))
# puja
Pj = R.groupby('puja').agg(dia=('dia', 'first'), fill=('fill', 'max'), pnl=('pnl', 'sum'), coste=('coste', 'sum'), catf=('cat', lambda x: min(x)))
Pf = Pj[Pj['fill'] == 1]
P('  por PUJA (mercado,lado; categoria = mejor de sus ordenes): rellenas %d de %d' % (len(Pf), len(Pj)))
for c in 'ABCD':
    s = Pf[Pf['catf'] == c].reset_index();
    if len(s): e, lo, hi = ev_ic(s); P('    %s pujas %3d (%.1f %%) coste %.2f EV %+.3f [%+.3f,%+.3f]' % (c, len(s), 100 * len(s) / len(Pf), s['coste'].sum(), e, lo, hi))
# ---------------- modelo
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, brier_score_loss
def feats(df, vt, va):
    return np.column_stack([np.log1p(df[vt]), np.log1p(df[va]), np.log1p(df['cola']), ((df[vt] + df[va]) >= df['cola'] + 0.5 * df['size']).astype(float),
                            np.log(df['vida'] + 1), df['off']])
COLS = ['lVt', 'lVa', 'lQ', 'fifo', 'lvida', 'off']
tr = R['dia'].isin(['2026-10-20', '2026-10-21']).values; te = ~tr; y = R['fill'].values
pd.DataFrame(np.column_stack([feats(R, 'Vt250', 'Va250'), y]), columns=COLS + ['fill']).to_csv(OUT + 'feats_r11.csv', index=False)
def fit_eval(vt, va, nombre):
    X = feats(R, vt, va); sc = StandardScaler().fit(X[tr]); m = LogisticRegression(C=1.0, max_iter=2000).fit(sc.transform(X[tr]), y[tr])
    ph = m.predict_proba(sc.transform(X))[:, 1]; base = y[tr].mean()
    b = brier_score_loss(y[te], ph[te]); b0 = brier_score_loss(y[te], np.full(te.sum(), base))
    P('  %-22s TEST AUC %.3f Brier %.4f (base %.4f, skill %+.3f) P media virtual %.4f real %.4f (ratio %.2f) | coef %s' % (
        nombre, roc_auc_score(y[te], ph[te]), b, b0, 1 - b / b0, ph[te].mean(), y[te].mean(), ph[te].mean() / y[te].mean(),
        ' '.join('%s%+.2f' % (c, w) for c, w in zip(COLS, m.coef_[0]))))
    return ph, m, sc
P('\n== (2) Modelo de relleno (logit, TUNE 20-21 -> TEST 22-23; n TUNE %d/%d rellenos, TEST %d/%d)' % (tr.sum(), y[tr].sum(), te.sum(), y[te].sum()))
ph, mod, sc = fit_eval('Vt250', 'Va250', 'M_excl (sin propios)')
ph_pl, _, _ = fit_eval('Vt_pl', 'Va_pl', 'PLACEBO +90 s')
ph_in, _, _ = fit_eval('Vt_incl', 'Va_incl', 'M_incl (circular)')
q = pd.qcut(ph[te], 10, duplicates='drop'); cal = pd.DataFrame({'p': ph[te], 'y': y[te], 'q': q}).groupby('q', observed=True).agg(n=('y', 'size'), pv=('p', 'mean'), yr=('y', 'mean'))
P('  calibracion M_excl TEST por deciles (n, P virtual, real):'); P('   ' + ' | '.join('%d %.3f/%.3f' % (r.n, r.pv, r.yr) for r in cal.itertuples()))
for nombre, rule in (('ESTRICTO', R['Vt250'] > 0), ('TOQUE', (R['Vt250'] + R['Va250']) > 0), ('FIFO', (R['Vt250'] + R['Va250']) >= R['cola'] + 0.5 * R['size']), ('CAPA1-v2 (con propios)', R['capa1_incl'] > 0)):
    r_ = rule.values.astype(int); tp = (r_[te] & y[te]).sum()
    P('  regla %-22s TEST P virtual %.4f real %.4f recall %.2f precision %.2f' % (nombre, r_[te].mean(), y[te].mean(), tp / max(1, y[te].sum()), tp / max(1, r_[te].sum())))
# ---------------- (3) brecha
P('\n== (3) Politica vigente de B re-simulada sobre sus ordenes reales (TEST 22-23 y TOTAL); EV por EUR, coste virtual = P*size*p')
for nm, msk in (('TEST', te), ('TUNE', tr), ('TOTAL', np.ones(len(R), bool))):
    d = R[msk]; pr = ph[msk]; win = d['gana'].values - d['p'].values
    ev_real = d['pnl'].sum() / d['coste'].sum()
    st = (d['Vt250'] > 0).values; ev_st = (st * d['size'] * win).sum() / max((st * d['size'] * d['p']).sum(), 1e-9)
    to = ((d['Vt250'] + d['Va250']) > 0).values; ev_to = (to * d['size'] * win).sum() / max((to * d['size'] * d['p']).sum(), 1e-9)
    ev_m = (pr * d['size'] * win).sum() / (pr * d['size'] * d['p']).sum()
    pi = ph_in[msk]; ev_mi = (pi * d['size'] * win).sum() / (pi * d['size'] * d['p']).sum()
    P('  %-5s real %+.3f (pnl %+.2f, coste %.2f) | ESTRICTO %+.3f (coste %.2f, pnl %+.2f) | TOQUE %+.3f | M_excl %+.3f (coste %.2f pnl %+.2f) | M_incl %+.3f | brecha cerrada por M_excl %.0f %%, por TOQUE %.0f %%' % (
        nm, ev_real, d['pnl'].sum(), d['coste'].sum(), ev_st, (st * d['size'] * d['p']).sum(), (st * d['size'] * win).sum(), ev_to, ev_m, (pr * d['size'] * d['p']).sum(), (pr * d['size'] * win).sum(), ev_mi,
        100 * (ev_m - ev_st) / (ev_real - ev_st) if abs(ev_real - ev_st) > 1e-9 else np.nan, 100 * (ev_to - ev_st) / (ev_real - ev_st) if abs(ev_real - ev_st) > 1e-9 else np.nan))
P('\n== EV REAL por posicion de cola (cola = acciones delante en nuestro nivel al postear, REST ~100 ms antes)')
R['qb'] = pd.cut(R['cola'], [-0.1, 10, 40, 100, 1e9], labels=['0-10', '10-40', '40-100', '>=100'])
R['frac'] = (R['Vt250'] + R['Va250']) / (R['cola'] + R['size'])
for qb, d in R.groupby('qb', observed=True):
    f = d[d['fill'] == 1]; e, lo, hi = ev_ic(f) if len(f) else (np.nan,) * 3
    P('  cola %-6s ordenes %4d rellenos %3d P %.3f | coste %6.2f pnl %+7.2f EV %+.3f [%+.3f,%+.3f] | cat A/B/C/D %s | por dia %s' % (
        qb, len(d), len(f), len(f) / len(d), f['coste'].sum(), f['pnl'].sum(), e, lo, hi, '/'.join(str(int((f['cat'] == k).sum())) for k in 'ABCD'), porday(f) if len(f) else ''))
for c in 'ABC':
    for qb, d in F[F['cat'] == c].groupby(pd.cut(F[F['cat'] == c]['cola'], [-0.1, 10, 40, 1e9], labels=['0-10', '10-40', '>=40']), observed=True):
        if len(d): e, lo, hi = ev_ic(d); P('    cat %s cola %-5s n %3d coste %6.2f EV %+.3f [%+.3f,%+.3f]' % (c, qb, len(d), d['coste'].sum(), e, lo, hi))
open(OUT + 'salida_r11.txt', 'w').write('\n'.join(L) + '\n')
