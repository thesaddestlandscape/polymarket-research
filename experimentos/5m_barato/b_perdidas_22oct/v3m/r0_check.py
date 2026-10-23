#!/usr/bin/env python3
"""r0_check.py DIA... -- Gate R0 del PREREG_V3_PUERTA_v2 §2: simv3m (m5_registro) frente a simv2 original (sa_ms) en 17-21 Oct."""
import sys, json, numpy as np
SA = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/datos/simv2/'; V = '/root/polymarket-research-datalogs/v3m_puerta/'
res = {}
for d in sys.argv[1:]:
    a = np.load(SA + f'simv2_{d}.npz', allow_pickle=True); b = np.load(V + f'simv3m_{d}.npz', allow_pickle=True)
    ia = {m: i for i, m in enumerate(a['mkt'])}; ib = {m: i for i, m in enumerate(b['mkt'])}
    com = sorted(set(ia) & set(ib)); xa = np.array([ia[m] for m in com]); xb = np.array([ib[m] for m in com])
    def eq(x, y): return (np.isclose(x, y, atol=1e-6, rtol=0) | (np.isnan(x) & np.isnan(y)) | ((x == y)))
    pa, pb = a['p'][xa], b['p'][xb]; ma, mb = a['minpc'][xa], b['minpc'][xb]
    va, vb = np.isfinite(pa), np.isfinite(pb); fa, fb = va.argmax(1), vb.argmax(1); qa, qb = va.any(1), vb.any(1)
    sa = np.round(a['ba'][xa].astype(float) - a['bb'][xa].astype(float), 2); sb = np.round(b['ba'][xb].astype(float) - b['bb'][xb].astype(float), 2)
    r = np.arange(len(com)); s1a = sa[r, fa]; s1b = sb[r, fb]
    same_first = (qa == qb) & ((~qa) | (fa == fb)); same_spr = same_first & ((~qa) | eq(s1a, s1b))
    res[d] = dict(n_orig=len(ia), n_nuevo=len(ib), comunes=len(com), frac_comunes=len(com) / max(len(ia), 1),
                  celdas_p_iguales=float(eq(pa, pb).mean()), celdas_minpc_iguales=float(eq(ma, mb).mean()),
                  mercados_mismo_paso1=float(same_first.mean()), mercados_mismo_spread_puerta=float(same_spr.mean()),
                  side_igual=float((a['side'][xa] == b['side'][xb]).mean()), win_igual=float((a['win'][xa] == b['win'][xb]).mean()))
    print(d, json.dumps({k: (round(v, 5) if isinstance(v, float) else v) for k, v in res[d].items()}), flush=True)
json.dump(res, open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/v3m/r0_check.json', 'w'), indent=1)
