# Q-TECHO (OLA 6): techo de precio por orden p_max = q_cons - f - m para B, + politica CONTRA-only + nowcast de acierto (23-Oct-2026, ~11:50Z)
Estado: **EXPLORATORY. Candidata a B: NINGUNA. Beneficio validado: 0 EUR.** Solo lectura (B, ejecutores, crons, config intactos; sin ordenes, sin commits). Prereg `PREREG.md` (sha 850d7101..., `sha256sum -c PREREG.sha256` OK) y `PREREG_ADENDA1.md` (2cd6d875..., CONTRA-only y nowcast; escrita antes de calcular A/B) congelados ANTES de calcular. Hashes de codigo y salidas: `HASHES.txt`. Datos pesados en `/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl` (68 MB; symlink en datalogs). Todo con `nice 19 ionice -c3`, ulimit, un proceso a la vez; $ ~ EUR sin convertir; maker fee 0, rebate NO sumado.
**Que es ask real y que no.** Poblacion de rellenos (tablas de q, techo, CONTRA-only, B) = **precio de relleno real del maker** (no ask; seleccion adversa incluida) con desenlace oficial. **ASK/BID real** (P-REAL, T=180 s+250 ms) solo en el mapa de la sec. 6 y en el nowcast. Nada aqui esta a "precio de modelo" salvo la proxy 2025 del nowcast (residuo gana-q, marcada).

