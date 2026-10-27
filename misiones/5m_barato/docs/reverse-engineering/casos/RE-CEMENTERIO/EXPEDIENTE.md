# Expediente RE-CEMENTERIO — 26-Oct-2026 (cheap5m-reverse-engineer)
Estado de cierre: EVIDENCE_INSUFFICIENT · Bloqueo dominante (A-K): H (económico: ninguna línea revisada tiene EV propio >0 con potencia; el EV poblacional del nicho barato cambia de signo según el régimen) · Secundarios: E (cola propia ≠ población: falta fidelidad del simulador y cola real), G (n y días: varias líneas nunca terminadas), B (dos descartes por medición mal hecha), K (carga >4: lo pesado no se ha ejecutado)
Sin validación independiente. Reglas de fuente aplicadas (VALIDACION_INDEPENDIENTE_26OCT): la verdad de B es on-chain por order_hash (202 rellenos, 221,30 €, EV −0,0724, IC90 por cierre −0,31..+0,20); no cito cifras de etiquetado_pasivo_B; la brecha rellena−no rellena no se usa como evidencia.

## 1. Fenómeno
Javi pide revisar todo lo descartado, rechazado, refutado o «bajado» en 5m barato, para mitigar la AS y para generar €. Clasificación: REFUTADA_CORRECTAMENTE / INVALIDADA_POR_MEDICIÓN / NUNCA_BIEN_PROBADA / INCONCLUSA / REABRIBLE_CON_MECANISMO_NUEVO. Fuentes: informes de `experimentos/5m_barato/**`, `docs/REGISTRO_HIPOTESIS.md`, `LIBRO_OBJETIVO_200K.md`, `MISION_CLICK_B.md`, `PENDIENTES_5M_BARATO.md`, `tintero/INFORME.md`, CLAUDE.md §3.6 y memorias. Las cifras marcadas «(informe)» las copio del artefacto citado sin recalcularlas. Las marcadas «(E-RE-CM)» las he recalculado hoy.

## 2. Experimentos propios (los dos ligeros, ~30 s cada uno, con prereg previo)
- **E-RE-CM-01, pre-apertura** (`PREREG_E01.md`, sha256 7af36d07…491c; script `scripts/e01_preapertura.py`; salida `e01_salida.txt`; desenlace 100 % en €). Hecho: cosechar v1-v3 cotiza solo «primeros 15 s DE LA VENTANA (no antes de abrir)» (`analisis_5m_cosechar_apertura.py:184`), así que la pre-apertura nunca se había medido.
  - Rellenos maker de la población en 5m con T>300 s, del 06 al 21-Oct (16 días): EV −0,0025, IC90 por días −0,0125..+0,0081, ~457 k€/día de coste (BTC 0,30-0,70 en su mayoría). Con rebate, +0,0045.
  - Ninguna celda moneda×banda pasa la regla: de 32 celdas, una sobrevive al BH (BTC 0,05-0,10) y tiene 1 día.
  - Las bandas baratas pre-apertura dan EV espectaculares (+1,7..+9,9). Son lotería: 76-2.000 €/día, sin los 2 mejores días <0, IC enormes.
  - Contaminación declarada: el tramo T>300 incluye los casados de los primeros ~2,4 s por el retraso del bloque.
  - Veredicto: REFUTADA_CORRECTAMENTE a nivel población.
- **E-RE-CM-02, BTC 5m banda barata** (`PREREG_E02.md`, sha256 2fe247f1…d860; `scripts/e02_btc_barato.py`; `e02_salida.txt`). Resuelve la contradicción F1/F2 que señaló el tintero.
  - BTC 0,05-0,30, T 60-300 s: en DESC (06-13) +0,086 (IC90 días +0,034..+0,140, 6/8 días positivos). En HOLD (14-21) +0,018 (IC −0,082..+0,106, 5/8; sin los 2 mejores días −0,053; top-1 4 %). Unos 300 k€/día de coste y ~2.700 makers.
  - Control ALT3 (nicho de B): DESC +0,144 → HOLD −0,049 (IC −0,165..+0,060).
  - Veredicto: INCONCLUSA. F1 y F2 no se contradicen: F1 promedia las dos mitades y F2 mira solo HOLD. El EV de la población cambia CON el régimen y a la vez en BTC y en las alts.

