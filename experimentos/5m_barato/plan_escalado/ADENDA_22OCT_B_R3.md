# ADENDA 22-Oct-2026 (~15:50Z) al PLAN_MAESTRO: filas H35/H47 alts rehechas con la realidad de B y R3 (risk-economics)
Estado: **EXPLORATORY**. Validado: 0 €. Solo análisis. No he tocado B, el supervisor, los procesos, los crons, la config live ni `PLAN_MAESTRO.md` (sha 74656eb4db4050c3).
Números: `adenda_22oct_numeros.py` → `adenda_22oct_salida.txt` (misma carpeta). Ejecutado con nice 19, ionice -c3 y ulimit -v 3 GB, en menos de 20 s. $ ≈ € sin convertir. EV ponderado por € (Σpnl/Σcoste). Maker sin comisión y sin rebate salvo donde se indica.

## 0. Resumen
1. **B real se ha deteriorado.** Con datos frescos (185 posiciones liquidadas, 15:46Z) da **EV −0,025** (IC90 por cierre −0,29..+0,27) y −5,10 $. El +0,008 de las 15:06Z era una foto de 179 posiciones. Por días: +0,07 / +0,17 / −0,26, y sin los 2 mejores días queda en −0,26. Lejos del gate de +0,05.
2. **n efectivo, con el cierre como unidad.**
   - B: 72-76 rellenos/día se quedan en **~57-60 entradas independientes/día** (ICC intra-cierre 0,26, IC90 0,04-0,47; DEFF 1,28) en ~7 h activas. Con ρ=1 el suelo es de 40 cierres/día.
   - R3 a capacidad del simulador: 130 rellenos/día se quedan en **99/día** (IC90 96-103; ICC 0,56; DEFF 1,32).
   - Al ritmo real que se puede capturar, R3 está entre **~22/día** (shadow cons_r) y **~40/día** (ritmo de B extrapolado a 20 h).
3. **El PLAN_MAESTRO sobrestimaba la velocidad ×2.** El crecimiento de Kelly es g = n·EV²/(**2**σ²), no n·EV²/σ². Con ½ Kelly es 3/8·n·EV²/σ². Todos los «días» de la ADENDA 20-Oct se duplican con Kelly y se multiplican por 2,7 con ½ Kelly (§3).
4. **Desde 5 $ no hay autofinanciación posible.** El mínimo del exchange es de 5 acc (1,05 $), así que una tanda de 5 $ apuesta el 21 % por relleno, mientras que el Kelly está en el 0,6-2,2 %: entre 10 y 35 veces Kelly. El log-crecimiento por relleno sale negativo en todos los escenarios con EV ≤ +0,30 (−0,05 a −0,07). Es la misma conclusión de `tandas` por otra vía: P(500 pujas) = 10-22 %.
   - Capital para arrancar al mínimo con EV +0,07: **~75 $ (Kelly) / ~150 $ (½ Kelly)**.
5. **Con capital, R3 llegaría pronto a su techo, pero el techo es pequeño.** Si el EV real fuera +0,07, R3 pasaría de 75 $ a su techo de profundidad (K=20) en 13-44 días. Ese techo vale **2,4-6,1 k€/año** (base) y **10,8 k€/año** (optimista).
   - El stake para 200 k sería de 80-207 $ por relleno, entre 33 y 85 veces lo que cabe en el libro.
   - B/alts no pasa de ≈5 % de los 200 k. **El hueco de ≥189 k no lo cierra el maker de alts.**

## 1. n efectivo de entradas independientes por día (pregunta 1)
Fórmula: n_eff = Σ_cierres m/(1+(m−1)·ICC), con el ICC de ANOVA sobre el acierto dentro del cierre. El IC90 sale de bootstrap de cierres.

| Fuente | Rellenos/día | Cierres/día | ICC (IC90) | **n_eff/día (IC90)** | DEFF | Nota |
|---|---|---|---|---|---|---|
| B real, 21-Oct completo | 72 | 40 | 0,26 (0,04-0,47) | **56,5** (50-69 según ICC) | 1,28 | ~7 h activas. Con ρ=1, 40 |
| B real, 22-Oct completo | 76 | 41 | ídem | **59,5** (52-73) | | día bajista: B compró Up |
| B real, R3 verdadero (37 rellenos) | 10-16 | 8-10 | — | ~8-13 | ~1,2 | a ~7 h/día; extrapolado a 20 h (hora ≥4): ~49 rellenos, ~40 n_eff |
| Simulador BASE 17-21 (capacidad) | 560 | 267 | 0,48 (0,43-0,53) | 353 (343-366) | 1,58 | entre días: var observada / var iid = 1,19 |
| **Simulador R3 17-21 (capacidad)** | 130 | 89 | 0,56 (0,44-0,68) | **99 (96-103)** | 1,32 | entre días: 0,59, sin sobredispersión visible (5 días, estimación débil) |
| Shadow R3 cons_r 22-Oct (parcial) | ~26 | — | — | ~22 (con DEFF 1,2) | — | `r3_escalado` §2.3; no es un día válido |

