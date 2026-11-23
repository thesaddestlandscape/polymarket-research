# DICTAMEN_VALIDADOR_23nov (statistical-validator, 23-Nov-2026 ~20:10Z; guardado por el chief)
Sin EV ni PnL de días ≥18-Nov leído. Sha verificados OK: PREREG 16be06b6, ADENDA_CRITERIOS 0953109e, ADENDA_K6 3a3efc47, CONTRATO_CALMA, CONTRATO_CXB60_REEVAL 539dbf2d, INFORME_DATOS. FAILED: run_hbgap.sh (rehecho por el chief tras el arreglo de la puerta de carga; copia previa en hbgap.sha256.pre_fix_carga).

0. ALERTA: rf5A_2026-11-18.pkl y rf5_f5_0_2026-11-18.pkl (pnl de un día ciego) generados a las 19:13Z, antes de las adendas → PRECINTADOS (PRECINTO_CIEGOS_18nov.txt, chmod 000, prohibido abrirlos). El 18-Nov es INCOMPLETE por 3a. Causa: con_tx/units calculado sobre la cinta ya filtrada a horas sanas (comprobación vacía).
1. ADENDA_RF5_CRITERIOS: APRUEBA_CON_CAMBIOS C1-C4. Umbral 22/24 razonable; no retroactividad correcta. d±1 completo: 1/13 días válidos en 10-22 Nov frente a 3/13 aplicando la regla solo a d. Exclusiones posiblemente ligadas al volumen: publicar descriptivos. Desenlace 0,80 insuficiente. t_proc = 1 ms y tabla de suelo sucesora: aceptados con el límite declarado.
2. ADENDA_RF5_K6_CALMA: APRUEBA_CON_CAMBIOS C5-C7.
3. CONTRATO_CALMA_T1_PASST_V4: APRUEBA_CON_CAMBIOS C8. CONTRATO_CXB60_REEVAL: APRUEBA_CON_CAMBIOS C9 (coherente con CXB60 fuera de K1-K6, decisión de Javi 23-Nov).
4. maker_ms 16-22 Nov: cobertura de segundos 92,5-99,1 %, ninguna hora por debajo de 3010/3600 s; reinicios de 42-47 s; cortes: 20-Nov 06h ~175 s, XRP 72-126 s. 19-22 VÁLIDOS en maker_ms para CXB60. El detector hueco_feed de CXB60 está degenerado (100 % true, vac_max 50-59 s) y cxb60_informe.py:38 lo cuenta como 0 (cadena sin espacio).
5. Nulo por filtrado posterior: RECHAZA para uso confirmatorio (ver test 3).

