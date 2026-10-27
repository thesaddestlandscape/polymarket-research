# CAPACIDAD-DISENO: volumen alcanzable de B y diseños que lo multiplican sin multiplicar la selección adversa (24-Oct-2026, ~10:45Z)
Estado: **DESCUBRIMIENTO / EXPLORATORY. Validado 0 €.** Solo lectura (B, live, crons, config intactos; sin órdenes ni commits; solo GET públicos de gamma/clob/data-api). `nice 19 ionice -c3`, `ulimit -v ≤3 GB`, RSS <1 GB, fuera de 06-09Z. Unidades pUSD≈€ sin convertir (restaría 10-15 %). EV siempre ponderado por € (Σpnl/Σcoste), maker sin fee salvo columna "+reb".
Fuentes: `mapa_escala/datos/{niche_dia.csv, niche_fin.csv.gz, niche_maker_dia.csv.gz, s7_tiempo_dia.csv}` (rellenos on-chain MAKER 06..21-Oct, 16 días, desenlace oficial 100 %, T en (60,L], DESC 06-13 / OOS 14-21), `contabilidad_wallet_dedicada/posiciones.csv`, y GET a `data-api.polymarket.com/activity?type=MAKER_REBATE`. Scripts y salidas: `scripts/c1..c7`, `datos/` (hashes en `datos/HASHES_scripts.txt`). Re-uso, no repito: `mapa_escala`, `q_techo`, `r3_escalado`, `seleccion_adversa_plan`, `pares_huecos`, `tendencia_wallets`.

## 0. Respuesta corta
1. **El volumen existe; lo que no existe es EV propio.** Flujo maker 5m (6 monedas, T 60-300 s) = **5,3 M €/día**; el nicho de B (ETH+SOL+XRP 0,10-0,30) son **33,9 k €/día** (0,6 %) y B mueve **55 €/día** (221 € en 4 días, 202 posiciones, EV propio **−0,072**) = **0,16 % del nicho** [`posiciones.csv`, `datos/disenos.csv`]. Para 200 k€/año hace falta un volumen de **49,8 k €/día con EV +0,011 (solo rebate), 27 k a +0,02, 11 k a +0,05, 5,5 k a +0,10**: el 0,9-15 % del flujo según nicho. Con la cuota medida (0,4-0,9 %, R3) y los EV observados, **suma 6,3 k€/año conservador, ≈0,3 k base con la brecha propia de B, y 98 k «base sin brecha» que NO es defendible** (ver §6).
2. **Hallazgo nuevo y verificado: el rebate maker del 20 % ES REAL y se paga a diario (00:45Z), pero con un umbral de ≈1 €/día acumulado** [`datos/c4_rebate_check.txt`, `c5_umbral_rebate.txt`]. 40 makers muestreados: pagado/inferido (0,014·(1−pc)·coste) = **1,01-1,76 en todos los de >50 k€/16 d** (16/16 días con pago). Por maker-día (603 observaciones): con inferido ≥1,0 €/día **pago en el 100 %** (n=437); por debajo, 12-43 % y sin acumulación. **La wallet dedicada tiene 0 filas MAKER_REBATE (GET 24-Oct)**: B acumula 55 €/día × 0,0112 = **0,6 €/día < 1** → por eso "0 $ recibidos". Es la primera explicación medida de la falta de rebate (hipótesis fuerte, no probada causalmente). El rebate vale **+0,011 €/€ en 0,10-0,30**, **+0,007 en 0,50** y **+0,001 en 0,90-0,99** (columna "+reb"); no cambia el signo de B (−0,072 → ≈−0,061) pero es un EV real que el mapa había etiquetado «inferido».
3. **Rewards de liquidez en 5m/15m = 0** (GET 24-Oct 10:3xZ, `clob.polymarket.com/markets/<cid>` de un 5m BTC en vivo: `rewards.rates = null`, `min_size 50`, `max_spread 4.5`; gamma `clobRewards = None`). Hay parámetros pero no hay bolsa de premios.
4. **Sí existe un tipo de maker que gana de forma persistente y a gran volumen: los grandes makers de BTC 5m** (c3/c6). De 702 makers con ≥2.000 € en DESC, los 35 de mayor PnL(+reb) en DESC rinden en OOS **+0,0081 sin rebate / +0,0131 con él sobre 1,74 M€/día** (14,0 k€/día + 8,7 k€/día rebate), pool completo +0,0082 con rebate; placebo +0,009, p 0,014-0,09 según el criterio de selección, IC90 por makers del top-5 % por EV (−0,087,+0,232). Ex-post (descriptivo, elegidos viendo 16 d): `0x21f4c1a1` 167 k€/día, EV +1,57 %, **+42 k€ en 16 d, 8/8 días**, 100 % BTC. En longshots 0,10-0,30 el top gana +0,047/+0,062 frente a −0,034/+0,010 del resto. **Es la existencia-prueba de que el «click» está en BTC 5m con volumen y posición de cola, no en alts a 5 acc**, pero (i) 8 días OOS, (ii) 318 de 702 makers pierden dinero, (iii) los simuladores nuestros (cosechar, pares) NO lo reproducen (24/24 celdas OOS <0; `pares_huecos`) → **fidelidad del simulador, no ausencia de edge, es el cuello**.
5. **Selección adversa medida (no se elimina por diseño):** rellenos de B-tipo aciertan 15,8-18,4 % vs 43,7-52,2 % de las pujas no rellenadas (E1, 3.123 rellenos); AS por relleno −0,137/−0,084/−0,071/−0,043 por tramo 0,10-0,30 (`q_techo` §6); el 55 % del coste rellenado no tiene señal previa. Ningún diseño de volumen la reduce: **cada diseño hereda el EV de población de su celda menos la brecha de cola** (B: −0,053, IC90 cierre −0,32..+0,20, n=202).