- **Lectura.** La correlación dentro del cierre es real: 52 de los 58 cierres con varias posiciones en B van del mismo lado. Pero recorta el n un 22-32 %, no lo reduce a «una apuesta por cierre».
- Lo que sí puede comprimir más el n es la **dirección del día** (el 22-Oct, B compró el lado barato contra la tendencia). Con 3-5 días no se puede medir bien: el simulador BASE da 1,19× la varianza iid entre días.
- La regla prudente para los gates sigue siendo **IC90 por días y por cierre**.

## 2. Filas H35/H47 alts del plan, rehechas (pregunta 2)
Supuestos de todas las filas:
- σ² por € = (1−p)/p = 3,81 (p = 0,208, el de B). Stake mínimo 1,05 $.
- Kelly por relleno: f* = EV/(σ²·DEFF).
- Techo de profundidad K=20: coste medio 2,44 $/relleno y deterioro del EV −0,017 (`r3_escalado` §4.1; K=50 rompe, −0,066).
- €/año en el techo = rellenos/día × 2,44 × (EV − 0,017) × 365.

| Escenario | EV | Rell./día · n_eff | Kelly/relleno | **Capital para el mínimo (Kelly / ½K)** | g a 5 $ (por relleno) | g Kelly / ½K por día | Días hasta el techo K20 desde el capital mínimo (K / ½K) | Días 5 $→techo si no hubiera mínimo | **€/año en el techo** | Stake para 200 k ($/relleno) | ¿Cabe? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B actual, pesimista (sim BASE) | −0,18 | 73 · 57 | 0 | ∞ | −0,095 | 0 | nunca | nunca | 0 | — | — |
| **B actual, base (real fresco)** | **−0,025** | 73 · 57 | 0 | ∞ | −0,069 | 0 | nunca | nunca | **0** | — | — |
| B actual + rebate (+0,011, 0 $ cobrados) | −0,014 | 73 · 57 | 0 | ∞ | −0,067 | 0 | nunca | nunca | 0 | — | — |
| B actual, optimista (= gate) | +0,05 | 73 · 57 | 1,03 % | 102 / 203 $ | −0,056 | 1,9 / 1,4 % | 45 / 60 | 204 / 321 | 2,1 k | 227 | NO, ×93 |
| B 24 h a capacidad del simulador, optimista | +0,05 | 560 · 354 | 0,83 % | 126 / 253 $ | −0,056 | 11,6 / 8,7 % | 7 / 10 | 35 / 55 | 16,4 k | 30 | NO, ×12 |
| R3 pesimista (política sim) | −0,041 | 26 · 22 | 0 | ∞ | −0,071 | 0 | nunca | nunca | 0 | — | — |
| R3 base con retención histórica | +0,03 | 50 · 40 | 0,63 % | 167 / 333 $ | −0,059 | 0,47 / 0,35 % | 178 / 238 | 920 / 1.422 | 0,6 k | 843 | NO, ×346 |
| **R3 base recalibrado** | **+0,07** | 50 · 40 | 1,47 % | **71 / 143 $** | −0,052 | 2,6 / 1,9 % | **33 / 44** | 136 / 217 | **2,4 k** | 207 | NO, ×85 |
| R3 base recalibrado, capacidad completa | +0,07 | 130 · 98 | 1,39 % | 75 / 151 $ | −0,052 | 6,3 / 4,8 % | 13 / 18 | 56 / 89 | **6,1 k** | 80 | NO, ×33 |
| **R3 optimista**, capacidad completa | +0,11 | 130 · 98 | 2,19 % | 48 / 96 $ | −0,046 | 15,7 / 11,7 % | 5 / 7 | 20 / 32 | **10,8 k** | 45 | NO, ×19 |
| (cota alta del IC, no es un escenario) | +0,35 | 130 · 98 | 6,96 % | 15 / 30 $ | −0,005 | (artefacto de la aproximación) | ~1 | ~1-2 | 38,5 k | 13 | NO, ×5 |

