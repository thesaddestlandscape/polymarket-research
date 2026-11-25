#!/usr/bin/env python3
"""compara_v3_v4.py [DIR_V3_ACTUAL] -- compara v3 vs v4 (sin polvo). Solo lectura -> compara_v3_v4.json.
 (1) verif 20-23 Oct: verif_real/out_v3/V3_<d>.pkl (publicado) vs out_v4 (columnas f_q/f_tf de los 3 tags x BASE/OPT).
 (2) passT 26-Oct..09-Nov, A/B limpio: RT_v3dd con engine_v3 ACTUAL (re-ejecutado en DIR_V3_ACTUAL, mismo codigo/entradas) vs RT_v3dd v4: filas solo-v3 (deben ser polvo), solo-v4, celdas distintas en filas comunes.
 (3) paridad G0 vs lo PUBLICADO: CX_v3dd[R] (G0, 15 dias) vs RT_v3dd v4 var G0: filas, q, tf, agregados (47.470 seg / 4.601 rellenos / coste 3.422,49 / pnl -527,76 / EV -0,1542)."""
import json, sys, os, numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; V3A = sys.argv[1] if len(sys.argv) > 1 else None
FLOOR = 1e-3; TOLQ = 1e-6; out = {'verif': {}, 'passT_vs_v3actual': {}, 'G0_vs_publicado': {}}
VD = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']; PD = [d.strftime('%Y-%m-%d') for d in pd.date_range('2026-10-26', '2026-11-09')]
for d in VD:
    a = pd.read_pickle(H + f'verif_real/out_v3/V3_{d}.pkl'); b = pd.read_pickle(H + f'verif_real/out_v4/V3_{d}.pkl')
    assert list(a.columns) == list(b.columns) and len(a) == len(b) and (a.oid.values == b.oid.values).all()
    r = {'ordenes': len(a), 'cambian': []}
    for c in [c for c in a.columns if c.endswith('_f_q') or c.endswith('_f_tf')]:
        x, y = a[c].values.astype(float), b[c].values.astype(float); dif = ~((x == y) | (np.isnan(x) & np.isnan(y)))
        for i in np.where(dif)[0]: r['cambian'].append(dict(col=c, coin=str(a.coin.values[i]), L=float(a.L.values[i]), v3=float(x[i]), v4=float(y[i])))
    qc = [c for c in a.columns if c.endswith('_f_q')]
    r['polvo_v3'] = int(sum(((a[c] > 0) & (a[c] < FLOOR)).sum() for c in qc)); r['polvo_v4'] = int(sum(((b[c] > 0) & (b[c] < FLOOR)).sum() for c in qc))
    r['n_fill_v3'] = {c: int((a[c] > 0).sum()) for c in qc}; r['n_fill_v4'] = {c: int((b[c] >= FLOOR).sum()) for c in qc}
    out['verif'][d] = r
