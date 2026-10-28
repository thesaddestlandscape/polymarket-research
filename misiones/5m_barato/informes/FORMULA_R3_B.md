# FORMULA R3 (B): frontera de información de la compuerta ε + identidad del barrendero

Agente: polymarket-quantum-alpha-miner. Fecha: 2026-10-28 (prereg hasheado 10:56Z; ejecución 10:59Z-11:35Z). Continúa `FORMULA_R2_B.md`. No se autocertifica nada: la validación es de un validador/red-team independiente.
Expediente: `/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/` (prereg `PREREG_FORMULA_R3.md`, hashes `HASHES_R3.txt`, salidas `analysis_salida.txt`, `identity_salida.txt`, `identity_salida_exploratorio.txt`, `postsweep_salida.txt`).

## 0. Veredicto
**REJECTED** para la hipótesis «×10 de información» y para la familia pasiva L1/L2 como vía de información: el criterio pre-registrado da FALLO: el ΔLL central de M5 tiene el signo contrario al exigido (+1,2e-4 frente a ≤ −2,0e-3), el límite inferior de su IC90 por días (−1,17e-3) no llega al umbral y el mejor ΔLL de cualquier modelo y retardo (−3,4e-4) queda a 6× del umbral. **Logger L2: NO.** **Barrendero/«barrido final a favor»: INSUFFICIENT_EVIDENCE** (hipótesis candidata, no confirmada; prueba hacia delante barata en §8).

| Criterio (M5, LR 130 ms, OOS 23-26 Oct, 130.151 filas, 4 días) | Umbral | Medido |
|---|---|---|
| P1 σ_ε = desv. típica de q̂ − m130 | ≥ 2,6 pp | **1,33 pp** |
| P2 ΔLL = LL(q̂) − LL(m130), IC90 por días (t, gl 3) | ≤ −2,0e-3 y límite sup. < 0 | **+1,2e-4** [−1,17e-3; +1,42e-3] |
| P3 pendiente de calibración de (y−m) sobre ε̂ | ≥ 0,7 | **0,37** [−0,61; 1,34] |

Con la ε ampliada la información **calibrada** es ≈ 9e-5 nats/fila (pendiente² × ΔLL predicho: 0,37² × 6,4e-4 en OOS; 0,33² × 8,35e-4 en IS-CV), es decir σ efectiva ≈ 0,5 pp. La ε de R2 con coeficientes fijos (dos rasgos) da σ ≈ 0,64-0,71 pp y ΔLL −1,5e-4 (IS) / −2,6e-4 (OOS). Resultado: la información calibrada de M5 (σ efectiva ≈ 0,5 pp) no supera a la de la ε fija de R2 (σ efectiva ≈ 0,64 pp en IS, pendiente 1,01): ni ×10 ni mejora.

