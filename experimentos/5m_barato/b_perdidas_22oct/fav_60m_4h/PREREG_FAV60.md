# PREREG FAV60-VPV v1 — favoritos 60m/4h maker, un solo lado (25-Oct-2026 ~11:10Z, ANTES de calcular ningún desenlace)
Autor: cheap5m-alpha-researcher (encargo del chief). Solo shadow/análisis. Nada a real.

## Pregunta
¿El +0,076 €/€ de la POBLACIÓN de rellenos maker 60m BTC/ETH/SOL [0,70-0,90) (F2 §1/§6, 18..23-Oct, on-chain) sobrevive
(a) reproducido desde datos crudos con desenlace oficial y (b) para una PUJA VIRTUAL PROPIA en cola (selección adversa propia)?

## Paso 1 — reproducción de población (no es el gate)
Rellenos on-chain MAKER (taker != 0xe111…), compra del lado lc (side=1 se convierte al contrario), unidad = (mercado, lado, bucket 0,05),
T=fin−ts ∈ (60, 3600] (60m) / (60, 14400] (4h). EV/€ = Σpnl/Σcoste. Mapa token→mercado y desenlace: gamma (closed=true, outcomePrices),
independiente del mapa de F2. Días 18..24-Oct (24-Oct desde onchain_fills crudo). Objetivo: +0,076 ±0,01 en 18..23. 4h: [0,65-0,99).

## Paso 2 — pujas virtuales (vpv) = TEST PRINCIPAL
Fuente: registro ms (maker_ms_*, filas q = top of book del token con hora de RECEPCIÓN c5; filas t = prints), 12..24-Oct (cierres con fin <= 25-Oct 00:00Z).
Universo: mercados 60m BTC, ETH, SOL (XRP/DOGE/BNB solo si aparecen; no entran al gate). Libro cruzado (bid>=ask) descartado.
Regla: para cada (mercado, lado s) t0 = primera fila q (orden por recepción) con T=fin−t0 ∈ (120, 3600] y bid_s ∈ [0,70, 0,90).
Puja virtual a P = bid_s(t0) (join, detrás de la cola), activa desde t0+0,1 s, viva hasta fin−60 s, sin cancelar. 5 acciones.
Relleno PES (gate): primer instante con ask_s <= P−0,01, o print en s a precio <= P−0,01, o bid del contrario >= 1−P+0,01 (atraviesa).
Relleno OPT (informativo): ask_s <= P, o print en s <= P, o bid contrario >= 1−P.
PnL por acción relleno = 1{gana s} − P. Comisión maker 0 (takerOnly). Rebate 20 % = 0,014·P·(1−P)/acción solo como variante
(no se cobra por debajo del suelo de pago; gate SIN rebate). No rellenas: contrafactual 1{gana s} − P para medir la AS.
Desenlace: gamma outcomePrices (oficial; cobertura reportada; missing != 0). Contraste BTC con vela 1H Binance (cierre >= apertura → Up) y reportar coincidencia.

## Gate (UNA celda, K=1): BTC+ETH+SOL, [0,70-0,90), relleno PES, sin rebate
n rellenas >= 40 (mercado-lado), >= 10 días distintos (día = fecha UTC de fin), EV/€ ponderado > 0 con IC90 bootstrap por DÍAS lo > 0,
EV sin los 2 mejores días > 0, placebo: mismo set de rellenas con el desenlace del mismo lado del mercado de la MISMA moneda 24 h antes
→ EV_real − EV_placebo con IC90 por días lo > 0; inversión: misma regla en [0,10-0,30) debe NO dar EV>0 con IC lo>0 (si lo da, el método está roto).
Desglose obligatorio (exploratorio, sin gate): moneda × bucket 0,05 × PES/OPT; AS = acierto(rellenas) − acierto(no rellenas) con IC90 por días;
partición días vistos por F2 (18..23) vs no vistos (12..17, 24).
Si n o días no llegan: veredicto EXPLORATORY con fecha estimada (n/día medido).
## Capacidad (honesta)
€/año = EV_PES × coste rellenado/día (5 acc) × 365; techo = 1 % del flujo maker on-chain de la celda × EV. Sin extrapolar si el gate no pasa.
