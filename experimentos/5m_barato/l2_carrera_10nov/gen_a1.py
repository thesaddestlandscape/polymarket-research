#!/usr/bin/env python3
"""gen_a1.py -- genera ADDENDUM_A1.md (determinista, sin marcas de tiempo) a partir de out/paso0/{ev,e1n1,x1}.json y escribe ADDENDUM_A1.sha256. Solo dias quemados. 0 ordenes."""
import sys, os, json, hashlib, numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, H)
import l2eval as E, paso0_lib as P
sh = lambda f: hashlib.sha256(open(f, 'rb').read()).hexdigest()
ev, en, x1 = (json.load(open(H + f'out/paso0/{n}.json')) for n in ('ev', 'e1n1', 'x1'))
U, S = P.cargar()
L = []; w = L.append
w('# ADDENDUM A1 a PREREG_L2_V2 -- generado por gen_a1.py (determinista; sin marcas de tiempo)')
w('Generado ANTES de cualquier look sobre dias >=10-Nov (ningun dato >=10-Nov leido: eval_log.jsonl solo contiene dias <=2026-11-09). NO cambia ninguna regla de PREREG_L2_V2: solo fija cartera, dias y parametros de TRAIN.')
w(f'- PREREG_L2_V2.md sha256 {E.PREREG_SHA}')
for f in ('l2eval.py', 'paso0_lib.py', 'paso0_run.py', 'test_l2eval.py', 'gen_a1.py'): w(f'- {f} sha256 {sh(H + f)}')
for f in ('out/g0_fills.pkl', 'out/g0_segs.pkl'): w(f'- entrada {f} sha256 {sh(H + f)}')
w(f'- semilla {E.SEED}; permutaciones/bootstrap B=20000; alpha_look={E.ALPHA}')
w('\n## 1. Dias (por codigo, sin PnL)')
w('Regla de dia valido (l2eval.valida_dia): >=12 horas sanas (bad_D.json), b40 del dia extraido sin fichero corrupto (stats.json), sa_ms presente. Dia HOLD = >=2026-11-10.')
w('Quemados <=09-Nov (valido L2 = cumple la regla; 26-Oct..02-Nov no tienen b40 -> solo etapa 0/TRAIN de reglas que no usan L2): ' + '; '.join(f"{v['dia']}:{'OK' if v['valido'] else 'NO'}({v['horas_sanas']}h{'; ' + ','.join(v['motivos']) if v['motivos'] else ''})" for v in ev['validez']))
w('\n## 2. EV incondicional G0 (rb 0 / 0,2), 15 dias 26-Oct..09-Nov, desenlace de RT passT, ponderado por EUR')
g = ev['G0']
w(f"- G0: colocaciones {g['colocaciones']}, rellenos {g['fills']}, coste {g['cost']} EUR; rb0 EV {g['pnl0']['ev_eur']} IC90 dias {g['pnl0']['ic90_dias']}; rb0,2 EV {g['pnl2']['ev_eur']} IC90 dias {g['pnl2']['ic90_dias']}; sin 2 mejores dias {g['pnl2']['ev_sin_2_mejores_dias']}; dias + {g['pnl2']['pct_dias_pos']}; pnl/colocacion {g['pnl2']['pnl_por_colocacion']}")
g = ev['G0_geo6']; w(f"- G0^GEO6: rellenos {g['fills']}, coste {g['cost']}; rb0 EV {g['pnl0']['ev_eur']} IC90 {g['pnl0']['ic90_dias']}; rb0,2 EV {g['pnl2']['ev_eur']} IC90 {g['pnl2']['ic90_dias']}; dias + {g['pnl2']['pct_dias_pos']}")
a = ev['aceptacion_G0_0307_L2valido']; w(f"- Aceptacion §4 (G0 03-07 Nov con L2 valido): n {a['n']} (esperado {a['esperado_n']}), EV {a['ev']} (esperado {a['esperado_ev']}), pnl {a['pnl']} EUR -> {'OK' if a['ok'] else 'FALLA'}")
w('\n## 3. Etapa 0 y TRAIN (reglas congeladas, sin tocar)')
e = en['E1']['lam310_G0']
for rb in ('0.0', '0.2'):
    r = e['rb'][rb]; w(f"- E1 Lambda=310 base G0 rb{rb}: quita {e['n_quitadas']}/{e['n_unidades']} rellenos ({e['frac_coste_quitado']} del coste); Delta {r['sum_delta']} EUR; placebo estratificado media {r['placebo_media']} p {r['placebo_p']}; placebo grupo-token media {r['placebo_grupo_token_media']} p {r['placebo_grupo_token_p']}; dias + {r['pct_dias_pos']}; inversion (ultimo grupo) Delta {r['delta_inv']}; KILL={r['kill_E1']}")
