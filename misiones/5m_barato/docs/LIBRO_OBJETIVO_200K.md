# Libro de cuentas del objetivo 5m barato — 200.000 €/año netos como SUMA de subestrategias

Lo mantiene `cheap5m-objetivo-200k` (o `cheap5m-risk-economics` / el chief). Solo cuenta como ingreso lo que está en el
peldaño ≥5 de `FLUJO_DE_TRABAJO.md` (micro-real, live, rampa) con su gate superado; todo lo demás va en "potencial" y
etiquetado. Toda cifra con fecha, n, IC90 por días y fuente. **EV siempre ponderado por € (Σpnl/Σcoste).**
Unidades: pUSD ($) tal como salen de los ficheros; NO se ha convertido a € (convertir restaría ~10-15 %).

## Resumen — corte 19-Oct 13:30Z (3ª pasada; 2ª = 19-Oct 06:50Z, 1ª = 17-Oct 14:10Z)

| Escenario (anual) | pUSD/año | Cómo se calcula |
|---|---|---|
| **Ingreso VALIDADO (peldaño ≥5 de la familia)** | **0** | nada ha llegado al peldaño 5; la familia solo tiene dry-run/forward |
| Conservador (lo que sigue en pie sin su mejor operación/día) | **0** | V4 sin su mejor operación −0,002; H5M primeras 5 acc +0,003 (−0,023,+0,026); R5K forward −0,292 |
| Base (15 % del optimista de V4+H35; R5K = 0) | **≈ 2 k** (antes ≈ 12 k) | retención observada de exploratorias en forward: 11 %, 28 %, ~0 % (+ R5K, 4º caso: el forward de 2 días ya no es compatible con +0,2, p=0,0007); R5K base 0 porque su punto forward es negativo con IC90 por cierre < 0 |
| Optimista NO validado (cola favorable, sin doble conteo) | **≈ 34 k** (antes ≈ 78 k) | tomador 4,9 k + H35 alts a 5 acc 9,4 k + R5K 19,7 k (BTC, EV +0,065 = el máximo compatible con el forward a p ≥ 0,01 unilateral; antes 64 k a EV +0,212) |
| Techo teórico si H35 escalara LINEALMENTE a 50 acc (no medido) | ≈ 119 k (antes ≈ 163 k) | 4,9 + 94,3 + 19,7: **aun con TODO a favor queda < 200 k** |
| **Hueco hasta 200 k** | **200.000 validado · ≈ 166 k contra el optimista · ≈ 81 k contra el techo teórico** | |

Fórmulas (anual = coste/día × EV × 365; fuentes en cada fila): tomador 2,08 ejec/día × 23,4 $ × 0,277 × 365 = 4,9 k;
H35 alts 354 $/día × 0,073 × 365 = 9,4 k (×10 = 94 k si K=50); R5K 830 $/día × 0,065 × 365 = 19,7 k (verificado con
Python 19-Oct 13:30Z: se por cierre = 0,154 del IC90 del vigía; EV máximo con P(fwd ≤ −0,292 | EV) ≥ 0,01 = +0,065).

**Qué falta, en orden (corte 19-Oct 13:30Z):**
1. **Edge**: todo es EXPLORATORY y hoy ha empeorado: el único con IC90 por días > 0 de la 2ª pasada (H5M sin BTC) es POBLACIÓN, post
   hoc, y su versión de «llegar el primero» (primeras 5 acc) es +0,003; R5K, el mayor pilar del optimista, tiene forward negativo.
2. **Capacidad (el cuello real, sigue)**: 548 €/día = coste-base diario de 11 k$ a EV +0,05, 5,5 k$ a +0,10. Lo medido: tomador 16-49 $/día;
   H35 alts 354 $/día; R5K 550-830 $/día. La única palanca de escala que queda es **H35 con K>5 (×10 = 94 k), que NO está simulado**
   (columnas x10/x20 vacías) y es lo que H45 mide.
