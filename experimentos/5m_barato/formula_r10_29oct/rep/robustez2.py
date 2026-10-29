#!/usr/bin/env python3
"""Robustez R10 parte 2 (29-Oct): regla interpretable (surrogate arbol entrenado SOLO en IS sobre la seleccion del HGB congelado) + cortes fijos IS + regimenes de libro. OOS solo se reporta."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
exec(open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez.py').read().split("VAR = {")[0])
from sklearn.tree import DecisionTreeClassifier, export_text
pk = pickle.loads(open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb').read()); M = pk['hgb']; thr = pk['thr']; print('thr frozen', thr)
def hgb(): return H(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
p = np.full(len(di), np.nan); p[idx] = oof; p[isO] = M.predict_proba(F_[isO])[:, 1]; thq = float(np.quantile(oof, 0.05)); P('q05 OOF IS (raw HGB p) %.5f' % thq)
rng = np.random.default_rng(5)
def run(mask, ds, name, tag=''):
    f = firstfill(fl[:, 2] & dedupe(v3 & mask)); return f, stats(f, ds)
def rep(mask, name):
    f = firstfill(fl[:, 2] & dedupe(v3 & mask)); P('  %-44s IS %s || OOS16-27 %s' % (name, fmt(stats(f, IS)), fmt(stats(f, OO)))); return f
def alea(mask_pop, mask_sel, name):
    # ALEATORIO: misma fraccion de ordenes que la regla dentro de la poblacion, por particion IS / OOS; 20 repeticiones, media del EVw
    pop = dedupe(v3 & mask_pop); res = {}
    for pn, ds in (('IS', IS), ('OOS', OO)):
        mp = np.isin(di, ds); fr = (dedupe(v3 & mask_sel) & mp).sum() / max(1, (pop & mp).sum()); ev = []
        for r in range(20):
            s_ = pop & mp & (rng.random(len(di)) < fr); f = firstfill(fl[:, 2] & s_); st = stats(f, ds); ev.append(st['evw'] if st else np.nan)
        res[pn] = (np.nanmean(ev), np.nanstd(ev))
    P('  ALEATORIO(%s) misma fraccion: IS EVw %+.3f sd %.3f | OOS %+.3f sd %.3f' % (name, *res['IS'], *res['OOS']))
T = (trem >= 200) & (trem < 286); low = p <= thq
P('== A) referencias (T200-286)'); fH = rep(low & T, 'HGB congelado bajo (q05 IS)'); fS = rep(T, 'SIEMPRE (bb-3c, todas)'); alea(T, low & T, 'HGB')
# ---- surrogate: arbol sobre la seleccion del HGB, solo IS, filas T200-286 con precio
CS = ['trem', 'acc1', 'acc5', 'acc30', 'acc60', 'np5', 'np30', 'np60', 'tsl200', 'tsl800', 'n800_60', 'coin_n60', 'bb', 'spr', 'bs', 'cbb', 'bid15', 'm15', 'dbb5', 'hour']
X = np.nan_to_num(F_[:, [COLS.index(c) for c in CS]], nan=-1.0); rows = isI & v3 & T
for dep in (3, 4):
    tr = DecisionTreeClassifier(max_depth=dep, min_samples_leaf=1500, class_weight='balanced', random_state=0).fit(X[rows], low[rows])
    pr = tr.predict(X); tp = (pr & low & rows).sum(); P('-- surrogate profundidad %d (IS, T200-286): precision %.2f recall %.2f vs seleccion HGB' % (dep, tp / max(1, (pr & rows).sum()), tp / max(1, (low & rows).sum())))
    if dep == 3: P(export_text(tr, feature_names=CS, max_depth=4)); 
    sr = (pr.astype(bool)) & T; rep(sr, 'surrogate d%d' % dep)
    if dep == 3: alea(T, sr, 'surrogate d3')
# ---- reglas con cortes fijos IS (cuartiles de las filas IS T200-286 con precio)
Q = lambda c, q: float(np.nanquantile(F_[rows, COLS.index(c)], q)); col = lambda c: F_[:, COLS.index(c)]
cuts = {c: (Q(c, .25), Q(c, .5), Q(c, .75)) for c in ('acc30', 'acc60', 'np60', 'spr', 'bid15', 'cbb', 'np5', 'bs', 'tsl200')}
P('== B) cortes IS (Q25/Q50/Q75 en filas IS T200-286): ' + '; '.join('%s %.3g/%.3g/%.3g' % (c, *v) for c, v in cuts.items()))
with np.errstate(invalid='ignore'):
    R1 = T & (col('acc60') <= cuts['acc60'][0]); R2 = R1 & (col('np60') >= cuts['np60'][1]); R3 = R2 & (col('spr') <= cuts['spr'][1]); R4 = R3 & (col('bid15') >= cuts['bid15'][1])
    R5 = T & (col('acc30') <= cuts['acc30'][0]) & (col('np60') >= cuts['np60'][1]); R6 = R5 & (col('cbb') <= cuts['cbb'][1])
for nm, m in (('acc60<=Q25', R1), ('+np60>=Q50', R2), ('+spr<=Q50', R3), ('+bid15>=Q50', R4), ('acc30<=Q25 & np60>=Q50', R5), ('  + cbb<=Q50', R6)):
    f = rep(m, nm); 
    if nm in ('+spr<=Q50', '+bid15>=Q50'): alea(T, m, nm)
    # solape con HGB
    P('      solape con seleccion HGB: %d de %d reglas ordenes, HGB %d' % ((m & low & v3).sum(), (m & v3).sum(), (low & T & v3).sum()))
# ---- regimenes: poblacion SIEMPRE y HGB-bajo
P('== C) regimenes de libro (cortes IS), SIEMPRE vs HGB-bajo dentro del regimen, T200-286')
REG = {}
with np.errstate(invalid='ignore'):
    REG['acc60 Q1 (muy tranquilo)'] = col('acc60') <= cuts['acc60'][0]; REG['acc60 Q2-Q3'] = (col('acc60') > cuts['acc60'][0]) & (col('acc60') <= cuts['acc60'][2]); REG['acc60 Q4 (agitado)'] = col('acc60') > cuts['acc60'][2]
    REG['spr<=Q50 (apretado)'] = col('spr') <= cuts['spr'][1]; REG['spr>Q50 (ancho)'] = col('spr') > cuts['spr'][1]
    REG['bid15>=Q75 (alto)'] = col('bid15') >= cuts['bid15'][2]; REG['bid15<Q75'] = col('bid15') < cuts['bid15'][2]; REG['bid15 NaN'] = ~np.isfinite(col('bid15'))
    REG['np60>=Q50 (activo)'] = col('np60') >= cuts['np60'][1]; REG['np60<Q50 (poco activo)'] = col('np60') < cuts['np60'][1]
    REG['tranquilo: acc60<=Q50 & spr<=Q50'] = (col('acc60') <= cuts['acc60'][1]) & (col('spr') <= cuts['spr'][1]); REG['tranquilo & bid15>=Q50'] = REG['tranquilo: acc60<=Q50 & spr<=Q50'] & (col('bid15') >= cuts['bid15'][1])
    REG['agitado y ancho: acc60>Q50 & spr>Q50'] = (col('acc60') > cuts['acc60'][1]) & (col('spr') > cuts['spr'][1])
for nm, rm in REG.items():
    P(' [%s]  fraccion de filas T200-286: %.2f' % (nm, (rm & T & v3).sum() / max(1, (T & v3).sum())))
    rep(T & rm, '   SIEMPRE'); rep(T & rm & low, '   HGB bajo')
open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/salida_robustez2.txt', 'w').write('\n'.join(L))
