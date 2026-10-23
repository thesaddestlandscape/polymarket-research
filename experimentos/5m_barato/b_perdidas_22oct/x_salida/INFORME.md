# X-SALIDA (OLA 5): salida a nivel de CURVA DE SALDO / TANDA de B hacia 200 k€ (23-Oct-2026, calculado 09:03-09:22Z)
Estado: **EXPLORATORY**. Beneficio validado: 0 €. Solo lectura: B, supervisor, ejecutores, crons y config intactos; sin órdenes, sin claves, sin commits. Prereg `PREREG.md` (sha256 449422c4…, `sha256sum -c PREREG.sha256` = OK) congelado a las 08:58Z antes de calcular ningún estadístico. Todo lo posterior va marcado POST-HOC. Hashes de código y salidas: `HASHES.txt`. Salidas pesadas en `/root/polymarket-research-datalogs/x_salida/` (22 MB). Cálculo con `nice -n 19 ionice -c3`, `ulimit -v 3000000`, un proceso a la vez, ~12 min en total, nada pesado antes de las 09:00Z. $ ≈ € sin convertir.

## 0. Conclusión en 8 líneas
1. **Ninguna regla de salida a nivel de curva crea EV, y la demostración es directa.** En el entorno sintético con el flujo y los precios reales de B, el ΔPnL de cada regla es `EV_verdadero × Δcoste desplegado` (cociente ΔPnL/Δcoste de las reglas que más recortan: +0,036..+0,056 con e=+0,05, +0,100..+0,116 con e=+0,10, −0,042..−0,058 con e=−0,05; Wald) y ≈0 con e=0, |Δ|≤1,40 $ (§3.3). Una regla de parada solo decide cuánto volumen se juega: si el EV es negativo «mejora» el PnL por jugar menos, y si es positivo lo recorta en la misma proporción.
2. **No hay estructura explotable en los incrementos por cierre.** Con permutación intra-día calibrada (falsos positivos 2,7-6,7 % al 5 % nominal con desenlaces sintéticos), el proxy largo DL (110 k cierres, 549 días) muestra una autocorrelación lag-1 de **+0,011** (p Bonferroni 0,009), una pendiente de EV sobre beneficio previo del día y un VR(8)=1,035, todos del mismo signo (momentum diminuto, ≈1 % de la varianza). La población real de makers DP (1.614 cierres, 6 días, MDE lag-1 0,07) da signo contrario (lag-1 −0,028, VR(8)=0,93, p 0,22/0,24) y B real (112 cierres, MDE 0,27) da −0,013 (p 0,96). El criterio fijado (mismo signo y p Bonferroni <0,05 en DL **y** DP) **no se cumple**. «No se ve al nivel MDE», no «demostrado que no existe».
3. **Las ganancias aparentes de las reglas en B real son EV negativo + camino.** Reproduciendo B (19,59 $, sin suelo duro) todas las reglas de parada suben el PnL (hasta +41 $ TPd6) porque B tiene EV −0,068/€ (201 posiciones, IC90 por cierre −0,318..+0,204, por días −0,394..+0,373) y quitan volumen; el mejor p de placebo es 0,007 (TPd6), por encima de Bonferroni 0,05/14=0,0036, y ninguna de las 14 se mantiene en el segundo instrumento (DP: ΔPnL ≤ +2,4 $ con IC90 por días que incluye 0, y negativo en las que recortan volumen) ni con e=+0,05.
4. **El drawdown sí se mueve con las reglas de tope diario/rotación (con e=+0,05, TPd3: dd medio 41,4→27,0 y p90 62→41; MAXROT1: →19,3 y p90 27) pero a coste de PnL esperado −60 % / −85 % con e=+0,05**, y el crecimiento log g no mejora salvo con edge ≤0 (donde ninguna regla es positiva). Es varianza, no EV.
5. **Candidata: NINGUNA.** Gate para que alguna se vuelva candidata y modo pasivo sin riesgo en §6 (`scripts/pasivo.py` ya calcula las 14 reglas sobre cada día real de B; salida `datalogs/x_salida/pasivo.csv`).
6. **Hacia 200 k€: la salida no mueve el hueco.** Con EV y σ medidos (σ²/€ 4,14, DEFF 1,19, n_eff 52/día) el Kelly de B es 0 porque el EV medido es negativo. Si el EV fuera +0,07 harían falta ≈7.800 $/día de nocional (115× B real, 25× el techo R3 K=20, 1,5× todo el nocional de la población de makers de ETH/SOL/XRP 5m barato); a EV +0,20, 2.740 $/día (40× B, 8,6× techo R3, 0,53× el pool entero). Con el techo de profundidad (2,44 $/relleno, deterioro 0,017) el ingreso máximo con 73-130 fills/día es 3,4-6,1 k€/año a EV 0,07 y 11,9-21 k€ a EV 0,20. Hueco honesto ≥ 189 k€/año (§5).
7. **La palanca que sí existe es de capital/tamaño, no de salida:** con 19,59 $ el log-crecimiento por relleno es negativo (stake mínimo 1,05 $ = 5,4 % del saldo, de 4 a 9× el Kelly) y la política «operar siempre» arruina (W<5 $) en 56 % de las trayectorias con EV +0,07 y en 82 % con +0,03; con 150 $ baja a 5 %/33 %. Es decisión de Javi (sin recargas planificadas).
8. **Aviso de premisa:** la prereg y las 40 reglas anteriores asumían suelo duro 12 $. Las tandas 26-28 arrancaron con base 11,86 / 7,33 / 6,31 $ (ledger `movimientos.csv`), es decir, se opera por debajo; añado el entorno POST-HOC `S_H0` (19,59 $ sin suelo duro) que replica mejor a B (R0 −17,84 $ con 169 de 201 posiciones vs real −14,88 $ con 201).

