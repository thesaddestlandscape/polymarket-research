#!/usr/bin/env python3
"""forward_r1.py -- forward pasivo de R1 (E1D, cancelacion ms) REPARADO tras el red-team 24/26-Oct. Solo lectura, sin dinero real.
Lee las caches del extractor unico de ../forward/forward_a1.py (prints_D.pkl = rellenos de bid poblacionales, ventanas_D.pkl = R1 por mercado) -> no relee m5_registro.
Regla (PREREG_FWD_R1.md, sha en PREREG_FWD_R1.sha256): saltar la ventana (moneda,mercado 5m) si R1 <= tercil 1/3 de R1 de su CELDA (moneda x bloque 4 h x laborable/fin de semana)
con todas las ventanas de dias anteriores (historico E1D 05-23 Oct + forward expansivo). INVERSION = saltar R1 > tercil 2/3. Salida forward_r1_diario.csv + RESUMEN.md."""
import os, sys, glob, json, hashlib, time, numpy as np, pandas as pd
from scipy import stats
AQ = os.path.dirname(os.path.abspath(__file__))
DL = os.environ.get('FWD_DL', '/root/polymarket-research-datalogs/mitigar_as_25oct/forward') + '/'; OUT = os.environ.get('FWD_OUT', AQ) + '/'
HIST = os.environ.get('FWD_HIST', '/root/polymarket-research-datalogs/e1_cancelacion_ms/e1d_dia_2026-10-*.pkl'); DESDE = os.environ.get('FWD_DESDE', '2026-10-24')
if not os.environ.get('FWD_NOCHECKPRE'):
    assert hashlib.sha256(open(AQ + '/PREREG_FWD_R1.md', 'rb').read()).hexdigest() == open(AQ + '/PREREG_FWD_R1.sha256').read().split()[0], 'prereg alterado'
