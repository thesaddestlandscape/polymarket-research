#!/usr/bin/env python3
"""dfuerte_lib.py - rasgos causales de ventana 5m (PREREG_DFUERTE sha 5efad7c6...). Mismas funciones para analisis y etiquetador forward.
Entrada Z[coin] = (m0, X) con X (n,6) = [close,high,low,vol,tbv,ntr] indexado por minuto en que TERMINA la barra (NaN = missing)."""
import sys, os, numpy as np, pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'scripts'))
import regimen_lib as L
from scipy.special import ndtr
COH = ['BTC', 'ETH', 'SOL', 'XRP']; ALLC = ['BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE']
KS = [5, 15, 30, 60, 120, 240, 720, 1440]
FEATS = (['z%d' % k for k in KS] + ['az15'] +                                                     # F1
         ['ER15', 'ER60', 'ER240', 'VR240', 'VR15_1440', 'hurst', 'ac1', 'ac5'] +                 # F2
         ['VOLR', 'rv15_60', 'rv5_60', 'lvolref', 'lvol', 'pk_ratio', 'lastrange'] +              # F3
         ['skew60', 'skew240', 'kurt240', 'maxj60', 'jumpr', 'n3s', 'bigjump'] +                 # F4
         ['imb5', 'imb15', 'imb60', 'vol15', 'vol5', 'ntr15', 'tsize'] +                          # F5
         ['coh_z15', 'coh_frac', 'btc_z15', 'coh_disp', 'idio_z15', 'coh_z60'] +                  # F6
         ['hsin', 'hcos', 'dsin', 'dcos', 'usa', 'mday'] + ['c_' + c for c in ALLC] +             # F7
         ['dcon24', 'dopp24', 'pos24', 'pos4', 'posday', 'dcon_pd', 'dopp_pd', 'since_ext'])      # F8
FAM = {'F1': FEATS[0:9], 'F2': FEATS[9:17], 'F3': FEATS[17:24], 'F4': FEATS[24:31], 'F5': FEATS[31:38], 'F6': FEATS[38:44],
       'F7': FEATS[44:50] + ['c_' + c for c in ALLC], 'F8': FEATS[56:64]}
assert FEATS[56] == 'dcon24' and len(FEATS) == 64, (FEATS[56], len(FEATS))

def csum(a): return np.concatenate([[0.0], np.cumsum(np.nan_to_num(a))])
def wsum(cs, io, W): return cs[io + 1] - cs[io + 1 - W]
def lpa(B, i): return L.lp_at(B, i)

def msq_ratio(B, io, m, W):  # var de retornos m-pasos / (m * var 1m) sobre las W barras que acaban en io; y la media de d_m^2
    lp = B['lp']; d = np.full(len(lp), np.nan); d[m:] = lp[m:] - lp[:-m]; d2 = d ** 2; ok = np.isfinite(d2)
    cs = csum(d2); cn = np.concatenate([[0], np.cumsum(ok)]); s = wsum(cs, io, W); n = wsum(cn.astype(float), io, W)
    return np.where(n > 0.7 * W, s / np.maximum(n, 1), np.nan)

def prod_lag(a, lag):
    p = np.full(len(a), np.nan); p[lag:] = a[lag:] * a[:-lag]; return csum(p)

def chunks(n, c=6000):
    for s in range(0, n, c): yield slice(s, min(n, s + c))

