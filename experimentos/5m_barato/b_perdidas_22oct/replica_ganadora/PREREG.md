# PREREG — Réplica de la ganadora W (0xb0f85baa…, «pspspsps5») en B · 25-Oct-2026 ~12:10Z
Congelado ANTES de calcular ningún EV con libro5. Agente dedicado (encargo chief 25-Oct). Solo lectura.

## Hipótesis ya cerradas por agentes previos (no se re-testean; se citan)
Información externa Binance/Chainlink/cross-asset/imbalance (senales_externas), q calibrada (H-A), escalera ingenua y
reposición (H-C), cartera carry+tickets (H-D), posición en cola por bloque, contraparte concreta, horas (uniforme),
inventario/salida (W nunca vende ni cubre el otro lado: |YES−NO|/(YES+NO)=1,00), rebate (~0,26 % del coste).

## Hipótesis nuevas (mutuamente excluyentes como explicación PRINCIPAL; K=5, alfa Bonferroni 0,01)
Universo: rellenos MAKER de compra (side 0, taker≠exchange) en 5m BTC a p<0,40, cierres 19..24-Oct (libro5 disponible).
DESC = cierres 19-21 Oct; OOS = 22-24 Oct. Desenlace oficial. EV ponderado por $ (Σpnl/Σcoste); IC90 bootstrap por CIERRE
y por día. Relleno = el de la población on-chain (cota optimista: condicional a relleno, sin cola nuestra).
Hora del casado tf = ts_est(bloque) − offset, offset calibrado con libro5_tx del 24-Oct (mediana).
Alta de una orden = último incremento Δ>0 del tamaño del nivel (token, B, p) en libro5 con |Δ−acc_fill| ≤ max(0,02; 1 %)
anterior a tf − 0,2 s (atribución aproximada; se reporta la tasa de casación W vs población).

H1 VIDA-CORTA: la edad (tf − alta) de las órdenes rellenas de W es menor que la de la población (mediana W/pob ≤ 0,5) Y en la
   población los rellenos de órdenes jóvenes (edad ≤ A, A = mediana de edad de W en DESC) tienen EV mayor que los viejos
   (brecha ≥ +0,05 con IC90 por cierre >0 en OOS). Política: pujar y cancelar a los A s, re-pujar.
H2 RECARGA-TRAS-BARRIDO: las órdenes de W se dan de alta ≤ X s (X=3) después de una operación en el mismo token (el nivel
   acaba de ser barrido) en mayor proporción que la población (≥ +15 pp) Y en la población esas órdenes ganan más que el
   resto (brecha ≥ +0,05, IC90 por cierre >0 en OOS). Política: tras un barrido vendedor, recolocar pujas en ≤68 ms.
H3 PROFUNDIDAD-EN-ALTA: W da de alta sus órdenes k≥2 ticks por debajo del mejor bid del momento (proporción ≥ +15 pp sobre
   la población) Y en la población las altas profundas ganan más (brecha ≥ +0,05, IC90 por cierre >0 en OOS).
H4 NIDO-15m: en los 5m que son el último tramo de un 15m (cierre múltiplo de 900 s), W compra el lado s implicado por las
   referencias TWAP60 oficiales (ref15>ref5 ⇒ s=Up) más que la población (≥ +10 pp de su $) Y la población en el lado s
   gana más que en el no-s (brecha ≥ +0,05, IC90 por cierre >0 en OOS).
H5 REBATE/REWARDS: la ventaja de W desaparece al quitar el rebate (20 % de 0,07·p(1−p) por acción del tomador) y no tiene
   tamaño ≥50 acc para rewards. Se refuta si EV de W sin rebate ya es >0 con IC90 por días >0 (dato previo +0,031).

Especificidad: una hipótesis solo «explica» a W si la brecha W − población se reduce ≥50 % al condicionar en ella.
Gate de política (B-réplica): n≥40 cierres con relleno, ≥10 días, EV/€ ponderado IC90 por días >0, sin 2 mejores días >0,
placebo (rasgo permutado dentro de día×tramo de precio) e inversión; BH-FDR sobre K=5. Con 6 días: EXPLORATORY por diseño.
Restricciones de la réplica: alta 68 ms, cancelación 60 ms, taker delay 145 ms, min 5 acc, fee 0,07 tomador, rebate 20 %.
Cualquier cambio tras ver resultados = adenda con hora.