## 0. Respuesta corta (10 lineas)
1. **El techo p_max no funciona: ningun q bate al PRECIO de relleno, y el precio es lo unico que el q "sabe".** En TEST 17-21 (n=36.125 rellenos, 34.560 EUR, walk-forward diario) log-loss: precio pc 0,4952 < MAP 0,4974 < LOGIT-FWD 0,4983 ~ LOGIT-FULL 0,4982 < HGB 0,5011 (indicador R3 0,5070; mid5 0,5097). Los q baten al mid5 (p.ej. MAP-mid5 -0,0122, IC90 cierre -0,0150/-0,0095) pero **pierden contra pc** (MAP-pc +0,0022, IC +0,0013/+0,0030): G-Q1 FALLA. El mid5 es la vara equivocada para un q condicionado a relleno (esta ~3c por encima del precio pagado); la correcta es pc. En DESC (13-16) tambien: pc 0,5198 < MAP 0,5210 < LOGIT 0,5253 < HGB 0,5279 (AUC 0,604/0,590/0,574).
2. **La regla de techo no tiene dPnL (G-Q2 FALLA).** DESC: ninguna de las 18 celdas familia x m tiene dPnL>0 (mejor MAP m=0: -509 EUR, retiene 66 %); seleccion congelada: MAP m=0 (el menos malo; la prereg elige el maximo, no exige >0). TEST: dPnL +425 (IC90 cierre -362/+1.156), p permutacion por cierre 0,456, 3/5 dias, **sin 2 mejores dias -7**, EV retenido -0,043 vs EV total -0,041; **la inversion (saltar la cola ALTA del edge, mismo EUR) da +966 (IC +149/+1.749)**: el edge q-pc no ordena (EV por decil de edge: +0,004 en el peor decil, -0,07..-0,10 en los 4 mejores).
3. **El error sistematico es de PRECIO para el TOMADOR, pero no para el maker**: al ask real (17 dias, ETH/SOL/XRP, n=4.477) acierto - ask = +0,002/+0,009/+0,004/-0,006 por tramo (calibrado) y EV tras fee 0,07 = -0,040/-0,007/-0,033/-0,070. Un bid en reposo SIN condicionar a relleno tendria acierto - bid ~ +0,02 (EV +0,157/+0,104/+0,105/+0,066), y los rellenos de otros makers dan EV +0,02..+0,035: **la seleccion adversa por relleno vale -0,14/-0,08/-0,07/-0,04 por tramo** (descriptivo, periodos distintos). El premio maximo de cualquier filtro es recuperar parte de ese 4-14 %/EUR; un techo de precio no lo ataca (el precio no es el problema, el relleno si).
4. **CONTRA-only (saltar CON, |rpre|>=7,7 bps) es el unico cruce con senal, y es de REGIMEN**: TEST 17-21: EV CON **-0,129** (n=11.468), NEU -0,071, CONTRA **+0,075** (n=11.971); la politica retiene el 68,6 % del EUR con EV retenido -0,001 (IC -0,082/+0,078), dPnL **+1.400** (IC +74/+2.686), p cierre 0,002, 4/5 dias, sin 2 mejores +161, haircut 50 % +700; positivo en las 3 monedas (ETH +667, SOL +455, XRP +278) y en 3 de 4 bloques de 6 h (12-18 UTC -405). **En DESC 09-16 (OOS para la regla) no hay diferencia: CON +0,050, NEU +0,064, CONTRA +0,052; dPnL -1.160 (IC -3.312/+902), p 0,365, 4/8 dias.** CONTRA-CON por dia: media +0,019 en 09-16, +0,249 en 17-21; positivo 9 de 13 dias (sd diaria ~0,3). En B real (202 posiciones, 20-23 Oct): saltar CON quita 60 posiciones con EV -0,368 y deja +0,054 (dPnL +24,4, IC -1,8/+47,3), pero son 4 dias del mismo regimen.
5. **Combinar con techo/r60 no mejora de forma estable**: PC+MAP+r60 TEST retiene 39,9 % con EV +0,029 (IC -0,060/+0,114), dPnL +1.813 (IC +273/+3.259), p cierre 0,006, sin 2 mejores +214; DESC -1.957 (p 0,25). r60 de W2 solo: TEST +269 (p 0,58), DESC -629; **en B real el signo es el contrario** (22 saltadas con EV +0,578, dPnL -13,2).
6. **R2/R3 (en TEST en muestra: +2.260 / +2.196, p 0,0005/0,001, 5/5 dias) NO se reproducen en 09-16** (con mis rasgos reconstruidos del registro): R2 -2.715, R3 -2.743, EV retenido +0,065/+0,083 vs saltado +0,052/+0,047, 2/8 dias. Es decir, la separacion R2/R3 de la poblacion es de 17-21, no estructural en 13 dias (el nivel diario de la poblacion pasa de +0,0556 en 09-16 a -0,0411 en 17-21; dias entre -0,09 y +0,14). Aviso importante para el forward del 02-Nov.
7. **Nowcast de acierto de longshots: NO predice.** Ask real, 17 dias, 9.220 longshots (ask 0,10-0,30), N=6/12/24 ventanas: ninguna de las 12 pendientes primarias pasa Bonferroni 0,0042 (min p 0,011, SOL N=24, pendiente +0,129; pool ETH/SOL/XRP N=12 +0,087 p 0,049; N=24 +0,112 IC90 dias +0,010/+0,197 p 0,057; ETH negativa; BTC/BNB/DOGE de signo mixto); proxy 2025 (n ~75 k por moneda, 349 d, residuo gana-q): pendientes -0,007..+0,023, p 0,43-0,99. Falsos positivos de la prueba con desenlaces sinteticos 3/80 = 3,7 %. MDE (p95 del nulo) 0,08-0,15 por moneda y 0,07-0,12 agrupado en Oct-26: **no podemos excluir una persistencia de ~0,1 en 17 dias, pero en la proxy larga (MDE 0,02-0,06) es <=0,02**.
8. **EV/EUR alcanzable y hueco**: efecto incremental de la unica regla con senal (PC) pooled en 13 dias = +0,015/EUR (EV retenido pooled +0,040, DESC +0,058, TEST -0,001; R3 TEST +0,108 solo en muestra). Con el nocional de X-SALIDA: B actual 25 k$/anio -> **0,4 k EUR/anio (0,2 % de 200 k)**; techo R3 (130 fills x 2,44 $) 116 k$ -> 1,7-6,7 k (0,9-3,4 %); 3 % del flujo del nicho (MAPA-ESCALA 33,9 k EUR/dia x ret 0,686) 255 k$ -> 3,8-14,8 k (1,9-7,4 %); 5 % -> 6,4-24,6 k (3,2-12,3 %). El EV necesario para 200 k seria 8,0 (B), 1,73 (techo R3), 0,79 (3 % del nicho) o 0,47 (5 %). Con la brecha de ejecucion de B (-0,053, MAPA-ESCALA) los niveles de EV pooled/DESC quedan en -0,3..+2 k. **Cierra como maximo el 0,2-3 % del hueco en escenarios medidos y hasta ~12 % solo con 5 % de cuota NO medida y EV de la mitad buena del periodo.**
9. **Lo que falta, exacto**: (i) un simulador de ORDEN (B_FIEL de cola_vs_cruce, reaccion 280 ms, reposicion 1,5 s) con el techo/CONTRA-only dentro para medir la sustitucion; el nivel de unidad aqui es COTA SUPERIOR (E1/R3: la politica real recupera ~la mitad); (ii) L2/posicion en cola (DATA_BLOCKED) para atacar el relleno, que es donde esta la AS; (iii) `m5_registro` 22-23 Oct (el del 22 fallo; extraer `maker_ms` crudo) = dias vírgenes y la mañana mala de hoy (06:30-08:56Z); (iv) >=10 dias forward desde 23-Oct y >=60 dias de P-REAL para el nowcast.
10. **Pasivo con fecha**: PC/R0 ya esta en el gate forward de R-TEND (2-Nov, >=10 dias, >=300 saltadas); Q-TECHO anade solo la lectura de MAP m=0 y r60 con umbrales congelados (`datos/congelado_desc.json`) y exige que el q ordene (decil de edge) antes de hablar de techo; el nowcast se re-corre con P-REAL ampliado (cron propuesto de P-REAL) cuando haya 60 dias con las 6 monedas agrupadas (gate: pendiente>0, p<0,0042, mismo signo en la proxy) = ~5-Dic.

