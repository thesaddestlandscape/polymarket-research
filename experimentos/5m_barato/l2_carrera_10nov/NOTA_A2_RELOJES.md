# NOTA A2 (BORRADOR, SIN CONGELAR) -- relojes. 11-Nov-2026. Estado: PARTIAL (tareas 1-5 hechas; E1/X1 con reloj causal EN CURSO, ver §6)
No modifica PREREG_L2_V2 (573dae38) ni ADDENDUM_A1 (13249423): ambos intactos. Solo dias <=09-Nov; 0 ordenes; ningun dia HOLD abierto; sin PnL/EV del HOLD. Contrato: CONTRATO_RELOJES.md. Datos: out_v2/*.json.

## 1. Declaracion de reloj (corrige la premisa de PREREG §1 y de ADDENDUM A1 §6.4)
- `sa_ms/ms_D.npz::q_t, t_t` = sello del EXCHANGE (no recepcion). Verificado: v2 (ms_extract_v2.py) reproduce v1 en las 14 columnas (out_v2/regresion_extractor_2026-11-03.json, 18.255.998 filas q, identico).
- passT MEZCLABA: caida L1 en EXCHANGE (`D.qt`) o `recv_print - 63` (RECEPCION con constante). Conocimiento (features de la rejilla, disparos) leido en EXCHANGE = mira 15-60 ms al futuro.
- Modos nuevos (passT_v2.py MODO DIA): `legacy` (== original, regresion exacta: 03-Nov 287 rellenos G0, pnl 2,66, `tf` identicos fila a fila), `causal` (features en RECEPCION; mecanica de relleno y `tf` en EXCHANGE), `rx` (todo recepcion).

## 2. Calibracion rx-ex (extractor v2, filas q y t de ETH/SOL/XRP 5m/15m, 3 dias, un fichero cada vez) -- out_v2/calib_relojes_<D>.json
| dia | n q | q p5/p50/p90/p99 (ms) | t p5/p50/p90/p99 | negativos | rafaga>100 ms (exceso sobre suelo) |
|---|---|---|---|---|---|
| 03-Nov | 18.255.998 | 15/17/29/125 | 15/17/29/176 | 0 % | 1,14 % |
| 05-Nov | 22.797.081 | 16/18/32/139 | 16/18/28/168 | 0 % | 1,27 % |
| 09-Nov | 23.492.070 | 16/18/32/140 | 16/18/30/198 | 0 % | 1,30 % |
- Hora: p50 17-20 ms todo el dia (max 20 a las 18-19Z del 05-Nov); p90 22-46 ms; las horas 15, 17-21Z y 07Z tienen p90 y rafagas mas altos (carga de mercado, no del reloj).
- Suelo estable ~15-16 ms (min 13-14, 0 % negativos): red + offset de reloj exchange-local; el offset local-NTP medido es 0,2 ms (chrony, 11-Nov), asi que casi todo el suelo es red o offset del exchange (no separable sin anclas simetricas).
- SELLO DE LOTE vs RED ESTABLE: tramas (mensajes con el mismo rx = un frame del WS) con dispersion de sellos >20 ms: ~2,3 % de mensajes, lag p50 55-58 ms, p90 156-168, p99 510-850 ms, 16-18 % con exceso >100 ms; tramas unicas o dispersion <=20 ms: lag p50 17-18, p99 70-109. Spearman exceso vs edad dentro de la trama +0,35..+0,39 y vs tamano de trama +0,36..+0,42 => el exceso es de LOTE (sello anterior al instante real), no de red. 0 duplicados exactos de q entre procesos.
- No estacionario entre epocas: en Oct 20-22 (anclas B real, control misma ventana) el suelo era 37-39 ms (p50 40-43, n 4.220-11.389 filas q); en Nov 15-16 ms. La calibracion es POR EPOCA (el 22-Oct hubo Rescale del VPS: causa no verificada).

## 3. Anclas propias (ordenes reales ya enviadas; solo lectura) -- out_v2/anclas_*.json
- Sonda1 04-Nov (n=9 altas, 4 cancelaciones; `alta` + canal de usuario): RTT POST local p50 117 (min 64, max 232); sello EXCHANGE de aceptacion menos envio p50 79 ms (42-175); ack menos sello exchange p50 31 (22-76); canal usuario rx-ex p50 16 (15-28), igual al suelo del feed publico. Cancelacion: sello exchange menos envio p50 35 (32-46, n=4), RTT 56-66.
- B real 20-22-Oct (n=9 anclas utiles de 3 dias con 405/1.121/1.746 pujas; solo vale cuando la puja cambia el top del libro; 15 pujas candidatas en el top, 6 ambiguas o sin fila q coincidente): sello exchange del alta en el feed publico menos `t_call0` p50 ~56 ms (48-113); recepcion menos `t_call0` p50 ~93; recepcion menos `t_ret` +3..+16; rx-ex de NUESTRO alta 37-53 ms = igual al suelo de esa epoca (control 37-43): el feed no retrasa mas a nuestras ordenes que al resto.
- Lectura: `t_arr_ex` (aceptacion en el exchange) = envio + 48-56 ms (B, Oct) / +42-175 p50 79 (Sonda, Nov, n=9): LAT_POST=68 del motor es conservador en B y OPTIMISTA en la mitad de los casos de Sonda. Con n=9+9 no hay IC; no se cambia ningun parametro. Anclas publicas de Sonda: 8 de 9 con >1 candidato (+5 en nivel 0,01 muy poblado) -> no usables; solo 1 (rx-ex 17, user_ex-pub_ex -1 ms: ambos canales llevan el mismo sello).
- NO verificado: offset real exchange-local (un sentido de la red); anclas de Sonda en el feed publico (ambiguas); anclas >=26-Oct (ninguna orden propia con t_send identificable fuera de B 20-27-Oct y Sonda 04-Nov).

## 4. Condicion 1 de INTEGRIDAD: tf y aceptacion con reloj correcto, 03-Nov (out_v2/condicion1_2026-11-03.json)
| modo | rellenos G0 | pnl rb0,2 | EV | L2 valido (n / pnl / EV) |
|---|---|---|---|---|
| original (q11) | 287 | 2,66 | +0,0124 | 141 / -53,68 / -0,5117 |
| legacy v2 | 287 | 2,66 | +0,0124 | 141 / -53,68 / -0,5117 (identico) |
| causal | 287 | 2,66 | +0,0124 | 141 / -53,68 / -0,5117 |
| rx | 286 | 3,45 | +0,0161 | 141 / -53,68 / -0,5117 |
- Cambia `tf`: causal vs legacy, 272 de 287 emparejables por (k,L,seg): dtf p50 0, p5 -115, p95 +47, p99 +119 ms, |dtf|<=50 ms 93 %, 55 % identicos; 15 rellenos cambian de segmento pero con el mismo pnl total (-6,12). rx vs legacy: dtf p50 +23,5 ms. Origen: 62 % de los sellos de la cinta usaban el fallback `recv-63` (30.621 de 50.844 eventos); en causal el fallback es `t_ev` del tx (exchange): 29.530; caida L1 19.926.
- Aceptacion §4 completa (1.350 rellenos 03-07, EV -0,2447): NO recalculada con reloj causal (solo 03-Nov hecha: EV L2 valido sin cambio, ni de signo ni de 1 EUR). Aceptacion 03-07 con modos legacy/causal esta en la cola C (ver §6).
- Hecho nuevo: en EXCHANGE el print (`t_ev` de libro5_tx) llega p50 187 ms DESPUES de la caida L1 que lo evidencia (19.908 de 49.438 eventos con caida localizable en [recv-400, recv]; IQR 59-292; 99,8 % positivos; out_v2/diag_print_vs_caida_2026-11-03.json). lag_print-lag_caida ~0: el retraso del print no es de transporte. Matiz: la regla de busqueda (primera transicion en 400 ms) puede emparejar caidas ajenas; NO es una calibracion del 63 ms. Su uso correcto: tm de causal = caida L1 con sello exchange o `t_ev`; no es una correccion constante.

## 5. Decisiones del Paso 0 afectadas (provisional; sin cambiar reglas ni umbrales)
- E1 KILL (placebo grupo p=1,0, 15 dias, Lambda 150-560) y X1 KILL (12 variantes Delta<0): desfase p50 17-18 ms <= 13 % de Lambda=150 y 7 % de d_det 250: NO esperable que cambien; verificacion con reloj causal sobre los 15 dias en curso (§6). X1 usa sa_ms para el ESTADO FISICO del libro: reloj exchange (paso0_lib_v2.x1_dia(clock='ex', fuente='v2')).
- Q2(3) "reduccion-L menos print -228 ms": mezcla EX/RX; en un mismo reloj ~ -209 ms o menos; con el hecho de §4 (print +187 ms en exchange) la comparacion exige re-hacerse en un reloj; no afecta a KILL.
- "Reduccion L vs tf |dt|<=50 ms 37 %": resolucion del orden del desfase (17 ms) y de dtf p5..p95 = -115..+47 ms: no interpretable a 50 ms con el reloj antiguo.
- LAT_POST=68 vs anclas (n=9+9): sin cambio propuesto; reportar sensibilidad a +/-30 ms en cualquier informe de maker.
- Cambios de codigo de integridad (cond. 2): paso0_lib_v2.py: `assert ... or True` sustituido por RuntimeError y conteo (`U.attrs['n_rellenos_sin_segmento']`); el original (hash en A1) NO se edita. Conteo en 03-Nov: 0 (test: test_assert_real_rellenos_sin_segmento).

## 6. Pendiente / cola (PARTIAL honesto)
Corre run_relojes_C.sh (pid en out_v2/run_C.pid, log out_v2/run_C.log; espera 06-09Z; idempotente): extrae v2 de 26-Oct..09-Nov (un dia cada vez), passT causal 15 dias, regresion de paso0_lib_v2 con fills originales (out_v2/paso0_orig), E1/N1 y X1 con reloj causal (out_v2/paso0_causal), aceptacion 03-07 legacy vs causal (out_v2/condicion1_2026-11-03_..._2026-11-07.json). Hasta que acabe: NO se puede afirmar que E1/X1 sigan KILL con reloj causal en los 15 dias.
Reproduccion: `cd experimentos/5m_barato/l2_carrera_10nov && bash run_relojes_A.sh && bash run_relojes_C.sh` (nice 19, ulimit 3 GB, fuera de 06-09Z). Tests: `python3 -m pytest -q test_relojes.py` (6 OK).
Siguiente: statistical-validator (n efectivo por cierre/dia, ponderacion por EUR, criterio de dia valido incluyendo H1 de Binance, veto >=85 %) y alpha-miner (reabrir E1/X1 con prerreg propio SOLO si C cambia el signo; si no, siguen KILL).

## 7. Registro de ejecucion (fail loud)
- 09:01-09:53Z: A (extraccion/calibracion/condicion 1/anclas) completada tras 3 aborts por MemoryError con ulimit 3 GB (arreglos: columnas int32, ordenacion columna a columna, OPENBLAS/MALLOC_ARENA_MAX=1, Day2 con `otro(i)` int32). Logs: out_v2/run_A_parte1.log, run_A.log, run_C_abortado1..4.log.
- C relanzado 09:53Z (pid out_v2/run_C.pid, log out_v2/run_C.log); ETA E1/N1/X1 causal ~11:45Z; resultados finales en out_v2/paso0_causal/*.json, out_v2/paso0_orig/*.json (regresion), out_v2/condicion1_2026-11-03_2026-11-04_2026-11-05_2026-11-06_2026-11-07.json. Comprobar con `tail out_v2/run_C.log` (fin = `PARTE C COMPLETA`).
- Cambios NO commiteados (todo en experimentos/5m_barato/l2_carrera_10nov/, sin tocar dev, main live, crons ni procesos ajenos). Datos: datalogs/sa_ms2/ms2_<D>.npz (+manifest).
