# Wallet «pspspsps5» (post promocional) — auditoría read-only, 24-Oct-2026
Estado: **EXPLORATORY**. Solo lectura (data-api/gamma públicos, m5_onchain archivo). Sin enlaces de referido, sin tocar B/live/crons/F2. nice 19 ionice -c3, ulimit 3 GB.

## 1. Identidad y universos (observado)
- Handle `pspspsps5` -> `0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5` (gamma `public-search`, seudónimo Fearless-Omega). data-api `traded` = 184.241 mercados (post: 183.843: coincide).
- **Ya estaba en nuestros universos**: `tomadores_universo_hist` figura como «candidata» TODOS los días 30-Sep..24-Oct (25 ficheros); además `ballenas_diario.csv` (34 filas jul-sep), `wallets_sistematicas_rol_27_29sep.json`, `wallet_first_buy/*` (33). No es 0x21f4/0xe290/0x86b1. Es **100 % MAKER** (ver §3): el EV de «copiarla como tomadora» (nuestro universo de tomadores) es irrelevante.
- Solo 5m: BTC/ETH/SOL (+ 20 DOGE, 18 BNB, 14 HYPE en todo el histórico). Solo COMPRAS (0 ventas), mantiene a resolución.

## 2. El post frente a datos (PnL con desenlace oficial)
Fuente primaria: ledger on-chain 05-23 Oct (`m5_onchain`, 52.328 fills, 9.311 mercados, desenlace oficial 100 %) + `/activity` TRADE 22-Sep..07-Oct con desenlace gamma `closed=true` (8.545/8.545). Validado: data-api 22-Oct = 2.568 trades y 21.876 $ = on-chain exacto; ledger vs API posición a posición coincide al céntimo (5.902 posiciones).
| | Post | Medido |
|---|---|---|
| 30 días 24-Sep..23-Oct | +34.407 $, verde 24/30 | **+29.646 $, verde 24/30**; leaderboard oficial «mes» +28.923 $ (vol 2,07 M) |
| histórico | +299.217 $ | leaderboard «all» **+270.478 $** (vol 21,55 M) |
| EV por € (30 d, Σpnl/Σcoste 791.820 $) | — | **+0,037**; EV diario medio 0,034, sd 0,045 |
| sin 2 mejores días / sin 5 mejores | — | +21.700 $ / +14.234 $ (mejor día +5.344, peor −1.429) |
- Cifras del post ~14-16 % infladas frente al leaderboard oficial pero la forma (24/30 verdes) se reproduce: **no es fabricada**. t de PnL diario = 3,99 (30 d); con 5 días ya t≥1,645.
- **Trampa de supervivencia aplicable a quien mire su perfil**: `/closed-positions` solo contiene ganadoras redimidas (30/30 verdes, +120.139 $ en 30 d, EV 0,166): omite las perdedoras no redimidas (en 06-22 Oct: 4.595 unidades, 0 % acierto, −43.945 $). El PnL de «posiciones cerradas» es falso; usar leaderboard o ledger.
- Ventana ejemplo (19,62 $ -> 309,59 $): 2 de 443 ventanas con coste 15-25 $ ganan >200 $. Cola de la distribución; nada tipo ventana-elegida-a-posteriori cambia el total, pero el ejemplo no es típico (ventana mediana de mercado: -0,56 $).

## 3. Reconstrucción (05-23 Oct, 19 días completos; unidad mercado+lado; fee real on-chain)
- Total: coste 421.770 $, **PnL +13.114 $, EV +0,031**, IC90 por días (+0,016, +0,046); verde 15/19 días completos. Fee pagado 0 $: **100 % de fills maker** (taker de la fila ≠ exchange). Rebate maker estimado (20 % de la comisión que pagaría el tomador, NO observado on-chain): ~+1.100 $ (+0,26 % del coste); todo lo de abajo es SIN rebate.
- Mercado: 466/día, ticket mediano 8,6 $, medio 45 $; solo 17,2 % de mercados con ambos lados (no cosecha pares). PnL de mercado: media +1,41, mediana −0,56; 39 % mercados >0; **top 1 % de mercados = 173 % del PnL; sin los 20 mejores, 5.230 $**. Correlación de PnL por ventana entre monedas: 0,02-0,06 (ventanas con >=2 longshots acertados 0,4 % vs 0,1 % si independientes).
- Entra tarde, no al abrir: 76 % del coste con T (s hasta cierre) 60-180 s. Solo 5.384 de 52.328 fills a T>240 s.
- PnL por precio de relleno (fills; coste / PnL / EV):
| bucket | fills | coste $ | PnL $ | EV | IC90 días |
|---|---|---|---|---|---|
| <0,10 | 16.311 | 15.085 | +5.052 | +0,335 | (0,18, 0,49) |
| 0,10-0,40 | 15.037 | 33.079 | +5.450 | +0,165 | — |
| 0,40-0,60 | 6.103 | 25.094 | −477 | −0,019 | — |
| 0,60-0,90 | 8.811 | ~81.000 | −229 | ~−0,003 | — |
| >=0,90 | 6.066 | 267.555 | +3.320 | +0,012 | (0,004, 0,020) |
  Tickets <0,10 = **31 % de los fills pero 3,6 % del coste**; 39 % del PnL. Capital: 63 % en el carry >=0,90 (maker, +1,2 % por ciclo de ~2 min, 96,1 % acierto vs precio 94,9 %).
