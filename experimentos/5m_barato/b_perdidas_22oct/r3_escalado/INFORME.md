# R3: capacidad, escalado, techo anual y escalera de capital (22-Oct-2026, ~15:40Z, risk-economics)
Estado: **EXPLORATORY**. Todo es solo lectura y simulación. No he tocado B (`experimento_maker_h47.py`, sha c82f5dc5f304b8a6, verificado 15:35Z), el supervisor, los procesos, los crons, la config live ni ninguna orden. Tampoco he reabierto `reglas_congeladas.json` v2 (daa88e37…) ni el preregistro del brazo shadow (4acd5420…). Ejecución con `nice -n 19 ionice -c3`, `ulimit -v 3000000`; RSS máximo 0,42 GB, ~3 s por día.
Unidades: $ ≈ € sin convertir, igual que el LIBRO (convertir restaría un 10-15 %). EV siempre ponderado por € (Σpnl/Σcoste). Maker sin comisión y **sin sumar el rebate** (+0,011, 0 $ cobrados hasta hoy).

## 0. Respuesta corta (12 líneas)
1. **R3 separa, pero en el simulador no crea edge.** Simulador E1 con libro y operaciones a ms, ETH/SOL/XRP, 17-22 Oct, 4.408 mercados. En los rellenos de la puja tipo B, R3 verdadero da +0,025 frente a −0,228 de R3 falso: DIF +0,253, placebo permutado +0,008, p=0,003, 5/6 días positivos. Pero la **política R3** (cotizar solo con R3 verdadero) da **−0,041**, IC90 por días (−0,132; +0,049), sin los 2 mejores días −0,136. El 22-Oct, el único día virgen y parcial, da −0,137 (n=65).
2. **Recalibrado al nivel de B real, el EV central pasa a ~+0,07 con un IC enorme.** El simulador solo cuenta los rellenos por cruce, y ahí acierta igual que B: los cruces de B dan −0,09 y el simulador −0,11 en los mismos días. Lo que no modela es el relleno en cola al precio, que es el 59 % de los rellenos de B y da +0,19 (n=85, IC90 por cierre −0,26..+0,66). Con la mezcla de R3 (49 % cola): **EV(R3 en B) ≈ +0,07, rango −0,19..+0,35**. Mirado directamente, B real con R3 verdadero da +0,41, pero n=37 y sin los 2 mejores días −0,08.
3. **Capacidad: ~130 rellenos/día y ~136 €/día de puja a 5 acc.** Es con una puja por mercado y sin tope de vivas: 233 de 788 mercados/día pasan alguna vez por R3, que está activo el 14,7 % del tiempo. Por moneda: ETH 59, SOL 44, XRP 27 rellenos/día. Es un nicho concurrido: en la población hay **119 makers distintos/día** y 1.316 unidades/día en solo 211 mercados-lado.
4. **Tamaño: el EV se mantiene hasta K=20 y se rompe en 50.** En el simulador, con relleno(K) = min(K, volumen que atraviesa en 1 s), el EV es −0,033 (K5), −0,043 (K10), −0,050 (K20) y −0,099 (K50). Spearman(barrido, acierto) = −0,02. El € diario crece ×1,6 a K10, ×2,3 a K20 y ×3,3 a K50.
5. **Ampliar a la banda 0,30-0,50: no** (exploratorio). La política R3 da −0,192, IC90 por días (−0,276; −0,080), y DIF +0,076 (p=0,035; 2/6 días con signo contrario). **BTC: no** (REJECTED en v2). BNB/DOGE: sin datos ms (DATA_BLOCKED).
6. **Techo anual honesto de R3** (3 alts, todos los mercados, K≤20, con el deterioro por K): conservador **0** / base **~1,5 k€** (EV +0,03) / optimista **~11 k€** (K=20, EV +0,11−0,017). El rebate sumaría hasta +1,3 k€ si se llega a pagar. El «15-25 k€» de `b_seleccion_adversa/INFORME.md §F` multiplicaba el flujo de TODOS los makers: no es alcanzable para un solo participante. **Aporte a los 200 k: ≤5,5 %.**
7. **Capital y ruina.** Con 5,12 $ sobre el suelo, P(drawdown ≥5,12 $ antes de 300 rellenos R3 a K=5) ≈ **1,00 con cualquier EV**. Ese peldaño solo puede probar la maquinaria y la concordancia con el shadow, no el EV.
   - Para que P(DD ≥ C) ≤ 10 % hace falta: K=5 y 300 rellenos → C ≈ 56-73 $; K=5 y 1.000 → 85-136 $; K=10 y 500 → 135-190 $; K=25 y 1.000 → 430-680 $.
   - Para que el IC90 excluya 0 con EV real +0,10 hacen falta ~2.700 rellenos: unos 73 días al ritmo de B (~37/día), o 21 días a la capacidad R3 completa.
