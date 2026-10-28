# PREREG_FORMULA_R3 - frontera de informacion de la compuerta eps de B (Ronda 3)

Fecha: 2026-10-28. Escrito y hasheado ANTES de medir (HASHES_R3.txt). Agente: polymarket-quantum-alpha-miner. No se autocertifica nada: validacion y refutacion por agentes independientes. Presupuesto: 20 llamadas de herramienta.

## 1. Pregunta y mandato
R2 (FORMULA_R2_B.md): la compuerta eps = q^ - mid de B rinde exactamente la cota analitica con sigma_eps = 0,98 pp (+0,24/+0,53/+0,84 pp en p1), 0 celdas CANDIDATE: el techo es la informacion, no la cola ni la profundidad. Mandato de Javi (via chief): conseguir x10 de informacion y usar el barrido final a favor.
Lectura operativa, fijada antes de medir:
(a) x10 de informacion = dLL x10 (de 2,8e-4 a 2,8e-3 nats/fila, es decir sigma_eps x raiz(10) = 3,1 pp). Umbral de exito pre-registrado: sigma_eps >= 2,6 pp (dLL ~ -2,0e-3), cerca del minimo que habilita +2 pp/acc con la compuerta GP5 (seccion 2).
(b) barrido final = el barrido (orden tomadora que casa contra pujas de la zona de B) que rellena la puja, ultimo evento de su vida. Se estudia (i) que rasgos observables ANTES del barrido lo anticipan (flujo firmado, Binance, BTC a alts, DeltaC multi-horizonte) y (ii) cuanta seleccion adversa es atribuible a barrenderos identificables (on-chain 26-27 Oct): tasa, tamano, concentracion, cadencia. La identidad on-chain llega ~2,4 s tras el casado: solo etiqueta/atribucion; el unico uso en decision contemplado es con barridos ANTERIORES a t-5 s.

## 2. Cota analitica (calculada antes de medir)
Para eps ~ N(0, s^2): ganancia maxima de EV/acc de una compuerta cotizar solo si eps >= c: E[eps | eps >= c] = s*phi(c/s)/(1-Phi(c/s)) (q^ calibrada). Con q ~ 0,22: dLL = s^2/(2 q (1-q)) = 2,91 s^2 nats/fila.

| sigma_eps (pp) | dLL (nats/fila) | c=0 | c=+0,5 pp (GP5) | c=+1,0 pp |
|---|---|---|---|---|
| 0.98 | 2.8e-04 | +0.78 pp (cotiza 50 %) | +1.13 pp (cotiza 30 %) | +1.51 pp (cotiza 15 %) |
| 1.50 | 6.5e-04 | +1.20 pp (cotiza 50 %) | +1.53 pp (cotiza 37 %) | +1.90 pp (cotiza 25 %) |
| 2.10 | 1.3e-03 | +1.68 pp (cotiza 50 %) | +2.01 pp (cotiza 41 %) | +2.36 pp (cotiza 32 %) |
| 2.60 | 2.0e-03 | +2.07 pp (cotiza 50 %) | +2.40 pp (cotiza 42 %) | +2.75 pp (cotiza 35 %) |
| 3.10 | 2.8e-03 | +2.47 pp (cotiza 50 %) | +2.80 pp (cotiza 44 %) | +3.14 pp (cotiza 37 %) |

sigma minimo para E[eps | eps >= +0,5 pp] = +2,0 pp: 2.09 pp (minimo matematico). El umbral 2,6 pp deja margen por (i) q^ no perfectamente calibrada, (ii) eps no gaussiana, (iii) rellenos no uniformes en el tiempo. El resultado de R2 (sigma 0,98 pp; p1 +0,24/+0,53/+0,84 pp) encaja con la primera fila.

## 3. Poblacion, reloj y etiqueta
Filas = (token, tick de 2 s del reloj de RECEPCION) con: bb retrasado 130 ms en [0,10; 0,29], spread >= 0,02, T en [60; 290] s, sin TD Binance activo (elegibilidad congelada de alpha_miner_b_27oct/sim.py). 22 dias 2026-10-05..26: IS = 05..22 (18 dias), OOS = 23..26 (4 dias); el OOS no se usa para elegir nada. Etiqueta y = 1 si el token gana (desenlace oficial: maker_ms_desenlaces_cache.json; las filas sin desenlace se descartan y se declara la cobertura). Referencia de toda metrica: m130 = mid del libro retrasado 130 ms (precio de referencia de la puja de B), tambien para LR = 60/30 ms.