- **Lotería no es la historia entera**: tres fuentes de PnL: tickets <0,10 (+5,1 k), banda 0,10-0,40 (+5,5 k) y carry >=0,90 (+3,3 k).

## 4. Mecanismo del ticket barato (hecho / inferencia / incógnita)
Hechos:
- Fills <0,10: acierto 5,39 % (por cuenta) vs precio 4,54 %; EV +0,295, IC90 días (+0,15,+0,44), n=12.850 fills (14 días, 05-23 Oct comparables). Descubrimiento 05-12 Oct +0,41 (IC +0,25,+0,54); **holdout 17-23 Oct +0,18 (IC −0,04,+0,41)**. Por monedas BTC +0,36, SOL +0,62, ETH +0,07 (cruza 0).
- Por unidad entera (mercado+lado), precio medio <0,10 (n=4.848): **EV +0,0008, IC90 (−0,17,+0,18)**, acierto 4,06 % vs precio 3,90 % -> como compra aislada es justo. Descubrimiento −0,03 / holdout +0,03.
- La diferencia la crea la ESCALERA (K=2 clases, post hoc): fills <0,10 en unidades que también tienen fills >=0,10: n=5.818 fills, 1.520 unidades, EV +0,78 (IC +0,52,+1,02), acierto 8,6 % vs 5,7 %, desc +1,05 / hold +0,48 (ambos IC>0). Fills <0,10 «puros» (unidad entera <0,10): EV +0,04 (desc −0,20 / hold +0,23). Pero la unidad escalera ENTERA (todos sus fills, 22.891 $) tiene EV −0,010: el beneficio del tramo bajo se compensa con los fills altos de la misma posición (promedia a la baja).
- **Población frente a W (mismos días, mismos fills pasivos de compra <0,10, 5m, 6 monedas, on-chain)**: población sin W n=1,60 M fills, 862.698 $: **EV −0,038 (IC90 −0,13,+0,05)**, acierto 3,68 % vs precio 3,98 %; descubrimiento +0,063, **holdout −0,133 (IC −0,28,−0,01)**. W: +0,295. **Brecha W−población +0,33 (desc +0,35, hold +0,31)**. W es 1,4 % del $ pasivo <0,10.
- Selección adversa: la población maker barata sufre (acierto/precio = 0,92); W no (1,19). B real: 175 posiciones, EV ponderado −0,012, acierto 21,1 % vs 21,5 % implícito (ratio 0,98), IC cruza 0, correlación intra-cierre 0,77. Las posiciones de W no están correlacionadas entre monedas (0,02-0,06) y reparte 466 mercados/día; B apuesta las 3 monedas a la vez en el mismo cierre.
Inferencias (no probadas): W no «evita» la selección adversa por saber el desenlace; la evita por QUÉ rellenos acepta (escalera descendente, tamaño ~1 $ en el fondo y 23 $ en >=0,60, entrada a T 60-180 s). Es compatible con un maker que compra caídas en un mercado que sobre-reacciona en el último tercio; no está identificado el predictor ex ante.
Incógnitas: qué señal usa (Binance/otro mercado), si cancela/recotiza (no hay pedidos, solo fills), tasa de relleno, si el 0,10-0,40 es el mismo mecanismo. No medido: asimetría Up vs Down de los tickets (post: «Down 3-10 c»), comparador población para la banda 0,10-0,40 (solo extraje <0,10).

