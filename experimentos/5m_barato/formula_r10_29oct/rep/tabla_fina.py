#!/usr/bin/env python3
"""Tabla fina R10 (29-Oct): contabilidad corregida + T_rem x banda de precio, IS (06-15) vs OOS (16-27). Solo lectura de hz_BTC.npz y frozen_R10; escribe rep/salida_tabla_fina.txt"""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/rep')
from r8lib import *
import pickle, hashlib
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
R10 = BASE; N = 10.0; rng = np.random.default_rng(29)
Z = np.load(R10 + 'hz_BTC.npz', allow_pickle=True); days = list(Z['days']); nd = len(days); IS, OOS, DEV = part(days); OO = OOS + DEV
di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; F_ = Z['F'].astype(float); COLS = list(Z['cols']); tg = Z['tg']; fl = Z['fl']; tf = Z['tf']; yy = Z['Y10'].astype(int)
trem = F_[:, COLS.index('trem')]; isI = np.isin(di, IS); isO = ~isI
pk = open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb').read(); print('sha', hashlib.sha256(pk).hexdigest()[:12]); M = pickle.loads(pk); thr = M['thr']
def hgb(): return HistGradientBoostingClassifier(max_iter=200, learning_rate=0.07, max_depth=5, min_samples_leaf=100, random_state=1)
lg = lambda p: np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1)
idx = np.flatnonzero(isI); oof = np.zeros(len(idx))
for a, b in GroupKFold(5).split(idx, groups=di[idx]): oof[b] = hgb().fit(F_[idx[a]], yy[idx[a]]).predict_proba(F_[idx[b]])[:, 1]
score = np.full(len(di), np.nan); score[idx] = M['platt'].predict_proba(lg(oof))[:, 1]; score[isO] = M['platt'].predict_proba(lg(M['hgb'].predict_proba(F_[isO])[:, 1]))[:, 1]
thr2 = float(np.quantile(score[isI], 0.05)); print('thr frozen %.6f recomputed %.6f' % (thr, thr2)); assert abs(thr - thr2) < 1e-4
# mercado por (dia,token)
MK = {}
for i, d in enumerate(days): MK[i] = np.load(EXTD['BTC'] + 'b_%s.npz' % d)['tok_mk']
mkid = np.array([hash(str(MK[a][b])) for a, b in zip(di, u)])
def dedupe(sel):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def firstfill(f, key):
    """una observacion por clave: la orden rellenada mas temprana (por instante de relleno)"""
    ii = np.flatnonzero(f); o = ii[np.argsort(tf[ii, 2], kind='stable')]
    k = np.stack([di[o], key[o]], 1); _, first = np.unique(k, axis=0, return_index=True); out = np.zeros(len(f), bool); out[o[first]] = True; return out
def stats(f, ds, nds=None):
    num = np.where(f, N * (y - tg[:, 2]), 0.0); den = np.where(f, N * tg[:, 2], 0.0); dn = np.bincount(di, weights=num, minlength=nd); dd = np.bincount(di, weights=den, minlength=nd)
    nfl = np.bincount(di, weights=f.astype(float), minlength=nd)
    sel = [i for i in ds if dd[i] > 0]
    if not sel: return None
    ev = dn[sel] / dd[sel]; m, lo, hi = r4.tci(ev); pnl = dn[ds]; pm, plo, phi = r4.tci(pnl)
    fm = f & np.isin(di, ds); eu = float(np.mean((y[fm] - tg[fm, 2]) / tg[fm, 2]))
    return dict(n=int(fm.sum()), nd=len(sel), evw=float(dn[sel].sum() / dd[sel].sum()), evu=eu, lo=lo, hi=hi, pos=int((ev > 0).sum()), s2=float(np.sort(ev)[:-2].mean()) if len(ev) > 3 else float('nan'), eurd=float(pm), elo=plo, ehi=phi, cost=float(dd[ds].mean()))
def fmt(s):
    if s is None: return '-'
    return 'n%d d%d EVw%+.3f EVu%+.3f [%+.2f,%+.2f] +%d sin2%+.2f %+.2fE/d[%+.2f,%+.2f]' % (s['n'], s['nd'], s['evw'], s['evu'], s['lo'], s['hi'], s['pos'], s['s2'], s['eurd'], s['elo'], s['ehi'])