Cómo leer la tabla:
- **Tanda ≠ Kelly.** La tanda de 5 $ es una apuesta del 21 % por relleno. Con cualquier EV realista eso es un sobre-apalancamiento con crecimiento negativo. La tanda solo prueba la maquinaria (`r3_escalado` §6, `tandas` §3).
- **«Capital para el mínimo»** es el bankroll en el que 1,05 $ = f*·W. Es la cifra comparable a los 56-73 $ que pide `r3_escalado` para P(DD) ≤ 10 % en 300 rellenos. Hoy la wallet dedicada tiene **14,34 pUSD** on-chain (15:45Z, `contabilidad_wallet_dedicada/INFORME.md`) con suelo duro de 12.
- **Con EV ≤ 0 no hay escalado**, ni con Kelly ni con ninguna rampa. Ese es hoy el caso de B tal como opera (−0,025).
- **El cuello de botella no es la velocidad sino el techo.** Con EV +0,07 real y capital mínimo aportado, R3 llega a su techo en 2-6 semanas. Desde ahí no crece: el libro no absorbe más de K≈20 sin empeorar.

## 3. Corrección de la fórmula del PLAN_MAESTRO (ADENDA 20-Oct)
- Con log-utilidad, f* = μ/σ² y g* = μ²/(2σ²) por apuesta. El plan usaba g = n·EV²/σ², que es el doble.
- Con ½ Kelly, g = 3/8·n·EV²/σ². El plan ponía ½ Kelly = g/2 sobre la cifra ya inflada, así que subestimaba los días por 4/3.

| n/día | EV | Stake final | Plan: días con Kelly | **Correcto: Kelly** | **Correcto: ½ Kelly** |
|---|---|---|---|---|---|
| 2,8 | 0,08 | 2.446 € | 1.666 | 3.332 | 4.443 |
| 10 | 0,08 | 685 € | 383 | 766 | 1.021 |
| 20 | 0,08 | 342 € | 169 | 338 | 450 |
| 50 | 0,08 | 137 € | 55 | **111** | **148** |
| 50 | 0,04 | 274 € | 258 | 517 | 689 |

- Además, el n de esas filas debe ser el **n_eff** de §1, no el de rellenos. La fórmula del stake final (200.000/(EV·365·n)) sí usa los rellenos, porque el € se cobra por relleno. El crecimiento y el riesgo usan n_eff.
- La conclusión de diseño del 20-Oct se mantiene pero se endurece: harían falta ≈50 entradas **efectivas**/día con EV ≥ 0,08 **y** que el stake final quepa en el libro, y aun así son ~4-5 meses con ½ Kelly, no ~2.

## 4. Qué haría falta para que B/alts aporte una parte real y qué queda de hueco (pregunta 3)
Con el techo K=20 (2,44 $/relleno, deterioro 0,017), `adenda_22oct_salida.txt` §3:

| EV real | Rellenos/día para 200 k | × capacidad R3 (130/día) | Moneda-marco equivalentes (a 43,5 R3/día cada uno) | Rellenos/día para 20 k (10 %) |
|---|---|---|---|---|
| +0,05 | 6.809 | ×52 | ~157 | 681 (×5,2) |
| +0,07 | 4.240 | ×33 | ~97 | 424 (×3,3) |
| +0,11 | 2.416 | ×19 | ~56 | 242 (×1,9) |
| +0,20 | 1.228 | ×9 | ~28 | 123 (×0,9) |

- **Para que R3, tal como existe (3 alts en 5m), dé 20 k/año** necesitaría un EV real de **+0,19** a capacidad completa. Para 50 k, +0,45, que es inverosímil.
- **Para que dé ≥10 % de los 200 k con un EV realista (+0,07-0,11)** hace falta **×2-3 su capacidad**, es decir, el mismo mecanismo en más universo:
  - (a) BTC 5m, que es el 75 % del bote pero está REJECTED en v2 y necesita un conductor propio (H63);
  - (b) 15m de las alts con padre 1 h, para lo que no hay datos ms del 1 h (DATA_BLOCKED);
  - (c) BNB/DOGE: menos de 1 k€ aunque funcionara.
  - Ninguna de las tres tiene hoy evidencia.
