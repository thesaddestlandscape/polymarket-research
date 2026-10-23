# PREREG Q-TECHO (techo de precio por orden para B) - escrito 23-Oct-2026 ~09:50Z, ANTES de calcular ningun estadistico de q/regla
Rol: investigacion, solo lectura (B, ejecutores, crons, config intactos; sin ordenes; sin commits). Conocimiento previo declarado (leido en informes, no recalculado): R2/R3/R1 se eligieron con la poblacion 17-21 Oct; logit 17 rasgos fit 09-15 / eval 16-21 dio AUC 0,604 (casi todo precio); E1/S1/P-REAL/X-SALIDA/W2 como en sus informes. No he mirado EV por tramo, por rasgo ni por moneda de las unidades 09-21 en esta ola.

## 1. Datos y unidad
- Poblacion U = unidades de OTROS makers ETH/SOL/XRP 5m, 09..21-Oct (13 dias; `b_seleccion_adversa/datos/units/units_D.pkl`; pc en [0,10;0,30], T en (60;300] s, primeras 5 acc por (maker,mercado,lado); el 21 parcial). Es la poblacion CONDICIONADA A RELLENO (precio de relleno real del maker, desenlace oficial `gana`; sin oficial = missing, se cuenta y se excluye). pnl = sh*gana - c; maker fee 0, rebate NO sumado. EV siempre ponderado por EUR (sum pnl / sum c).
- Rasgos en t_obs = ts - 4 s (regla de build_units; causal). Tres conjuntos: **FWD** (deployable y comprobable forward con `sa_r1/units2_D`): pc, T, moneda, hora UTC, vol30, bb, ba, bs, as_ (solo para imbalance; opcional), spread, depth_ticks=(bb-pc)/0,01, b15, a15, lvl15=b15-pc, gap15=b15-bb, d15_30, dbb30, vol30ws, + Binance: r60f (retorno signado por lado de Binance mid bookTicker t_obs vs t_obs-60 s, bps; + = a favor del lado), rpre_s (rpre de `ventanas_bookticker` signado por lado), CON = rpre_s >= +7,7. **FULL** = FWD + gap_last, dp5, dp30, dp60, hi60, rng60, d_open, vol_all, flow60, fv_gap, z, sig_bps_s, b10 (solo diagnostico de techo de informacion: no existen en el forward). Los rasgos de libro (bb..vol30ws) de 17-21 salen de `ms_units.pkl`; los de 09-16 se extraen del registro `m5_registro`/`m15_registro` con el mismo asof por recepcion (QA: reextraer 17-18 y comparar con ms_units, tolerancia declarada en el informe). Excluidos por no observables o identidad: taker, tk_score, nf, inf120.
- Binance: `binance_bookticker_D.csv` (recepcion). Faltante -> NaN (HGB lo maneja; LOGIT imputa mediana + indicador).

## 2. Particion (fija)
- DESCUBRIMIENTO = 09..16-Oct. Seleccion interna walk-forward: dias de test 13,14,15,16, entrenando con 09..d-1.
- TEST = 17..21-Oct, walk-forward diario (entrena con todos los dias < d, incluidos los de TEST ya pasados; refit diario, hiperparametros congelados). TEST se evalua UNA vez con lo congelado en DESC. Aviso: el agregado 17-21 ya lo vieron otros informes (R2/R3 elegidas ahi: favorece a las lineas base en TEST; 09-16 es OOS genuino para R2/R3 y se reporta aparte).
- Forward (gate): dias >= 23-Oct con `sa_r1/units2_D` + Binance; ver seccion 7.

## 3. Modelos de q (P(ganar | relleno, x)), uno por moneda
- MAP: tasa de acierto por (moneda x tramo de pc 0,05) con encogimiento a la media de la moneda (k=50). Es el "mapa q->precio por tramo".
- LOGIT: regresion logistica L2 (rasgos estandarizados incl. logit(pc)), C elegido en {0,01; 0,1; 1} por log-loss del walk-forward de DESC.
- HGB: HistGradientBoosting (max_depth 3, max_iter 150, lr 0,05, l2 1, min_samples_leaf 200), semilla 20261024.
- LOGIT y HGB en FWD (candidatos) y FULL (diagnostico). Calibracion: isotonica sobre predicciones fuera de muestra de 3 bloques contiguos de dias del entrenamiento.
- Benchmarks de prediccion: precio pc (q=pc), mid5 = (bb+ba)/2 en t_obs, MAP, y los indicadores R2/R3 (media de acierto por bandera ajustada en entrenamiento).