8. **Aviso para el gate del 02-Nov.** El veredicto CONFIRMADA del brazo shadow exige EV_POLÍTICA con IC95 > 0 en cons_x y cons_r. Si el gemelo del shadow queda tan duro como E1, lo más probable es REDUCE_PERDIDA o ACUMULANDO aunque R3 sí gane en B. Lo que lo decide es la concordancia de relleno real↔shadow y la proporción de rellenos en cola frente a cruce, que el vigía ya mide.
9. **Hallazgo nuevo, post hoc: la tarde (16-24 UTC) es mala dentro de R3 en dos instrumentos.** En el simulador, 4/5 días negativos (−0,157 frente a +0,010 antes de las 16 UTC). En la población, 3/4 días negativos (−0,18/−0,12 frente a +0,12..+0,30). B real, sin R3, apunta al revés (+0,23, n=24). Lo propongo como variante para forward, no como corte (ver §6).
10. **Siguiente prueba única:** la lectura diaria de la **concordancia relleno real↔shadow y de la mezcla cola/cruce, por regla y por franja horaria**, con los datos que el vigía R3 ya guarda (§7). Coste 0 y no toca el preregistro. Resuelve si el nivel recalibrado (+0,07) se sostiene.

## 1. Instrumentos, fidelidad y multiplicidad
| Instrumento | Qué es | Días | Fidelidad respecto a B real | Para qué sirve aquí |
|---|---|---|---|---|
| **Simulador E1 + flags R2/R3** (`r3_esc_sim.py`) | El MISMO simulador CONS de `seleccion_adversa_plan/scripts/e1_sim.py`: puja tipo B (ETH k2, SOL/XRP k1, bid 0,11-0,30, T 298-65, asentado 1,5 s); relleno = print que ATRAVIESA la puja. Le añado, en la rejilla de 100 ms, flags R2/R3 con los parámetros exactos de `r3_regla.py` (bid15 mismo lado − puja ≤ 0,030 con 15m no cruzado; vol30 = acciones casadas en los dos tokens del 5m en (max(t−30 s, apertura), t] por recepción; hora UTC ≥ 4), las 3 políticas (BASE / R2 / R3 = primer print que atraviesa con la regla verdadera en ese tick) y el volumen que atraviesa la puja en 1 s y en 5 s (V1/V5) | 17-21 completos + 22 hasta ~14:40Z; desenlace oficial 100 % (0 missing en la banda 0,11-0,30) | BASE reproduce exactamente E1 (531/577/324 rellenos y Σobj idénticas el 17, 20 y 22). Acierto de lo rellenado 17,0 % (B 21,7 %); solo modela rellenos por cruce | Efectos relativos (DIF), capacidad (mercados y rellenos/día), escalado K, banda |
| **Población** (`b_seleccion_adversa/datos/ms_units.pkl`) | Primeras 5 acc de OTROS makers por mercado-lado, rasgos de libro, ETH/SOL/XRP banda 0,10-0,30 | 17-21 (21 parcial) | No es la selección propia de B (cola, repegados) | Capacidad del nicho, concurrencia de makers, 2º instrumento por moneda/hora |
| **B real** (`salida/datos/unidades_b.csv` → `datos/b_real_r3.csv`) | 166 rellenos de B 20-22 Oct; 144 con print en el WS (22 sin print = missing); flags R2/R3 en print−100 ms; volumen del barrido | 3 días | Es la verdad, pero n pequeño | Recalibración del nivel |
| r3_shadow 22-Oct (datalogs) | Brazo en vivo desde 11:42Z | Parcial, no es día válido | — | Solo recuentos (sin EV; primera lectura formal el 02-Nov) |

