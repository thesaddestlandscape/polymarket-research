# PREREG E-RE-BR-01 — descomposición económica de B sin condicionar al relleno (escrito ANTES de calcular; manda mtime+sha)
Datos fijos: ledger `DL/experimento_h47_B_ledger.jsonl` (puja_post: precio, libro al pujar, t_dec), `DL/etiquetado_pasivo_B/etiquetado_B_2026-10-2{0..3}.csv.gz` (unidad orden: acc_llena CORREGIDA por calibracion_etiqueta enmienda 1; gana_lado oficial), `contabilidad_wallet_dedicada/posiciones.csv` (tanda_B, verdad de PnL). Solo lectura.
Definiciones (por €, ponderado por €, maker fee 0, rebate aparte):
- puja = (mercado, lado) cadena de órdenes; m0 = mid del libro en la PRIMERA orden de la puja; b0 = mejor bid ahí.
- Para rellenos (órdenes con acc_llena>0): EV_f = Σacc·(gana−pc)/Σacc·pc = SPREAD + SEL + COND, con
  SPREAD = Σacc·(m_o−pc)/Σacc·pc (m_o = mid al armar ESA orden; captura de nivel/spread),
  SEL = Σacc·(g_u − m0)/Σacc·pc evaluado con el promedio NO condicionado de la puja (ver U), 
  COND = resto = EV_f − SPREAD − SEL (condicionamiento al relleno + deriva m0→m_o).
- U (no condicionado, todas las pujas armadas, 1 por puja, peso = coste nominal armado 1ª orden): Σw·(gana−m0)/Σw·m0. Mide dónde/cuándo elige pujar B (calibración + selección mercado-momento), sin condicionar al relleno.
- P(fill) por orden, por puja y por mercado.
Preguntas y decisiones:
Q1 P(fill) por puja. Si está en [0,38-0,68] (±15 pp del 52,8 % virtual de F8), el argumento «virtual 52,8 % vs real 5,1 %» es una comparación de UNIDADES (orden vs vida) y queda INVALIDADO como motivo de rechazo; la transferencia F8/mitigar_as pasa a REQUIERE_REMEDIR por puja. Fuera de ese rango, el argumento se mantiene.
Q2 Componente dominante de EV_f: el de mayor |valor| entre SPREAD, U·(peso) y COND, con IC90 por cierre (bootstrap 2.000 por slug-cierre). Si |COND| > |U| y COND IC90<0 ⇒ la palanca es de EJECUCIÓN (cancelar/nivel); si |U| ≥ |COND| y U IC90<0 ⇒ SELECCIÓN (dónde/cuándo, p. ej. R0); si ambos IC cruzan 0 ⇒ G (sin n).
Q3 Consistencia: EV_f por órdenes (corregido) vs posiciones.csv: diferencia ≤0,02 €/€ o se reporta como discrepancia.
Q4 Rebate: valor por € = 0,2·0,07·(1−p) a la p media de rellenos; ¿supera B el suelo de pago (~1 $/día ⇒ ≥89 €/día de coste relleno, rebate_ganadores)? Volumen diario real de B por día.
No se ajusta nada tras ver resultados; cualquier corte adicional se marca POST-HOC.