## 1. Mandato, lectura operativa y qué se verificó (datos, rangos, reloj)
- Lectura del mandato de Javi: «×10 de información» = σ_ε del orden de 3,1 pp (ΔLL ≈ 2,8e-3); umbral de éxito prerregistrado 2,6 pp (ΔLL ≤ −2,0e-3, IC90 por días < 0, pendiente de calibración ≥ 0,7). «Barrido final a favor» = un estado observable ANTES del relleno (identidad o cadencia del barrendero, barrido grande reciente) que ordene la selección adversa; la identidad on-chain llega ≥ 2,2 s después del casado, así que solo cuenta como etiqueta/atribución y nunca como rasgo en M1-M5.
- Filas = (token, tick de 2 s del reloj de RECEPCIÓN) elegibles de B (bb retrasado 130 ms ∈ [0,10; 0,29], spread ≥ 0,02, T ∈ [60; 290] s, sin TD Binance; elegibilidad de `alpha_miner_b_27oct/sim.py`). 22 días 2026-10-05..26: **578.309 filas, 576.595 con desenlace (99,70 %)**; IS 05-22 = 446.444 (18 días), OOS 23-26 = 130.151 (4 días). Por moneda: BTC 10.200, ETH 18.448, SOL 107.396, XRP 106.379, DOGE 154.699, BNB 179.473. FV15 disponible en el 85,5 % de las filas. Filas con relleno estricto a 2 s: 48.370 (8,4 %); primeros rellenos por mercado-token: 24.606 (OOS 4.754).
- Benchmark de toda métrica: m130 (mid del libro retrasado 130 ms). Etiqueta y = el token gana (`maker_ms_desenlaces_cache.json`).
- Rasgos (todos a t − LR, LR = 130/60/30 ms): B1 L1 recalibrado; B2 retornos Binance 0,2/1/5 s firmados (crudos y ×κ/√T); B3 flujo firmado de filas `t` (propio y complementario, 1/5/30 s, nº impresiones, última impresión, tiempo desde ella); B4 BTC 5m → alts (mid BTC YES de la ventana, cambios 1/5 s, retornos Binance BTC); B5 ΔFV15 a 1/5/30 s y momento propio del mid. Logística con offset, ridge fijo 1e-4, CV por días (6 grupos de 3) en IS; el OOS no se tocó para elegir nada.
- Pipeline: `feat3.py` (selftest 7/7 OK; 22 `FIN_DIA rc=0`; 22 ficheros `out/f_*.npz`), `analysis3.py`, `identity3.py`. Smoke en 2026-10-10 con `out_smoke` (solo prueba de código). Sin REHASH: ningún fichero hasheado cambió tras el prereg.
- Recursos: 2 trabajadores, nice 19, ionice -c3, ulimit 4,5/6 GB; load5 7,3 al cierre (uptime 11:34Z); guardas del chief: load1 < 14 y MemAvailable > 1,2 GB; fuera de 06:00-09:30Z. Sin órdenes, sin `.env`, sin crons, sin commits.

## 2. Mecanismo raíz: por qué falla
La información que el mid no contiene y que está disponible 130 ms antes del relleno es minúscula. Añadir bloques sube la dispersión BRUTA de las predicciones (0,91 → 1,33 pp de M1 a M5) pero la parte añadida es ruido: la pendiente de calibración cae de ≈ 1,0 (M0 en IS) a 0,33-0,37. El placebo de permutación confirma que los ajustes de M5 valen algo frente a ajustes aleatorios de igual tamaño (ΔLL +1,2e-4 frente a +5,1e-4 ± 0,7e-4, p = 0,005) pero su ruido cuesta más que su señal (neto peor que el mid). Evidencia: fuerte (IS-CV 18 días y OOS coinciden; no lineal y ridge coinciden).

| Modelo (LR 130) | σ_ε OOS | ΔLL OOS [IC90 días] | pendiente OOS | ΔLL IS-CV [IC90 18 días] |
|---|---|---|---|---|
| M0 ε de R2 fija (A2 0,026; A3 0,085) | 0,71 | −2,6e-4 [−7,5e-4; +2,2e-4] | 1,38 | −1,5e-4 [−2,95e-4; +2,7e-6] (pend. 1,01) |
| M1 L1 recalibrado | 0,91 | −2,9e-5 [−1,41e-3; +1,35e-3] | 0,47 | +5,4e-4 [−5,8e-5; +1,15e-3] |
| M2 +Binance | 1,01 | −4,9e-5 | 0,50 | |
| M3 +flujo firmado | 1,11 | +6,9e-5 | 0,39 | |
| M4 +BTC→alts | 1,16 | −1,6e-5 | 0,49 | |
| **M5 +multi-horizonte** | **1,33** | **+1,2e-4** [−1,17e-3; +1,42e-3] | **0,37** | **+4,8e-4** [−9,1e-5; +1,05e-3] (pend. 0,33) |
| M1/M5 sin libro L1 | 0,70 / 1,21 | +1,2e-4 / +2,6e-4 | 0,23 / 0,23 | |
| M1 / M5 con LR 60 ms | 1,27 / 1,60 | −2,7e-4 / −1,1e-4 | 0,69 / 0,54 | |
| M1 / M5 con LR 30 ms | 1,39 / 1,69 | −3,4e-4 / −1,5e-4 | 0,72 / 0,56 | |

