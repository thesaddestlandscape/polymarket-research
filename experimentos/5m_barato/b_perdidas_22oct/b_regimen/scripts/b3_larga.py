#!/usr/bin/env python3
"""b3_larga.py -- ADENDA 2: dependencia del regimen de tendencia (z240) de la brecha CON-CONTRA y de la direccion, via proxy larga (precio de modelo) y ask real P-REAL. EXPLORATORY."""
import sys, os, json
import numpy as np, pandas as pd
DET = '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/detector_regimen'
sys.path.insert(0, DET + '/scripts')
HERE = os.path.dirname(os.path.abspath(__file__)); OUTD = os.path.join(HERE, '..', 'datos'); BAR = '/root/polymarket-research-datalogs/regimen_5m/'
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
RNG = np.random.default_rng(20261027); NB = 3000
def z240_for(coin, tmin, bars):
    m0 = int(bars[coin + '_m0']); Pp = pd.Series(bars[coin + '_P']).ffill(limit=5).values; lp = np.log(Pp); R = np.diff(lp, prepend=np.nan)
    cq = np.concatenate([[0.0], np.cumsum(np.where(np.isfinite(R), R ** 2, 0.0))]); cn = np.concatenate([[0], np.cumsum(np.isfinite(R).astype(int))])
    io = (np.asarray(tmin) - m0).astype(int); ok = (io - 1440 >= 1) & (io < len(lp))
    ioc = np.where(ok, io, 1500); cnt = cn[ioc + 1] - cn[ioc - 1439]; sq = cq[ioc + 1] - cq[ioc - 1439]
    s = np.where(ok & (cnt >= 0.8 * 1440), np.sqrt(sq / np.maximum(cnt, 1)), np.nan)
    z = (lp[np.clip(io, 0, len(lp) - 1)] - lp[np.clip(io - 240, 0, len(lp) - 1)]) / (s * np.sqrt(240)); z[~ok] = np.nan; return z
def classes(U, zcol='z240'):
    U['reg'] = np.where(U[zcol] >= 1, 'ALC', np.where(U[zcol] <= -1, 'BAJ', np.where(U[zcol].isna(), 'NA', 'LAT')))
    zs = U.sd * U[zcol]; U['aln'] = np.where(zs >= 1, 'ALIGN', np.where(zs <= -1, 'COUNTER', np.where(zs.isna(), 'NA', 'FLAT'))); return U
def day_cells(U, key, num, den):
    g = U.groupby(['dia', key, 'cls']).agg(n=(num, 'sum'), d=(den, 'sum')); return g
def boot_stat(U, num, den, fn, nb=NB, unit='dia'):
    """fn(S) -> estadistico, S = dict[(key,cls)] -> (sum_num, sum_den) arrays por unidad; bootstrap de unidades (dias o cierres)."""
    keys = [(a, b) for a in ('reg', 'aln') for b in ('CON', 'CONTRA')]
    units = sorted(U[unit].unique()); ix = {d: i for i, d in enumerate(units)}; k = len(units)
    M = {}
    for a in ('reg', 'aln'):
        g = U.groupby([unit, a, 'cls']).agg(n=(num, 'sum'), d=(den, 'sum'))
        for (u, cell, cl), r in g.iterrows():
            M.setdefault((a, cell, cl), np.zeros((k, 2)))[ix[u]] = (r.n, r.d)
    for cl in ('CON', 'CONTRA'):
        M[('all', 'all', cl)] = sum(M[('reg', c, cl)] for c in ('ALC', 'LAT', 'BAJ', 'NA') if ('reg', c, cl) in M)
    # direccion (todas las unidades, no solo CON/CONTRA)
    for cell in ('ALIGN', 'COUNTER', 'FLAT'):
        v = np.zeros((k, 2)); m = U.aln == cell; g = U[m].groupby(unit).agg(n=(num, 'sum'), d=(den, 'sum'))
        for u, r in g.iterrows(): v[ix[u]] = (r.n, r.d)
        M[('dir', cell, 'ALL')] = v
    def ev(w, key):
        if key not in M: return np.nan
        s = (M[key] * w[:, None]).sum(0); return s[0] / s[1] if s[1] > 0 else np.nan
    def stats(w):
        o = {}
        for a in ('reg', 'aln'):
            for cell in (('ALC', 'LAT', 'BAJ') if a == 'reg' else ('ALIGN', 'FLAT', 'COUNTER')): o[f'D_{cell}'] = ev(w, (a, cell, 'CON')) - ev(w, (a, cell, 'CONTRA'))
        o['D_all'] = ev(w, ('all', 'all', 'CON')) - ev(w, ('all', 'all', 'CONTRA')); o['I_bull'] = o['D_ALC'] - o['D_BAJ']; o['I_aln'] = o['D_ALIGN'] - o['D_COUNTER']
        o['Dir'] = ev(w, ('dir', 'COUNTER', 'ALL')) - ev(w, ('dir', 'ALIGN', 'ALL')); o['EV_CTR'] = ev(w, ('dir', 'COUNTER', 'ALL')); o['EV_ALN'] = ev(w, ('dir', 'ALIGN', 'ALL'))
        o['EV_CON_ALC'] = ev(w, ('reg', 'ALC', 'CON')); o['EV_CONTRA_ALC'] = ev(w, ('reg', 'ALC', 'CONTRA')); o['EV_CON_BAJ'] = ev(w, ('reg', 'BAJ', 'CON')); o['EV_CONTRA_BAJ'] = ev(w, ('reg', 'BAJ', 'CONTRA')); o['EV_CON_LAT'] = ev(w, ('reg', 'LAT', 'CON')); o['EV_CONTRA_LAT'] = ev(w, ('reg', 'LAT', 'CONTRA'))
        return o
    base = stats(np.ones(k)); bs = {kk: [] for kk in base}
    for _ in range(nb):
        w = np.bincount(RNG.integers(0, k, k), minlength=k).astype(float); s = stats(w)
        for kk in bs: bs[kk].append(s[kk])
    res = {}
    for kk in base:
        a = np.array(bs[kk]); lo, hi = np.nanpercentile(a, [5, 95]); res[kk] = (base[kk], lo, hi)
    return res, k