3. **Capital**: igual que la 2ª pasada (rotación pequeña, riesgo sí). Hoy: principal 41,64 $ libres + 1,04 $ en posiciones
   (`data/live/balance_real.json` 19-Oct 13:25Z; `pusd_onchain` 50,80 → ~9 $ sin conciliar con `free_usdc`); dedicada 19,59 pUSD (memoria 17-Oct,
   NO re-verificada: la dirección completa solo está en la credencial, que no se lee). Toda rampa es decisión de Javi.

## Nota 22-Oct 15:40Z (risk-economics, fila R3 de B; fuente `experimentos/5m_barato/b_perdidas_22oct/r3_escalado/INFORME.md`)
- **R3 (B maker ETH/SOL/XRP con bid15 ≤3c + vol30 ≥26 + hora ≥4)**: peldaño 2-4 (forward shadow congelado, 1ª lectura 02-Nov); validado 0.
  Simulador E1 17-22 Oct: separa (DIF +0,253, placebo p=0,003, 5/6 días) pero política −0,041 IC90 días (−0,132,+0,049); recalibrado a B real
  (59 % de sus rellenos son en cola al precio, +0,19, que el simulador no modela) ≈ +0,07 (rango −0,19..+0,35). Capacidad 130 rellenos/día,
  136 €/día a 5 acc; K≤20 aguanta (−0,017), K=50 no (−0,066); banda 0,30-0,50 REJECTED (−0,192). **Anual: 0 / ~1,5 k / ~11 k** (K=20) + rebate ≤1,3 k;
  sustituye al «15-25 k» de `b_seleccion_adversa/INFORME.md §F` (flujo de todos los makers, no capturable). Capital: P1 a 5 acc necesita 56-73 $ para 300 rellenos
  con P(DD)≤10 % (hoy 5,12 $ ⇒ solo maquinaria/concordancia). Variante exploratoria propuesta: R3 + hora <16 UTC (2 instrumentos, 7/9 días-instrumento).

## Qué ha cambiado en la 3ª pasada (19-Oct 06:50Z → 13:30Z)

Fuentes: `experimentos/5m_barato/validacion_19oct/informe.md` (06:44Z), `h43_auditoria_datos/informe.md` (07:39Z), `v4_comprar_lo_bueno/salidas/*.txt`
(08:13-08:18Z, SIN informe.md aún), `logs/vigia_5m_barato_r5k.log` (09:31Z), `dev/informes/h47_code_review1_19oct.md` (07:36Z),
`wallets_18oct/stage1.log` (09:20Z, solo etapa 1). Solo lectura, sin cómputo pesado.

- **H43 R5K, forward del vigía congelado (09:31Z): 2 días (17-18 Oct), 130 unidades, 1.201 $, EV ponderado −0,292, IC90 por cierre (−0,546,−0,040)**;
  17-Oct −0,28, 18-Oct −0,31; sin top-20 −1,0; el IC90 YA excluye 0 por abajo. Compatibilidad (se 0,154 por cierre): P(fwd ≤ obs | EV real +0,20) = 0,0007;
  | +0,10 = 0,005; | +0,05 = 0,013; | 0 = 0,029. La reconstrucción del validador (69 u., −0,306 el 18) coincide con el vigía (−0,31).
  Estado formal: EN CURSO (2/10 días; no se retoca el gate congelado). Auditoría de datos: sin corrupción ni look-ahead; definición única (K cosechable
  T∈(60,270], completas, día de cierre) deja el in-sample 06-16 en **n=985, +0,201, IC90 días (+0,109,+0,294), 9/11 días +, sin 2 mejores días +0,135, sin top-20 +0,105**
  (el «+0,212, n=1.010» no se reproduce exacto) y el 17-Oct en −0,190 por cierre (−0,275 por fichero). La regla salió de 24 celdas (≈5 independientes: máximo esperado por azar ≈ +0,10).
  Pool in-sample+forward por coste = +0,143, pero contaminado por selección: NO se usa. Es un subconjunto BTC de H5M y el 18-Oct fue su peor día: no son confirmaciones independientes.
  **Efecto en el libro: R5K pasa de 64,2 k (optimista) a 19,7 k, base 0.**