**Multiplicidad.** R3 (regla, umbral 0,03, 26 acc, hora 4) viene congelada: aquí no se elige nada para R3. Lo que sí miro y es **EXPLORATORIO**:
- 11 celdas de la política R3: 3 monedas, 4 bandas y 4-5 bloques horarios.
- 4 tamaños × 2 ventanas (V1/V5).
- 1 banda nueva (0,30-0,50).

No corrijo por multiplicidad, así que ninguna celda es un gate.

Días: 17-21 entraron en la elección de R2 (población, `scan_pop_libro_reglas`), así que solo el **22-Oct es virgen** para R2/R3, y es parcial. R1 se eligió con 09-21.

## 2. Capacidad (pregunta 1)
### 2.1 Simulador (1 puja por mercado-lado, sin tope de 5 vivas; `datos/r3_esc_an.txt §1`)
| Día | Mercados con bid en banda | Con R2 alguna vez | Con R3 alguna vez | Rellenos BASE | R2 | **R3** | % del tiempo válido en R3 | % con bid15 |
|---|---|---|---|---|---|---|---|---|
| 17 | 806 | 324 | 232 | 531 | 176 | 122 | 13,9 | 96,2 |
| 18 | 799 | 329 | 249 | 582 | 189 | 130 | 14,8 | 94,8 |
| 19 | 791 | 313 | 238 | 567 | 186 | 132 | 14,6 | 96,5 |
| 20 | 787 | 308 | 232 | 577 | 194 | 132 | 14,8 | 94,6 |
| 21 | 757 | 268 | 216 | 542 | 168 | 136 | 15,9 | 95,8 |
| 22 (parcial) | 468 | 188 | 128 | 324 | 109 | 65 | 13,1 | 95,2 |

- **Media de 17-21: 130 rellenos R3/día** (23 % de los de BASE). Equivalen a **136 €/día de puja rellenada a 5 acc** (precio medio 0,209) y a **89 cierres/día** con al menos un relleno R3. Racimo por cierre: media 1,47 rellenos, 37 % de los cierres con ≥2.
- Por moneda (rellenos R3/día): ETH 59,4 · SOL 43,8 · XRP 27,2.
- Por hora UTC (rellenos R3/día, 17-21): de 4,0 a 9,6 por hora entre las 04 y las 23. El máximo está a las 07 (9,6) y a las 10 (9,4), y hay menos entre las 19 y las 23 (4,0-5,6). La regla corta todo lo anterior a las 04.

### 2.2 Población (otros makers; `datos/r3_esc_ruina.txt §1`)
- **R3: 1.316 unidades/día, 1.318 €/día de primeras-5, en solo 211 mercados-lado/día y 111 cierres/día, con 119 makers distintos/día.** Sin regla: 7.225 unidades, 6.912 €, 945 mercados-lado.
- Es un nicho **concurrido**: ~6 makers por mercado-lado. Nuestros rellenos en cola al precio se reparten con ellos; los de cruce no, porque un barrido consume a todos.
- Por moneda: ETH 823 u/día (EV +0,055), SOL 334 (+0,240), XRP 159 (+0,164).
- Por bloque horario, EV de otros makers: 04-08 +0,270 · 08-12 +0,301 · 12-16 +0,118 · **16-20 −0,181 · 20-24 −0,123**.