## 5. Tamaño de muestra y varianza
- Unidades <0,10: sd del retorno por unidad ~6,4 €/€. Para detectar +0,05 con z=1,645 harían falta ~44.000 unidades; con +0,29 (EV de fills de W) ~1.300 unidades independientes. W genera ~282 unidades/día y 836 fills/día baratos; un réplica de 1 orden por mercado-lado en BTC como máximo ~576/día y con tasa de relleno <1.
- 13/20 días verdes solo con tickets (65 %); sin los 2 mejores días los tickets <0,10 siguen +3.442 $; el neto «unidad entera» pura sin 2 mejores días −1.022 $. Es varianza alta con edge condicional pequeño, no un cajero.
- Todo el PnL, 30 d: 24/30 verdes, t=3,99 -> estadísticamente positivo, pero concentrado: sin 5 mejores días 14,2 k (48 %).

## 6. Cruce con nuestras líneas
- **5m barato v4/V7 (bid15 - ask5)**: línea distinta (tomadora sobre implicación 15m); no solapa.
- **B (maker H47, ~0,21)**: W en la misma banda 0,10-0,40 gana +0,165 por € (n=15.037 fills, 33 k$), B -0,012 (n=175). W no se puede comparar 1:1 (B: bids al top, 5 acc, ETH/SOL/XRP; W: ladder, BTC dominante).
- **TP1 banda 0,00-0,10**: la población maker pasiva en esa banda es -0,038 (holdout -0,133): TP1 no debe esperar edge genérico; el único mecanismo con diferencial es el de W y no está identificado ex ante.
- **Rebate**: +0,26 % del coste (irrelevante para W; en tickets <0,10 el rebate/EV ~4 %).
- **Selección de wallets (placebo)**: W cumple lo pedido por `seleccion_tomadores_persistentes` solo como tomadora; como maker aparece persistente. El criterio fijado debe evaluarse en días distintos de la selección: W ya estaba como candidata desde 30-Sep, su holdout de tickets (17-23 Oct) sigue positivo (+0,18, IC90 cruza 0); el total diario 17-23 Oct es verde en 6 de 7 días del ledger.

## 7. Propuesta de shadow/forward (PREREG, no tocar B/live/crons) — K=2 hipótesis, alfa 0,05/2
Solo se lanza si Javi lo aprueba; escribe en `datalogs/` con gz; nada de órdenes.
- **S1 ESCALERA-CAÍDA-5M (BTC; diseño y decisión en BTC)**: en cada mercado 5m BTC, desde T=180 s (decisión), simular bids pasivos en [0,30; 0,20; 0,10; 0,05; 0,03] SOLO en el lado cuyo precio medio cae por debajo de 0,40 tras haber estado >=0,40 (misma restricción que W: unidad = mercado+lado, 1 ticket por nivel, 5 acc, relleno solo si una operación ATRAVIESA el nivel, cola a partir del registro ms; sin rebate; fee 0). Métrica primaria: EV ponderado por € de los fills <0,10 DENTRO de unidades escalera; control: bids a un nivel único <0,10 sin historia (población); criterio de éxito: EV >= +0,10, IC90 por días >0, >=10 días, n>=800 unidades <0,10, >=7/10 días verdes, brecha vs control >= +0,10; refutado si EV <= 0 o brecha IC90 incluye 0 en el 2º tramo. Descubrimiento 05-23 Oct YA mirado (contaminado): forward desde 25-Oct, mínimo 10 días antes de leer.
- **S2 CARRY-90 (control de capital, solo medición)**: bids pasivos a 0,90-0,99 en el lado ganador implícito; referencia W +0,012 por € (IC +0,004,+0,020, n=6.066 fills, 2.548 unidades); gate: n>=1.500 unidades, >=10 días, EV>=+0,01, IC90>0, y capital/ciclo declarado (63 % del capital de W; no se aplica con 5 € de dedicada).
- No hacer: copiar sus fills; usarla como señal de dirección (no hay evidencia de información, es maker).
Veredicto actual: **mecanismo NO replicado todavía**; el único diferencial observado (tickets en escalera, +0,33/€ frente a la población) no es una regla ex ante y se ha encontrado post hoc (K>=15 cortes mirados); holdout de tickets agregados +0,18 con IC que cruza 0.

## 8. Refutaría la hipótesis «hay un mecanismo replicable»
- S1 forward con EV <= 0 o brecha vs control con IC90 por días incluyendo 0 tras 10 días y n>=800 unidades.
- Que el EV de W en tickets (+0,295) caiga bajo +0,05 en 14 días nuevos (señal de régimen).
- Que la brecha W - población en banda 0,10-0,40 (no extraída aquí) sea ~0 (entonces el diferencial es solo de los tickets).