def own_features(c, m0, X, tm):
    """Rasgos de la moneda c en las aperturas tm (minutos epoch). Devuelve DataFrame (sin orientar ni cross-coin)."""
    P = X[:, 0]; B = L.base_series(m0, P); io = tm - m0; n = len(io)
    f = L.features_open(B, io); s60 = f['s60']; o = np.sign(f['rpre'])
    out = {'coin': np.full(n, c), 'tmin': tm, 'rpre': f['rpre'], 'r60': f['r60'], 'o': o, 's60': s60, 'ER60': f['ER60'], 'VR240': f['VR240'], 'VOLR': f['VOLR'], 'DAYT': f['DAYT']}
    lp0 = lpa(B, io)
    for k in KS: out['z%d' % k] = np.clip(o * (lp0 - lpa(B, io - k)) / (s60 * np.sqrt(k)), -8, 8)
    out['az15'] = np.abs(out['z15'])
    def ER(w):
        lo = io - w + 1; path = B['cabs'][io + 1] - B['cabs'][lo]; cnt = B['cn'][io + 1] - B['cn'][lo]; net = np.abs(lp0 - lpa(B, io - w))
        e = np.where(path > 0, net / np.where(path > 0, path, 1), np.nan); e[cnt < 0.8 * w] = np.nan; return e
    out['ER15'] = ER(15); out['ER240'] = ER(240)
    out['VR15_1440'] = msq_ratio(B, io, 15, 1440) / (15 * L.rms(B, io, 1440) ** 2)
    ms = [1, 2, 4, 8, 16, 32]; lv = np.stack([np.log(msq_ratio(B, io, m, 720)) for m in ms], 1); lm = np.log(ms)
    lmc = lm - lm.mean(); out['hurst'] = np.where(np.isfinite(lv).all(1), (lv - np.nanmean(lv, 1, keepdims=True)) @ lmc / (lmc @ lmc) / 2, np.nan)
    R0 = B['R0']; r2 = R0 ** 2; c1 = prod_lag(R0, 1); c2 = csum(r2)
    out['ac1'] = wsum(c1, io, 240) / np.maximum(wsum(c2, io, 240), 1e-30)
    d5 = np.full(len(R0), np.nan); d5[5:] = B['lp'][5:] - B['lp'][:-5]; d5z = np.nan_to_num(d5)
    out['ac5'] = wsum(prod_lag(d5z, 5), io, 1440) / np.maximum(wsum(csum(d5z ** 2), io, 1440), 1e-30)
    # F3
    s15 = L.rms(B, io, 15); s5 = L.rms(B, io, 5); out['rv15_60'] = (s15 / s60) ** 2; out['rv5_60'] = (s5 / s60) ** 2; out['lvol'] = np.log(s60 * 1e4)
    H = X[:, 1]; Lw = X[:, 2]; hl = np.log(H / Lw); hl2 = hl ** 2
    pk15 = np.sqrt(wsum(csum(hl2), io, 15) / 15 / (4 * np.log(2))); out['pk_ratio'] = pk15 / s15
    hl_last = np.where((io >= 0) & (io < len(hl)), hl[np.clip(io, 0, len(hl) - 1)], np.nan); out['lastrange'] = hl_last / s60
    # F4/F8 con ventanas deslizantes por trozos
    keys = ['skew60', 'skew240', 'kurt240', 'maxj60', 'jumpr', 'n3s', 'bigjump', 'dcon24', 'dopp24', 'pos24', 'pos4', 'since_ext']
    for k in keys: out[k] = np.full(n, np.nan)
    s240 = L.rms(B, io, 240); R = B['R']; lp = B['lp']
    for sl in chunks(n):
        ii = io[sl]; oo = o[sl]
        r60 = R[ii[:, None] - np.arange(60)[None, :]]; r240 = R[ii[:, None] - np.arange(240)[None, :]]
        for nm, r, mw in (('60', r60, 48), ('240', r240, 190)):
            ok = np.isfinite(r).sum(1) >= mw; m2 = np.nanmean(r ** 2, 1); m3 = np.nanmean(r ** 3, 1)
            sk = oo * m3 / m2 ** 1.5; sk[~ok] = np.nan; out['skew' + nm][sl] = sk
            if nm == '240': k4 = np.nanmean(r ** 4, 1) / m2 ** 2; k4[~ok] = np.nan; out['kurt240'][sl] = k4
        ar = np.abs(r60); out['maxj60'][sl] = np.nanmax(np.where(np.isfinite(ar), ar, -1), 1) / s240[sl]
        rv = np.nansum(r60 ** 2, 1); bv = (np.pi / 2) * np.nansum(np.abs(r60[:, 1:]) * np.abs(r60[:, :-1]), 1)
        out['jumpr'][sl] = np.maximum(0, 1 - bv / np.maximum(rv, 1e-30)); out['n3s'][sl] = np.nansum(ar > 3 * s240[sl][:, None], 1)
        am = np.nanargmax(np.where(np.isfinite(ar), ar, -1), 1); out['bigjump'][sl] = oo * r60[np.arange(len(ii)), am] / s240[sl]
        l24 = lp[ii[:, None] - np.arange(1440)[None, :]]; mx = np.nanmax(l24, 1); mn = np.nanmin(l24, 1); l0 = lp[ii]; sg = s60[sl]
        dcon = np.where(oo > 0, mx - l0, l0 - mn) / sg; dopp = np.where(oo > 0, l0 - mn, mx - l0) / sg
        out['dcon24'][sl] = np.log1p(np.clip(dcon, 0, 1e3)); out['dopp24'][sl] = np.log1p(np.clip(dopp, 0, 1e3))
        pos = (l0 - mn) / np.maximum(mx - mn, 1e-12); out['pos24'][sl] = np.where(oo > 0, pos, 1 - pos)
        l4 = l24[:, :240]; mx4 = np.nanmax(l4, 1); mn4 = np.nanmin(l4, 1); p4 = (l0 - mn4) / np.maximum(mx4 - mn4, 1e-12); out['pos4'][sl] = np.where(oo > 0, p4, 1 - p4)
        ext = np.where(oo[:, None] > 0, l24, -l24); out['since_ext'][sl] = np.nanargmax(np.where(np.isfinite(ext), ext, -1e9), 1) / 1440.0
    # dia UTC en curso y dia previo (desde cierres)
    mday = (m0 + io) % 1440; out['mday'] = mday / 1440.0; i0 = io - mday
    dayc = pd.Series(P); dk = pd.Series((m0 + np.arange(len(P))) // 1440)
    g = dayc.groupby(dk.values); cmx = g.cummax().values; cmn = g.cummin().values
    dmx = g.max(); dmn = g.min(); day_i = (m0 + io) // 1440
    mxd = cmx[io]; mnd = cmn[io]; posd = (P[io] - mnd) / np.maximum(mxd - mnd, 1e-12); out['posday'] = np.where(mday < 60, np.nan, np.where(o > 0, posd, 1 - posd))
    pmx = dmx.reindex(day_i - 1).values; pmn = dmn.reindex(day_i - 1).values; l0 = lp0
    dc = np.where(o > 0, np.log(pmx) - l0, l0 - np.log(pmn)) / s60; do_ = np.where(o > 0, l0 - np.log(pmn), np.log(pmx) - l0) / s60
    out['dcon_pd'] = np.log1p(np.clip(dc, 0, 1e3)); out['dopp_pd'] = np.log1p(np.clip(do_, 0, 1e3))
    # F5 flujo
    vol, tbv, ntr = X[:, 3], X[:, 4], X[:, 5]; cv, ct, cn_ = csum(vol), csum(tbv), csum(ntr)
    for k in (5, 15, 60):
        sv = wsum(cv, io, k); out['imb%d' % k] = o * (2 * wsum(ct, io, k) - sv) / np.maximum(sv, 1e-12)
    v1440 = wsum(cv, io, 1440); out['vol15'] = wsum(cv, io, 15) / np.maximum(v1440 / 96, 1e-12); out['vol5'] = wsum(cv, io, 5) / np.maximum(v1440 / 288, 1e-12)
    n1440 = wsum(cn_, io, 1440); out['ntr15'] = wsum(cn_, io, 15) / np.maximum(n1440 / 96, 1e-12)
    out['tsize'] = (wsum(cv, io, 15) / np.maximum(wsum(cn_, io, 15), 1)) / np.maximum(v1440 / np.maximum(n1440, 1), 1e-12)
    # tiempo
    hr = ((tm % 1440) / 60.0); dow = ((tm // 1440 + 3) % 7)   # epoch day 0 = jueves -> lunes=0
    out['hsin'] = np.sin(2 * np.pi * hr / 24); out['hcos'] = np.cos(2 * np.pi * hr / 24); out['dsin'] = np.sin(2 * np.pi * dow / 7); out['dcos'] = np.cos(2 * np.pi * dow / 7)
    out['usa'] = ((hr >= 13.5) & (hr < 20)).astype(float)
    for cc in ALLC: out['c_' + cc] = np.full(n, float(cc == c))
    D = pd.DataFrame(out)
    # vol de referencia 14 d previos (rolling temporal)
    idx = pd.to_datetime(tm * 60, unit='s'); ls = pd.Series(np.log(s60), index=idx)
    ref = ls.rolling('14D', closed='left', min_periods=1152).median().values; D['lvolref'] = np.log(s60) - ref
    er = pd.Series(f['ER60'], index=idx); D['med_ER'] = er.rolling('14D', closed='left', min_periods=1152).median().values
    ok = np.isfinite(D.med_ER) & np.isfinite(D.ER60) & np.isfinite(D.VR240)
    t = (D.ER60 >= D.med_ER) & (D.VR240 >= 1); r = (D.ER60 < D.med_ER) & (D.VR240 < 1)
    D['R'] = np.where(ok, np.where(t, 'TREND', np.where(r, 'REVERT', 'MIXTO')), 'NA')
    D['z60raw'] = o * 0 + (lp0 - lpa(B, io - 60)) / (s60 * np.sqrt(60))   # sin orientar, para cross-coin
    D['z15raw'] = (lp0 - lpa(B, io - 15)) / (s60 * np.sqrt(15)); D['dia'] = tm // 1440
    # unidades T=180/120
    for T in (180, 120):
        iT = io + T // 60; ret = lpa(B, iT) - lp0; sT = L.rms(B, iT, 60); m = (300 - T) / 60; zz = np.abs(ret) / (sT * np.sqrt(m))
        D['q%d' % T] = ndtr(-zz); D['ret%d' % T] = ret * 1e4
        fin = lpa(B, io + 5) - lp0; up_side = ret < 0
        win = np.where(up_side, fin >= 0, fin < 0).astype(float); win[~np.isfinite(fin) | ~np.isfinite(ret)] = np.nan; D['win%d' % T] = win; D['up%d' % T] = up_side
    return D

def grid(Z, coins, warm=1500):
    lo = max(Z[c][0] for c in coins) + warm; hi = min(Z[c][0] + len(Z[c][1]) for c in coins) - 8
    return np.arange((lo + 4) // 5 * 5, hi, 5)

def all_features(Z, coins, tm=None):
    tm = grid(Z, coins) if tm is None else tm
    Ds = [own_features(c, Z[c][0], Z[c][1], tm) for c in coins]
    # cross-coin: sobre COH presentes en Z
    cc = [c for c in COH if c in coins]; zz15 = {d.coin.iloc[0]: d.z15raw.values for d in Ds}; zz60 = {d.coin.iloc[0]: d.z60raw.values for d in Ds}
    for D in Ds:
        c = D.coin.iloc[0]; o = D.o.values; oth = [x for x in cc if x != c]
        m15 = np.nanmean([zz15[x] for x in oth], 0); m60 = np.nanmean([zz60[x] for x in oth], 0)
        D['coh_z15'] = o * m15; D['coh_z60'] = o * m60; D['idio_z15'] = o * (zz15[c] - m15)
        D['coh_frac'] = np.nanmean([(np.sign(zz60[x]) == o).astype(float) for x in oth], 0)
        D['btc_z15'] = o * (zz15['BTC'] if (c != 'BTC' and 'BTC' in zz15) else m15)
        D['coh_disp'] = np.nanstd([zz15[x] for x in cc], 0)
    return pd.concat(Ds, ignore_index=True)

def to_units(W, Tsel=180, thr=7.7):
    """Unidades longshot CON/CONTRA a partir de la tabla de ventanas."""
    q = W['q%d' % Tsel]; ret = W['ret%d' % Tsel]; win = W['win%d' % Tsel]; up = W['up%d' % Tsel].astype(bool)
    m = (q >= 0.10) & (q < 0.30) & win.notna() & W.rpre.notna() & (ret != 0) & (W.rpre.abs() >= thr)
    U = W[m].copy(); U['T'] = Tsel; U['q'] = q[m]; U['win'] = win[m]; sd = np.where(up[m], 1.0, -1.0)
    U['con'] = (np.sign(U.rpre.values) == sd).astype(int); U['pcon'] = np.where(U.con == 1, U.q, 1 - U.q); U['y'] = np.where(U.con == 1, U.win, 1 - U.win)
    return U