- **V4 (validador 06:40Z + causalidad 08:18Z), sin cambios de datos: sigue 25 ejecutables / 58 señales / +0,277; sin la mejor operación −0,002; 96 % del PnL en un día.**
  Hallazgo que reorienta el trabajo: la SEÑAL existe (36/58 = 62,1 % de acierto frente a ask_t0 medio 0,422; «PnL de papel» al ask_t0 +101 € sobre 148 € = +0,685; 94,5 € de ese papel
  está en las 33 no ejecutables) pero lo ejecutable es selección adversa (ejecutables 10/25 = 40 % a precio 0,397; no ejecutables 26/33 = 78,8 %; Fisher p = 0,003). El rival nos gana siempre:
  ventaja sobre nuestro casado a L215 (reloj exchange): consumo n=16 p50 179 ms (p10-p90 69-479), cancela/recotiza n=13 p50 263 ms (179-581); 29/29 por >0 ms, 24/29 por ≥100 ms.
  Es un evento de Binance: movimiento ≥1 bp orientado que EMPIEZA antes del instante en 29,3 % de las 58 señales (13/58 = 22,4 % con ≥255 ms de antelación, IC90 (0,138,0,31)) frente a 8,0 % (7,4 %) de placebo del mismo día/moneda/orientación (n=17.400).
  Control por margen causal (137.000 filas ejecutables a L215, 06-18 Oct, `controles_margen.txt`): margen en [−0,1,0,025) → EV −0,20/−0,31/−0,28 con IC90 por cierre < 0 (acierto = precio − 3 a −13 pp);
  margen ≥ 0,025 solo 14 filas/14 cierres (EV +0,21/+0,53, IC90 cruza 0): la condición de V4 casi no se da fuera de los eventos, y en 13-18 Oct no hay ninguna señal ≥0,025 que gane de forma robusta.
  Lectura: desde este VPS (FOK 213 ms, taker delay 145 ms) la señal NO es capturable como tomador; el techo ≈5 k$/año de la rama tomador se confirma por un camino distinto (la ventaja es 150-300 ms y es estructural).
  Latencia → EV: L150 +0,415 (31) → L215 +0,277 (25) → L250 +0,062 (22): cae a ≈0 con +35 ms.
- **H5M población, ponderado por € (validador, 10 días, 20.078 u.)**: +0,040, IC90 días (−0,012,+0,087); por cierre (−0,012,+0,095). **Primeras 5 acciones +0,003, IC90 días (−0,023,+0,026)**;
  por moneda ponderado: ETH +0,123, BNB +0,091, SOL +0,055, BTC +0,034, DOGE −0,025, XRP −0,069. 18-Oct −0,175 (bootstrap por cierre P(dif ≥0) = 0,0003) sin causa de régimen.
  Regla de parada propuesta por el validador: 19-21 Oct juntos con media-vigía ≤ +0,05 o ponderado ≤ 0 con IC90 por cierre que no excluye 0 → ruptura desde el 18-Oct. El «CONFIRMADA» del vigía (6/6) es la media de cocientes.
  (La cifra de la 2ª pasada «IC90 (−0,025,+0,095)» era el IC de la media de días del EV diario; el de Σpnl/Σcoste con bootstrap por días es (−0,012,+0,087). Ambos cruzan 0.)
- **H47 (micro-órdenes)**: código `experimento_maker_h47.py` + tests en dev; `/code-review` medium #1 (07:36Z) dio 10 hallazgos SIN aplicar (los 4 primeros sesgan justo la tasa de relleno y el acuerdo sim↔real:
  asentar 0,35 s frente a 1,5 s del harness, `relleno_real` solo desde `c.estado`, gemelo CONS con `t_post = t0`, bucle infinito en 'asentando'). Pendiente: aplicar 1-10 + mutación → 2ª review → OK final de Javi.
  Aviso del implementador: repegado 35-65 órdenes/puja → B ≈ 8-15 k órdenes, riesgo 429. Javi dio (memoria 19-Oct) OK a A+B con suelo 12 pUSD, y exige OK final antes de enviar. Aún 0 órdenes reales.
