# CAUSALIDAD del "print +187 ms después de la caída L1" (11-Nov-2026, solo lectura, TRAIN 26-Oct..09-Nov; HOLD >=10-Nov NO mirado)
No modifica PREREG_L2_V2 ni ADDENDUM_A1. 0 órdenes. Código y salidas: `causalidad_187ms/` (scripts + `*_salida.txt` + `HIST_<D>.json`).
Pickles intermedios (EMP_<D>.pkl, G0_cxbtrue.pkl) en scratchpad de sesión (efímeros): se regeneran con `emparejado.py D DIR` (~15 s/día, RSS 0,7 GB, ulimit 1,5 GB).

## 0. Veredicto
**ARTEFACTO de emparejado (c), con la parte (b) como mecanismo.** El retraso real print<-casado es **~20 ms**, no 187 ms.
- Regla vieja (diag_print_vs_caida.py = passT_v2 causal = passT_copia legacy = verif_real/verif.py l.43-55): "primera transición bid>pmin -> bid<=pmin
  en [recv-400, recv]". Para un print de UN solo nivel en el mejor bid (pmin = bid), el bid ya es <= pmin antes del casado: la transición que
  encuentra NO es el consumo sino el instante en que pmin PASÓ A SER el mejor bid (retirada/consumo del nivel de encima). Además la ventana solo
  mira hacia atrás (0-400 ms): el 99,8 % "positivo" y la mediana ~187 (≈ centro de la ventana) son de construcción.
- Prueba: de 237.259 emparejados viejos de un nivel (npr=1, 76,3 % de los 310.948 viejos, 15 días), **0,0 %** coinciden con la fila de consumo
  exacto (ni con la laxa); en barridos de 2 niveles sí 96,7 %. Viejo menos verdadero (190.218 con emparejado exacto único): p5/p25/p50/p75/p95 =
  0/33/144/251/359 ms. La transición vieja es un relleno previo del nivel superior en 12-22 % y retirada/otro en 78-88 % por día (`comp_salida.txt`).

## 1. Emparejado independiente (`emparejado.py`)
Unidad = (token, tx) de la cinta ON-CHAIN (`precursores_barrido/out/tape_D.pkl`: fills maker BUY de m5_onchain con tx, log_index, maker; src tx_ws)
unida por HASH de tx (exacto) a `libro5_tx` (t_ev EXCHANGE, recv RX). Firma en filas q de `sa_ms2/ms2_D.npz` (reloj EXCHANGE, mismo campo t_ev del
WS): bid == p antes y (bid == p y szb baja EXACTAMENTE S = Σ acciones del tx a ese precio, ±0,015) o (bid < p y szb previo == S). Barrido (npr>=2):
una sola fila que salta de bid>=pmax a bid<=pmin. Ventana SIMÉTRICA ±1.500 ms alrededor de t_ev. Placebo: misma búsqueda con t_ev ±20 s (mismo token).
log_index no se usa (el libro agrega por nivel). Relojes: d_ex = t_ev(print) - ex(fila q) (EX-EX, no depende de la época); d_rx = recv(print) - rx(fila q).

| | valor (15 días, 765.315 eventos) |
|---|---|
| tasa con >=1 firma exacta / exactamente 1 (sin ambigüedad) | 87,9 % / 62,6 % (478.720); sin firma 12,1 % (lotes que mezclan tamaños) |
| ambigüedad por tamaño | S<=5 acc: 53,5 % únicos; 5-10: 72,4 %; 10-50: 67,4 %; >50: 45,6 % (34 % sin firma) |
| **d_ex único p5/p25/p50/p75/p90/p95** | **16/18/20/23/33/76 ms**; negativos 0,5-0,7 %/día |
| d_rx único (lo que ve una decisión) | 5/17/20/24/36/84 ms |
| pico real [0,60) ms vs placebo, por día | 16.564-64.278 vs 28-500 (contaminación <1 %) |
| estabilidad | p50 d_ex 18-21 ms los 15 días; idéntico en la época lenta (26-27 Oct, rx-ex p50 38-41 ms) y en la rápida (17-18 ms) |
| libro cruzado en la fila emparejada | 12-276/día (<0,5 %) |
Lectura de (a)/(b)/(c): (a) el feed de trades sale ~20 ms después del diff de libro del mismo casado (real, pequeño, p95 76); (b) la "caída"
vieja es en su mayoría una retirada del nivel de encima; (c) falso emparejamiento = 76 % de los emparejados viejos. Hay además un "hombro" de
firmas exactas a 100-500 ms (8-80 k/día vs placebo 0,2-3,4 k): consumos de igual tamaño en tx vecinas (operativa en racimo, muchos de 5 acc), no afecta a los únicos.

