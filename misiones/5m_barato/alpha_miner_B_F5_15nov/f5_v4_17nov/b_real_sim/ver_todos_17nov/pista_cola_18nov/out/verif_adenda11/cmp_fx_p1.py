#!/usr/bin/env python3
"""ADENDA_11 §8(2): fixture fx3h p1 v11 (fxP1) frente a p1 v10 (fxN1): IDENTICO salvo absr5/r5/absr5_rx (+ cover_fich nuevo, version, files/inputs/DCHK). Sale con codigo 1 si falla."""
import pickle, sys, json, os, numpy as np, pandas as pd
O = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
new = pickle.load(open(f'{O}/p1_btc_2026-11-12_fxP1.pkl', 'rb')); old = pickle.load(open(f'{O}/verif_adenda07/fx_artefactos/p1_btc_2026-11-12_fxN1.pkl', 'rb'))
EXC = {'EV': {'absr5', 'r5', 'absr5_rx'}, 'PL': {'absr5', 'r5', 'absr5_rx'}, 'PW': {'absr5', 'r5', 'absr5_rx'}, 'CP': {'absr5'}}
res = dict(version_nuevo=new['version'], version_viejo=old['version']); ok = True
def norm(c): return c.astype(object).where(c.notna(), None) if str(c.dtype) == 'category' else c
for k in ('EV', 'PL', 'PW', 'CP'):
    a, b = new[k], old[k]; r = dict(filas_nuevo=len(a), filas_viejo=len(b))
    ca, cb = set(a.columns), set(b.columns); r['cols_solo_nuevo'] = sorted(ca - cb); r['cols_solo_viejo'] = sorted(cb - ca)
    ok &= (set(r['cols_solo_nuevo']) <= {'absr5_rx'}) and not r['cols_solo_viejo'] and len(a) == len(b)
    dif = []
    for c in sorted(cb & ca):
        if c in EXC[k]: continue
        x, y = norm(a[c]).reset_index(drop=True), norm(b[c]).reset_index(drop=True)
        if not x.equals(y): dif.append(c)
    r['columnas_distintas_no_permitidas'] = dif; ok &= not dif
    if 'absr5' in a.columns:
        n_dif = int((~((a.absr5.reset_index(drop=True) == b.absr5.reset_index(drop=True)) | (a.absr5.isna().reset_index(drop=True) & b.absr5.isna().reset_index(drop=True)))).sum()); r['filas_con_absr5_distinto'] = n_dif; r['frac_absr5_distinto'] = round(n_dif / max(1, len(a)), 4)
    if 'absr5_rx' in a.columns: r['viol_absr5_rx_gt_t_menos_1000'] = int((a.absr5_rx > a.t - 1000).sum()); ok &= r['viol_absr5_rx_gt_t_menos_1000'] == 0; r['frac_absr5_rx_valido'] = round(float((a.absr5_rx >= 0).mean()), 4)
    res[k] = r
for k in ('JN', 'OCN', 'BAD', 'OWNR', 'cover', 'suelo', 'D', 'coin', 'sg_estructural'):
    eq = (new[k] == old[k]); res[k + '_igual'] = bool(eq); ok &= bool(eq)
cf = new.get('cover_fich'); res['cover_fich'] = cf; ok &= bool(cf and all(c['n'] > 0 for c in cf)); res['DCHK_nuevo'] = new['DCHK']; res['IDENTICO_salvo_absr5_r5_absr5_rx'] = bool(ok)
json.dump(res, open(f'{O}/verif_adenda11/cmp_fx_p1.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str)); sys.exit(0 if ok else 1)
