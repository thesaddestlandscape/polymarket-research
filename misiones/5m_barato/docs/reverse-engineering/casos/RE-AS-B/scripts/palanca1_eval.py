#!/usr/bin/env python3
"""palanca1_eval.py [dias...]  -- evalua PREREG_PALANCA1.md (sha256 en PREREG_PALANCA1.sha256). SOLO LECTURA. python3 -I.
Entrada: /root/polymarket-research-datalogs/palanca1/p1_<dia>.csv.gz (palanca1_extraer.py)."""
import sys, numpy as np, pandas as pd
DIAS = sys.argv[1:] or ['2026-10-24', '2026-10-25', '2026-10-26']
D = '/root/polymarket-research-datalogs/palanca1/'
X = pd.concat([pd.read_csv(D + 'p1_%s.csv.gz' % d) for d in DIAS], ignore_index=True)
ACC, FEE, AGE_MAX, T_MIN, R, SEED = 5.0, 0.07, 30000, 10.0, 2000, 2711
for c in ['ask_L', 'as_L', 'bid_L', 'bs_L', 'age_ms', 'gana_buy', 'b_m', 'Q0_m']: X[c] = pd.to_numeric(X[c], errors='coerce')
X['Tp'] = X.T_ev_s - X.L / 1000.0; X['unit'] = X.mk.astype(str) + '|' + X.lado_ev
print('filas', len(X), X.groupby(['dia', 'kind']).size().unstack().to_dict('index'))
X['ok0'] = X.gana_buy.notna() & (X.age_ms <= AGE_MAX) & (X.Tp >= T_MIN) & (X.ask_L > 0) & (X.ask_L < 1)
X['exec'] = X.ok0 & (X.as_L >= ACC)
fee = ACC * FEE * X.ask_L * (1 - X.ask_L)
X['t_cost'] = ACC * X.ask_L + fee; X['t_pnl'] = ACC * X.gana_buy - X.t_cost
X['m_ok'] = X.ok0 & (X.bid_L > 0) & (X.bid_L < 1)
X['m_fill'] = X.m_ok & (X.mk_pes == 1); X['m_cost'] = ACC * X.bid_L; X['m_pnl'] = ACC * (X.gana_buy - X.bid_L)
rng = np.random.default_rng(SEED)
def sums(q, pc, cc):
    g = q.groupby('cierre').agg(p=(pc, 'sum'), c=(cc, 'sum'), n=(pc, 'size'))
    r = (q[pc] / q[cc]).groupby(q.cierre).sum(); g['r'] = r; return g
def boot(g, fn):
    idx = np.arange(len(g)); P, C, Rr, N = g.p.values, g.c.values, g.r.values, g.n.values; v = []
    for _ in range(R):
        s = rng.choice(idx, len(idx)); v.append(fn(P[s], C[s], Rr[s], N[s]))
    return np.percentile(v, [5, 95])
evw = lambda P, C, Rr, N: P.sum() / C.sum(); evu = lambda P, C, Rr, N: Rr.sum() / N.sum()
def lin(nm, q, pc, cc):
    if len(q) == 0: print('  %-34s n=0' % nm); return None
    g = sums(q, pc, cc); a = q[pc].sum() / q[cc].sum(); u = (q[pc] / q[cc]).mean()
    i1 = boot(g, evw); i2 = boot(g, evu)
    print('  %-34s n=%4d cierres=%4d coste=%8.1f pnl=%+8.2f EVw=%+.4f IC90cierre(%+.3f,%+.3f) | EVu=%+.4f (%+.3f,%+.3f)' % (nm, len(q), q.cierre.nunique(), q[cc].sum(), q[pc].sum(), a, i1[0], i1[1], u, i2[0], i2[1]))
    return a
def dias(q, pc, cc, tag):
    out = {}
    for d, h in q.groupby('dia'): out[d] = (len(h), round(h[pc].sum() / h[cc].sum(), 4))
    print('    por dia %s: %s' % (tag, out)); return out
def sin2(q, pc, cc):
    byd = {d: h[pc].sum() / h[cc].sum() for d, h in q.groupby('dia')}
    if len(byd) <= 2: print('    sin 2 mejores dias: <=2 dias, NO calculable'); return
    best = sorted(byd, key=byd.get, reverse=True)[:2]; h = q[~q.dia.isin(best)]
    print('    sin 2 mejores dias (%s): n=%d EVw=%+.4f (queda %d dia)' % (best, len(h), h[pc].sum() / h[cc].sum(), h.dia.nunique()))
def sin_cierres(q, pc, cc):
    g = q.groupby('cierre').agg(p=(pc, 'sum'), c=(cc, 'sum')); top = g.p.sort_values(ascending=False).index[:2]
    h = g.drop(top); print('    [extra descriptivo] sin los 2 mejores CIERRES: EVw=%+.4f (n cierres %d)' % (h.p.sum() / h.c.sum(), len(h)))