def fmt(res):
    return ' | '.join(f'{k}={v[0]:+.3f}[{v[1]:+.3f},{v[2]:+.3f}]' for k, v in res.items() if k in ('D_all', 'D_ALC', 'D_LAT', 'D_BAJ', 'I_bull', 'D_ALIGN', 'D_FLAT', 'D_COUNTER', 'I_aln', 'Dir'))
def nn(U): return {c: int((U.reg == c).sum()) for c in ('ALC', 'LAT', 'BAJ')} | {c: int((U.aln == c).sum()) for c in ('ALIGN', 'FLAT', 'COUNTER')}
# ---------------- L: proxy larga
P('#### b3-L proxy larga (precio de MODELO; e = win - q; EV = sum e / sum q); IC90 por bootstrap de DIAS (liberal)')
SAMP = {'2025 (349 d, proxy)': ('panel_y2025', 'barras_y2025', 'win_proxy'), 'backfill (129 d, proxy)': ('panel_backfill', 'barras_backfill', 'win_proxy'), 'dic_ene (40 d, oficial)': ('panel_dic_ene', 'barras_dic_ene', 'win_oficial')}
SIGN = {}
for nom, (pan, bar, wcol) in SAMP.items():
    D = pd.read_csv(f'{DET}/datos/{pan}.csv.gz', usecols=['coin', 'tmin', 'T', 'q', 'lado_up', 'win_proxy', 'rpre', 'dia'] + (['win_oficial'] if wcol == 'win_oficial' else []))
    bars = np.load(BAR + bar + '.npz')
    for grp, coins in (('ETH/SOL/XRP', ['ETH', 'SOL', 'XRP']), ('BTC', ['BTC'])):
        U = D[D.coin.isin(coins) & (D['T'] == 180)].copy(); U = U[U[wcol].notna()]
        U['sd'] = np.where(U.lado_up, 1.0, -1.0); U['cls'] = np.where(U.rpre.abs() < 7.7, 'NEU', np.where(np.sign(U.rpre) == U.sd, 'CON', 'CONTRA')); U['e'] = U[wcol] - U.q
        U['z240'] = np.nan
        for c in coins:
            m = (U.coin == c).values
            if m.any(): U.loc[m, 'z240'] = z240_for(c, U.tmin.values[m], bars)
        U = classes(U); U = U[U.reg != 'NA']
        res, k = boot_stat(U, 'e', 'q', None); SIGN[(nom, grp)] = res
        P(f'{nom} {grp}: n={len(U)} dias={k} celdas {nn(U)}'); P('   ' + fmt(res)); P('   EV(CON/CONTRA) ALC ' + f'{res["EV_CON_ALC"][0]:+.3f}/{res["EV_CONTRA_ALC"][0]:+.3f} LAT {res["EV_CON_LAT"][0]:+.3f}/{res["EV_CONTRA_LAT"][0]:+.3f} BAJ {res["EV_CON_BAJ"][0]:+.3f}/{res["EV_CONTRA_BAJ"][0]:+.3f} | EV COUNTER {res["EV_CTR"][0]:+.3f} ALIGN {res["EV_ALN"][0]:+.3f}')
        if nom.startswith('2025') and grp == 'ETH/SOL/XRP':
            U['mes'] = pd.to_datetime(U.dia * 86400, unit='s').dt.strftime('%Y-%m'); P('   por mes (Dir=EV COUNTER-ALIGN | I_bull | I_aln):')
            for mth, Ux in U.groupby('mes'):
                rr, kk = boot_stat(Ux, 'e', 'q', None, nb=300); P(f'     {mth}: dias {kk} Dir {rr["Dir"][0]:+.3f} I_bull {rr["I_bull"][0]:+.3f} I_aln {rr["I_aln"][0]:+.3f} D_all {rr["D_all"][0]:+.3f}')