- Mejor ΔLL de cualquier modelo y retardo: −3,4e-4 (M1, 30 ms), 6 veces por encima del umbral; el límite inferior más optimista del IS-CV (18 días) es −2,95e-4 (M0): el −2,0e-3 queda excluido al 90 %.
- Sensibilidades post-hoc declaradas (`sens3.py`, `gbm3.py`; no prerregistradas): ridge λ 1e-3..1 en M5 → ΔLL OOS +6,5e-6..+9,0e-5; gradiente no lineal (HistGB, 150 árboles prof. 3) → σ 1,39/1,27 pp, ΔLL +4,4e-4 (IS-CV) / −1,9e-5 (OOS), pendiente 0,33/0,49; encogido ×0,5 → σ 0,70/0,63, ΔLL +1,8e-5 [−2,5e-4; +2,8e-4] / −1,5e-4 [−5,1e-4; +2,1e-4]. La no linealidad no rescata nada.
- Por moneda (M5 OOS) ΔLL: BTC +5,7e-4, ETH −8,9e-4, SOL +7,9e-4, XRP −3,6e-4, DOGE +8,4e-4, BNB −1,8e-4; ninguna con IC90 que excluya 0 (BTC/ETH son 5 % de las filas: spread de 1 tick casi nunca elegible).
- Sin los 2 mejores días: M5 IS-CV +7,1e-4; OOS +1,06e-3 (peor, no mejor).
- Retardo: pasar de 130 a 30-60 ms mejora M1 en ≈ 2-3e-4 nats/fila (12-16 % del umbral, IC90 cruza 0); además la infraestructura fija LR (VPS cerca del CLOB descartado por Javi).

## 3. Cota analítica con la σ alcanzada (calculada antes y después)
Prereg (§2): σ mínima para +2,0 pp/acc con GP5 (c = +0,5 pp) = **2,09 pp**; umbral con margen 2,6 pp; «×10» en ΔLL = 3,1 pp. Con σ medida (gaussiana, q̂ calibrada): M5 OOS σ 1,33 → E[ε | ε ≥ +0,5 pp] = +1,40 pp (cotiza 35 %). Pero con pendiente 0,37 lo realizable es ≈ 0,37 × 1,40 ≈ 0,5 pp, coherente con el proxy estático: dEV ≈ 0.

Proxy estático de GP (informativo; primer relleno por mercado-token, puja a bb+0,01 cola 0, sin TD/reposicionamientos; EV/acc sin compuerta −0,0085 con n = 24.606; no es comparable en nivel con R2): con M5, c = +0,5 pp pasa el 62,9 % del peso, dEV 22 días +0,0014 [−0,0011; +0,0040], OOS +0,0002 [−0,0044; +0,0047], placebo por precio de relleno p = 0,585; c = +2 pp: 22 días −0,0006 [−0,0068; +0,0056] (OOS +0,0156 [−0,0018; +0,0330] con 4 días; a 22 días ≈ 0: no significativo). Con M1, c = +2 pp: −0,0103 [−0,0169; −0,0037]. E[ε̂ | primer relleno] = +1,12 pp frente a +0,81 pp en todas las filas: los rasgos no ven selección adversa en el instante del relleno. El objetivo de ganancia del prereg (+2,0 pp/acc) no se alcanza (mejor dEV a 22 días: +0,0014/acc); **no se repite GP** (el prereg lo condicionaba al éxito de P1-P3). El placebo estratificado por precio de relleno corrige el defecto de R2 (estratos en la elegibilidad).

## 4. Regla sobre el logger L2 (prerregistrada)
σ(M5) = 1,33; σ(M5 sin libro L1) = 1,21 → el libro L1 aporta 0,55 pp en cuadratura; cota generosa de L2 (duplicar esa parte) σ_L2máx = **1,64 pp < 2,1 pp**. **No hay término medible que justifique el logger L2; se cierra la familia pasiva (información L1/L2) para B.** Reabrir solo con un rasgo nuevo que eleve la información calibrada OOS en ≥ 1 pp en cuadratura.