## 1. Datos (hashes en `HASHES.txt`; copias en datalogs)
| Conjunto | Contenido | n | Notas |
|---|---|---|---|
| DB | B real H47-B liquidadas con desenlace oficial, snapshot 09:05Z (`posiciones.csv`, sha 85316693…) | 201 posiciones, 112 cierres, 4 días UTC (20: 37, 21: 72, 22: 77, 23: 15 parcial) | coste 220,16 $, PnL −14,88 $, **EV pond −0,0676**; 1 posición abierta (tanda 28) excluida |
| DP | población real otros makers ETH/SOL/XRP 5m, 17-22 Oct, 5 acc, pc 0,10-0,30, T 60-300 s (`cola_posicion/datos/pop_units_*`) | 28.871 unidades, 1.614 cierres, 6 días (22-Oct parcial) | cobertura de desenlace 100 %; EV pond **−0,0215**; sin B (`es_b==0`) |
| DL | proxy largo `detector_regimen/datos/panel_*` T=180, q∈[0,10;0,30], ETH/SOL/XRP, prioridad bookticker>backfill>dic_ene>y2025 | 174.075 filas, 109.978 cierres, 549 días | precio de MODELO q, **no ask real**, EV proxy −0,161: solo sirve para estructura temporal, no para niveles |
Unidad estadística: el CIERRE (n efectivo B ≈ 52 entradas independientes/día de 62 posiciones, DEFF 1,19).

