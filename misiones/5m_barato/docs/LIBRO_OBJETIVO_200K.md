# Libro de cuentas del objetivo 5m barato — 200.000 €/año netos como SUMA de subestrategias

Lo mantiene `cheap5m-objetivo-200k` (o `cheap5m-risk-economics` / el chief). Solo cuenta como ingreso lo que está en el
peldaño ≥5 de `FLUJO_DE_TRABAJO.md` (micro-real, live, rampa) con su gate superado; todo lo demás va en "potencial" y
etiquetado. Toda cifra con fecha, n, IC90 por días y fuente. **EV siempre ponderado por € (Σpnl/Σcoste).**
Unidades: pUSD ($) tal como salen de los ficheros; NO se ha convertido a € (convertir restaría ~10-15 %).

## Resumen — corte 19-Oct 06:50Z (2ª pasada; la 1ª fue el 17-Oct 14:10Z)

| Escenario (anual) | pUSD/año | Cómo se calcula |
|---|---|---|
| **Ingreso VALIDADO (peldaño ≥5 de la familia)** | **0** | nada ha llegado al peldaño 5; la familia solo tiene dry-run/forward |
| Conservador (lo que sigue en pie sin su mejor operación/día) | **0** | V4 sin su mejor operación EV −0,002; H5M sin 2 mejores días +0,006; R5K día 1 −0,275 |
| Base (15 % del optimista) | **≈ 12 k** | retención observada de estimaciones exploratorias en forward: 11 % (precierre multi-instante +0,089→+0,01), 28 % (H5M +0,142→+0,040 ponderado), ~0 % (15m reposición +0,263→−0,006): media 13 %, se usa 15 % |
| Optimista NO validado (todo se cumple en su cola favorable, sin doble conteo) | **≈ 78 k** | tomador 4,9 k + H35 alts a 5 acc 9,4 k + R5K 64,2 k (BTC) |
| Techo teórico si H35 escalara LINEALMENTE a 50 acc (no medido) | ≈ 163 k | 4,9 + 94 + 64,2: aun con TODO a favor queda < 200 k |
| **Hueco hasta 200 k** | **200.000 validado · ≈ 122 k contra el optimista · ≈ 37 k contra el techo teórico** | |

Fórmulas (anual = coste/día × EV × 365; fuentes en cada fila): tomador 2,08 ejec/día × 23,4 $ × 0,277 × 365 = 4,9 k;
H35 alts 354 $/día × 0,073 × 365 = 9,4 k (×10 = 94 k si K=50); R5K 830 $/día × 0,212 × 365 = 64,2 k.

**Qué falta, en orden (corte 19-Oct):**
1. **Edge**: todo es EXPLORATORY. Lo único con IC90 por días > 0 (H5M sin BTC +0,085 (+0,011,+0,145), 10 días) es la
   POBLACIÓN de makers, no lo que capturaríamos nosotros; y se miró después de ver los datos (post hoc).
2. **Capacidad (el cuello real)**: 548 €/día = coste-base diario de **11 k$ a EV +0,05, 5,5 k$ a +0,10, 2,7 k$ a +0,20**.
   Lo medido hoy: tomador 16-49 $/día; H35 alts 354 $/día; R5K 550-830 $/día; la piscina entera de makers ex-BTC mueve
   35 k$/día (BTC 270 k$/día). Hacen falta 8-31 % de la piscina alt, o capturar ≥1 % de BTC con EV ≥ +0,2.
3. **Capital**: NO es el cuello de la rotación (exposición simultánea de decenas de $), sí del RIESGO: con el modelo
   Browniano (ruina 5 %: B = ln20·σ²/(2μ)) y σ = 2,05 por € y fill medido, H35 a K=50 necesita ~0,9 k$ (si el EV es el
   optimista) a ~6 k$ (si es el base); R5K ~0,3 k$ a ~1,8 k$. Hoy: principal 40,57 $ libres (+1,04 $ en posiciones;
   `data/live/balance_real.json` 19-Oct 06:30Z, `pusd_onchain` 49,72 → diferencia ~9 $ sin conciliar con `free_usdc`),
   dedicada 19,59 pUSD (memoria 17-Oct 08:45Z y mensaje del chief; no re-verificada on-chain hoy: la dirección completa
   solo está en la credencial, que no se lee). Toda rampa es decisión de Javi.

