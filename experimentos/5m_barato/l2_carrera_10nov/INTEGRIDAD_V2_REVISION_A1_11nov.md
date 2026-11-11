# INTEGRIDAD V2 -- revision A1 y reloj sa_ms (11-Nov-2026, data-integrity). Solo lectura; 0 ordenes; ningun dia >=10-Nov abierto.
Hashes verificados hoy: PREREG 573dae38..., ADDENDUM_A1 13249423..., l2eval/paso0_lib/paso0_run/gen_a1/test_l2eval coinciden con A1 (prefijos). eval_log.jsonl: max dia 2026-11-09, ninguna llamada hold=True.

## (d) Reloj de sa_ms -- VEREDICTO: RED para la afirmacion "sa_ms = recepcion"; AMBER para las conclusiones que dependen de ella
Evidencia:
1. `b_seleccion_adversa/scripts/ms_extract.py` lee de maker_ms las filas q/t con `names=[tipo,t,tok,c1..c5]` y guarda `q_t = t - t0` (columna 2). En libro_estado_ws.py (lineas 396-ss) la fila q es `q,{t_ev},tok,bid,ask,sz_bid,sz_ask,{_T_RECV}`: columna 2 = `t_ev` = hora del EXCHANGE (timestamp del WS del CLOB); la recepcion (col 8 en q, col 7 en t) NO se copia a sa_ms. Verificado en muestra real (maker_ms_2026-11-09_3468001, 1,88 M filas q, 21,7 k t).
2. Por tanto `sa_ms.q_t` es reloj del exchange, no de recepcion. El ADDENDUM A1 §6.4 lo deja "no verificado" y el PREREG §1 ("Reloj: todo rasgo <= t en RECEPCION (sa_ms / libro5)") lo da por supuesto: la premisa es falsa para sa_ms.
3. Desfase recepcion - sello (muestra de un fichero, primeros 3 M de lineas, un solo dia/proceso; NO es poblacion): q p5/p50/p90/p99 = 16/19/36/260 ms; t = 16/18/34/428 ms; 0 % negativos. Cola larga = sello de lote (coherente con la trampa 07-Oct: 4/10 price_change con sello 192-468 ms anterior a nuestro envio).
4. Anclas propias (ordenes reales con hora de envio): NO re-medidas hoy (no localice el fichero de ordenes con t_send en el tiempo asignado) -> NO VERIFICADO; vale la medicion del 07-Oct (memoria, n=10).
5. Mezcla de relojes confirmada en el pipeline: passT (passT_copia/passT.py l.23) pone tm = (primera caida L1 en `D.qt`=sa_ms q_t, reloj EXCHANGE) o, si no hay caida en 400 ms, `t_print - 63` donde t_print = t_ws_ms del tape chain = recepcion de libro5_tx (reloj RECEPCION). capt.Day (dev) tambien usa `z['q_t']+t0`. l2_triggers.py y b40/libro5 si ordenan por recepcion (rx, seq).
Impacto cuantificado: sesgo mediano ~19 ms (tf por caida L1 sale ~19 ms ANTES de lo que veria nuestro proceso; p90 36; p99 ~260). Lambda de E1 = 150/310/560 y d_det 250 ms: efecto mediano despreciable (<=13 % de Lambda=150), pero la cola (1-5 % de eventos) puede invertir el orden libro vs print en ráfagas.
Conclusiones que dependen de ello:
- Paso 0 E1 KILL (placebo p 0,32/1,0): robusto; un desfase de ~20 ms no lo cambia. Inversion +570: igual.
- Paso 0 X1 KILL (12 variantes todas Delta<0; d_det 150-500): robusto a ~20 ms; X1 usa sa_ms (nivel 1 del complementario) con t_arm = t_dec (ambiguedad ya declarada).
- INTEGRIDAD_V2 Q2 (3): "reduccion-L menos print complementario, mediana -228 ms": mezcla exchange (sa_ms) vs recepcion (print): el verdadero valor en un mismo reloj sera ~ -228+19 = -209 ms (orden de magnitud, no verificado); la regla cualitativa (la reduccion precede al print) se mantiene.
- "Reduccion de L vs tf mediana -10 ms; |dt|<=50 ms 37 %, <=20 ms 17,5 %": ESTA resolucion (<=50 ms) es del mismo orden que el desfase de reloj (p50 19 ms) y no se puede interpretar sin corregirlo.
- TESTS_BARATOS T2 (recall 0,35: reloj/emparejado ~0,01): el test cambio la fuente de cinta (cadena->WS), no el reloj de sa_ms; su dictamen "reloj ~0,01" no cubre el desfase exchange-vs-recepcion. NO verificado que un reloj coherente no mueva el recall.
- Tape 'chain' usa recepcion de libro5_tx, que llega ~63-128 ms DESPUES de la cotizacion que muestra el libro consumido (trampa 03-Nov): sigue sin corregirse en passT; tm = print-63 es justo esa correccion constante, no por evento.

