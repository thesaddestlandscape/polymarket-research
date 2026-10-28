#!/usr/bin/env python3
"""formula_r6_28oct/r6x.py - extrae rellenos BTC/ETH con maker/orden + contexto S + libro BTC + saltos Binance. Manda PREREG_FORMULA_R6.md. Idempotente."""
import sys, os, gzip, time, zlib, json
import numpy as np
E4 = '/root/polymarket-research/experimentos/5m_barato/'
sys.path.insert(0, E4 + 'formula_r4_28oct'); sys.path.insert(0, E4 + 'formula_r3_28oct'); sys.path.insert(0, E4 + 'formula_r5_28oct')
import r4, r5f
I = r4.I
BASE = E4 + 'formula_r6_28oct/'; OUT = BASE + 'fills/'; EXT = E4 + 'formula_r5_28oct/ext/'
def crc(s): return zlib.crc32(s.encode()) & 0xffffffff


def ctx(rhat, coin, rec, size, ccoin, lo, hi, th):
    n = len(rhat); delay = np.full(n, np.nan); sz_ = np.full(n, np.nan); cnt = np.zeros(n)
    k = size >= th
    for c in np.unique(coin):
        kk = k & (ccoin == c)
        if not kk.any(): continue
        r = rec[kk]; s = size[kk]; o = np.argsort(r); r = r[o]; s = s[o]
        q = np.nonzero(coin == c)[0]
        a = np.searchsorted(r, rhat[q] - lo, side='right'); b = np.searchsorted(r, rhat[q] - hi, side='right')
        has = (a - b) > 0; i = np.clip(a - 1, 0, len(r) - 1); qq = q[has]
        delay[qq] = rhat[qq] - r[i[has]]; sz_[qq] = s[i[has]]; cnt[q] = a - b
    return delay, sz_, cnt


def maker_rows(day, tkset):
    mk = []; od = []; hx = {}
    with gzip.open(r4.onc_fmt(day) % day, 'rt') as f:
        next(f)
        for ln in f:
            if ln[0] != 'F': continue
            c = ln.rstrip('\n').split(',')
            if c[7] == I.EX or c[8] != '0': continue
            if crc(I.ntok(c[9])) not in tkset: continue
            ma = float(c[10]); ta = float(c[11])
            if ta <= 0: continue
            p = ma / ta
            if not (I.PLO <= p <= I.PHI): continue
            m = crc(c[6]); mk.append((float(c[2]), p, m, crc(c[5]))); hx[m] = c[6]
    return mk, hx


