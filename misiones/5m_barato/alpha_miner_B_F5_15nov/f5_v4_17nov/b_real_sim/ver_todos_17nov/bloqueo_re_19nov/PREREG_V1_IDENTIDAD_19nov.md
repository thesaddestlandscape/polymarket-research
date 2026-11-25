# PREREG V1 — identidad de mensaje del resto en reposo del tomador (RE bloqueo B). 19-Nov ~09:45Z, ANTES de medir. Solo lectura, 0 ordenes, no EV.
Datos: libro5_ms_2026-11-17_185094.csv.gz (+ si da tiempo 2026-11-17_3094008) [volumen libro5_ms_prot] y onchain_fills_2026-11-17.csv.gz (+18 si el tramo cruza). Universo: tokens 5m presentes en el tramo libro5.
## Verdad on-chain (Nov, tomadores PUBLICOS)
Fila de la orden TOMADORA = OrderFilled con taker == exchange (0xe111180000d2663c0091e4f400237545b87b996b); order_hash = hash de la orden tomadora; maker = wallet tomadora; side 0 BUY / 1 SELL del token_id.
REST+ (resto en reposo PROBADO): el mismo order_hash aparece despues (bloque > bloque de tx1) como fila MAKER (taker != exchange). Precio limite p_lim = precio de esa 1a fila maker (USDC/acciones). REST? = tomadora sin aparicion maker posterior (FAK, llena, o GTC cancelada: no identificable sin calldata).
## Reglas WS (reloj: recepcion rx; rasgos solo con filas <= t)
Incremento = subida de tamano de un nivel (token, lado, precio) respecto a su estado previo (B snapshot o d), en filas d o B.
- V1a (mismo lote rx): incremento cuyo rx == rx de una fila T del MISMO token o de su complementario.
- V1b (mismo evento): V1a con ademas t_ms del incremento == t_ms de la T.
- V1c (= R4 de ADENDA_A2): |rx_inc - rx_T| <= 2 ms.
Para un REST+ con orden BUY de X a p_lim, el resto se busca como incremento en X lado B a p_lim (o espejo: complementario lado A a 1-p_lim); SELL: X lado A a p_lim (o comp lado B a 1-p_lim). Emparejado REST+ <-> T: T de X o comp con rx en [ts_est_tx1 - 8000, ts_est_tx1 + 1000] ms; si hay varias, cualquiera que cumpla la regla (se reporta cuantas candidatas).
## Metricas
recall_V = REST+ con incremento que cumple V / REST+ con cobertura libro5 (tx1 dentro del tramo y token visto).
precision_lb_V = disparos de V (incrementos en X o comp a cualquier precio en el mismo lote que una T) cuyo (token o espejo, precio) coincide con un REST+ cuyo tx1 cae en [rx+0, rx+8000] / disparos. Es COTA INFERIOR (GTC cancelados sin relleno cuentan como FP).
Precision de nivel (la util para B): restringida a disparos al precio del lado opuesto de la T (resto = mismo precio que limite del tomador; se reporta tambien sin restringir).
Placebos: (i) tick +-0,01 sobre REST+ (recall placebo); (ii) temporal: misma regla contra pseudo-T en rx_T + 10000 ms (tasa de disparo y precision).
Tamano: para aciertos, ratio delta / R_lb (R_lb = suma acciones de las filas maker posteriores del hash); compatible si delta >= 0,98*R_lb.
Informativo: fraccion REST+ entre todas las tomadoras 5m del tramo (dimensiona el canal GTC vs FAK).
## Aceptacion (fija)
Regla V aceptada como identificador si recall_V >= 0,50 Y recall_V >= 3x placebo tick Y precision_lb_V (nivel) >= 0,30 Y disparo placebo temporal <= 0,2x disparo real. Elegida = la que pasa con mayor precision (empate: mayor recall). Si ninguna: INSUFFICIENT y se reporta el dato que falta.
Multiplicidad: 3 variantes, 1 tramo; cualquier cambio post-medicion = adenda declarada.