## 5. Bloque de identidad del barrendero (on-chain 26-27 Oct; atribución, no feature)
`identity3.py` (`/root/polymarket-research-datalogs/keep_onchain_re_as_b/onchain_fills_2026-10-26|27.csv.gz` × `m5_registro`). Unidad: puja de maker BUY de tokens 5m en [0,09; 0,31] rellenada; barrendero = `taker` de la fila del maker; barrido = (tx, taker, token).
- Población: 26-Oct 166.328 rellenos / 1.581 mercados / 4.585 barrenderos (909 con ≥ 30 rellenos) / 108.273 barridos; 27-Oct 158.548 / 1.580 / 4.457 (865) / 102.532.
- Reloj: casado con impresión `t` del registro el 51,6 % / 52,1 %; bloque − recepción p10/p50/p90 = 1,43/2,19/2,89 s y 1,45/2,20/2,92 s (consistente con ≈ 2,2-2,4 s). Por eso la identidad solo es etiqueta.
- Concentración: top1/top5/top10 del volumen 3,7/14,4/21,7 % y 2,9/13,6/21,8 %; HHI 0,0075/0,0071. Disperso: no hay un barrendero dominante.
- EV/E de todos los rellenos de la zona (Σ tam·(y−p)/Σ tam·p): **+0,278 [+0,091; +0,463] el 26 y −0,135 [−0,319; +0,039] el 27**: el efecto día (±20 pp) domina; los IC por mercado no lo recogen.
- I2 persistencia (informados = 20 % peor EV/E con ≥ 30 rellenos el día A): día B EV/E informados vs resto −0,290 vs −0,121 (dif −0,169 [−0,308; −0,025]) A=26→B=27, y +0,067 vs +0,293 (dif −0,226 [−0,456; −0,014]) A=27→B=26; son el 6-7 % de los rellenos; Spearman entre días ρ = +0,085, p = 0,014 (n = 836). Persistencia real pero débil. **Oráculo** (evitar a los informados conociéndolos de antemano): solo +1,5/+1,4 pp de EV/E.
- I3 puerta de cadencia (relleno de un informado en la misma moneda en (t−60 s, t−5 s]): señala el **76,5 % / 70,9 %** de los rellenos (puerta degenerada, veto casi total), dif −0,220 [−0,433; +0,013] y −0,072 [−0,315; +0,185]: **no cumple el criterio prerregistrado** (además el IC90 cruza 0 en ambos sentidos). Descartada como feature.
- Exploratorio post-hoc dentro de día (`identity3b.py`, 8 contrastes sin corregir, 2 días): rellenos de barridos ≥ 200 acc frente a < 50: +0,291 [−0,051; +0,635] / +0,271 [−0,041; +0,591]; ≥ 4 makers frente a 1: +0,173 [−0,038; +0,403] / +0,207 [+0,015; +0,411]; barrendero con ≥ 10 rellenos previos frente a 0: +0,712 [−0,017; +1,458] / +0,567 [−0,006; +1,010]; tras barrido ≥ 200 en la misma moneda en (t−60 s, t−5 s] (observable antes): +0,119 [−0,152; +0,372] / +0,149 [−0,069; +0,362], 44-45 % de los rellenos. Mismo signo en 2/2 días, pero es un solo fenómeno correlado (barridos grandes = bots de alta cadencia), el IC90 toca 0 y con 8 contrastes no hay corrección que lo sostenga. Es el único candidato de «barrido final a favor».
- Análogo a nivel de token en 22 días (contraste único hasheado antes, `PREREG_POSTSWEEP_R3.md`, `postsweep3.py`): presión neta vendedora ≥ 200 acc en los 30 s previos → dEV = **+0,0055**/acc [−0,0048; +0,0159], 12/22 días > 0, placebo por precio de relleno p = 0,074, cobertura 20,3 %: **no cumple** (pedía ≥ +0,02, IC90 > 0, p < 0,05). Sensibilidad (no decide): umbral 100 acc dEV +0,0048 [−0,0076; +0,0148], placebo p = 0,154; umbral 400 acc dEV +0,0055 [−0,0076; +0,0166], placebo p = 0,050 (en el borde, pero con IC90 por días que cruza 0 y siendo 1 de 3 umbrales mirados). Mismo signo en IS (+0,0052, 10/18 días > 0) y en OOS (+0,0072 [−0,0249; +0,0393], 2/4 días > 0), con magnitud unas 4 veces menor que la exigida.
- Límites: 2 días = 1 réplica; barrendero = dirección, no persona; ningún rasgo de identidad entra en M1-M5; el taker es anónimo hasta el casado, así que ninguna identidad es observable antes del primer barrido.