w('  Sensibilidad Lambda 150/500/560 (G0 y G0^GEO6): KILL en todas (placebo de grupo aleatorio por token-ventana supera a E1 en todas: p=1,0).')
w('  => E1: KILL en etapa 0. FUERA de la cartera A1.')
xb = x1['variantes']['base_M1500']
w(f"- X1 (dias {len(x1['dias_usados'])}: {x1['dias_usados'][0]}..{x1['dias_usados'][-1]}, d_det 250, M 150-1500): coberturas {xb['n_coberturas']}, Delta {xb['delta']} EUR, IC90 por cierre inf {xb['ic90_lb_por_cierre']}, dias+ {xb['pct_dias_pos']}, placebo p {xb['placebo_p']} (media {xb['placebo_media']}), sin 2 mejores {xb['sin_2_mejores']}, monedas+ {xb['monedas_pos']}, tamano>=q {xb['tam_ge_q']}, espejo {xb['frac_espejo']}, inversion (lentas) {xb['delta_inversion_lentas']}; pasa_etapa0={xb['pasa_etapa0']}")
w('  Sensibilidad (d_det 150/500, -2 ticks, M_cut 1000/2000): ninguna de las 12 variantes con Delta>0 y pasa_etapa0=True (todas Delta<0). Limite: sa_ms solo da el nivel 1 del libro del complementario (no recorre niveles); esperada subestimacion de profundidad, no de precio.')
w('  => X1: KILL en etapa 0. FUERA de la cartera A1.')
n1 = en['N1']; v = n1['val_cronologica']
w(f"- N1 TRAIN (26-Oct..09-Nov, base G0^GEO6): {n1['celdas_armadas']} celdas armadas de {n1['celdas_totales']} ({n1['celdas_n30']} con n>=30); coste NO armado {n1['cobertura_exacta']:.6f} (muerte si >=0,85: {'SI' if n1['muerte'] else 'NO, por 0,000217 de margen'}).")
for rb in ('0.0', '0.2'):
    r = n1['gate']['rb'][rb]; rv = v['gate']['rb'][rb]
    w(f"  rb{rb}: in-sample Delta {r['sum_delta']} (placebo media {r['placebo_media']}, p {r['placebo_p']}: SELECCION in-sample, no evidencia); VALIDACION CRONOLOGICA descriptiva (celdas de 26-Oct..02-Nov evaluadas en 03-09 Nov; {v['celdas_armadas_train']} celdas): Delta {rv['sum_delta']} vs placebo media {rv['placebo_media']} p {rv['placebo_p']} dias+ {rv['pct_dias_pos']} cobertura {rv['cobertura_coste']}")
