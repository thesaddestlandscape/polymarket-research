# PREREG V3 — modelo de CANCELACION de B como funcion del libro (replay mecanico + carrera de latencia). Congelado ANTES de correr nada de V3 sobre TEST (22-23 Oct).
Hora: la del mtime de este fichero y su sha256 en PREREG_V3.sha256 (no una hora escrita a mano).

## Lo ya visto (honestidad)
- TEST 22-23 Oct ya mirado EN AGREGADO en rondas 1 y 2 (P_puja real 49,7 %; Capa G P_puja 29,3 %, AUC 0,633; placebo +90 s 35,1 %, AUC 0,625; EV real -0,321). NO es hold-out virgen. Nada de V3 (modelo M) se ha calculado sobre TEST.
- Pista post-hoc del validador (3 grupos de rellenos, 20-23 Oct, INCLUYE TEST): sin print visible n=36 EV -0,65; carrera n=62 +0,26; dentro n=104 -0,13. Al haberse hallado con TEST dentro, NO puede confirmarse con TEST: queda EXPLORATORY pase lo que pase aqui.
- Visto en TUNE (20-21 Oct) para construir M (permitido): la regla de B esta en el codigo (dev experimento_maker_h47.py, H35 DEEP_PEG): puja en objetivo_h35(top bid, top ask, k) (k eth 2, sol 1, xrp 1), bid top en (0,11-0,30], cancela/repega cuando el objetivo cambia, una sola puja por mercado, un relleno cierra la puja, ASENTAR 1,5 s antes de reponer, parada a T=60 s. Fidelidad en TUNE (t0_salida.txt): objetivo reconstruido con el libro q grabado = precio real en 89,4 % de 1.526 ordenes; react (intencion_cancel - primer cambio del objetivo en el libro grabado) p50 145 ms, |react|<=300 ms 71 %, >1 s 6 %; post_half p50 94 ms; asentar p50 1.757 ms (75,8 % <=3 s; el resto son esperas de banda/saldo). Corrida unica de M en TUNE (t1_tune_salida.txt): P_puja M 0,620 vs real 0,616, AUC 0,790, placebo +90 AUC 0,554, Mdet AUC 0,721; vida 1a orden mediana real 698 ms vs Mdet 446 ms, Spearman 0,644; ordenes/puja real 8,6 vs M 13,2 (B real se frena por saldo/max_vivas: 804 bloqueo_suelo_saldo en el ledger; no esta en el libro y M NO lo modela). Grupos en TUNE (depuracion de t3): DENTRO 59, CARRERA 36, SIN_PRINT 14; recall M 0,78/0,88/0,51 vs placebo 0,65/0,65/0,60. Los umbrales de abajo se fijan DESPUES de ver TUNE (legitimo) y ANTES de TEST.
- Nada se re-ajusta con TEST. Si algo falla, se reporta.

## Modelo M (fijado; hashes abajo)
Para cada puja real de TEST (token, inicio = t_dec de su 1a orden real; mismo inicio que la Capa G de v2): maquina de estados de B sobre el libro q grabado por RECEPCION: decide en t_dec con el objetivo del libro en ese instante (si no hay, espera al primer objetivo valido + react); orden en el libro desde t_dec+post_half; intencion de cancelar en (primer cambio del objetivo en filas de libro valido) + react, o en T=60 s; ventana [t_ini, t_cancel+30 ms]; relleno = regla de la Capa 1 de v2 (e=250 ms, g=0,5, f=0, elegida solo en TUNE); si no rellena, siguiente decision en t_cancel + asentar. Latencias muestreadas de las distribuciones EMPIRICAS de TUNE (tune_latencias.json; react en (-300, 3000) ms de no rellenas, asentar <=3 s), 20 replicas por puja, semilla 7 -> P_puja_M. Mdet = medianas. Placebo M_PL90 = mismo libro, prints desplazados +90 s. NO usa Binance, profundidad, cola, ni el estado de saldo de B (hazard estadistico con esas variables NO se ajusta: la regla es determinista del top del libro; se informa como hipotesis rival H2 a discriminar por C6).
Comparadores: Capa G de v2 (test_capaG.csv: P_G, P_PL+90) por la misma puja. El placebo -90 s NO se usa (degenerado, validador 3c).

## Criterios en TEST (22-23 Oct, 187 pujas, IC90 bootstrap por CIERRE = cie, 2.000 reps, semilla 11; IC por DIAS no estimable con 2 dias: se informa por dia)
C1 calibracion: |media P_M - real| <= 0,10 y su IC90 contiene 0.
C2 discriminacion: AUC(P_M) >= 0,70.
C3 placebo: AUC(P_M) - AUC(P_M_PL90) >= 0,10 y IC90 inferior > 0.
C4 mejora sobre G: IC90 inferior de AUC(P_M) - AUC(P_G) > 0 y |sesgo M| < |sesgo G|.
C5 dias: |P_M - real| <= 0,15 en cada dia.
C6 vida: Spearman(vida real 1a orden, vida Mdet 1a orden) >= 0,4 y mediana Mdet/real en [0,5, 2].
C7 informativo: EV/EUR de M (relleno esperado x (gana - precio de relleno simulado), 5 acc) vs real on-chain, IC90 por cierre.
Veredicto: MEJORA_CALIBRADA = C1..C6; MEJORA_PARCIAL = C2, C3 y C4 (falla C1, C5 o C6); NO_MEJORA = falla C2, C3 o C4.

## Los 3 grupos de rellenos (t3_grupos.py, definicion fijada)
Cada orden real rellena on-chain, con su ventana REAL [t_ini, t_fin] y la regla de consumo (cualquier tamano): tp = primer print consumidor en [t_ini, t_fin+250 ms]. SIN_PRINT si no hay; CARRERA si hay t_cancel_int y tp > t_cancel_int; DENTRO en otro caso. A nivel puja, el grupo de su 1a orden rellena.
Tratamiento: (a) prediccion (informativa, no decide el veredicto): en TEST, P_M - P_M_PL90 > 0 en DENTRO y CARRERA y <= 0,05 en SIN_PRINT (M no ve lo invisible). (b) EV por grupo en TEST se reporta como REPLICA NO INDEPENDIENTE (la pista se hallo con estos dias): EXPLORATORY siempre. Confirmacion solo con ordenes reales de B posteriores al 23-Oct (no existen: ultimo puja_post real 23-Oct ~08:55Z): criterio para cuando existan: EV(SIN_PRINT) < EV(resto) con IC90 por cierre de la diferencia < 0, n>=30 rellenos SIN_PRINT, >=5 dias.

## Hashes (sha256, 16 primeros)
664f830a4950c811  v3lib.py
6f3a92869f298d72  t1_sim.py
e883bb4f85b5cf4f  t2_eval.py
9857dc4f602a71fc  t3_grupos.py
e6dcdf6f56333ff0  tune_latencias.json
587004ef49411844  ../datos_tune_sel.json
678afbfa46557ae5  ../v2lib.py