### 2.3 Shadow en vivo (22-Oct 11:42-15:20Z, parcial, NO es día válido; solo recuentos)
- 138 mercados cerrados, 120 completos.
- Rellenos cons_x: BASE 22 · R2 7 · R3 6. En cons_r: 15 · 4 · 4.
- R3/BASE = 27 % (el simulador da 23 %). Al ritmo de cons_r (~26 rellenos R3/día) se llegaría a n_true ≥ 200 en unos 8-10 días: el gate del 02-Nov va **justo** de n.
- La tasa de relleno BASE del shadow, unos 17 rellenos por cada 100 mercados, está muy por debajo del 61-72 % por puja de B. Hay que mirar la concordancia del vigía antes de fiarse del nivel.

## 3. EV con el rigor del preregistro (pregunta 1)
### 3.1 Simulador (5 acc fijas, como B; `datos/r3_esc_an.txt §2`)
| Subconjunto | n rellenos | Coste € | EV | IC90 días | IC90 cierre | Sin 2 mejores días | Días + |
|---|---|---|---|---|---|---|---|
| BASE, todos | 3.123 | 3.255 | −0,183 | (−0,243; −0,118) | (−0,251; −0,117) | −0,247 | 0/6 |
| BASE con R3 verdadero al rellenar | 547 | 575 | **+0,025** | (−0,100; +0,146) | (−0,133; +0,182) | −0,104 | 2/6 |
| BASE con R3 falso | 2.576 | 2.680 | −0,228 | (−0,292; −0,161) | (−0,296; −0,157) | −0,293 | 0/6 |
| **Política R3**, DESC 17-19 | 384 | 407 | −0,078 | (−0,165; +0,011) | (−0,248; +0,109) | −0,168 | 1/3 |
| **Política R3**, TEST 20-22 | 333 | 344 | +0,003 | (−0,109; +0,096) | (−0,211; +0,217) | −0,080 | 1/3 |
| **Política R3**, todo | 717 | 751 | **−0,041** | (−0,132; +0,049) | (−0,173; +0,099) | −0,136 | 2/6 |
| Política R3, solo 22-Oct (virgen, parcial) | 65 | 70 | −0,137 | — | (−0,512; +0,272) | — | 0/1 |
| Política R2, todo | 1.022 | 1.095 | −0,114 | (−0,201; −0,036) | (−0,226; +0,002) | −0,174 | 1/6 |

- **DIF (R3 − no R3, rellenos BASE) = +0,253.** Placebo (flag permutado dentro de día × moneda, 2.000 veces): media +0,008, p95 +0,148, **p = 0,003**. Por día: +0,58 / +0,20 / +0,19 / +0,09 / +0,36 / **−0,06 el 22-Oct**.
- Lectura: R3 reduce la pérdida de forma robusta (5/6 días), pero la política, al nivel de este simulador, ronda 0 o es negativa.
- La política es peor que «BASE con R3 verdadero» (−0,041 frente a +0,025). Al cancelar y volver a cotizar, recoge rellenos posteriores que son peores: el mismo efecto de sustitución que vio E1.
- El otro simulador (`simv2`, `an_v2b.txt`) daba +0,123 para A&R1. **Dos simuladores de cinta discrepan 0,16 en el nivel**: el nivel absoluto de un simulador no es transferible, como ya se había dicho.

### 3.2 Recalibración al nivel de B real (`datos/b_real_r3.csv`, DESCRIPTIVO)
| B real 20-22 Oct | n | EV | IC90 días | IC90 cierre | Sin 2 mejores días | Días + |
|---|---|---|---|---|---|---|
| Todos | 166 | +0,016 | (−0,149; +0,175) | (−0,260; +0,313) | −0,224 | 2/3 |
| Sin print en el WS (missing) | 22 | −0,422 | | | | |
| **R3 verdadero en su print** | 37 | **+0,410** | (+0,102; +0,839) | (−0,256; +1,244) | **−0,079** | 2/3 |
| R3 falso | 107 | −0,050 | (−0,208; +0,093) | | −0,242 | 1/3 |
| R2 verdadero | 51 | +0,250 | (−0,058; +0,661) | | −0,153 | |
| **Relleno en cola al precio** (sin print por debajo en 1 s) | 85 (59 %) | **+0,190** | (+0,133; +0,267) | (−0,264; +0,659) | | 3/3 |
| Relleno por cruce (print por debajo) | 59 (41 %) | −0,091 | (−0,722; +0,363) | (−0,515; +0,381) | | 2/3 (22-Oct −1,0) |

