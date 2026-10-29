#!/usr/bin/env python3
"""test_nan_predice_y: para cada rasgo de un dataset, ¿'es NaN' predice la etiqueta y? (detector de fuga por AUSENCIA: rasgo = NaN porque no hay datos en TODA la ventana, incluido el futuro).
Uso: test_nan_predice_y.py FICHERO.npz [--F F --cols cols --y y --day di --tok u --strat bb --umbral 0.10 --nmin 200]
     (npz con matriz F[n,k], nombres cols, etiqueta y, y opcional claves de dia/token) o FICHERO.csv (columnas = rasgos, --y NOMBRE).
Salida: por rasgo: tasa NaN, y|NaN, y|finito, diferencia, corr punto-biserial, version a nivel TOKEN (1 fila por token: NaN en alguna fila), consistencia por dias (n dias con signo igual) y, si --strat, diferencia dentro de cortes del estratificador (descarta confusion).
Veredicto FUGA_PROBABLE si |dif|>=umbral con n_nan>=nmin y mismo signo en >=80% de los dias; SATURADO si y|NaN<=0.02 o >=0.98. Codigo de salida 1 si hay FUGA_PROBABLE (reutilizable como puerta: un rasgo con 'sin dato' no puede decidir el resultado)."""
import sys, argparse, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument('f'); ap.add_argument('--F', default='F'); ap.add_argument('--cols', default='cols'); ap.add_argument('--y', default='y')
ap.add_argument('--day', default='di'); ap.add_argument('--tok', default='u'); ap.add_argument('--strat', default=None); ap.add_argument('--umbral', type=float, default=0.10); ap.add_argument('--nmin', type=int, default=200)
ap.add_argument('--filas', default=None, help='expresion numpy opcional sobre columnas (p.ej. "(trem>=200)&(trem<286)")'); a = ap.parse_args()
if a.f.endswith('.npz'):
    Z = np.load(a.f, allow_pickle=True); F = Z[a.F].astype(float); cols = [str(c) for c in Z[a.cols]]; y = Z[a.y].astype(float)
    di = Z[a.day] if a.day in Z.files else np.zeros(len(y), int); tk = Z[a.tok] if a.tok in Z.files else np.arange(len(y))
else:
    import csv; R = list(csv.DictReader(open(a.f))); cols = [c for c in R[0] if c != a.y]; y = np.array([float(r[a.y]) for r in R])
    F = np.array([[float(r[c]) if r[c] not in ('', 'nan', 'NaN', 'None') else np.nan for c in cols] for r in R]); di = np.zeros(len(y), int); tk = np.arange(len(y))
cl = {c: F[:, i] for i, c in enumerate(cols)}; m = np.ones(len(y), bool)
if a.filas: m = eval(a.filas, {'np': np}, cl)
print('%s: filas %d (seleccion %d), rasgos %d, y medio %.4f' % (a.f, len(y), m.sum(), len(cols), y[m].mean())); bad = 0
print('%-12s %7s %8s %8s %8s %7s | %-24s | dias(+/n) | estrato' % ('rasgo', 'nan%', 'y|NaN', 'y|fin', 'dif', 'corr', 'nivel token (nan/fin)'))
tkey = di.astype(np.int64) * 10_000_000 + tk.astype(np.int64)
for c in cols:
    v = cl[c]; nn = np.isnan(v) & m; fn = np.isfinite(v) & m
    if nn.sum() == 0 or fn.sum() == 0: print('%-12s %7.2f  (sin NaN o todo NaN)' % (c, 100 * nn.sum() / max(1, m.sum()))); continue
    d = y[nn].mean() - y[fn].mean(); r = np.corrcoef(np.isnan(v[m]).astype(float), y[m])[0, 1] if np.isnan(v[m]).std() > 0 else np.nan
    # nivel token: token con alguna fila NaN
    k = tkey[m]; uk, inv = np.unique(k, return_inverse=True); anyn = np.bincount(inv, weights=np.isnan(v[m]).astype(float)) > 0; ytok = np.bincount(inv, weights=y[m]) / np.bincount(inv)
    tn = ytok[anyn].mean() if anyn.any() else np.nan; tf = ytok[~anyn].mean() if (~anyn).any() else np.nan
    sg = []; 
    for dd in np.unique(di[m]):
        s = di == dd; x1 = nn & s; x0 = fn & s
        if x1.sum() >= 30 and x0.sum() >= 30: sg.append(y[x1].mean() - y[x0].mean())
    sg = np.array(sg); same = int((np.sign(sg) == np.sign(d)).sum()) if len(sg) else 0
    est = ''
    if a.strat and a.strat in cl:
        s_ = cl[a.strat]; qs = np.nanquantile(s_[m], [0.25, 0.5, 0.75]); b = np.digitize(s_, qs); ds = []
        for q in range(4):
            x1 = nn & (b == q); x0 = fn & (b == q)
            if x1.sum() >= 30 and x0.sum() >= 30: ds.append(y[x1].mean() - y[x0].mean())
        est = 'dif/estrato ' + ' '.join('%+.2f' % x for x in ds)
    flag = ''
    if abs(d) >= a.umbral and nn.sum() >= a.nmin and len(sg) and same / len(sg) >= 0.8: flag = ' FUGA_PROBABLE'; bad += 1
    if nn.sum() >= a.nmin and (y[nn].mean() <= 0.02 or y[nn].mean() >= 0.98): flag += ' SATURADO'
    print('%-12s %7.2f %8.4f %8.4f %+8.4f %+7.3f | %.3f / %.3f (n%d/%d) | %d/%d%s%s' % (c, 100 * nn.sum() / m.sum(), y[nn].mean(), y[fn].mean(), d, r, tn, tf, anyn.sum(), (~anyn).sum(), same, len(sg), (' | ' + est) if est else '', flag))
print('\n== MODA (valor centinela: p.ej. 0 o 300000 = "sin datos" codificado explicito; mismo criterio, excluye NaN)')
for c in cols:
    v = cl[c]; fv = np.isfinite(v) & m
    if fv.sum() < a.nmin: continue
    vals, cnt = np.unique(np.round(v[fv], 6), return_counts=True); j = cnt.argmax(); sh = cnt[j] / fv.sum()
    if sh < 0.05 or len(vals) < 5: continue
    mo = fv & (np.round(v, 6) == vals[j]); ot = fv & ~mo; d = y[mo].mean() - y[ot].mean(); sg = []
    for dd in np.unique(di[m]):
        s_ = di == dd
        if (mo & s_).sum() >= 30 and (ot & s_).sum() >= 30: sg.append(y[mo & s_].mean() - y[ot & s_].mean())
    sg = np.array(sg); same = int((np.sign(sg) == np.sign(d)).sum()) if len(sg) else 0
    fl_ = ' FUGA_PROBABLE' if (abs(d) >= a.umbral and mo.sum() >= a.nmin and len(sg) and same / len(sg) >= 0.8) else ''
    print('%-12s moda %-10g %6.2f%% y|moda %.4f y|otros %.4f dif %+.4f dias %d/%d%s' % (c, vals[j], 100 * sh, y[mo].mean(), y[ot].mean(), d, same, len(sg), fl_)); bad += bool(fl_)
print('RESULTADO: %s' % ('%d rasgo(s) FUGA_PROBABLE' % bad if bad else 'ningun rasgo cumple el criterio de fuga')); sys.exit(1 if bad else 0)