PRIM = ('ETH', 'SOL', 'XRP'); MINCELDA = 60
def celda(W): 
    t0 = pd.to_datetime(W.fin.values - 300, unit='s', utc=True)
    return W.coin.astype(str) + '|' + (t0.hour // 4).astype(str) + '|' + np.where(t0.dayofweek < 5, 'lab', 'fds')
H = pd.concat([pd.read_pickle(f)[1][['coin', 'mid', 'fin', 'dia', 'R1']] for f in sorted(glob.glob(HIST))], ignore_index=True); H['gap_frac'] = np.nan
H = H[H.coin.isin(PRIM)]
dias = sorted(os.path.basename(f)[9:19] for f in glob.glob(DL + 'ventanas_2026-*.pkl') if os.path.basename(f)[9:19] >= DESDE)
dias = [d for d in dias if os.path.exists(DL + f'prints_{d}.pkl') and json.load(open(DL + f'manifest_{d}.json')).get('estado') == 'COMPLETE']
FW = {d: pd.read_pickle(DL + f'ventanas_{d}.pkl') for d in dias}; PR = {d: pd.read_pickle(DL + f'prints_{d}.pkl') for d in dias}
rows = []; cier = []; rng = np.random.default_rng(20261026)
for d in dias:
    prev = pd.concat([H] + [FW[x] for x in dias if x < d], ignore_index=True); prev = prev[np.isfinite(prev.R1)]; prev['celda'] = celda(prev)
    te = FW[d][FW[d].coin.isin(PRIM)].copy(); te['celda'] = celda(te)
    cuts = {c: np.quantile(g.R1.values, [1/3, 2/3]) for c, g in prev.groupby('celda') if len(g) >= MINCELDA}
    P = PR[d]; P = P[P.coin.isin(PRIM)]
    w = P.groupby(['coin', 'mid']).agg(pnl=('pnl', 'sum'), coste=('coste', 'sum')).reset_index()
    te = te.merge(w, on=['coin', 'mid'], how='left'); te[['pnl', 'coste']] = te[['pnl', 'coste']].fillna(0.0)
    c1 = te.celda.map(lambda c: cuts[c][0] if c in cuts else np.nan).values; c2 = te.celda.map(lambda c: cuts[c][1] if c in cuts else np.nan).values
    ok = np.isfinite(te.R1.values) & np.isfinite(c1)
    sk = ok & (te.R1.values <= c1); inv = ok & (te.R1.values > c2); gap = ok & (te.gap_frac.values <= 0.05)
    lab = pd.Timestamp(d).dayofweek < 5
    def metr(m, nombre, sub=None):
        t = te if sub is None else te[sub]; mm = m if sub is None else m[sub]; n = len(t)
        if n == 0: return dict(dia=d, variante=nombre)
        k = int(mm.sum()); tot = t.pnl.sum(); dP = -t.pnl.values[mm].sum(); exp_ = -(k / n) * tot; v = t.pnl.values
        sims = np.array([-v[rng.choice(n, k, replace=False)].sum() if k else 0.0 for _ in range(2000)]) - exp_
        return dict(dia=d, variante=nombre, laborable=int(lab), ventanas=n, saltadas=k, sin_corte=int((~ok).sum()), coste=t.coste.sum(), pnl_siempre=tot, dPnL=dP, exceso=dP - exp_, p_dia=float((sims >= dP - exp_).mean()),
                    pnl_sk=t.pnl.values[mm].sum(), coste_sk=t.coste.values[mm].sum(), ev_saltadas=(t.pnl.values[mm].sum() / t.coste.values[mm].sum()) if t.coste.values[mm].sum() > 0 else np.nan, ev_resto=(t.pnl.values[~mm].sum() / t.coste.values[~mm].sum()) if t.coste.values[~mm].sum() > 0 else np.nan)
    rows += [metr(sk, 'R1_celda'), metr(inv, 'inversion'), metr(sk, 'R1_sin_huecos', sub=gap)]
    for c in PRIM: rows.append(dict(metr(sk, 'R1_' + c, sub=(te.coin == c).values)))
    g = pd.DataFrame({'fin': te.fin.values, 'x': -np.where(sk, te.pnl.values, 0) + sk.mean() * te.pnl.values}).groupby('fin').x.sum()
    cier += [dict(dia=d, fin=float(a), x=float(b)) for a, b in g.items()]
T = pd.DataFrame(rows); T.to_csv(OUT + 'forward_r1_diario.csv', index=False, float_format='%.6g')
def ts(e):
    e = np.asarray(e, float); n = len(e)
    if n < 2: return dict(n=n, s=float(e.sum()), lo=np.nan, hi=np.nan, p=np.nan, pos=int((e > 0).sum()))
    se = e.std(ddof=1) / np.sqrt(n); h = stats.t.ppf(0.95, n - 1) * se
    return dict(n=n, s=float(e.sum()), lo=float(e.mean() - h), hi=float(e.mean() + h), p=float(1 - stats.t.cdf(e.mean() / se, n - 1)) if se > 0 else np.nan, pos=int((e > 0).sum()))
L = ['# RESUMEN forward R1 (E1D, reparado) -- ' + time.strftime('%FT%TZ', time.gmtime()), '', f'Pasivo, solo lectura, 0 EUR validados. Dias nuevos con extractor COMPLETE: **{len(dias)}** ({", ".join(dias) or "ninguno"}). Gate: >=10 dias (~03-Nov).', '']
if len(T):
    A = T[T.variante == 'R1_celda'].set_index('dia'); I = T[T.variante == 'inversion'].set_index('dia'); G = T[T.variante == 'R1_sin_huecos'].set_index('dia')
    L += ['| dia | lab | ventanas | saltadas | sin corte | pnl operar siempre | dPnL | exceso vs azar | p dia | EV saltadas | EV resto | inversion exceso |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    for d, r in A.iterrows(): L.append(f"| {d} | {r.laborable} | {r.ventanas} | {r.saltadas} | {r.sin_corte} | {r.pnl_siempre:.0f} | {r.dPnL:.0f} | {r.exceso:.0f} | {r.p_dia:.3f} | {r.ev_saltadas:.3f} | {r.ev_resto:.3f} | {I.loc[d].exceso:.0f} |")
    n = len(A); s = ts(A.exceso.values); d_ = A.dPnL
    Cc = pd.DataFrame(cier); bs = [rng.choice(Cc.groupby('fin').x.sum().values, len(Cc.groupby('fin')) ).sum() for _ in range(2000)]; lo_c = float(np.quantile(bs, .05))
    peor = A.pnl_siempre.idxmin(); mej = A.dPnL.idxmax(); top2 = A.exceso.sort_values().index[-2:]
    gate = {'1_exceso>0, p<0,05 (placebo por dias), IC90 cierre inferior>0': s['s'] > 0 and s['p'] < 0.05 and lo_c > 0,
            '2a_dPnL vs operar siempre>0': d_.sum() > 0, '2b_dPnL>0 sin el peor dia de operar-siempre (%s)' % peor: d_.drop(peor).sum() > 0 if n > 1 else False,
            '2c_dPnL>0 sin el mejor dia de dPnL (%s) [20-Oct equivalente]' % mej: d_.drop(mej).sum() > 0 if n > 1 else False, '2d_dPnL>0 sin los 2 mejores dias': d_.drop(d_.sort_values().index[-2:]).sum() > 0 if n > 2 else False,
            '2e_exceso>0 sin los 2 mejores dias': A.exceso.drop(top2).sum() > 0 if n > 2 else False, '2f_>=60% dias con exceso>0': (A.exceso > 0).mean() >= 0.6, '2g_inversion<0': I.exceso.sum() < 0,
            '3_sin ventanas con >5% huecos: exceso>0 y dPnL>0': G.exceso.sum() > 0 and G.dPnL.sum() > 0}
    for c in ('ETH', 'SOL'):
        R = T[T.variante == 'R1_' + c]; gate[f'4_{c}: EV saltadas < EV resto (coste ponderado)'] = bool(len(R) and R.coste_sk.sum() > 0 and (R.pnl_sk.sum() / R.coste_sk.sum()) < ((R.pnl_siempre.sum() - R.pnl_sk.sum()) / (R.coste.sum() - R.coste_sk.sum())))
    lab_ = A[A.laborable == 1]
    if len(lab_) >= 5: gate['5_solo laborables: exceso>0 y dPnL>0'] = lab_.exceso.sum() > 0 and lab_.dPnL.sum() > 0
    L += ['', f"Acumulado ({n} d): dPnL vs operar siempre **{d_.sum():.0f} $**; exceso vs azar {s['s']:.0f} $ (IC90 dias ({s['lo']:.0f},{s['hi']:.0f})/dia, p dias {s['p']:.4f}, IC90 cierre inferior {lo_c:.0f}); dias exceso>0: {s['pos']}/{n}; inversion {I.exceso.sum():.0f} $; peor dia operar-siempre {peor}; mejor dPnL {mej}.", '', '## Gate (PREREG_FWD_R1)']
    L += [f"- {k}: {'SI' if v else 'no'}" for k, v in gate.items()]
    L.append('**VEREDICTO: ' + (('PASA todo (PROMISING en poblacion; NO autoriza dinero real: exige n>=150 propios + /code-review + OK Javi)' if all(gate.values()) else 'NO PASA') if n >= 10 else f'EN CURSO {n}/10 dias (descriptivo, sin veredicto)') + '**')
    L += ['', '## Por moneda (acumulado)', '| moneda | saltadas/ventanas | dPnL | exceso | EV saltadas (pond. EUR) | EV resto (pond. EUR) |', '|---|---|---|---|---|---|']
    for c in PRIM:
        R = T[T.variante == 'R1_' + c]
        if len(R): L.append(f"| {c} | {int(R.saltadas.sum())}/{int(R.ventanas.sum())} | {R.dPnL.sum():.0f} | {R.exceso.sum():.0f} | {R.pnl_sk.sum() / max(R.coste_sk.sum(), 1e-9):.3f} | {(R.pnl_siempre.sum() - R.pnl_sk.sum()) / max(R.coste.sum() - R.coste_sk.sum(), 1e-9):.3f} |")
open(OUT + 'RESUMEN.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L[:6]))