## 1. Datos (que fuente da que)
| Fuente | n | Uso | Notas |
|---|---|---|---|
| `b_seleccion_adversa/datos/units/units_09..21` (poblacion de rellenos de OTROS makers ETH/SOL/XRP 5m, pc (0,10-0,30], T 60-300 s, primeras 5 acc por maker-mercado-lado) | 113.918 (13 d; 21-Oct parcial: 3.318) | todos los q y reglas | desenlace oficial `gana` (build_units solo conserva resueltos; el 100 % se asume del constructor, no recontrolado); EV pond. dia: -0,09..+0,14 |
| rasgos de libro 5m/15m en t_obs=ts-4 s: reextraidos de `m5_registro`/`m15_registro` (`scripts/s1_attach.py`, 13 dias) | cobertura bb 99,9 %, b15 99,8 % | FWD | QA vs `ms_units.pkl` (18-Oct): bb/ba iguales (1e-6) 87 %, b15 90 %, R2 94 % de acuerdo (recepcion vs hora del exchange); **vol30ws no coincide (mediana x0,85, corr 0,68)**: el umbral de R3 (26) es aproximado en mi tabla |
| Binance bookTicker (recepcion) -> r60f (retorno 60 s hasta t_obs, signado por lado) y rpre (ventanas_bookticker) | r60f 88,8 %, rpre 99,7 % | Binance | r60f exige dato <30 s |
| P-REAL `ask_t0` 05-21 Oct (ASK/BID reales T=180+250 ms, 6 monedas, desenlace oficial) | 56.402 token-ventana; 9.220 longshots (ask 0,10-0,30) | mapa precio->acierto y nowcast | |
| `panel_y2025` (proxy Binance, 349 d, residuo gana_proxy - q modelo) | 305.741 filas (solo BTC/ETH/SOL/XRP) | replica de estructura temporal del nowcast | NO es ask real; BNB/DOGE ausentes |
| B real `contabilidad_wallet_dedicada/posiciones.csv` (H47-B liquidadas) | 202, 20-23 Oct | descriptivo | |
| FUERA: Jon-Becker 18-Dic..27-Ene (sin precios de 5m), `m5_registro` 22-23 Oct (fallo del 22), libro L2/cola | - | - | DATA_BLOCKED |
**Division fija**: DESC 09-16 (seleccion interna walk-forward 13-16); TEST 17-21 una pasada (refit diario). Declarado: el agregado 17-21 ya lo vieron otros informes y R2/R3/R1 se eligieron ahi (favorece a las lineas base en TEST; 09-16 es OOS genuino para ellas).

