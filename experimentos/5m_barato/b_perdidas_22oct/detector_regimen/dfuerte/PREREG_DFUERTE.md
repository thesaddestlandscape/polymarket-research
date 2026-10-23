# PREREG D-FUERTE (23-Oct-2026 ~07:55Z) - detector de regimen de ventana 5m FUERTE (OLA 5)
Congelado ANTES de calcular ningun modelo, AUC, I_det ni DeltaPnL con desenlaces. Antes de este fichero solo se han descargado datos (klines publicas Binance con volumen) y escrito codigo de rasgos sin tocar desenlaces. Todo lo posterior a ver resultados va marcado POST-HOC. `sha256sum -c PREREG_DFUERTE.sha256`.
Solo lectura: B, ejecutores, modulos compartidos, crons y config intactos; sin ordenes, sin claves, sin commits. Unico dato externo: GET publico de klines 1m Binance (sin clave).

## 1. Etiqueta objetivo (causal, no depende del ask)
Poblacion = ventanas 5m (apertura t_o multiplo de 300 s) con unidad "longshot" del PREREG_RTEND (T=180 s; lado que VA PERDIENDO con q=Phi(-z) en [0,10;0,30); z=|ret|/(s60*sqrt(m)), s60 = desv. 1m de los 60 min previos a t_o+T) y |rpre|>=7,7 bps (rpre = ret de los 15 min previos a t_o). Unidad CON si el lado longshot coincide con sign(rpre), CONTRA si no.
Direccion CON de la ventana: o = sign(rpre) (Up si rpre>0). Para cada unidad: p_con = q (CON) o 1-q (CONTRA) = prob. de modelo de que gane el lado CON; y = 1[gana el lado CON] (CON: y=win_longshot; CONTRA: y=1-win_longshot). Residuo r_con = y - p_con. Equivalencias: e(CON) = r_con; e(CONTRA) = -r_con; Delta = EV(CON)-EV(CONTRA) es el contraste que la etiqueta mide. Desenlace: proxy Binance (S_A, S_D, reciente) u OFICIAL Jon-Becker (S_B). "A precio real donde exista": S_C (pop 17-22 Oct, baratas 5-14 Oct) con PnL en EUR.
Todos los rasgos se calculan con barras 1m CERRADAS <= t_o y se ORIENTAN por o cuando se indica (para que "a favor de CON" sea +).

## 2. Rasgos (familias; 1m OHLCV Binance spot; BASE = logit(p_con) en todos los modelos)
F1 tendencia multiescala orientada: o*(lp[t_o]-lp[t_o-k])/(s60*sqrt(k)), k en {5,15,30,60,120,240,720,1440}, recortada a +-8; |z15|.
F2 eficiencia/Hurst local: ER15, ER60, ER240; VR240 y VR (r15 vs r1 en 1440); pendiente log-var vs log-m (m=1..32, ventana 720 min) /2 = Hurst; autocorr lag1 de r1 (240) y de r5 no solapado (1440).
F3 volatilidad: s60/s1440 (VOLR), RV15/RV60, RV5/RV60, log(s60/mediana 14 d previos de s60 de la moneda), log s60 en bps, ratio Parkinson (H-L) 15m vs cierre, rango de la ultima barra / s60. (La vol IMPLICITA del mercado NO se incluye: no hay historico; ver sec.9.)
F4 asimetria y saltos: skew de r1 (60, 240) orientada por o, curtosis 240, max|r1|/s240 en 60 min, razon de salto con bipower (1-BV/RV, 60 min), nº de |r1|>3*s240 en 60, signo*tamano del mayor salto orientado.
F5 volumen y flujo de Binance: desbalance taker (2*tbv-vol)/vol acumulado 5/15/60 min orientado por o; vol15/(media 15 min de las 24 h previas); vol5 igual; ntr ratio; tamano medio de trade vs 24 h.
F6 coherencia entre monedas (BTC,ETH,SOL,XRP, misma t_o): media orientada por o de los z15 de las otras monedas; fraccion de monedas con sign(r60)=o; z15 de BTC orientado (si la moneda es BTC, media de las otras); dispersion de z15 entre monedas; z15 propio menos media de las otras; media orientada de z60 de las otras.
F7 tiempo/identidad: hora UTC (sin,cos), dia de semana (sin,cos), sesion USA (13:30-20:00 UTC), minutos desde 00:00 UTC, dummies de moneda.
F8 posicion en el rango: distancia en sigmas (s60) al max y al min de 24 h orientada por o; posicion en rango 24 h, 4 h y rango del dia UTC en curso (0..1, orientada); distancia al max/min del dia UTC anterior orientada; minutos desde el extremo de 24 h en la direccion CON (/1440).
Rasgo NaN -> mediana del entrenamiento (logistica) o nativo (GBM). Estandarizacion con media/desv. del entrenamiento.

## 3. Modelos candidatos (K = 11, declarados; ninguno mas se evalua para decidir)
M1..M8: logistica L2 (C=0,02, lbfgs, max_iter 400) sobre BASE + una familia F1..F8 (cada una sola). M9: logistica BASE+F1..F8 (C=0,02). M10: HistGradientBoostingClassifier (max_depth 3, max_iter 150, lr 0,03, min_samples_leaf 500, l2 10, sin early stopping, semilla 1) sobre BASE+F1..F8. M11: como M9 pero ajustada solo sobre unidades CON con y=win_longshot (aplicada a todas).
Salida: s_hat = P(y=1|X,p_con) - p_con (residuo previsto del lado CON; s_hat<0 = "regimen en que CON rinde peor"). Hiperparametros FIJOS (no se ajustan). Controles fuera de K: C0 = solo BASE + dummies de moneda; C1 = bandera R-TEND (TREND=-1, REVERT=+1, MIXTO/NA=0; mismas definiciones que `regimen_lib.add_classes`); C2 inversion (-s_hat); C3 s_hat permutado dentro de dia x moneda.

