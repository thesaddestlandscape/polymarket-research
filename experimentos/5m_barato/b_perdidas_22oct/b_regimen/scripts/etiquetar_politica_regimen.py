#!/usr/bin/env python3
"""etiquetar_politica_regimen.py -- ETIQUETADOR PASIVO B-REGIMEN (PREREG_PASIVO_BREGIMEN.md). Solo LECTURA de datalogs; no importa nada del repo; sin red; no toca B.
Uso: python3 -I etiquetar_politica_regimen.py dia YYYY-MM-DD [--out DIR]     (etiqueta ordenes de B y poblacion del dia; idempotente: sobrescribe el fichero del dia de forma atomica)
Dependencias: L1 (etiquetado_B_D), L1b (poblacion/pob_D, hasta 2 dias previos para AR2h), regimen_5m/barras_dia/bars_*.npz (de etiquetar_regimen.py)."""
import os, sys, glob, json, datetime as dt, fcntl
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'; ETQ = DL + '/etiquetado_pasivo_B'; BD = DL + '/regimen_5m/barras_dia'
OUT_DEF = DL + '/b_regimen_pasivo'; THR = 7.7; AR_W = 7200; AR_LAG = 60; AR_NMIN = 200; AR_U = -0.10
def barras(d):
    """Serie continua 1m de los 3 dias d-2..d (1441 puntos por dia con solape) -> {coin: (m0, P)}."""
    day = dt.date.fromisoformat(d); fs = [(day - dt.timedelta(days=k)).isoformat() for k in (2, 1, 0)]; zs = []
    for x in fs:
        p = f'{BD}/bars_{x}.npz'
        if os.path.exists(p): zs.append(np.load(p))
    if not zs: return {}
    m0 = int(zs[0]['m0']); n = int(zs[-1]['m0']) - m0 + 1441; out = {}
    for c in ('ETH', 'SOL', 'XRP', 'BTC', 'BNB', 'DOGE'):
        P = np.full(n, np.nan)
        for z in zs:
            o = int(z['m0']) - m0; a = z[c]; s = np.isfinite(a); P[o:o + 1441][s] = a[s]
        out[c] = (m0, P)
    return out
def z240(B, coin, tmin):
    if coin not in B: return np.full(len(tmin), np.nan)
    m0, Pp = B[coin]; Pp = pd.Series(Pp).ffill(limit=5).values; lp = np.log(Pp); R = np.diff(lp, prepend=np.nan)
    cq = np.concatenate([[0.0], np.cumsum(np.where(np.isfinite(R), R ** 2, 0.0))]); cn = np.concatenate([[0], np.cumsum(np.isfinite(R).astype(int))])
    io = (np.asarray(tmin) - m0).astype(int); ok = (io - 1440 >= 1) & (io < len(lp)); ioc = np.where(ok, io, 1500)
    cnt = cn[ioc + 1] - cn[ioc - 1439]; sq = cq[ioc + 1] - cq[ioc - 1439]; s = np.where(ok & (cnt >= 0.8 * 1440), np.sqrt(sq / np.maximum(cnt, 1)), np.nan)
    z = (lp[np.clip(io, 0, len(lp) - 1)] - lp[np.clip(io - 240, 0, len(lp) - 1)]) / (s * np.sqrt(240)); z[~ok] = np.nan; return z
def poblacion(d):
    L = []
    for k in (2, 1, 0):
        x = (dt.date.fromisoformat(d) - dt.timedelta(days=k)).isoformat(); p = f'{ETQ}/poblacion/pob_{x}.csv.gz'
        if os.path.exists(p): L.append(pd.read_csv(p, usecols=['dia', 'coin', 'lado', 'fin_s', 'ts', 'T_s', 'precio', 'coste', 'pnl', 'gana_lado', 'rpre_bps', 'abs_rpre', 'clase_rpre']))
    if not L: return pd.DataFrame()
    P = pd.concat(L, ignore_index=True); return P[P.pnl.notna() & P.coste.notna() & P.fin_s.notna()].reset_index(drop=True)
def ar2h(POP, t):
    """EV realizado de la poblacion con fin_s en (t-7200, t-60]; NA si n<200 (fail-closed)."""
    if len(POP) == 0: return np.full(len(t), np.nan), np.zeros(len(t), int)
    o = np.argsort(POP.fin_s.values, kind='stable'); fs = POP.fin_s.values[o]; cp = np.concatenate([[0], np.cumsum(POP.pnl.values[o])]); cc = np.concatenate([[0], np.cumsum(POP.coste.values[o])])
    hi = np.searchsorted(fs, np.asarray(t) - AR_LAG, 'right'); lo = np.searchsorted(fs, np.asarray(t) - AR_W, 'right'); n = hi - lo
    return np.where(n >= AR_NMIN, (cp[hi] - cp[lo]) / np.maximum(cc[hi] - cc[lo], 1e-9), np.nan), n
