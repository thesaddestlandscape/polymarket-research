import sys, os, json, io, contextlib, numpy as np
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r7_28oct')
import r7a
from r7a import *
r7a.XS = (100,); r7a.MS = (3,); r7a.LATS = (-26.0, 68.0)
G = json.load(open(r4.I.CACHE)); days0 = sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_'))
with contextlib.redirect_stdout(io.StringIO()): days = r5f.inclusion(days0)
nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
IS, OOS, DEV = dd(6, 15), dd(16, 25), dd(26, 27)
rows = []
for di, d in enumerate(days):
    E, PL = r7a.day_events(d, di, G); rows += E.get((100, 3), []); del E, PL
P('== R7 A2: mecanismo VELOCIDAD de la continuacion (X=100, m=3; "pre-posicionada" = orden ya en el libro al armar, sin latencia; "reactiva" = GTC 68 ms)')
di = np.array([r['di'] for r in rows]); y = np.array([r['y'] for r in rows]); tg = np.array([r['tgt'] for r in rows]); td = np.array([r['tk'] + 5.0 for r in rows])
tf0 = np.array([r['tf-26'] for r in rows]); dt = tf0 - td; f0 = np.isfinite(tf0); f68 = np.array([r['j68'] >= 0 for r in rows])
adv = np.array([r['f'][14] for r in rows]); cumv = np.array([r['f'][0] for r in rows])
R = dict(di=di, num=NACC * (y - tg), den=NACC * tg)
bins = [(0, 94), (94, 500), (500, 2000), (2000, 12000)]
for lb, m0 in (('TODAS las pre-posicionadas', f0),) + tuple(('dt [%d,%d) ms' % b, f0 & (dt >= b[0]) & (dt < b[1])) for b in bins):
    for pn, ds in (('IS', IS), ('OOS 16-25', OOS), ('DEV', DEV)):
        s = summ(R, m0 & np.isin(di, ds), ds, nd); P('  pre-posicionada %-26s %-9s %s | fills/d %.0f' % (lb, pn, F(s), (m0 & np.isin(di, ds)).sum() / len(ds)))
for pn, ds in (('IS', IS), ('OOS 16-25', OOS)):
    P('  reactiva (68 ms) %-9s %s' % (pn, F(summ(R, f68 & np.isin(di, ds), ds, nd))))
    P('  pre-posicionada que la reactiva PIERDE (dt<94 ms) y salto adverso previo <2 s: %s | sin salto: %s' % (F(summ(R, f0 & (dt < 94) & (adv < 2000) & np.isin(di, ds), ds, nd)), F(summ(R, f0 & (dt < 94) & (adv >= 2000) & np.isin(di, ds), ds, nd))))
# cuota de tamano: por tamano acumulado en el armado
for lb, m0 in (('cum<200', cumv < 200), ('200-400', (cumv >= 200) & (cumv < 400)), ('>=400', cumv >= 400)):
    P('  pre-posicionada dt<94 ms %-8s OOS: %s' % (lb, F(summ(R, f0 & (dt < 94) & m0 & np.isin(di, OOS), OOS, nd))))
del rows
P('\n== R7 D: dosis-respuesta continua (rellenos de todos los makers, BTC, estado S800)')
R = load6(days, 0); S = np.isfinite(R['dA']); r_i = (R['y'] - R['p']) / R['p']; w = R['den']
xs = np.log(np.where(S, R['sA'], 800.0) / 800.0); inw = (R['swsz'] >= 200).astype(float)
def wls(m, idx=None):
    mm = np.flatnonzero(m) if idx is None else idx; Xm = np.vstack([np.ones(len(mm)), xs[mm], inw[mm]]).T; W = w[mm]
    return np.linalg.solve((Xm * W[:, None]).T @ Xm, (Xm * W[:, None]).T @ r_i[mm])
for nm_, ds in (('IS 06-15', IS), ('OOS 16-25', OOS), ('DEV 26-27', DEV)):
    m = S & np.isin(R['di'], ds); b = wls(m); bs = []
    byday = {dd_: np.flatnonzero(S & (R['di'] == dd_)) for dd_ in ds}
    for _ in range(200):
        pick = rng.choice(ds, len(ds)); mm = np.concatenate([byday[x] for x in pick])
        try: bs.append(wls(None, mm)[1])
        except Exception: pass
    P('  WLS EV/E ~ a + b*log(tam barrido/800) + c*dentro_barrido, %s: a %+.3f b %+.3f IC90 dias [%+.3f,%+.3f] c %+.3f (n=%d)' % (nm_, b[0], b[1], *np.percentile(bs, [5, 95]), b[2], m.sum()))
    if nm_.startswith('IS'): bIS = b
OOS2 = dd(16, 27); mi = S & np.isin(R['di'], OOS2); pred = bIS[0] + bIS[1] * xs[mi] + bIS[2] * inw[mi]; mis = S & np.isin(R['di'], IS)
ss_res = (w[mi] * (r_i[mi] - pred) ** 2).sum(); ss_c = (w[mi] * (r_i[mi] - np.average(r_i[mis], weights=w[mis])) ** 2).sum()
P('  R2 OOS ponderado frente a media IS: %.4f' % (1 - ss_res / ss_c))
edges = [800, 1000, 1400, 2000, 3000, 5000, 1e9]
for ctx, cm in (('dentro de barrido', R['swsz'] >= 200), ('post-barrido', R['swsz'] < 200)):
    for k in range(len(edges) - 1):
        mk_ = S & cm & (R['sA'] >= edges[k]) & (R['sA'] < edges[k + 1]); o = []
        for pn, ds in (('IS', IS), ('OOS', OOS2)):
            s = summ(R, mk_, ds, nd); o.append('%s %s' % (pn, ('EVw %+.3f [%+.3f,%+.3f] +%d/%d %.0fEUR/d' % (s['pool'], s['lo'], s['hi'], s['pos'], s['nd'], s['eurd'])) if s else '-'))
        P('  %-18s tam [%d,%s): %s' % (ctx, edges[k], ('%d' % edges[k + 1]) if edges[k + 1] < 1e8 else 'inf', ' | '.join(o)))
# pieza nueva: retardo desde el barrido (continuo) en post-barrido
for lb, lo_, hi_ in (('5-10 s', 5000, 10000), ('10-20', 10000, 20000), ('20-40', 20000, 40000), ('40-60', 40000, 60001)):
    mk_ = S & (R['swsz'] < 200) & (R['dA'] >= lo_) & (R['dA'] < hi_); P('  post-barrido retardo %-7s IS %s | OOS+DEV %s' % (lb, F(summ(R, mk_, IS, nd)), F(summ(R, mk_, OOS2, nd))))
open(BASE + 'salida_r7d.txt', 'w').write('\n'.join(r6a.LINES))