## 2. Qué conclusiones previas quedan afectadas (hay que RECALCULAR, no reinterpretar)
- **tf de G0 causal** (`out_v2/g0_fills_causal_ALL.pkl`, 4.616 rellenos emparejados): 58,5 % (2.699) vienen de la rama 'drop' (mal sellada); en 'thru1'
  (2.042 de esos) el relleno real ocurre p50 **+163 ms** después del tf usado (p5/p95 de toda la rama: 0/+360). La rama 't_ev' (41,5 %) está 18-20 ms
  TARDE respecto a la fila de libro; `recv-63` (legacy) queda ~-28 ms (Nov) / ~-3 ms (Oct): la constante 63 era razonable, la regla de caída no.
- **Doble conteo en engine.fill_segment BASE**: ordena (t, tipo) con el libro (tipo 0) antes que el print; si el print va sellado >= la fila de libro que
  ya refleja su consumo, la cola "ahead" se descuenta dos veces (rellenos fantasma/tempranos en 'cola'/'nivel'). Afecta a la rama t_ev de causal
  (sellos +20 ms). Sello correcto = ex(fila de consumo) - 1 ms. NO cuantificado.
- **E1** (Λ 150/310/560 vs errores de tf p50 163 ms), **X1** (M = tf - t_top ∈ [150, 1500]: con tf viejo ≈ t_top los thru1 caían con M≈0 y quedaban
  fuera), **CXB/PCXB**, aceptación condición 1 03-07 (EV -0,2447), N1 (celdas por rellenos G0∧GEO6), "Q2(3) -228 ms", "reducción L vs tf |dt|<=50 37 %":
  **sus KILL/valores no pueden afirmarse hasta re-correr con tf corregido**.
- **T2 / TESTS_BARATOS "reloj ~0,01 de recall"** y AUDITORIA (recall 0,35 / precisión 0,71): `verif_real/verif.py` usa la MISMA regla (l.43-55) y las
  vidas reales tienen mediana 0,66 s: un desplazamiento de ~150 ms entra/saca prints del segmento. El dictamen "reloj ~0,01" no cubre este error.
- **Trampa de CLAUDE.md "print llega después... mediana 128 ms (341 barridos 26-Oct)"**: medido en un solo reloj, es ~20 ms (barridos npr=2: p50 22, p95 101).
  Propuesta para el chief: corregir la línea (no la edito).

## 3. Explotar el hallazgo (mandato Javi): lo que hay y lo que no
- NO existe una ventana causal de ~187 ms entre ver el consumo en el libro y el print: por recepción el print llega p50 20 ms (p95 84) después. Decidir
  por el diff de libro adelanta ~20 ms a quien decide por trades (y ~0,9 s a quien usa RTDS): ventaja real pero pequeña.
- SÍ es real (y es lo que medía el artefacto): cuando el bid cae por debajo de nuestra L (en 'thru1' el mercado ya vende por debajo), el vendedor que
  nos rellenaría llega p50 ~163 ms DESPUÉS de la caída visible. Decisión causal (solo info por recepción): **CXB-true = cancelar al ver bid < L**,
  efectiva en EX = t_trig_rx + l. Estimación de PRIMER ORDEN sobre los rellenos G0 de passT (no el motor; sin re-armado ni cola), TRAIN 15 días
  (`eval_cxb_salida.txt`, `eval2_salida.txt`, `kept_salida.txt`):

