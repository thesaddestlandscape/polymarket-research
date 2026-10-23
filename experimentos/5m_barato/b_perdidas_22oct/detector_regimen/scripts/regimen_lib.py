#!/usr/bin/env python3
"""regimen_lib.py - detector de regimen CAUSAL (PREREG_RTEND sha 0cbe5e44...). Solo numpy/pandas. Sin red, sin escritura salvo donde el llamador diga.
Entrada: P[coin] = (m0, arr) con arr[k] = cierre de la barra 1m que TERMINA en el minuto (m0+k) (minutos desde epoch); NaN = missing."""
import numpy as np, pandas as pd, math
COH_COINS = ['BTC', 'ETH', 'SOL', 'XRP']
THR_RPRE = 7.7
def Phi(x): return 0.5 * (1 + np.vectorize(math.erf)(np.asarray(x, float) / math.sqrt(2)))

def _roll(a, w):  # suma de a[i-w+1..i] (a sin NaN)
    c = np.concatenate([[0.0], np.cumsum(a)]); out = np.full(len(a), np.nan); out[w - 1:] = c[w:] - c[:-w]; return out

def base_series(m0, P):
    n = len(P); lp = np.log(P); R = np.full(n, np.nan); R[1:] = lp[1:] - lp[:-1]
    ok = np.isfinite(R); R0 = np.where(ok, R, 0.0)
    return dict(m0=m0, P=P, lp=lp, R=R, R0=R0, ok=ok, n=n, cabs=np.concatenate([[0.0], np.cumsum(np.abs(R0))]),
                cq=np.concatenate([[0.0], np.cumsum(R0 ** 2)]), cn=np.concatenate([[0], np.cumsum(ok.astype(np.int64))]))

def rms(B, i, w):  # sqrt(media R^2) en las w barras que acaban en i (indices arrays); NaN si <0.8w validas
    i = np.asarray(i); lo = i - w + 1; good = lo >= 1
    lo2 = np.where(good, lo, 1)
    cnt = B['cn'][i + 1] - B['cn'][lo2]; sq = B['cq'][i + 1] - B['cq'][lo2]
    v = np.sqrt(np.where(cnt > 0, sq / np.maximum(cnt, 1), np.nan)); v[(~good) | (cnt < 0.8 * w)] = np.nan; return v

def lp_at(B, i):
    i = np.asarray(i); out = np.full(len(i), np.nan); g = (i >= 0) & (i < B['n']); out[g] = B['lp'][i[g]]; return out

def features_open(B, io):
    """Rasgos a la apertura (indice io = minuto de apertura). Todo con barras terminadas <= io."""
    io = np.asarray(io); f = {}
    f['rpre'] = (lp_at(B, io) - lp_at(B, io - 15)) * 1e4
    f['r60'] = (lp_at(B, io) - lp_at(B, io - 60)) * 1e4
    lo = io - 59; good = lo >= 1; lo2 = np.where(good, lo, 1)
    path = B['cabs'][io + 1] - B['cabs'][lo2]; cnt = B['cn'][io + 1] - B['cn'][lo2]
    net = np.abs(lp_at(B, io) - lp_at(B, io - 60))
    er = np.where(path > 0, net / np.where(path > 0, path, 1), np.nan); er[(~good) | (cnt < 48)] = np.nan; f['ER60'] = er
    # VR240: r5 no solapados alineados a io
    K = 48; idx = io[:, None] - 5 * np.arange(K)[None, :]
    r5 = lp_at(B, idx.ravel()) - lp_at(B, (idx - 5).ravel()); r5 = r5.reshape(-1, K)
    ok5 = np.isfinite(r5).sum(1) >= 40
    m5 = np.nanmean(r5 ** 2, axis=1) if len(io) else np.array([])
    m1 = rms(B, io, 240) ** 2
    f['VR240'] = np.where(ok5, m5 / (5 * m1), np.nan)
    s60 = rms(B, io, 60); f['s60'] = s60
    s24 = rms(B, io, 1440); f['VOLR'] = s60 / s24
    # tendencia del dia UTC: desde 00:00 UTC
    mins_day = (B['m0'] + io) % 1440; i0 = io - mins_day
    dt = (lp_at(B, io) - lp_at(B, i0)) / (rms(B, io, 60) * np.sqrt(np.maximum(mins_day, 1)))
    dt[mins_day < 120] = np.nan; f['DAYT'] = dt
    return f

def add_classes(df, hist_days=14):
    """df: columnas coin, dia (int: minuto_epoch//1440), ER60, VR240 (una fila por apertura), ER_dia_prev. Anade med_ER(14d previos), R, D."""
    df = df.copy(); df['med_ER'] = np.nan
    for c, g in df.groupby('coin'):
        days = sorted(g.dia.unique())
        for d in days:
            h = g[(g.dia < d) & (g.dia >= d - hist_days)].ER60.dropna()
            if len(h) >= 5 * 288 * 0.8 and len(set(g[(g.dia < d) & (g.dia >= d - hist_days)].dia)) >= 5:
                df.loc[g.index[g.dia == d], 'med_ER'] = h.median()
    R = np.full(len(df), 'NA', dtype=object); ok = df.med_ER.notna() & df.ER60.notna() & df.VR240.notna()
    t = (df.ER60 >= df.med_ER) & (df.VR240 >= 1); r = (df.ER60 < df.med_ER) & (df.VR240 < 1)
    R[(ok & t).values] = 'TREND'; R[(ok & r).values] = 'REVERT'; R[(ok & ~t & ~r).values] = 'MIXTO'; df['R'] = R
    return df

def er_dia_prev_table(B, m_ini_dia_list):
    """ER del dia UTC (barras 15m): para cada dia-int d (minuto_epoch//1440) -> |net|/sum|d15| ; NaN si <90 % barras."""
    out = {}
    for d in m_ini_dia_list:
        i0 = d * 1440 - B['m0']; idx = i0 + 15 * np.arange(97)
        if idx[0] < 0 or idx[-1] >= B['n']: out[d] = np.nan; continue
        lp = B['lp'][idx]
        if np.isfinite(lp).sum() < 90: out[d] = np.nan; continue
        l2 = lp[np.isfinite(lp)]; path = np.abs(np.diff(l2)).sum(); out[d] = abs(l2[-1] - l2[0]) / path if path > 0 else np.nan
    return out

def d_class(erd, hist_days=14):
    """erd: dict dia->ER_dia. Devuelve dict dia -> 'TENDENCIA'/'RANGO'/'NA' con la mediana de los 14 dias ANTERIORES (>=5 disponibles) comparada con ER del dia anterior (dia-1)."""
    out = {}
    for d in erd:
        prev = erd.get(d - 1, np.nan)
        hist = [erd[k] for k in range(d - 1 - hist_days, d - 1) if k in erd and np.isfinite(erd[k])]
        out[d] = 'NA' if (not np.isfinite(prev) or len(hist) < 5) else ('TENDENCIA' if prev >= np.median(hist) else 'RANGO')
    return out
