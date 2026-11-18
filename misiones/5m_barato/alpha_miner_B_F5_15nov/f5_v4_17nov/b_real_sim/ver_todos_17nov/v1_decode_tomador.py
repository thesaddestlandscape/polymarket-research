#!/usr/bin/env python3
"""v1_decode_tomador.py (ver_todos_17nov, 17-Nov) -- SOLO LECTURA. Decodifica matchOrders (selector 0x3c2b4399, parse identico a
experimentos/5m_barato/b_perdidas_22oct/cola_posicion/scripts/c7_decode_calldata.py) de los 202 tx de rellenos reales de B (20-23 Oct) y anade, por relleno,
la ORDEN TOMADORA: limite equivalente en precio-bid de nuestro token (eq), tamano total, remanente, timestamp firmado, y si el tamano del tomador == lo que nos casaron.
Une con la clase FN/TP de r2_call00a35_intc33_v3d (valida_v5.evalua, sin tocarlo). Salida: tomador_202.pkl + v1_resumen.json."""
import json, os, sys, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; B = os.path.dirname(H.rstrip('/')) + '/'
sys.path.insert(0, B); import valida_v5 as VV
OWN = '0x659a40ff9920febc5a66836213040924343d297f'
def parse(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big')
    off_t, off_m, tfill, off_f = w(32), w(64), w(96), w(128)
    def order(s):
        f = [w(s + 32 * k) for k in range(12)]
        return dict(maker='0x' + f[1].to_bytes(32, 'big')[12:].hex(), tokenId=str(f[3]), mA=f[4], tA=f[5], side=f[6], ts=f[8])
    to = order(off_t); n = w(off_m); mk = [order(off_m + 32 + w(off_m + 32 * (1 + i))) for i in range(n)]
    nf = w(off_f); fl = [w(off_f + 32 * (1 + i)) for i in range(nf)]
    return to, mk, fl, tfill
CD = {}
for f in ('/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', H + 'calldata_extra.jsonl'):
    for l in open(f):
        d = json.loads(l); CD[d['tx']] = d['input']
R = VV.carga('r2_call00a35_intc33_v3d'); out, F = VV.evalua(R, 'BASE', verbose=False)
X = pd.read_pickle('/root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov/inventario2.pkl')
rf = R[R.real_fill == 1].copy(); rf['sim'] = rf.v3d_BASE_f_q >= VV.FLOOR
rf = rf.merge(F[['oid', 'causa']], on='oid', how='left'); rf['causa'] = rf.causa.fillna('TP')
rf = rf.merge(X[['oid', 'tok', 'tx', 'estructura', 'n_otros', 'own_sh_tx', 'taker_tipo', 'ntx']], on='oid', how='left')
rows = []
for r in rf.itertuples():
    inp = CD.get(r.tx)
    if inp is None or not inp.startswith('0x3c2b4399'): rows.append(dict(oid=r.oid, dec='sin_calldata')); continue
    to, mk, fl, tfill = parse(inp); tok = str(r.tok)
    own = [o for o in mk if o['maker'] == OWN and o['tokenId'] == tok]
    if to['tokenId'] == tok and to['side'] == 1: eq = to['tA'] / to['mA']; tsz = to['mA'] / 1e6; tipo = 'vende_propio'
    elif to['tokenId'] != tok and to['side'] == 0: eq = 1 - to['mA'] / to['tA']; tsz = to['tA'] / 1e6; tipo = 'compra_comp'
    else: eq = np.nan; tsz = np.nan; tipo = f"otro_t{to['tokenId'] == tok}_s{to['side']}"
    rem = 1 - tfill / to['mA'] if to['mA'] else np.nan
    rows.append(dict(oid=r.oid, dec='ok', tk_tipo=tipo, tk_eq=eq, tk_sz=tsz, tk_rem=rem, tk_ts=to['ts'], own_ts=own[0]['ts'] if own else np.nan, n_mk=len(mk),
                     n_mk_otros=sum(o['maker'] != OWN for o in mk)))
T = rf.merge(pd.DataFrame(rows), on='oid', how='left')
T['eq_menos_L'] = (T.tk_eq - T.L).round(4); T['mas_alla'] = T.eq_menos_L < -0.0049; T['en_L'] = T.eq_menos_L.abs() <= 0.0049
T['sz_igual_nuestro'] = (T.tk_sz - T.own_sh_tx).abs() <= 0.02
T['dts_tk_menos_own'] = T.tk_ts - T.own_ts                 # ms entre firma del tomador y firma de nuestra orden
T['dts_tk_menos_fill'] = T.tk_ts - T.real_tm3             # ms entre firma del tomador y sello de nuestro relleno (tm3)
T.to_pickle(H + 'tomador_202.pkl')
def cls(c): return 'TP' if c == 'TP' else c.split('(')[0]
T['cl'] = T.causa.map(cls); S = {}
for c, g in T.groupby('cl'):
    S[c] = dict(n=len(g), dec_ok=int((g.dec == 'ok').sum()), tipos=g.tk_tipo.value_counts().to_dict(), estructura=g.estructura.value_counts().to_dict(),
                mas_alla=int(g.mas_alla.sum()), en_L=int(g.en_L.sum()), rem_gt1pct=int((g.tk_rem > 0.01).sum()), sz_igual=int(g.sz_igual_nuestro.sum()),
                n_mk_otros_gt0=int((g.n_mk_otros > 0).sum()), dts_own_p10_50_90=[float(x) for x in np.nanpercentile(g.dts_tk_menos_own, [10, 50, 90])],
                dts_fill_p10_50_90=[float(x) for x in np.nanpercentile(g.dts_tk_menos_fill, [10, 50, 90])] if g.dts_tk_menos_fill.notna().any() else None,
                pnl=float((g.real_q * (g.gana - g.L)).sum()), coste=float((g.real_q * g.L).sum()))
json.dump(S, open(H + 'v1_resumen.json', 'w'), indent=1, default=str); print(json.dumps(S, indent=1, default=str))