## 2. PARTE A - estructura de los incrementos (`xs_a.py` → `parteA.json`)
Permutación intra-día (5.000 en DB y DP, 2.000 en DL; semilla 20261023), p bilateral alrededor de la media nula (S5 unilateral), Bonferroni ×6 por conjunto.
| Estadístico | DB (n=112, MDE lag-1 0,265) | DP (n=1.614, MDE 0,070) | DL (n=109.978, MDE 0,008) |
|---|---|---|---|
| S1 lag-1 | −0,013 (p 0,96) | −0,028 (p 0,22) | **+0,0107 (p 0,0015; Bonf 0,009)** |
| lag-2 / lag-3 (desc.) | −0,166 / +0,084 | +0,004 / +0,011 | +0,006 / +0,005 |
| S2 pendiente EV vs beneficio previo del día | −0,0167 (p 0,63) | +0,0016 (p 0,99) | **+0,00091 (p 0,0005; Bonf 0,003)** |
| S3 reversión tras pico ≥2σ (n cond.) | −0,90 (59 casos; p 0,16) | −1,56 (418; p 0,41) | +0,0012 (20.944; p 0,78) |
| S4 VR(8) [VR 2/4/16] | 0,884 [1,00/0,92/0,58] (p 0,94) | 0,929 [0,97/0,96/0,92] (p 0,24) | **1,035 [1,01/1,03/1,04] (p 0,0005; Bonf 0,003)** |
| S5 máx. |EV bloque 4 h − global| | 0,468 (p 0,25) | 0,176 (p 0,18) | 0,043 (p 0,002; Bonf 0,012) |
| S6 (solo DL) lag-1 del EV diario / razón de varianza | | | +0,029 (p 0,50) / 1,074 (p 0,11), 547 días |
- **Calibración con desenlaces sintéticos** (Bernoulli con copula intra-cierre ρ=0,333, e=0, 150 réplicas × 300 permutaciones): falsos positivos al 5 % nominal en DB S1-S5 = 4,7/3,3/2,7/4,0/6,7 %; en DP 5,3/4,0/4,0/4,7/4,7 %. La permutación intra-día está calibrada; el sesgo de 8,8-11,3 % de D-FUERTE era del bootstrap de días. DL no se calibró con sintéticos (su desenlace no es simulable con el mismo método); su p es exacto bajo intercambiabilidad de cierres dentro del día.
- **Lectura.** DL contiene un momentum intradía real pero minúsculo (lag-1 0,011; EV condicional a un cierre +1σ: ≈+0,02 EV/€, si lo tradujéramos a la escala de B) y de signo contrario al que se ve (sin significación) en DP y en B real; y un efecto de bloque horario (EV −0,135..−0,204 por bloque) que DP no replica (p 0,18). Por ello no se cumple el criterio y no se convierte en regla. Potencia: con MDE 0,07 (DP) y 0,27 (DB) **no podemos excluir** un lag-1 de |0,07| en DP, que daría hasta ≈0,07σ por cierre; con 112 cierres B real casi no tiene potencia (cuatro días).
- **Hora en DP, POST-HOC:** el EV pond de 06-12 UTC es **+0,135** (por días +0,03/−0,10/+0,04/+0,25/+0,39/+0,18) frente a −0,0215 del día entero (horas 1-5 y 19-23 negativas). Es una mirada posterior en 6 días (SE ≈0,07), con la dirección del día dominando; no la uso como regla. Explica por qué el pseudo-B de §3.2 sale con EV +0,12/+0,15 y no con el de B real.

## 3. PARTE B - reglas de salida sobre la curva (`xs_sim.py`, `xs_b.py`, `xs_g.py`)
Simulador del PREREG §3 (tanda con presupuesto Bd, suelo móvil con ratchet +1, rotación si E≥H+Bd, parada de la trayectoria si no). Fidelidad: R0 con 19,59 $ y H=12 toma 138/201 posiciones y da −2,77 $ (la trayectoria se para a los 1,9 días); con H=0 (S_H0, POST-HOC) toma 169/201 y da −17,84 $ frente al real −14,88 $ (discrepancia −2,96 $; las 32 posiciones bloqueadas son las que el presupuesto del simulador no habría permitido). No se ha ajustado.
Multiplicidad: 14 reglas, Bonferroni 0,05/14 = **0,00357**.

