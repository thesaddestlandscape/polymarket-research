#!/usr/bin/env python3
"""resumen_final.py -- resumen MECANICO de EXP-1 (<= 50 lineas) a partir de los JSON de exp1/ (solo lectura). Las etiquetas salen de las reglas del ADDENDUM1; NO certifican nada: faltan validador y red-team independientes.
Uso: python3 -I resumen_final.py   -> imprime y escribe RESUMEN_FINAL.txt"""
import os, glob, json, time
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
def J(n):
    p = H + n
    return json.load(open(p)) if os.path.exists(p) else None
E1, E2, E3, E5, E6, E7, S = (J(n) for n in ('E1_B_real_v3.json', 'E2_poblacion.json', 'E3_reglas.json', 'E5_regimen.json', 'E6_brecha.json', 'E7_calma.json', 'STATUS.json'))
S = S or {}
def f(x, d=3):
    try: return 'n/d' if x is None or x != x else f'{x:+.{d}f}'
    except Exception: return str(x)
def ci(a, d=2):
    try: return f'[{a[0]:+.{d}f},{a[1]:+.{d}f}]'
    except Exception: return 'n/d'
L = [f'EXP-1 B x F5, relojes v3 | addendum 6fc7dba5 | {time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())} | etiquetas mecanicas del addendum; NADA validado (faltan validador y red-team independientes)']
# ---- cobertura E2
st = {}; fall = []
for p in sorted(glob.glob(H + 'cache/pob_2026-*.json')):
    try: m = json.load(open(p))
    except Exception: continue
    e = m.get('estado'); st.setdefault(e, []).append(m['dia'][5:])
    if e == 'FAILED': fall.append(m['dia'][5:] + ('=C3' if 'C3' in str(m.get('error')) else ('=MemoryError(tope 2,2 GB)' if 'MemoryError' in str(m.get('error')) else '=otro')))
tot = sum(len(v) for v in st.values()) - (1 if '10-08' in sum(st.values(), []) else 0)
L.append(f"E2 dias (09-Oct..14-Nov = 37 esperados): COMPLETE {len(st.get('COMPLETE', []))}, FAILED {len(st.get('FAILED', []))} [{' '.join(fall)}], PENDING_DESENLACE {len(st.get('PENDING_DESENLACE', []))}, sin intentar {37 - tot} | fases: " + ', '.join(f"{k} {v.get('estado')}" for k, v in S.items()))
# ---- (a) B real
if E1:
    bf = pd.read_pickle(H + 'B_fills_v3.pkl'); ev = bf.pnl.sum() / bf.coste.sum()
    L.append(f"(a) B real, tm3: {len(bf)} fills / {bf.mkt_lado.nunique()} unidades / {bf.cierre.nunique()} cierres / {bf.dia.nunique()} dias, 100 % R1 (20-23 Oct): EV pond. {f(ev, 4)} (PnL {bf.pnl.sum():+.2f} EUR sobre {bf.coste.sum():.1f}) [MEDIDO]")
    g = []
    for l in (35, 60, 100, 150):
        o = E1.get(f'v3 l_ef={l} (todas las ramas)', {}).get('grad_bajo_alto', {}); g.append((l, o.get('g'), o.get('ic90')))
    sg = {np.sign(x[1]) for x in g if x[1] is not None}
    L.append('    gradiente F5 bajo-alto por l_ef: ' + '; '.join(f'{l}: {f(v, 3)} IC90cierre {ci(c, 2)}' for l, v, c in g) + f" -> {'INSUFFICIENT (el signo cambia con l_ef; IC90 cruza 0; n requerido 52k-255k unidades)' if len(sg) > 1 else 'EXPLORATORIA (mismo signo; IC90 cruza 0)'}")
    rs = bf.groupby('rama').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), co=('coste', 'sum')); L.append('    por rama del sello (n, pnl EUR, EV): ' + '; '.join(f'{k} {int(r.n)}, {r.pnl:+.2f}, {r.pnl / r.co:+.3f}' for k, r in rs.iterrows()) + ' [EXPLORATORIA: ramas = calidad del sello, no regla ex ante]')
# ---- E3
if E3:
    R = E3['RES']; b = E3['base']; L.append(f"(a2) reglas de cancelacion sobre los 215 fills (K_B=6, p<=0,0083; latencia SIMULADA; replica de disparo CXB {E3['DIAG'].get('replica_cxb_dif')} % vs funcion validada):")
    for rg in ('CXB60', 'F5C', 'UNION'):
        L.append('    ' + rg + ': ' + '; '.join(f"l{l}: dEV {f(R[f'{rg}_l{l}']['dEV'], 3)} IC90 {ci(R[f'{rg}_l{l}']['dEV_ic90'], 2)}, dPnL {R[f'{rg}_l{l}']['dPnL']:+.1f} EUR, evit {R[f'{rg}_l{l}']['n_evit']:.0f}, placebo p {R[f'{rg}_l{l}']['placebo_p_EVkept']:.2f}" for l in (35, 60)))
    ok = [k for k in ('CXB60_l35', 'CXB60_l60', 'F5C_l35', 'F5C_l60', 'UNION_l35', 'UNION_l60') if R[k]['dEV_ic90'][0] > 0 and R[k]['placebo_p_EVkept'] <= 0.0083]
    L.append(f"    -> {'ALGUNA cumple' if ok else 'INSUFFICIENT: ninguna cumple (IC90 por cierre cruza 0, placebo p>=0,43, 202 unidades/4 dias); no refuta'}; solo rama sig (163 fills, EV base {f(E1['v3 l_ef=60 SOLO sig']['todo'], 3) if E1 else 'n/d'}): dEV positivo en CXB60/F5C/UNION [EXPLORATORIA, ver E3_reglas.txt]")