- **E-RE-CM-03, H50: régimen del día anterior** (`PREREG_E03.md`, sha256 db840071…dbc31; `scripts/e03_regimen_d1.py`; `e03_salida.txt`). Población 5m 0,05-0,30, T 60-300 s, 16 días.
  - Correlación EV(d−1)→EV(d): BTC r=0,34 (p por permutación 0,057); ALT3 r=0,14 (p 0,21).
  - La política «operar solo si ayer ganó» mejora +0,032 (BTC) y +0,066 (ALT3) €/€, con 15 pares de días cada una.
  - Veredicto: NO USABLE según el prereg (p ≥0,05). INCONCLUSA con signo compatible: se queda en forward pasivo, sin ningún cambio a B.

## 3. Matriz del cementerio
| línea | evidencia (artefacto, cifra) | clasificación | nota |
|---|---|---|---|
| Cosechar al abrir v1/v2 BTC (H10/H11/H32) | 24/24 celdas OOS <0; par completo y aun −0,04; pata suelta −0,80 €/€ (informe tintero) | REFUTADA_CORRECTAMENTE | el bug de v1 (registro no cronológico) se corrigió antes del veredicto |
| Cosechar v3 (ETH/SOL/XRP + BTC 05-21) | DESC 05-14, `cosechar_abrir/datos/s6_informe_desc.txt`: mejores políticas BTC −0,051, ETH −0,083, SOL −0,116, XRP −0,191 €/€, IC90 por días <0, 0-2/10 días positivos | INCONCLUSA formal / signo REFUTADO | falta el OOS 15-21 del propio prereg (`s6_analisis.py` sin flag, minutos) y `s7_fidelidad`; cerrarlo, no reabrirlo |
| H33 cosechar con vol alta | OOS n=14-16, 40 combinaciones (informe) | INCONCLUSA | multiplicidad; solo forward |
| Posicionado ANTES de abrir | E-RE-CM-01 | REFUTADA_CORRECTAMENTE (población) | antes NUNCA_BIEN_PROBADA |
| LOWLOW-PAIR (H14) | 1.314 patas sueltas, 0 ganan; −0,197 €/mercado, 0/5 días (informe) | REFUTADA_CORRECTAMENTE | — |
| Pares 5m maker (H16) / maker de un solo lado | OOS −0,050 / ≈0 | REFUTADA_CORRECTAMENTE (pares); el lado único ES B | — |
| F7 precio del par | P4 −0,038 (IC90 −0,080,−0,002) | REFUTADA_CORRECTAMENTE | — |
| Pata suelta activa (PSA) | `pata_suelta_activa/datos/eval.txt`: C0/BASE −0,055, IC90 días (−0,112,−0,004), 0/3 días, 252 mercados | NUNCA_BIEN_PROBADA por días (n=3), signo negativo | sin INFORME; completar la rezagada vale +0,051 €/€ frente a mantener (no es EV) |
| Caja de dos patas 250-400 ms (H28) | suelo del tomador 215 ms; rival en vuelo (H24) | REFUTADA_CORRECTAMENTE (ejecución) | el −35/−179 $ sigue sin auditar: NO_REPRODUCIDA |
| Cajas altcoin (H21) | XRP +703 $, BTC −7.553 $… (comunicado; artefacto NO_LOCALIZADO) | NUNCA_BIEN_PROBADA | primero localizar el artefacto; la misma latencia de tomador aplica |
| Anidados 4h (H31) | 2 eventos en 493 cierres; capacidad 3-19 $ (informe) | REFUTADA_CORRECTAMENTE (capacidad) | — |
| FV v1-v3, FV v4 tomador, FV-LONGSHOT (H15) | Brier 0,07644 vs precio 0,07639; M=0 OOS −0,073 = control (informe) | REFUTADA_CORRECTAMENTE | q_techo: ningún q bate al precio de relleno (log-loss 0,4952 vs 0,4974, n=36.125) |
| Maker FV 4/4b (H08) | nunca construido; H07 no reproducible (semillas +0,028/+0,032/+0,061) | NUNCA_BIEN_PROBADA, premisa REFUTADA | sin un q mejor que el precio, el maker FV no tiene de dónde sacar margen |
| FV v5 (H34) | 75 tests, sin validar | INCONCLUSA | validación independiente pendiente |
| Ganadoras persistentes | roster BH vacío (informe) | REFUTADA_CORRECTAMENTE | — |
| Copiar makers ganadoras / tomadoras | selección por resultado (14-Oct); OOS −0,004 | REFUTADA_CORRECTAMENTE | — |
| pspspsps5 (0xb0f8…) | ventaja real (placebo z=3,8; +0,20/+0,44 en holdout), mecanismo no hallado | INCONCLUSA | pausada sin requisito cuantificable |
| mo-money (H30) | +5,5 pp en la 1ª pata (informe); PENDING desde 14-Oct, 1 día corrido; lo direccional «se secó» en octubre | NUNCA_BIEN_PROBADA | prior bajo |
| 0x21f4 / 0xe290 / 0x86b1 (BTC 5m) | +22..+34 k€ en 16 días con rebate del 31-43 %; 44/48 positivos ex post; rellenan el 12-37 % a ≥2 ticks bajo el bid (rebate_ganadores) | INCONCLUSA | F1 huella: ningún rasgo de comportamiento predice EV persistente (lookalikes p=0,86) |
| Carry ≥0,90 (F3) | pujas virtuales propias, regla pesimista: −0,047 (IC90 −0,055..−0,039, n=45.631) | REFUTADA_CORRECTAMENTE como puja propia | el descarte «con el estrés de B ≈0» (tintero) estaba mal medido, pero F3 lo midió directamente |
| Favoritos 60m 0,70-0,90 puja propia | `fav_60m_4h/datos/gate.json`: rellenas −0,0575 (IC90 días −0,081..−0,034, 2/13 días) | REFUTADA_CORRECTAMENTE | ojo: el `AS_pp −33` de ese fichero es la identidad; no cuenta |
| 60m barato 0,10-0,30 / 4h / diario | rellenas −0,044 (IC −0,10..+0,014); 4h con 36 cierres; diario en recolección | INCONCLUSA / NUNCA_BIEN_PROBADA | — |
| F2 «ninguna celda 5m barata sin AS» | brecha −20..−27 pp en las 6 monedas | INVALIDADA_POR_MEDICIÓN | la brecha sale en cualquier celda por construcción |
| Nichos con «estrés −0,053» (mapa_escala, tintero, PLAN) | −0,072 (B) frente a −0,019 (población) de periodos distintos; en el mismo periodo B −0,030 ≈ población −0,045 | INVALIDADA_POR_MEDICIÓN (el estrés) | rehacer los escenarios sin ese término |
| 15m ETH favoritos 0,70-0,99 (FAV-15M-ETH) | población +0,025 (IC90 días +0,018..+0,031, 16/18 días, 77 % de 402 makers positivos, BH q=0,024) | REABRIBLE como subestrategia nueva (Javi 26-Oct) | descartada antes solo por el estrés mal medido; falta la puja propia (§5) |
| H5M «CONFIRMADA» (H26) | media de cocientes; ponderado por € +0,040 (IC cruza 0); primeras 5 acc +0,003 | INVALIDADA_POR_MEDICIÓN (la confirmación) | como población ≈0 |
| Modelo de colocación | manifests BLOCKED el 19-Oct (dos veces), nunca terminó | NUNCA_BIEN_PROBADA | depende del simulador sin cola calibrada (B_FIEL NO_REPRODUCE) |
| H39/H39b MM continuo a dos lados | PENDING por orden de Javi (después de B) | NUNCA_BIEN_PROBADA | no preregistrar ni simular hasta que Javi lo ordene |
| H23 maker pre-posicionado, H55 favorito anidado (tomador y maker) | capacidad 2-3 $/evento; H55 n=19 +0,061, alts −0,082 | INCONCLUSA (capacidad ≤3 k€) | — |
| Tomador V2-V7, H43 R5K, H53/H54, entrada con retraso, bid15 rancio, cancelar en el taker-delay | rival 150-300 ms por delante (29/29); R5K forward −0,292; probado con órdenes reales | REFUTADA_CORRECTAMENTE | V4/V6/V7 siguen en forward congelado (n<40: INCONCLUSA formal) |
| Filtros sobre los rellenos de B (régimen, >0,243, rasgos, tomadores informados) | n=202 rellenos ⇒ SE del EV ≈0,17 | NUNCA_BIEN_PROBADA por n (G) | salvo los detectores con n grande: D-FUERTE AUC 0,554 y ex-ante 0,513, REFUTADA_CORRECTAMENTE |
| Cancelación en ms (BN_W300) | REJECTED con 329.998 rellenos | REFUTADA_CORRECTAMENTE | A1/F5 y R1 siguen PROMISING/EXPLORATORY en forward |
| X-SALIDA | ΔPnL = EV·Δvolumen (es un teorema) | REFUTADA_CORRECTAMENTE | — |
| Rebate 20 % | +0,011 €/€ solo con ≥89 €/día de volumen | condicional (no refutado) | — |
| Rewards de liquidez 5m | `rewards.rates=null` (tintero); earnings [] durante 13 días | REFUTADA_CORRECTAMENTE (no hay bolsa) | se contradice con `rewardsMinSize 50` de gamma: verificar el endpoint antes de citarlo |
| «AS −18 pp mecánica» como premio (MISION_CLICK_B) | identidad (RE-AS-B, validación) | INVALIDADA_POR_MEDICIÓN | — |
| «Puja de B ≈ virtual 52,8 %» | 55,5 % por puja frente a 52,8 % virtual: coincidencia de unidades distintas, no calibración (validación) | INVALIDADA_POR_MEDICIÓN | — |

