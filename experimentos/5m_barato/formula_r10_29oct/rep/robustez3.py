#!/usr/bin/env python3
"""Robustez R10 parte 3 (29-Oct): regla sin modelo (surrogate d3 fijado en IS) + margen bid15-bb + regimenes + precio m + placebo bid15 barajado. OOS solo se reporta."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
exec(open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/robustez.py').read().split("VAR = {")[0])
col = lambda c: F_[:, COLS.index(c)]; T = (trem >= 200) & (trem < 286); bid15 = col('bid15'); bb = col('bb'); cbb = col('cbb')
def evm(mask, m, ds):
    vm = np.isfinite(tg[:, m]); keep = dedupe_m(vm & mask, m); f = fl[:, m] & keep
    ii = np.flatnonzero(f); o = ii[np.argsort(tf[ii, m], kind='stable')]; k = np.stack([di[o], u[o]], 1); _, first = np.unique(k, axis=0, return_index=True); out = np.zeros(len(f), bool); out[o[first]] = True
    num = np.where(out, N * (y - tg[:, m]), 0.0); den = np.where(out, N * tg[:, m], 0.0); dn = np.bincount(di, weights=num, minlength=nd); dd = np.bincount(di, weights=den, minlength=nd); sel = [i for i in ds if dd[i] > 0]
    if len(sel) < 2: return None, keep
    ev = dn[sel] / dd[sel]; mm, lo, hi = r4.tci(ev); fm = out & np.isin(di, ds)
    return dict(n=int(fm.sum()), nd=len(sel), evw=float(dn[sel].sum() / dd[sel].sum()), lo=lo, hi=hi, pos=int((ev > 0).sum()), s2=float(np.sort(ev)[:-2].mean()) if len(ev) > 3 else float('nan'), eurd=float(np.mean(dn[ds])), fill=float(fm.sum() / max(1, (keep & np.isin(di, ds)).sum()))), keep
def dedupe_m(sel, m): return dedupe(sel)
def rep(mask, name, m=2):
    a, _ = evm(mask, m, IS); b, _ = evm(mask, m, OO); P('  %-46s IS %s fill%.0f%% || OOS %s fill%.0f%%' % (name, fmt(a), 100 * (a or {}).get('fill', 0), fmt(b), 100 * (b or {}).get('fill', 0)))
rows = isI & v3 & T; Q = lambda x, q: float(np.nanquantile(x[rows], q))
S3 = np.zeros(len(di), bool); S3 = T & (((bid15 > 0.51) & (bb > 0.23)) | ((bid15 > 0.51) & (bb <= 0.23) & (trem > 240)) | ((bid15 <= 0.51) & (cbb > 0.66) & (bb > 0.28)))
P('== D) regla S3 (arbol d3 entrenado en IS sobre la seleccion HGB; sin modelo en uso) T200-286, m=3 (bb-3c)'); rep(S3, 'S3'); rep(T & ~S3, 'complemento T200-286 & ~S3'); rep(T, 'SIEMPRE T200-286')
P('   por m (bb-1c, -2c, -3c):')
for m in (0, 1, 2): rep(S3, '  S3 m=%d (bb-%dc)' % (m + 1, m + 1), m)
mg = bid15 - bb; cm = [Q(mg, q) for q in (.25, .5, .75)]; P('== E) margen = bid15 - bb (cortes IS Q25/Q50/Q75 en T200-286: %.3f/%.3f/%.3f)' % tuple(cm))
with np.errstate(invalid='ignore'):
    for nm, mk in (('margen<Q25', mg < cm[0]), ('Q25-Q50', (mg >= cm[0]) & (mg < cm[1])), ('Q50-Q75', (mg >= cm[1]) & (mg < cm[2])), ('margen>=Q75', mg >= cm[2]), ('margen>=0 (bid15>=bb)', mg >= 0), ('margen>=0.10', mg >= 0.10), ('margen>=0.20', mg >= 0.20)): rep(T & mk, nm)
    P('-- regimenes de la regla S3: por banda bb / T_rem / lado complementario')
    for nm, mk in (('bb<0.15', bb < 0.15), ('bb 0.15-0.22', (bb >= 0.15) & (bb < 0.22)), ('bb 0.22-0.29', (bb >= 0.22) & (bb < 0.29)), ('bb>=0.29', bb >= 0.29)): rep(S3 & mk, 'S3 & ' + nm)
    for lo_, hi_ in ((200, 220), (220, 240), (240, 260), (260, 286)): rep(S3 & (trem >= lo_) & (trem < hi_), 'S3 & T%d-%d' % (lo_, hi_))
    for nm, mk in (('bid15>0.51', bid15 > 0.51), ('bid15<=0.51 (rama cbb>0.66)', bid15 <= 0.51)): rep(S3 & mk, 'S3 & ' + nm)
    for nm, mk in (('acc60 Q1', col('acc60') <= Q(col('acc60'), .25)), ('acc60 Q2-3', (col('acc60') > Q(col('acc60'), .25)) & (col('acc60') <= Q(col('acc60'), .75))), ('acc60 Q4', col('acc60') > Q(col('acc60'), .75))): rep(S3 & mk, 'S3 & ' + nm)
    # S3 solo con HGB-bajo y sin
    pass
P('== F) placebo: bid15 barajado dentro de cada dia (misma regla S3 con cortes fijos) x5')
rng = np.random.default_rng(3); ev_p = []
for r in range(5):
    b2 = bid15.copy()
    for d in range(nd):
        w = np.flatnonzero(di == d); b2[w] = bid15[w][rng.permutation(len(w))]
    S3p = T & (((b2 > 0.51) & (bb > 0.23)) | ((b2 > 0.51) & (bb <= 0.23) & (trem > 240)) | ((b2 <= 0.51) & (cbb > 0.66) & (bb > 0.28))); a, _ = evm(S3p, 2, IS); b, _ = evm(S3p, 2, OO); ev_p.append((a['evw'], b['evw'])); 
P('   EVw placebo IS/OOS: ' + ' '.join('%+.3f/%+.3f' % e for e in ev_p))
open('/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep/salida_robustez3.txt', 'w').write('\n'.join(L))