### 3.1 Tabla regla → ΔPnL, Δdrawdown, g, IC, placebo (Δ frente a R0 sobre el mismo flujo)
Columnas: **B-H0** = replay del flujo real de B (19,59 $, sin suelo duro; Δ y Δ_est=Δreal−Δpermutado intra-día, p placebo de 2.000 permutaciones, IC90 de bootstrap de bloques de 6 cierres entre paréntesis); **DP** = pseudo-B de población, S_real (19,59 $, 10 días, 1.800 trayectorias: 300 por día-fuente), ΔPnL con IC90 por día-fuente (t, 5 gl) y Δ_est con p por día-fuente; **Sintético** = flujo y precios de B con resultados Bernoulli (e = EV verdadero), E_ini 40 $, 12 días, ΔPnL con e=+0,05 (% del PnL de R0, que es +20,05 $) y con e=0; Δ dd medio con e=0 (R0 = 41,2 $); g = ln(E_fin/40)/12 por día con e=+0,05 / +0,10 (R0: −0,0080 / +0,0331).
| Regla | B-H0 ΔPnL (IC90 bloques) | B-H0 Δ_est / p | DP ΔPnL [IC90 días] | DP Δ_est [IC90 días] / p | Sint. Δ e=+0,05 (%) / e=0 | dd (e=0) | g (+0,05 / +0,10) |
|---|---|---|---|---|---|---|---|
| R0 actual | −17,84 | | +17,87 | | +20,05 / 0 | 41,2 | −0,0080 / +0,0331 |
| W2.5 | +23,97 (−3,4,+45,7) | +15,4 / 0,109 | −0,88 [−2,00,+0,24] | −0,26 [−2,54,+2,01] / 0,83 | −3,39 (−17 %) / −1,02 | 38,3 | −0,0075 / +0,0281 |
| W3.5 | +6,00 (−4,6,+29,8) | +3,7 / 0,37 | +1,40 [−1,33,+4,13] | +1,33 [−0,20,+2,86] / 0,14 | −0,05 (0 %) / −0,25 | 40,8 | −0,0046 / +0,0310 |
| W8 (arranca solo si E≥20) | +11,85 (−3,3,+25,8) | +13,6 / 0,038 | no arranca (−17,87) | n/m | −0,28 (−1 %) / −1,02 | 39,9 | −0,0053 / +0,0341 |
| NR sin ratchet | +5,06 (−3,8,+22,6) | +10,4 / 0,044 | +2,44 [−0,31,+5,18] | +0,50 [−0,52,+1,52] / 0,37 | +1,64 (+8 %) / +0,04 | 42,7 | −0,0091 / +0,0329 |
| TPd3 objetivo diario 3 | +24,86 (−11,7,+40,6) | +18,4 / 0,133 | −10,38 [−24,56,+3,80] | +1,77 [+0,07,+3,48] / 0,09 | −12,06 (−60 %) / −0,08 | 29,0 | −0,0050 / +0,0137 |
| TPd6 objetivo diario 6 | **+41,12** (−10,7,+26,1) | +36,9 / **0,007** | −8,36 [−21,12,+4,40] | +1,40 [−0,80,+3,59] / 0,26 | −10,25 (−51 %) / −0,02 | 32,1 | −0,0060 / +0,0186 |
| TPT3 objetivo tanda 3 + pausa 1 h | +18,41 (−15,0,+36,5) | +12,5 / 0,19 | −3,78 [−9,46,+1,91] | +1,88 [−0,09,+3,85] / 0,11 | −5,09 (−25 %) / −1,06 | 35,2 | −0,0093 / +0,0175 |
| TPT6 objetivo tanda 6 + pausa 1 h | +7,98 (−11,8,+35,5) | +4,5 / 0,30 | −1,74 [−5,36,+1,88] | +2,79 [+0,20,+5,39] / 0,08 | −4,01 (−20 %) / +0,28 | 37,2 | −0,0093 / +0,0242 |
| LOCK3_50 | +10,79 (−4,0,+12,9) | +10,0 / 0,098 | −0,74 [−1,68,+0,20] | −0,19 [−1,13,+0,75] / 0,71 | −0,70 (−4 %) / +0,88 | 40,4 | −0,0075 / +0,0301 |
| LOCK6_50 | +2,82 (−3,3,+6,2) | +2,7 / 0,18 | −0,16 [−0,55,+0,23] | +0,05 [−0,15,+0,26] / 0,64 | −0,07 (0 %) / +0,23 | 40,9 | −0,0079 / +0,0302 |
| LOCK3_75 | +7,34 (−2,8,+29,8) | +5,8 / 0,23 | −0,80 [−2,88,+1,28] | −0,26 [−1,96,+1,43] / 0,77 | −0,29 (−1 %) / +0,28 | 40,7 | −0,0083 / +0,0305 |
| MAXROT1 | +13,02 (−32,3,+18,6) | +7,4 / 0,25 | −9,43 [−22,53,+3,68] | +4,58 [−1,54,+10,70] / 0,19 | −16,99 (−85 %) / −1,30 | 20,2 | −0,0014 / +0,0074 |
| MAXROT2 | +24,40 (−18,9,+21,8) | +21,2 / 0,053 | −8,35 [−25,16,+8,45] | +3,36 [−6,00,+12,73] / 0,50 | −13,70 (−68 %) / −1,40 | 27,2 | −0,0046 / +0,0150 |
| TIME40 | −1,50 (0,0) | −1,9 / 0,83 | −1,25 [−3,75,+1,25] | −0,42 [−1,59,+0,75] / 0,50 | −1,48 (−7 %) / −0,35 | 40,3 | −0,0068 / +0,0274 |
Lectura:
- **B-H0 y S_real/S_free de B** (en `parteB.json`): todos los Δ de reglas que cortan volumen son positivos porque B tiene EV −0,097 sobre este flujo (R0). El mejor p de placebo es 0,007 (TPd6), que ni pasa Bonferroni (0,00357) ni se mantiene en DP (−8,4 [−21,1,+4,4]). La probabilidad de que el mínimo de 14 p-valores independientes quede ≤0,007 es ≈9 %: es lo esperable por azar. No he desglosado la ganancia de TPd6 por día; es compatible con camino (B ganó el 20-21-Oct y perdió el 22-Oct) y no hay replicación fuera de B, así que no la trato como estructura.
- **Δ_est (estructura)**: en DP-S_real positivo en 9 de 14 reglas con IC90 por días >0 solo en TPd3 [+0,07,+3,48] y TPT6 [+0,20,+5,39] (p por días 0,09 y 0,08, ≫0,00357), y en S_free TPT6 [+2,58,+17,08] (p 0,041) y W2.5 [+0,65,+2,99] (p 0,026); en B real la Δ_est de TPT6 es +4,5 (p 0,30) y no hay concordancia de signo con DL (momentum). **Ninguna regla cumple el criterio de palanca útil** (ΔPnL>0 con IC90>0 en DP **y** Δ_est>0 con IC90>0 **y** p<0,00357 **y** ΔEV retenido ≥0 **y** Δ>0 en B y ≥5 de 6 días **y** pérdida ≤10 % con e=+0,05): las que mantienen el PnL con e=+0,05 (W3.5, W8, NR, LOCK*, TIME40) no recortan volumen, no tienen Δ_est significativa y no mejoran nada; las que recortan volumen (TPd, TPT, MAXROT, W2.5) pierden del 17 % al 85 % del PnL con e=+0,05.
- **EV pseudo-B ≠ EV de B real.** El pseudo-B (cierres con la probabilidad horaria de B y 1+Poisson(0,8) unidades por cierre) sale con EV +0,12/+0,15 porque las horas 06-12 UTC de DP son +0,135 (§2). Por eso solo uso Δ_est y el barrido de e del entorno sintético para el nivel.