## 4. Qué se puede sostener / qué NO
SÍ:
- La revisión no encuentra ninguna línea refutada por medición errónea que, re-medida, salga positiva. Los dos descartes mal medidos (el estrés −0,053 y la brecha de F2) solo afectaban a FAV-15M-ETH y a cotas que no deciden nada.
- La pre-apertura queda cerrada con datos de población.
- El EV del maker barato de la población es del régimen: DESC +0,09/+0,14 → HOLD +0,02/−0,05, en BTC y en las alts.
NO:
- Que el EV de la población sea capturable por nuestra cola. F3 y fav 60m, que dan ≥0 en población, salen −0,05 con puja propia.
- Que algo de esto sume € validados.

## 5. Reabribles y no terminadas (experimento mínimo; no se suma nada solapado)
| prio | línea | mecanismo/predicción nueva | experimento mínimo | coste | valor de la información | €/año potencial (contrafactual) |
|---|---|---|---|---|---|---|
| (ref.) | FAV-15M-ETH → misión 15m v5, no se trabaja aquí | vender el boleto del longshot como maker en el favorito; predicción: la puja propia al final de la cola rinde ≥ +0,01 €/€ | (a) EV de puja propia: pujas virtuales 5 acc al final de la cola, regla pesimista, 15m ETH 0,70-0,99, ≥10 días, desenlace oficial (mismo código que F3 y fav60); (b) cuota alcanzable: fracción de los rellenos on-chain del nivel que habría tocado una puja de 5 acc en el top, por día | medio, tras 09:30Z | alto: es la única celda con BH q<0,05 y 16/18 días | flujo ~79 k€/día; cuota sin medir; 1 % ≈6 k, 5 % ≈29 k sin estrés (validación). Prior bajo: F3 y fav60 salieron −0,05 con puja propia |
| 2 | Cosechar v3: cerrar el prereg | — | `s6_analisis.py` (OOS 15-21) + `s7_fidelidad.py` | minutos | bajo (DESC negativo en todo) | 0 |
| 3 | H50 régimen d−1 (B y B-BTC) | EJECUTADO hoy (E-RE-CM-03): INCONCLUSA, r 0,34/0,14, p 0,057/0,21 | acumular días: repetir la misma prueba con ≥30 pares (≈20-Nov) sobre cells nuevas, sin cambiar la regla | 0 (re-ejecutar el script) | medio: decide CUÁNDO operar | ≤ lo de B; no se suma con B |
| 4 | Modelo de colocación | el nivel (SPREAD) y COND están acoplados; un modelo de colocación ataca los dos a la vez | relanzar `lanzar_modelo.py` solo cuando el simulador reproduzca la cola | alto (bloqueado por fidelidad) | medio | — |
| 5 | Cajas altcoin | — | localizar el artefacto de «XRP +703 $» y reproducirlo | bajo | bajo | — |
Lo demás no se reabre: refutado con n suficiente o sin mecanismo nuevo.