## (e) Revision de ADDENDUM_A1 -- VEREDICTO: APRUEBA CON CONDICIONES (AMBER para uso confirmatorio; no es evidencia de edge)
Por metrica (fuente, campo, ancla, unidad, metodo):
- Dias validos (§1): regla por codigo (bad_D.json, stats.json, sa_ms), sin PnL: correcto. Nota: 09-Nov valido L2 pero NO valido thru1 (hueco H1 148 s) -> criterio mixto sin decidir (Paso 0 §1.8).
- EV incondicional G0 (§2): fuente g0_fills.pkl/RT passT, desenlace oficial; unidad colocacion (47.368), denominador coste de rellenos, ponderado por EUR, IC90 por dias, sin 2 mejores dias: CUMPLE la regla de poblacion completa (no relleno = 0; pnl/colocacion -0,0117 reportado). Pendiente: la descomposicion P(relleno) x EV|relleno no esta (4.633/47.368 = 9,8 % calculable, EV|relleno -0,16: reportarla).
- E1/X1 KILL (§3): etapa 0 con placebo estratificado dia x L x moneda + placebo de grupo + inversion: metodologicamente solido. Limite declarado: sa_ms solo da nivel 1 del complementario.
- N1 TRAIN: ancla T_arm (T al armar, de g0_segs) y bidL = bid(t-300ms)-L: ex-ante, NO hay fuga de T_rem al relleno; bloque UTC desde t_dec: ex-ante. Join F-S verificado hoy: 0 NaN en bidL (la linea `assert U.bidL.notna().all() or True` en paso0_lib.py es vacia, pero no hubo perdida; si cambian los datos podria perder rellenos en silencio -> condicion 2).
- N1 n: n por celda = FILLS; en las 11 celdas armadas n_fills = n_mercados (verificado hoy: 30-84 mercados distintos por celda), OK; PERO el mismo mercado rellena varios niveles L y por tanto entra en varias celdas (3.219 fills G0^GEO6 = 1.180 mercados = 815 cierres): celdas ETH L=0,13/0,16/0,19 del mismo bloque/T_rem no son independientes; ETH/SOL comparten cierre (racimo, trampa 02-Oct). n efectivo << 3.219.
- N1 P^ = (aciertos+0,5)/(n+1) por fill, NO ponderado por EUR (q varia) -> usar ponderado o declarar equivalencia (condicion 4).
- N1 seleccion: 11 de 144 celdas (37 con n>=30) elegidas por P^>=L+0,02 sin correccion de multiplicidad; in-sample +367 EUR con placebo p=0 es seleccion (A1 lo dice); fuera de muestra (03-09 Nov, 7 celdas) p=0,67 vs placebo, dias+ 0,57. Lectura A1 ("opera menos") correcta.
- Veto >=85 %: coste no armado 0,849783 por 0,000217: en HOLD casi seguro veto (A1 lo admite). Consecuencia de diseno: la unica pieza de A1 esta casi condenada a ser etiquetada veto/REJECTED, y con sd diaria 40-52 EUR/dia hacen falta 33-43 dias a alpha 0,003125 (A1 §5) cuando solo hay looks a 10 y 20 dias: G2 inalcanzable salvo efecto >2x el de TRAIN. No es fuga, es potencia: el resultado esperado es INSUFFICIENT/REJECTED, no un "descubrimiento".
- Denominadores: Delta/Sigma coste base ok; el "coste no armado" se mide sobre coste de RELLENOS (no de colocaciones) -> la quita de colocaciones no armadas que nunca se habrian rellenado no cuenta; coherente con pnl=0 sin relleno, pero conviene reportar tambien % de colocaciones quitadas.
- E2/B1/N3/H-VIDA/N2: BLOCKED/PENDIENTE, correctamente no incluidos; A1 no debe reabrirse con ellas sin A2 previo al look.
Condiciones (numeradas):
1. Corregir/declarar el reloj: en ADDENDUM/PREREG-aclaracion (sin tocar los congelados; nota A2) fijar que sa_ms q_t = EXCHANGE, no recepcion, y que passT mezcla relojes (tm exchange vs print recepcion); antes del primer look recalcular tf/tm con recepcion (columna c5/c7 de maker_ms) en una muestra y reportar el cambio en G0 y en la aceptacion (1350, -0,2447). Si la aceptacion se mueve >1 EUR o cambia el signo de E1/X1, REVISAR.
2. Sustituir el `assert ... or True` por un assert real o contar rellenos sin segmento (hoy 0) y registrar el conteo en el informe del primer look.
3. Reportar siempre IC y placebo de N1 por CIERRE o dia (no por fill): n efectivo = cierres (815 para G0^GEO6), no 3.219 fills; celdas del mismo cierre = una apuesta.
4. Reportar P^ y Delta ponderados por EUR (Sum pnl/Sum coste) ademas del conteo por fill.
5. Mantener la etiqueta: N1 = "operar menos" (P^ fuera de muestra no supera placebo); no presentar como edge. Si el HOLD da veto >=85 %, el veredicto es veto/REJECTED, no "casi PROMISING".
6. Anadir la descomposicion P(relleno) x EV|relleno y % de colocaciones quitadas a todo informe de cartera.
7. Decidir antes del look si el criterio de dia valido incluye H1 de Binance (thru1) o solo horas sanas L2 (09-Nov es valido L2 / no valido thru1).
8. El look HOLD debe escribir eval_log.jsonl con hold=True (A1 §6.3, sin verificar hoy) y usar solo celdas de A1 (sin re-armar con HOLD).

## No verificado (fail loud)
- Anclas propias (ordenes reales con hora de envio) para medir el desfase exchange-recepcion: no localizadas; solo una muestra de un fichero de un dia.
- Que el desfase p50 19 ms sea estable por hora/carga (la memoria dice p90 280 -> 115 ms segun carga).
- Efecto numerico de corregir el reloj sobre la aceptacion de 1350 fills y sobre Q2 (-228 ms).
- Contenido de los ficheros HOLD (no abiertos, por diseno).
Siguiente prueba minima: re-ejecutar passT/aceptacion en 1 dia (03-Nov) con `tm` en recepcion (c5) y comparar tf; coste CPU bajo (un dia, nice 19, fuera de 06-09Z).
