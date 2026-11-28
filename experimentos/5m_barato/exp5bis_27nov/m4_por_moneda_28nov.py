#!/usr/bin/env python3
"""m4_por_moneda_28nov.py  (28-Nov, paso 3 item 2, ANEXO3 §2 / ANEXO_V2 §4). DIAGNOSTICO etiquetado AMBER; nunca 'exacta' (0 filas propias de B en la cadena). Solo LEE fn5bis_celdas_DIA.pkl (celdas (mercado, lado, nivel L) de TODAS las ordenes armadas de la politica real K6 = DEEP_PEG+repegado; primer relleno por celda;
motor=1 si alguna orden del nivel tuvo q>0 (incondicional: las no rellenadas cuentan 0), obs_nivel/obs_duro de la cadena on-chain V2+V3 en ventana nominal). Dias elegibles por moneda (ANEXO3 §2): ETH 18,24,25,26; SOL/XRP 24,25,26 (V3 verificado; 18-Nov no elegible por contrato); BTC: BLOCKED (no esta en el motor, ANEXO3 §3).
Criterio ANEXO_V2 §4 por moneda: sesgo = P_motor - P_obs (duro y nivel por separado) con IC90 por DIAS (t de Student sobre los sesgos diarios) que contenga 0 y |sesgo| <= max(0,5 pp, 25 % de P_obs); P_motor dentro del cota [P_obs_duro, P_obs_nivel]; n >= 5 dias COMPLETE (>=10 GREEN) y >= 40 eventos duros observados y >= 40 celdas con motor=1; Brier del motor vs observado y su skill frente a la constante P_obs medio;
recall duro. Si no se cumple n => INSUFFICIENT por moneda (no 'sesgo menor'). Ponderacion: por celda (unidad mercado-lado-nivel, tamano acc ~ 5 const.); por lo/hi: todas las ventanas son clase 'lo' (columna `clase`), 0 'hi' => sin sensibilidad hi."""
import json, sys, math
import numpy as np, pandas as pd
O = '/root/polymarket-research-datalogs/exp5bis_27nov/'
DIAS = {'eth': ('2026-11-18', '2026-11-24', '2026-11-25', '2026-11-26'), 'sol': ('2026-11-24', '2026-11-25', '2026-11-26'), 'xrp': ('2026-11-24', '2026-11-25', '2026-11-26')}
T90 = {1: 6.314, 2: 2.920, 3: 2.353, 4: 2.132, 5: 2.015, 6: 1.943, 7: 1.895, 8: 1.860, 9: 1.833}


def ic90_por_dias(v):
    v = np.asarray(v, float)
    n = len(v)
    if n < 2: return (None, None)
    m = v.mean(); se = v.std(ddof=1) / math.sqrt(n); t = T90.get(n - 1, 1.645)
    return (float(m - t * se), float(m + t * se))


def evalua_moneda(G, coin, dias):
    g = G[(G.coin == coin) & (G.dia.isin(dias))]
    out = dict(coin=coin, dias_pedidos=list(dias), dias_con_datos=sorted(g.dia.unique().tolist()), celdas=int(len(g)))
    if not len(g): out['veredicto'] = 'INSUFFICIENT (sin celdas)'; return out
    m, o, d = g.motor.astype(float), g.obs_nivel.astype(float), g.obs_duro.astype(float)
    out.update(P_motor=float(m.mean()), P_obs_duro=float(d.mean()), P_obs_nivel=float(o.mean()), n_duro=int(d.sum()), n_motor1=int(m.sum()), n_obs_nivel=int(o.sum()))
    for nom, ob in (('duro', d), ('nivel', o)):
        porday = [float((x.motor.astype(float) - (x.obs_duro if nom == 'duro' else x.obs_nivel).astype(float)).mean()) for _, x in g.groupby('dia')]
        lo, hi = ic90_por_dias(porday); sesgo = float(m.mean() - ob.mean()); tol = max(0.005, 0.25 * float(ob.mean()))
        out[f'sesgo_vs_{nom}'] = dict(sesgo=sesgo, por_dia=porday, ic90_dias=[lo, hi], ic_contiene_0=(None if lo is None else bool(lo <= 0 <= hi)), tolerancia=tol, dentro_tolerancia=bool(abs(sesgo) <= tol))
    out['P_motor_dentro_cota_duro_nivel'] = bool(d.mean() <= m.mean() <= o.mean())
    pbar = float(o.mean()); brier = float(((m - o) ** 2).mean()); b0 = float(((pbar - o) ** 2).mean())
    out['brier_motor_vs_obs_nivel'] = brier; out['brier_constante'] = b0; out['brier_skill'] = (None if b0 == 0 else 1 - brier / b0)
    out['recall_duro'] = (float(m[d == 1].mean()) if (d == 1).any() else None); out['motor0_obs_duro1(FN duros)'] = int(((m == 0) & (d == 1)).sum())
    nd = g.dia.nunique()
    falta = []
    if nd < 5: falta.append(f'{nd} dias < 5')
    if out['n_duro'] < 40: falta.append(f"{out['n_duro']} eventos duros < 40")
    if out['n_motor1'] < 40: falta.append(f"{out['n_motor1']} celdas motor=1 < 40")
    out['n_dias'] = int(nd)
    out['veredicto'] = ('INSUFFICIENT (' + '; '.join(falta) + ')') if falta else ('GREEN_CANDIDATO' if (out['sesgo_vs_duro']['dentro_tolerancia'] and out['sesgo_vs_nivel']['dentro_tolerancia'] and out['P_motor_dentro_cota_duro_nivel']) else 'AMBER/RED (revisar sesgo)')
    out['etiqueta'] = 'diagnostico AMBER: calibracion contra cota de makers ajenos, nunca exacta (0 filas propias)'
    return out