L = []
def P(s): print(s, flush=True); L.append(s)
v3 = np.isfinite(tg[:, 2]); low = score <= thr
# ---------- (1) contabilidad
kI = dedupe(v3 & low); fI = fl[:, 2] & kI
P('== (1) INCIDENCIA fill>100%: s["nf"]=mask.sum() cuenta rellenos de los 22 dias; nk=ordenes de la particion => ratio inflado (IS=22d/10d...). Bug de INFORME, no de EV. fill real por particion (r8T logit INV m3 T200-286 / HGB bajo todas T):')
nord = {n: int((kI & np.isin(di, ds)).sum()) for n, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV))}; nfi = {n: int((fI & np.isin(di, ds)).sum()) for n, ds in (('IS', IS), ('OOS', OOS), ('DEV', DEV))}
P('  HGB bajo: ordenes %s rellenos %s -> fill real %s' % (nord, nfi, {k: '%.0f%%' % (100 * nfi[k] / max(1, nord[k])) for k in nord}))
P('  ademas: varias ordenes (cada 10,3 s) por token pueden rellenarse varias veces en el mismo (dia,token) y en las dos patas del mercado (observaciones correlacionadas)')
for nm, f in (('A ordenes (orig)', fI), ('B 1/(dia,token)', firstfill(fI, u)), ('C 1/(dia,mercado)', firstfill(fI, mkid))):
    P('  INV HGB [%s] IS %s' % (nm, fmt(stats(f, IS)))); P('      OOS16-27 %s | OOS16-25 %s' % (fmt(stats(f, OO)), fmt(stats(f, OOS))))
    tb = f & (trem >= 200) & (trem < 286); P('      T200-286 IS %s' % fmt(stats(tb, IS))); P('                OOS16-27 %s | 16-25 %s' % (fmt(stats(tb, OO)), fmt(stats(tb, OOS))))
# comparadores T200-286 sin modelo, mismo conteo
tb_sel = v3 & (trem >= 200) & (trem < 286); kS = dedupe(tb_sel); fS = fl[:, 2] & kS
for nm, f in (('SIEMPRE T200-286 A', fS), ('SIEMPRE T200-286 B', firstfill(fS, u))): P('  %s IS %s' % (nm, fmt(stats(f, IS)))); P('      OOS16-27 %s' % fmt(stats(f, OO)))
# ---------- (2) tabla fina
EDG = list(range(120, 300, 20)); PB = [(0.09, 0.15), (0.15, 0.22), (0.22, 0.2901)]
def cell(pop, lo, hi, pl, ph):
    sel = v3 & (trem >= lo) & (trem < hi) & (tg[:, 2] >= pl - 1e-9) & (tg[:, 2] < ph)
    if pop == 'HGB': sel = sel & low
    k = dedupe(sel); return firstfill(fl[:, 2] & k, u)
P('\n== (2) TABLA FINA tramos 20 s (120-300; T_rem<=286) x precio de relleno. Contabilidad B (1 relleno por (dia,token)), orden cada 10,3 s dentro de la celda. EVw=ponderado por EUR, EVu=por relleno, IC90 por dias de EVw, +k=dias positivos, sin2=sin 2 mejores dias, E/d=pnl neto medio por dia de calendario.')
P('Regla de seleccion (solo IS 06-15): EV_IS>0, n_IS>=40, >=7/10 dias positivos. OOS solo se reporta.')
CAND = {}
for pop in ('HGB', 'SIN'):
    P('--- poblacion %s' % ('INVERSION HGB (score<=q05 IS)' if pop == 'HGB' else 'SIN modelo (todas las ordenes bb-3c en la celda)'))
    for lo in EDG:
        hi = lo + 20
        for (pl, ph) in [(0.09, 0.2901)] + PB:
            f = cell(pop, lo, hi, pl, ph); a = stats(f, IS); b = stats(f, OO)
            ok = a is not None and a['evw'] > 0 and a['n'] >= 40 and a['pos'] >= 7
            if ok: CAND[(pop, lo, hi, pl, ph)] = f
            if a is None and b is None: continue
            P('  %s T%d-%d p[%.2f,%.2f) IS %s || OOS %s %s' % (pop[:3], lo, hi, pl, ph, fmt(a), fmt(b), '<<CAND' if ok else ''))
# ---------- candidatos: comparadores y recuento
P('\n== candidatos IS (regla fijada): %d de %d celdas; con 4 sub-celdas x 9 tramos x 2 poblaciones = 72 celdas, a alfa 5%% se esperan ~3-4 falsos positivos' % (len(CAND), 72))
for (pop, lo, hi, pl, ph), f in CAND.items():
    b = stats(f, OO); 
    sel = v3 & (trem >= lo) & (trem < hi) & (tg[:, 2] >= pl - 1e-9) & (tg[:, 2] < ph); kS_ = dedupe(sel); fs = firstfill(fl[:, 2] & kS_, u)
    ra = firstfill(fl[:, 2] & dedupe(sel & (rng.random(len(di)) < max(0.05, (f.sum()) / max(1, fs.sum())))), u)
    sg = stats(fs, OO); rr = stats(ra, OO)
    P('  %s T%d-%d p[%.2f,%.2f): OOS %s\n      SIEMPRE-celda OOS %s\n      ALEAT.-celda  OOS %s' % (pop, lo, hi, pl, ph, fmt(b), fmt(sg), fmt(rr)))
