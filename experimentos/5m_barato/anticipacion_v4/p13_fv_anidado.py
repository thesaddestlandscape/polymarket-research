#!/usr/bin/env python3
"""Paso 13: INFORMACION que los rivales podrian usar y nosotros no: el 15m es suelo de P(5m s) mas el 'excedente' P(ref5 <= P_C < ref15) que depende de |gap| entre TWAP60 oficiales,
spot Binance (recepcion) y sigma. FV5 = bid15 + Phi(z/sT) - Phi((z-|gap|)/sT), z = distancia spot-ref5 (bp) orientada al lado s, sT = sigma300*sqrt(T/300), sigma = std movil 2 h causal de retornos a 300 s.
edge2 = FV5 - ask5 - fee. VARIANTES FIJADAS ANTES: E0 edge2>=0 ; E1 >=0,02 ; E2 >=0,05 ; E3 edge2>=0,02 & ask5>=0,50. 1a entrada por cierre (instantes de feat_D, m>=-0,10), limite=ask5, +215 ms nivel 1. Bonferroni x4."""
import sys, glob, numpy as np, pandas as pd
from math import erf, sqrt
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_lo/r3'.replace('lo_lo', 'lo_bueno'))
from simlib import binance
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
fee = lambda p: 0.07 * p * (1 - p)
Phi = np.vectorize(lambda x: 0.5 * (1 + erf(x / sqrt(2))))
def refs(D):
    f = glob.glob(f'/root/polymarket-research/data/prices/polybolt_{D}.csv*')[0]
    d = pd.read_csv(f, usecols=['asset', 'canal', 'value', 'event_ts_ms', 'source']); d = d[(d.asset == 'BTC') & (d.canal == 'twap60') & (d.source == 'chainlink')].drop_duplicates('event_ts_ms')
    return dict(zip(d.event_ts_ms // 1000, d.value))
OUT = []
for f in sorted(glob.glob(O + 'feat_*.csv.gz')):
    D = f[-17:-7]; F = pd.read_csv(f).drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
    if not len(F): continue
    ref = {}
    for dd in (pd.Timestamp(D) - pd.Timedelta(days=1), pd.Timestamp(D), pd.Timestamp(D) + pd.Timedelta(days=1)):
        try: ref.update(refs(dd.strftime('%Y-%m-%d')))
        except Exception: pass
    B = binance(D); g = np.arange(B['rx'][0], B['rx'][-1], 10000); p = pd.Series(B['prx'][np.searchsorted(B['rx'], g, side='right') - 1])
    r300 = np.log(p.shift(-30) / p) * 1e4; known = r300.shift(30)              # r300 conocido en i = retorno de [i-60 s... i-30 pasos] -> causal
    sig = known.rolling(720, min_periods=100).std().values; sig = np.where(np.isnan(sig), np.nanstd(r300), sig)
    F['ref5'] = (F.cierre - 300).map(ref); F['ref15'] = (F.cierre - 900).map(ref); F = F.dropna(subset=['ref5', 'ref15']).copy()
    t = F.t.values.astype(np.int64)
    S = B['prx'][np.clip(np.searchsorted(B['rx'], t, side='right') - 1, 0, len(B['rx']) - 1)]
    sgn = np.where(F.lado == 'Up', 1, -1); F['z'] = sgn * (S / F.ref5.values - 1) * 1e4; F['gabs'] = np.abs(F.ref5 / F.ref15 - 1) * 1e4
    sg = sig[np.clip((t - g[0]) // 10000, 0, len(sig) - 1).astype(int)]; Tsec = np.clip(F.cierre.values - t / 1000, 1, None)
    sT = np.maximum(sg * np.sqrt(Tsec / 300), 0.5)
    F['fv5'] = F.bid15 + Phi(F.z.values / sT) - Phi((F.z.values - F.gabs.values) / sT)
    F['edge2'] = F.fv5 - F.ask5 - fee(F.ask5); OUT.append(F); print(D, len(F), flush=True)
F = pd.concat(OUT); F['gana'] = F.gana.astype(bool)
F.to_pickle(O + 'p13_feat.pkl')
rng = np.random.default_rng(8)
def prim(mask):
    d = F[mask].groupby('cierre').head(1).copy(); d['ejec'] = d.acc_e215 > 0; d['p'] = d.ask_e215
    d['coste'] = np.where(d.ejec, d.acc_e215 * (d.p + fee(d.p)), 0.0); d['pnl'] = np.where(d.ejec, d.acc_e215 * (d.gana.astype(float) - d.p - fee(d.p)), 0.0); return d
def boot(x, key, q):
    g_ = x.groupby(key)[['pnl', 'coste']].sum().values
    if len(g_) < 3: return (np.nan, np.nan)
    ix = rng.integers(0, len(g_), (4000, len(g_))); r = g_[ix, 0].sum(1) / np.maximum(g_[ix, 1].sum(1), 1e-9); return tuple(np.percentile(r, [q, 100 - q]).round(3))
def rep(x, nom):
    e = x[x.ejec]
    if e.coste.sum() <= 0: print(f'  {nom:12s} n=0'); return
    by = e.groupby('dia')[['pnl', 'coste']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = e[~e.dia.isin(top)]
    print(f'  {nom:12s} disp={len(x):3d} ejec={len(e):3d} dias={e.dia.nunique():2d} coste={e.coste.sum():6.1f} EV={e.pnl.sum()/e.coste.sum():+.3f} acierto={e.gana.mean():.2f} precio={e.p.mean():.2f} IC90cierre={boot(e,"cierre",5)} Bonf4inf={boot(e,"cierre",1.25)[0]} IC90dia={boot(e,"dia",5)} sin2mejores={(y.pnl.sum()/y.coste.sum() if y.coste.sum()>0 else np.nan):+.3f} dias+={(by.pnl>0).sum()}/{len(by)}')
print('\nsurplus medio (fv5-bid15) P10/50/90:', np.percentile(F.fv5 - F.bid15, [10, 50, 90]).round(3), '| sigma300 usado P50', round(float(np.median(F.fv5)), 3))
V = {'E0 edge2>=0': F.edge2 >= 0, 'E1 edge2>=.02': F.edge2 >= 0.02, 'E2 edge2>=.05': F.edge2 >= 0.05, 'E3 edge2>=.02&ask>=.5': (F.edge2 >= 0.02) & (F.ask5 >= 0.5), 'REF V4 m>=.05': F.m >= 0.05}
for k, mk in V.items():
    d = prim(mk & ~F.edge2.isna()); print('---', k); rep(d, 'TODO'); rep(d[d.dia <= '2026-10-12'], 'DESC 06-12'); rep(d[d.dia >= '2026-10-13'], 'TEST 13-18')