# ---- (b)
if E2:
    L.append('(b) poblacion (prints bid q en (0,10;0,30], CENSURADA: gradiente, no EV de regla), celdas decisivas K_pop=4 (p<=0,0125 maxstat, >=2/3 dias+):')
    for k in ('p35|R1', 'p60|R1', 'p35|R2', 'p60|R2'):
        c = E2['decisivas'].get(k)
        if not c: L.append(f'    {k}: n/d'); continue
        if 'grad_media_dia' not in c: L.append(f"    {k}: {c.get('etiqueta')}"); continue
        L.append(f"    {k}: grad bajo-alto media diaria {f(c['grad_media_dia'], 3)} IC90dias_inf {f(c['ic90_dias_inf'], 3)}, dias+ {c['dias_pos']}/{c['n_segmentos']}, sin 2 mejores {f(c['sin2mejores'], 3)}, pooled {f(c['grad_pooled'], 3)} IC90cierre {ci(c['ic90_cierre'], 2)}, maxstat p {c['p_placebo_maxstat']:.2f}, n {c['n_prints']} prints/{c['n_cierres']} cierres -> {str(c['etiqueta']).split(';')[0].split('(')[0].strip()}")
# ---- (c) Calma-T1
if E7:
    F = E7['FORWARD 02-Nov..14-Nov (R2)']; T = F['T1']; P = F['T1_menos_PLA']; lit = E7['literal_prereg']['main 02..14-Nov']
    L.append(f"(c) Calma-T1 sello v3, forward 02-14 Nov R2 ({T['n_dias']} dias, n {T['n']}): T1-G0 {T['dEUR']:+.0f} EUR IC90dias {ci(T['ic90_dias'], 0)}, dias+ {T['dias_pos']}/{T['n_dias']}, sin 2 mejores {T['sin2mejores']:+.0f}; merito T1-PLA {P['dEUR']:+.0f} IC90 {ci(P['ic90_dias'], 0)}; EV abs T1 {f(T['EV'], 3)} vs G0 {f(T.get('EV_G0'), 3)}")
    L.append(f"    PREREG_CALMA_T1 literal: {lit['veredicto_literal']} (EV T1 {f(lit['EV_T1'], 3)} <= 0 con 13 dias; T1>PLA en {100 * lit['frac_dias_T1_mayor_PLA']:.0f} % de dias; T1_c300 {f(lit['EV_T1_c300'], 3)}); puerta NO cerrada | mitigacion T1-G0: {S.get('E7', {}).get('etiqueta_mitigacion', 'n/d')}")
# ---- E5
if E5:
    P5 = E5.get('PRIMARIO tipo B, todo T, todos los terciles', {}); nm = {'1': 'D1 vol30', '2': 'D2 vol4h', '3': 'D3 EV bloque previo', '4': 'D4 EV slot'}
    L.append('E5 conductores de regimen (poblacion tipo B, walk-forward desde 23-Oct, K_reg=4): ' + ' | '.join(f"{nm[k]}: " + (f"dEV dia {f(v.get('media_dia'), 3)} IC90inf {f(v.get('ic90_dias_inf'), 3)} dias+ {v.get('dias_pos')}/{v.get('n_dias')} -> {str(v.get('etiqueta')).split(';')[0].split('(')[0].strip()}" if v.get('n_unidades') else 'sin unidades evaluables') for k, v in P5.items()))
# ---- E6
if E6:
    pb = E6['pop']['p60|B']; pt = E6['pop']['p60|todas']; gap = -pb['brecha_pond']
    L.append(f"E6 brecha de B: EV real {f(E6['B']['ev'], 3)} vs poblacion misma celda dia x moneda tipo B {f(pb['esperado_pond_coste_B'], 3)} (pond.; agrupada {f(pb['esperado_agrupado'], 3)}) -> brecha {f(pb['brecha_pond'], 3)}; vs todas las filas {f(pt['esperado_pond_coste_B'], 3)} -> {f(pt['brecha_pond'], 3)} [POBLACION vs MEDIDO; {pb['celdas']} celdas]")
    if E3: L.append('    palancas (dEV sobre B real; % de la brecha-a-poblacion cerrada): ' + '; '.join(f"{rg} l60 {R[f'{rg}_l60']['dEV']:+.3f} ({100 * R[f'{rg}_l60']['dEV'] / gap:+.0f} %)" for rg in ('CXB60', 'F5C', 'UNION')) + '; colocacion/tamano/cola: SIN MEDIR (residuo)')
L.append('Integridad: C3 (suelo rx-ex por ventana de 10 min) alterna ~20/~40 ms DENTRO de las epocas por timestamp (16-Oct 64 % ventanas a 40; 24-Oct 62 % a 20): dias que fallan C3 excluidos y listados; la estratificacion correcta es por suelo de ventana (ADDENDUM2 pendiente, ~2 h).')
out = '\n'.join(L); open(H + 'RESUMEN_FINAL.txt', 'w').write(out + '\n'); print(out); print(f'[{len(L)} lineas]')
