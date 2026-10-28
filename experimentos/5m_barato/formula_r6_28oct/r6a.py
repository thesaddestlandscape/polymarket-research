#!/usr/bin/env python3
"""formula_r6_28oct/r6a.py - analisis A-E. Manda PREREG_FORMULA_R6.md (hash en HASHES_R6.txt)."""
import sys, os, math, json
import numpy as np
from scipy import stats
E4 = '/root/polymarket-research/experimentos/5m_barato/'
sys.path.insert(0, E4 + 'formula_r4_28oct'); sys.path.insert(0, E4 + 'formula_r3_28oct'); sys.path.insert(0, E4 + 'formula_r5_28oct')
import r4, r5f
BASE = E4 + 'formula_r6_28oct/'; FD = BASE + 'fills/'
LINES = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)
rng = np.random.default_rng(6280)
COLS = ['coin', 'T', 'rhat', 'trem', 'mk', 'tk', 'p', 'sz', 'y', 'swsz', 'maker', 'order', 'dA', 'sA', 'd4', 's4', 'dP', 'sP', 'bb', 'ba', 'cbb', 'cba', 'side', 'jdt', 'jdn']
def load(days, coin):
    out = {c: [] for c in COLS}; di = []
    for i, d in enumerate(days):
        z = np.load(FD + 'f_%s.npz' % d); m = z['coin'] == coin
        for c in COLS: out[c].append(z[c][m])
        di.append(np.full(int(m.sum()), i))
    R = {c: np.concatenate(v) for c, v in out.items()}; R['di'] = np.concatenate(di)
    R['den'] = R['sz'] * R['p']; R['num'] = R['sz'] * (R['y'] - R['p'])
    return R
def dayev(R, mask, nd):
    n = np.bincount(R['di'], weights=R['num'] * mask, minlength=nd); d = np.bincount(R['di'], weights=R['den'] * mask, minlength=nd)
    with np.errstate(all='ignore'): e = n / d
    return e, d, n
def summ(R, mask, dsel, nd):
    e, d, n = dayev(R, mask, nd); sel = [i for i in dsel if d[i] > 0]
    if len(sel) == 0: return None
    v = e[sel]; m, lo, hi = r4.tci(v); s2 = float(np.sort(v)[:-2].mean()) if len(v) > 3 else float('nan')
    return dict(nd=len(sel), eur=float(d[sel].sum()), eurd=float(d[sel].mean()), pool=float(n[sel].sum() / d[sel].sum()), mean=m, lo=lo, hi=hi, pos=int((v > 0).sum()), s2=s2, nf=int(mask.sum()))
def F(s):
    if s is None: return 'sin datos'
    return 'EVw %+.3f dia %+.3f [%+.3f,%+.3f] +%d/%d sin2 %+.3f | %.0f EUR/d n=%d' % (s['pool'], s['mean'], s['lo'], s['hi'], s['pos'], s['nd'], s['s2'], s['eurd'], s['nf'])
def duplift(R, S, extra, dsel, nd):
    n1 = np.bincount(R['di'], weights=R['num'] * (S & extra), minlength=nd); d1 = np.bincount(R['di'], weights=R['den'] * (S & extra), minlength=nd)
    n0 = np.bincount(R['di'], weights=R['num'] * (~S), minlength=nd); d0 = np.bincount(R['di'], weights=R['den'] * (~S), minlength=nd)
    sel = [i for i in dsel if d1[i] > 0 and d0[i] > 0]
    if not sel: return None
    v = (n1[sel] / d1[sel]) - (n0[sel] / d0[sel]); m, lo, hi = r4.tci(v)
    return dict(m=m, lo=lo, hi=hi, pos=int((v > 0).sum()), nd=len(sel), eur=float(d1[sel].sum()), e1=float(n1[sel].sum() / d1[sel].sum()), e0=float(n0[sel].sum() / d0[sel].sum()))
