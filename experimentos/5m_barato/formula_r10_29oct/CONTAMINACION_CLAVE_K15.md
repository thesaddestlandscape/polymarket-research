# Contaminación por clave k15 vieja — auditoría de R7/R8/R9 (29-Oct-2026, solo lectura)
Hecho: `kstart` de `k15/k_*.npz` = CIERRE del 15m. Clave vieja `(cie-300)//900*900` = cierre del 15m ANTERIOR (ya resuelto, bid ~0,97/0,03). Correcta: `+900`. Los ficheros k15 NO hay que reconstruirlos: basta la clave (ya corregida solo en `formula_r10_29oct/r10_build.py:60`).
Consumidores de la clave vieja (únicos): `formula_r7_28oct/r7a.py:45` (def bid15, FEATS[11]=m15 en :17), `formula_r8_28oct/r8h_build.py:59` (cols bid15/m15/dbid15 en :8,:66; escribe `hz_BTC.npz`), `formula_r9_28oct/r9fwd.py:24,28` (usa r7_15m + parche de texto de la línea vieja de r8h_build).
Verificado SIN clave vieja: R1-R6 (R2 `sim2.py:51` y R3 `feat3.py:47` usan e15 = ceil(cie/900)*900 = cierre = CORRECTO), `r8L/r8x/r8x2/r8x3/r8c/r8c_eth/r8_eth_ext/r9d/r9e/r7c/r7d/r7_simc` (grep 0 de bid15/m15 salvo lo indicado).
ETH: `r8h_build.py:13-18` solo carga k15 si coin=='BTC' => bid15/m15/dbid15 todo-NaN en ETH (`r8h_an_eth.py` los ignora; informe R8 incidencia 1). ETH NO usa k15 => INTACTA.