## 1. Nocional maker/tomador por marco × moneda × banda (16 días; `datos/disenos.csv`)
Maker = volumen casado a favor del lado comprado por el maker; tomador = contraparte exacta (coste = acc − coste_maker; pnl = −pnl_maker − fee). Capacidad = lo que el mercado casa, NO profundidad en reposo ni cuota alcanzable.
| celda (T 60-300 s, 5m salvo indicación) | maker €/día | EV maker [IC90 días] (IC cierre) | días+ | sin 2 mejores días / sin 5 mejores cierres | DESC / OOS | +rebate | tomador €/día · EV |
|---|---|---|---|---|---|---|---|
| ALT3 0,10-0,30 (nicho B) | 33.904 | +0,051 [−0,029,+0,130] (−0,008,+0,108) | 10/16 | +0,002 / +0,007 | +0,134 / **−0,049** | +0,062 | 140.085 · −0,026 |
| BTC 0,20-0,30 | 167.793 | +0,060 [+0,012,+0,101] (+0,017,+0,104) | 12/16 | +0,036 / +0,043 | +0,083 / +0,037 | +0,071 | 513.102 · −0,037 |
| BTC 0,10-0,20 | 101.185 | +0,048 [−0,032,+0,130] | 9/16 | −0,002 / +0,022 | +0,090 / +0,004 | +0,059 | 587.245 · −0,018 |
| ALL (6) 0,10-0,30 | 305.147 | +0,055 [+0,004,+0,106] (+0,012,+0,099) | 11/16 | +0,026 / +0,041 | +0,091 / +0,017 | +0,066 | 1.249.990 · −0,027 |
| BNB+DOGE 0,10-0,30 | 2.265 | +0,049 [−0,016,+0,113] | 10/16 | +0,010 / +0,012 | +0,024 / +0,085 | +0,060 | 9.558 · −0,025 |
| ALL 0,05-0,10 | 36.017 | +0,029 [−0,061,+0,121] | 9/16 | −0,015 / −0,026 | +0,099 / −0,038 | +0,042 | 471.418 · −0,007 |
| ALL 0,01-0,05 | 22.447 | −0,069 [−0,183,+0,043] | 8/16 | −0,130 / −0,209 | −0,047 / −0,087 | −0,055 | 1.073.200 · +0,000 |
| ALL 0,30-0,50 | 766.689 | +0,008 [−0,010,+0,025] | 8/16 | −0,004 / +0,004 | +0,015 / +0,001 | +0,016 | 1.162.097 · −0,033 |
| ALL 0,50-0,70 | 1.194.322 | −0,013 [−0,027,0,000] | 7/16 | −0,020 / −0,016 | −0,017 / −0,010 | −0,008 | 817.061 · −0,021 |
| ALL 0,70-0,90 | 1.411.033 | −0,006 [−0,017,+0,004] | 6/16 | −0,013 / −0,008 | −0,015 / +0,002 | −0,004 | 368.956 · −0,030 |
| ALL 0,90-0,99 (88 % BTC) | 870.596 | +0,007 [+0,001,+0,013] (+0,001,+0,012) | 10/16 | +0,004 / +0,007 | +0,002 / +0,012 | +0,008 | 48.166 · −0,190 |
| 15m ALL 0,10-0,30 | 119.139 | +0,041 [−0,052,+0,127] | 9/16 | −0,008 / −0,063 | +0,138 / −0,067 | +0,052 | 488.988 · −0,023 |
| 15m ALL 0,30-0,50 | 303.208 | +0,055 [+0,012,+0,098] (−0,003,+0,110) | 13/16 | +0,030 / +0,010 | +0,115 / −0,014 | +0,063 | 457.401 · −0,064 |
| 15m ALT3 0,70-0,99 | 126.873 | +0,019 [+0,014,+0,025] (+0,008,+0,030) | 14/16 | +0,017 / +0,017 | +0,025 / +0,014 | +0,021 | 22.395 · −0,166 |
| 15m ETH 0,70-0,99 | 78.922 | +0,026 [+0,019,+0,033] (+0,011,+0,040) | 14/16 | +0,022 / +0,023 | +0,032 / +0,020 | +0,028 | 13.710 · −0,205 |
| 60m ALL 0,70-0,90 (4 días) | 91.665 | +0,089 [+0,040,+0,136] | 4/4 | +0,047 / +0,069 | n/a / +0,089 | +0,092 | 23.437 · −0,402 |
| 60m ALL 0,10-0,30 (4 días) | 20.786 | **−0,366** [−0,503,−0,246] | 0/4 | −0,503 / −0,580 | n/a | −0,355 | 86.131 · +0,075 |
| 4h 0,90-0,99 / 4h 0,30-0,50 / 24h 0,30-0,50 (4 d) | 5.531 / 6.490 / 14.884 | +0,047 / +0,055 / +0,287 | 4/4, 3/4, 3/4 | +0,040 / −0,004 / −0,143 | n/a | | no suman |
**Tomador:** el EV de población del tomador es ≤0 en todas las celdas con volumen (−0,007..−0,064), salvo 15m 0,50-0,70 (+0,014) y 15m BTC 0,70-0,99 (+0,035): pequeños, sin gate, y como tomador desde este VPS ya está cerrado (taker delay 145 ms; `CLAUDE.md`). **El nocional tomador (1,2 M€/día en 0,10-0,30) es 4× el del maker porque compra el lado caro, pero su EV sale de lo que pierde el maker + la comisión: no es una vía.**
**Banda 0,00-0,10 (N4, backfill descriptivo, NO cuenta):** 5m ALL 0,01-0,10: 58.464 €/día, EV −0,008 [−0,097,+0,080], sin 2 mejores días −0,057, OOS −0,057 → sin edge; la celda ETH/SOL 0,05-0,10 de referencia (ALT3: +0,098, IC90 días (−0,114,+0,349), sin 2d −0,081, OOS −0,052) no se sostiene. El forward N4 sigue (gate 24-Oct..02-Nov).
**Ventana de T (c2, EXPLORATORIO, 1 de 146 celdas del mapa):** 5m ALL 0,10-0,30 con T (60,150]: 119.944 €/día, **+0,083 [+0,023,+0,143]**, 10/16 días, sin 2d +0,042, DESC +0,096 / OOS +0,069 (+0,094 con rebate), sin ALT3 +0,089. La ventana donde opera B, T (150,300] en ALT3: +0,061 [−0,054,+0,175], OOS **−0,088**. Hay ~7 falsos positivos esperados entre 15 celdas con IC>0 de 146 → hipótesis de trabajo, no hallazgo.