P('\nSIGNOS (ETH/SOL/XRP) 2025 / backfill / dic_ene: ' + ' ; '.join(f'{st}: ' + '/'.join(f'{SIGN[(n_, "ETH/SOL/XRP")][st][0]:+.3f}' for n_ in SAMP) for st in ('D_all', 'I_bull', 'I_aln', 'Dir')))
# ---------------- R: ask real
P('\n#### b3-R ask real P-REAL 05-21 Oct (U1 ask [0,10-0,30), T=180 lag 250, fee 0,07)')
import preal_analisis as PA
desen = json.load(open('/root/polymarket-research-datalogs/preal/desenl_cache.json'))
W = pd.read_csv(DET + '/datos/ventanas_bookticker.csv.gz', usecols=['coin', 'tmin', 'rpre'])
import glob
et = [pd.read_csv(f, usecols=['coin', 'tmin', 'rpre']) for f in sorted(glob.glob(BAR + 'etiquetas/regimen_*.csv.gz'))]
W = pd.concat([W] + et, ignore_index=True).drop_duplicates(['coin', 'tmin'], keep='first').rename(columns={'rpre': 'rpre_bar'})
X, dias = PA.carga(); Y = PA.prep(PA.largo(X, 180, 250), W, desen)
bars = np.load(BAR + 'barras_bookticker.npz')
def U1(coins):
    p, c = PA.precio_cols(Y, 'ask'); m = Y.coin.isin(coins) & Y.vivo & ~Y.cruz & Y.ask.notna() & Y.ask.ge(0.10) & Y.ask.lt(0.30) & Y.gana.notna() & Y.cls.isin(['CON', 'CONTRA', 'NEU']) & p.notna()
    U = Y[m].copy(); U['cst'] = c[m]; U['pnl'] = U.gana - U.cst; U['sd'] = U.sgn; U['z240'] = np.nan
    for cn in coins:
        mm = (U.coin == cn).values
        if mm.any(): U.loc[mm, 'z240'] = z240_for(cn, U.tmin.values[mm], bars)
    U = classes(U); return U[U.reg != 'NA']
for grp, coins in (('ETH/SOL/XRP', ['ETH', 'SOL', 'XRP']), ('BTC/BNB/DOGE', ['BTC', 'BNB', 'DOGE'])):
    U = U1(coins)
    for unit in ('cierre', 'dia'):
        res, k = boot_stat(U, 'pnl', 'cst', None, unit=unit)
        P(f'{grp} (IC90 por {unit}, {k} unidades) n={len(U)} celdas {nn(U)}'); P('   ' + fmt(res)); P('   EV(CON/CONTRA) ALC ' + f'{res["EV_CON_ALC"][0]:+.3f}/{res["EV_CONTRA_ALC"][0]:+.3f} LAT {res["EV_CON_LAT"][0]:+.3f}/{res["EV_CONTRA_LAT"][0]:+.3f} BAJ {res["EV_CON_BAJ"][0]:+.3f}/{res["EV_CONTRA_BAJ"][0]:+.3f} | EV COUNTER {res["EV_CTR"][0]:+.3f} ALIGN {res["EV_ALN"][0]:+.3f}')
    t = U.groupby(['reg', 'cls']).agg(n=('pnl', 'size'), dias=('dia', 'nunique')); P(t.unstack().to_string())
open(OUTD + '/b3_resultados.txt', 'w').write('\n'.join(OUT))