## 2. G-Q1: el q no bate al precio (n=36.125, TEST)
| predictor | log-loss | Brier | AUC | q - pc (logloss, IC90 cierre) | q - mid5 (logloss, IC90 cierre) |
|---|---|---|---|---|---|
| precio de relleno pc | 0,49518 | 0,15904 | 0,6064 | - | - |
| MAP (moneda x tramo 0,05, encogido) | 0,49735 | 0,15972 | 0,5966 | +0,0022 (+0,0013, +0,0030) peor | -0,0122 (-0,0150, -0,0095) mejor |
| LOGIT FWD (C=1, 17 rasgos+Binance) | 0,49829 | 0,16011 | 0,5942 | +0,0031 (+0,0015, +0,0048) peor | -0,0113 mejor |
| LOGIT FULL (+13 rasgos de flujo/FV) | 0,49824 | 0,16005 | 0,5964 | +0,0031 peor | -0,0113 mejor |
| HGB FWD (prof. 3, isotonica) | 0,50109 | 0,16077 | 0,5845 | +0,0057 (+0,0033, +0,0082) peor | -0,0087 mejor |
| indicador R3 (media por bandera) | 0,50702 | 0,16281 | 0,5175 | | |
| mid5 (bb+ba)/2 en t_obs (n=36.089) | 0,50967 | 0,16456 | 0,5838 | | |
Versus MAP: LOGIT +0,0009 (IC -0,0003/+0,0022), HGB +0,0035 (+0,0013/+0,0057, peor). Ningun rasgo anade informacion fuera de muestra sobre el precio (coincide con el logit anterior AUC 0,604). Fiabilidad del q primario por decil: la calibracion global es buena (q 0,131..0,298 vs acierto 0,130..0,283) salvo el decil (0,184-0,200] con q 0,193 y acierto 0,138 (EV -0,225, n=4.129): un solo tramo de precio (pc ~0,18-0,20) concentra la perdida del periodo (post-hoc; 1 de 10 deciles).

## 3. G-Q2/G-Q3: techo de precio (TEST, precio de relleno real del maker)
| regla | skip/n | ret | EV ret [IC90] | EV skip | dPnL [IC90 cierre] | p cierre | dias+ | sin 2 mejores | haircut 50 % |
|---|---|---|---|---|---|---|---|---|---|
| **PRIMARIA MAP m=0** (congelada en DESC) | 11.388 | 0,674 | -0,043 [-0,108,+0,022] | -0,038 | +425 [-362,+1.156] | 0,456 | 3/5 | -7 | +213 |
| inversion (cola alta del edge, mismo EUR) | 12.322 | 0,674 | -0,019 | -0,086 | +966 [+149,+1.749] | n/a | 3/5 | +161 | +483 |
| H-r60 (r60f <= p20 DESC por moneda) | 5.885 | 0,847 | -0,039 | -0,051 | +269 [-457,+975] | 0,584 | 3/5 | -274 | +134 |
| R0 / CONTRA-only (CON) | 11.468 | 0,686 | -0,001 [-0,082,+0,078] | -0,129 | +1.400 [+74,+2.686] | 0,002 | 4/5 | +161 | +700 |
| R2 (en muestra) | 25.912 | 0,290 | +0,084 | -0,092 | +2.260 [+439,+4.026] | 0,0005 | 5/5 | +738 | +1.130 |
| R3 (en muestra) | 28.810 | 0,209 | +0,108 [-0,054,+0,264] | -0,080 | +2.196 [+295,+4.005] | 0,001 | 4/5 | +582 | +1.098 |
| q a retencion igualada con R3 (0,209) | 30.517 | 0,209 | -0,027 | -0,045 | +1.227 [-640,+3.017] | 0,597 | 3/5 | +185 | +614 |
| q-cap DENTRO de R3 (7.315 retenidas) | 2.126 | 0,700 | +0,074 | +0,187 | **-405** [-817,+6] | 0,755 | 2/5 | -438 | -203 |
- G-Q3: dPnL(primaria) - dPnL(R0) = -975 (IC -2.137/+213); dPnL(q a retencion R3) - dPnL(R3) = -969 (IC -2.040/+187). El q no bate a R0 ni a R3; dentro de R3 el techo quita rellenos buenos (EV saltado +0,187).
- Rejilla descriptiva familia x m en TEST (30 celdas, multiplicidad declarada): el dPnL crece monotonamente con lo que se salta (m=0,06 salta todo: +1.419 = -PnL total del periodo); **ninguna celda tiene EV retenido >0 con IC90 por encima de 0**; la unica con IC90 de dPnL >0 es LOGIT-FULL m=0 (+839, IC +19/+1.676; rasgos no desplegables), 1 de 30.
- Por moneda (primaria): ETH +440, SOL -135, XRP +119. EV retenido: ETH -0,071, SOL +0,014, XRP -0,025.
- **Sustitucion no modelada**: todas las dPnL de unidad son cota superior (E1: la politica real conserva ~la mitad; R3: "R3 verdadero" +0,025 vs politica R3 -0,041).

