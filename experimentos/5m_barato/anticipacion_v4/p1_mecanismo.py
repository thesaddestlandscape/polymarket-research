#!/usr/bin/env python3
"""Paso 1 anticipacion_v4: mecanismo de los rivales (R1 0x9783f45c, R2 0xe38cc08b, R3 0x27e99389) en BTC 5m.
Solo lectura. Usa rival_D.csv (r3_out: fills tomadores casados con WS + 5 placebos por fill en el mismo mercado-lado), polybolt twap60
(ref5=twap60@C-300, ref15=twap60@C-900), Binance aggTrades por RECEPCION. Salida: resumen en p1_out.txt + p1_fills.csv.gz (cache)."""
import sys, glob, os, gzip
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
import numpy as np, pandas as pd
from math import erf, sqrt
from simlib import binance, O
R3 = O + 'r3_out/'; OUT = []
def Phi(x): return 0.5 * (1 + np.vectorize(erf)(x / sqrt(2)))
def refs(D):
    f = glob.glob(f'/root/polymarket-research/data/prices/polybolt_{D}.csv*')[0]
    d = pd.read_csv(f, usecols=['asset', 'canal', 'value', 'event_ts_ms', 'source'])
    d = d[(d.asset == 'BTC') & (d.canal == 'twap60') & (d.source == 'chainlink')].drop_duplicates('event_ts_ms')
    return dict(zip(d.event_ts_ms // 1000, d.value))
days = sorted(f[-14:-4] for f in glob.glob(R3 + 'rival_2026-*.csv'))
prev = None
for D in days:
    r = pd.read_csv(R3 + f'rival_{D}.csv'); r = r[r.match == 1].copy()
    ref = refs(D)
    # refs del dia siguiente/previo para cierres cerca de medianoche
    for dd in (pd.Timestamp(D) - pd.Timedelta(days=1), pd.Timestamp(D) + pd.Timedelta(days=1)):
        try: ref.update(refs(dd.strftime('%Y-%m-%d')))
        except Exception: pass
    B = binance(D)
    g = np.arange(B['rx'][0], B['rx'][-1], 1000)
    p = B['prx'][np.searchsorted(B['rx'], g, side='right') - 1]
    sig = np.std(np.log(p[300:] / p[:-300])) * 1e4          # bp por 300 s
    r['ref5'] = (r.cierre - 300).map(ref); r['ref15'] = (r.cierre - 900).map(ref)
    r['gap_bp'] = (r.ref5 / r.ref15 - 1) * 1e4               # >0: ref5>ref15 -> s=Down
    r['s_up'] = r.ref15 > r.ref5
    r['sgn'] = np.where(r.lado == 'YES', 1, -1)
    r['lado_es_s'] = (r.lado == 'YES') == r.s_up
    t = (r.ex - 150).values
    for clk, key in (('rx', 'prx'), ('E', 'pE')):
        ts = B['rx'] if clk == 'rx' else B['E']; pp = B[key]
        sp = pp[np.clip(np.searchsorted(ts, t, side='right') - 1, 0, len(ts) - 1)]
        r[f'z_{clk}'] = r.sgn * (sp / r.ref5 - 1) * 1e4
    r['T_s'] = (r.cierre * 1000 - t) / 1000
    r['fv_gbm'] = Phi(r.z_rx.values / (sig * np.sqrt(np.clip(r.T_s.values, 1, None) / 300)))
    r['sig300'] = sig
    r['m15'] = r.s15_bid - r.s5_ask - 0.07 * r.s5_ask * (1 - r.s5_ask)    # margen V4 con bid15
    r['d_ask15'] = r.s15_ask - r.s5_ask
    r['edge_gbm'] = r.fv_gbm - r.s5_ask
    OUT.append(r); print(D, len(r), 'sig300 bp', round(sig, 2), flush=True)
A = pd.concat(OUT); A.to_csv(O + 'r3_out/p1_fills.csv.gz', index=False)
# ---------------- resumen
f = open('/root/polymarket-research/experimentos/5m_barato/anticipacion_v4/p1_out.txt', 'w')
def P(*a):
    print(*a); print(*a, file=f)
R = A[A.placebo == 0].copy(); PL = A[A.placebo == 1].copy()
R['rafaga'] = R.ex // 60                                       # rafaga ~ 60 ms
R1 = R.sort_values('ex').drop_duplicates(['w', 'cierre', 'lado', 'rafaga'])
P('fills reales', len(R), 'rafagas', len(R1), 'placebo', len(PL), 'ref5 missing', R.ref5.isna().mean().round(3))
P('lado == s (implicado por TWAP):', R.groupby('w').lado_es_s.mean().round(3).to_dict(), '| placebo', PL.lado_es_s.mean().round(3))
# unidades: primera compra
U = R.sort_values('ex').groupby(['w', 'cierre', 'lado']).first().reset_index()
P('unidades', len(U), U.groupby('w').size().to_dict(), 'T de la 1a compra P10/50/90', np.percentile(U.T_s, [10, 50, 90]).round(0))
def auc(x, y):
    d = pd.DataFrame({'x': x, 'y': y}).dropna(); 
    if d.y.nunique() < 2: return np.nan
    rk = d.x.rank(); n1 = d.y.sum(); n0 = len(d) - n1
    return (rk[d.y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)
P('\nAUC real(rafagas) vs placebo (mismo mercado-lado, T 10-295 s) por rasgo causal en ex-150 ms:')
cols = ['m15', 'd_ask15', 's5_ask', 's15_bid', 's15_ask', 'z_rx', 'z_E', 'edge_gbm', 'fv_gbm', 'T_s', 's5_da1s', 's15_db1s', 'R250', 'R1000', 's5_asz']
S = pd.concat([R1.assign(y=1), PL.assign(y=0)])
for w in ['R1_9783', 'R2_e38c']:
    s = S[(S.w == w) & S.lado_es_s]
    P(w, '(lado=s) n real', int((s.y == 1).sum()), 'placebo', int((s.y == 0).sum()), {c: round(auc(s[c], s.y), 3) for c in cols})
# regla: percentiles de los rasgos en el envio
for w in ['R1_9783', 'R2_e38c']:
    s = R1[(R1.w == w) & R1.lado_es_s]
    for c in ['m15', 'edge_gbm', 'z_rx', 's5_ask', 'T_s', 'gap_bp']:
        P(w, c, 'P10/25/50/75/90', np.nanpercentile(s[c], [10, 25, 50, 75, 90]).round(3), '| placebo', np.nanpercentile(PL[PL.w == w][c], [10, 25, 50, 75, 90]).round(3))
# EV por tramo de edge_gbm y de m15 (fills por rafaga, ponderado por usd)
R1 = R1.dropna(subset=['gana']); R1['pnl'] = R1.acc * (R1.gana.astype(float) - R1.p) - R1.fee; R1['coste'] = R1.usd + R1.fee
for c, bins in (('m15', [-9, -.1, -.05, 0, .05, 9]), ('edge_gbm', [-9, -.1, -.05, 0, .05, .1, .2, 9]), ('z_rx', [-99, -3, -1, 0, 1, 3, 99])):
    for w in ['R1_9783', 'R2_e38c']:
        s = R1[R1.w == w].copy(); s['b'] = pd.cut(s[c], bins)
        t_ = s.groupby('b', observed=True).agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), coste=('coste', 'sum')); t_['EV'] = (t_.pnl / t_.coste).round(3)
        P(w, c, '\n' + t_[['n', 'coste', 'EV']].round(1).to_string())
# seleccion de cierres: universo = mk (cierres con lado s) ; fraccion operada por rival segun |gap|
mk = pd.concat([pd.read_csv(f_, usecols=['dia', 'cierre', 'lado']).drop_duplicates() for f_ in glob.glob(R3 + 'mk_*.csv') if os.path.getsize(f_) > 0])
mk = mk[mk.dia.isin(days)]
gp = A.drop_duplicates('cierre').set_index('cierre').gap_bp.abs()
traded = {w: set(R[R.w == w].cierre) for w in R.w.unique()}
mk['absgap'] = mk.cierre.map(gp)
P('\ncierres universo (dias con rival)', len(mk), 'cierres con gap conocido (solo los que algun rival opero)', mk.absgap.notna().sum())
for w in ['R1_9783', 'R2_e38c']:
    P(w, 'cierres operados', len(traded[w]), 'de', len(mk), '=', round(len(traded[w]) / len(mk), 3), '| solo dias con >=100 fills:', R[R.w == w].dia.value_counts().head(3).to_dict())
f.close()
