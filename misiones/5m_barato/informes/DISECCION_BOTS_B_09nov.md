# Disección de los bots que rellenan a B — 09-Nov-2026 (preguntas 1 y 2; la 3 solo como hipótesis prerregistrable)
Agente: cheap5m-wallet-intelligence-analyst. Solo lectura y 0 órdenes. No se ha tocado ningún cron, proceso vivo, B, la Sonda ni el F2. Todo con nice 19, ionice 3 y ulimit 3 GB, fuera de 06-09Z y de 22:15-22:30Z.
**Etiqueta: EXPLORATORY. Veredicto: FALTA_INFO.** El mecanismo está identificado, pero ninguna regla ex ante supera el HOLD. Los datos 26-Oct..06-Nov estaban quemados para Q11: aquí DISC y HOLD son los dos exploratorios, y solo confirma el forward desde 10-Nov.

## 0. Datos, unidad y cobertura
- **Rellenos reales de B**: 239 filas H47-B (`contabilidad_wallet_dedicada/movimientos.csv`, 20-23 Oct + 30-Oct..02-Nov), 224 mercados, 8 días. 199 pierden y 40 ganan. EV ponderado −0,081 €/€ (−18,02 € sobre 223,30 € de coste). El tomador sale de `m5_onchain` (fila maker = wallet dedicada; 239/239 identificados). Los 24 rellenos BTC del 30-Oct..02-Nov (subvariante, 0/24 ganan) solo entran en Q1.
- **Población del plano de B**: órdenes tomadoras que rellenan bids de banda, es decir, makers que compran L a pc 0,05-0,35 en 5m ETH/SOL/XRP. Periodo 20-Oct..08-Nov (20 días): DISC = 20-29 Oct (n=220.655) y HOLD = 30-Oct..08-Nov (n=222.393). Unidad = orden tomadora (agrega makers), no relleno. Muestra de ≤25.000 órdenes/día (cobertura 93-100 %). Print del WS emparejado en el 96-99,9 %. Desenlace oficial al 100 %.
- **Reloj**: τ = hora del exchange del print emparejado. Los rasgos usan la RECEPCIÓN ≤ τ−100 ms y el on-chain previo hasta el bloque ≤ τ−3 s. Comprobación de fuga: ningún rasgo supera la AUC del propio precio.
- **Banco de rasgos (174 útiles, 207 brutos)**: libro 5m del lado L y del complementario, libro 15m (bid15), deltas a 0,5-60 s, prints firmados, Binance spot de la moneda y de BTC (retornos a 0,2-300 s, CVD, vol. realizada, distancia a la apertura), perp 5 min (delta, OI), tiempo del ciclo/hora/ms, tamaño y lado de la orden, flujo on-chain previo, wallets distintas e historia del tomador. **No están dentro**: Chainlink/Pyth, libros de 1h/4h, profundidad L2 más allá del top y ticks del perp.