## Cambios desde la 1ª pasada (17-Oct 14:10Z)

- **H5M (población, `unidades_2026-10-09..18.csv.gz`, 20.078 unidades, 10 días, desenlace 100 %)**: ponderado por € **+0,040**
  (Σpnl 121,6 k$ / Σcoste 3,053 M$), por unidad +0,122 (el +0,121 del vigía). EV medio diario ponderado +0,035, IC90 por días
  **(−0,025,+0,095)**, 7/10 días +, sin 2 mejores días **+0,006**. Día a día ponderado: −0,019, +0,066, +0,063, +0,065,
  +0,063, +0,134, +0,197, +0,017, −0,060, **−0,174 (18-Oct)**. BTC es el 89 % del coste (EV +0,034, IC90 (−0,036,+0,094),
  sin 2 mejores −0,006) y manda el signo del día (BTC 15-Oct +69 k$, 17-Oct −19 k$, 18-Oct −46 k$). **Sin BTC: +0,085, IC90
  días (+0,011,+0,145), 7/10, sin 2 mejores +0,032, coste 34,8 k$/día, PnL 3,0 k$/día** (ETH+SOL +0,105 (+0,023,+0,171), 8/10).
  Post hoc, varias miradas (sin BTC, ETH+SOL): EXPLORATORY. El «CONFIRMADA» del vigía (6/6 gates) mide la media de
  cocientes por unidad, no dinero.
- **V4 OOS** (`logs/vigia_5m_barato_forward.log`, 19-Oct 04:39Z): 58 señales, **25 ejecutables a L215**, +15,76 €, EV +0,277,
  IC90 días (−0,356,+1,046), 12 días (7 +), sin BTC −0,461, sin top-1 % **−0,002**, sin mejor día +0,013, **96 % del PnL en un
  día**, gates 6/10 (pasan G2 días, G3 EV, G5, G8, G9, G10; fallan G1 n 25/40, G4, G6, G7). Ya-visto: es UNA operación BTC.
- **R5K forward** (`logs/vigia_5m_barato_r5k.log`, 18-Oct 09:30Z; la de hoy sale a las 09:30Z): 17-Oct, **61 unidades**, coste 552 $,
  EV ponderado **−0,275**, IC90 por cierre (−0,634,+0,119), sin top-20 −1,0, 1/10 días. UN día: no refuta (listón: ≥40
  unidades, ≥10 días, EV<+0,05 o IC90 cierre cruza 0 o sin top-20 ≤0) ni confirma.
- **Colocación**: dataset `m5_maker_colocacion` COMPLETE 9/9 (driver.log 17-Oct 18:19Z). Contiene los motores DEEP_k1/k2 y JOIN de
  H35 para 14-16 Oct y **reproduce a 3 decimales las cifras de H35 del 14-Oct** (ETH k2 +0,186, XRP k1 +0,102, BTC k2 −0,011,
  ALL k2 +0,022): H35 está de hecho completo 9/9 (el reintento 15-16 «sin hueco» ya no hace falta). Modelo `coloc_modelo.py` sin correr.
- **V7 (forward formal, `v7_informe.json` 19-Oct 05:54Z): n=1, +2,21 €, 1 día**. El «revive 16-Oct, 6 mercados, +6,49 €» salió
  de un análisis de descubrimiento, NO del vigía: no cuenta. **V6** (`v6_informe.json`): L355 n=3 −3,04 €, L475 n=3 +2,46 €.
  **V5**: 11 señales, L215 4 ejecuciones +17,04 € (BTC 2, +14,78), L355 1 ejecución −0,006; 3/11 gates. **V2** (log 05:05Z):
  15 mercados +9,68 €, EV 0,267, sin mejor día −0,229. **V3a**: 5 mercados +0,63 €, EV 0,067, IC90 (−0,543,+0,003).