### 3.2 Drawdown y varianza (E-S, POST-HOC `xs_g.py`, 800 trayectorias por e, E_ini 40 $, 12 días)
| e (EV verdadero) | R0 PnL medio (sd) | R0 dd medio / p90 | R0 P(parada) | TPd3 PnL / dd p90 / P(parada) | MAXROT1 PnL / dd p90 / P(parada) | TPT6 PnL / dd p90 |
|---|---|---|---|---|---|---|
| 0,00 | +1,6 (42,4) | 42,3 / 63,6 | 0,62 | +1,2 / 43,0 / 0,46 | −0,0 / 27,9 / 0,13 | +1,1 / 55,4 |
| +0,05 | +17,0 (52,4) | 41,4 / 62,4 | 0,50 | +8,5 / 40,7 / 0,37 | +4,6 / 27,2 / 0,10 | +12,4 / 53,0 |
| +0,10 | +46,9 (60,9) | 39,1 / 56,4 | 0,31 | +17,4 / 37,3 / 0,24 | +9,7 / 26,6 / 0,07 | +33,2 / 49,4 |
- El drawdown ya viene del pago (acierto ≈21 %, +4,1/−1,1 $): con e=+0,10 el dd de R0 sigue en 39 $. Las reglas de tope diario/rotación bajan el dd entre 6 y 21 $ pero en la misma proporción en la que bajan el PnL esperado.
- **Parada total de la trayectoria (E<17 $) con 40 $ iniciales**: R0 50 % con e=+0,05 y 31 % con +0,10. El suelo duro actúa como kill que salta en falso aunque el edge sea real (coincide con `tandas/INFORME.md` §3, 80 % con 19,59 $).