## 4. Regla (techo por orden) y seleccion
- Skip de la unidad si pc > q_cons - f - m, con q_cons = q calibrado, f = 0 (maker, sin fee; rebate no contado), m en {0; 0,01; 0,02; 0,03; 0,04; 0,06}.
- Seleccion en DESC: entre {MAP, LOGIT-FWD, HGB-FWD} x m se elige el de mayor dPnL_total (= -PnL de las saltadas) sujeto a retener >= 25 % del EUR y EV retenido > EV sin regla; si ninguno cumple, el resultado es "sin candidata" y se informa igual en TEST como descriptivo. Se congela (familia, m, C) y se pasa a TEST sin tocar.
- Reglas Binance (hipotesis de W2/R-TEND): **R_r60**: saltar si r60f <= p20 de r60f por moneda en DESC (umbral congelado); **R0**: saltar si CON (rpre_s >= 7,7 bps). Lineas base descriptivas: R2 (retener si b15 existe, no cruzado y lvl15 <= 0,03), R3 = R2 & vol30ws >= 26 & hora >= 4 (ambas fail-closed si falta dato).
- Efecto de sustitucion NO modelado (la unidad es el relleno; E1/R3: la politica real recupera ~la mitad menos): todo dPnL es COTA SUPERIOR; se informa tambien con haircut 50 %.

## 5. Pruebas y gates (TEST 17-21; una sola pasada)
Hipotesis contrastadas en TEST (Bonferroni x3 = 0,0167): H-Q (regla elegida), H-r60, H-MAP (si distinta de H-Q). R0, R2, R3 solo descriptivas.
G-Q1 (q bate al mercado): log-loss y Brier fuera de muestra del q elegido < los del benchmark mid5 (subconjunto con libro) y < MAP y < indicador R3, diferencia pareada con IC90 por cierre (bootstrap por `fin`, 2.000) con limite superior < 0.
G-Q2 (regla): dPnL_total > 0 con IC90 por cierre inferior > 0; p de permutacion POR CIERRE < 0,0167 (banderas aleatorias a nivel (cierre,moneda,tramo de pc) con la tasa de skip del estrato dia x moneda x tramo; 2.000); dPnL > 0 en >= 60 % de los dias; sin los 2 mejores dias > 0; EV/EUR retenido > EV sin regla; inversion (saltar la misma fraccion por la cola contraria del edge q-pc) con dPnL <= 0; retencion >= 25 % del EUR.
G-Q3 (bate a R0/R3): dPnL(regla) - dPnL(R0) con IC90 por cierre > 0; frente a R3 se compara a retencion igualada con la regla q (top por edge q-pc hasta la misma retencion que R3) y como incremento DENTRO de R3 (retenidas por R3: dPnL de q-cap adicional, IC por cierre).
Si falla G-Q1 pero pasa G-Q2/G-Q3 se etiqueta "regla sin q" (no mejora la prediccion; solo un filtro). Todo se etiqueta EXPLORATORY: 13 dias, un regimen, relleno de OTROS makers, sustitucion no modelada.
Desagregados siempre: por moneda, por dia, por tramo de pc, ETH/SOL/XRP; sin los 2 mejores dias; precio = precio de relleno real del maker (NO ask) en la poblacion; ask real SOLO en el bloque P-REAL.

## 6. Bloques descriptivos adicionales
- P-REAL map: `datalogs/preal/ask_t0_D` (05-21 Oct, 6 monedas) con desenlace oficial de `desenl_cache.json`: acierto vs ask a T=180 s+250 ms por tramo 0,05 y moneda; EV al ask con fee 0,07; descomposicion con la poblacion: AS(tramo) = acierto(relleno maker a pc) - acierto(ask no condicionado en el mismo tramo). Marcado "ask real" vs "precio de relleno maker".
- B real (`salida/datos/unidades_b.csv`, 201 posiciones 20-23 Oct): aplicar SOLO las reglas que no necesitan rasgos de libro (MAP entrenado en las 13 dias, R_r60, R0) con coin/lado/pc/instante; descriptivo (n bajo).
- Hueco a 200 kEUR: con dEV/EUR medido y el nocional de X-SALIDA (B 68 $/dia; techo R3 130 fills x 2,44 $ = 317 $/dia; pool 5.163 $/dia), fraccion = dEV x nocional anual / 200.000. Sin extrapolar capacidad a partir de una muestra descubrimiento.

## 7. Candidata y forward
Si G-Q1..3 pasan en TEST: candidata a forward, no a B. Gate forward (sin cambios de umbral/modelo; coeficientes congelados en `datos/modelo_congelado.json` con sha): >= 10 dias >= 23-Oct con `units2_D` y Binance, >= 600 unidades saltadas, dPnL con IC90 por cierre inferior > 0, permutacion por cierre p < 0,0167, >= 60 % de dias dPnL > 0, sin los 2 mejores dias > 0, retencion >= 25 %. Reloj: mismo que R-TEND/R3: 10 dias completos = 1-Nov, evaluable 2-Nov. Si no pasa G-Q1..3 en TEST: no hay candidata; queda en pasivo (mismo script, sin coste) con la regla congelada y fecha 2-Nov.
Multiplicidad declarada: 3 familias x 6 margenes en DESC (seleccion interna), 3 hipotesis en TEST; C de LOGIT en 3 valores.
