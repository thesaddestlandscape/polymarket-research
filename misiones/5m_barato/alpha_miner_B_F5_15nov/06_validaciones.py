#!/usr/bin/env python3
"""Paso 6: (a) coherencia F5_post del ledger vs F5 del feed q en t_dec para las ordenes rellenadas; (b) n necesario para B real; (c) EV de B real con rebate; (d) sensibilidad a quitar los 2 mejores cierres/dias."""
import os, sys, json, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
SH = np.int64(1) << np.int64(41)
F = pd.read_pickle(AQ + '/B_fills.pkl'); O = pd.read_pickle(AQ + '/B_ordenes.pkl')
tid = F.groupby('oid').tid.first(); Of = O[O.relleno].merge(tid.rename('tid'), left_on='oid', right_index=True); Of['t_ms'] = (Of.t_dec * 1000).astype('int64')
def leeq(path, keep):
    out = []
    for ch in pd.read_csv(path, header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000, compression='gzip', dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True)
res = []
for d, g in Of.groupby('dia'):
    Q = leeq(DL + f'q_{d}.gz', set(g.tid.unique())); K = Q.id.values * SH + Q.r.values; o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, K)); K = K[o]; R = Q.r.values[o]; TA = Q.ta.values[o]; B = Q.b.values[o]; A = Q.a.values[o]
    ids = g.tid.values.astype(np.int64); t = g.t_ms.values; i = np.searchsorted(K, ids * SH + t, 'right') - 1; ok = (i >= 0); i = np.maximum(i, 0); ok &= ((K[i] // SH) == ids) & ((t - R[i]) <= 30000) & (B[i] < A[i])
    res.append(pd.Series(np.where(ok, np.log1p(TA[i]), np.nan), index=g.index))
Of['F5_q_tdec'] = pd.concat(res); m = Of.dropna(subset=['F5_q_tdec', 'F5_post'])
tq = ter(m.F5_q_tdec.values); tl = ter(m.F5_post.values)
txt = ['# (a) Coherencia F5 en la decision: ledger (puja_post.libro) vs feed q en t_dec, ordenes rellenadas: n=%d de %d' % (len(m), len(Of)),
       'misma etiqueta de tercil: %.1f%% | |dF5|<0,05: %.1f%% | corr(F5_ledger,F5_q) = %.3f' % ((tq == tl).mean() * 100, (np.abs(m.F5_q_tdec - m.F5_post) < 0.05).mean() * 100, np.corrcoef(m.F5_q_tdec, m.F5_post)[0, 1]),
       pd.crosstab(pd.Series(tl, name='ledger'), pd.Series(tq, name='q_feed')).to_string()]
# (b) n necesario B real
F['pnl'] = F['size'] * (F.gana - F.precio); F['coste'] = F['size'] * F.precio; F['rebate'] = 0.2 * 0.07 * F.precio * (1 - F.precio) * F['size']
G = F.sort_values(['bloque', 'logidx_fill']).groupby('mkt_lado').agg(pnl=('pnl', 'sum'), coste=('coste', 'sum'), dia=('dia', 'first'), cl=('cierre', 'first'), F5_250=('F5_250', 'first'), F5_100=('F5_100', 'first'))
G['ter'] = ter(G.F5_250.values); G = G.reset_index()
txt += ['', '# (b) n necesario (B real, lag 250 ms): unidades mercado-lado, IC90 por cierre (bootstrap 2000)']
for r in ('todo', 'G1', 'G2'):
    (lo, hi), _ = boot_cluster(G, r, 2000); m_ = G.ter.isin(RET[r]); e = ev(G.pnl[m_], G.coste[m_]); n = int(m_.sum()); se = (hi - lo) / (2 * 1.645)
    txt.append(f'{r}: EV {e:+.3f} n={n} IC90 ({lo:+.3f},{hi:+.3f}) SE {se:.3f}; SD por unidad (retorno/EUR) = {np.std((G.pnl/G.coste)[m_], ddof=1):.2f}; n para IC90 inf>0 si el EV verdadero fuese la mitad del medido: ' + (f'{n*(se*1.645/(e/2))**2:,.0f} unidades' if e > 0 else 'inf (EV<=0)'))
for hip in (0.02, 0.05, 0.10):
    (lo, hi), _ = boot_cluster(G, 'G1', 2000); se = (hi - lo) / (2 * 1.645); n = int(G.ter.isin(RET['G1']).sum()); txt.append(f'G1 si el EV verdadero fuese +{hip:.2f}: n unidades para IC90 inf>0 = {n*(se*1.645/hip)**2:,.0f} (B real aporto {len(G)} unidades en 4 dias => {n*(se*1.645/hip)**2/ (len(G)/4):,.0f} dias a ese ritmo)')
txt += ['', '# (c) rebate teorico B real: EV sin rebate %+.4f, con rebate %+.4f (coste %.2f EUR; rebate %.2f EUR)' % (ev(F.pnl, F.coste), ev(F.pnl + F.rebate, F.coste), F.coste.sum(), F.rebate.sum())]
d = G.groupby('dia').apply(lambda x: pd.Series({'n': len(x), 'pnl': x.pnl.sum(), 'coste': x.coste.sum()}), include_groups=False); txt += ['', '# (d) B real por dia (unidades)', d.round(2).to_string(), f"EV sin el mejor dia: {ev(d.pnl.sort_values().iloc[:-1], d.coste[d.pnl.sort_values().iloc[:-1].index]):+.3f}"]
open(AQ + '/validaciones.txt', 'w').write('\n'.join(txt)); print('\n'.join(txt))