## 4. CONTRA-only como politica de maker completa (ADENDA 1 A; rellenos, no ask)
| periodo | clase | n | EUR | acierto | pc | EV/EUR |
|---|---|---|---|---|---|---|
| DESC 09-16 | CON | 24.171 | 23.394 | 0,2236 | 0,2128 | +0,050 |
| | NEU | 27.145 | 26.458 | 0,2265 | 0,2122 | +0,064 |
| | CONTRA | 26.118 | 25.283 | 0,2221 | 0,2118 | +0,052 |
| TEST 17-21 | CON | 11.468 | 10.863 | 0,1849 | 0,2110 | **-0,129** |
| | NEU | 12.662 | 12.193 | 0,1980 | 0,2112 | -0,071 |
| | CONTRA | 11.971 | 11.486 | 0,2301 | 0,2109 | **+0,075** |
Por moneda TEST (CON/CONTRA): ETH -0,107/+0,029, SOL -0,147/+0,138, XRP -0,183/+0,134. Por bloque 6 h TEST: CONTRA +0,31 en 06-12 UTC, -0,09/-0,06 en 00-06 y 18-24; CON -0,20..-0,25 salvo 12-18 (+0,14). Por dia CONTRA-CON: 09..21 = -0,33, +0,17, +0,20, -0,27, +0,11, +0,29, +0,09, -0,11 | +0,10, +0,31, +0,42, -0,12, +0,54 (`datos/q_techo_dia_clase.txt`).
Politicas (retencion en EUR; precio = relleno maker; IC90 por cierre; p por permutacion por cierre; Bonferroni 0,05/5 = 0,01 para las 5 combinadas):
| politica | DESC dPnL [IC] (ret, p, dias+) | TEST dPnL [IC] (ret, EV ret, p, dias+, sin 2 mejores) |
|---|---|---|
| PC = saltar CON | -1.160 [-3.312,+902] (0,69; 0,37; 4/8) | +1.400 [+74,+2.686] (0,69; -0,001; 0,002; 4/5; +161) |
| PC+MAP | -1.858 [-4.122,+260] (0,51; 0,43; 3/8) | +1.488 [+66,+2.860] (0,47; +0,004; 0,021; 4/5; +172) |
| PC+r60 | -1.337 [-3.678,+869] (0,59; 0,18; 4/8) | +1.687 [+290,+3.015] (0,59; +0,013; 0,004; 3/5; +122) |
| PC+MAP+r60 | -1.957 [-4.370,+362] (0,43; 0,25; 3/8) | +1.813 [+273,+3.259] (0,40; +0,029; 0,006; 4/5; +214) |
| PC+R3 (retener R3) | -2.957 [-6.154,-9] (0,22; 0,33; 2/8) | +2.097 [+106,+3.920] (0,20; +0,100; 0,0015; 4/5; +601) |
- Respuestas: **(a) el EV de los rellenos CONTRA se mantiene?** en 17-21 si (+0,075; 4/5 dias), en 09-16 no distingue (+0,052 igual que CON). **(b) volumen**: PC retiene 69 % del EUR (CON es el 31 %). **(c) concentracion**: TEST repartida en las 3 monedas; por hora el dPnL sale de 00-12 y 18-24 UTC y pierde en 12-18; DESC pierde en ETH y SOL.
- Pooled 13 dias: EV total +0,025, EV retenido PC +0,040, **dEV incremental +0,015** (IC cruza 0). Es la cifra honesta de lo que PC aporta como nivel medio; el +0,13 por CON-vs-CONTRA de TEST es del regimen 17-21.
- Coherencia con P-REAL: al ask real del tomador, CON rinde -0,159 y CONTRA +0,075 en 17 dias (05-21); para los rellenos del maker 09-16 la brecha no aparece (precio pagado igual, 0,2128 vs 0,2118, y acierto igual), es decir, **la causa de PRECIO del tomador no se traslada al maker; el efecto del maker en 17-21 es de acierto (0,185 vs 0,230)**. Uno de los dos periodos esta mal representado: 09-16 podria ser un regimen sin efecto o 17-21 un regimen con efecto; ni 13 dias ni 17 permiten distinguirlo.