## 6. Hallazgos adversariales
1. Efecto día: el EV/E del mismo universo cambia de signo entre dos días consecutivos (+27,8 % / −13,5 %); cualquier comparación entre días mezclados o IC por mercado está sesgado. Por eso la evidencia decisiva es IS-CV por días (18) y el OOS de 4 días se lee solo como confirmación; el OOS (IC90 ±1,3e-3) tiene potencia insuficiente por sí solo para detectar −2e-3, el IS-CV sí lo excluye.
2. σ_ε bruta se infla con ruido de estimación (M5: 1,33 pp bruta frente a 0,5 pp efectiva): el criterio P3 de pendiente era imprescindible; sin él un modelo sobreajustado habría «pasado» σ.
3. Las filas excluyen los estados con TD Binance activo: la información de saltos de Binance ya la cosecha la cancelación TD de B; lo medido es la información adicional más allá de TD.
4. Muestreo uniforme cada 2 s con autocorrelación alta: la unidad estadística es el día (IC por días), no la fila.
5. El proxy de GP no es el simulador (sin vidas de orden, TD ni reposicionamientos; una unidad por mercado-token): sirve para contrastes, no para niveles ni euros.
6. Exploratorios (`identity3b.py`, `sens3.py`, `gbm3.py`) NO prerregistrados; `postsweep3.py` hasheado antes de ejecutarlo; todos en `HASHES_R3.txt`. Ningún resultado exploratorio se usa como evidencia de aceptación.
7. Incidencia menor: el smoke se lanzó con `--outdir out_smoke` sin barra final y escribió `out_smokef_2026-10-10.npz` en la carpeta (movido a `out_smoke/`; no es un error del código hasheado; el pipeline completo usa `out/`).

## 7. Impacto en cartera
Sin contribución incremental: B pasivo sigue sin ventaja de información (EV on-chain −7,2 %, n = 202, cifra del encargo de la sesión principal, no remedida aquí). Aritmética de capacidad con el proxy de R3 (una unidad por mercado-token, sin reposiciones; no validada): incluso si la compuerta M5 con c = +0,5 pp hubiera dado +2 pp/acc (el éxito que se pedía), 15.332 primeros rellenos × ≤ 5 acc × 0,02 € ≈ 1,5 k€ en 22 días ≈ 25 k€/año, muy lejos de 200 k€. Con la información calibrada real (≈ 0,5 pp) la compuerta aporta ≲ 0,5 pp/acc. La familia pasiva L1 no puede ser una pata del objetivo de 200 k€ por la vía de información.