- **Wallets 18-Oct (quién tomó contra los makers)**: SOLO etapa 1 hecha (fills parquet 09-18 Oct, tx 14-18; `stage1.log` 09:20Z). `a1_tomadores`…`a4_estado` escritos pero sin salida: sin informe.
  El ángulo 7 (quién gana y cómo) sigue sin cifra nueva; es lo que explicaría si el 17-18 Oct fue un cambio de tomadores.
- **Colocación (modelo)**: sin salida nueva. **Dataset de colocación 17-18 Oct: NO existe** (base_*.csv.gz llega a 16-Oct) mientras los `maker_ms_2026-10-17/18_*.csv.gz` crudos siguen en disco
  (retención ≈5 d: los de 14-Oct aún están; los de 17-Oct caerán hacia 22-Oct). H45 y el OOS de 17-18 Oct dependen de ellos: **ventana de datos que caduca**.
- No hay datos nuevos de V2/V3/V5/V6/V7/FV v4/PRECIERRE/15m reposición desde la 2ª pasada (los crons de 04:35-06:13Z ya estaban leídos); no se recalculan.

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
| **H43 R5K** (maker tras 5.000 acc, **solo BTC**: ninguna otra moneda llega a 5.000) | 2 · EXPLORATORY, **forward en contra** (24 celdas miradas, 11 días) | definición única 06-16 Oct: +0,201 días (+0,109,+0,294), sin 2 mejores días +0,135, sin top-20 +0,105; **forward 17-18 Oct (vigía 09:31Z): −0,292, IC90 cierre (−0,546,−0,040)** | 985 unid./11 d + 130 unid./2 d | 92 unid./día × 9 $ (K=50) = 830 $/día; residual de volumen tras cruzar 5.000: mediana 1.191 acc (p10 134, p90 4.977; 17-Oct, 61 unid.) | 0 / **0** / **19,7 k** (EV +0,065 = cota forward al 1 %; antes 64,2 k) | BTC maker (excluye H35 alts); subconjunto BTC de H5M | forward del vigía + regla de parada propuesta (ver pruebas); H46 offline; NO micro-órdenes brazo 2 mientras el forward acumulado sea < +0,05 |
| **H35 DEEP_PEG alts** (ETH k2, SOL k1, XRP k1; elegidos en DESC) | 2 · EXPLORATORY, simulador SIN calibrar (NO_REPRODUCE→criterio v2 post hoc); cola desconocida en ~75 % de pujas | ETH+SOL+XRP k1: DESC +0,076 (−0,128,+0,199) 4/6 d, sin 2 mejores −0,003; **OOS 14-16 +0,067** (−0,121,+0,269) 2/3 d, sin 2 mejores −0,046; 9 días +0,073 (−0,056,+0,153) 6/9, sin 2 mejores +0,030; JOIN mismas monedas OOS +0,022 | 3.050 rellenos / 9 d (OOS 1.088 / 3 d); por moneda OOS: ETH +0,046, SOL +0,066, **XRP +0,121 (+0,020,+0,229) 3/3** | 339 rellenos/día, 354 $/día a 5 acc (29,6 % de las pujas se rellenan); K>5 NO simulado (columnas x10/x20 vacías) | 0 / ≈ 1,4 k / 9,4 k (K=5); 94 k si K=50 (no medido; H45) | maker de banda (lo contiene), H39 | micro-órdenes brazo 1 (calibrar cola) + H45 escala |
| **H35 BTC** (DEEP) | REJECTED en sim para BTC | k1 DESC −0,068 (−0,137,−0,007) 1/6 d; OOS −0,011 | 1.703 + 1.069 rellenos | — | 0 | — | fuera de la prueba real |
| **Maker de banda** (unirse al bid, 5 acc, JOIN) | 2 · línea base | JOIN sim todas las monedas DESC −0,034, OOS +0,022 (+0,032 con rebate); población ponderada 10 d +0,040 (IC90 cruza 0); nuestras primeras 5 acc ≈ +0,007 (10-13 Oct, auditoría 17-Oct) | ~2.000 unid./día | ~2.200 $/día a 5 acc | 0 / 0 / ≈ 0 (primeras 5 acc +0,003, IC90 días (−0,023,+0,026), 10 d; ponderado población +0,040 (−0,012,+0,087)) | contiene a H35/R5K | es la línea base a batir, no se suma |
| **Modelo de colocación** | 1 · dataset COMPLETE 9/9, modelo sin correr (lo corre otro agente hoy tras 09:15Z) | — | 9 días (DESC 05-10, OOS 14-16) | — | — | todas las maker | gate ≥ +0,05 sobre mejor k de la línea base por moneda, IC90 días y cierre > 0, placebo e inversión peores |
| **H39 MM-REPOSO** | 1 · PENDING, bloqueada por calibración | ganadoras on-chain +1,1/+1,6 %/€ (2 wallets, 7/7 d OOS) | — | — | — | maker | tras calibrar la cola |
| **V4 / V2 / V3 / V5 / V6 / V7** (UN solo canal tomador: no se suman) | 4 · FORWARD congelado | V4 OOS +0,277 (−0,356,+1,046), sin top-1 −0,002; ejecutables 40 % vs no ejecutables 78,8 % (Fisher p=0,003); rival 150-300 ms por delante; V7 n=1; V6 n=3 | 25 ejec./12 d (V4) | 2,08 ejec./día; nocional al ask nivel 1 p50 13,6 $, p90 234 $; coste/día 16 $ (tope 10 $/señal), 49 $ (tope 50 $) | 0 / ≈ 0,7 k / **4,9 k** (15 k sin tope por señal) | mismo evento | seguir forward; G1 n≥40 ≈ 26-28 Oct (G4/G6/G7 fallarán salvo cambio); «28-37 k» de V7 y «30 k» de V6 son de descubrimiento y NO cuentan |
| **PRECIERRE** (referencia, fuera de la familia) | 6 · LIVE 2 € | +0,133 (33 órdenes, 17 aciertos, IC90 días cruza 0) | 33 / 19 d con orden | ~1,3 órdenes/día | ~0,12 k a 2 € | — | rampa 5 € solo con ≥40 órdenes post-arreglo (hoy 2) |
| **H44-H47** (registradas PENDING en REGISTRO 19-Oct) | 0 · PENDING; H47 en dev con code-review #1 sin aplicar; H44 forward desde 19-Oct | — | — | — | — | — | ver «3 pruebas» 3ª pasada |

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