- **FV v4** (OOS 14-18 Oct, `m5barato_forward_diario.log` 06:13Z): ΔBrier vs mid negativo en 5/5 días, IC90 (−0,0029,−0,0019), R² 0,12-0,29;
  como tomador n=1.126, **EV +0,021, IC90 días (−0,023,+0,067)**, días +0,042/+0,066/−0,024/−0,068/+0,096. Sigue REJECTED
  como tomador; la información existe pero se cobra como guarda del maker (H34), no como orden.
- **PRECIERRE** (live 2 €, `data/live/trades.csv`, 33 cerradas desde 24-Sep): 17/33, **+8,30 €**, EV ponderado +0,133; desde el
  arreglo FOK de 17-Oct 08:16Z solo **2 órdenes** (+6,24 €). Días con orden: 19 (9 +), media +0,437 €/día, IC90 (−1,14,+2,01).
  Anualizado a 2 € ≈ 120 €. Referencia fuera de la familia; rampa 5 € exige ≥40 órdenes post-arreglo (hoy 2).
- **15m barato reposición** (fuera de la familia, `vigia_15m_barato_reposicion_forward.log`): 6 días, 778 unidades, EV −0,006, IC90
  (−0,178,+0,168); la exploración +0,263 (IC90 +0,024) se evaporó en forward. Es el tercer ejemplo de retención ~0.
- **Rebate verificado en metadata 5m hoy** (gamma GET `btc-updown-5m-1792391700`, 19-Oct ~06:45Z): `feeSchedule {rate 0.07,
  takerOnly true, rebateRate 0.2}`, `orderMinSize 5`, `rewardsMinSize 50 / maxSpread 4.5` sin programa (clobRewards None).
  Rebate de maker ≈ 0,2·0,07·(1−p) por € (+0,011 a p=0,22) — falta comprobar que el pago llega: solo un relleno real lo dirime.

## Subestrategias