- **Por qué el simulador es más duro que B.** E1 solo cuenta cruces. En los cruces, B real (−0,09) y el simulador en los mismos días (−0,11) coinciden. B gana su parte positiva en los rellenos en cola al precio, y esos el simulador no los tiene.
- **EV recalibrado de R3 en B** = 0,49 × EV(cola) + 0,51 × EV(cruce, R3):
  - Supuestos: la mezcla cola/cruce en R3 es la medida en B (49 % cola, n=37); EV(cola) en R3 ≈ EV(cola) general de B; EV(cruce, R3) = política R3 del simulador.
  - Central: 0,49 × 0,19 + 0,51 × (−0,04) ≈ **+0,07**.
  - Rango con el IC90 por cierre de la cola y de la política: **−0,19..+0,35**.
- Otros anclajes: población R3 +0,114 (IC90 por días +0,079..+0,155, pero con A elegida en 17-19); B real R3 directo +0,41 (n=37); 22-Oct virgen −0,14 (simulador) y −0,08 (B real R3, n=16).
- La retención histórica de exploratorias en forward es del 11-28 % (LIBRO, trampa 3). Por eso el **escenario base usa +0,03** y el optimista +0,11.

### 3.3 Celdas (EXPLORATORIO, 11 celdas sin corregir; `r3_esc_an.txt §3`)
- **Por moneda** (política R3, simulador):
  - ETH −0,076 (n=331)
  - SOL +0,059 (n=235; 4/6 días)
  - XRP −0,119 (n=151; IC90 por días −0,46..+0,22)
  - La población dice ETH +0,055, SOL +0,240 y XRP +0,164: XRP no concuerda entre instrumentos y **lo decide H62 / N=500**.
- **Por banda de puja:** 0,15-0,20 da +0,114 (n=178, sin los 2 mejores días +0,003). Las demás dan entre −0,06 y −0,21. No es un corte.
- **Por hora:** 16-20 UTC da **−0,374** (n=114, IC90 por días −0,59..−0,18, 1/5 días +). Hora ≥16 juntas: −0,157 (n=215) frente a +0,010 antes de las 16 (n=502).
  - Por día, ≥16 frente a <16 en el simulador: 17: −0,13/+0,22 · 18: −0,44/−0,04 · 19: −0,22/−0,12 · 20: +0,11/−0,17 · 21: −0,09/+0,27.
  - En la población: 17: −0,27/+0,26 · 18: −0,14/+0,36 · 19: −0,10/+0,16 · 20: +0,19/+0,11.
  - Son dos instrumentos concordantes en 7 de 9 días-instrumento. B real (todas las pujas, no solo R3) da +0,23 a ≥16 UTC con n=24.

## 4. Escalado (pregunta 2)
### 4.1 Tamaño de la puja (simulador, relleno(K) = min(K, acciones que atraviesan en 1 s/5 s), con suelo de 5 en B)
| Política | K | EV (V1) | IC90 días | € diario relativo a K5 | Acc/día (V1) |
|---|---|---|---|---|---|
| R3 | 5 | −0,033 | (−0,120; +0,058) | 1,0 | 543 |
| R3 | 10 | −0,043 | (−0,106; +0,019) | 1,6 | 895 |
| R3 | 20 | −0,050 | (−0,113; +0,014) | 2,3 | 1.342 |
| R3 | 50 | **−0,099** | (−0,222; +0,020) | 3,3 | 1.903 |
| BASE | 5 → 50 | −0,184 → −0,181 | | 1 → 3,0 | |