## Las 3 pruebas de mayor valor — actualizadas en la 3ª pasada (por € de capacidad en juego)

Criterio: capacidad anual que la prueba puede confirmar o matar ÷ coste. Con el techo ahora en ≈119 k, de los cuales 94 k son H35 a K=50 (no medido),
**la prueba que decide si el hilo puede acercarse a 100 k es la de escala, y es gratis y caduca.**

1. **H45 · H35-ESCALA + OOS 17-18 Oct (offline, ≈0 €, URGENTE)**. Construir el dataset de colocación de 17 y 18 Oct (no existe: `m5_maker_colocacion/base_*` llega a 16-Oct)
   con los `maker_ms_2026-10-17/18_*.csv.gz` crudos antes de que roten (≈22-Oct), con K = 5/25/50 acc en el simulador (hoy las columnas x10/x20 están vacías).
   Gate (ya en REGISTRO H45): EV(25) ≥ EV(5) − 0,03 y rellenos×coste ≥ 4× el de 5 acc; EV(25) ≤ 0 ⇒ capacidad H35 ≈ 9 k y el hilo maker alt queda cerrado como camino a 200 k.
   Valor: decide 9 k frente a ≈94 k (el 79 % del techo). Lo que NO resuelve: simulador sin calibrar (eso es H47). 18-Oct entra como día de estrés (H5M −0,175).
   Coste/quién: execution-engineer, 1 solo trabajo pesado, turno 00-06Z, `nice -n 19 ionice -c3`, `ulimit -v` 2 GB, MemAvailable > 2,5 GB y load < 16 (hoy load ≈10, MemAvail 2,7 GB: de día no).