def placebo(real, pl, pc, cc, tag):
    units = set(real.unit); P = pl[pl.unit.isin(units)]
    ev_real = real[pc].sum() / real[cc].sum(); evs = []
    cs = sorted(set(real.cierre) | set(P.cierre)); cidx = {c: i for i, c in enumerate(cs)}
    rp = np.zeros(len(cs)); rc = np.zeros(len(cs)); pm = np.zeros((10, len(cs))); pcm = np.zeros((10, len(cs)))
    for c, h in real.groupby('cierre'): rp[cidx[c]] = h[pc].sum(); rc[cidx[c]] = h[cc].sum()
    for j, h in P.groupby('draw'):
        evs.append(h[pc].sum() / h[cc].sum())
        for c, hh in h.groupby('cierre'): pm[j, cidx[c]] = hh[pc].sum(); pcm[j, cidx[c]] = hh[cc].sum()
    evs = np.array(evs); dif = ev_real - evs.mean()
    v = []
    for _ in range(R):
        s = rng.choice(len(cs), len(cs)); er = rp[s].sum() / rc[s].sum()
        ep = np.mean([pm[j, s].sum() / pcm[j, s].sum() for j in range(len(evs)) if pcm[j, s].sum() > 0]); v.append(er - ep)
    i = np.percentile(v, [5, 95])
    print('    PLACEBO %s: real EVw=%+.4f (n=%d) | placebo %d draws: media %+.4f p5 %+.4f p95 %+.4f (n medio %.0f) | percentil real %.0f%% | dif real-placebo %+.4f IC90cierre(%+.3f,%+.3f)'
          % (tag, ev_real, len(real), len(evs), evs.mean(), np.percentile(evs, 5), np.percentile(evs, 95), len(P) / max(len(evs), 1), (evs < ev_real).mean() * 100, dif, i[0], i[1]))
rl = X[X.kind == 'real']; pb = X[X.kind == 'placebo']
print('\n== COBERTURA (real; unidades = mercado-lado primer evento)')
for L in (100, 250, 500):
    r = rl[rl.L == L]
    print(' L=%d: eventos %d | sin gana %d | age>%d %d | Tp<%g s %d | ask invalido %d | ok0 %d | ejecutables taker (as>=5) %d | maker colocables %d, rellenos pes %d'
          % (L, len(r), r.gana_buy.isna().sum(), AGE_MAX, (r.age_ms > AGE_MAX).sum(), T_MIN, (r.Tp < T_MIN).sum(), (~((r.ask_L > 0) & (r.ask_L < 1))).sum(), r.ok0.sum(), r['exec'].sum(), r.m_ok.sum(), r.m_fill.sum()))
r = rl[(rl.L == 250) & rl.ok0]
print(' L=250: por dia (ok0):', r.groupby('dia').size().to_dict(), '| por moneda:', r.groupby('coin').size().to_dict())
print(' Tev (s) p10/p50/p90: %s | b_sw p50 %.2f | ask_prev->ask_L: sube en %.1f%%, igual %.1f%%, baja %.1f%%, mov medio %+.4f'
      % (np.percentile(r.T_ev_s, [10, 50, 90]).round(1), r.b_sw.median(), 100 * (r.ask_L > pd.to_numeric(r.ask_prev, errors='coerce')).mean(), 100 * (r.ask_L == pd.to_numeric(r.ask_prev, errors='coerce')).mean(),
         100 * (r.ask_L < pd.to_numeric(r.ask_prev, errors='coerce')).mean(), (r.ask_L - pd.to_numeric(r.ask_prev, errors='coerce')).mean()))
print(' orden de recepcion: edad del estado (ms) p50/p90/max: %s' % np.percentile(r.age_ms, [50, 90, 100]).round(0))
print('\n== TAKER (comprar el complementario al ask nivel 1, 5 acc, fee 0,07*p*(1-p)); PRIMARIA = L=250')
for L in (250, 100, 500):
    q = rl[(rl.L == L) & rl['exec']]; tag = 'PRIMARIA' if L == 250 else 'secundaria'
    print(' -- L=%d (%s)' % (L, tag)); lin('todos los dias', q, 't_pnl', 't_cost'); dias(q, 't_pnl', 't_cost', 'L=%d' % L); sin2(q, 't_pnl', 't_cost'); sin_cierres(q, 't_pnl', 't_cost')
    q26 = q[q.dia == '2026-10-26']; q2425 = q[q.dia != '2026-10-26']
    lin('24+25 (in-sample)', q2425, 't_pnl', 't_cost'); lin('26 (fuera de muestra)', q26, 't_pnl', 't_cost')
    pl = pb[(pb.L == L) & pb['exec']]; placebo(q, pl, 't_pnl', 't_cost', 'L=%d' % L)
    if L == 250:
        for cn, h in q.groupby('coin'): lin('[desc.] moneda ' + cn, h, 't_pnl', 't_cost')
        # cota NO ejecutable: comprar al ask previo (antes de moverse)
        ap = pd.to_numeric(q.ask_prev, errors='coerce'); h = q[ap.notna() & (ap > 0) & (ap < 1)].copy(); ap = ap[h.index]
        cst = ACC * ap + ACC * FEE * ap * (1 - ap); h['u_cost'] = cst; h['u_pnl'] = ACC * h.gana_buy - cst
        lin('[cota NO ejecutable] al ask previo', h, 'u_pnl', 'u_cost')
print('\n== MAKER (puja virtual 5 acc al mejor bid del complementario en t_sw+L; relleno pes; sin fee ni rebate; solo rellenos)')
for L in (250, 100, 500):
    q = rl[(rl.L == L) & rl.m_fill]; tag = 'maker-principal' if L == 250 else 'secundaria'
    print(' -- L=%d (%s): colocables %d, rellenos pes %d (%.1f%%), opt %d' % (L, tag, rl[(rl.L == L) & rl.m_ok].shape[0], len(q), 100 * len(q) / max(1, rl[(rl.L == L) & rl.m_ok].shape[0]), rl[(rl.L == L) & rl.m_ok & (rl.mk_opt == 1)].shape[0]))
    lin('rellenos pes', q, 'm_pnl', 'm_cost'); dias(q, 'm_pnl', 'm_cost', 'L=%d' % L); sin2(q, 'm_pnl', 'm_cost')
    q26 = q[q.dia == '2026-10-26']; lin('26 (fuera de muestra)', q26, 'm_pnl', 'm_cost')
    placebo(q, pb[(pb.L == L) & pb.m_fill], 'm_pnl', 'm_cost', 'L=%d' % L)
print('\nFIN')