def FU(u):
    if u is None: return 'sin datos'
    return 'dEV %+.3f [%+.3f,%+.3f] +%d/%d | EV_S %+.3f EV_noS %+.3f | S %.0f EUR/d' % (u['m'], u['lo'], u['hi'], u['pos'], u['nd'], u['e1'], u['e0'], u['eur'] / max(1, u['nd']))
def signflip_max(V, K=5000):
    V = np.nan_to_num(V); n = V.shape[1]
    sg = rng.choice([-1.0, 1.0], size=(K, n)); mu = (sg @ V.T) / n; s2 = (V ** 2).mean(1)[None, :] - mu ** 2
    t = mu / np.sqrt(np.maximum(s2, 1e-18) / n); obs = V.mean(1) / np.sqrt(np.maximum((V ** 2).mean(1) - V.mean(1) ** 2, 1e-18) / n)
    return obs, (t.max(1))
def main():
    import io, contextlib
    days0 = sorted(f[2:12] for f in os.listdir(FD) if f.startswith('f_'))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): days = r5f.inclusion(days0)
    P('== R6 dias incluidos (%d): %s' % (len(days), ','.join(d[-2:] for d in days)))
    nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
    ISd, OOSd, DEVd = dd(5, 15), dd(16, 25), dd(26, 27); SELd, MEASd = dd(6, 15), dd(16, 27); ALL_d = dd(5, 31)
    for coin, nm in ((0, 'BTC'), (1, 'ETH')):
        R = load(days, coin); S = np.isfinite(R['dA']); nfill = len(S)
        P('\n==== %s: filas %d, en S800 %.1f %% (EUR %.1f %%)' % (nm, nfill, 100 * S.mean(), 100 * (R['den'] * S).sum() / R['den'].sum()))
        # ---- A reproduccion
        P('-- A reproduccion dEV/E (S800 menos no-S), IC90 por dias (R5: 06-25 +0,110 [+0,028,+0,192]; 22 dias +0,149 [+0,062,+0,236])')
        for lab, ds in (('06-25', dd(6, 25)), ('22 dias(06-27)', dd(6, 27)), ('IS 05-15', ISd), ('OOS 16-25', OOSd), ('DEV 26-27', DEVd)):
            P('  %s: %s' % (lab, FU(duplift(R, S, np.ones(nfill, bool), ds, nd))))
        # ---- B wallets
        def wstats(ds):
            m = np.isin(R['di'], ds); mk = R['maker'][m]; u, inv = np.unique(mk, return_inverse=True)
            den = np.bincount(inv, weights=R['den'][m]); num = np.bincount(inv, weights=R['num'][m])
            pair = np.unique(mk * 64 + R['di'][m]); ad = np.bincount(np.searchsorted(u, pair // 64), minlength=len(u))
            return u, den, num, ad
        for dirn, (sel, meas) in (('SEL 06-15 -> MEAS 16-27', (SELd, MEASd)), ('SEL 16-27 -> MEAS 06-15', (MEASd, SELd))):
            u, den, num, ad = wstats(sel); el = (ad >= 5) & (den >= 200); ue = u[el]; ev = num[el] / den[el]
            q = np.quantile(ev, [0.2, 0.8]); W = ue[ev >= q[1]]; L = ue[ev <= q[0]]; REST = ue[(ev > q[0]) & (ev < q[1])]
            P('-- B %s %s: wallets %d, elegibles %d (EV SEL: top20 >= %+.3f, bottom20 <= %+.3f); n W/L/REST %d/%d/%d' % (nm, dirn, len(u), el.sum(), q[1], q[0], len(W), len(L), len(REST)))
            mM = np.isin(R['di'], meas)
            for g, ws in (('GANADORAS', W), ('RESTO', REST), ('PERDEDORAS', L)):
                mg = np.isin(R['maker'], ws) & mM; sM = summ(R, mg, meas, nd)
                u2, den2, num2, _ = wstats(meas)
                P('   %-10s MEAS: %s | EUR S %.1f %%' % (g, F(sM), 100 * (R['den'] * (mg & S)).sum() / max(1, (R['den'] * mg).sum())))
            u2, den2, num2, _ = wstats(meas); pos = np.searchsorted(u2, ue); okp = (pos < len(u2)); okp[okp] = u2[pos[okp]] == ue[okp]
            nM = np.where(okp, num2[np.clip(pos, 0, len(u2) - 1)], 0.0); dM = np.where(okp, den2[np.clip(pos, 0, len(u2) - 1)], 0.0)
            isW = np.isin(ue, W); evW = nM[isW].sum() / max(1e-9, dM[isW].sum()); pl = []
            for _ in range(2000):
                ix = rng.choice(len(ue), size=int(isW.sum()), replace=False); pl.append(nM[ix].sum() / max(1e-9, dM[ix].sum()))
            pl = np.array(pl); P('   placebo (2000 sorteos): EV MEAS ganadoras %+.3f vs placebo media %+.3f, p(placebo>=) = %.3f | inversion (perdedoras) %+.3f' % (evW, pl.mean(), (pl >= evW).mean(), nM[np.isin(ue, L)].sum() / max(1e-9, dM[np.isin(ue, L)].sum())))
            if coin == 0 and dirn.startswith('SEL 06'): GRP = (W, REST, L)
        if coin != 0: continue
        # ---- B conductas (BTC, SEL 06-15 -> MEAS 16-27)
        W, REST, L = GRP; mM = np.isin(R['di'], MEASd)
        o, inv = np.unique(R['order'], return_inverse=True); no = len(o)
        first = np.full(no, np.inf); np.minimum.at(first, inv, R['rhat']); last = np.full(no, -np.inf); np.maximum.at(last, inv, R['rhat'])
        omk = np.zeros(no, np.int64); omk[inv] = R['maker']; otk = np.zeros(no, np.int64); otk[inv] = R['tk']; op = np.zeros(no); op[inv] = R['p']
        cnt_o = np.bincount(inv)
        oo = np.lexsort((first, otk, omk)); same_prev = np.zeros(no, bool); same_prev[1:] = (omk[oo][1:] == omk[oo][:-1]) & (otk[oo][1:] == otk[oo][:-1])
        dp_prev = np.full(no, np.nan); dp_prev[oo[1:][same_prev[1:]]] = (op[oo][1:] - op[oo][:-1])[same_prev[1:]]
        same_next = np.zeros(no, bool); same_next[:-1] = same_prev[1:]
        gap_next = np.full(no, np.nan); dp_next = np.full(no, np.nan)
        gap_next[oo[:-1][same_next[:-1]]] = (first[oo][1:] - last[oo][:-1])[same_next[:-1]]; dp_next[oo[:-1][same_next[:-1]]] = (op[oo][1:] - op[oo][:-1])[same_next[:-1]]
        nord_tk = np.zeros(no); key = omk * 1000003 + otk; uk, ik = np.unique(key, return_inverse=True); nord_tk = np.bincount(ik)[ik]
        gn = gap_next[inv]; dn = dp_next[inv]; nordf = nord_tk[inv]; age_o = R['rhat'] - first[inv]
        persist = S & (first[inv] <= (R['rhat'] - np.nan_to_num(R['dA'], nan=0) + 1000.0))
        wm = R['maker'] * 4000003 + R['mk']; uwm, iwm = np.unique(wm, return_inverse=True)
        ntk_wm = np.array([len(x) for x in [None]]) if False else None
        wmtk = np.unique(np.stack([iwm, R['tk']], 1), axis=0); ntk = np.bincount(wmtk[:, 0], minlength=len(uwm))[iwm]
        off = np.round((R['p'] - R['bb']) / 0.01); offc = np.where(np.isfinite(off), np.where(off < 0, 0, np.where(off == 0, 1, 2)), 3)
        hour = ((R['T'] % 86400) // 3600).astype(int)
        # coste de par por (maker, mercado, token)
        pairc = np.full(nfill, np.nan)
        s1 = np.bincount(iwm * 2 + np.clip(R['side'], 0, 1), weights=R['den'], minlength=2 * len(uwm)); q1 = np.bincount(iwm * 2 + np.clip(R['side'], 0, 1), weights=R['sz'], minlength=2 * len(uwm))
        with np.errstate(all='ignore'): pc = (s1[0::2] / q1[0::2]) + (s1[1::2] / q1[1::2])
        pairc = pc[iwm]
        C = {
         'contexto': (np.where(R['swsz'] >= 200, 0, np.where(S, 1, 2)), ['dentro de barrido on-chain (swsz>=200)', 'estado S post-barrido', 'sin S']),
         'delay s (S)': (np.where(S, np.digitize(R['dA'], [10000, 20000, 40000]), 4), ['5-10', '10-20', '20-40', '40-60', 'noS']),
         'nivel p-bb ticks': (offc, ['p<bb (profundo)', 'p=bb', 'p>bb (mejora)', 'sin libro']),
         'tam relleno acc': (np.digitize(R['sz'], [5, 20, 100]), ['<5', '5-20', '20-100', '>=100']),
         'tam barrido (S)': (np.where(S, np.digitize(R['sA'], [1600, 3200]), 3), ['800-1600', '1600-3200', '>=3200', 'noS']),
         'orden en S': (np.where(S, np.where(persist, 0, 1), 2), ['persistente (ya rellena en barrido)', 'nueva tras barrido', 'noS']),
         'ordenes/(wallet,token)': (np.clip(nordf, 1, 4).astype(int) - 1, ['1', '2', '3', '4+']),
         'cambio precio vs orden previa': (np.where(np.isnan(dp_prev[inv]), 3, np.where(dp_prev[inv] < -1e-9, 0, np.where(dp_prev[inv] > 1e-9, 2, 1))), ['baja', 'igual', 'sube', 'primera orden']),
         'reposicion tras relleno (sig. orden)': (np.where(np.isnan(gn), 3, np.where(gn <= 30000, np.where(dn < -1e-9, 0, np.where(dn > 1e-9, 2, 1)), 4)), ['<=30s precio menor', '<=30s igual', '<=30s mayor', 'ninguna', '>30s']),
         'ambos lados (wallet,mercado)': (np.where(np.isfinite(pairc), 1, 0), ['un lado', 'ambos tokens']),
         'lado token': (R['side'].astype(int) + 1, ['sin libro', 'side0', 'side1']),
         'hora UTC': (hour // 6, ['00-06', '06-12', '12-18', '18-24']),
         'T_rem s': (np.digitize(R['trem'], [60, 120, 180, 240]), ['<60', '60-120', '120-180', '180-240', '>=240']),
         'edad orden desde 1er relleno s': (np.digitize(age_o, [1, 5000, 30000]), ['0 (primer)', '<5', '5-30', '>30']),
         'Binance desde salto bajista s': (np.where(np.isfinite(R['jdt']), np.digitize(R['jdt'], [2000, 10000]), 3), ['<2', '2-10', '>10', 'n/d']),
         'salto bajista <=5 s tras relleno': (R['jdn'].astype(int), ['no', 'si']),
        }
        G = {'TODAS': mM, 'GANADORAS': mM & np.isin(R['maker'], W), 'RESTO': mM & np.isin(R['maker'], REST), 'PERDEDORAS': mM & np.isin(R['maker'], L)}
        P('\n-- B conductas (BTC, MEAS 16-27, grupos elegidos en SEL 06-15): cada celda = %EUR del grupo | EV/E | n')
        for nmC, (cl, labs) in C.items():
            P(' [%s]' % nmC)
            for k, lab in enumerate(labs):
                row = []
                for g, gm in G.items():
                    m = gm & (cl == k); tot = (R['den'] * gm).sum()
                    row.append('%s %4.1f%% %+.2f n%d' % (g[:4], 100 * (R['den'] * m).sum() / max(1, tot), (R['num'][m].sum() / R['den'][m].sum()) if m.sum() and R['den'][m].sum() > 0 else float('nan'), m.sum()))
                P('   %-38s %s' % (lab, ' | '.join(row)))
        P('   tamano medio de relleno acc S, por tamano de barrido (GANADORAS/RESTO): ' + '; '.join('%s %.1f/%.1f' % (lb, R['sz'][G['GANADORAS'] & S & (C['tam barrido (S)'][0] == k)].mean(), R['sz'][G['RESTO'] & S & (C['tam barrido (S)'][0] == k)].mean()) for k, lb in enumerate(['800-1600', '1600-3200', '>=3200'])))
        wsel = np.unique(R['maker'][mM & S & np.isin(R['maker'], W)]); P('   pares: coste medio de par (p_lado0+p_lado1, ponderado) GANADORAS %.3f RESTO %.3f (n con ambos tokens %d/%d)' % (np.nanmean(pairc[G['GANADORAS']]), np.nanmean(pairc[G['RESTO']]), np.isfinite(pairc[G['GANADORAS']]).sum(), G['GANADORAS'].sum()))
        # ---- C tramo S util
        P('\n-- C tramo S util (todos los makers, BTC): dEV por clase y particion')
        dims = {'T_rem': (np.digitize(R['trem'], [60, 120, 180, 240]), ['<60', '60-120', '120-180', '180-240', '>=240']), 'hora': (hour // 6, ['00-06', '06-12', '12-18', '18-24']),
                'precio': (np.digitize(R['p'], [0.15, 0.22]), ['.09-.15', '.15-.22', '.22-.31']), 'tam barrido': (np.where(S, np.digitize(R['sA'], [1600, 3200]), -1), ['800-1600', '1600-3200', '>=3200']),
                'delay s': (np.where(S, np.digitize(R['dA'], [10000, 20000, 40000]), -1), ['5-10', '10-20', '20-40', '40-60'])}
        keep = {}
        for dn_, (cl, labs) in dims.items():
            for k, lab in enumerate(labs):
                ex = (cl == k); us = {}
                for pn, ds in (('IS', ISd), ('OOS', OOSd), ('DEV', DEVd)): us[pn] = duplift(R, S, ex, ds, nd)
                P('  %-11s %-10s IS %s\n  %s OOS %s\n  %s DEV %s' % (dn_, lab, FU(us['IS']), ' ' * 22, FU(us['OOS']), ' ' * 22, FU(us['DEV'])))
                if us['IS'] and us['IS']['m'] >= 0.05 and us['IS']['eur'] / max(1, us['IS']['nd']) >= 30: keep.setdefault(dn_, []).append(k)
        P('  clases IS dEV>=+0,05 y >=30 EUR/d (regla ex-ante): %s' % json.dumps({k: [dims[k][1][i] for i in v] for k, v in keep.items()}))
        tram = np.ones(nfill, bool)
        for dn_, ks in keep.items(): tram &= np.isin(dims[dn_][0], ks) | (dn_ in ('delay s', 'tam barrido') and False)
        tram &= S
        for pn, ds in (('IS', ISd), ('OOS', OOSd), ('DEV', DEVd)):
            e1 = summ(R, tram, ds, nd); u = duplift(R, S, tram, ds, nd); P('  TRAMO conjuncion %s: %s | %s | cobertura EUR S %.1f %%' % (pn, F(e1), FU(u), 100 * (R['den'] * tram * np.isin(R['di'], ds)).sum() / max(1, (R['den'] * S * np.isin(R['di'], ds)).sum())))
        P('  covariables diarias: dia | EUR S | %fills S | tam medio S | adverso<=5s | EV_S | EV_noS | dEV')
        cv = []
        for i, d in enumerate(days):
            m = R['di'] == i; e, dnn, _ = dayev(R, S & m, nd); e0, _, _ = dayev(R, (~S) & m, nd)
            P('   %s %7.0f %5.1f%% %6.1f %5.3f %+.3f %+.3f %+.3f' % (d[-2:], dnn[i], 100 * S[m].mean(), R['sz'][m & S].mean(), R['jdn'][m].mean(), e[i], e0[i], e[i] - e0[i])); cv.append((dnn[i], S[m].mean(), R['sz'][m & S].mean(), R['jdn'][m].mean(), e[i] - e0[i]))
        cv = np.array(cv); P('   Spearman dEV con EUR S/%S/tam/adverso: ' + ' '.join('%+.2f' % stats.spearmanr(cv[:, k], cv[:, 4])[0] for k in range(4)))
        # ---- D familia de conductas
        P('\n-- D familia de 48 conductas (poblacion de rellenos de todos los makers en S800 BTC)')
        fam = []; V = []
        trs = R['trem']
        for dl in ((5000, 20000), (20000, 60001), (5000, 60001)):
            for lv in (0, 1):
                for tr in ((60, 290), (120, 240)):
                    for sz_ in (800, 1600):
                        for pr in (0.15, 0.0):
                            m = S & (R['dA'] >= dl[0]) & (R['dA'] < dl[1]) & (trs >= tr[0]) & (trs < tr[1]) & (R['sA'] >= sz_) & (R['p'] >= pr)
                            if lv: m &= np.isfinite(off) & (off >= 0)
                            fam.append((dl, lv, tr, sz_, pr, m))
        def famstats(ds):
            Vv = np.full((len(fam), len(ds)), np.nan)
            for j, (_, _, _, _, _, m) in enumerate(fam):
                e, d_, _ = dayev(R, m, nd)
                for t, i in enumerate(ds):
                    if d_[i] > 0: Vv[j, t] = e[i]
            return Vv
        def lab(f): return 'delay[%d,%d)s nivel>=bb:%d Trem[%d,%d) barrido>=%d p>=%.2f' % (f[0][0] // 1000, f[0][1] // 1000, f[1], f[2][0], f[2][1], f[3], f[4])
        for dirn, (sel, meas) in (('IS 06-15 -> OOS 16-25 y DEV 26-27', (SELd, [OOSd, DEVd])), ('inversa IS 16-27 -> 06-15', (MEASd, [SELd]))):
            Vs = famstats(sel); lo = np.array([r4.tci(v[np.isfinite(v)])[1] if np.isfinite(v).sum() > 2 else -9 for v in Vs]); j = int(np.argmax(lo))
            obs, nullmax = signflip_max(Vs); pj = (nullmax >= obs[j]).mean()
            P(' %s: elegida %s | IS %s | p max-stat (volteo signos, 48) %.3f; candidatas con cota inf IC90>0 en IS: %d/48' % (dirn, lab(fam[j]), F(summ(R, fam[j][5], sel, nd)), pj, int((lo > 0).sum())))
            for ds in meas:
                m = fam[j][5]; s = summ(R, m, ds, nd); P('    medida: %s' % F(s))
                shifted = np.isfinite(R['dP']) & (R['dP'] >= fam[j][0][0]) & (R['dP'] < fam[j][0][1]) & (trs >= fam[j][2][0]) & (trs < fam[j][2][1]) & (R['sP'] >= fam[j][3]) & (R['p'] >= fam[j][4])
                if fam[j][1]: shifted &= np.isfinite(off) & (off >= 0)
                P('    placebo (barridos +30 min): %s | inversion (en S, fuera de la conducta): %s' % (F(summ(R, shifted, ds, nd)), F(summ(R, S & ~m, ds, nd))))
                P('    VARIANTES en la medida: EV>0 en %d/48 (media familia %+.3f); EV medio todos los rellenos noS: %s' % (sum(1 for f in fam if (summ(R, f[5], ds, nd) or {'pool': -1})['pool'] > 0), np.mean([(summ(R, f[5], ds, nd) or {'pool': 0})['pool'] for f in fam]), F(summ(R, ~S, ds, nd))))
            if dirn.startswith('IS 06'):
                m = fam[j][5]; mo = m & np.isin(R['di'], OOSd); fl = (R['den'] * (S & np.isin(R['di'], OOSd))).sum() / len(OOSd); cf = (R['den'] * mo).sum() / len(OOSd)
                u2, inv2 = np.unique(R['maker'][mo], return_inverse=True); wsh = np.sort(np.bincount(inv2, weights=R['den'][mo]))[::-1] / R['den'][mo].sum()
                mkk = np.unique(np.stack([R['mk'][mo], R['maker'][mo]], 1), axis=0); nmk = np.bincount(np.unique(mkk[:, 0], return_inverse=True)[1])
                ev_ = summ(R, m, OOSd, nd)['pool']
                P('    CUOTA OOS: conducta %.0f EUR/d = %.1f %% del flujo S800-BTC (%.0f EUR/d); wallets %d, top1 %.1f %% top5 %.1f %%; makers por mercado mediana %.0f -> cuota justa 1/n = %.1f %% del flujo de la conducta = %.2f %% del flujo S' % (cf, 100 * cf / fl, fl, len(u2), 100 * wsh[0], 100 * wsh[:5].sum(), np.median(nmk), 100 / np.median(nmk), 100 * cf / fl / np.median(nmk)))
                P('    EUR/ano a EVw %+.3f: cuota 9%% del flujo S -> %.0f ; cuota 1/n de la conducta -> %.0f ; cuota del flujo S necesaria para 200k: %s' % (ev_, ev_ * 0.09 * fl * 365, ev_ * cf / np.median(nmk) * 365, ('%.1f %%' % (100 * 200000 / (ev_ * fl * 365))) if ev_ > 0 else 'imposible'))
        # ---- E v057 / v258
        P('\n-- E nichos de v057 y v258 (rellenos de todos los makers) y criterios')
        niches = {'v057 (>=400, 1-120 s, Trem 60-290, p .20-.29, p=bb)': np.isfinite(R['d4']) & (R['s4'] >= 400) & (trs >= 60) & (trs < 290) & (R['p'] >= 0.20) & (R['p'] <= 0.29) & (off == 0),
                  'v258 (>=800, 5-60 s, Trem 120-240, p<.29, p>=bb)': S & (R['sA'] >= 800) & (trs >= 120) & (trs < 240) & (R['p'] <= 0.29) & np.isfinite(off) & (off >= 0)}
        flS = lambda ds: (R['den'] * (S & np.isin(R['di'], ds))).sum() / len(ds)
        for nn, m in niches.items():
            for pn, ds in (('IS', ISd), ('OOS', OOSd), ('DEV', DEVd)):
                s = summ(R, m, ds, nd); P('  %s %s: %s | cuota del flujo S800 %.2f %%' % (nn[:4], pn, F(s), 100 * (R['den'] * (m & np.isin(R['di'], ds))).sum() / len(ds) / flS(ds)))
            for q_, ds in (('DEV', DEVd),): pass
        # C5 ruido: bootstrap por mercado del nicho v258 y v057 en OOS
        P(' C5 (>=8/10 dias+) por RUIDO, ejecutando 543 ejec x 20 acc (~%d EUR/d) sobre el nicho, EV verdadero m (bootstrap por mercado, 3000 dias):' % int(543 * 20 * 0.25))
        for nn, m in niches.items():
            mo = m & np.isin(R['di'], OOSd); u_, iv = np.unique(R['mk'][mo], return_inverse=True)
            c_ = np.bincount(iv, weights=R['den'][mo]); p_ = np.bincount(iv, weights=R['num'][mo]); base = p_.sum() / c_.sum(); tgt = 543 * 20 * 0.25
            if len(u_) < 20: P('  %s: nicho con pocos mercados' % nn[:4]); continue
            res = {}
            for mtrue in (0.0, 0.03, 0.05, 0.10):
                wins = 0; K = 1500
                for _ in range(K):
                    ix = rng.integers(0, len(u_), size=len(u_)); cs = np.cumsum(c_[ix]); k = int(np.searchsorted(cs, tgt)) + 1; ix = ix[:k]
                    ev = (p_[ix].sum() / c_[ix].sum()) - base + mtrue; wins += ev > 0
                res[mtrue] = wins / K
            from scipy.stats import binom
            P('  %s: P(dia+) y P(>=8/10 dias+): ' % nn[:4] + ' | '.join('m=%+.2f: %.2f / %.3f' % (k, v, 1 - binom.cdf(7, 10, v)) for k, v in res.items()))
    open(BASE + 'salida_r6a.txt', 'w').write('\n'.join(LINES))
if __name__ == '__main__': main()
