#!/usr/bin/env python3
"""ADENDA_11 §6: SMD/KS/E1 de absr5 antes (p7 DISENO antiguo, absr5 hasta t-50) y despues (p7 DISENO nuevo, absr5 <= t-1000), 12 y 16-Nov. Solo balance, sin tasas."""
import json, os
O = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); out = {}
def pick(r):
    lo = r['prim|vec']['por_clase']['lo']; E = r.get('E', {}); o = {}
    for t, v in lo['estratos'].items():
        if v.get('n_soporte'): o[t] = dict(n_soporte=v['n_soporte'], SMD_absr5_bp_pesado=(v.get('SMD') or {}).get('absr5_bp'), E1_SMD_absr5_bp=((E.get('E1_simple', {}).get('por_estrato', {}).get(t) or {}).get('SMD') or {}).get('absr5_bp'), E2_KS_absr5=(E.get('estratos', {}).get(t, {}).get('E2_KS') or {}).get('absr5'))
    P = E.get('pooled', {}); o['pooled'] = {k: dict(n=v.get('n'), SMD_absr5_bp=(v.get('SMD') or {}).get('absr5_bp'), KS_absr5=(v.get('KS') or {}).get('absr5')) for k, v in P.items()}
    return o
for D in ('12', '16'):
    fo, fn = f'{O}/obsoletos_preD1/p7_btc_2026-11-{D}_DISENO_preADENDA11.json', f'{O}/p7_btc_2026-11-{D}_DISENO.json'
    out[D] = dict(antes=pick(json.load(open(fo))) if os.path.exists(fo) else 'falta ' + fo, despues=pick(json.load(open(fn))) if os.path.exists(fn) else 'falta ' + fn)
json.dump(out, open(f'{O}/absr5_antes_despues_adenda11.json', 'w'), indent=1, default=str); print(json.dumps(out, indent=1, default=str))