2. **H47 · SIM-REAL, escalón A y luego B (≤1 $ y luego EV≈0 ± ~17 $)**. Bloqueos concretos: aplicar los 10 hallazgos de la review #1 (los 1-4 sesgan la tasa de relleno y el acuerdo sim↔real), tests de mutación, review #2, OK final de Javi.
   Gate fijado (±8 pp tasa, acuerdo ≥0,70 en ambas direcciones, markout ±0,03). Expectativa honesta: el maker pequeño de población vale ≈ +0,003 en las primeras 5 acc, así que H47 validará o invalidará la
   MAQUINARIA y el simulador, no creará EV; si el simulador falla, el 9,4 k de H35 y el 94 k pasan a «solo dinero real». Añadir al diseño: contar cuántas pujas B se rellenan en los ~2 s previos a un movimiento adverso (selección adversa real)
   y guardar el rebate cobrado por relleno (única forma de verificar el 0,2). Quién: execution-engineer + chief + Javi (presupuesto de pérdida explícito, N fijo = 230 pujas, parada solo por suelo 12 pUSD).
3. **Parada de atención de R5K + H46 offline (≈0 €)**. (a) Regla adicional pre-registrada (NO cambia el gate formal del vigía): si al 24-Oct (≥7 días de forward) el EV ponderado acumulado tiene IC90 por cierre con límite superior < +0,05,
   R5K pasa a REJECTED como camino a escala y se retira el brazo 2 de las micro-órdenes; si el acumulado sube a ≥ +0,05 con ≥ 400 unidades, vuelve al libro. Hoy: 130 u., límite superior −0,040. (b) H46 (R5K normalizado por moneda en ETH/SOL/XRP) como
   lectura de solo lectura sobre `m5_onchain` con el cuantil fijado en DESC 05-10: es la variante que la directiva de Javi pide ante el negativo y solo tiene sentido si la dosis-respuesta existe fuera de BTC. Gate de H46 intacto (≥40 u., ≥10 días, EV ≥ +0,05, IC90 cierre > 0, sin top-20 > 0).
   (c) Terminar la etapa 2 de wallets 18-Oct (a1-a4, 0 €): ¿cambió el perfil de tomadores el 17-18 Oct? Si sí, es régimen y no azar, y afecta a R5K, H5M y H35 a la vez.

Quedan como seguimiento gratuito (no pruebas nuevas): H44 (H5M ex-BTC, ≈29-Oct), regla de ruptura de H5M 19-21 Oct (media-vigía ≤ +0,05 o ponderado ≤ 0), V4 G1 (≈26-28 Oct; se espera que NO pase G4/G6/G7).
Colocación (modelo) sigue sin correr; su salida decide t_q y k de las pujas de B pero no sustituye a H47.

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
- **H48 · R5K-PARADA (regla de atención, 3ª pasada; no toca el vigía)**. Con el forward del vigía H43 congelado: al 24-Oct (≥7 días) si el IC90 por cierre del EV ponderado acumulado tiene límite superior < +0,05 → REJECTED como camino a escala y fuera del brazo 2 de micro-órdenes;
  si ≥ 400 unidades y EV ≥ +0,05 con IC90 cierre > 0 → vuelve al libro. Hoy 130 u., (−0,546,−0,040). Coste 0.
- **H49 · V4-GUARDA (solo si el chief quiere aprovechar el hallazgo del 19-Oct)**. La señal de V4 (62 % de acierto frente a ask 0,42) ES información; el rival la cobra a 150-300 ms. Variante con mecanismo distinto, no tomador: usar el evento V4 (bid15(s) − ask5(s) − fee ≥ 0,05) como DISPARADOR DE CANCELACIÓN/REPEGADO
  de las pujas H35 abiertas de la misma moneda (aprox. H34) y medir en el simulador el EV de las pujas vivas con y sin evento en los ~2 s previos al relleno (prueba justa: apartar solo lo que llega antes del relleno; trampa del 07-Oct de simuladores que cancelan «para siempre»). Gate: EV(sin evento) − EV(con evento) ≥ +0,05 con IC90 cierre > 0, ≥ 40 rellenos con evento. Coste: offline sobre el dataset de H45.