| Subestrategia | Peldaño / estado | EV/€ ponderado (IC90) | n / días | Capacidad medida | Anual (cons / base / opt) | Solape | Siguiente prueba |
|---|---|---|---|---|---|---|---|
| **H43 R5K** (maker tras 5.000 acc, **solo BTC**: ninguna otra moneda llega a 5.000) | 2 · EXPLORATORY (24 celdas miradas, 11 días) | descriptivo +0,212 (cierre +0,102/+0,326), sin 2 mejores días +0,141, sin top-20 +0,117; **forward día 1 −0,275 (−0,634/+0,119)** | 1.010 unid./11 d + 61 unid./1 d | 92 unid./día × 9 $ (K=50) = 830 $/día; residual de volumen tras cruzar 5.000: mediana 1.191 acc (p10 134, p90 4.977; 17-Oct, 61 unid.) | 0 / ≈ 9,6 k / 64,2 k | BTC maker (excluye H35 alts) | vigía 09:30Z (forward); fill/cola con micro-órdenes brazo 2 |
| **H35 DEEP_PEG alts** (ETH k2, SOL k1, XRP k1; elegidos en DESC) | 2 · EXPLORATORY, simulador SIN calibrar (NO_REPRODUCE→criterio v2 post hoc); cola desconocida en ~75 % de pujas | ETH+SOL+XRP k1: DESC +0,076 (−0,128,+0,199) 4/6 d, sin 2 mejores −0,003; **OOS 14-16 +0,067** (−0,121,+0,269) 2/3 d, sin 2 mejores −0,046; 9 días +0,073 (−0,056,+0,153) 6/9, sin 2 mejores +0,030; JOIN mismas monedas OOS +0,022 | 3.050 rellenos / 9 d (OOS 1.088 / 3 d); por moneda OOS: ETH +0,046, SOL +0,066, **XRP +0,121 (+0,020,+0,229) 3/3** | 339 rellenos/día, 354 $/día a 5 acc (29,6 % de las pujas se rellenan); K>5 NO simulado (columnas x10/x20 vacías) | 0 / ≈ 1,4 k / 9,4 k (K=5); 94 k si K=50 (no medido) | maker de banda (lo contiene), H39 | micro-órdenes brazo 1 (calibrar cola) + H45 escala |
| **H35 BTC** (DEEP) | REJECTED en sim para BTC | k1 DESC −0,068 (−0,137,−0,007) 1/6 d; OOS −0,011 | 1.703 + 1.069 rellenos | — | 0 | — | fuera de la prueba real |
| **Maker de banda** (unirse al bid, 5 acc, JOIN) | 2 · línea base | JOIN sim todas las monedas DESC −0,034, OOS +0,022 (+0,032 con rebate); población ponderada 10 d +0,040 (IC90 cruza 0); nuestras primeras 5 acc ≈ +0,007 (10-13 Oct, auditoría 17-Oct) | ~2.000 unid./día | ~2.200 $/día a 5 acc | 0 / ≈ 2 k / ≈ 14 k | contiene a H35/R5K | es la línea base a batir, no se suma |
| **Modelo de colocación** | 1 · dataset COMPLETE 9/9, modelo sin correr (lo corre otro agente hoy tras 09:15Z) | — | 9 días (DESC 05-10, OOS 14-16) | — | — | todas las maker | gate ≥ +0,05 sobre mejor k de la línea base por moneda, IC90 días y cierre > 0, placebo e inversión peores |
| **H39 MM-REPOSO** | 1 · PENDING, bloqueada por calibración | ganadoras on-chain +1,1/+1,6 %/€ (2 wallets, 7/7 d OOS) | — | — | — | maker | tras calibrar la cola |
| **V4 / V2 / V3 / V5 / V6 / V7** (UN solo canal tomador: no se suman) | 4 · FORWARD congelado | V4 OOS +0,277 (−0,356,+1,046), sin top-1 −0,002; V7 n=1; V6 n=3; V2/V3 sin muestra | 25 ejec./12 d (V4) | 2,08 ejec./día; nocional al ask nivel 1 p50 13,6 $, p90 234 $; coste/día 16 $ (tope 10 $/señal), 49 $ (tope 50 $) | 0 / ≈ 0,7 k / **4,9 k** (15 k sin tope por señal) | mismo evento | seguir forward; G1 n≥40 ≈ 26-28 Oct (G4/G6/G7 fallarán salvo cambio); «28-37 k» de V7 y «30 k» de V6 son de descubrimiento y NO cuentan |
| **PRECIERRE** (referencia, fuera de la familia) | 6 · LIVE 2 € | +0,133 (33 órdenes, 17 aciertos, IC90 días cruza 0) | 33 / 19 d con orden | ~1,3 órdenes/día | ~0,12 k a 2 € | — | rampa 5 € solo con ≥40 órdenes post-arreglo (hoy 2) |
| **H44-H47** (propuestas de esta pasada, ver abajo) | 0 · sin registrar | — | — | — | — | — | el chief decide |

## Cerrado (no reabrir sin mecanismo nuevo)
Cosechar al abrir (H10/H11/H32/H33), pares maker estáticos, FV v1-v3 y FV v4 tomador, H26 "Binance en contra" (look-ahead),
H26-MS y la predicción de Binance con margen (anticipa volatilidad, no pérdida), precursores externos (Bybit, barrido en
otra moneda), salidas tras relleno (H37/H40/H41), LOWLOW/LONGSHOT tomador, caja de 2 patas, vender bid15 rancio.

## Los 10 ángulos (corte 19-Oct)