def run(day):
    out = OUT + 'f_%s.npz' % day
    if os.path.exists(out): print(day, 'ya hecho'); return
    t0 = time.time(); D = r4.load_day(day)
    rows, hx = maker_rows(day, set(D['tk'].tolist()))
    T = np.array([r[0] for r in rows]); p = np.array([r[1] for r in rows])
    assert len(T) == len(D['T']) and np.allclose(T, D['T']) and np.allclose(p, D['p'], atol=1e-9), 'desalineado %s %d %d' % (day, len(T), len(D['T']))
    maker = np.array([r[2] for r in rows], np.int64); order = np.array([r[3] for r in rows], np.int64)
    c = r5f.cl2(D, 'ALL'); rhat = D['rhat']; coin = D['coin']
    sel = np.nonzero((coin == 0) | (coin == 1))[0]
    R = {k: D[k][sel] for k in ('coin', 'T', 'rhat', 'matched', 'trem', 'mk', 'tk', 'tkr', 'swid', 'p', 'sz', 'y', 'swsz', 'swT')}
    R['maker'] = maker[sel]; R['order'] = order[sel]
    rh = R['rhat']; cn = R['coin']
    R['dA'], R['sA'], R['cA'] = ctx(rh, cn, c['rec'], c['size'], c['coin'], 5000., 60000., 800.)
    R['d4'], R['s4'], _ = ctx(rh, cn, c['rec'], c['size'], c['coin'], 1000., 120000., 400.)
    R['dP'], R['sP'], _ = ctx(rh, cn, c['rec'] + 1800000., c['size'], c['coin'], 5000., 60000., 800.)
    n = len(rh)
    for k in ('bb', 'ba', 'cbb', 'cba'): R[k] = np.full(n, np.nan)
    R['side'] = np.full(n, -1, np.int8); R['jdt'] = np.full(n, np.nan); R['jut'] = np.full(n, np.nan); R['jdn'] = np.zeros(n, bool)
    ef = EXT + 'b_%s.npz' % day; cov = 0
    if os.path.exists(ef):
        z = np.load(ef, allow_pickle=True)
        tokmk = np.array([crc(str(s)) for s in z['tok_mk']]); qtok = z['qtok']; qt = z['qt']; qbb = z['qbb']; qba = z['qba']
        o = np.lexsort((qt, qtok)); qtok = qtok[o]; qt = qt[o]; qbb = qbb[o]; qba = qba[o]
        bnd = np.searchsorted(qtok, np.arange(len(tokmk) + 1)); tside = z['tok_side']
        jd = np.sort(z['jd']); ju = np.sort(z['ju'])
        assert jd.size == 0 or jd.min() > 1e12, 'unidad jd'
        ts = rh - 300.0
        for m in np.unique(R['mk'][cn == 0]):
            ix = np.nonzero((R['mk'] == m) & (cn == 0))[0]; js = np.nonzero(tokmk == m)[0]
            if len(js) == 0: continue
            B = []; A = []
            for j in js:
                a, b = bnd[j], bnd[j + 1]
                if b == a: B.append(np.full(len(ix), np.nan)); A.append(np.full(len(ix), np.nan)); continue
                k = np.searchsorted(qt[a:b], ts[ix], side='right') - 1
                bb_ = np.where(k >= 0, qbb[a:b][np.clip(k, 0, None)], np.nan); ba_ = np.where(k >= 0, qba[a:b][np.clip(k, 0, None)], np.nan)
                bad = bb_ > ba_; bb_[bad] = np.nan; ba_[bad] = np.nan
                B.append(bb_); A.append(ba_)
            B = np.array(B); A = np.array(A)
            d = np.abs(B - R['p'][ix][None, :]); d[np.isnan(d)] = 9
            best = np.argmin(d, axis=0); ok = d[best, np.arange(len(ix))] < 0.05
            for r_, i in enumerate(ix):
                if not ok[r_]: continue
                b = best[r_]; R['bb'][i] = B[b, r_]; R['ba'][i] = A[b, r_]; R['side'][i] = tside[js[b]]
                if len(js) == 2: R['cbb'][i] = B[1 - b, r_]; R['cba'][i] = A[1 - b, r_]
        cov = np.isfinite(R['bb'][cn == 0]).mean() if (cn == 0).any() else 0
        b0 = cn == 0; t_ = ts[b0]
        for nm, arr in (('jdt', jd), ('jut', ju)):
            if arr.size:
                k = np.searchsorted(arr, t_, side='right') - 1
                R[nm][b0] = np.where(k >= 0, t_ - arr[np.clip(k, 0, None)], np.nan)
        if jd.size:
            a = np.searchsorted(jd, rh[b0], side='right'); b = np.searchsorted(jd, rh[b0] + 5000., side='right'); R['jdn'][b0] = b > a
    np.savez_compressed(out, **R)
    json.dump({str(k): v for k, v in hx.items()}, open(OUT + 'hex_%s.json' % day, 'w'))
    print(day, 'ok filas', n, 'BTC', int((cn == 0).sum()), 'cobertura bb BTC %.3f' % cov, 'S800 BTC %.3f' % np.isfinite(R['dA'][cn == 0]).mean(), '%.0f s' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    days = sys.argv[1:] or sorted(f[2:12] for f in os.listdir(r4.OUT) if f.startswith('d_'))
    for d in days:
        try: run(d)
        except Exception as e: print(d, 'ERROR', repr(e), flush=True)