- (Nota, no es hipótesis de la familia) **Universo**: repetir la regla congelada de 15m reposición en ETH/SOL/XRP como vista de
  población (BTC 15m forward −0,006, pero en 5m las alts rinden más que BTC). Solo si el chief quiere ampliar al 15m.

## Se puede descartar ya (como camino a 200 k)

- **R5K como pilar de escala (64 k)**: forward −0,292 (IC90 cierre (−0,546,−0,040), 130 u.) y regla elegida entre 24 celdas; solo sobrevive como cola ≤ 19,7 k hasta que el forward acumulado diga otra cosa. **No gastar micro-órdenes del brazo 2.**
- **«Comprar lo bueno» de V4 como tomador desde este VPS**: el rival llega 150-300 ms antes (29/29) porque el movimiento de Binance empieza antes del instante; no hay forma de acortar los 213 ms del FOK ni de cancelar durante el taker delay (cerrado 14-Oct) ni VPS cerca (descartado por Javi). Se mantiene solo la señal como guarda del maker (H34).
- **El «CONFIRMADA» de H5M como evidencia de ventaja de un maker pequeño** (media de cocientes): ponderado +0,040 con IC que cruza 0, primeras 5 acc +0,003.

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
6. **EV de la cola favorable dependiente de la cola equivocada**: el 64 k de R5K salía de EV +0,212 (24 celdas, 11 días) sin acotar con el forward; con 2 días ya es incompatible con +0,2 (p=0,0007). Acotar siempre el escenario optimista con la verosimilitud del forward disponible (EV máximo con P ≥ 0,01), no con el punto exploratorio.
7. **Señal real ≠ señal capturable**: V4 tiene 62 % de acierto frente a 42 % de precio en las 58 señales y aun así el ejecutable acierta 40 % = precio (Fisher p=0,003): cobrar la señal exige llegar antes que un rival que gana por 150-300 ms. Medir siempre capturado/papel (aquí 30 % de las ganadoras) y a quién se cede el resto.
8. **Dos ICs distintos para «ponderado por € a 10 días»** (media de los EV diarios con t de Student vs bootstrap por días de Σpnl/Σcoste): (−0,025,+0,095) frente a (−0,012,+0,087). Decir cuál; ninguno excluye 0.

## Fuentes

**3ª pasada (19-Oct 13:15-13:40Z, solo lectura, sin cómputo pesado; cuentas en Python ligero):** `experimentos/5m_barato/validacion_19oct/informe.md`; `h43_auditoria_datos/informe.md` (+ `a7_cierre_final.py`);
`v4_comprar_lo_bueno/salidas/{final_tablas,final2,segundo_evento,placebo_bin,controles_margen,margen_pre,chk_onchain,analiza3}.txt` (sin informe.md);
`logs/vigia_5m_barato_r5k.log` (09:31Z), `logs/vigia_5m_barato_maker_forward.log`, `logs/vigia_5m_barato_forward.log`; `/root/polymarket-research-dev/informes/h47_code_review1_19oct.md`;
`experimentos/5m_barato/wallets_18oct/stage1.log`; `datalogs/maker_ms_2026-10-1*.csv.gz` (ls: existen 14-19 Oct) y `datalogs/m5_maker_colocacion/` (ls: base hasta 16-Oct);
`data/live/balance_real.json` (ts 2026-10-19T13:25:09Z). se/p de R5K: Python propio, IC90 del vigía con normal (z=1,645).

**2ª pasada (todas leídas/recalculadas el 19-Oct 06:10-06:55Z, solo lectura, `ulimit -v 1500000`):**

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