- Volumen que atraviesa una puja R3 en 1 s: P(≥10) 0,53, P(≥20) 0,29, P(≥50) 0,09, mediana 10. En B real, contando lo casado a su precio o mejor en 1 s: P(≥10) 0,50, P(≥20) 0,22, mediana 10.
- **corr(tamaño, acierto)**: Spearman(barrido, gana) −0,024 en R3 y +0,005 en BASE.
  - EV por tamaño del barrido: <5: +0,02 · 5-10: −0,01 · 10-20: +0,03 · 20-50: −0,10 · ≥50: −0,17.
  - Los barridos grandes son algo peores. Por eso K=50 cae ~0,07 y K≤20 solo ~0,01-0,02.
  - **No se fuerza el libro**: el tamaño extra solo se llena con volumen que ya atraviesa, no hace falta cruzar.
- **Límite.** No están modeladas la posición en cola de una puja grande (con más tamaño hay más rellenos en cola parciales, que es la parte buena de B) ni la cancelación más lenta de una puja parcialmente llena. **K=20 es el techo razonable que se puede defender; K=50 empeora en el único instrumento que lo mide.**

### 4.2 Número de monedas y bandas
- **3 alts**: ya es todo lo que hay en el registro ms (npz: ETH/SOL/XRP 5m+15m).
- **BTC**: REJECTED en v2 (A −0,030, IC90 por días −0,213..+0,161, n=36.407). Es el 75 % del bote, así que necesita un conductor propio (H63).
- **BNB/DOGE**: DATA_BLOCKED. No están en el npz, y su bote maker en la banda (pie 09-18 Oct) es +0,07 k$/día y −0,03 k$/día: aunque R3 funcionara, sumarían <1 k€/año.
- **Banda 0,30-0,50** (`datos/r3_b3050_an.txt`):
  - Capacidad 223 rellenos R3/día y 450 €/día.
  - Política R3: **−0,192**, IC90 por días (−0,276; −0,080), 1/6 días.
  - DIF +0,076 (p=0,035; −0,05 y −0,03 en 2 días).
  - 22-Oct: 34 mercados sin desenlace (missing).
  - **El mecanismo no se extiende a la banda alta: REJECTED como palanca de capacidad (exploratorio).**

## 5. Techo anual honesto (pregunta 3) y encaje en los 200 k
Fórmula: €/día de puja rellenada R3 (simulador, 17-21, con el suelo de 5 acc de B) × max(EV + deterioro por K, 0) × 365. Rebate aparte.

| K | €/día | Conservador (EV 0) | Base (+0,03) | Optimista (+0,11) | Rebate (+0,011), si se paga |
|---|---|---|---|---|---|
| 5 | 136 | 0 | 1,5 k | 5,5 k | 0,5 k |
| 10 | 215 | 0 | 1,6 k | 7,9 k | 0,9 k |
| **20** | 317 | 0 | 1,5 k | **10,8 k** | 1,3 k |
| 50 | 443 | 0 | 0 | 7,1 k | 1,8 k |

- **Techo de R3 = 0 / ~1,5 k / ~11 k €/año.**
  - Supuestos: un participante, 3 alts, todas las horas ≥4 UTC, sin tope de vivas.
  - La concurrencia de los otros 119 makers está sin restar en los rellenos en cola.
  - Variante sin la tarde (16-24 UTC): ~70 % del volumen con EV +0,05 más alto en el simulador, así que techo optimista parecido (~10-11 k) con menos varianza. Es exploratorio.
- **Para el LIBRO.** R3 pasa a ser una fila con optimista ≤11 k y base ~1,5 k, por debajo del «15-25 k» que se había comunicado. Hoy no cuenta nada como ingreso: es peldaño 2-4 (forward congelado).
  - Para que R3 «sume» de verdad hace falta: (a) que el forward del 02-Nov dé CONFIRMADA, o REDUCE_PERDIDA con concordancia que justifique el recalibrado; (b) peldaño micro-real con concordancia ≥ 0,70; (c) capital (§6).
  - **Aun con todo a favor, R3 es ≤5,5 % del objetivo.** El hueco a 200 k depende de BTC (H63), de otro marco anidado (15m con padre 1 h: sin datos ms del 1 h en el npz) o de otro mecanismo, no de escalar R3.