## 1. Pregunta 1 — quién nos rellena cuando perdemos
| Cluster (KMeans k=5 sobre perfiles DISC, silueta 0,19 = estructura débil) | Perfil | Wallets | % € de banda | EV maker DISC (IC90 día) | EV maker HOLD (IC90 día) | Top1 wallet DISC/HOLD | Rellenos B (pierden) | EV B |
|---|---|---|---|---|---|---|---|---|
| C2 HFT tomador (154 órd/día, mayoría BTC, pc 0,54) | latencia | 503 | 57,9 % | −0,008 (−0,083,+0,075) | −0,005 (−0,053,+0,040) | 8 % / 16 % | **179 (146)** | **−0,257** |
| C1 compra el favorito (pc 0,90) | — | 811 | 17,6 % | +0,016 (−0,058,+0,083) | −0,029 (−0,096,+0,028) | 6 % / 4 % | 20 (16) | +0,198 |
| C4 ticket grande (62 acc) | — | 229 | 11,1 % | −0,003 (−0,316,+0,364) | +0,146 (+0,012,+0,309) | 12 % / 23 % | 2 (2) | −1,0 |
| C0 minorista activo | — | 906 | 3,3 % | +0,177 (+0,062,+0,286) | +0,048 (−0,025,+0,123) | 3 % / 11 % | 8 (6) | +1,61 |
| C_pequeño (<50 órd en DISC) / C_nuevo | — | 3.174 | 10,0 % | +0,36 / n.d. | +0,08 / +0,08 | — | 1 (0) | — |
- **No hay un cluster ni una wallet concentrada**. 88 tomadores distintos. Entre los 199 perdedores: top1 12,1 %, top3 25,1 %, top5 34,2 % (top ≤30 % CUMPLE). La heterogeneidad por tomador es la del azar (permutación dentro del día, p=0,74, `s4`). No persiste entre 20-21 y 22-23 Oct (Spearman −0,34, n=12 tomadores, p=0,29). La mayor rellenadora (0x20d2…, 32 rellenos) da a B un EV de +0,15.
- Placebo de etiquetas de cluster en HOLD: la dispersión del EV entre clusters es la del azar (obs 0,174, p95 nulo 0,307, p=0,30). El signo del EV por cluster se mantiene en 3 de 5 de DISC a HOLD.
- **La identidad no aporta información sobre la pérdida más allá del precio** (HGB entrenado en DISC y evaluado en HOLD). AUC: precio 0,668, precio+cluster 0,667, 174 rasgos 0,646 (sobreajuste), aditivo 0,662, placebo 0,492. El EV por decil de riesgo predicho no es monótono.
- **Diferencia clave**: contra el MISMO C2, la población maker queda en ≈0 (−0,008/−0,005) y B en −0,257. **El problema no es QUIÉN rellena, sino CÓMO está expuesta la orden de B.**

## 2. Pregunta 2 — mecanismo (miner automatizado: 870 tests rasgo×cluster, BH-FDR 5 %, réplica en HOLD con |AUC−0,5|≥0,03 y el mismo signo)
- Excluidos los rasgos de identidad/tamaño (que explican la pertenencia de forma trivial), quedan 805 tests de mercado: 714 pasan BH y 342 replican. Con n≈10⁵ todo pasa BH; lo que cuenta es el tamaño del efecto replicado.
- **C2 (el 85 % de los rellenos de B)** dispara **cuando Binance spot se ha movido CONTRA el lado del maker en los últimos 0,5-2 s**: bn_r1 AUC 0,378 en DISC y 0,364 en HOLD, bn_cvd1 0,39/0,38, bid L alto. Es arbitraje de latencia sobre bids rancios.
- C0 y C_pequeño, en cambio, entran después de un movimiento A FAVOR del maker (bn_r1 0,58/0,61) y contra ellos el maker gana. C1 depende del nivel de precio y del tiempo al cierre.
- **Ráfagas** (≥2 tomadores distintos en el mismo bloque y mercado; es el 50 % de las órdenes):
  - En la población, el maker gana solo en las órdenes solas (DISC +0,094, IC90 día +0,036..+0,150; HOLD +0,046) y queda negativo o ≈0 en ráfaga (1ª −0,047/−0,010, siguientes −0,077/−0,009).
  - **B**: 87/210 rellenos en ráfaga, EV −0,39/−0,41 (−34,1 €), frente a 123 solos con EV **+0,189 (+24,5 €)**.
  - Hueco entre el 1er print de la ráfaga y el relleno de B: p25 28 ms, p50 89 ms, p75 575 ms. Solo el ~25-30 % es cancelable (cancelación 61 ms + WS).
- **Edad de la orden de B al rellenarse** (post_ok del ledger → print): p25 297 ms, mediana 826 ms. Rellenos con edad 0,3-3 s: EV −0,26/−0,29 (n=114). Con edad 3-10 s: +0,62 (n=36). B re-pega unas 8 órdenes por mercado y se expone justo cuando el precio va contra ella.
- **Situación de B en la población**: un relleno en el top con Binance en contra (bn_r1 ≤ −1 bp) da DISC −0,125 (IC90 día −0,238..−0,019), pero en HOLD −0,042 frente a −0,036 sin el disparador: **NO replica**. Rellenos de B con bn_r1 ≤ −1: 61/210, EV −0,36 frente a +0,09 (in-sample; coincide con BN_W300_X2 de E1C, que quedó EXPLORATORY).