## 9. Limitaciones
- Ledger on-chain solo desde 05-Oct; 24-Sep..04-Oct viene de `/activity` TRADE (sin ventas, 100 % compras, igual que on-chain) con desenlace gamma 100 %. Día 05-Oct difiere API vs ledger (-277 vs +124 $) por corte de día; usado el ledger.
- Población: 16 de 19 días extraídos (12-Oct, 22-Oct más pendientes en cola; 13-16 Oct no extraídos), tokens no mapeados excluidos. «Fills pasivos de compra <0,10» incluyen mercados 5m de todas las monedas.
- Rebate estimado, no observado. Sin libro/colas: nada de tasa de relleno ni cancelaciones. «Escalera» y «pura» son clases ex post de sus propios fills.

## 10. Paths, hashes y reproducción
Scripts (sha256 16 car.): f1_rellenos `a8efc8017f85e104`, f2_ledger `874449e634a6b7e8`, f3_analisis `bdc486a5e206ca7f`, f4_api_dia `0a4cdb03cc9448d2`, f5_closed `697d8c002b9e163f`, f6_fills_bajos `5bc8a2125272f526`, f7_poblacion `14eb16214c96d8e8`, f8_closed `ae5c539c002fa3fb`, f9_actividad `65580f848306a6ab`, f10 `ef56293a44c3a6c1`, f11_treinta_dias `d93c22aa45f7f8be`, f12_pob_vs_w `da24c8f6973cb821` en `/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5/scripts/`.
Salidas: `f3_salida.txt`, `f6_salida.txt`, `f12_salida.txt` (misma carpeta); datos en `/root/polymarket-research-datalogs/wallet_pspspsps5/` (rellenos_D, fills, units, actividad, closed, dia_api_sep_oct, poblacion_D).
Orden: `f1_rellenos.py <días>` -> `f2_ledger.py` -> `f3_analisis.py`, `f6_fills_bajos.py`; `f9_actividad.py` -> `f11_treinta_dias.py`; `f7_poblacion.py <días>` -> `f12_pob_vs_w.py`; todo con `nice -n 19 ionice -c3 python3 -I`. Warnings: en f12 `desenlaces()` escribe su caché habitual de gamma; en f1 se importan funciones de `analisis_mo_money_pares_5m` (solo lectura).

---
# FASE 2 — Ingeniería inversa ex ante de la ventaja de W (24-Oct, aprobada por Javi)
Estado: **EXPLORATORY. Regla NO hallada.** Observable = fills on-chain (hora de bloque ~2,4 s) + Binance bookTicker (hora de RECEPCIÓN, rasgos medidos a t−3 s del fill). No hay órdenes, cancelaciones ni tiempos de reposo de W: son INIDENTIFICABLES con datos públicos. Descubrimiento = cierres 05-13 Oct, holdout = 17-23 Oct (15 días con rasgos; rellenos pasivos <0,10 de TODAS las monedas, 1,6 M fills población, 12.850 de W). Desenlace oficial 100 %. Unidad primaria = fill ponderado por $ (como W) con IC90 bootstrap por días; placebo a nivel unidad.

## 1. Hechos de estructura (scripts f14, 52.328 fills / 10.910 unidades de W)
- Mediana 9 fills por unidad (p90 33): tiene una «pared» de bids a CADA tick de 1 c (95,7 % de los fills <0,10 están en múltiplos de 0,01), ~10 acc por nivel (usd mediano 0,25-0,67 en <0,10; 31 $ en ≥0,90). Rellenos sucesivos: 57 % bajan 1 c, 21 % mismo precio, 22 % suben; dt mediano 0 s (barridos en el mismo bloque), p90 18 s.
- Primer fill de una unidad con fills <0,10: precio mediano 0,05; 24 % empieza ≥0,10 (escalera de verdad). T del primer fill: p10 72 s, mediana 128 s, p90 236 s (entra tarde, nunca al abrir).
- Reparto: Up 48,2 % / Down 51,8 % (sin sesgo de lado, igual por moneda); mercados con fills/día BTC 192, ETH 175, SOL 146 de 288 (rellenos, no decisiones). Hora de cierre casi uniforme (3-5,7 % del coste por hora UTC; mínimo 10-12 h, máximo 21-23 h). Qué mercados NO cotiza es inidentificable (solo se ve lo relleno).