## 8. Siguiente experimento decisivo (uno)
**Prueba hacia delante del estado «barrido grande reciente en la misma moneda» con ≥ 10 días on-chain**, única señal con tamaño de efecto relevante (+12 a +15 pp de EV/E, mismo signo 2/2 días) y observable antes del relleno.
- Cómo: ya hay `onchain_fills` completos de 20 a 27 Oct en el directorio raíz de datalogs (observados hoy 9 ficheros, 20..28 Oct; la retención real no está verificada y la nota del encargo hablaba de 4 días: copiarlos a `keep_onchain_re_as_b/` antes de que roten). Registro de mercados/impresiones verificado con `identity3.load_registry` para: 2026-10-20, 2026-10-21, 2026-10-22, 2026-10-23, 2026-10-24, 2026-10-25, 2026-10-26, 2026-10-27. La prueba puede empezar HOY con los días de confirmación hacia atrás (20, 21, 22, 23, 24, 25 Oct) y sumar el 28 Oct en adelante: ≥ 10 días de confirmación el 01-11 si todos cargan. Tamaños medidos al cerrar esta ronda: onchain_fills_2026-10-20.csv.gz 268 MB; onchain_fills_2026-10-21.csv.gz 276 MB; onchain_fills_2026-10-22.csv.gz 263 MB; onchain_fills_2026-10-23.csv.gz 297 MB; onchain_fills_2026-10-24.csv.gz 303 MB; onchain_fills_2026-10-25.csv.gz 303 MB; onchain_fills_2026-10-26.csv.gz 264 MB; onchain_fills_2026-10-27.csv.gz 261 MB; onchain_fills_2026-10-27_parcial_1434Z.csv.gz 151 MB; onchain_fills_2026-10-28.csv.gz 116 MB; onchain_fills_2026-10-28_parcial.csv.gz 32 MB. Coste en euros 0; ≈ 1 min de cómputo por 2 días con `identity3b.py`.
- Preregistro (hash antes de mirar): estado S = existe un barrido ≥ 200 acc en la misma moneda en (t−60 s, t−5 s]; contraste dEV/E = EV/E(S) − EV/E(no S) sobre todos los rellenos de la zona, por día. Los días 26-27 Oct generaron la hipótesis (DESCUBRIMIENTO) y no cuentan para el gate. Éxito sobre días de CONFIRMACIÓN: dEV/E ≥ +0,10, IC90 por días > 0 con ≥ 10 días y ≥ 8 de 10 días positivos, cobertura de S entre 10 % y 60 %, placebo por precio de relleno p < 0,05; solo entonces simular una puja condicionada con vidas de orden (sim3 heredero de sim2).
- Fracaso: dEV/E < +0,05 o IC90 que cruza 0 con ≥ 10 días → se cierra el «barrido a favor» y B pasivo queda sin vía de información.
- Por qué cambia la decisión: es la única hipótesis viva con efecto de pp altos en el eje de selección adversa; si cae, el esfuerzo pasa a la otra vía no dependiente de predecir y: recompensas de liquidez 5m (REWARDS-5M, pendiente previo; no medida aquí).

## 9. Reproducibilidad
- Directorio: `/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/`. Hashes sha256 en `HASHES_R3.txt`: PREREG `53b4c42baf285056f4d87bbef737d24625be92793f17af2dddece79b4cecb8c3`, `feat3.py` `167a375824da0ab9502f43b4931f50bb7557bfad633b052a9cfacf10b7b84505`, `analysis3.py` `33ded57efe2e92d616ed443e4e0e6582cb9981f2ea2aaa9cba4577b2114f1e9f`, `identity3.py` `a4d84add1c9476efc866717547f6664573636501857364e2b9459a7c6bcaf348`; exploratorios añadidos al final del fichero.
- Comandos: `python3 feat3.py --selftest`; `bash run_all_r3.sh` (22 días + identidad + análisis, marca `FIN_R3` en `run3.log`, duración ≈ 29 min); salidas `analysis_salida.txt`, `identity_salida.txt`. Exploratorios: `python3 identity3b.py`, `python3 sens3.py`, `python3 gbm3.py`, `python3 postsweep3.py` (cada uno < 3 min).
- Estado: COMPLETO (22/22 días, 99,70 % de cobertura de desenlaces, 22 `FIN_DIA rc=0`). Código del simulador congelado (`alpha_miner_b_27oct/sim.py`) y de R2 (`formula_r2_28oct/sim2.py`) sin tocar.

## 10. Incertidumbres no resueltas
- Potencia del OOS de 4 días y efecto día: no se puede afirmar «información exactamente 0», solo que no alcanza ni el 10-15 % del umbral.
- Rasgos no probados: profundidad multinivel (L2, el libro solo trae nivel 1), otros activos fuera de Binance, información de wallets antes del casado (no existe), modelos con interacciones no pre-especificadas.
- Identidad: 2 días, 52 % de casado con el registro; las direcciones no son personas; el «barrido grande» a nivel de moneda solo existe on-chain.
- B real on-chain (−7,2 %, n = 202) no se vuelve a medir aquí.