## 5. Nowcast de acierto de longshots (ADENDA 1 B; ASK real, EV "gana - ask")
Pendiente OLS del residuo de la ventana-moneda siguiente sobre la media de residuos de las N ventanas cerradas anteriores (>= N/3 longshots; agrupado >= 2N/3); p unilateral por permutacion intradia de residuos entre tokens del mismo dia (conserva el nivel del dia: contrasta persistencia INTRADIA por encima del dia); IC90 por dias (bootstrap de dias); calibracion con Bernoulli(ask), e=0: 3/80 falsos positivos al 5 % nominal.
| | N=6 | N=12 | N=24 |
|---|---|---|---|
| ETH | -0,025 (p 0,68) | -0,030 (0,64) | -0,019 (0,51) |
| SOL | +0,025 (0,26) | +0,070 (0,063) | **+0,129 (0,011)**, IC dias [-0,000,+0,241] |
| XRP | -0,020 (0,75) | +0,082 (0,124) | +0,055 (0,38) |
| agrupado ETH+SOL+XRP | +0,036 (0,18) | +0,087 (0,049) | +0,112 (0,057), IC dias [+0,010,+0,197] |
| replicas BTC / BNB / DOGE | +0,048 / -0,006 / +0,041 | -0,030 / -0,034 / +0,068 | -0,004 / -0,014 / +0,034 |
| proxy 2025 ETH/SOL/XRP/BTC (349 d) | -0,001 / +0,005 / +0,007 / +0,012 | +0,009 / -0,007 / +0,016 / +0,015 | +0,014 / -0,005 / +0,023 / +0,002 |
Bonferroni 0,05/12 = 0,0042: **ninguna pasa**. Lectura: sesgo positivo en el agrupado (0,04-0,11) coherente con regimen intradia, pero p 0,05-0,06 y MDE ~0,09-0,12; en la proxy 2025 (MDE 0,02-0,06) la persistencia es <=0,02. Regla derivada NO calculada (no se cumple la condicion de la prereg). **El dia malo de hoy (06:30-08:56Z, 13,0 % vs 24,8 %)**: NO evaluable aqui (sin `m5_registro` 22-23 Oct); es un episodio, y con un MDE de ~0,1 en 17 dias no basta para decidir. Dato exacto que falta: el registro ms de 22-23 Oct (extraccion de `maker_ms` crudo antes de que rote) + >=40 dias mas de P-REAL.