## 2. ¿Es suerte? Placebo por unidades (f16)
W (fills <0,10): EV +0,319 en 4.486 unidades frente a muestras aleatorias de unidades de la población con la misma mezcla de monedas: nulo −0,031 (sd 0,093), **z=3,8, p<1/1500**; por periodos DESC z=1,8 (p=0,03), HOLD **z=3,3** (p<1/1500). La ventaja NO es varianza de la banda.

## 3. Rasgos ex ante que NO explican la brecha (todos medidos en descubrimiento y holdout)
- Brecha emparejada por (moneda, precio 3 tramos, T 3 tramos): población emparejada +0,098 / −0,105 frente a W +0,301 / +0,336 → **brecha +0,20 (DESC) y +0,44 (HOLD)**. Añadiendo la cola (acciones por delante en el nivel y bloque): +0,21 / +0,435: la posición en cola NO la explica (W tiene EV >0 en todas las posiciones; población ≈0 o negativa en todas).
- zs (z de Binance con el signo del lado; + = el spot apoya al lado): W gana sobre todo en zs∈(−1,0] (**+0,58 DESC, +0,78 HOLD**, hit/precio 1,23 y 1,48; IC90 días inferiores +0,31/+0,32) frente a la población en el mismo tramo (+0,175 / −0,012). Esa franja contiene ~50 % del $ de W y ≈75 % de su PnL en tickets. Pero la población en esa misma franja NO gana en el holdout: la franja no es la regla, solo donde W elige mejor. En zs<−1 (spot ya en contra): W ≈ +0,19/+0,25 (cruza 0), población −0,05/−0,19.
- Reglas candidatas simples sobre la población (K=12, alfa Bonferroni 0,0042: zs<−1, zs<0, mov10 contra el lado, caída previa ≥0,2/0,4, T<120/180 y 3 combinaciones): **ninguna** deja EV de población >0 en holdout (rango −0,02..−0,13; hit/precio 0,83-0,89). EV de W dentro/fuera de cada regla es positivo en ambos lados en casi todas → no discriminan a W.
- Tamaño del barrido (niveles <0,10 golpeados en el mismo bloque): sin patrón estable (W: 1 nivel −0,08 / +0,25; 4-7 niveles +0,33 / +0,70; población ≈ −0,19..+0,13).
- **Escalera ingenua (el «mecanismo» candidato S1), optimista y sin cola**: pujar 10 acc en cada tick 0,01-0,09 y darla por rellena la primera vez que cualquier operación pasiva toca el nivel: EV **−0,145 (DESC, IC90 −0,17,−0,12) y −0,254 (HOLD, −0,32,−0,20)** con n≈107 k posiciones; condicionada a T≤180 s, a zs>−1, a mov10 ≥0: −0,09..−0,27 (todos <0). Es decir, estar en todos los ticks pierde incluso regalando la cola. Lo que hace W no es la escalera en sí.
## 4. Hipótesis que quedan (no verificables sin sus órdenes)
(a) Ciclo de vida: retira/recoloca bids (por Binance, por otro mercado o por T) y por eso solo se rellena en barridos «sin información»; su firma sería exactamente lo observado (EV>0 independiente de cola/barrido/zs, hit/precio 1,2-1,5). Solo se contrasta con micro-órdenes reales con cancelación (E1 ms) o con el registro de eventos de nivel (`price_change` del WS, no atribuible a W).
(b) Cuándo coloca: bids de larga vida puestos antes que el resto en niveles profundos (la cola por delante no lo apoya: 26 % de sus fills son los primeros del nivel, igual que la población 27 %).
(c) Selección de mercados/ventana por una señal externa a Binance spot (otro mercado, 15m, libro del lado contrario). No testada: no tenemos el libro del lado opuesto alineado al bloque de cada fill en los 15 días (el registro ms solo cubre 4).
**Veredicto fase 2: regla mínima no encontrada; la brecha persiste (+0,2 a +0,4 por €) tras emparejar moneda, precio, tiempo, cola, z y movimiento de Binance.** La fidelidad de una réplica simulada con libro5 no se midió: no hay regla que simular (la única candidata, la escalera ingenua, da −0,15/−0,25 aun con cola gratis).