- **Reparto honesto de los 200 k:**

  | Pieza | €/año |
  |---|---|
  | B tal como opera | **0** |
  | R3 conservador | 0 |
  | R3 base | ~2,4 k (ritmo B) – 6,1 k (capacidad completa) |
  | R3 optimista | ~10,8 k (+ rebate ≤1,3 k si se paga) |
  | **Hueco fuera de B/alts** | **≥189 k (≥94,6 %)** |

  El hueco depende de BTC (H63), de H55 en más monedas y marcos, de PRECIERRE, o de un mecanismo nuevo. Escalar el maker de alts no lo cierra, ni con todo a favor.

## 5. Propuesta para la revisión del 27-Oct (pregunta 4; el capital lo decide Javi)
**Tabla que hay que traer actualizada ese día, por fila (B, R3 shadow, R3-en-B):**
- n de rellenos;
- n_eff/día (cierre e ICC);
- EV ponderado con IC90 por días y por cierre;
- EV sin los 2 mejores días;
- mezcla cola/cruce y EV de cada tipo de relleno;
- concordancia de relleno real↔shadow;
- saldo on-chain y distancia al suelo;
- P(llegar a N=500) recalculada;
- estado del rebate (¿ha llegado algún pago?).

Que lo regenere `adenda_22oct_numeros.py` con el CSV de posiciones de ese día, más el vigía R3.

**Lo que se puede decidir el 27-Oct.** Habrá ~5 días de shadow R3, que todavía no es un gate (el gate es el 02-Nov), y la primera lectura de E1b es el 28-Oct.
1. **No añadir capital a B tal como opera.** Su EV es ≤0 con datos frescos y la tabla dice «nunca escala» con EV ≤ 0. Que B siga hasta el suelo para probar la maquinaria es lo que ya está aceptado. Si toca el suelo antes de 500 pujas (probabilidad 0,8-0,9), es pérdida de potencia, no un veredicto.
2. **Peldaño de capital realista, CONDICIONAL, para P1 micro-real R3 (5 acc, ~1,05 $/relleno):**
   - **~75 $ en la wallet dedicada** (Kelly con EV +0,07; coincide con los 56-73 $ de P(DD) ≤ 10 % en 300 rellenos), es decir, unos +60 $ sobre el saldo actual.
   - Con ½ Kelly serían ~150 $ (≈ +135 $).
   - Solo después del 02-Nov y solo si se cumple todo esto:
     - (a) shadow R3 CONFIRMADA, o REDUCE_PERDIDA con concordancia ≥0,70;
     - (b) EV(cola, R3) ≥ +0,05 con ≥60 rellenos de cola en ≥7 días (`r3_escalado` §7);
     - (c) `/code-review` + OK de Javi.
   - Qué compra: validar el EV de R3 en dinero real en ~2.700 rellenos (~21-70 días). Si se valida, deja una pieza de 2-11 k€/año. **No compra un camino a 200 k.**
3. **No subir K por encima de 20** ni ampliar a la banda 0,30-0,50 (REJECTED exploratorio).
4. **Recalcular la tabla Kelly de la ADENDA 20-Oct del PLAN_MAESTRO con la §3**: n_eff y g/2. La tabla de autofinanciación por peldaño de H55 (125-212 días) no cambia, porque usa el capital de ruina y no g; pero su n debe pasar a ser n_eff.
5. **Pedir a quien corresponda la siguiente prueba de mayor valor fuera de las alts:** el conductor de BTC (H63) y H55 en más monedas y marcos, que es donde está el ≥94 % del hueco.

## 6. Límites
- B: 3 días (el 20-Oct parcial) y ~7 h activas al día. El ritmo «20 h» es una extrapolación.
- El ICC de B tiene un IC ancho (0,04-0,47).
- El simulador es más duro que B (solo cruces) y no cuenta la concurrencia de los 119 makers en la cola.
- σ² y Kelly usan la aproximación gaussiana con el DEFF medio. Para EV ≥ 0,3 sobrestima g: la fila +0,35 es solo una cota.
- La sobredispersión por días se ha medido con 5 días.
- Los $ no están convertidos a €.

**Fuentes (sha256/16):**
- `contabilidad_wallet_dedicada/posiciones.csv` 6ccd7008b1e17f7d (foto de 15:52Z; cambia con cada tanda);
- `b_perdidas_22oct/r3_escalado/datos/b_real_r3.csv` 38daed4ece9a2b70 y `esc_2026-10-17..22.csv.gz`;
- informes `r3_escalado`, `tandas`, `anatomia`, `seleccion_adversa_plan` y `red_team/rt*.txt` (22-Oct);
- `adenda_22oct_numeros.py` 89d410d226050086;
- `adenda_22oct_salida.txt` f71d2962e5d6dd3b.