1. **Edge**: ninguna subestrategia bate su línea base con IC90 por días > 0 y sin sus mejores días *en lo capturable*.
   Lo más cercano: H35 XRP OOS (+0,020,+0,229) con 3 días (el gate pide ≥6) y H5M ex-BTC (+0,011,+0,145), ambas post hoc.
2. **Capacidad/frecuencia**: es el cuello. Tomador 2 ejec./día con 13,6 $ de mediana; maker alts 339 rellenos/día de 1 $; R5K
   61-92 unid./día solo BTC. K>5 no está simulado para DEEP (las columnas x10/x20 del dataset están vacías).
3. **Capital/rampa**: para medir mecanismo basta la dedicada; para el escenario optimista a K=50 hacen falta 0,9-6 k$ de
   colchón de riesgo. La rampa 2→5→10 € es de PRECIERRE (0 escalones ganados); en 5m barato aún no hay peldaño 5.
4. **Costes**: fee taker 0,07·p(1−p); rebate maker 0,2 sobre esa fee (verificado en metadata 5m hoy, no el pago); sin recompensas de
   liquidez; el maker no paga fee. Slippage del tomador: a +150 ms 22/43 asks ya consumidos (H25).
5. **Universo**: 6 monedas con gate propio; el edge maker está en alts (ETH/SOL/XRP) y BTC solo en R5K; 15m BTC reposición
   forward −0,006; 4h sin capacidad (H31). Falta medir 15m alts (misma regla congelada, solo población) y 60 min.
6. **Ejecución/latencia**: maker 68 ms alta / 60 ms cancelación; tomador 215 ms; desfase te→rx 21/38/161 ms (nice −10 al lector
   aplicado 17-Oct 22:15Z); harness de órdenes reales YA existe en dev (`experimento_pares_cola_15m.py`, 1.457 líneas, 26
   /code-review, ledger por hash EIP-712, cancelación por hash, kill, cuadre on-chain, ensayo en seco) → adaptarlo, no escribir de cero.
7. **Quién gana**: la piscina maker alt gana +0,085; persistentes tomadoras ≈ menos explotables (+0,058 al maker vs +0,19 resto);
   H39: 2 cosechadoras +1,1/+1,6 %/€; V7: 6 wallets = un operador −45 % desde el pico, sustituidas por 0x56f609c6 (17-Oct:
   8.500 fills maker + 3.383 tomador, 245 k acc maker) y 0x29efa7c2.
8. **Regímenes**: día malo 18-Oct (H5M −0,174, todas las monedas bajan salvo ETH); escalón 13-Oct del margen 5m/15m. Con 10 días no
   se puede separar régimen de ruido; el signo del día lo manda BTC (89 % del coste).
9. **Combinación**: tomador (un evento = una apuesta), H35 y R5K son monedas distintas (aditivas), línea base y H39 contienen a
   H35 (no se suman); PRECIERRE independiente pero del mismo bolsillo de riesgo. Suma optimista sin doble conteo ≈ 78 k.
10. **Lo rechazado, planteamiento**: FV v4 falló como orden (taker +0,021) pero ΔBrier < 0 en 5/5 días → mal planteado como
    tomador, vive como guarda del maker (H34 OPEN). 15m reposición, pares, cosechar: falló la idea. Nada se reabre.

## Palanca de mayor valor de la información HOY

**Calibrar la cola con rellenos reales (micro-órdenes H35 en ETH/SOL/XRP).** Es el único dato que falta para todo el hilo maker
(colocación, H35, H39, escala K, captura de R5K): el 75 % de las pujas simuladas tienen cola desconocida y el simulador no
reproduce a la población (NO_REPRODUCE). Sin esa calibración, 64 k decisiones/día de libro5 no se pueden convertir en una cifra
creíble; con ella, el offline se vuelve fiable y barato. **Ojo: lo que NO medirá es el EV** (abajo).