## 6. Mapa precio->acierto con ask/bid REAL y seleccion adversa (descriptivo, `datos/preal_mapa.txt`)
ETH/SOL/XRP, tramos (0,10-0,15], (0,15-0,20], (0,20-0,25], (0,25-0,30]:
| | n | acierto - px | EV |
|---|---|---|---|
| ASK real tomador T=180+250 ms, fee 0,07 | 1.435/1.158/1.016/868 | +0,002/+0,009/+0,004/-0,006 | -0,040/-0,007/-0,033/-0,070 |
| BID real en reposo sin condicionar a relleno (fee 0) | 1.337/1.160/979/843 | +0,020/+0,019/+0,024/+0,019 | +0,157/+0,104/+0,105/+0,066 |
| Rellenos de otros makers 09-21 (precio de relleno, fee 0) | 24.057/27.026/28.839/33.996 | +0,002/+0,004/+0,009/+0,008 | +0,020/+0,020/+0,035/+0,023 |
| **AS por relleno** (relleno - bid sin condicionar) | | | -0,137/-0,084/-0,071/-0,043 |
Por moneda el acierto - ask es ruidoso (ETH tramo 0 +0,093 EV, XRP tramo 3 -0,180; n 260-660). BTC/BNB/DOGE: acierto - ask -0,019/-0,012/+0,008/+0,009 (EV -0,195/-0,115/-0,018/-0,017). Lectura: el mercado esta calibrado en el agregado (no hay "longshots baratos" que un techo pudiera explotar) y la perdida del maker es **de relleno** (se llena cuando el precio ya va contra el), consistente con E1/S1/cola_vs_cruce.

## 7. B real (202 posiciones H47-B, 20-23 Oct, EV -0,072, 19,3 % de acierto; DESCRIPTIVO)
R0/PC: salta 60 (EV -0,368), retiene 142 con EV +0,054, dPnL +24,4 (IC cierre -1,8/+47,3). MAP techo m=0: salta 80 (EV -0,177), dPnL +15,5 (-20,1/+47,3); m=0,01 +19,8; m=0,02 +23,2 (retiene 17,6 %). r60: dPnL -13,2. Dias: 20-Oct +0,070 (37), 21 +0,166 (72), 22 -0,267 (77), 23 -0,584 (16): el resultado de B esta dominado por el dia. Nada de esto es un gate.

## 8. EV/EUR, EUR/anio y hueco a 200.000 (nocional de X-SALIDA y MAPA-ESCALA; `datos/q_techo_hueco.txt`)
| nocional anual | dEV +0,015 (PC incremental, pooled) | EV +0,040 (PC retenido, pooled) | EV +0,058 (PC en DESC) | EV +0,108 (R3, TEST en muestra) | EV/EUR necesario para 200 k |
|---|---|---|---|---|---|
| B actual 25 k | 0,4 k (0,2 %) | 1,0 k (0,5 %) | 1,4 k (0,7 %) | 2,7 k (1,3 %) | 8,0 |
| techo R3 116 k | 1,7 k (0,9 %) | 4,6 k (2,3 %) | 6,7 k (3,4 %) | 12,5 k (6,3 %) | 1,73 |
| 3 % del nicho (33,9 k EUR/dia x ret 0,686) 255 k | 3,8 k (1,9 %) | 10,2 k (5,1 %) | 14,8 k (7,4 %) | 27,5 k (13,8 %) | 0,79 |
| 5 % del nicho 424 k | 6,4 k (3,2 %) | 17,0 k (8,5 %) | 24,6 k (12,3 %) | 45,8 k (22,9 %) | 0,47 |
Con IC: el EV retenido de PC en DESC es +0,058 (IC90 +0,005/+0,118) y en TEST -0,001 (-0,082/+0,078): el rango anual del 3 % es -0,2..+30 k. La cuota (3-5 %) NO esta medida (escenario); restar la brecha de ejecucion de B (-0,053) a los niveles de EV deja el 3 % en -3,3..+1,3 k. El unico numero cercano a "mover la aguja" (R3 TEST 5 % cuota, 46 k) es EN MUESTRA y no se reproduce en 09-16. **Fraccion del hueco cerrada por Q-TECHO con lo validado: 0 %; por los escenarios medidos con IC: 0,2-7 % (3 % de cuota), hasta ~12 % solo con 5 % de cuota y el EV de la mitad buena.**