## 2. Fill-ability y cuota alcanzable «sin mover precio» (medida, no supuesta)
- **B hoy:** 61-72 % de relleno por puja (E1/B), 55 €/día, ~50 posiciones/día; = 0,16 % del flujo del nicho; ~1,2 % de las «unidades primeras-5-acc» (4.715 €/día, `mapa_escala` §0.3).
- **R3 (simulador E1, 17-22 Oct):** capacidad **130 rellenos/día = 136 €/día a 5 acc** (0,40 % del nicho de 33,9 k); K=20 → ×2,3 = 313 €/día (**0,92 %**), EV −0,050 (K=20) y −0,099 (K=50): el EV se rompe a K=50 (`r3_escalado` §0.4). Es la única cuota anclada a medida; **las cuotas de 3-5 % del mapa no están medidas** (TP2 pendiente).
- Para cualquier otra celda (BTC 0,20-0,30, favoritos, 15m) la fill-ability y el AS **no están medidos con órdenes** (DATA_BLOCKED: L2/posición en cola). La cuota 0,4-0,9 % se extrapola como supuesto.
- Capital: no limita (exposición p95 al 5 % de cuota 14-72 € en 5m BTC 0,20-0,30; mapa §4). Limita varianza (DD): R3 a 5 acc necesita 56-73 $ para 300 rellenos con P(DD)≤10 %.