### 3.3 Prueba de Wald (REGLA DURA), entorno sintético con e conocido (1.500 trayectorias por e)
| e | ΔPnL/Δcoste de las 6 reglas que más recortan coste (TPd3, TPd6, TPT3, TPT6, MAXROT1, MAXROT2) | esperado = e |
|---|---|---|
| −0,10 | −0,082 a −0,105 | −0,10 |
| −0,05 | −0,042 a −0,058 | −0,05 |
| 0,00 | −0,004 a +0,010 (todas |Δ|≤1,40 $, ≤1,75 SE) | 0 |
| +0,05 | +0,036 a +0,056 | +0,05 |
| +0,10 | +0,100 a +0,116 | +0,10 |
(W2.5 y las reglas con Δcoste≈0 dan cocientes inestables y no se usan.) Las reglas con recorte grande de coste clavan Δ=e×Δcoste. Los incrementos son martingala-con-deriva-e dentro de la precisión de la simulación, así que **la regla no cambia el EV por euro**: solo cuánto € se arriesga y el camino.

## 4. PARTE C - tamaño y plan de escalado (`xs_c.py` → `parteC.json`)
### 4.1 Momentos medidos (EV ponderado por €)
| | B real (DB) | Población (DP) | Pool pseudo-B (cierre-1+Poisson(0,8)) |
|---|---|---|---|
| EV pond | **−0,0676** | −0,0215 | −0,092 (peso por cierre) |
| IC90 por cierre (bootstrap 2.000) | −0,318..+0,204 | −0,087..+0,040 | |
| IC90 por días completos (t) | −0,394..+0,373 (3 d) | −0,154..+0,094 (5 d) | |
| EV por día | +0,070 / +0,166 / −0,267 / −0,554 (23-Oct, n=15) | −0,049/−0,147/−0,114/−0,025/+0,185/+0,062 | |
| σ² por € (ponderada por coste) | 4,14 | 3,61 | 4,15 |
| DEFF (cluster por cierre) | 1,19 | 11,0 (cierres con ~18 unidades, no comparable) | 1,45 |
| posiciones/día · n_eff/día | 62 · 52 | 5.182 · 470 | |
| nocional/día | 68,2 $ | 5.163 $ | |
- f\* Kelly = EV/(σ²·DEFF) = **0 para B real y DP** (EV<0). g = n_eff·EV²/(2σ²) por día = 0.
- Con el pool pseudo-B (σ²·DEFF = 6,0): f\* = 0,5 % (EV 0,03), 1,2 % (0,07), 1,8 % (0,11), 3,3 % (0,20). Saldo mínimo para stake 1,05 $ = ½ Kelly: 420 / 180 / 115 / 63 $; mínimo de crecimiento log positivo (1,05 $ ≤ 2·f\*·W): 105 / 45 / 29 / 16 $. (La ADENDA 22-Oct daba 143-150 $ con EV 0,07 usando σ²·DEFF = 3,81·1,3; aquí DEFF 1,45 sube el mínimo a 180 $.) Todo esto es **SCENARIO**: parte de un EV que hoy no está medido (B real es negativo).

### 4.2 Nocional necesario para 200.000 €/año limpios (365 d; EV neto por €)
| EV | nocional/día | × B real | × techo R3 K=20 (130 fills × 2,44 $) | × pool DP | fills/día a 2,44 $ |
|---|---|---|---|---|---|
| 0,03 | 18.265 $ | 268 | 57,6 | 3,5 | 7.486 |
| 0,05 | 10.959 | 161 | 34,5 | 2,1 | 4.491 |
| 0,07 | 7.828 | 115 | 24,7 | 1,5 | 3.208 |
| 0,11 | 4.981 | 73 | 15,7 | 0,96 | 2.042 |
| 0,20 | 2.740 | 40 | 8,6 | 0,53 | 1.123 |
| 0,30 | 1.826 | 27 | 5,8 | 0,35 | 749 |
(260 días: ×1,40 en todas las filas.) El pool DP es lo que ponen **todos** los makers en ETH/SOL/XRP 5m barato en un día, con EV agregado −0,02: capturar el 50 % a EV +0,20 no es un escenario de mercado.