## Tabla (conclusión -> usa rasgo -> consecuencia). Tipo: NEG = negativa (un rasgo sin info podría haberla causado)
| # | Ronda / conclusión (cifra) | Fichero:línea | Rasgo | Consecuencia |
|---|---|---|---|---|
| 1 | R8 B2 hazard Y10 AUC OOS 0,684 [0,672,0,694], Y5 0,702, Y4 0,667, lift 4,8x, skill +0,037 | r8h_an.py:12,15,26-30 (F_ con las 30 cols; HGB y logit) | SÍ (3 de 30 cols) | INVÁLIDA como cifra citable; A REPETIR con hz R10 (probable cambio pequeño; T_rem sigue siendo rasgo principal) |
| 2 | R8 B2 política cotizar bb-m si hazard>=q: elegida OOS -0,217 2/10 REJECTED (NEG) | r8h_an.py (score) | SÍ | A REPETIR con +900 |
| 3 | R8 B2 comparadores ORÁCULO -0,281 0/10, SIEMPRE -0,150, ALEATORIO -0,104; "saber que viene el barrido y estar bb-1..-3 PIERDE" | r8h_an.py (oráculo usa barrido real, no score) | NO | INTACTA. Es cota superior de CUALQUIER predictor de llegada: "hazard alto no da dinero" no depende del rasgo |
| 4 | R8 B2 INVERSIÓN HGB (hazard bajo) OOS +0,695 9/10 (61 €/d) | r8h_an.py | SÍ | INVÁLIDA (cifra); es el hilo vivo => repetir en R10 |
| 5 | R8 T_rem (48 políticas T_rem x hazard x m) elegida OOS -0,134, logit INVERSIÓN -0,083 REJECTED (NEG) | r8T.py:8,10 (hz_BTC.npz; prep incluye bid15) | SÍ | A REPETIR con hz R10 (barata, mismo script) |
| 6 | R8 "Nada CANDIDATE" global | — | parcial | Se mantiene para tomador/maker reactiva/colocación/brecha (INTACTAS); lo dependiente del hazard (#2,#4,#5) queda abierto hasta R10 |
| 7 | R8 Bloque 1/1b/1c reloj R6 (artefacto +0,274; D_now OOS +0,349; causal +0,365) | r8x.py, r8L.py, r8x3.py | NO | INTACTA |
| 8 | R8-L1RETRASO (b) tomador t+215 ms +0,048 REJECTED; (a) maker bb_corr -0,314 REJECTED; (c) clasificador del retraso AUC 0,687 + oráculo invertido REJECTED | r8L.py (10 rasgos sin m15) | NO | INTACTA (aviso: su AUC 0,687 se parece al 0,684 pero es otro modelo) |
| 9 | R8 Bloque 3 brecha real-sim +0,135 [+0,012,+0,258]; Bloque 4 colocación W5-60 etc. REJECTED | r8c.py | NO | INTACTA |
| 10 | R8 Bloque 5 ETH: hazard AUC 0,607, política -0,195, inversión -0,754, T_rem ETH, celda T120-200 +1,018 | r8h_an_eth.py, r8c_eth.py, r8T.py ETH | NO (cols NaN) | INTACTA |
| 11 | R7 A puja profunda armada (6 variantes, OOS -0,151), A2 velocidad, placebo | r7a.py/r7d.py (sin m15 en la regla) | NO | INTACTA |
| 12 | R7 A covariable margen15 = bid15(s)-objetivo "no discrimina" (NEG: ≤0 -0,146 vs >0,10 -0,145) | r7a.py:158-159 | SÍ | A REPETIR con +900 (ahora el rasgo es informativo: corr(bid15,bb) +0,26/+0,48) |
| 13 | R7 B predictor: Y1 AUC 0,654/0,662, Y2 0,623/0,596, cancelación tardía AUC 0,598 ahorro 0 € (NEG) | r7a.py:17,83,164-166 (FEATS[11]=m15 + flag NaN) | SÍ (1 de 17) | A REPETIR con +900 (la cota oráculo 39,7 k€ no depende) |
| 14 | R7 C brecha de ejecución 8-11 pp (v258 re-ejecutada) | r7c.py, r7_simc.py | NO | INTACTA |
| 15 | R7 D dosis-respuesta; "relleno DENTRO del barrido" y mecanismo M1 "ya estar en el libro" (+0,242/+0,108/+0,567) | r7d.py (importa r7a, no usa m15) | NO | INTACTA (M1 sigue vivo, no depende de k15) |
| 16 | R9 E2 hazard bajo HGB BTC IS +0,504/OOS +0,695/DEV +1,268, 20/22 días, concentración T_rem 200-286, capacidad ~15 k€/año; modelo congelado `frozen_E2_hgb_BTC.pkl` sha 971a86f4 | r9c.py:25-32 (hz_BTC.npz) | SÍ | INVÁLIDA (cifra, capacidad, congelado). NO ejecutar `r9fwd.py` (construye con clave vieja, :24,:28). Sustituir por R10 (`r10_train/r10fwd`) |
| 17 | R9 E1 red de sobre-disparo bb-4..-6 + hazard alto: 18/18 negativas, elegida OOS -0,195 (NEG) | r9a.py:10,44-46 (logit con bid15 como score), comparadores SIEMPRE -0,173 / ORÁCULO -0,430 independientes | SÍ en la puerta q; NO en comparadores | A REPETIR (barata; la conclusión es robusta porque SIEMPRE y ORÁCULO ya son negativos). Reusar `fills_r9_BTC.npz` si el orden de filas es idéntico |
| 18 | R9 E3 rejilla de colocación 72 ventanas REJECTED | r9d.py | NO | INTACTA |
| 19 | R9 E4 brecha estricto/toque (solo-toque +0,14…+0,27) | r9a.py (parte E4, sin score) | NO | INTACTA |
| 20 | R9 E5 ETH T120-200 hazard bajo m=3 (+1,018, `frozen_E5_logit_ETH.pkl` 31f64a2a) EVIDENCE_INSUFFICIENT | r9c.py ETH (cols NaN) | NO | INTACTA |
| 21 | R9 E6 L1 ex-ante no anticipa el nivel de parada (NEG) | r9e.py:5-7 (solo bb, trem, bs) | NO | INTACTA |
| 22 | R9 "bandera de datos: bid15 mediana 0,97 => lado contrario" | — | — | RESUELTA: era el 15m anterior ya resuelto (clave), no el lado |
| 23 | Memorias 28/29-Oct (checkpoint_28oct_noche_R8:16, _R8_en_curso:11, 29oct_R9:14, pendientes_29oct:13) repiten AUC 0,684, ORÁCULO, INVERSIÓN, E2 | solo texto | — | Heredan #1,#4,#16 (INVÁLIDAS); #3 intacta |

Recuento (23 filas): INVÁLIDA 3 (#1 cifra AUC, #4, #16) + 1 heredada (#23); A REPETIR 5 (#2, #5, #12, #13, #17); INTACTA 14 (#3, #7-#11, #14, #15, #18-#22, y #6 en parte); sin dudosas abiertas salvo #6 (global, depende de #2/#4/#5). Negativas dependientes del rasgo que hay que repetir: #2, #5, #12, #13, #17. Negativas NO dependientes: #3 (oráculo), #7-#9, #11, #14, #15, #18-#21.
Nota: R9 E1 y R8 B2 dependían además de un OOS ya visto; R10 dejó explícito que solo el forward posterior al congelado es limpio.

## Cola de repeticiones (valor/coste, mayor primero)
1. R10 E2 BTC: `bash formula_r10_29oct/run_r10.sh` (build con +900 -> hz R10 -> train -> congelar -> HASHES con FECHA_CONGELADO; forward solo días > D con `r10fwd.py`). Valor máximo (único hilo vivo, juez forward), coste medio-alto (reconstruir 22 días de hz, pesado: fuera de 06-09Z, nice 19, ulimit). Sustituye al forward de r9fwd.
2. Con el hz R10 ya construido (coste solo análisis): `r8h_an.py` (AUC corregido; ¿aporta el 15m real al hazard?) + política q/m (#1, #2) + `r8T.py` (#5). Bajo coste, resuelve la afirmación "predecir llegada no da dinero" con rasgo correcto (el oráculo ya la limita).
3. R7 margen15 / predictor B (#12, #13): editar copia de `r7a.py` con +900 (en dev, sin tocar el original) y repetir solo B + covariable A. Medio-bajo coste; valor: el bid15 correcto es la señal central de v4 (bid15(s)-ask5(s)), puede aportar al filtro de armado.
4. R9 E1 (#17) con hz R10 (`r9a.py` con ruta nueva). Bajo valor esperado (comparadores ya negativos), bajo coste.
Nada que repetir: ETH, R7 A/C/D, R8 bloques 1/3/4/L1, R9 E3/E4/E5/E6.

## Pendiente (no resuelto)
- Desajuste 590/594: en `salida_r9c.txt:4` solo consta "721 rellenos en 590 (día,token)"; no he localizado el 594 (probable recuento de claves +900 casadas del auditor). No era barato de cerrar: dejarlo para el agente de R10 (contar `kmap.get(...+900)` frente a tokens, día 2026-10-20).
- No se ha verificado si `fills_r9_BTC.npz` conserva el mismo orden de filas que un hz R10 (asumir sí solo tras comprobar `di,u,t`).

## Repeticiones (29-Oct, agente R10; hz corregido +900, mismas filas/días/columnas que el hz R8; scripts copiados a rep/ sin tocar originales; salidas salida_r8h_BTC.txt, salida_r8T_BTC.txt, rep/log_*.txt)
Metodología R8 intacta (política elegida con IS, OOS=16-25, DEV=26-27, pesos por EUR "EVw", IC90 por días, sin2 = sin los 2 mejores días, comparadores SIEMPRE/ALEATORIO/ORACULO/INVERSION).
| Ítem | Antes (bid15 inválido) | Después (+900) |
|---|---|---|
| Hazard Y10 AUC OOS HGB | 0,684 [0,672,0,694] | 0,687 [0,677,0,696] (Y5 0,702->0,705; Y4 0,667->0,666; lift top1% 4,8x->4,9x; skill +0,037 igual) |
| Política hazard alto, elegida OOS | q.95 m3 -0,217 (2/10) | q.95 m2 EVw -0,219 [IC90 por días -0,313,-0,129] 0/10, sin2 -0,259; las 9 políticas negativas en OOS |
| ORACULO OOS | -0,281 0/10 | -0,277 0/10 |
| SIEMPRE / ALEATORIO OOS | -0,150 / -0,104 | -0,137 / -0,113 |
| INVERSION (hazard bajo) OOS | +0,695 [+0,359,+0,997] 9/10 sin2 +0,484 n721 | +0,345 [+0,114,+0,662] 8/10 sin2 +0,232 n682 (IS +0,386 8/10; DEV +0,504 2/2 IC cruza 0) |
| r8T elegida (T_rem x hazard x m) OOS | -0,134 | T60-120 medio m3 OOS ~-0,134 (p max 0,997); ALEATORIO misma banda -0,182 |
| r8T INVERSION logit OOS | -0,083 | -0,153 [-0,305,-0,019] 3/10 (HGB sí, logit no) |
Conclusiones: el AUC apenas cambia (el 15m real casi no aporta al hazard; trem manda, -0,55). "Predecir llegada del barrido" sigue sin dar dinero (ORACULO -0,277). Sobrevive solo la INVERSION HGB (la mitad de EV que con la clave vieja) y NO la logit: la señal es del modelo no lineal, no del hazard monótono. Mediana acc60 de los rellenos "bajo" 315 vs 1.728 en SIEMPRE: son libros tranquilos, más que "hazard".
OOS limpio: NINGUNO. La regla (hazard bajo, q05, m3, T_rem 200-286) se descubrió mirando el OOS 16-27 en R8/R9; el modelo R10 solo reentrena con IS 06-15. Único dato limpio = forward r10fwd desde 30-Oct.

## Tabla fina (29-Oct, agente R10; `rep/tabla_fina.py` -> `rep/salida_tabla_fina.txt`, log `rep/log_tabla.txt`; modelo sha 5e495915 sin tocar; hz con +900)
**(1) Incidencia "fill 88-139 %" = bug de INFORME de r8T/r8h (`summ()['nf']=mask.sum()` cuenta rellenos de los 22 días; el denominador `nk` es de la partición).** El EV no se ve afectado. Fill real HGB bajo: 1.824 órdenes, 735 rellenos (IS 41 %, OOS 39 %, DEV 39 %). Sí hay doble conteo real: varios rellenos por (día,token) (735 en 603). Contabilidad corregida B = 1 relleno por (día,token) (el más temprano); C = 1 por (día,mercado) es igual que B en OOS.
| INVERSIÓN HGB | IS 06-15 | OOS 16-27 (12 d) | OOS 16-25 |
|---|---|---|---|
| A órdenes (orig.) | +0,364 n473 9/10 | +0,350 n262 | +0,298 n211 8/10 |
| B 1/(día,token) | +0,358 n385 9/10 | +0,319 [+0,14,+0,48] n218 10/12 sin2 +0,23 | +0,264 [+0,07,+0,47] n171 8/10 sin2 +0,16 |
| T200-286, B | +0,437 n321 9/10 | +0,446 [+0,23,+0,66] n174 12/12 sin2 +0,31 | +0,436 [+0,18,+0,70] n131 10/10 |
El EV baja (T200-286 OOS16-25: +0,556 -> +0,436) pero sobrevive. SIEMPRE T200-286 (B): OOS -0,134 [-0,20,-0,07]; ALEATORIO por celda negativo.
**(2) Tabla fina** (tramos 20 s x banda de precio; 72 celdas): regla IS fijada (EV_IS>0, n_IS>=40, >=7/10 días +): pasan 6 celdas HGB (en realidad 3 tramos: 220-240, 240-260, 280-300; la sub-banda 0,22-0,29 es casi todo el tramo) y 2 SIN modelo (T220-240 y T240-260 p0,22-0,29; EV_IS +0,077/+0,014 con IC que cruza 0, OOS -0,20/-0,11: ruido). T200-220 HGB IS -0,095, T120-200 HGB IS -0,02/OOS -0,29 (NO genera). T280-300: OOS +0,39 pero IC cruza 0, sin2 +0,05 -> NO subregla. T260-280 no pasa la regla IS (6/10) aunque OOS +0,44. Con 72 celdas se esperan ~3-4 falsos positivos.
**(3) Reparto:** 102 % (IS) y 111 % (OOS) del PnL del HGB sale de T200-286; T120-200 aporta -13 % en OOS. Pero la regla "solo T_rem" no tiene valor: SIN modelo T200-286 -0,134 OOS, incluso con p<0,22 (-0,190) y con filtros triviales (acc60, bid15, tsl200 por cuartil IS: -0,09 a -0,24 OOS). dEV (HGB - SIN) en T200-286: IS +0,50 [+0,32,+0,68] 9/10; OOS +0,58 [+0,36,+0,81] 12/12. Conclusión: T_rem concentra DÓNDE dispara el HGB, el valor lo pone el modelo no lineal (la logit sale negativa); riesgo de sobreajuste al HGB persiste y el OOS 16-27 NO es limpio (regla elegida mirándolo). Único juez: forward desde 30-Oct.
**Uniones (B), E/d = pnl neto por día de calendario, IC90 por días, OOS 16-27:** HGB T220-260 IS +0,819 n157 9/10 | OOS +0,859 [+0,64,+1,09] n56 12/12 sin2 +0,73 +10,8 E/d [+7,9,+13,7] (IS +33,3 E/d). HGB T220-286 IS +0,551 n288 | OOS +0,523 [+0,32,+0,73] n161 12/12 sin2 +0,39 +18,6 E/d [+12,1,+25,1]. HGB T200-286 OOS +0,446 n174 +17,2 E/d [+10,0,+24,4]. HGB T240-286 OOS +0,484 n148 +15,8 E/d. HGB T260-286 IS +0,266 (5/10, IC cruza 0) OOS +0,454 n118 +11,7 E/d. (N=10 acc/orden; stake real de pruebas mucho menor.)

## Robustez (29-Oct, agente R10; `rep/robustez.py`..`robustez7.py`, salidas `rep/salida_robustez*.txt`, `rep/log_robustez*.txt`; modelo congelado sha 5e495915 sin tocar; todo entrenado SOLO en IS 06-15; OOS 16-27 solo reportado; contabilidad B = 1 relleno por (día,token); EVw = ponderado por EUR; IC90 por días)
**(1) Semillas e hiperparámetros** (5 semillas con max_features=0,8; umbral = q05 de la predicción OOF del IS; OOS T200-286, 12 días):
| variante | OOS EVw media ± sd [min,max] | IS(OOF) ens. | walk-forward IS (3 folds, 6 días de test, T200-286) |
|---|---|---|---|
| base d5/hoja100/200 it | +0,60 ± 0,14 [+0,42,+0,76] | +0,47 | 6/6 semillas EV +0,56 a +0,83, 6/6 días + |
| reg1 d3/hoja300/150 it | +0,68 ± 0,15 [+0,46,+0,93] | +0,45 | +0,49 a +0,93 |
| reg2 d3, 8 hojas/hoja800 | +0,62 ± 0,39 [+0,07,+1,09] | +0,27 | +0,28 a +0,61 (una semilla IC cruza 0) |
| reg3 d2/hoja1000 | +0,39 ± 0,37 [-0,03,+0,95] | +0,10 (IC cruza 0) | +0,11 a +0,35 |
Ensemble de 5 semillas OOS T200-286: base +0,675 [+0,53,+0,88] n209; reg1 +0,733 [+0,58,+0,91] n172. Umbral q05 estable (sd 0,0001-0,0002). Lectura: con capacidad media (d3-d5) el efecto sale en TODAS las semillas (EV +0,42 a +0,93, IC90>0); con regularización fuerte se degrada y se vuelve inestable (selecciona distinto). La dispersión entre semillas (sd 0,14-0,15) es del mismo orden que el IC por días: reportar EV ~+0,4 a +0,7, no un punto.
**(2) Qué aprende el HGB.** Importancia por permutación (OOS, AUC cae): `trem` -0,079 (resto ≤ -0,015: acc30, acc60, np60, np5, bb, cbb). PDP: p(Y10) = 0,13 a trem 71 s, 0,047 a 121 s, 0,031-0,035 a 185-273 s: casi todo es «mucho tiempo restante → hazard bajo»; acc30/acc60 altos y cbb alto SUBEN el hazard; np60/bb altos lo bajan. Esto explica que SIN modelo la banda T200-286 sea -0,134: T_rem sola no genera valor.
Surrogate (árbol d3 sobre la selección del HGB, IS): bid15>0,51 & bb>0,23, o bid15>0,51 & bb≤0,23 & trem>240, o **bid15≤0,51 & cbb>0,66 & bb>0,28** (regla S3). S3 SIN modelo, T200-286, m=3: IS +0,605 [+0,51,+0,68] n1.043 10/10 d; OOS +0,451 [+0,35,+0,55] n1.221 12/12 sin2 +0,40 (+122 E/d, N=10 acc); complemento -0,281; ALEATORIO misma fracción -0,130; SIEMPRE -0,134; bid15 barajado por día -> IS +0,12 / OOS 0,00. Reglas con cortes de cuartiles del IS (acc60≤Q25; +np60; +spr; acc30≤Q25&np60≥Q50; margen bid15-bb) NO generan (OOS -0,22 a +0,15 salvo la última con cbb≤Q50, +2,0 n47: ver abajo, no fiable).
**ALERTA: toda la ganancia de S3 está en UNA hoja** (bid15≤0,51 & cbb>0,66 & bb>0,28): IS +1,20 n580, OOS +1,04 [+0,93,+1,14] n639, 12/12 días, hasta con bb-1c/-2c (fill 34 %/30 %). La otra rama de S3 (bid15>0,51) es NEGATIVA (-0,22 OOS). La hoja implica que el token a ~0,31 gana el 62-63 % (también las órdenes NO rellenadas: 0,616), frente a 0,30 en el mismo bucket de precio sin la condición; a cbb≤0,66 gana ~0,12. Eso es ≈ +0,9 €/€ incluso a un tomador: resultado espectacular = primero bug. Descartado: emparejamiento (mismo mercado, lado opuesto, 1-ca≈bb en 3 días), orden de `qt` por token (monótono en 576 tokens). NO descartado: causa (81 % de los rellenos OOS vienen de prints del lado complementario; los cbb 0,66-0,72 con bb 0,28-0,35 son estados «bb+cbb≈0,97-0,99»). Antes de congelar: replicar con el ask real/libro_snapshots y con un tomador a 215 ms, y auditar cómo se construye `cbb` (r10_build.py l.54) frente a un 'ya lo sabía el libro' (qt retrasado/receipt).
**(3) Regímenes (cortes IS de filas T200-286; HGB-bajo dentro del régimen; OOS 16-27)** — SIEMPRE negativo en todos (OOS -0,10 a -0,24):
| régimen | HGB-bajo IS | HGB-bajo OOS | veredicto |
|---|---|---|---|
| acc60 Q1 (muy tranquilo) | +0,36 n188 | +0,50 [+0,09,+0,93] n99 | rentable, IC ancho |
| acc60 Q2-Q3 | +0,71 n157 | +0,38 [+0,07,+0,64] n92 | rentable |
| acc60 Q4 (agitado) | +0,45 n27 | +0,72 n9 | n<40, no concluye |
| spr ≤Q50 (96 % de filas) | +0,41 n313 | +0,46 [+0,25,+0,66] n168 | = el HGB entero |
| spr >Q50 (ancho) | +1,24 n21 | +0,21 n17 | n<40 |
| bid15 ≥Q75 | +0,21 n198 (IC cruza 0) | +0,32 [+0,05,+0,62] n131 | débil |
| bid15 <Q75 | +0,83 n127 | +0,82 [+0,13,+1,62] n43 | rentable, n justo |
| np60 ≥Q50 (activo) | +0,59 n82 | +0,99 [+0,43,+1,57] n43 | rentable |
| np60 <Q50 | +0,41 n267 | +0,43 [+0,22,+0,74] n149 | rentable |
| tranquilo (acc60≤Q50 & spr≤Q50) | +0,39 n263 | +0,47 [+0,29,+0,71] n143 12/12 | rentable |
| tranquilo & bid15≥Q50 | +0,31 n210 | +0,43 [+0,24,+0,70] n126 | rentable |
Los regímenes del HGB NO se separan limpiamente por un solo rasgo: el valor es del modelo (o de S3-hoja), no de un régimen simple. Candidatas dry-run (sin dinero real; N/A mientras no se audite la hoja): (a) HGB-ensemble reg1 q05, T200-286, maker bb-3c, vida 10 s, una orden por token; (b) hoja S3 con bb-1c (fill mayor), mismo tope de vida; sin cancelación probada. Gate de ambas: forward desde 30-Oct (n≥40, ≥10 días, IC90 días>0, sin2>0, vs SIEMPRE/ALEATORIO).

## Auditoría hoja S3 (29-Oct, QA independiente; `rep/audit_s3.py` -> `rep/salida_audit_s3.txt`, `rep/audit_s3b.py` -> `rep/salida_audit_s3b.txt`/`rep/log_audit_s3b.txt`; solo lectura, modelo sha 5e495915 sin tocar)
**Veredicto: LOOK-AHEAD (fuga por AUSENCIA).** `r10_build.py:22-27` construye `S[u]` con `D.stream(u)` = TODOS los prints del token en la ventana (incl. los POSTERIORES a t); `:50-55` pone `cbb, dcbb1, dcbb5, comp_acc5 = NaN` si el stream del complementario está vacío en TODA la ventana (`sc is None`), aunque su L1 exista en t. Los prints guardados son solo SELL<=0,32 / BUY>=0,68 (`formula_r5_28oct/r5.py:57`): que el complementario c llegue a venderse <=0,32 (o u a comprarse >=0,68) en el resto de la ventana es casi "u gana".
- T200-286, bb>0,28: cbb NaN en 50,3 % de filas, **y|NaN = 0,0000 (n=28.845)**, y|finito = 0,623 (n=28.451); igual en todas las bandas de bb (y|NaN 0,000). NaN <=> stream(comp) vacío en toda la ventana: 100 % (n=57.250 con L1 causal existente). Etiquetas OK (y+y_comp=1 100 %; libro final coincide 99,95 %). bb y bid15 (+900) reproducen al 100 %; el orden de qt y el emparejamiento no son la causa.
- `cbb>0,66` en la hoja = "cbb no NaN" = futuro. Con cbb CAUSAL (L1 del complementario en t+L), la hoja pasa de y 0,628 a **y 0,303 con ask 0,317** (n=20.941 filas, 3.848 tokens).
- TOMADOR ask t0+215 ms, fee 0,07p(1-p), 1/(día,token): hoja hz (con fuga) OOS +0,805; **hoja causal OOS −0,082 [−0,17,−0,01] 2/12 días**, IS −0,005; con rasgos retrasados 1-3 s OOS −0,075..−0,086 (no hay efecto de ms, la fuga es de minutos).
- MAKER relleno estricto, hoja causal: bb-1c OOS −0,106 [−0,21,−0,01] 3/12 (rellenos y 0,255 vs precio 0,285; no rellenadas 0,359); bb-3c OOS −0,120 [−0,22,−0,04]. Selección adversa normal, sin edge.
- Multiplicidad (volteo de signos por días, B=20.000, 74 tests OOS): sobreviven max-T p<0,05 HGB T220-240 (0,036) y unión T220-286 (0,040); T200-286 0,078; T240-260 0,32; T280-300 0,98. BH q<0,10: T220-240, T240-260, T220-286, T200-286. **Irrelevante: el score del HGB usa las 4 columnas con fuga** (contaminación cuantificada en `rep/salida_audit_s3b.txt` §3).
- Consecuencia: INVÁLIDAS las cifras R10 que usan hz con cbb/dcbb/comp_acc5 (INVERSIÓN HGB +0,345, tabla fina, uniones, robustez, S3, candidatas dry-run (a)/(b)) y, por la misma construcción, R8 B2/R9 E2 (`r8h_build.py` idéntico). El forward `r10fwd.py` hereda la fuga si construye igual. Reparación mínima: calcular rasgos del complementario solo con datos <= t (cbb = L1 de c en t, comp_acc5 = 0 si no hay prints antes de t), reconstruir hz y reentrenar; auditar cualquier `S.get(...) is None` / NaN por ausencia.
- §3 contaminación del HGB congelado: sus rellenos tienen cbb NaN 42,4 % (T200-286) frente a 60,2 % en SIEMPRE, y TODO rellenado con cbb NaN pierde (EVw −1,000 en todos los días). Esa diferencia de proporción ES la "INVERSIÓN" +0,446. Con las 4 columnas a NaN para todos (sin fuga, umbral original): OOS −0,118 [−0,39,+0,20] 4/12 días; T200-286 OOS −0,079 [−0,45,+0,26]; IS −0,30/−0,31. HGB REENTRENADO en IS sin las 4 columnas (q05 OOF): todas las T OOS −0,119 [−0,27,+0,05] 4/12 (IS −0,099); T200-286 OOS −0,066 [−0,29,+0,15] 4/12 (IS −0,144). R10 E2 = REJECTED hasta reconstruir hz de forma causal.

## (A) Barrido del patrón «rasgo = NaN/valor por AUSENCIA en toda la ventana» (29-Oct, agente R10c; solo lectura; test reutilizable `causal/test_nan_predice_y.py`)
Patrón: rasgo en t calculado con `D.stream(u)`/prints de TODA la ventana (incluye futuro) y NaN o centinela si no hay ninguno. Causa de la fuga R10: `sc = S.get(c)` (stream del complementario completo) -> `comp_acc5/cbb/dcbb1/dcbb5 = NaN` si no hay NINGÚN print en la ventana (`r10_build.py:50-55`, `r8h_build.py:50-54` idéntico).
**Test automático** (`python3 causal/test_nan_predice_y.py hz.npz --strat bb --filas "(trem>=15)&(trem<286)"`): por rasgo, y|NaN vs y|finito, versión a nivel token, consistencia por días, dif. por estratos de bb, y tabla MODA (centinelas 0/300000). Sale 1 si hay FUGA_PROBABLE (|dif|>=0,10, n>=200, mismo signo >=80 % de los días). Resultado sobre los hz EXISTENTES (22 días, T15-286): **R8 BTC `hz_BTC.npz`: comp_acc5, cbb, dcbb1, dcbb5 NaN 52,0 %, y|NaN=0,0000 vs 0,479, dif −0,479, 22/22 días, SATURADO; R8 ETH: idem NaN 53,9 %, y|NaN 0,0000 vs 0,507 (22/22)**; R10 BTC (T200-286, bb>0,28): NaN 50,3 %, y|NaN 0,0000 vs 0,623, 22/22. Los 4 rasgos son el único NaN con señal; el resto de NaN (dbb1, bid15 ~0,03 %) <200 filas. La tabla MODA además marca `comp_acc5=0` (99 % de filas, y 0,48 vs 0,23: la rama «finito» es la que tenía el futuro) y acc5/np5/acc60/np60=0 (+0,10 en ETH/BTC, verosímilmente causal: «sin flujo vendedor» es información real; revisar, no es fuga probada).
| Constructor / consumidor | fichero:línea | ¿Afectado? | Qué conclusión depende |
|---|---|---|---|
| hz R8 BTC/ETH (build) | `formula_r8_28oct/r8h_build.py:22-27,50-55` | **SÍ** (NaN-si-no-hay-prints; test: 22/22 días, y\|NaN=0) | R8 B2 (hazard AUC 0,684, política hazard alto, INVERSIÓN +0,695), r8T (T_rem×hazard), ETH hz |
| hz R10 (build) | `formula_r10_29oct/r10_build.py:22-27,50-55` | **SÍ** (misma) | INVERSIÓN HGB +0,345/+0,446, tabla fina, uniones, robustez, hoja S3, candidatas dry-run (a)/(b), modelo sha 5e495915 |
| consumidores del hz | `r8h_an.py`, `r8h_an_eth.py:15`, `r8T.py`, `r10_train.py`, `rep/*` | **SÍ** (heredan columnas) | idem; `prep()` añade `isnan(cbb,comp_acc5)` como indicador explícito -> la fuga entra por 2 vías |
| R9 E1/E2/E4 | `r9a.py:32,44` (stream completo para MN de relleno = etiqueta, legítimo; `prep()` con flags isnan(cbb/comp_acc5)) , `r9c.py:46`, `fills_r9_BTC.npz` | **SÍ** vía rasgos (el MN de rellenos es resultado, no rasgo) | R9 E1 (logit hz), E2 (INVERSIÓN), comparadores logit |
| forward R9/R10 | `r9fwd.py:19-41` y `r10fwd.py:29-45` (ejecutan `r8h_build`/`r10_build` por `exec`) | **SÍ**: construyen el mismo rasgo con el stream del día completo; en forward el futuro está disponible al reconstruir el día, no en vivo | `r10fwd.py` desde 30-Oct heredaría la fuga: NO usar hasta apuntarlo a `causal/r10c_build.py` |
| `r8x.py:13` (ctx2/ctx8) | `tot[cid] >= 200/800` = tamaño FINAL del cluster como contexto de cada print | DUDOSO (análisis descriptivo «qué pasa dentro de racimos grandes»; si se usara como filtro de regla sería futuro) | R8 B1/B3 retrospectivos; revisar si alguna conclusión de regla lo usa |
| `r8x2.py:10`, `r8x3.py:11`, `r8L.py:14` | `r8L`: `X8 = cum[i] >= 800` (acumulado causal); `r8x3/r8x2`: L1 en st−5 ms | NO | R8 L1-retraso, T_rem (no usan NaN por ausencia) |
| `r7a.py` (R7 B/C) | `:66,110` `clu[u]=(st, cend[tot>=100])` (cierre de cluster con total final) y `cb=q1(c,td)` (L1 del complementario en td) | cbb: **NO** (L1 causal en td; NaN = sin L1 a esa hora, no futuro). `clu`: DUDOSO-leve (fin de cluster conocido con +300 ms) | R7 predictor B/margen15 (además bid15 sin +900: ya invalidado aparte) |
| `r6x.py:61,89` | cbb/cba por L1 del par en el instante | NO | R6 colocación |
| `r5.py:57` (awk de prints) | filtra SELL<=0,32/BUY>=0,68 por precio del print (no futuro) | NO por sí mismo, PERO es la causa de que el stream vacío ≡ «u nunca se pagó ≥0,68» | cualquier rasgo derivado del stream de un token con «vacío = NaN/0» |
| `n800_60`, `coin_n60`, `tsl200/800` en hz | usan `tot` FINAL del cluster (puede incluir prints > t) y `cst` (inicio) | DUDOSO-leve (cluster grande aún abierto en t cuenta como grande) | corregido en `r10c_build.py` (cluster cerrado = fin+300 ms ≤ t) |
| Vigías congelados v4/V2-V7/FV v4, F2 (`vigia_5m_barato_forward.py:169,212-267,405`, `f2_5m_barato_dryrun.py:233,254-352`, `run_m5barato_forward_diario.sh`) | rasgos = L1 y bid15/ask5 en el instante de decisión; `None` = «sin cotización en ese momento» (se cuenta como no ejecutable, `unk`) | **NO** (no usan streams de ventana completa; el NaN no deriva del futuro). Residual: unidades con desenlace desconocido (`unk`) se excluyen -> vigilar supervivencia, ya cubierto por G-gates | gates G1-G10 de v4 |
| H5M `vigia_5m_barato_maker_forward.py:44-82` | unidad = rellenos on-chain ex-post; «final de la cola» (rank en la tx) es ex-post por diseño | DUDOSO (no es regla causal sino observación; ya anotado «aproximación» y trampa media por unidad) | gate G6 final-cola |
Conclusión (A): la fuga está en TODO lo derivado del hz R8/R10 (BTC y ETH); los vigías congelados y F2 no usan este patrón. Pendiente de higiene: `r10fwd.py`/`r9fwd.py` apuntan al build con fuga.

## (B) Reconstrucción CAUSAL del hz BTC y reentreno (29-Oct, agente R10c; `causal/r10c_build.py` -> `causal/hz_BTC.npz`; `causal/r10c_analysis.py` -> `causal/salida_r10c_analysis.txt`, `log_analysis.txt`; build 12:17-13:09Z, mismas 337.226 filas y 22 días que el hz R10; originales y modelo sha 5e495915 sin tocar)
Cambios de `r10c_build.py` frente a `r10_build.py` (copia, no se editó el original): (1) rasgos del complementario solo con datos <= t: `cbb/dcbb1/dcbb5` = L1 del complementario en t (NaN solo si ese token aún no tiene L1 conocido), `comp_acc5` = 0 y `comp_tsl`=300000 explícitos si no hay prints antes de t (no NaN por futuro); (2) clusters grandes (`tsl200/800`, `n800_60`, `coin_n60`) solo cuando YA están cerrados (fin+300 ms <= t); los inicios `B8` solo para etiquetas; (3) columnas extra del complementario (cba, cspr, cbs, dcba1/5, comp_tsl, comp_np5, sumb, suma, c_exist) y `a215` = ask propio a t+215 ms (solo para evaluar, no es rasgo).
**Test NaN-predice-y sobre el hz causal** (`causal/salida_test_nan_causal.txt`, 40 columnas, T15-286): NINGÚN NaN predice y (los 4 rasgos ya no tienen 50 % de NaN). Única marca: tabla MODA acc5/np5 = 0 (7,8 % de filas, y 0,329 vs 0,222, 22/22 días): se calcula con prints <= t (`wsum` causal), «u sin flujo vendedor en 5 s» es información legítima (estaba igual en el hz con fuga); no es fuga por ausencia.
**Reentreno** (misma familia HGB d5/hoja100/200 it, 30 columnas núcleo, Y10, Platt, umbral q05 del OOF del IS 06-15, regla INVERSIÓN m=3 vida 10 s relleno estricto, 1 relleno por (día,token), EVw ponderado por €, IC90 por días; OOS = 16-27, 12 días). AUC Y10: IS(OOF) 0,686 / OOS 0,688 (el AUC no cambia: el hazard se predice igual, pero ya no hay «dinero» escondido). Nota de informe: la `n` impresa en cada línea es el total de rellenos IS+OOS (misma incidencia de informe ya anotada en r8T; el EV no se ve afectado).
| Política (causal) | IS 06-15 (OOF) | OOS 16-27 |
|---|---|---|
| HGB-bajo q05, todas T | −0,232 [−0,403,−0,101] 1/10 d | **−0,107 [−0,252,+0,031] 5/12 d**, sin2 −0,182 |
| HGB-bajo q05, T200-286 | −0,223 [−0,385,−0,072] 2/10 | **−0,075 [−0,246,+0,089] 5/12**, sin2 −0,175 |
| SIEMPRE (todas) / T200-286 | −0,068 / −0,041 | −0,120 [−0,170,−0,074] 2/12 / −0,134 [−0,201,−0,067] 2/12 |
| ALEATORIO misma fracción (20 semillas) | — | −0,151 (rango −0,366…−0,004) |
| logit-bajo q05 (todas / T200-286) | −0,047 / −0,047 | −0,108 [−0,205,−0,010] 3/12 / −0,105 [−0,204,−0,004] 3/12 |
| HGB-ALTO q95 (cola contraria) | −0,083 | −0,207 [−0,304,−0,122] 1/12 |
Comparación: con el hz con fuga la misma regla daba OOS +0,446 (T200-286); con el hz causal −0,075: la «INVERSIÓN» desaparece (el HGB-bajo causal ni siquiera gana en IS). No supera SIEMPRE ni ALEATORIO de forma significativa (IC cruza 0 y está dentro del rango de ALEATORIO); gate G (IC90 días>0, sin2>0) NO se cumple. **R10 E2 / hazard BTC = REJECTED por reconstrucción causal.**

## (C) Ingeniería inversa de la fuga: ¿se anticipa «el complementario deja de cotizar barato» con L1 en t? (29-Oct; mismo script `causal/r10c_analysis.py`; modelos ajustados SOLO con IS 06-15, margen fijado de antemano {0,05, 0,10, 0,15}; EV al ask real a t0+215 ms con fee 0,07p(1−p) (tomador) y rellenos estrictos bb−1c/bb−3c (maker, sin rebate); 1 por (día,token); EVw; IC90 por días)
Modelos: BASE (bb, spr, bs, trem), CX logit (+ dbb1/5, cbb, dcbb1/5, cba, cspr, cbs, dcba1/5, bb+cbb, ba+cba + indicadores de L1 ausente), CX HGB d3/hoja300/100 it. **Calibración OOS: Brier BASE 0,1672, CX logit 0,1673, CX HGB 0,1674 frente al mid-bb 0,1670; AUC OOS 0,631 / 0,631 / 0,630; corr(p̂,y) 0,188/0,188/0,187.** El L1 del complementario y su velocidad (1-5 s), spread, profundidad y suma de libros NO añaden información sobre el resultado al precio propio (la fuga era 100 % futuro, no información en t).
| Celda | OOS 16-27 EVw [IC90 días] días+ (n) |
|---|---|
| Tomador BASE m0,05 / m0,10 / m0,15 | −0,081 [−0,214,+0,043] 4/12 (1.389) / −0,268 (156) / −0,150 (46) |
| Tomador CX logit m0,05 / 0,10 / 0,15 | −0,199 [−0,342,−0,080] 2/12 (1.279) / −0,117 (143, IC cruza 0) / −0,263 (38) |
| Tomador CX HGB m0,05 / 0,10 / 0,15 | −0,063 [−0,228,+0,046] 4/12 (1.678) / −0,010 (103, IC −0,63,+0,48) / +0,566 (19, n<40, sin2 −0,36) |
| Maker CX logit bb−1c m0,05 / 0,10 | −0,086 [−0,160,−0,006] / −0,233 (118) |
| Maker CX HGB bb−1c m0,10 (IS +0,341 7/10) | **+0,024 [−0,164,+0,266] 7/12 sin2 −0,053 n318** |
| Maker CX HGB bb−3c m0,10 (IS +0,302 9/10) | −0,021 [−0,186,+0,136] 6/12 sin2 −0,109 n922 |
Placebo (p̂ del CX logit permutado dentro de cada día, 400 permutaciones, estadístico = máximo de EVw OOS sobre los 3 márgenes): real −0,117, placebo media −0,109, p95 −0,097, p = 0,887. Las dos celdas maker con IS bueno (HGB, margen 0,10) se pierden fuera de muestra (de +0,34/+0,30 a +0,02/−0,02), patrón clásico de sobreajuste/IS-OOS. Multiplicidad: 24 celdas miradas; ninguna cumple n>=40, >=10 días, IC90 días>0 y sin2>0 a la vez (la única con EV OOS >+0,5 tiene n=19).
**Veredicto (C): NO existe señal causal explotable en el L1 del complementario.** Lo que la fuga contenía («el complementario llegará a venderse <=0,32») es el desenlace mismo, conocido solo después. Límite honesto: modelos simples y pre-especificados con 10 días de IS; no se probó el libro profundo (L2) ni el flujo de prints del complementario más allá de comp_acc5/comp_np5/comp_tsl (incluidos en el nucleo del HGB reentrenado, sin efecto).
Reproducción: `nice -n 19 ionice -c3 bash causal/run_c.sh` (build, ~52 min) y `python3 causal/r10c_analysis.py` (~25 min con carga); test: `python3 causal/test_nan_predice_y.py FICHERO.npz --strat bb --filas "(trem>=15)&(trem<286)"`.
Pendiente de higiene: `r10fwd.py`/`r9fwd.py` ejecutan el build con fuga; no instalar su cron; si se quiere forward de esta línea, apuntar a `causal/r10c_build.py`.