## 3. Lo que no vemos
1. **Residuos**:
   - El 33 % de los inicios de ráfaga no tiene ningún disparador visible (ni Binance, ni libro, ni print), y esos son benignos (EV +0,028 frente a −0,056 de los que sí lo tienen).
   - 72 de 249 wallets grandes tienen un ms dentro del segundo NO uniforme (BH 5 %): son temporizadores. En cambio, el 1er print de ráfaga sí es uniforme: no hay un ciclo de infraestructura.
   - Hay tamaños repetidos (moda hasta 100 %) y wallets que solo operan 5-6 días.
   - Tabla en `datos/s9_huellas_wallets.csv`.
2. **Fuentes candidatas que no recogemos o no hemos usado** (coste, latencia):
   - (a) aggTrade del perp de Binance, tick a tick: gratis y público, ~igual que spot; perp suele liderar.
   - (b) Coinbase/OKX/Bybit spot WS: gratis.
   - (c) Chainlink/Pyth (ya en disco, no metido en el banco).
   - (d) Libros 1h/4h del mismo activo (ya en disco).
   - (e) L2 por orden del CLOB (logger previsto 16-17 Nov): recotizaciones de makers antes de la ráfaga.
   - (f) Horas de funding y cierres de vela.
   - (g) Mempool de Polygon: inútil, va después del casado.
3. **Test mínimo por fuente**: AUC del movimiento en [τ−1 s, τ−0,1 s] para inicio de ráfaga frente a orden sola. Se captura solo si supera a Binance spot en ≥0,03 en DISC y en HOLD.
   - Orden: (c) y (d) a coste 0 → (a) logger fase 0 gz, retención 7 d, ~150 MB/día fuera de git → (e) cuando llegue el L2.
   - **Propuesta, no ejecutada.**

## 4. Contra-política (SOLO hipótesis para prerregistrar; no se ha afinado ni elegido mirando el forward)
- **H-DB1**: no tener el bid de B en el libro (cancelar o no re-pegar) mientras r_Binance(1 s, recepción) ≤ −1 bp contra L. Se repone tras 1 s sin movimiento en contra.
- **H-DB2**: cancelar al primer print contrario en el mercado (W=1 s, c=τ−100 ms).
  - En la población: EXCESO DISC +0,046 (IC90 −0,011..+0,106), HOLD +0,020 (−0,002..+0,042).
- Ojo: los umbrales salen de DISC y de los rellenos de B (sesgo declarado).
- **Cómo se mediría**: forward desde 10-Nov en el simulador con las MISMAS guardas del ejecutor de B, EV ponderado por €, IC por cierre y por día, sin los 2 mejores días, contra placebo (disparo aleatorio con la misma tasa) e inversión.
- **Qué la refuta**: EXCESO ≤0 o IC90 por día que cruce 0 con ≥10 días; o que el placebo dé lo mismo.

## 5. Reproducción (`experimentos/5m_barato/diseccion_bots_b_09nov/`; datos 8,2 GB en VOL `agentes_datos/diseccion_bots_b_09nov`, borrables tras la validación)
- Scripts (sha16): s1 c57932e9, s2 7f9cf61e, s3 2c56628d (run_s3.sh dfcd6d3d), s4 d369443f, s5 5f9f1980, s6 37984a5f, s7 88fe1675, s8 1b6d984d, s9 9e3bfbaf, s10 1e536423.
- Salidas: `datos/s8_A.out`, `s8.out`, `s9.out`, `s10.out`, `s11_proxy_B.out`, `s12_rafaga_disparo.out`, `s8_tabla_clusters.csv` (bac7091e), `wallet_cluster.json` (43bf7f06).
- Orden de ejecución: `s2 D…`, `run_s3.sh D…`, `s5 D…`, `s1`, `s4`, `s7`, `s6`, `s8` (`SKIP_A=1` para saltar el placebo), `s9`, `s10`. Todos con `ARROW_DEFAULT_MEMORY_POOL=system OMP_NUM_THREADS≤2 ulimit -v 3000000 nice -n 19 ionice -c3`.
- **Avisos**:
  - Los clusters son débiles.
  - B = 210 rellenos in-sample.
  - BTC queda fuera de la población.
  - Los rellenos de otros makers no son órdenes recién re-pegadas como las de B: el proxy de la población no reproduce la exposición de B.

**Siguiente paso único:** que el statistical-validator congele PREREG_DB1 (H-DB1 + H-DB2, con placebo e inversión) y se evalúe en forward pasivo desde 10-Nov con el simulador de B sobre el registro ms (y el L2 cuando exista).