KS = ['var', 'k', 'L', 'seg']; tot = dict(rows_v3=0, rows_v4=0, solo_v3=0, solo_v3_no_polvo=0, solo_v4=0, comunes=0, comunes_q_dif=0, comunes_tf_dif=0, comunes_otras_dif=0, max_dq_comunes=0.0, max_dpnl_comunes=0.0)
G = dict(seg_v4=0, fill_v4=0, fill_cx=0, solo_cx=0, solo_v4=0, q_dif=0, tf_dif=0, cost_v4=0.0, pnl_v4=0.0, cost_cx=0.0, pnl_cx=0.0, polvo_cx=0, n_seg_cx=0, d_pnl_solo_cx=0.0, filas_solo_cx=[])
for d in PD:
    b = pd.read_pickle(H + f'out_v4/RT_v3dd_{d}.pkl'); assert ((b.q == 0) | (b.q >= FLOOR)).all()
    if V3A:
        a = pd.read_pickle(V3A + f'RT_v3dd_{d}.pkl'); m = a.merge(b, on=KS, how='outer', suffixes=('_3', '_4'), indicator=True)
        s3 = m[m._merge == 'left_only']; s4 = m[m._merge == 'right_only']; cm = m[m._merge == 'both']
        tot['rows_v3'] += len(a); tot['rows_v4'] += len(b); tot['solo_v3'] += len(s3); tot['solo_v4'] += len(s4); tot['comunes'] += len(cm)
        tot['solo_v3_no_polvo'] += int((s3.q_3 >= FLOOR).sum())
        dq = (cm.q_3 - cm.q_4).abs(); tot['comunes_q_dif'] += int((dq > TOLQ).sum()); tot['max_dq_comunes'] = max(tot['max_dq_comunes'], float(dq.max()) if len(cm) else 0.0)
        dp = (cm.pnl_3 - cm.pnl_4).abs(); tot['max_dpnl_comunes'] = max(tot['max_dpnl_comunes'], float(dp.max()) if len(cm) else 0.0)
        tot['comunes_tf_dif'] += int((cm.tf_3 != cm.tf_4).sum())
        for c in ('T', 'ftype', 'canc', 'gana', 'tf_rxb', 'tf_rxp', 'rama', 't_dec', 'cost'):
            x, y = cm[c + '_3'], cm[c + '_4']; tot['comunes_otras_dif'] += int(((x.astype(float) - y.astype(float)).abs() > 1e-6).sum()) if x.dtype.kind in 'fiu' else int((x != y).sum())
        out['passT_vs_v3actual'].setdefault('dias', {})[d] = dict(solo_v3=[dict(var=r['var'], act=r['act_3'], L=float(r.L), q=float(r.q_3), pnl=float(r.pnl_3)) for _, r in s3.iterrows()][:30], n_solo_v3=len(s3), n_solo_v4=len(s4))
    # (3) G0 vs publicado (CX_v3dd R, post arreglo de tf)
    cx = pd.read_pickle(H + f'out_v3/CX_v3dd_{d}.pkl'); R = cx['R']; R = R[R['var'] == 'G0']; g = b[b['var'] == 'G0']; S = pd.read_pickle(H + f'out_v4/SEGT_v3dd_{d}.pkl')
    mm = R.merge(g, on=['k', 'L', 'seg'], how='outer', suffixes=('_cx', '_v4'), indicator=True); sc = mm[mm._merge == 'left_only']; sv = mm[mm._merge == 'right_only']; bo = mm[mm._merge == 'both']
    G['seg_v4'] += len(S); G['fill_v4'] += len(g); G['fill_cx'] += len(R); G['solo_cx'] += len(sc); G['solo_v4'] += len(sv)
    G['q_dif'] += int(((bo.q_cx - bo.q_v4).abs() > TOLQ).sum()); G['tf_dif'] += int((bo.tf_cx != bo.tf_v4).sum())
    G['cost_v4'] += float(g.cost.sum()); G['pnl_v4'] += float(g.pnl.sum()); G['cost_cx'] += float(R.cost.sum()); G['pnl_cx'] += float(R.pnl.sum()); G['polvo_cx'] += int(((R.q > 0) & (R.q < FLOOR)).sum())
    G['d_pnl_solo_cx'] += float(sc.pnl_cx.sum()); G['filas_solo_cx'] += [dict(dia=d, act=r.act_cx, L=float(r.L), q=float(r.q_cx), pnl=float(r.pnl_cx)) for _, r in sc.iterrows()]
    G['n_seg_cx'] += int(cx['A'][cx['A']['var'] == 'G0'].n_seg.sum())
G['ev_v4'] = G['pnl_v4'] / G['cost_v4']; G['ev_cx'] = G['pnl_cx'] / G['cost_cx']
out['passT_vs_v3actual']['total'] = tot; out['G0_vs_publicado'] = G
json.dump(out, open(H + 'compara_v3_v4.json', 'w'), indent=1, default=str)
for d, r in out['verif'].items(): print('verif', d, 'ordenes', r['ordenes'], 'celdas que cambian', len(r['cambian']), 'polvo v3/v4', r['polvo_v3'], r['polvo_v4'])
print('passT v4 vs v3-actual', tot); print('G0 v4 vs publicado(CX)', {k: v for k, v in G.items() if k != 'filas_solo_cx'}); print(G['filas_solo_cx'])