## 4. Rasgos (todos observables a t-LR, LR en {130, 60, 30} ms; reloj de recepcion)
B1 (L1 recalibrado como R1/R2): dq, DeltaC0 = logit FV15 - logit m, hasfv, lmd (logit m_LR - logit m130), spread, log1p(bs), log1p(as), T, T^2, logit m130, dummies de bb (>=0,15; >=0,20; >=0,25), dummies de moneda.
B2 (Binance): retornos 0,2/1/5 s del simbolo de la moneda firmados por lado (YES = Up = +1), crudos y escalados por kappa(m)/raiz(T), kappa = phi(Phi^-1(m))/(m(1-m)).
B3 (flujo firmado de las filas t): flujo propio y del complementario (equivalente al token) a 1/5/30 s en log1p con signo, numero de impresiones a 5 s, ultima impresion menos mid, tiempo desde la ultima.
B4 (BTC a alts): logit del mid del 5m BTC YES de la misma ventana, sus cambios a 1/5 s y retornos Binance BTC a 1/5 s, firmados por lado; 0 para BTC.
B5 (multi-horizonte): DeltaFV15 a 1/5/30 s (logit FV15(t) - logit FV15(t-h)) y momento propio del mid a 1/5/30 s.
Modelos acumulativos M1 = B1, M2 = B1+B2, M3 = +B3, M4 = +B4, M5 = +B5. M0 = eps de R2 con coeficientes fijos (A2 = 0,026; A3 = 0,085; sin reajuste). M1nb y M5nb = sin {dq, log1p(bs), log1p(as)} (regla L2).

## 5. Ajuste y validacion
Logistica con offset logit(m130), ridge fijo lambda = 1e-4 sobre variables estandarizadas con media y desviacion del entrenamiento (sin seleccion de hiperparametros), L-BFGS <= 150 iteraciones. M1 y M5: validacion cruzada por dias en IS (6 grupos de 3 dias consecutivos, prediccion fuera de pliegue). Los cinco modelos se reajustan con todo el IS y se evaluan en OOS. Ningun ajuste ve el OOS. Sin seleccion de rasgos ni cambio de lambda tras ver resultados.

## 6. Metricas y criterios
Primaria (LR = 130 ms, M5, OOS, filas elegibles):
P1 sigma_eps = desviacion tipica de q^ - m130 >= 2,6 pp;
P2 dLL = LL(q^) - LL(m130) <= -2,0e-3 nats/fila, con limite superior del IC90 por dias (t, gl = 3, media de 4 dias OOS) < 0;
P3 pendiente OOS de (y - m) sobre eps^ >= 0,7 (no sobreconfiada).
EXITO = P1 y P2 y P3: se repite GP (criterios c1-c9 de R2) con la eps ampliada y placebo estratificado por precio de relleno. PARCIAL: sigma_eps en [1,5; 2,6) y limite superior del IC90 de dLL < 0. FALLO: el resto.
Secundarias (informativas, no deciden): IS-CV de M1 y M5 (IC90 por 18 dias, sin los 2 mejores dias), por moneda, placebo de permutacion de (q^ - m) dentro de estratos (dia, moneda, T en tramos de 30 s, m en tramos de 0,02; 200 permutaciones), sensibilidad LR = 60/30 ms (M1 y M5, offset m130), ablacion acumulativa M1 a M5. Calibracion: dLL_pred = media(eps^2 / (2 m (1-m))) frente a realizado.