## 6. LIBRO DE SUMA (corte 26-Oct; € ≈ pUSD; validado = peldaño real con gate)
| subestrategia | estado | validado | exploratorio (central) | contrafactual / optimista | capacidad medida | solape | siguiente experimento |
|---|---|---|---|---|---|---|---|
| B (H35/H47 alts, maker barato) | REAL parada (sin recarga) | 0 | −1,5 k€/año (−0,072 × ~60 €/día; on-chain) | ≤8 k (R1/A1 + K20: solapan, supone EV +0,06 frente al R3 medido −0,041) | R3 136 €/día a K5 (~310 a K20) | contiene B-BTC, A1, R1, R0 | forward R1 (~03-Nov), A1 (~04-Nov), E03 |
| FAV-15M-ETH — **misión 15m v5** (Javi 26-Oct; `informes/m15v5_libro_investigacion_13oct.md`) | EXPLORATORY | 0 | missing (falta la puja propia) | 6-29 k sin estrés (1-5 % de cuota, sin medir) | flujo ~79 k€/día (población) | NO se suma con B ni con 5m barato | lo decide la misión 15m v5 (experimento en §5 fila 1, solo como referencia) |
| B-BTC banda barata | INCONCLUSA (E-RE-CM-02) | 0 | población HOLD +0,018 (IC cruza 0); sim propia H35 BTC −0,068 | — | 300 k€/día de flujo (población) | con B si se opera a la vez | §5 prio 3; F5 BTC = decisión de Javi |
| Tomador V4 (+V2/V3/V5-V7, un solo canal) | forward congelado | 0 | ≈0,7 k | 4,9 k (15 k sin tope) | 2,08 ejecuciones/día | — | G1 n≥40 (~27-28 Oct) |
| H55 favorito anidado / H23 | EXPLORATORY | 0 | ≈0 | ≤3 k | 2-3 $/evento | con V4 | — |
| R5K (H43) | forward en contra | 0 | 0 (−0,292) | ≤19,7 k (techo con forward compatible) | 830 €/día | maker BTC | acumular forward |
| PRECIERRE (referencia, fuera de la familia) | LIVE 2 € | n=33, +0,133, IC por días cruza 0: no validado | ~0,12 k | — | ~1,3 órdenes/día | — | rampa ≥40 órdenes |
| H39 MM dos lados | PENDING (Javi) | 0 | — | wallets de referencia +0,85..+1,5 %/vol (exploratorio) | — | maker | cuando Javi lo ordene |
**Suma 5m barato** (sin FAV-15M-ETH, que es de 15m v5): validado 0 €. Exploratorio central ≈ −1,5 k + 0,7 k ≈ −1 k€/año. Optimista sin solapes ≈ 8 + 4,9 + 3 + 19,7 ≈ 36 k€/año, sumando escenarios favorables no medidos (no es una previsión). **Hueco a 200 k€: 200 k contra lo validado; ≥164 k incluso contra el optimista.**
Qué tendría que ser verdad para cerrarlo (validación §4: 0,10 × 5.479 €/día × 365 = 200 k): EV propio ≥ +0,10 €/€ sobre ~5,5 k€/día de rellenos, o +0,05 sobre ~11 k€/día. Equivale a ~18× la capacidad de R3 a K20 en el nicho de B, o a una cuota relevante del BTC barato (300 k€/día) con un EV propio que hoy no existe.