### Qué aprenderíamos y con cuántas órdenes (cálculo propio, base `base_*.csv.gz` de colocación)
- σ por relleno de 5 acc a ~0,2 = **2,05 por € (≈ 2,1 $)**; coste medio 1,05 $. Para que el IC90 del EV caiga bajo ±0,05 hacen
  falta ~4.500 rellenos; para detectar +0,07 con 80 % de potencia ~3.900; a 339 rellenos/día de toda la piscina y 5 pujas vivas
  serían >15 días, con **σ acumulada ≈ 115-130 $**. **El EV no se mide con dinero real en esta cartera.**
- Sí se mide (binario/tiempo, varianza baja): tasa de relleno real vs simulada (p≈0,30: **±5 pp con 230 pujas, ±3 pp con 630**),
  tiempo hasta relleno, acuerdo sim/real puja a puja (2×2), cola delante al entrar, markout +5/+30/+120 s por relleno (σ SUPUESTA ~0,2 por €, `mo30_*` no está calculado en el dataset:
  ±0,04 con ~70 rellenos), pago del rebate, latencias propias y la maquinaria (ledger, cancelación por hash, kill, cuadre).
- Diseño en dos escalones: **A (≈0 $, 1 día)**: 30-40 pujas post-only a 0,01-0,03 (5 acc = 5-15 c) para validar maquinaria y
  cuadre; **B (calibración)**: **~230 pujas** (≈ 1-1,5 días con 5 vivas; ≈ 70 rellenos) en ETH(k2)/SOL(k1)/XRP(k1), 1 puja por
  unidad, T 270→60 s, repegado como H35. Brazo 2 (R5K, BTC, K=5, solo con el disparo): ~230 pujas en ~3 días (61-92 unid./día).
- **Riesgo que Javi debe ver antes del OK**: el tope «≤5 €» es de EXPOSICIÓN simultánea; la pérdida acumulada no queda acotada por
  él. Con ~70 rellenos y EV≈0, σ ≈ 17 $: P(perder ≥5 $) ≈ 39 %, P(≥10 $) ≈ 28 %, P(vaciar los 19,6) ≈ 13 % (más con parada por
  camino). Un kill por pérdida acumulada de 5 € se dispararía por azar en la mayoría de las corridas (trampa kill-switch documentada).
  Propuesta: **N de pujas fijo (230), parada solo por suelo de saldo (p. ej. 12 pUSD) y por fallo de maquinaria, nunca por PnL del
  experimento**; decidir presupuesto de pérdida explícito.
- Dos cautelas de ejecución: (a) el harness exige ≥1 $ de nocional y precio ∈[0,20,0,80]; la banda 0,11-0,30 con 5 acc queda en
  0,55-1,5 $ → comprobar si el mínimo de 1 $ aplica a límite post-only o subir a 6-10 acc; (b) el harness es 15m (T 840→90): hay
  que adaptar T, una sola cara, repegado k=1/2, y repasar solo el diff con `/code-review` medium (acotar a 3-5 invariantes:
  pérdida/exposición, identidad por hash, doble envío).
- **Gate de la prueba (propuesto, fijar antes de empezar)**: simulador VÁLIDO para esa regla si |tasa real − sim| ≤ 8 pp, P(relleno
  real | relleno sim) ≥ 0,70 y P(relleno sim | relleno real) ≥ 0,70 y |markout real − sim| ≤ 0,03; si no, el simulador queda
  inválido para variantes dependientes de cola y el hilo maker pasa a «solo dinero real».

## Las 3 pruebas de mayor valor (orden de ejecución)

1. **Micro-órdenes reales, escalón A hoy-mañana y B tras el OK** (arriba). Coste: ingeniería (adaptar harness + diff review) y
   ≤ 1 $ (A) / EV≈0 ± ~17 $ (B). Gate: el propuesto. Quién: execution-engineer en dev + chief + OK de Javi (decide el presupuesto de pérdida).