## 3. Rebate y rewards (ángulo 4)
| fuente | estado | evidencia |
|---|---|---|
| Rebate maker 20 % de la comisión del tomador (cripto 0,07·p(1−p)) | **REAL, pagado a diario 00:45Z, umbral ≈1 €/día por wallet** | `c4`: pagado/inferido 1,01-1,76 (16 makers >50 k€/16 d); `c5`: 100 % de pago con inferido ≥1,0 (n=437), 12-43 % por debajo; dedicada: 0 filas `MAKER_REBATE` |
| Magnitud | +0,011 €/€ en 0,10-0,30, +0,008 en 0,30-0,50, +0,001 en 0,90-0,99; **pool 5m de todos los makers ≈ 22 k€/día (≈8 M€/año)**; los 702 makers: 507 k€ de PnL con rebate en 16 d (185 k€ sin él + 322 k€ de rebate inferido = 63 %) | `datos/disenos.csv` (`reb_dia`), `c3` |
| Rewards de liquidez 5m/15m | **0** (`rates: null`) | GET clob/gamma, 24-Oct |
| Consecuencia | para B: concentrar el volumen en días con ≥100 €/día (≥90 € en 0,2; ≥140 en 0,5) desbloquea +0,011 €/€ sin cambiar nada más (~0,6 €/día hoy, 220 €/año: pequeño) | derivado |
**Cautela:** pagado/inferido >1 (1,3-1,6 en medianos) incluye volumen de otros marcos (60m, 4h) que el inferido de 5m+15m no cuenta; no es evidencia de que el tipo real supere el 20 %. El rebate es el **único componente positivo independiente de la selección adversa**: en la población de makers 5m es ~63 % del beneficio total de los 702 makers.