## 4. Particion temporal y walk-forward por MESES (nada se ajusta con todo el periodo)
Muestras: S_D 2025-01-01..2025-12-16 (proxy, 4 monedas); S_B 2025-12-17..2026-01-28 (4 monedas; desenlace OFICIAL en las unidades con Jon-Becker); S_A 2026-03-26..2026-06-24 y 2026-07-13..2026-08-17 (6 monedas; ETH,SOL,XRP primarias, BTC/BNB/DOGE replica); RECIENTE 2026-09-24..2026-10-22 (klines publicas, 4 monedas). Calentamiento de 14 d para las referencias de mediana (minimo 5 d presentes; si no, NaN).
Para cada mes calendario de test M: entrenar con todas las unidades de meses anteriores (expansion), purgando el dia anterior a M; minimo 3 meses de entrenamiento. FASE D (descubrimiento) = meses de test 2025-04..2025-12(16). FASE T (TEST, jamas usada para elegir) = 2025-12-17..2026-01-28, 2026-03..2026-08, y RECIENTE evaluado con el modelo CONGELADO (sec.7) entrenado hasta 2026-08-17.
Seleccion en FASE D: modelo* = el de mayor AUC_strat agregado fuera de muestra (sec.5a) entre los K; tau* = argmax del exceso de DeltaPnL (sec.5c) en FASE D, sobre la rejilla tau en {0,00; 0,01; 0,02; 0,03; 0,05} (reglas: saltar unidades CON con s_hat <= -tau). Congelados antes de mirar FASE T.

## 5. Metricas (siempre fuera de muestra)
(a) AUC_strat: AUC de s_hat vs y dentro de estratos de p_con (cubos 0,05), media ponderada por n+*n-; por mes; agregado; solo CON; solo CONTRA. IC90 por bootstrap de DIAS (2000). Referencia: C0 y C1 (el detector debe batir a C1 y a C0).
(b) I_det = Delta(tercil inferior de s_hat) - Delta(tercil superior), terciles globales del periodo evaluado (solo rasgos, sin desenlaces); Delta con EV/EUR a precio de modelo. IC90 y p dos colas por bootstrap de dias (2000); signo por mes; por moneda. Comparable a I_R(R-TEND) = -0,073.
(c) Curva DeltaPnL vs tau: DeltaPnL = -Sum e de las unidades CON saltadas (acciones iguales, precio de modelo); exceso = DeltaPnL - esperanza del placebo (mismo nº de saltos por dia x moneda x cubo q, calculada analiticamente); IC90 de dias; placebo por permutacion (500) y p; INVERSION (saltar s_hat >= +tau) y C3. Tambien EV/EUR de las saltadas y fraccion saltada.
(d) Precios reales (solo modelo congelado): S_C pop 17-22 Oct y baratas 5-14 Oct (sin 14 Oct fuera): regla tau*, DeltaPnL en EUR, IC90 por cierre, placebo (como r3_precios), por dia. p_con = precio pagado de la unidad (aproximacion declarada: el modelo se entreno con q de modelo).
(e) Multiplicidad: se declaran K=11 modelos y 5 umbrales. p del modelo* en FASE T se reporta crudo y x11 (por modelos) y x55 (estricto, modelos x umbrales). Todas las demas celdas (monedas, meses) son descriptivas.

## 6. Criterio de ACEPTACION (FASE T, modelo* y tau* congelados)
TODO a la vez: (1) AUC_strat agregado >=0,60 y >=0,60 en >=75 % de los meses de test; (2) I_det<0 con p corregido (x11) <0,05; (3) signo de I_det negativo en >=75 % de los meses y en >=2 monedas independientes (cada una con I_det<0 y IC90 de dias inferior al 90 % de su cola...: se exige I_det<0 y p una cola <0,10); (4) exceso de DeltaPnL (tau*) >0 con IC90 de dias >0, placebo p<0,05, y mayor que el de C1; (5) en precios reales (S_C) DeltaPnL>0 sin empeorar la regla incondicional. Si falla cualquier punto: NO aceptado (se informa el que falla y que feature/dato falta).
Se reporta tambien el techo realista: si AUC<0,55 en todos los modelos, el detector causal con estos rasgos NO discrimina de forma fuerte (resultado valido).

## 7. Entregables congelados
Si algun modelo supera el listado, se congela el modelo* entrenado hasta 2026-08-17 (pesos o pickle + sha256 + tau*). Etiquetador forward pasivo `etiquetar_dfuerte.py` (solo lectura de klines publicas diarias + archivo propio; rasgos y score para p_con en {0,10..0,29}) y evaluador/gate (como R-TEND: >=10 dias forward, >=300 unidades saltadas, exceso con IC90 por cierre >0, placebo p<0,05, dP>0 en >=60 % de dias, sin los 2 mejores dias >0).
## 8. Sensibilidades (no deciden)
T=120; unidades NEU; monedas BTC/BNB/DOGE; sin F7 (hora/dia); sin F5 (si el flujo no estuviera disponible en forward).
## 9. NO probado (declarado): vol implicita/mid del mercado y sesgo de lado de los rellenos (sin historico mas alla de 5-22 Oct: requiere extraer m5_registro/libro5_ms del mid a la apertura), 15m, Hurst R/S clasico, perps (CVD/OI) por falta de historico.