## 5. ¿Aplicable a B? (sin tocarlo)
- B = bids al top del lado barato ~0,21, 5 acc, ETH/SOL/XRP, EV −0,012 (n=175). W en la banda 0,10-0,40: +0,165 por € (n=15.037 fills, 33 k$, BTC dominante). Sin regla identificada **no hay cambio de variante que proponer**: copiar «bids en todos los ticks» perdería (−0,15..−0,25 optimista) y las condiciones que sí discriminan nada.
- Lo único portable sin la regla es una MEDIDA, no una política: añadir al forward de B el registro de si cada puja fue rellenada en un barrido con z de Binance en (−1,0] y T 60-180 s, para ver si dentro de esa franja B se parece a W (hit/precio 1,2-1,5) o a la población (0,9-1,0). Requeriría /code-review + OK Javi y no cambia el comportamiento de B.
- €/año: **0 € hoy**. Techo teórico, solo si la regla existiera y se replicase la mezcla de tickets a escala B (≈50 $/día de coste en <0,10, ~6,5 % del de W: 774 $/día): EV +0,3 → ≈15 $/día ≈ 5,5 k$/año; con el stake live máximo (2 €) y 5 € de dedicada, órdenes de magnitud menos. No sostiene 200 k€/año.

## 6. PREREG S1/S2 (forward pasivo, K=2)
`PREREG_S1_S2.md`, sha256 `f39fed75a9ad22c94f6407…` (ver `PREREG_S1_S2.sha256`; `sha256sum -c` en esa carpeta). S1 se espera refutar (prior arriba), S2 es medición de capital. Cron propuesto en el propio fichero (10:25 UTC, no instalado).

## 7. Reproducción y hashes (fase 2)
`f13_features.py` (761970dec0a10835) -> `f14_escalera_w.py` (14c15c15b632a8b9), `f15_regla.py` (ea030b1f05a1f6e5), `f16_placebo_escalera.py` (116f8e4372ea39e9), `f17_cola.py` (d2f064ed34638c68); salidas `f15_salida.txt`, `f16_salida.txt`, `f17_salida.txt`; datos `feat_D.csv.gz`, `poblacion_D.csv.gz` en `/root/polymarket-research-datalogs/wallet_pspspsps5/`. Todo `nice -n 19 ionice -c3 python3 -W ignore -I` con `ulimit -v 3000000`.
Warnings: ref de apertura = media del mid de Binance en [apertura−62, apertura−3] (aprox. del TWAP60 oficial, no el oficial); σ por moneda-día constante; hora de bloque ≈ +2,4 s respecto al casado; el fill es el barrido, no la orden de W; algunas monedas/tokens sin bookTicker quedan fuera de los rasgos (f15 filtra z finito). Los cortes de la fase 2 son post hoc (K declarado = 12 reglas + 8 bandas de zs + 4 bandas de cola/barrido); el placebo y el holdout son lo único confirmatorio.

---
# FASE 3 — Ciclo de vida de órdenes, estructura y 4 hipótesis (24-Oct; encargo de Javi «ir hasta el final»)
Estado: **EXPLORATORY. Mecanismo NO identificado; ninguna de H-A/H-C/H-D lo explica; H-B no es contrastable con datos públicos.** `PREREG_FASE3_H.md` (sha256 `a834f5466530ee0eb4b0…`) se redactó DESPUÉS de la Fase 2 (mismos días): K=4, alfa 0,0125, y los resultados son confirmatorios solo en el sentido de «refutada»; lo positivo (H-E) es post hoc. Datos: ledger on-chain con `order_hash`/tx/contraparte para 14 días de cierre (07-24 Oct; 05, 06, 13-16 Oct no extraídos), rasgos Binance (recepción) de Fase 2.