## 9. Regla candidata, gate y fecha
- **Candidata: NINGUNA.** No hay ni q que bata al precio (G-Q1) ni regla con dPnL IC>0 y p<0,0167 de la familia techo (G-Q2); PC pasa p en TEST pero falla el OOS 09-16 (DESC -1.160). Etiqueta: **REJECTED para el techo de precio; EXPLORATORY/REGIMEN para CONTRA-only; REJECTED para el nowcast con los datos actuales**.
- **Pasivo con gate congelado**: (1) CONTRA-only/R0 ya corre en el forward de R-TEND (>=10 dias desde 23-Oct, >=300 saltadas, IC90 cierre dPnL>0, placebo p<0,0167, >=60 % dias, sin 2 mejores, EV retenido > base): **2-Nov**; Q-TECHO anade como control que el EV de CONTRA-CON sea >0 en la poblacion en >=7 de 10 dias y que el dia de regimen (EV total del dia) no explique el dPnL (regresion dPnL ~ EV_dia). (2) Techo MAP m=0 y r60: mismas fechas, solo informativos (umbrales en `datos/congelado_desc.json`); no se exige nada mas hasta que el decil de edge ordene. (3) Nowcast: re-correr `scripts/s8_nowcast.py` con P-REAL ampliado; gate = pendiente agrupada de 6 monedas >0, p<0,0042, mismo signo en proxy; con SE actual ~0,05 se necesitan ~60 dias (~5-Dic si el cron de P-REAL se instala).
- **Segunda ronda propuesta (sin coste de datos nuevos)**: (a) simulador de orden B_FIEL con PC/techo/r60 (mide sustitucion y reposicion); (b) descomponer el nivel diario de la poblacion (que hace buen o mal dia: -0,09..+0,14) con variables de mercado ya en el registro (vol realizada 1 h, ER60, hora), porque domina todos los dPnL; (c) extraer 22-23 Oct de `maker_ms` crudo para el OOS virgen y la mañana mala.

## 10. Limites y desviaciones declaradas
- La seleccion en DESC tomo "mayor dPnL sujeto a ret>=25 % y EV_ret>EV_all": como ningun dPnL>0, eligio el menos malo (MAP m=0); se informa. Seleccion de C del LOGIT: C=1 (diferencias de 4e-5 entre valores).
- El primer lanzamiento de `s3_modelo.py` calculo la fase 1 (log en `datos/q_techo_fase12_desc.log`) y se interrumpio en el HGB-FULL de TEST por oversuscripcion de hilos (load 20); la fase 2 se recalculo con `s3b_test.py` (mismo codigo/semilla, sin HGB-FULL, OMP_NUM_THREADS=4). HGB-FULL no se evaluo (diagnostico).
- Tramos: un bug de bucketing (off-by-one) en el primer mapa P-REAL se corrigio antes de usar ningun resultado; las tablas son las corregidas.
- Rasgos: t_obs = ts-4 s para todo (el rasgo de decision real de B estaria mas fresco: hasta ~1-2 s, lo que podria o no mejorar q; E1 mostro que solo ~8 % del coste tiene senal <100 ms antes del relleno). r60f/rpre faltan 11 %/0,3 % (no saltados cuando faltan).
- Poblacion = rellenos de otros makers (5 acc primeras), no la seleccion propia de B (cola, repegados). EV de 17-21 y de 09-16 son de regimenes distintos; sin 22-23 Oct.
- vol30ws de mi tabla no es el del shadow R3 (x0,85): R3 aqui es aproximada; R2 (solo b15/pc) es robusta (94 % de acuerdo con `ms_units`).
- Multiplicidad: 3 familias x 6 m en DESC; en TEST 3 hipotesis (Bonferroni 0,0167), 5 combinadas (0,01), 12 contrastes del nowcast (0,0042); la rejilla de 30 celdas y las lineas base son descriptivas.
- Maker fee 0, rebate no contado (+0,011 si llegara a pagarse). $ no convertidos a EUR (restaria 10-15 %).

## 11. Reproducir
`cd .../q_techo; for d in 2026-10-09..21: python3 -I scripts/s1_attach.py $d` (65-150 s/dia, `ulimit -v 5000000`; `scripts/run_s1.sh`) -> `scripts/s2_feat.py` -> `scripts/s3_modelo.py` (fase 1; ~25 min con carga alta) -> `scripts/s3b_test.py` -> `scripts/s4_eval.py`; `s5_preal_mapa.py`, `s6_b.py`, `s7_contra.py`, `s8_nowcast.py [--solo-proxy]`. Todo `nice -n 19 ionice -c3`, OMP_NUM_THREADS=4, fuera de 06-09Z. Salidas en `datos/`; tabla de modelado en el volumen grande.