## 4. Diseños para multiplicar volumen (ángulo 2-3, 9, 10)
Cada fila: EV observado (celdas del §1), tope de capacidad, y por qué sí/no escala sin escalar la AS. «EXPLORATORIO» salvo que se indique; **ninguno VALIDADO**.
| # | diseño | EV/€ medido (n, IC) | tope capacidad (€/día maker del flujo) | ¿multiplica AS? | veredicto |
|---|---|---|---|---|---|
| D1 | **Más monedas** (BTC/BNB/DOGE además de ETH/SOL/XRP) 0,10-0,30 | ALL +0,055 [+0,004,+0,106], OOS +0,017; BTC 0,20-0,30 +0,060 [+0,012,+0,101] OOS +0,037; BTC 17-19-Oct −0,03/−0,18/−0,15; BH q=0,44 | 305 k€/día (BTC 169 k) | misma AS por relleno; B-BTC ya REJECTED con R2 | EXPLORATORIO; mejor pieza de volumen del mismo mecanismo |
| D2 | **Más buckets** 0,05-0,10 / 0,01-0,05 (N4) | −0,008 [−0,097,+0,080], OOS −0,057 | 58 k | no hay EV | DESCARTAR (forward N4 corre, coste 0) |
| D2b | 0,30-0,50 (5m) | +0,008 [−0,010,+0,025] +reb +0,016 | 767 k | AS menor (banda central) pero EV ≈ rebate | solo vale si la brecha de cola es ≈0: no medida |
| D3 | **Más marcos** 15m 0,30-0,50 / 0,10-0,30 | +0,055 / +0,041, OOS −0,014 / −0,067 | 303 k / 119 k | 15m: B real sin dato | REJECTED como fuente (OOS<0); 15m ETH/ALT3 favoritos ver D4 |
| D4 | **Favoritos** 5m 0,90-0,99 y 15m ETH/ALT3 0,70-0,99 (maker del lado favorito = vender el boleto del longshot) | 5m +0,007 [+0,001,+0,013]; 15m ETH +0,026 [+0,019,+0,033], 14/16 días (único que pasa BH q=0,024) | 871 k / 79-127 k | sin AS por relleno al estilo longshot, pero EV ≤ brecha de B | EXPLORATORIO; ≈6-10 k€/año a 0,9 %; 5m favoritos 0,4 pp de EV: no distinguible de la brecha |
| D5 | **Tamaño escalonado** (K 5→20) | R3 sim: −0,033 (K5), −0,050 (K20), −0,099 (K50); € diarios ×1,6/×2,3/×3,3 | K≤20 | EV por € cae al subir K | K≤20 máximo; K=50 REJECTED |
| D6 | **Ventana T (60,150]** en vez de (150,300] | ALL +0,083 [+0,023,+0,143] OOS +0,069; ALT3 +0,036 [−0,010,+0,078]; ALT3 (150,300] OOS −0,088 | 120 k€/día | cambia dónde opera B | EXPLORATORIO barato (cambio de reloj, no de mecanismo); forward ya expuesto en N1 |
| D7 | **Pares** (ambos lados, completar, salir, cosechar al abrir) | 11 variantes, todas negativas en OOS (−0,03..−0,34) | — | multiplica pata suelta | REJECTED (`pares_huecos`); el único caso ganador, `0x21f4`, no es replicable con nuestro simulador |
| D8 | **Wallets ganadoras de alts** (0xf074/0x0ab0 ETH, 100 % maker, asks, lotes 5 acc, inventario ≤15-30 acc) | +0,012/+0,015 por € sin rebate (elegidas viendo TEST) | ~10-30 k€/día cada una | no direccionales | NO copiable por conducta: no leen tendencia; EXPLORATORIO |
| D9 | **Gran maker BTC 5m** (c3/c6) | top-35 por PnL DESC: OOS +0,0081 / +0,0131 con rebate, 1,74 M€/día; top-5 % por EV: +0,053 IC90 makers (−0,087,+0,232) | 40-170 k€/día por wallet | AS de BTC: la mayoría pierde (318/702 con PnL<0) | **ÚNICO diseño con pasta demostrada por terceros**, pero 8 días OOS, selección por resultado, y requiere replicar cola/latencia: es el objetivo del trabajo de ms (E1), no de volumen |
| D10 | **Rebate puro** (maker neutro a precio medio, 0,30-0,70) | EV pop ex-rebate −0,013..+0,008, +rebate −0,008..+0,016 | 2 M€/día | neutro | no hay margen: sin AS el neto es ≈0; con la brecha de B es negativo |
| D11 | **60 min** 0,70-0,90 | +0,089 [+0,040,+0,136], 4/4 días, 4 días | 92 k | desconocida | candidato de EXTRACCIÓN (Test N-60m); no cuenta |
| D12 | **Otros mercados Polymarket** | 33,2 M€/día de volumen maker el 20-Oct, 2,05 M en 0,05-0,30 (`mapa_escala` §0.7) | grande | sports = AS por noticias | EV NO medido (otro repo/otro mapa de desenlaces); no cuenta |
| D13 | Rewards LP | 0 (`rates: null`) | — | — | CERRADO en 5m/15m |

