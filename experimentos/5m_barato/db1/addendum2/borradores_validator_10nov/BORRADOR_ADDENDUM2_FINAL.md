# ADDENDUM2 a PREREG_DB1 (§6, RMR): definicion operativa de "rafaga" — TEXTO FINAL BORRADOR (validator), NO congelado
Base: ADDENDUM2_PROPUESTO.md (alpha-miner, 10-Nov 08:45Z; criterio previo sha 18310f5f61f380a0…, 08:26:05Z). Se mantienen sus §2-§4, §6-§9
tal cual. Cambios del validator (i)-(iv) + dos aclaraciones; todo lo nuevo esta marcado.

## 1. Regla (sin cambio de fondo)
R0 se mantiene como definicion oficial de rafaga en RMR. Estatus: DESCRIPTIVA (contable). Poder discriminante general: INSUFFICIENT_EVIDENCE.
(ii) [NUEVO] La definicion normativa es el CODIGO de passdb.py (sha256 7ce11b651988b50f…, lineas 21 y 219): BAND_MAX = 0,20; cuenta
bids side 0 con pr <= BAND_MAX + 0,0049; rafaga = >= 2 tomadores distintos (excluidas CHAIN_CONTRACTS) por (bloque, mercado). Las cifras
de add2_* son una REPLICA APROXIMADA (suelo de extraccion 0,03: no cuenta bids 0,01-0,02, marca como mucho menos rafagas).
(iii) [NUEVO] Clausula de coherencia (POST HOC, efecto nulo en DB1 por construccion): passdb.check_band ya aplica, de forma ruidosa,
assert max(LEVELS de TODAS las variantes, incl. @CROSS/@STRICT/@OPT/@THIN) <= BAND_MAX y sobre el L de RX; debe tener test propio.
Si RMR se calcula sobre rellenos REALES de B o brazos con niveles > 0,20, se usa R2 (bids <= 0,40) y se reporta aparte.
(iv) [NUEVO] La etiqueta usa el bloque ENTERO (~2 s; incluye tomadores posteriores a nuestro relleno): es contable y NUNCA ex ante.
Ninguna regla de decision (brazo, cancelacion, filtro) puede usarla; el uso ex ante requiere reloj propio (ver H-DB3).
Apoyo en S_sim (−0,307 vs −0,062; n=3.591): IN-SAMPLE respecto de los quemados de DB1 (mismos dias); descriptivo, no es evidencia de brazos.

## 5.1 Placebo temporal — (i) [CORREGIDO, POST HOC; sustituye "No se corrige a posteriori"]
Defecto: comparar Δ de la regla con Δ de P-temp con coberturas 10x distintas (2-6 % vs ~35-50 %) no es una comparacion valida.
Criterio (b) corregido, para todo informe RMR futuro:
 - P-temp con la MISMA cobertura en € que la regla (±10 %), ensanchando la ventana desplazada hasta igualarla; o comparar V_adj = cob × Δ.
 - P-temp PASADO (−15 bloques) y FUTURO (+15) por separado; solo el pasado es informativo de algo accionable. (Hoy add2_dia.py los mezcla.)
 - IC90 por dia (bootstrap 2.000, semilla 20261110).
Efecto en DB1: ninguno (R0 es el statu quo y es descriptiva). Si con el criterio corregido una alternativa superase a R0, NO cambia la
etiqueta de DB1: abre un prerregistro nuevo.

## 5.2 Episodios -> H-DB3 (aclaracion)
"−0,154 vs +0,024 (14/20 dias)" es descriptivo, en S_pop (no en exposicion G0), sin IC, condicionado a la 2.a mitad (post hoc) y sin
artefacto reproducible en addendum2/out (no se encontro): no es base cuantitativa. H-DB3 va en prerregistro aparte.

## 6. BTC: DATA_BLOCKED; R0 satura (95,7 %). Definicion propia solo en contrato BTC-DB1-DESC.