## 6. Peldaños de capital y de gate (pregunta 4)
Monte Carlo de `r3_esc_ruina.py`, 20.000 trayectorias:
- Pago binario a precio 0,21.
- Racimos por cierre empíricos del simulador (media 1,47).
- Correlación ρ = 0,333 dentro del cierre, calibrada a la concordancia 0,774 de B (`tandas/INFORME.md`).
- σ por relleno de 5 acc ≈ 2,0 $.

| Peldaño | Stake por puja (K) | Requisito de entrada (todos, además de `/code-review` + OK Javi) | Capital para P(DD ≥ C) ≤ 10 % durante el peldaño | Riesgo con el capital de hoy (5,12 $ sobre 12) | Qué demuestra / criterio para subir |
|---|---|---|---|---|---|
| **P0 shadow** (en marcha) | — | Preregistro congelado 4acd5420 | 0 € | 0 | Gate del 02-Nov tal cual. Lectura complementaria: concordancia real↔shadow ≥ 0,70 y mezcla cola/cruce por regla (§7) |
| **P1 micro-real R3** (variante `b_r3`, tras N=500 de B) | ~1,05 € (5 acc) | R3 CONFIRMADA, o REDUCE_PERDIDA con concordancia ≥ 0,70 | 300 rellenos: **56-73 $** (e = +0,10..0). 1.000 rellenos: 85-136 $ | **P(DD ≥ 5,12 $ antes de 300 rellenos) ≈ 1,00** con cualquier EV de −0,05 a +0,10: el suelo lo para en pocas decenas de rellenos | Maquinaria (0 errores), tasa de relleno ±8 pp del shadow, mezcla cola/cruce ±10 pp, EV real no por debajo del predicho por el shadow en más de 2σ. **El EV no se puede demostrar aquí** |
| **P2** | ~2 € (≈10 acc) | P1 cumplido con ≥ 300 rellenos R3 y forward shadow ≥ 20 días con IC90 por días del EV recalibrado > 0 | 500 rellenos: **135-190 $** | ruina segura | Deterioro K10 frente a K5 ≤ 0,02 (simulador: −0,010) |
| **P3** | ~5 € (≈25 acc) | P2 + EV real acumulado con IC90 por días > 0 y sin los 2 mejores días > 0. Exige ~2.700 rellenos si el EV es +0,10 (~73 días al ritmo de B o 21 a capacidad completa) | 1.000 rellenos: **430-680 $** | — | EV(K25) ≥ EV(K10) − 0,03 |
| P4 | ~10 € (≈50 acc) | **No recomendado**: el simulador da −0,066 frente a K5 | 1.000 rellenos: 0,85-1,4 k$ | — | Solo si P3 no muestra deterioro |

- **Capital = decisión de Javi.** El calendario no tiene recargas, así que cada peldaño por encima de P1 es CONDICIONAL. Con el capital de hoy, R3 en dinero real solo valida la maquinaria y la concordancia.
- No se escala por PnL acumulado: un kill por pérdida salta en falso (trampas 19-Oct y 22-Oct).
- **Variante propuesta para forward, sin reabrir R3: «R3-DIA» = R3 + hora UTC < 16.**
  - Mecanismo: la tarde de EE. UU. trae más tomadoras direccionales informadas.
  - Concordancia: 2 instrumentos en 7 de 9 días.
  - Coste: ~30 % del volumen.
  - Se registraría como hipótesis nueva (el chief), medida en el MISMO brazo shadow como flag adicional sin tocar el preregistro. Gate: ≥10 días virgen, IC95 por días de DIF(<16 frente a ≥16 dentro de R3) > 0.