## Cambios para el agente de datos
- C1 (3a): «f_horas(d)>=22/24; en d−1 y d+1, sanas todas las horas que lee la simulación de d (lista declarada por el engineer con sha; por defecto 23h de d−1 y 00h de d+1). con_tx/units se calcula sobre TODAS las unidades, antes de filtrar horas.» + publicar volumen y volatilidad de excluidos frente a válidos y el resultado por bloque horario.
- C2: precintar los pkl del 18-Nov (HECHO por el chief) y declararlo en el ledger.
- C3 (3b): «frac_c = lados mercado-lado con relleno y desenlace oficial / lados con relleno, también ponderado por €. Válido si frac_c >= 0,99 en ETH, SOL y XRP tras el resolvedor hasta D+3; por debajo, PENDIENTE (terminal en D+3). El gate debe pasar TAMBIÉN con la cota de peor caso (relleno sin resolver = −coste).»
- C4 (BTC), condiciones añadidas: (6) tabla de suelo sucesora con BTC lo-válido + sha; (7) puertas C1/C3 para BTC y para los días 03-17 de los cortes; (8) equivalencia bit a bit ms_extract_lowmem frente a ms_extract (ETH, un día común); (9) Binance BTC (m5_registro) para V5/V6 de K1b; (10) maker_ms con tokens BTC 5min en todos los días 03-17 antes de p20/p80.
- C5 (K6 B): el max-statistic K1-K4 se queda como está firmado; K6 se contrasta solo si K1 = COMBINADA_EV_POSITIVO, con α=0,05 heredado. Gate de K6: Delta(K6−K1) pareado sobre los mismos días y órdenes, IC90 por días y por cierre con límite inferior >0, y Delta > placebo de Calma (p≤0,05; desplazamiento circular ≥60 s de los disparos, misma tasa). Si K1 no pasa, K6 queda DESCRIPTIVO. (Alternativa, si se elige antes de firmar: reserva α 0,04 para K1-K4 / 0,01 para K6.)
- C6 (K6 D): días de K6 = intersección de evaluables para K1 y K6; K1 también se publica sobre ese subconjunto; NO_EVALUABLE fijado por el manifest de entradas antes del EV; si NO_EVALUABLE >20 % de los días válidos → K6 INSUFFICIENT.
- C7 (K6 A): leave-one-out K6−F3, K6−V5 y K6−V6; partición exhaustiva por PRIMERA regla que cancela (F3/V5/V6/Calma/ninguna) con indicadores de «también habría disparado», y n, coste y PnL que suman el total; Calma∩F3 = 0 comprobado con un test.
- C8 (Calma): §4 «Unidad = (mercado, lado) con ≥1 alta intentada; PnL = el del 1.er relleno (CONTRATO_E1B §4); sin relleno = 0». §8: fuente real ms_D.npz ← maker_ms, hora sana = hueco máximo de recepción por moneda <60 s y ≥80 % de segundos con datos. CXB60 fuera, explícito.
- C9 (CXB60_REEVAL): (a) primaria CXB60, max-statistic sobre las 6 variantes; (b) puertas de sus propias entradas (maker_ms como en C8, desenlace como en C3, suelo); horas de libro5_tx solo si el sello passT_v4 las lee (lo declara el engineer; si las lee, 19-22 INCOMPLETE para la reeval); (c) días 13-17 en tabla aparte, el contador ≥10 solo cuenta días ≥18; (d) ningún veredicto condicionado a la mirada 1; (e) para B_CXB60×F5, todo día anterior a su firma es exploratorio; (f) sustituir hueco_feed por la auditoría a nivel de fichero, con sensibilidad que excluya los mercados cuya ventana solapa un hueco real ≥5 s; (g) comprobar que los mensajes de Telegram del vigía de CXB60 no publicaron EV de 18-22.
- C10: re-hashear run_hbgap.sh (HECHO por el chief).

## Tests para el engineer
1. El (i) se calcula sobre unidades sin filtrar: 18-Nov → INCOMPLETE; el evaluador se salta por código todo rf5dia que no esté COMPLETE.
2. Desenlace por moneda con relleno sin resolver: la cota de peor caso cambia el EV.
3. Nulo exacto en el simulador: todos los estadísticos de gate salen de la simulación. Verificar con un test que b_policy_sim no acopla mercados. Réplicas por día: base, veto a todas las Up, veto a todas las Down. Permutar el par (F5_0^Up, F5_0^Down) entre mercados dentro de día×moneda; para un lado que la base no intenta, F5_0 sale de la réplica con el otro lado vetado. Debe reproducir bit a bit la réplica directa de F3 del 17-Nov (57/59 lados).
4. Familia K: el desplazamiento circular de V5/V6/Calma exige volver a simular; K ≥1000 (o Besag-Clifford con h=20); p=(1+#{T*≥T})/(K+1) (no .mean()).
5. Tests 1-9 de la adenda E; K6 sin Calma == K1 bit a bit; conservación de órdenes en la partición de C7.
6. Detector de huecos de CXB60 + parseo del informe (aceptar «": true"»): en los mercados, vac_max p50 debe bajar de ~55 s a <10 s.

Auditoría: scratchpad del chief (gaps.awk, run_gaps.sh, sum.py, gaps_2026-11-16..22.txt). Ninguna etiqueta autoriza operar.
