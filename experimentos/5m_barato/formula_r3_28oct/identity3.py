#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r3_28oct/identity3.py - bloque de identidad del barrendero (on-chain 26-27 Oct) para PREREG_FORMULA_R3.md.
SOLO atribucion/etiqueta: la identidad llega ~2,4 s tras el casado; ningun rasgo de identidad entra en M1-M5.
Uso: identity3.py [--smoke]   (smoke: primeras 600k lineas de cada fichero; no decide nada)"""
import sys, os, gzip, json, math, time, datetime, traceback
import numpy as np
from collections import defaultdict
from scipy import stats

BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/'
REG = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
ONC = '/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_%s.csv.gz'
CACHE = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'
DAYS = ['2026-10-26', '2026-10-27']
PLO, PHI = 0.09, 0.31
SMOKE = '--smoke' in sys.argv
MAXL = 600000 if SMOKE else 10 ** 12
rng = np.random.default_rng(2811)
LINES = []


def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)


def ntok(s):
    s = s.strip()
    return str(int(s, 16)) if s.startswith('0x') else s


def load_registry(day):
    tok = {}; prints = defaultdict(list)
    d0 = datetime.datetime.fromisoformat(day + 'T00:00:00+00:00').timestamp()
    cmin = d0 + 299; cmax = d0 + 86401; n = 0
    with gzip.open(REG % day, 'rt') as f:
        next(f)
        for ln in f:
            n += 1
            if n > MAXL: break
            ty = ln[0]
            if ty == 'k':
                c = ln.rstrip('\n').split(',')
                if len(c) < 8 or c[4] != '5min' or c[7] not in ('YES', 'NO'): continue
                cie = datetime.datetime.fromisoformat(c[6]).timestamp()
                if not (cmin <= cie <= cmax): continue
                tok[ntok(c[2])] = (c[5], c[3], c[7], cie)
            elif ty == 't':
                c = ln.rstrip('\n').split(',')
                tk = ntok(c[2])
                if tk not in tok: continue
                p = float(c[3]); sd = c[4]
                if sd == 'SELL':
                    if not (PLO - 0.005 <= p <= PHI + 0.005): continue
                elif sd == 'BUY':
                    if not (1.0 - PHI - 0.005 <= p <= 1.0 - PLO + 0.005): continue
                else: continue
                rv = c[6].strip()
                prints[(tk, round(p, 3))].append((float(rv) if rv else float(c[1]), sd, float(c[5])))
    return tok, prints


def load_onchain(day, tok):
    rows = []; n = 0; nF = 0
    with gzip.open(ONC % day, 'rt') as f:
        next(f)
        for ln in f:
            n += 1
            if n > MAXL: break
            if ln[0] != 'F': continue
            c = ln.rstrip('\n').split(',')
            tk = ntok(c[9])
            if tk not in tok: continue
            nF += 1
            if c[7] == EX or c[8] != '0': continue
            ma = float(c[10]); ta = float(c[11])
            if ta <= 0: continue
            p = ma / ta
            if not (PLO <= p <= PHI): continue
            rows.append((float(c[2]), c[3], c[6], c[7], tk, p, ta))
    return rows, n, nF


def match(rows, tok, prints):
    comp = {}; bym = defaultdict(dict)
    for tk, (mk, coin, side, cie) in tok.items(): bym[mk][side] = tk
    for mk, d in bym.items():
        if 'YES' in d and 'NO' in d: comp[d['YES']] = d['NO']; comp[d['NO']] = d['YES']
    out = []
    for (ts, tx, mkr, tkr, tk, p, sz) in rows:
        tms = ts * 1000.0; best = None
        cands = [(tk, round(p, 3), 'SELL')]
        ct = comp.get(tk)
        if ct is not None: cands.append((ct, round(1.0 - p, 3), 'BUY'))
        for (t2, p2, sd) in cands:
            for (r, s2, z) in prints.get((t2, p2), ()):
                if s2 != sd or abs(z - sz) > max(0.02, 2e-3 * sz): continue
                d = tms - r
                if -1500.0 <= d <= 15000.0 and (best is None or abs(d - 2400.0) < abs(best - 2400.0)): best = d
        out.append(best)
    return out


def main():
    G = json.load(open(CACHE))
    F = defaultdict(list)
    for di, day in enumerate(DAYS):
        t0 = time.time()
        tok, prints = load_registry(day)
        rows, n_on, nF = load_onchain(day, tok)
        lag = match(rows, tok, prints)
        kept = 0
        for r, lg in zip(rows, lag):
            ts, tx, mkr, tkr, tk, p, sz = r
            mkid, coin, side, cie = tok[tk]
            o = G.get(mkid)
            if o not in ('YES', 'NO'): continue
            F['day'].append(di); F['ts'].append(ts); F['tx'].append(tx); F['tk'].append(tk); F['mk'].append(mkid)
            F['coin'].append(coin); F['p'].append(p); F['sz'].append(sz); F['y'].append(1.0 if o == side else 0.0)
            F['lag'].append(np.nan if lg is None else lg); F['wl'].append(tkr); kept += 1
        nl = np.array([x for x in lag if x is not None])
        q = np.percentile(nl, [10, 50, 90]).round(0).tolist() if len(nl) else []
        P('[%s] lineas_onchain=%d filas_F_tokens5m=%d pujas_zona=%d con_desenlace=%d | casadas con impresion t: %.1f %% | bloque-recepcion ms p10/p50/p90=%s | tokens5m=%d claves_impresion=%d (%.0f s)'
          % (day, n_on, nF, len(rows), kept, 100.0 * len(nl) / max(1, len(rows)), q, len(tok), len(prints), time.time() - t0))
        del tok, prints
    if not F['day']:
        P('SIN FILAS'); return
    day = np.array(F['day']); ts = np.array(F['ts']); p = np.array(F['p']); sz = np.array(F['sz']); yv = np.array(F['y'])
    wmap = {}; mmap = {}; cmap = {}; smap = {}
    wid = np.fromiter((wmap.setdefault(w, len(wmap)) for w in F['wl']), dtype=np.int64, count=len(day))
    mki = np.fromiter((mmap.setdefault(w, len(mmap)) for w in F['mk']), dtype=np.int64, count=len(day))
    coi = np.fromiter((cmap.setdefault(w, len(cmap)) for w in F['coin']), dtype=np.int64, count=len(day))
    swi = np.fromiter((smap.setdefault(k, len(smap)) for k in zip(F['tx'], F['wl'], F['tk'])), dtype=np.int64, count=len(day))
    NW = len(wmap); K = len(mmap)
    num = sz * (yv - p); den = sz * p
    fn = np.bincount(swi)[swi]; fs = np.bincount(swi, weights=sz)[swi]

    def ev_ci(mask, B=500):
        n_m = np.bincount(mki[mask], weights=num[mask], minlength=K); d_m = np.bincount(mki[mask], weights=den[mask], minlength=K)
        if d_m.sum() <= 0: return (np.nan, np.nan, np.nan)
        ev = n_m.sum() / d_m.sum(); act = np.nonzero(d_m > 0)[0]
        if len(act) < 5: return (ev, np.nan, np.nan)
        ix = rng.integers(0, len(act), (B, len(act)))
        bs = n_m[act][ix].sum(1) / d_m[act][ix].sum(1)
        return (float(ev), float(np.percentile(bs, 5)), float(np.percentile(bs, 95)))

    def diff_ci(m1, m0, B=500):
        n1 = np.bincount(mki[m1], weights=num[m1], minlength=K); d1 = np.bincount(mki[m1], weights=den[m1], minlength=K)
        n0 = np.bincount(mki[m0], weights=num[m0], minlength=K); d0 = np.bincount(mki[m0], weights=den[m0], minlength=K)
        e1 = n1.sum() / d1.sum() if d1.sum() > 0 else np.nan; e0 = n0.sum() / d0.sum() if d0.sum() > 0 else np.nan
        act = np.nonzero((d1 + d0) > 0)[0]
        if len(act) < 5 or not (d1.sum() > 0 and d0.sum() > 0): return (e1, e0, e1 - e0, np.nan, np.nan)
        ix = rng.integers(0, len(act), (B, len(act)))
        with np.errstate(all='ignore'):
            b1 = n1[act][ix].sum(1) / d1[act][ix].sum(1); b0 = n0[act][ix].sum(1) / d0[act][ix].sum(1)
        df = (b1 - b0)[np.isfinite(b1 - b0)]
        if len(df) < 50: return (e1, e0, e1 - e0, np.nan, np.nan)
        return (float(e1), float(e0), float(e1 - e0), float(np.percentile(df, 5)), float(np.percentile(df, 95)))

    fmt = lambda t: 'EV/E=%+.3f IC90[%+.3f,%+.3f]' % t
    P('== I0/I1 poblacion y concentracion (pujas de maker BUY de tokens 5m en [%.2f,%.2f] rellenadas; EV/E = sum tam*(y-p)/sum tam*p)' % (PLO, PHI))
    for di in range(len(DAYS)):
        mk_ = day == di
        cw = np.sort(np.bincount(wid[mk_], weights=den[mk_], minlength=NW))[::-1]; tot = cw.sum()
        nf = np.bincount(wid[mk_], minlength=NW)
        P('   %s rellenos=%d mercados=%d barrenderos=%d (>=30 rellenos: %d) barridos=%d | %s | top1/top5/top10 del volumen: %.1f/%.1f/%.1f %% HHI=%.4f'
          % (DAYS[di], int(mk_.sum()), len(np.unique(mki[mk_])), int((nf > 0).sum()), int((nf >= 30).sum()), len(np.unique(swi[mk_])), fmt(ev_ci(mk_)),
             100 * cw[:1].sum() / tot, 100 * cw[:5].sum() / tot, 100 * cw[:10].sum() / tot, float(((cw / tot) ** 2).sum())))

    def informed(learn):
        mkl = day == learn
        nf = np.bincount(wid[mkl], minlength=NW); ne = np.bincount(wid[mkl], weights=num[mkl], minlength=NW); de = np.bincount(wid[mkl], weights=den[mkl], minlength=NW)
        cand = np.nonzero(nf >= 30)[0]
        inf_ = np.zeros(NW, bool)
        if len(cand) < 5: return inf_, len(cand), np.nan
        evw = ne[cand] / np.maximum(de[cand], 1e-12); thr = float(np.percentile(evw, 20))
        inf_[cand[evw <= thr]] = True
        return inf_, len(cand), thr

    if len(DAYS) == 2:
        P('== I2 persistencia (informados = 20 %% peor EV/E entre barrenderos con >=30 rellenos el dia A; se miden el dia B)')
        for (A_, B_) in ((0, 1), (1, 0)):
            inf_, nq, thr = informed(A_)
            tb = day == B_; isinf = inf_[wid]
            e1, e0, df, lo, hi = diff_ci(tb & isinf, tb & ~isinf)
            P('   A=%s -> B=%s: calificados %d, informados %d (umbral EV/E %+.3f) | rellenos de informados el dia B: %d (%.1f %% de los rellenos, %.1f %% del volumen) | EV/E informados %+.3f vs resto %+.3f, dif %+.3f IC90[%+.3f,%+.3f]'
              % (DAYS[A_], DAYS[B_], nq, int(inf_.sum()), thr, int((tb & isinf).sum()), 100.0 * (tb & isinf).sum() / max(1, tb.sum()),
                 100.0 * den[tb & isinf].sum() / max(1e-12, den[tb].sum()), e1, e0, df, lo, hi))
            na = np.bincount(wid[day == A_], minlength=NW); nb = np.bincount(wid[tb], minlength=NW)
            ea = np.bincount(wid[day == A_], weights=num[day == A_], minlength=NW) / np.maximum(np.bincount(wid[day == A_], weights=den[day == A_], minlength=NW), 1e-12)
            eb = np.bincount(wid[tb], weights=num[tb], minlength=NW) / np.maximum(np.bincount(wid[tb], weights=den[tb], minlength=NW), 1e-12)
            both = np.nonzero((na >= 15) & (nb >= 15))[0]
            if len(both) >= 8:
                rho = stats.spearmanr(ea[both], eb[both])
                P('      Spearman EV/E por barrendero entre dias (>=15 rellenos ambos dias, n=%d barrenderos): rho=%+.3f p=%.3f' % (len(both), rho[0], rho[1]))
            sel = tb & isinf; win = np.zeros(len(day), bool)
            for c_ in range(len(cmap)):
                tsc = np.sort(ts[sel & (coi == c_)])
                ic = np.nonzero(tb & (coi == c_))[0]
                if len(tsc) == 0 or len(ic) == 0: continue
                a = np.searchsorted(tsc, ts[ic] - 5.0, side='right'); b = np.searchsorted(tsc, ts[ic] - 60.0, side='right')
                win[ic] = (a - b) > 0
            e1, e0, df, lo, hi = diff_ci(tb & win, tb & ~win)
            P('   I3 puerta de cadencia (misma moneda, relleno de un informado del dia A en (t-60 s, t-5 s]): senala %.1f %% de los rellenos del dia B | EV/E senalados %+.3f vs resto %+.3f, dif %+.3f IC90[%+.3f,%+.3f]'
              % (100.0 * (tb & win).sum() / max(1, tb.sum()), e1, e0, df, lo, hi))
            e1, e0, df, lo, hi = diff_ci(tb & win & ~isinf, tb & ~win & ~isinf)
            P('      solo rellenos de NO informados: senalados %.1f %% | EV/E %+.3f vs %+.3f, dif %+.3f IC90[%+.3f,%+.3f]' % (100.0 * (tb & win & ~isinf).sum() / max(1, (tb & ~isinf).sum()), e1, e0, df, lo, hi))
    P('== I4 cadencia propia (rellenos del mismo barrendero en (t-60 s, t-5 s], mismo dia)')
    cnt = np.zeros(len(day), np.int64)
    for di in range(len(DAYS)):
        ii = np.nonzero(day == di)[0]
        if len(ii) == 0: continue
        key = wid[ii].astype(np.float64) * 1e5 + (ts[ii] - ts[ii].min()); sk = np.sort(key)
        cnt[ii] = np.searchsorted(sk, key - 5.0, side='right') - np.searchsorted(sk, key - 60.0, side='right')
    for lab, mk_ in (('0', cnt == 0), ('1-2', (cnt >= 1) & (cnt <= 2)), ('3-9', (cnt >= 3) & (cnt <= 9)), ('>=10', cnt >= 10)):
        P('   previos=%-4s rellenos=%7d (%.1f %%) %s' % (lab, int(mk_.sum()), 100.0 * mk_.mean(), fmt(ev_ci(mk_))))
    P('== I5 tamano del barrido y makers alcanzados frente a EV/E (barrido = tx, barrendero, token)')
    for lab, mk_ in (('tam<10', fs < 10), ('10-50', (fs >= 10) & (fs < 50)), ('50-200', (fs >= 50) & (fs < 200)), ('>=200', fs >= 200)):
        P('   %-7s rellenos=%7d (%.1f %%) %s' % (lab, int(mk_.sum()), 100.0 * mk_.mean(), fmt(ev_ci(mk_))))
    for lab, mk_ in (('1 maker', fn == 1), ('2-3', (fn >= 2) & (fn <= 3)), ('>=4', fn >= 4)):
        P('   %-7s rellenos=%7d (%.1f %%) %s' % (lab, int(mk_.sum()), 100.0 * mk_.mean(), fmt(ev_ci(mk_))))
    P('LIMITES: 2 dias on-chain (26-27 Oct) = 1 replicacion A<->B; barrendero = direccion, no persona; reloj de bloque ~2,4 s tras el casado: NINGUN rasgo de identidad entra en M1-M5%s' % (' [SMOKE: no decide]' if SMOKE else ''))


if __name__ == '__main__':
    t0 = time.time()
    try: main()
    except Exception: P('ERROR identity3', traceback.format_exc()[-1500:])
    P('fin %.0f s' % (time.time() - t0))
    open(BASE + ('identity_salida_smoke.txt' if SMOKE else 'identity_salida.txt'), 'w').write('\n'.join(LINES) + '\n')
