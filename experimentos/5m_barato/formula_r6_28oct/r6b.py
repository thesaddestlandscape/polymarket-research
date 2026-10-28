import sys, os, numpy as np, io, contextlib
from scipy import stats
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r6_28oct')
import r6a
from r6a import *
def feats(R, S, ds):
    m = np.isin(R['di'], ds); mk = R['maker'][m]; u, inv = np.unique(mk, return_inverse=True)
    den = R['den'][m]; nu = len(u)
    pair = np.unique(mk * 64 + R['di'][m]); ad = np.bincount(np.searchsorted(u, pair // 64), minlength=nu)
    w = lambda x: np.bincount(inv, weights=den * x[m], minlength=nu) / np.maximum(np.bincount(inv, weights=den, minlength=nu), 1e-9)
    ev = np.bincount(inv, weights=R['num'][m], minlength=nu) / np.maximum(np.bincount(inv, weights=den, minlength=nu), 1e-9)
    tot = np.bincount(inv, weights=den, minlength=nu)
    f = np.vstack([np.bincount(inv, weights=R['sz'][m], minlength=nu) / np.bincount(inv, minlength=nu), w(R['f2']), w(R['f3']), w(R['f4']), w(R['f5']), w(R['f6']), np.bincount(inv, weights=R['f7'][m], minlength=nu) / np.bincount(inv, minlength=nu), w(R['f8'])])
    return u, f, ev, tot, ad
def main():
    days0 = sorted(f[2:12] for f in os.listdir(FD) if f.startswith('f_')); buf = io.StringIO()
    with contextlib.redirect_stdout(buf): days = r5f.inclusion(days0)
    nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
    SELd, MEASd = dd(6, 15), dd(16, 27)
    R = load(days, 0); S = np.isfinite(R['dA'])
    o, inv = np.unique(R['order'], return_inverse=True)
    key = R['maker'] * 1000003 + R['tk']; uk, ik = np.unique(key, return_inverse=True)
    pk = np.unique(np.stack([ik, inv], 1), axis=0); nord = np.bincount(pk[:, 0], minlength=len(uk))[ik]
    R['f2'] = (nord == 1).astype(float); R['f3'] = (R['swsz'] >= 200).astype(float); R['f4'] = ((R['swsz'] < 200) & S).astype(float)
    R['f5'] = (~np.isfinite(R['bb'])).astype(float); R['f6'] = (np.round((R['p'] - R['bb']) / 0.01) == 0).astype(float); R['f7'] = nord.astype(float)
    wm = R['maker'] * 4000003 + R['mk']; uwm, iwm = np.unique(wm, return_inverse=True)
    s1 = np.bincount(iwm * 2 + np.clip(R['side'], 0, 1), weights=R['sz'], minlength=2 * len(uwm)); R['f8'] = ((s1[0::2] > 0) & (s1[1::2] > 0))[iwm].astype(float)
    names = ['tam medio acc', '%EUR 1 orden/(wallet,token)', '%EUR dentro barrido', '%EUR S post', '%EUR sin libro/profundo', '%EUR p=bb', 'ordenes medias/(w,token)', '%EUR ambos tokens']
    for dirn, (sel, meas) in (('SEL 06-15 -> MEAS 16-27', (SELd, MEASd)), ('SEL 16-27 -> MEAS 06-15', (MEASd, SELd))):
        u, f, ev, tot, ad = feats(R, S, sel); el = (ad >= 5) & (tot >= 200)
        u2, f2_, ev2, tot2, _ = feats(R, S, meas); pos = np.searchsorted(u2, u[el]); ok = (pos < len(u2)); ok[ok] = u2[pos[ok]] == u[el][ok]
        okm = np.zeros(len(u), bool); idx_el = np.nonzero(el)[0]; okm[idx_el[ok]] = True; okm[idx_el[ok]] &= tot2[pos[ok]] >= 200
        ue = u[okm]; pe = np.searchsorted(u2, ue); evm = ev2[pe]; P('-- %s: wallets elegibles en SEL con >=200 EUR en MEAS: %d' % (dirn, len(ue)))
        for k in range(8):
            r, p = stats.spearmanr(f[k][okm], evm); r0, p0 = stats.spearmanr(f[k][okm], ev[okm]); P('   %-30s rho(rasgo SEL, EV MEAS) %+.3f p=%.4f | rho(rasgo, EV SEL) %+.3f' % (names[k], r, p, r0))
        Z = lambda x: (x - x.mean()) / (x.std() + 1e-12)
        comp = Z(f[0][el]) + Z(f[1][el]) + Z(f[2][el]); ue_all = u[el]
        top = ue_all[comp >= np.quantile(comp, 0.8)]; bot = ue_all[comp <= np.quantile(comp, 0.2)]
        mM = np.isin(R['di'], meas)
        for g, ws in (('compuesto top20', top), ('compuesto bottom20', bot)):
            P('   %s MEAS: %s' % (g, F(summ(R, np.isin(R['maker'], ws) & mM, meas, nd))))
        P('   resto MEAS (elegibles no top): %s' % F(summ(R, np.isin(R['maker'], ue_all[~np.isin(ue_all, top)]) & mM, meas, nd)))
        num = np.zeros(len(ue_all)); den_ = np.zeros(len(ue_all)); pos2 = np.searchsorted(u2, ue_all); okk = (pos2 < len(u2)); okk[okk] = u2[pos2[okk]] == ue_all[okk]
        pm = pos2[okk]; 
        den2 = np.bincount(np.searchsorted(u2, R['maker'][mM]) , weights=R['den'][mM], minlength=len(u2)); num2 = np.bincount(np.searchsorted(u2, R['maker'][mM]), weights=R['num'][mM], minlength=len(u2))
        num[okk] = num2[pm]; den_[okk] = den2[pm]; ist = np.isin(ue_all, top); evt = num[ist].sum() / max(1e-9, den_[ist].sum())
        pl = np.array([ (lambda ix: num[ix].sum() / max(1e-9, den_[ix].sum()))(rng.choice(len(ue_all), size=int(ist.sum()), replace=False)) for _ in range(2000)])
        P('   placebo: EV top %+.3f vs placebo media %+.3f, p=%.3f' % (evt, pl.mean(), (pl >= evt).mean()))
    open(BASE + 'salida_r6b.txt', 'w').write('\n'.join(r6a.LINES))
main()
