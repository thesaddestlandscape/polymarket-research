#!/usr/bin/env python3
"""condicion1.py DIA [DIA...] -- Condicion 1 de INTEGRIDAD_V2_REVISION_A1_11nov: tf y aceptacion de G0 con reloj correcto. Solo MEDIDA DE RELOJ (no reglas ni umbrales). 0 ordenes.
Para cada dia compara los modos legacy (== passT original), causal (conocimiento rx + mecanica ex) y rx (todo recepcion) sobre G0: n, pnl, EV ponderado por EUR (pnl rb0,2 / coste), n con L2 valido (trg.bad nulo = criterio de aceptacion del Paso 0) y emparejado por (k, L, seg): dtf, rellenos solo en uno.
Referencia original: q11/toxicidad_thru1/out (o passT_copia/out) RT_<D>.pkl + out/trg_<D>.pkl. Salida: out_v2/condicion1_<dias>.json."""
import sys, os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OV = H + 'out_v2/'
Q = H + '../q11/toxicidad_thru1/out/'; M = H + 'passT_copia/out/'
dias = sys.argv[1:]; R = dict(dias=dias, modos={}, pares={}, original={})


def pct(x):
    x = np.asarray(x, float)
    if len(x) == 0: return dict(n=0)
    p = np.percentile(x, [1, 5, 50, 95, 99]); return dict(n=int(len(x)), p1=float(p[0]), p5=float(p[1]), p50=float(p[2]), p95=float(p[3]), p99=float(p[4]), abs_le_20=round(float((np.abs(x) <= 20).mean()), 4), abs_le_50=round(float((np.abs(x) <= 50).mean()), 4), igual=round(float((x == 0).mean()), 4))


def resumen(F, T):
    m = F.merge(T[['k', 'L', 'tf', 'bad']], left_on=['k', 'L', 'tf_orig' if 'tf_orig' in F else 'tf'], right_on=['k', 'L', 'tf'], how='left', suffixes=('', '_t'), validate='1:1')
    v = m[m.bad.isna()]
    return dict(fills=int(len(F)), pnl=round(float(F.pnl.sum()), 2), cost=round(float(F.cost.sum()), 2), ev=round(float(F.pnl.sum() / F.cost.sum()), 4),
                n_l2valido=int(len(v)), pnl_l2valido=round(float(v.pnl.sum()), 2), ev_l2valido=round(float(v.pnl.sum() / v.cost.sum()), 4) if len(v) else None, bad=m.bad.fillna('ok').value_counts().to_dict())


for d in dias:
    G = {}
    for modo in ('legacy', 'causal', 'rx'):
        f = OV + f'g0_fills_{modo}_{d}.pkl'; t = OV + f'trg_{modo}_{d}.pkl'
        if not (os.path.exists(f) and os.path.exists(t)): continue
        F = pd.read_pickle(f); F['cost'] = F.q * F.L; F['tf_orig'] = F.tf; T = pd.read_pickle(t)
        G[modo] = F; R['modos'][f'{modo}_{d}'] = resumen(F, T)
    p = M if os.path.exists(M + f'RT_{d}.pkl') else Q
    r = pd.read_pickle(p + f'RT_{d}.pkl'); r = r[r['var'] == 'G0'].copy(); r['cost'] = r.q * r.L; tt = pd.read_pickle(H + f'out/trg_{d}.pkl')
    R['original'][d] = resumen(r.assign(tf_orig=r.tf), tt)
    if 'legacy' in G:
        a = G['legacy']; b = r
        R['pares'][f'legacy_vs_original_{d}'] = dict(mismas_filas=bool(len(a) == len(b) and (a.sort_values(['k', 'L', 'seg']).tf.values == b.sort_values(['k', 'L', 'seg']).tf.values).all()))
    if 'legacy' in G:
        for modo in ('causal', 'rx'):
            if modo not in G: continue
            a, b = G['legacy'], G[modo]; m = a.merge(b, on=['k', 'L', 'seg'], how='outer', suffixes=('_leg', '_new'), indicator=True)
            both = m[m._merge == 'both']
            R['pares'][f'{modo}_vs_legacy_{d}'] = dict(n_leg=int(len(a)), n_new=int(len(b)), solo_legacy=int((m._merge == 'left_only').sum()), solo_nuevo=int((m._merge == 'right_only').sum()), en_ambos=int(len(both)),
                                                         dtf_ms=pct((both.tf_new - both.tf_leg).values), dq_distintas=int((np.abs(both.q_new - both.q_leg) > 1e-9).sum()),
                                                         pnl_en_ambos_leg=round(float(both.pnl_leg.sum()), 2), pnl_en_ambos_new=round(float(both.pnl_new.sum()), 2),
                                                         pnl_solo_legacy=round(float(m[m._merge == 'left_only'].pnl_leg.sum()), 2), pnl_solo_nuevo=round(float(m[m._merge == 'right_only'].pnl_new.sum()), 2))
    # caida L1 vs print: sellos del mismo evento en ambos relojes (solo causal/rx guardan tf_rxb/tf_rxp)
    if 'causal' in G:
        c = G['causal']; x = c[(c.tf_rxb > 0) & (c.tf_rxp > 0)]
        R['pares'][f'causal_rx_caida_vs_print_{d}'] = dict(rxprint_menos_rxcaida=pct((x.tf_rxp - x.tf_rxb).values), rxcaida_menos_tf_ex=pct((x.tf_rxb - x.tf).values), n=int(len(x)), de=int(len(c)))
json.dump(R, open(OV + 'condicion1_' + '_'.join(dias) + '.json', 'w'), indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o))
print(json.dumps(R, indent=1, default=lambda o: o.item() if hasattr(o, 'item') else str(o)))