# ---------- (3) reparto del pnl
P('\n== (3) REPARTO: pnl neto por tramo T_rem (HGB INV, contabilidad B), OOS16-27 y IS, EUR totales y % del pnl')
fB = firstfill(fI, u); num = np.where(fB, N * (y - tg[:, 2]), 0.0)
for ds, nm in ((IS, 'IS'), (OO, 'OOS16-27')):
    tot = num[np.isin(di, ds)].sum(); r = []
    for lo, hi in ((15, 120), (120, 200), (200, 286)): m = np.isin(di, ds) & (trem >= lo) & (trem < hi); r.append('T%d-%d %+.1fE (%.0f%%, n%d)' % (lo, hi, num[m].sum(), 100 * num[m].sum() / tot, (fB & m).sum()))
    P('  %s total %+.1fE: %s' % (nm, tot, ' | '.join(r)))
P('  Dentro de T200-286: HGB-bajo vs SIN-modelo (mismas T/precio) y regla trivial acc60 / bid15')
bs_ = (trem >= 200) & (trem < 286) & v3
for nm, extra in (('SIN modelo', np.ones(len(di), bool)), ('HGB bajo', low), ('acc60<=q25 IS banda', F_[:, COLS.index('acc60')] <= np.nanquantile(F_[isI & bs_, COLS.index('acc60')], 0.25)), ('acc60<=q50 IS banda', F_[:, COLS.index('acc60')] <= np.nanquantile(F_[isI & bs_, COLS.index('acc60')], 0.5)), ('bid15>=q50 IS banda', F_[:, COLS.index('bid15')] >= np.nanquantile(F_[isI & bs_, COLS.index('bid15')], 0.5)), ('bid15>=q75 IS banda', F_[:, COLS.index('bid15')] >= np.nanquantile(F_[isI & bs_, COLS.index('bid15')], 0.75)), ('tsl200>=q75 IS banda', F_[:, COLS.index('tsl200')] >= np.nanquantile(F_[isI & bs_, COLS.index('tsl200')], 0.75)), ('acc60<=q25 & HGB bajo', (F_[:, COLS.index('acc60')] <= np.nanquantile(F_[isI & bs_, COLS.index('acc60')], 0.25)) & low)):
    f = firstfill(fl[:, 2] & dedupe(bs_ & extra), u); P('  T200-286 %-24s IS %s\n      %-24s OOS16-27 %s' % (nm, fmt(stats(f, IS)), '', fmt(stats(f, OO))))
# diferencia pareada por dia HGB - SIN en banda
fh = firstfill(fl[:, 2] & dedupe(bs_ & low), u); fs_ = firstfill(fl[:, 2] & dedupe(bs_), u)
def dayev_(f): n = np.bincount(di, weights=np.where(f, N * (y - tg[:, 2]), 0.0), minlength=nd); d = np.bincount(di, weights=np.where(f, N * tg[:, 2], 0.0), minlength=nd); return n, d
nh, dh = dayev_(fh); ns, ds_ = dayev_(fs_)
for nm, ds in (('IS', IS), ('OOS16-27', OO)):
    s_ = [i for i in ds if dh[i] > 0 and ds_[i] > 0]; v = nh[s_] / dh[s_] - ns[s_] / ds_[s_]; m, lo, hi = r4.tci(v); P('  dEV (HGB bajo - SIN modelo) en T200-286 %s: %+.3f [%+.3f,%+.3f] +%d/%d dias' % (nm, m, lo, hi, (v > 0).sum(), len(s_)))


# ---------- (4) tramos candidatos UNION (una sola contabilidad B sobre la union) + comparadores sin modelo
P('\n== (4) UNIONES congelables (HGB bajo; relleno 1/(dia,token) sobre la union), IS y OOS16-27 + SIN modelo mismo tramo')
def U(lo, hi, pl=0.09, ph=0.2901, model=True):
    sel = v3 & (trem >= lo) & (trem < hi) & (tg[:, 2] >= pl - 1e-9) & (tg[:, 2] < ph)
    if model: sel = sel & low
    return firstfill(fl[:, 2] & dedupe(sel), u)
for nm, args in (('HGB T220-260', (220, 260, .09, .2901, True)), ('HGB T220-286', (220, 286, .09, .2901, True)), ('HGB T200-286', (200, 286, .09, .2901, True)), ('HGB T240-286', (240, 286, .09, .2901, True)), ('HGB T260-286', (260, 286, .09, .2901, True)), ('HGB T120-200', (120, 200, .09, .2901, True)), ('SIN T220-260', (220, 260, .09, .2901, False)), ('SIN T200-286', (200, 286, .09, .2901, False)), ('SIN T200-286 p<0.22 (bb bajo)', (200, 286, .09, .22, False)), ('SIN T220-260 p<0.22', (220, 260, .09, .22, False))):
    f = U(*args); P('  %-30s IS %s\n  %-30s OOS16-27 %s | OOS16-25 %s' % (nm, fmt(stats(f, IS)), '', fmt(stats(f, OO)), fmt(stats(f, OOS))))
open(R10 + 'rep/salida_tabla_fina.txt', 'w').write('\n'.join(L))