### 4.3 Reinversión por tramos (Monte Carlo 2.000 trayectorias, 730 días, ½ Kelly con pool pseudo-B, stake = clamp(½f\*·W; 1,05; 2,44 $), deterioro lineal 0,017 hasta el techo, ruina W<5 $)
Posiciones/día 73 (ritmo de B en 20 h) · «operar siempre» (como B) / «guardia» (solo opera si 1,05 $ ≤ 2·f\*·W):
| EV | W0 | P(ruina) siempre / guardia | P(llegar al techo) | día de llegada (p50) | ingreso del último año p10/p50/p90 (siempre) | techo teórico 73 fills |
|---|---|---|---|---|---|---|
| 0,03 | 19,59 | 0,82 / 0,00 (no opera) | 0,16 / 0 | 281 / — | 0 / 0 / 558 | 845 |
| 0,03 | 150 | 0,33 / 0,00 | 0,62 / 0,32 | 287 / 262 | −108 / 182 / 1.711 | 845 |
| 0,07 | 19,59 | **0,56 / 0,00 (no opera)** | 0,44 / 0 | 54 / — | 0 / 0 / 4.241 | 3.446 |
| 0,07 | 75 | 0,18 / 0,00 | 0,82 / 0,60 | 49 / 44 | 0 / 3.186 / 4.633 | 3.446 |
| 0,07 | 150 | 0,05 / 0,00 | 0,95 / 0,90 | 37 / 38 | 1.958 / 3.363 / 4.693 | 3.446 |
| 0,11 | 19,59 | 0,39 / 0,00 | 0,61 / 0 | 22 / — | 0 / 5.265 / 7.129 | 6.046 |
| 0,11 | 75 | 0,05 / 0,01 | 0,95 / 0,88 | 18 | 4.441 / 6.025 / 7.269 | 6.046 |
| 0,20 | 19,59 | 0,16 / 0,12 | 0,84 / 0,71 | 7 | 0 / 11.751 / 13.158 | 11.898 |
| 0,20 | 75 | 0,00 | 1,00 | 4 | 10.709 / 11.946 / 13.265 | 11.898 |
(Con 130 posiciones/día los techos son 1,8× mayores: 6,1 k€ a EV 0,07, 21 k€ a 0,20; la tabla completa de 64 escenarios está en `parteC.json::reinversion`.)
- Con la ley del pago de B (σ²·DEFF≈6) y 19,59 $, la política «operar siempre» tiene probabilidad de ruina 56 % incluso con +0,07 verdadero: **la tanda de 5 $ y el stake mínimo de 1,05 $ no son Kelly sino un sobre-apalancamiento de 4-9×** (ratifica `tandas/INFORME.md` §3 y ADENDA §2). La «guardia» (no operar si el log-crecimiento esperado es negativo) con 19,59 $ implica no operar nunca hasta tener ≥45-180 $: sin recarga no hay trayectoria autofinanciada.
- **Retirada (palanca de caja, no de EV):** una vez alcanzado el techo de profundidad (W\*=2,44/(½f\*): 146 $ a EV 0,20, 266 $ a 0,11, 418 $ a 0,07, 976 $ a 0,03) el capital excedente no puede desplegarse (el libro no absorbe más de ≈2,44 $/relleno sin deterioro): retirar lo que supere W\* no cuesta EV y baja la cola de ruina. Antes de llegar, retirar frena el compounding.

## 5. Waterfall hacia 200.000 €/año (por columna de evidencia)
| Fuente | VALIDATED | FORWARD/EXPLORATORY | SCENARIO | Nota |
|---|---|---|---|---|
| Beneficio validado de la familia | 0 | | | sin gate superado |
| B maker 5m ETH/SOL/XRP tal como opera (EV −0,068, 201 pos.) | | 0 (EV<0; IC90 días −0,39..+0,37) | | ningún gate; 3 días completos |
| Esta ola: reglas de salida de curva (14) | | 0 (ninguna crea EV; Wald) | | solo varianza/camino |
| Retirada / reinversión por tramos | | | 0 de EV; evita ruina si hay capital ≥75-150 $ | decisión de Javi |
| R3 en el nicho (ADENDA 22-Oct §2, no recalculado) | | | 2,4-6,1 k€ (base) / 10,8 k€ (optimista) | techo K=20, EV +0,07/+0,11 supuesto |
| Total contado | **0** | **0** | **≤ ≈11 k€/año** | |
| **Hueco restante hacia 200.000 €** | | | **≥ 189 k€/año** | no lo cierra B/alts con salida ni con reinversión |
Qué cerraría el hueco (variable, no regla de salida): (i) un EV **neto ≥ +0,20 por € sostenido y demostrado con IC90 por días >0** sobre (ii) ≥1.100 fills/día de 2,44 $ o stakes 80-230 $ por relleno que el libro 5m barato no soporta (techo medido K=20; K=50 rompe −0,066), o (iii) otra clase de subestrategia con profundidad (V7/V6 de la cartera, fuera de esta ola). Evidencia necesaria: ≥10-20 días de IC90 por cierre/día >0 con EV pond ≥+0,05 en B real o en el brazo shadow R3 (gate G1 de 40 ejecutables), antes de modelar nada con reinversión.