## 7. Proxy estatico de GP (informativo)
Etiqueta de relleno: primera impresion equivalente (SELL del token a pe o BUY del complementario a 1-p) con pe <= bbl + 0,01 dentro de los 2 s siguientes al tick (puja a bb+0,01 con cola 0; aproximacion de p1 sin latencias LX/LT ni reposicionamientos). Unidad: primer relleno por (mercado, token); EV/acc = y - x + rho(x), x = bbl + 0,01, rho(x) = 0,2*0,07*x(1-x); peso min(tamano, 5)/5. Compuerta eps^ >= c, c en {0; 0,5; 1; 2} pp, con eps^ fuera de muestra (OOF en IS, modelo final en OOS). Se informa dEV = EV(paso) - EV(todos), IC90 por dias (22 dias y solo OOS) y placebo estratificado por PRECIO DE RELLENO: en cada estrato (moneda x centimo del precio de relleno) se sortean tantos rellenos como pasa la compuerta real (500 sorteos). Corrige el defecto del placebo de R2 (estratos en la elegibilidad: +6 pp por deriva te a relleno). La decision de repetir GP la fija la seccion 6; este proxy solo orienta.

## 8. Bloque de identidad del barrendero (atribucion; 2 dias)
Datos: onchain_fills 26 y 27 Oct (keep_onchain_re_as_b, maker/taker explicitos) x m5_registro de esos dias, tokens 5m. Unidad: puja de maker (BUY) en [0,09; 0,31] rellenada; barrendero = campo taker de la fila del maker; barrido = (tx, taker, token). Cruce con las impresiones t por token + precio equivalente (directo SELL a p o espejo BUY a 1-p) + tamano (tolerancia max(0,02; 0,2 %)), ventana de recepcion [bloque - 15 s; bloque + 1,5 s], elegido el mas cercano a -2,4 s; se informa tasa de casado y retardo bloque-recepcion.
Medidas (EV/E = suma tam*(y-p) / suma tam*p; IC90 por bootstrap de mercados, 500): I1 concentracion (top1/5/10, HHI, barrenderos con >= 30 rellenos); I2 persistencia: informados = 20 % peor EV/E entre barrenderos con >= 30 rellenos el dia A, EV/E de sus rellenos el dia B frente al resto (y A y B invertidos) y Spearman entre dias; I3 puerta de cadencia: rellenos del dia B en la misma moneda dentro de (t-60 s, t-5 s] de un relleno de un informado del dia A; I4 cadencia propia: numero de rellenos del mismo barrendero en (t-60 s, t-5 s]; I5 tamano del barrido y makers alcanzados frente a EV/E.
Criterio de termino medible: diferencia de EV/E <= -0,10 con limite superior del IC90 < 0 en AMBAS direcciones (A a B y B a A) y subconjunto senalado >= 5 % de los rellenos; si no, se descarta como feature. Limites declarados: 2 dias = 1 replicacion; el barrendero es una direccion, no una persona; el reloj de bloque llega ~2,4 s tras el casado: NINGUN rasgo de identidad entra en M1-M5.

## 9. Regla sobre el logger L2
Contribucion del libro L1 en M5: s_b = raiz(sigma^2(M5) - sigma^2(M5nb)); s_rest = sigma(M5nb). Cota generosa de L2 (duplicar la informacion de profundidad): sigma_L2max = raiz(s_rest^2 + (2 s_b)^2). Logger L2 justificado solo si sigma_L2max >= 2,1 pp (minimo matematico de la seccion 2) y M5 queda en PARCIAL o EXITO. Si FALLO y sigma_L2max < 2,1 pp: se cierra la familia pasiva L1 (sin logger L2). Reabrir solo con un rasgo nuevo que eleve sigma_eps OOS en >= 1 pp en cuadratura.

## 10. Protocolo y recursos
Smoke de codigo en 2026-10-10 (IS) con out_smoke: no se mira ninguna metrica de decision. Tras este hash solo se admiten correcciones de ERRORES de codigo evidentes (excepciones, formato) antes de ver resultados completos, registradas como REHASH en HASHES_R3.txt con su causa; cualquier cambio de rasgos, umbrales o criterios invalida el prereg y exige version nueva. Recursos: guard load1 < 14 y MemAvailable > 1,2 GB, nice 19, ionice -c3, 2 trabajadores, ulimit 4,5 GB (extraccion) y 6 GB (analisis), fuera de 06:00-09:30Z. Solo escribe en experimentos/5m_barato/formula_r3_28oct/ y misiones/5m_barato/informes/. Sin ordenes, sin .env, sin crons, sin commits.