PB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'


def tape_filas_por_moneda(dia, monedas=('eth', 'sol', 'xrp')):
    """Filas de la cinta on-chain que ALIMENTA al motor (tape_DIA.pkl de precursores_barrido) en los tokens de las ordenes de cada moneda. 0 => el motor es CIEGO para esa moneda-dia (la cinta se construyo solo con la cadena V2): su motor=0 no es calibracion."""
    R = pd.read_pickle(O + f'ordenes_K6_base_{dia}.pkl'); tc = pd.read_pickle(PB + f'tape_{dia}.pkl').token_id.astype(str)
    out = {}
    for c in monedas:
        r = R[R.coin.astype(str).str.lower() == c]; toks = set(r.token.astype(str)) | set(r.token_comp.astype(str)); out[c] = int(tc.isin(toks).sum())
    return out


def main():
    G = {d: pd.read_pickle(O + f'fn5bis_celdas_{d}.pkl') for d in ('2026-11-18', '2026-11-24', '2026-11-25', '2026-11-26')}
    G = pd.concat(G.values(), ignore_index=True)
    tape = {d: tape_filas_por_moneda(d) for d in ('2026-11-18', '2026-11-24', '2026-11-25', '2026-11-26')}
    res = {}
    for c in DIAS:
        dias_ok = tuple(d for d in DIAS[c] if tape[d][c] > 0)                                  # solo dias con cinta del motor NO ciega
        res[c] = evalua_moneda(G, c, dias_ok) if dias_ok else dict(coin=c, dias_pedidos=list(DIAS[c]))
        res[c]['dias_excluidos_motor_ciego'] = [d for d in DIAS[c] if tape[d][c] == 0]
        if not dias_ok: res[c]['veredicto'] = 'BLOCKED (el motor es ciego: tape_DIA.pkl sin filas de ' + c.upper() + ' en ' + ','.join(DIAS[c]) + '; la cinta se construyo sin la cadena V3; su motor=0 NO es calibracion)'
    res['tape_filas_por_moneda_dia'] = tape
    res['btc'] = dict(veredicto='BLOCKED (BTC no esta en el motor ni en sa_ms/tape; ANEXO3 §3b)')
    # por dia y moneda (descriptivo, no es criterio)
    res['descriptivo_por_dia_moneda'] = {f'{c}|{d}': dict(celdas=int(len(x)), P_motor=float(x.motor.mean()), P_obs_duro=float(x.obs_duro.mean()), P_obs_nivel=float(x.obs_nivel.mean()), n_duro=int(x.obs_duro.sum()), n_motor1=int(x.motor.sum())) for (c, d), x in G.groupby(['coin', 'dia'])}
    json.dump(res, open(O + 'paso3/m4_por_moneda.json', 'w'), indent=1, default=float)
    for c in DIAS:
        r = res[c]
        if 'P_motor' not in r: print(c, r['veredicto']); continue
        print(c, r['veredicto'], 'P_motor %.4f P_duro %.4f P_nivel %.4f sesgo_duro %.4f sesgo_nivel %.4f recall_duro %s FNduros %s' % (r['P_motor'], r['P_obs_duro'], r['P_obs_nivel'], r['sesgo_vs_duro']['sesgo'], r['sesgo_vs_nivel']['sesgo'], r['recall_duro'], r['motor0_obs_duro1(FN duros)']), 'dias', r['dias_con_datos'], 'excluidos(ciego)', r['dias_excluidos_motor_ciego'])


if __name__ == '__main__':
    main()