| regla | rellenos que quedan | EV/€ quedan (Σpnl/Σcoste) | IC90 por días | días+ | sin 2 mejores días |
|---|---|---|---|---|---|
| G0 (base) | 4.616 | -0,151 | | | |
| CXB reloj viejo l=60/100/150 | 1.127/1.192/1.237 | -0,037/-0,045/-0,054 | [-0,20;+0,14] aprox. | 7-8/15 | -0,145..-0,152 |
| CXB-true l=60 | 621 (401 cierres) | +0,052 | [-0,14;+0,26] | 10/15 | -0,037 |
| CXB-true l=100 | 714 (445 cierres) | +0,028 | [-0,17;+0,23] | 10/15 | -0,082 |
| CXB-true l=150 | 837 | -0,029 | [-0,22;+0,18] | 9/15 | -0,142 |
  Efecto INCREMENTAL de corregir el reloj (rellenos que solo evita el reloj verdadero): l=60: n=508, EV -0,143/€, pnl -54,0 € (Δ +54 €),
  IC90 por días del pnl evitado [-124,7;+16,9], 10/15 días negativos; l=100: n=479, -53,2 €; l=150: n=403, -33,4 €. Placebo de igual cobertura
  (día×L) del CXB entero: p=0,004-0,019, pero el placebo ya da +345..+435 € porque G0 pierde: el CXB "gana" sobre todo por operar menos.
  Motor real CXB150 con reloj viejo (RT_causal): n=1.736, EV -0,067 (mi aproximación no reproduce sus re-armados: no sustituye al motor).
- Conclusión: el reloj corregido mueve el CXB en la dirección buena (+33..+54 € en 15 días) pero **sin edge demostrado**: IC por días cruza 0, negativo sin
  los 2 mejores días, muy sensible a l (60 -> 150 ms cambia el signo) y l=60 supone cancelación aceptada ~40 ms tras ver la caída (Sonda n=4, 32-46 ms;
  en la época Oct la subida era ~2x). Etiqueta: EXPLORATORY in-sample.

## 4. Siguiente experimento (concreto)
1. `passT_v3.py causal_fix` (fichero NUEVO; no editar passT_v2/engine): tm = ex(fila de consumo exacta única) - 1 ms; si ambigua/sin firma, t_ev - 20 ms
   (constante POR DÍA = p50 d_ex de `agrega_salida.txt`) - 1 ms; eliminar la regla de caída. Mismas guardas (importa engine.run_segment/fill_segment,
   gate_vec, run_var). 15 días TRAIN, ~30 s/día con ulimit 3 GB (run_C.log) => ~10 min + extracción ya hecha (sa_ms2 15/15 días presentes).
2. Re-evaluar con `paso0_lib_v2`: G0 incondicional, E1, X1, CXB150/300/1000 + PCXB placebo, condición 1 (03-07), N1. Comparar fila a fila con causal.
3. `verif_v3` sobre 20-23 Oct con la misma corrección (constante de época: rx-ex 38-43 ms, d_ex 20) contra el ledger de B real por order_hash:
   precisión/recall nuevos (sustituye a T2).
4. Solo si CXB-true supera a su placebo PCXB y a G0 con IC por días >0 y sin 2 mejores días >0: prerreg propio (no reabre E1/X1 por renombrado).
Coste: ~1 h de CPU baja prioridad, 0 €, 0 órdenes. Datos: sa_ms2, tape_D.pkl, libro5_tx (D-1..D+1), g0_fills/RT_causal.

## 5. NO verificado (fail loud)
- Que `t_ev` de libro5_tx sea el sello del mensaje last_trade_price del mismo canal (no cruzado con las filas 't' de maker_ms).
- El doble conteo BASE: identificado por lectura de código, no medido.
- Firmas sin emparejar (12,1 %) y ambiguas (25,3 %): asumido el mismo retraso (fallback t_ev-20); los >50 acc tienen 34 % sin firma.
- Fills de tomadores contra pujas del complementario (mint) que no tocan el bid del token: fuera de la cinta side=0 por diseño.
- La estimación CXB-true NO es el motor (sin re-armado, cola, rem); n efectivo por cierre 401-490; HOLD no mirado; para 09-Nov se leyó libro5_tx del
  10-Nov solo para fechar tx del 09-Nov (igual que passT_v2/diag).