## 1. Estructura de órdenes (f18/f21; 41.238 fills, 34.885 `order_hash`)
- **Una orden = un fill en un bloque** (fills por orden: mediana 1, p90 2; span entre fills de una misma orden p50 0 s, máx 21 s; 94 % de las órdenes-tick a un único precio). No hay órdenes que descansen y se rellenen a trozos durante minutos: o sus órdenes son de vida muy corta, o son pequeñas y el barrido las completa. La vida de una orden antes del primer fill es INIDENTIFICABLE (no hay eventos de alta/baja públicos atribuibles).
- Tamaños repetidos: orden-tick de 5, 1, 10, 2 acciones y 32-40; tamaño de fill más frecuente 5,0 / 10,4-10,7 (≈5 $ a precio medio) / 10,0 / 1,1. Mezcla de órdenes pequeñas fijas y tamaños mayores (20-200 acc).
- Por tx: 1 fill, 1 orden, 1 nivel, 1 mercado (mediana); p90 2. Reposición en el mismo mercado+lado+nivel con otro `order_hash`: 22,4 % de las órdenes-tick, gap mediano 3 s (p10 0, p90 24 s).
- Contrapartes en tickets <0,10: **2.105 distintas**; top1 4,1 %, top5 13,5 %, top20 29,8 % del $ (HHI 0,007). EV vs top5 +0,155, vs resto +0,328: **no hay un vendedor concreto**. Las contrapartes «malas» (0 aciertos de W en ≥8 fills, primera mitad) no persisten: en la segunda mitad esas mismas dan +0,46 (n=1.196) — era ruido. EV por frecuencia de contraparte: ≥20 fills +0,19; 5-19 +0,51; 2-4 +0,78; 1 vez +0,31 (sin patrón monótono). Contrapartes del carry: 1.399, solapan 4 % con las de tickets.
- Capital (f19): desplegado por cierre de 5 min: media 90 $ (p50 32, p90 264, máx 1.515); 1,99 mercados vivos por cierre (máx 3 = una por moneda). Tickets 3,6 % del capital, carry 63 %. Neteo Up/Down: |YES−NO|/(YES+NO) = 1,00 en todos los mercados (nunca está largo de ambos lados en cantidades comparables; solo 8,7 % de mercados con ticks y carry, 798 de 806 en lados opuestos).

## 2. Las 4 hipótesis
**H-A (selección de mercados por probabilidad calibrada): REFUTADA.** q̂ calibrada (logit ajustado solo con población ex-W de DESC, n=12.717 unidades): coef. logit(p)=0,93, zs=+0,61. Φ(zs) crudo = 0,232 frente a acierto real 0,079 y precio 0,070 (el FV sin calibrar sobreestima ×3; la calibración deja q̂ ≈ 1,1-1,25 × precio). **W compra donde q̂/p es MENOR que la población** (1,105 frente a 1,255 en DESC). La regla q̂/p ≥ 1,43 (p90 de DESC): población +0,069 (DESC) / +0,044 (HOLD), IC90 anchos; W dentro de la regla +1,18 / −0,83 (n=252/494); **W fuera de la regla (94 % de sus fills): +0,26 (IC90 +0,13,+0,37) / +0,41 (+0,20,+0,65)**. Su edge está donde q̂ ≈ precio. No compra «longshots infravalorados» según un modelo con Binance.
**H-B (ciclo de vida: retira/recoloca): NO CONTRASTABLE; las señales indirectas no la apoyan.** (i) Distribución de zs y de mov10 de sus fills idéntica a la población (Fase 2) → no hay firma de cancelar por movimiento de Binance; (ii) markout del spot tras el fill: el spot se mueve MÁS en contra de su lado que en la población (30 s: −0,75 vs −0,55 bps; en su celda buena −0,63 vs −0,41), o sea NO compra justo antes de rebotes del spot; (iii) sin órdenes de larga vida observables. Queda como hipótesis sin test: solo micro-órdenes reales con cancelación o un feed de eventos de nivel atribuible.
**H-C (escalera con reposición): REFUTADA como fuente.** Primera orden del nivel: EV +0,338 (IC90 +0,17,+0,52; n=8.303 fills); reposiciones: +0,159 (−0,09,+0,41; n=2.399); reposición ≤5 s −0,113 (n=1.540), >5 s +0,689 (+0,25,+1,20; n=859). El edge ya está en la primera orden; reponer rápido no rinde. 
**H-D (cartera carry+tickets): REFUTADA como fuente de EV.** Mercados «solo tickets»: EV +0,217 (4.669 mercados, 39.747 $); «solo carry»: +0,009 (216.915 $); **«ambos, lados opuestos»: +0,003** (798 mercados, 90.179 $; los tickets de esos mercados −0,04) — en la cartera el ticket funciona como seguro: en los 18 mercados donde el carry pierde, el ticket del mismo mercado acierta 18/18 y paga +1.708 $, pero el seguro cuesta casi tanto como el carry gana. Correlación diaria tickets-carry −0,43 (diversifica varianza: Sharpe-día 0,71 cartera vs 0,74 tickets, 0,50 carry) pero el EV no sale de combinarlos: los tickets ganan en mercados donde NO tiene carry. Carry no «financia» tickets (capital de tickets 3,2 $ por cierre).