## 7. Refutación intentada
1. Pre-apertura: la contaminación por el bloque sesga a favor de parecerse a la ventana. Aun así, el agregado ≈0 con 457 k€/día. Las celdas baratas espectaculares solo aguantan con sus 2 mejores días (primero bug o lotería; ni siquiera pasan el n de días).
2. E02: el corte DESC/HOLD está fijado en el prereg. Con 8 días por mitad el IC por días es ancho. INCONCLUSA no es refutada.
3. Las cifras «(informe)» no están recalculadas: un red-team con datos crudos debe verificar las que deciden (cosechar v3 DESC, F3, fav60, FAV-15M-ETH).
4. Con mi propio sesgo («nada funciona») se puede pasar por alto una celda. Por eso no cierro FAV-15M-ETH ni B-BTC: quedan INCONCLUSA/REABRIBLE con su experimento.

## 8. Siguiente paso exacto y qué reabriría
1) Tras 09:30Z y con load5<4: el OOS de cosechar v3 (prio 2) y la prueba de régimen d−1 de B-BTC (prio 3). FAV-15M-ETH queda en manos de la misión 15m v5.
2) Validación independiente de este expediente.
3) Reabre cualquier fila REFUTADA un dato que contradiga su artefacto, o un mecanismo con predicción nueva y prereg propio.