2. **H45 Escala + OOS 17-18 Oct del simulador de H35** (offline, gratis): ¿sigue el EV de DEEP a 25/50 acc y con los 2 días nuevos
   (incl. el día malo 18-Oct)? Decide si la capacidad maker alt es 9 k o ~90 k/año. Coste: 2 corridas de dataset (~25 min/día) +
   K en el simulador, turno nocturno 00-06Z con `ulimit -v` 2 GB (si los maker_ms crudos de 17-18 Oct están en el volumen).
   Quién: execution-engineer. Va ANTES de pedir más stake.
3. **Forwards gratuitos que sí pueden mover el libro**: R5K (09:30Z, gate ≈ 27-Oct), **H44 vista alt de H5M** (nuevo, ≈ 29-Oct) y
   V4 (G1 ≈ 26-28 Oct). Coste ≈ 0 (H44 son ~20 líneas sobre los `unidades_*.csv.gz`). Quién: chief (cron externo, no toca los
   vigías congelados). Son lo único que puede subir el escenario conservador por encima de 0 sin dinero.

Colocación (modelo) corre hoy tras 09:15Z por otro agente: su salida decide la política de las pujas de B (qué t_q y k), pero
NO sustituye a la 1: sin calibración un +0,05 en simulación no es un +0,05 real.

## Hipótesis nuevas falsables (propuestas; solo el chief las registra)

- **H44 · H5M-ALT (vista externa del vigía congelado)**. Unidad: mercado-lado de ETH, SOL y XRP (fijadas ahora, BNB/DOGE fuera por
  n), banda 0,10-0,30, T 60-300, igual que H5M, leyendo `unidades_*.csv.gz` ya generados. Medida: Σpnl/Σcoste por día. **Forward
  desde 19-Oct** (los 10 días anteriores son la muestra en que se eligió). Gate: ≥10 días nuevos, EV ponderado ≥ +0,05, IC90 por
  días > 0, sin 2 mejores días > 0, ≥6/10 días +. Refutada si EV <+0,02 o IC90 por días contiene 0 a los 10 días. Coste: ~0.
- **H45 · H35-ESCALA**. Misma regla H35 (DEEP_k1/k2 elegidos en DESC por moneda, ETH/SOL/XRP), tamaños 5/25/50 acc y OOS 14-18 Oct.
  Gate: EV(25 acc) ≥ EV(5 acc) − 0,03 y rellenos/día × coste ≥ 4× el de 5 acc; si EV(25) ≤ 0 → capacidad H35 ≈ 9 k/año y el hilo
  maker alt queda cerrado como camino a 200 k. Coste: corrida nocturna.
- **H46 · R5K-NORM (alts)**. Umbral por moneda = cuantil 0,95 del volumen acumulado final por unidad en DESC (05-10 Oct), misma
  regla R5K (puja ≤50 acc al mejor bid con T 60-270 s tras cruzar), ETH/SOL/XRP, forward externo desde 19-Oct. Gate por moneda: ≥40
  unidades, ≥10 días, EV ponderado ≥ +0,05, IC90 por cierre > 0, sin top-20 > 0. Mecanismo: dosis-respuesta de R5K normalizada
  por actividad de la moneda; amplía la capacidad (hoy solo BTC). Multiplicidad: 3 monedas, un único cuantil. Coste: script de
  solo lectura sobre `m5_onchain` (patrón `vendedores_tardios_17oct`).
- **H47 · SIM-REAL (la calibración como hipótesis)**. Regla fijada arriba: 230 pujas reales H35 vs el simulador CONS reproduciendo
  las mismas decisiones; gate de acuerdo (±8 pp, 0,70/0,70, markout ±0,03). Falsable: si falla, el hilo maker offline se cierra.
- (Nota, no es hipótesis de la familia) **Universo**: repetir la regla congelada de 15m reposición en ETH/SOL/XRP como vista de
  población (BTC 15m forward −0,006, pero en 5m las alts rinden más que BTC). Solo si el chief quiere ampliar al 15m.

## Se puede descartar ya (como camino a 200 k)