w('  Lectura: N1 reduce perdidas porque opera menos; fuera de muestra NO supera al placebo (p~0,67). Pasa el criterio literal de muerte del prerreg por margen minimo; entra en A1 con esa fragilidad declarada (el veto >=85 % del gate HOLD sera casi seguro: coste no armado 0,8498).')
w('  Celdas armadas (act, L, bloque UTC 0-3, T_rem 0:<120/1:120-210/2:>=210 s; n, dias, P^): ' + '; '.join(f"({c['act']},{c['L']},{c['bloque']},{c['trb']},{c['n']},{c['dias']},{c['p_hat']})" for c in n1['celdas_armadas_lista']))
w('- E2: NO ejecutada en el Paso 0 (requiere logistica L2 sobre b40 DESC 03-07 Nov: lectura de ~2,6 GB comprimidos de b40 por token-ventana; programada para la ronda siguiente, ANTES del primer look). Estado A1: PENDIENTE.')
w('- B1: BLOCKED: requiere generador U2 (colocaciones virtuales L+0,01/+0,02) no construido (§6 f). No se puede hacer TRAIN. N3, H-VIDA: BLOCKED por U2.')
w('- N2 (BTC): DATA_BLOCKED en hoy: passT G0 es ETH/SOL/XRP, sa_ms se extrae con SA_COINS=ETH,SOL,XRP (sin BTC) y no existe RT/SEGT de BTC. k no baja.')
w('\n## 4. Cartera fija A1 (sin tocar tras el primer look)')
w('Cartera A1 = N1 con las celdas listadas (base G0^GEO6, sin ninguna otra pieza). E1 y X1 (KILL) no entran. E2, B1, N3, N2, H-VIDA: no entran salvo que su etapa 0/TRAIN se ejecute y se anexe en A2 ANTES del primer look. B_VIABLE se evalua sobre esta cartera.')
w('\n## 5. Potencia (sd diaria; Delta pareado)')
def pot(nm, xd): s = E.stats_potencia(xd); w(f"- {nm}: n_dias {s['n_dias']}, media {s['media_dia']:.2f}, sd {s['sd_dia']:.2f} EUR/dia, dias necesarios (alpha {E.ALPHA}, potencia 0,8) {s['dias_necesarios']:.0f}, media minima detectable a 10 dias {s['mde10']:.1f}, a 20 dias {s['mde20']:.1f} EUR/dia")
pot('Delta_d E1 L310 (rb0,2)', e['rb']['0.2']['daily']); pot('Delta_d N1 in-sample (rb0,2)', n1['gate']['rb']['0.2']['daily']); pot('Delta_d N1 validacion 03-09 (rb0,2)', v['gate']['rb']['0.2']['daily']); pot('Delta_d X1 base (rb0)', xb['daily'])
xd = U.groupby('dia').pnl2.sum().reindex(P.DIAS).values; w(f"- PnL_d G0 base (rb0,2): media {xd.mean():.2f}, sd {xd.std(ddof=1):.2f} EUR/dia; G0^GEO6 sd {U[U.geo6].groupby('dia').pnl2.sum().reindex(P.DIAS).std(ddof=1):.2f}; coste base medio {U.groupby('dia').cost.sum().mean():.1f} EUR/dia.")
w('- Lectura: sd diaria del Delta pareado 29-40 EUR/dia contra un coste base ~230 EUR/dia (12-17 %); con 10 dias solo se detectan Delta medios >~40 EUR/dia (~17 % del coste base/dia): detectar un efecto de 0,03 EUR/EUR requiere >>20 dias.')
w('\n## 6. Revisar antes del primer look')
w('1) E2 (ronda aparte); 2) generador U2 y aceptacion (§6f); 3) confirmar que el log de HOLD solo se abre con hold=True y escribe eval_log.jsonl; 4) que el reloj de sa_ms (columna t de maker_ms) es RECEPCION (no verificado en este Paso 0); 5) en X1 t_arm = t_dec (ambiguedad del prerreg: no se define t_arm); 6) pnl de RT trae rb 0,2 y se reproduce con la formula (verificado, 1e-15); 7) cuota diaria: b40/RT/x_/tape/bad de cada dia deben existir (valida_dia).')
txt = '\n'.join(L) + '\n'
open(H + 'ADDENDUM_A1.md', 'w').write(txt)
open(H + 'ADDENDUM_A1.sha256', 'w').write(hashlib.sha256(txt.encode()).hexdigest() + '  ADDENDUM_A1.md\n')
print(hashlib.sha256(txt.encode()).hexdigest())