def etiquetar(df, tcol, B, POP):
    df = df.copy(); df['tmin'] = (df.fin_s.values // 60 - 5).astype(np.int64); df['z240'] = np.nan
    for c in df.coin.unique():
        m = (df.coin == c).values; df.loc[m, 'z240'] = z240(B, c, df.tmin.values[m])
    sd = np.where(df.lado == 'YES', 1.0, -1.0); zs = sd * df.z240
    df['reg'] = np.where(df.z240 >= 1, 'ALC', np.where(df.z240 <= -1, 'BAJ', np.where(df.z240.isna(), 'NA', 'LAT')))
    df['aln'] = np.where(zs >= 1, 'ALIGN', np.where(zs <= -1, 'COUNTER', np.where(zs.isna(), 'NA', 'FLAT')))
    ab = df.abs_rpre.values if 'abs_rpre' in df else np.abs(df.rpre_bps.values)   # L1: clase_rpre es SOLO signo (a_favor si x>0); el umbral 7,7 bps va aparte (h_w1 = a_favor y abs>=7,7)
    df['cls'] = np.where(df.clase_rpre.isna() | ~np.isfinite(ab), 'NA', np.where(ab < THR, 'NEU', np.where(df.clase_rpre == 'a_favor', 'CON', 'CONTRA')))
    df['AR2h'], df['AR2h_n'] = ar2h(POP, df[tcol].values)
    na = lambda c: df[c].isna() | (df[c] == 'NA')
    df['F_R0'] = np.where(df.cls == 'NA', np.nan, (df.cls == 'CON').astype(float)); df['F_AR'] = np.where(df.AR2h.isna(), np.nan, (df.AR2h <= AR_U).astype(float))
    df['F_R0AR'] = np.where(df.AR2h.isna() | (df.cls == 'NA'), np.nan, ((df.cls == 'CON') & (df.AR2h <= AR_U)).astype(float))
    df['F_CONAR0'] = np.where(df.AR2h.isna() | (df.cls == 'NA'), np.nan, ((df.cls == 'CON') & (df.AR2h <= 0.0)).astype(float))
    df['F_CT'] = np.where(na('aln') | (df.cls == 'NA'), np.nan, ((df.cls == 'CON') & (df.aln == 'COUNTER')).astype(float))
    df['F_DIR'] = np.where(na('aln'), np.nan, (df.aln == 'COUNTER').astype(float)); df['F_AL'] = np.where(na('aln'), np.nan, (df.aln == 'ALIGN').astype(float)); return df
def main():
    a = sys.argv[1:]
    if len(a) < 2 or a[0] != 'dia': print(__doc__); return 2
    d = a[1]; out = a[a.index('--out') + 1] if '--out' in a else OUT_DEF; os.makedirs(out, exist_ok=True)
    lk = open(out + '/.lock', 'w'); fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    B = barras(d); POP = poblacion(d)
    if not B: print('sin barras para', d); return 3
    res = {}
    fb = f'{ETQ}/etiquetado_B_{d}.csv.gz'
    if os.path.exists(fb):
        Bd = pd.read_csv(fb); Bd = Bd[Bd.unidad == 'orden'].copy(); Bd['tref'] = Bd.t0.astype(float)
        Bd = Bd.rename(columns={'acc': 'acc_ord'}); Bd['fin_s'] = Bd.fin_s.astype(float)
        E = etiquetar(Bd, 'tref', B, POP); tmp = f'{out}/politica_B_{d}.csv.gz.tmp'; E.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, f'{out}/politica_B_{d}.csv.gz'); res['B'] = len(E)
    fp = f'{ETQ}/poblacion/pob_{d}.csv.gz'
    if os.path.exists(fp):
        Pd_ = pd.read_csv(fp); Pd_ = Pd_[Pd_.fin_s.notna() & Pd_.ts.notna()].copy()
        E = etiquetar(Pd_, 'ts', B, POP); tmp = f'{out}/politica_pob_{d}.csv.gz.tmp'; E.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, f'{out}/politica_pob_{d}.csv.gz'); res['pob'] = len(E)
        cov = {k: float(E[k].notna().mean()) for k in ('z240', 'AR2h', 'F_R0')}; res['cobertura_pob'] = cov
    for f_ in glob.glob(out + '/politica_*_*.csv.gz'):
        if os.path.basename(f_).split('_')[-1][:10] < (dt.date.fromisoformat(d) - dt.timedelta(days=45)).isoformat(): os.remove(f_)
    print(json.dumps(res)); return 0
if __name__ == '__main__': sys.exit(main())
