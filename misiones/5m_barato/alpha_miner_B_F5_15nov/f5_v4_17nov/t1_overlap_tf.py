#!/usr/bin/env python3
"""t1_overlap_tf.py -- SPEC_F5_V4_17nov.md T1(c). Cruza los rellenos G0 cuyo `tf` cambia entre v3 publicado (out_v3/CX_v3dd R) y v4 (out_v4/RT_v3dd) mas los rellenos-polvo (solo en v3) con la poblacion F5 de ADD3 (exp1/cache/D_pob_add3.pkl.gz).
Union: (coin, fin, lado_m == lado) y |r_ex - tf| <= 60 ms (el print de la poblacion lleva r_ex = tf + ~20 ms; sello r_v3 = r_ex-19-1), banda q (0,10;0,30]; q <= L (relleno al nivel o 'thru'). Solo lectura; 0 ordenes."""
import os, sys, json, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov'); from lib_ev import ter
L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; E1 = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'; HERE = os.path.dirname(os.path.abspath(__file__))
DIAS = [d.strftime('%Y-%m-%d') for d in pd.date_range('2026-10-26', '2026-11-09')]; TOL = 60
filas = []; pesos = {}
for d in DIAS:
    b = pd.read_pickle(L2 + f'out_v4/RT_v3dd_{d}.pkl'); g4 = b[b['var'] == 'G0']; R = pd.read_pickle(L2 + f'out_v3/CX_v3dd_{d}.pkl')['R']; R = R[R['var'] == 'G0']
    mm = R.merge(g4, on=['k', 'L', 'seg'], how='outer', suffixes=('_3', '_4'), indicator=True)
    sel = mm[((mm._merge == 'both') & (mm.tf_3 != mm.tf_4)) | (mm._merge == 'left_only')]
    P = pd.read_pickle(E1 + f'{d}_pob_add3.pkl.gz', compression='gzip'); P['tb'] = ter(P['F5_p60'].values); P['tb35'] = ter(P['F5_p35'].values); P['tipoB60'] = np.isfinite(P.bid_p60) & ((P.bid_p60 - P.q) >= 0.0099 - 1e-12)
    pesos[d] = dict(prints=len(P), coste=float(P.coste.sum()), coste_p60_lo_o_hi=float(P.coste.sum()))
    def busca(r, tf):
        if not np.isfinite(tf): return None
        m = P[(P.coin == r.act_3 if 'act_3' in r else P.coin == r.act) & (P.fin == r.fin_3) & (P.lado_m == r.lado_3) & ((P.r_ex - tf).abs() <= TOL) & (P.q <= r.L + 1e-6)]
        return None if m.empty else m.iloc[(m.r_ex - tf).abs().values.argmin()]
    for _, r in sel.iterrows():
        r = r.copy(); r['act'] = r.act_3 if isinstance(r.act_3, str) else r.act_4
        tf3 = r.tf_3 if r._merge != 'right_only' else np.nan; tf4 = r.tf_4 if r._merge == 'both' else np.nan
        row = dict(dia=d, coin=r['act'], L=float(r.L), tipo='polvo(solo v3)' if r._merge == 'left_only' else 'tf distinto', tf3=int(tf3), tf4=None if not np.isfinite(tf4) else int(tf4), delta_ms=None if not np.isfinite(tf4) else int(tf4 - tf3), q3=float(r.q_3), q4=None if r._merge == 'left_only' else float(r.q_4))
        for nm, tf in (('v3', tf3), ('v4', tf4)):
            p = busca(r, tf)
            if p is None: row.update({f'print_{nm}': False}); continue
            row.update({f'print_{nm}': True, f'q_print_{nm}': float(p.q), f'ter60_{nm}': p.tb, f'ter35_{nm}': p.tb35, f'tipoB60_{nm}': bool(p.tipoB60), f'coste_print_{nm}': float(p.coste), f'r_ex_{nm}': int(p.r_ex)})
        filas.append(row)
D = pd.DataFrame(filas); D.to_csv(HERE + '/T1_overlap_tf.csv', index=False)
n_tf = int((D.tipo == 'tf distinto').sum()); n_dust = int((D.tipo != 'tf distinto').sum())
T = D[D.tipo == 'tf distinto']
res = dict(n_tf_distinto=n_tf, n_polvo_solo_v3=n_dust, por_moneda=T.coin.value_counts().to_dict(), delta_ms=dict(min=int(T.delta_ms.abs().min()), mediana=float(T.delta_ms.abs().median()), max=int(T.delta_ms.abs().max())),
           con_print_pob_v3=int(T.print_v3.sum()), con_print_pob_v4=int(T.print_v4.fillna(False).astype(bool).sum()), ambos=int((T.print_v3 & T.print_v4.fillna(False).astype(bool)).sum()),
           mismo_print=int(((T.r_ex_v3 == T.r_ex_v4) & T.r_ex_v3.notna()).sum()) if 'r_ex_v3' in T else 0,
           tercil_p60_v3=T.ter60_v3.value_counts(dropna=False).to_dict() if 'ter60_v3' in T else {}, tercil_p60_v4=T.ter60_v4.value_counts(dropna=False).to_dict() if 'ter60_v4' in T else {},
           cambian_tercil_p60=int(((T.ter60_v3 != T.ter60_v4) & T.ter60_v3.notna() & T.ter60_v4.notna()).sum()) if 'ter60_v3' in T else 0,
           polvo_con_print_pob=int(D[D.tipo != 'tf distinto'].print_v3.sum()), coste_prints_cruzados_v3=float(T.coste_print_v3.sum()) if 'coste_print_v3' in T else 0.0, coste_pob_total_15d=float(sum(v['coste'] for v in pesos.values())),
           dias=DIAS)
json.dump(res, open(HERE + '/T1_overlap_tf.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str))