## 7. Siguiente prueba (única) y lo que no conviene hacer
**Prueba siguiente: lectura diaria de la «calibración B↔shadow» con datos que ya existen.** Coste 0, sin código en producción. Es una lectura complementaria, no cambia el gate.
- Del ledger de B (`puja_post`), y de la variante R3 cuando exista, se reconstruye cada relleno real como hago en `b_real()`: print, cola frente a cruce, R2/R3 en print−100 ms.
- Se cruza con el relleno simulado cons_x/cons_r del shadow sobre el mismo mercado.
- Métricas:
  - matriz 2×2 de relleno real × simulado;
  - % cola/cruce por regla;
  - EV por tipo de relleno y por regla;
  - franja ≥16 UTC.
- **Éxito:** concordancia ≥ 0,70 en ambas direcciones y EV(cola, R3) ≥ +0,05 con ≥ 60 rellenos de cola R3 en ≥ 7 días. Si se cumple, el nivel recalibrado (+0,07) gana credibilidad y P1 queda justificado aunque el gate dé REDUCE_PERDIDA.
- **Fracaso:** concordancia < 0,70, o EV(cola, R3) ≤ 0 con ≥ 60 rellenos. En ese caso el techo de R3 baja a 0-1,5 k y R3 queda como filtro de pérdida, no como fuente de €.
- Valor de la información: decide si R3 es una pieza de ~5-11 k o de ~0 sin gastar un $. Tarda ~10 días, los mismos del gate.

**No conviene:**
- Escalar K por encima de 20.
- Abrir la banda 0,30-0,50.
- Apilar S1 sobre R3 (+0,002, red team).
- Usar el «15-25 k» de la §F.
- Leer el EV de la política R3 del simulador como nivel de B: sobreestima la pérdida en la parte de cola, igual que simv2 la subestimaba.

## 8. Reproducir y ficheros (`experimentos/5m_barato/b_perdidas_22oct/r3_escalado/`)
- `r3_esc_sim.py DIA…` → `datos/esc_D.csv.gz`. Con `R3_PREF=b3050 R3_BAND_LO=0.30 R3_BAND_HI=0.50` → `datos/b3050_D.csv.gz`. `r3_esc_sim.py breal` → `datos/b_real_r3.csv`.
- `r3_esc_an.py` (con `R3_PREF=` opcional) → `datos/r3_{esc,b3050}_an.txt` y `_resumen.json`.
- `r3_esc_ruina.py` → `datos/r3_esc_ruina.{txt,json}`.
- Ejecutar desde /tmp con `nice -n 19 ionice -c3`, `ulimit -v 3000000` y `python3` del sistema (el `.venv` no tiene pyarrow para el pkl).
- Hashes sha256 (16): `r3_esc_sim.py` 714929dbc00ee678 · `r3_esc_an.py` 40e4ec538db24dcb · `r3_esc_ruina.py` 7b654edacbf5bdc3 · `r3_esc_an.txt` c03929013d0dc757 · `r3_b3050_an.txt` af359c099affdd80 · `r3_esc_ruina.txt` 20ba4c7d6b23ba01 · `b_real_r3.csv` 38daed4ece9a2b70.
- Entradas, sin modificar: `../salida/datos/ms_2026-10-17..22.npz`, `unidades_b.csv`, `desenlaces_extra.json`, `/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json`, `../../b_seleccion_adversa/datos/ms_units.pkl`, `/root/polymarket-research-datalogs/r3_shadow/r3_shadow_2026-10-22.jsonl.gz` (solo recuentos).
- Comprobación de identidad: BASE = E1 (mismos rellenos y Σobj el 17, 20 y 22); con la banda por defecto, la versión parametrizada da un CSV byte a byte idéntico (`cmp`).
- **Bug cazado y corregido en mi propio código:** `Dia.trades(k, t0, t1)` excluye las operaciones con hora exactamente t0 (`searchsorted 'right'`). El volumen del barrido debe pedirse desde r−1. Sin esa corrección, la mediana de V1 salía 0 y el «EV por K» quedaba sesgado.
- **Límites:**
  - 6 días, uno parcial; solo 1 virgen y parcial.
  - Simulador sin cola, sin latencias reales de API y sin tope de 5 vivas.
  - B real con 3 días y n=144 con print.
  - El racimo usa ρ calibrado en B.
  - El rebate no está sumado.