## 3. Dónde está la ventaja (H-E, post hoc, K de Fase 2 + 12 celdas nuevas): tamaño × spot cerca de la referencia
- El tamaño del fill lleva la información: EV por acciones del fill (fills <0,10): ≤20 acc ≈ población (W +0,15/+0,03 vs pob ≈0/−0,18); **20-200 acc: W +0,34..+0,62 (DESC) y +0,47/+0,44 (HOLD) frente a población ≈ 0/−0,09**; >200 acc: −1,0 (129 fills, 0 % acierto). Spearman(acc, win) = −0,007 dentro de W (el tamaño no ordena ganadores uno a uno).
- Celda **acc 20-200 y zs∈(−1,0]**: W **+0,73 (DESC; IC90 +0,38,+1,19; n=1.064) y +0,94 (HOLD; +0,33,+1,44; n=880)**, hit/precio 1,53 y 1,70; población en esa MISMA celda +0,145 (+0,01,+0,28) y −0,03 (−0,29,+0,20), hit/precio 1,13 y 0,98. Por moneda BTC: W +0,69/+1,05 vs pob +0,15/−0,02; SOL +1,04/+2,35; ETH +0,71/−0,22 (cruza 0). La celda contiene ~35 % del coste de tickets y ≈70 % de su PnL.
- Aun igualando tamaño, zs, moneda, precio y T, W gana +0,3..+0,9 por € más que la población: la diferencia viene de algo que no vemos (cuándo y dónde decide poner tamaño). No es timing del spot (markout peor), ni contraparte, ni cola, ni reposición, ni q̂ calibrada.

## 4. Política implementable en 5m barato y simulación
- **No hay política que traducir**: la regla no se ha encontrado; la mejor aproximación observable (bids ≥20 acc en el lado con zs∈(−1,0]) tiene, con las operaciones públicas como relleno optimista (sin cola), EV de población **+0,145 (DESC) y −0,03 (HOLD)**: no pasa el gate (≥+0,10 con IC90>0 en holdout). Simulación con libro5/simulador calibrado: NO ejecutada, no hay regla que simular; el replay disponible (impresiones) ya es el techo optimista y da ≈0 en holdout. Escalera ingenua (Fase 2): −0,145/−0,254.
- B (bandas H35, 5 acc, ETH/SOL/XRP): sus fills de 5 acc caen en la zona donde W tampoco gana (≤20 acc ≈ población). Subir el tamaño de la puja a 20-200 acc no replica W (la población con ese tamaño es ≈0). €/año: 0 € replicable hoy; el PnL de W en la celda (~3,5 k$ en 19 días a su escala) no es trasladable sin la regla de selección.
- Qué sí queda: (1) S1/S2 del PREREG_S1_S2 siguen como medición pasiva (S1 esperado negativo); (2) una sonda de bajísimo coste y fuera de B: registrar en el forward pasivo la celda «fill pasivo 20-200 acc, zs∈(−1,0], BTC» para ver si la población recupera el signo (+0,145 DESC / −0,03 HOLD sugiere que no); (3) lo único que podría revelar el ciclo de vida es una micro-orden real con cancelación (requiere OK de Javi y /code-review) o capturar el feed de eventos del WS (alta/baja/tamaños por nivel) alineado a los bloques de W durante varios días.

## 5. Limitaciones y reproducción
- `order_hash`/contraparte solo para W (la población no tiene order_hash en f7): no se pudo comparar vida de órdenes W frente a población. Fills = barridos, no decisiones. Ref de apertura aprox. (Binance), σ constante por moneda-día. Muestra de órdenes: 14 días de cierre (07-24 Oct, 05/06/13-16 Oct sin extraer; proceso cortado por carga del VPS). Markout de f25 con 5 días y población al 8 %.
- Scripts (sha256 16): f18_ordenes `f59ed9bc22c386db`, f19_cartera `fc636550a01c01c2`, f20_qcalibrada `6b209f8e5d5119e8`, f21_ordenes_cp `e92bf05482531232`, f22_tamano `9450cdd4073a6930`, f23_tamano_w `6b1a41d192d06824`, f24_celda `202a66c277395e39`, f25_markout `6b663c384c8e90f9` en `scripts/`; salidas `f20_salida.txt`, `f21_salida.txt`, `f22_salida.txt`, `f24_salida.txt`, `f25_salida.txt`. Datos: `ordenes_D.csv.gz`, `feat_D.csv.gz` en `/root/polymarket-research-datalogs/wallet_pspspsps5/`. Todo `nice -n 19 ionice -c3 python3 -W ignore -I`, `ulimit -v 3000000`.