- **Toda la rama tomador (V2, V3, V5, V6, V7) como palanca de escala**: aun con EV +0,277 el techo por profundidad es ≈5 k$/año
  (15 k sin tope por señal). Se queda el cron; no gastar más atención diaria. Las cifras de descubrimiento (V6 30 k, V7 28-37 k)
  no tienen respaldo forward (n=3, n=1).
- **FV v4 como tomador** (+0,021 OOS): ya REJECTED; solo como guarda (H34).
- **BTC en H35** (negativa en DESC y OOS), **DOGE/BNB en H35** (OOS n=80/74, DESC con signo contrario: sin conclusión) → fuera de la
  prueba real; BTC se cubre aparte con R5K.
- **JOIN al mejor bid como política** (negativo en DESC en BTC/XRP/ETH).

## Trampas cazadas en esta pasada (para el chief: añadir a TRAMPAS)

1. **Condicionar la unidad por su tamaño FINAL fabrica edge**: en H5M las unidades con ≤5 rellenos dan +0,336 (10/10 días) y las
   de >500 dan +0,037; el número final de rellenos depende del desenlace (el lado que gana sale de la banda al subir). Cualquier
   regla debe fijarse con información causal (R5K lo hace con el acumulado en tiempo real).
2. **«Tope de 5 €» es exposición, no pérdida**: la varianza por relleno (±2 $) hace que ese tope no acote nada acumulado; un kill por
   PnL acumulado se dispara por azar. Presupuesto de pérdida explícito + N fijo.
3. **Retención de exploratorias**: 3 casos medidos (11 %, 28 %, ~0 %). Ningún escenario base debería superar ~15-25 % del optimista
   mientras no haya forward.
4. **Vigía «CONFIRMADA» por media de unidad**: H5M 6/6 gates con +0,121, ponderado +0,040 con IC90 por días (−0,025,+0,095).
5. «Revive» de V7 (6 mercados, +6,49 €) no es del vigía formal (n=1): citar siempre el informe del hash.

## Fuentes (todas leídas/recalculadas el 19-Oct 06:10-06:55Z, solo lectura, `ulimit -v 1500000`)

H5M: `/root/polymarket-research-datalogs/vigia_5m_barato_maker/unidades_2026-10-09..18.csv.gz` (recalculado: ponderado por € y por días,
t(9)=1,833) y `logs/vigia_5m_barato_maker_forward.log`. V4/V2/V3: `logs/vigia_5m_barato_forward.log`, `_v2_`, `_v3_`; capacidad:
`datalogs/vigia_5m_barato/eventos_2026-10-*.csv` (primeros eventos desde 06-Oct, clase L215 A/D, `L215_precio × L215_disp_nivel1`).
V5/V6/V7/FV v4: `logs/m5barato_forward_diario.log` y `datalogs/m5barato_mision/v{5,6,7}_informe.json`. R5K: `logs/vigia_5m_barato_r5k.log`,
`datalogs/vigia_5m_barato_r5k/2026-10-17/out/band_2026-10-17.csv.gz`. H35/colocación: `datalogs/m5_maker_colocacion/base_2026-10-*.csv.gz`
(filtro `completo==1`, rellenas `lleno>0`, EV Σpnl/Σcoste, IC90 por días con t de Student) y `driver.log`. PRECIERRE: `data/live/trades.csv`
(strategy `RESOLUTION_SNIPER_PRECIERRE`, status CLOSED). Capital: `data/live/balance_real.json` (ts 2026-10-19T06:30:16Z). Fees/rebate:
gamma-api.polymarket.com `slug=btc-updown-5m-1792391700` (GET de lectura). Harness de órdenes: `/root/polymarket-research-dev/experimento_pares_cola_15m.py`
y `pares_contabilidad.py` (no ejecutados, no leídas las credenciales). Modelo de riesgo (ruina, n necesarios) = cálculo propio con
σ=2,05 por € medido en los 3.050 rellenos DEEP_k1 de ETH/SOL/XRP, aproximación Browniana.