## 6. Candidata y modo pasivo
**Regla candidata: NINGUNA.** Razones: (a) Wald: ΔPnL = e·Δcoste, (b) estructura temporal no replicada entre fuentes (DL momentum +0,011, DP/B signo contrario y no significativo), (c) las que reducen drawdown cuestan 20-85 % del PnL con e=+0,05, (d) el único p de placebo <0,01 (TPd6, 0,007) no pasa Bonferroni y se revierte en DP.
**Modo pasivo ya montado (sin tocar B):** `scripts/pasivo.py` recalcula las 14 reglas + R0 sobre cada día real de B (`posiciones.csv`) en dos entornos (S_real, S_H0) y añade una fila por (regla, día) a `/root/polymarket-research-datalogs/x_salida/pasivo.csv` (primera corrida 09:22Z: 120 filas). Sin cron (lo decide la sesión principal). **Gate para promover una regla a candidata** (todo a la vez, fijado ahora): (1) ≥20 días de DP o B (hoy 6 y 4) en los que S1-S4 de la parte A, repetidos, den el mismo signo y p Bonferroni <0,05 en DP y en DL y **no** contradigan a B; (2) en pseudo-B de DP Δ_est>0 con IC90 por días >0 y p <0,05/14 para esa regla; (3) pérdida ≤10 % del PnL con e=+0,05 y ΔEV retenido ≥0; (4) ≥10 días en pasivo con ΔPnL real de B >0. Hoy cumple (1)=no, (2)=no, (3)=solo las reglas que no recortan, (4) sin datos. Si alguna se acerca, se prerregistra una versión nueva (nuevo sha) y se vuelve a medir hacia delante; no se retoca esta.
**Lo que sí vale la pena hacer con el mismo esfuerzo:** decidir capital (recarga o no) y medir EV por cierre/día con IC antes de diseñar salida: sin EV positivo demostrado, ninguna curva de salida produce euros.

## 7. Límites y desviaciones declaradas
- Desviaciones del PREREG: permutaciones DL 2.000 (no 5.000); E-P 300 trayectorias × 6 días-fuente (1.800) en lugar de 3.000; E-S 1.500 (no 2.000); placebo E-B 2.000; entorno `S_H0` y tabla g/dd (`xs_g.py`) son POST-HOC; la regla «SIN» (sin ninguna regla) quedó fuera porque con Bd=∞ el simulador no arranca y R0 es la línea base; la prueba de humo de DB falló a primera con una conversión de fechas (todo caía en 1970), corregida antes de calcular.
- Primera corrida de la parte C descartada: muestreaba cierres enteros de DP (≈18 unidades, DEFF 11) en lugar de pseudo-B de 1,8 unidades; reejecutada con el pool pseudo-B (σ²·DEFF 6,0).
- EV de DL es de precio de modelo; DP excluye rellenos de B; el pseudo-B no reproduce cola/repegs de B y su EV (+0,12/+0,15) refleja las horas 06-12 UTC; la posición abierta de la tanda 28 no está incluida; B real son 4 días (3 completos): ninguna conclusión sobre B es de gate.
- El simulador ignora solapes entre cierres consecutivos (posiciones de 5 m resueltas antes del siguiente), la comisión (maker sin comisión y sin rebate) y las fricciones de stake mínimo del exchange (5 acc) salvo el mínimo 1,05 $.
- Multiplicidad: 14 reglas × 3 entornos × 3 métricas se miran; los p sin corregir de §3.1 son descriptivos. $ no convertidos a €.

## 8. Reproducir
`cd experimentos/5m_barato/b_perdidas_22oct/x_salida; for s in xs_data xs_a xs_b xs_c xs_g; do (ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I scripts/$s.py); done` (≈12 min en total; `xs_b` ≈10 min, 1 proceso). Semillas 20261023-20261025/777. Salidas: `parteA.json`, `parteB.json`, `parteC.json`, `parteG.json` (copias aquí; originales y pickles en datalogs).