## 5. Tabla €/año por diseño (celdas DISJUNTAS, sin doble conteo; `scripts/c7_tabla.py`, `datos/c7_tabla.txt`)
Regla: cons = 0,4 % del flujo (R3 5 acc medida) × max(0, min(IC90 días inferior, EV sin 2 mejores días, EV OOS)); base = 0,9 % (R3 K20 medida) × (EV OOS + rebate); opt = 3 % (NO medida) × (EV 16 d + rebate); «−brecha» resta el −0,053 de B (estrés).
| diseño (disjunto) | flujo €/día | EV16 / IC90 lo / sin2d / OOS | cons | base | opt | base−brecha | opt−brecha | clase |
|---|---|---|---|---|---|---|---|---|
| B: 5m ALT3 0,10-0,30 | 33.904 | +0,051 / −0,029 / +0,002 / −0,049 | 0 | 0 | 23.010 | 0 | 3.334 | EXPLORATORIO (REAL: EV −0,072) |
| 5m BTC 0,10-0,20 | 101.185 | +0,048 / −0,032 / −0,002 / +0,004 | 0 | 5.155 | 65.891 | 0 | 7.169 | EXPLORATORIO |
| 5m BTC 0,20-0,30 | 167.793 | +0,060 / +0,012 / +0,036 / +0,037 | 2.930 | 26.204 | 129.605 | 0 | 32.227 | EXPLORATORIO |
| 5m BNB+DOGE 0,10-0,30 | 2.265 | +0,049 / −0,016 / +0,010 / +0,085 | 0 | 711 | 1.491 | 317 | 176 | EXPLORATORIO |
| 5m ALL 0,05-0,10 | 36.017 | +0,029 / −0,061 / −0,015 / −0,038 | 0 | 0 | 16.517 | 0 | 0 | REJECTED |
| 5m ALL 0,30-0,50 | 766.689 | +0,008 / −0,010 / −0,004 / +0,001 | 0 | 23.171 | 135.331 | 0 | 0 | EXPLORATORIO (EV≈rebate) |
| 5m ALL 0,90-0,99 | 870.596 | +0,007 / +0,001 / +0,004 / +0,012 | 839 | 36.292 | 72.546 | 0 | 0 | EXPLORATORIO |
| 15m ALT3 0,70-0,99 | 126.873 | +0,019 / +0,014 / +0,017 / +0,014 | 2.525 | 6.618 | 29.675 | 0 | 0 | EXPLORATORIO (BH ok) |
| 15m ALL 0,30-0,50 | 303.208 | +0,055 / +0,012 / +0,030 / −0,014 | 0 | 0 | 210.197 | 0 | 34.231 | EXPLORATORIO |
| 15m BTC 0,10-0,30 | 98.950 | +0,063 / −0,045 / +0,006 / −0,065 | 0 | 0 | 80.667 | 0 | 23.241 | EXPLORATORIO |
| 60m ALL 0,70-0,90 (4 d) | 91.665 | +0,089 / +0,040 / +0,047 / +0,089 | 5.344 | 27.598 | 91.992 | 11.638 | 38.794 | DESCRIPTIVO (<10 d) |
| **SUMA con 60m (4 d)** | | | **11.637** | **125.750** | **856.923** | **11.955** | **139.171** | |
| **SUMA sin 60m (lo que tiene ≥16 días)** | | | **6.293** | **98.152** | **764.931** | **317** | **100.377** | |
Lectura honesta: (a) **VALIDADO = 0** (ninguna celda tiene dinero propio con EV>0; B real −0,072). (b) El «base sin brecha» de 98 k asume que nuestra cola rinde como la población media, que B contradice (−0,053, n=202, IC90 cierre amplísimo −0,32..+0,20); con brecha, base ≈0,3 k. (c) El «opt» de 765 k usa cuotas de 3 % no medidas y se solapa en la misma apuesta por cierre (rho ~0,35 entre monedas; 5m y 15m del mismo cierre = una apuesta): **no se debe citar como escenario**. (d) El 61 % del «base» es 5m 0,30-0,50 + 0,90-0,99, donde el EV (+0,001..+0,012 en OOS) es del orden del rebate: ahí el beneficio entero depende de que el rebate (real) cuele y de que la brecha de cola sea ≈0.
Hueco a 200 k€ (conservador): **193,7 k€**; base con brecha: **199,7 k€**; base sin brecha (no defendible): 101,8 k€.

## 6. Qué falta (edge, capacidad o capital)
- **Edge**: no hay celda con EV propio >0 medido con dinero. Lo más cercano son BTC 0,20-0,30 y los favoritos 15m ETH/ALT3, pero la brecha de cola de B (−0,053) los anula. Sin una cancelación/posición en cola que anule esa brecha (E1/S1/R3), cualquier suma de volumen es teórica.
- **Capacidad**: el mercado casa 5,3 M€/día en 5m; con EV +0,011 (solo rebate) hacen falta 49,8 k€/día = 0,9 % del 5m (≈2,2× lo medido en R3 K20 sobre 33,9 k, pero en celdas de 767 k-871 k €/día cuya cuota alcanzable NO está medida).
- **Capital**: no limita (decenas a cientos de €); limita el DD y la regla de rampa de Javi.
- **Hueco**: 200 k€ validado; la suma defendible hoy es 6,3 k€/año conservador (3,1 % del objetivo).

## 7. Las 3 pruebas de mayor valor de la información (VOI)
1. **Cuota y brecha de cola EN BTC 5m 0,20-0,30 y en 15m ETH 0,70-0,99, por micro-orden real o simulador calibrado (TP2 + T-REAL)**: mide si la brecha de B (−0,053) existe fuera de ETH/SOL/XRP. Coste: 0 € (TP2 offline sobre `libro5_ms`/`maker_ms`) + ≤5 € (150 rellenos a 5 acc, necesita OK de Javi + /code-review). Gate: brecha propio−población ≥−0,02, ≥150 rellenos, ≥10 días. Quién: E1 (cola) + risk-economics. Resuelve si D1/D4 valen 6-30 k€ o 0.
2. **Fidelidad del simulador contra los grandes makers de BTC (0x21f4, 0xe290, 0x86b1…)**: reproducir su PnL día a día (14,2 k DESC / 27,8 k OOS para 0x21f4) con el simulador de cola; si no se reproduce, el simulador subestima el rebate o la cola y todo «REJECTED por sim» (cosechar, pares) queda en duda. Coste 0, 1 agente, datos ya extraídos (`m5_onchain`, `maker_ms`). Gate: error ≤25 % en PnL y signo en ≥6/8 días. Si lo hace, D9 pasa a candidato de diseño (40-100 k€/día de volumen ≈ 100-200 k€/año a +0,013).
3. **Umbral del rebate en la dedicada**: subir (en una sola tanda) el volumen de un día a ≥100 € de coste maker en 0,10-0,30 y comprobar si aparece `MAKER_REBATE` a las 00:45Z. Coste ≈ 100 € de rotación con EV propio −0,07 → pérdida esperada ≈7 €: **no hace falta gastarlo**; alternativa 0 €: pedir a Polymarket/leer sus docs el umbral mínimo (se puede verificar sin dinero con las wallets de §1: ya hay 603 maker-días). Valor: fija si el +0,011 €/€ está al alcance de cualquier escala; coste 0.
Descartable ya (con n y fuente arriba): bandas 5m 0,01-0,10; 15m 0,10-0,30 y 0,50-0,70; pares/cosechar/cobertura; 60m 0,10-0,30 (−0,366); tomador como fuente de volumen; rewards LP en 5m/15m; «más cuota con K=50».

## 8. Limitaciones declaradas
16 días, un solo régimen (la población cambia de signo a mitad; 17-19 Oct malo). La cuota 0,4-0,9 % es de un solo nicho y K≤20. El EV de población ≠ EV de nuestra cola. Los 35 «grandes» están elegidos en DESC y medidos en 8 días de OOS (placebo p 0,014-0,09; IC90 por makers del top-5 % por EV cruza 0). Rebate: pagos observados vs inferido válidos para makers >1 €/día; pagado/inferido incluye otros marcos. La wallet = dirección (un operador puede usar varias). 60m/4h/24h: 4 días, sin gate. `c5` muestrea 70 makers aleatorios de 1.500-60.000 € (semilla 11), no toda la población; el umbral ≈1 € es una frontera empírica, no una regla documentada.
