# TESTS BARATOS T1-T3 (10-Nov-2026). Solo lectura, 0 ordenes. Datos 20-23 Oct (4 dias = 4 observaciones independientes, 129 clusters dia-ventana 5 min). EV ponderado por EUR (Sigma pnl/Sigma coste), rebate 0 | 0,2, desenlace oficial (`gana` de ordenes_b), IC90 bootstrap por cluster.
Codigo: verif_t2.py, analiza_t2.py (T2), t1_makers.py, analiza_t1.py (T1), t3_ledger.py (T3). Salidas: out/T2_<dia>.pkl, out/T1_tx.pkl, out/t3_stdout.txt, out/{ordenes_soporte,bloqueos,cancela_banda}.pkl. Sin commit. Reutiliza V_*.pkl, ownfills_*.pkl, ordenes_b.csv, b_fills_onchain.csv, onchain_fills_2026-10-2[0-3].csv.gz, experimento_h47_B_ledger.jsonl.

## T1 CIRCULARIDAD FN (131) vs TP (71) — dictamen: la circularidad se CONFIRMA; "toxicidad en barridos rapidos" NO se sostiene (ni se refuta)
Estructura on-chain del primer tx de cada relleno real (202 ordenes, 215 tx, 100 % casados por order_hash; tomador = suma de acciones de nuestro token en el tx):
| | n | tx con 1 solo maker (=solo nuestra orden) | n_makers 1/2/3/4+ | tamano tomador S_tok mediana (p25-p75) | acciones de OTROS makers mediana |
| FN | 131 | 69,5 % | 91/33/5/2 | 5,0 (5,0-8,2) | 0 |
| TP | 71 | 39,4 % | 28/38/2/3 | 6,9 (5,0-11,0) | 1,39 |
Mann-Whitney S_tok p=0,0005; n_makers p=0,0001; Fisher "solo nosotros" p<0,001. Con el motor sin fuga (WSXS, T2): TPx 73 con 39,7 % solo / FNx 129 con 69,8 %. Es decir, los FN son sobre todo tx donde solo consumio nuestra orden (sin print de otros), y los TP son barridos multi-maker.
EV (rebate 0 | 0,2), IC90 clusters:
- TP n=71 (60 cl) acierto 16,9 %: -0,213 [-0,53;+0,16] | -0,202. FN n=131 (88 cl) acierto 20,6 %: +0,014 [-0,32;+0,38] | +0,025. Todos n=202: -0,072 | -0,061 [-0,31;+0,21].
- Por n_makers (todos los reales, sin etiqueta del motor): solo-nuestra n=119 -0,076 [-0,37;+0,25]; multi n=83 -0,067 [-0,45;+0,35] => NO hay diferencia de EV entre tx solo-nuestros y multi-maker.
- Estandarizando FN-TP por estrato (n_makers x tamano tomador {<=5,5-7,7-10,>10}): diferencia +0,151 [-0,37;+0,71] (rb0) / +0,151 [-0,41;+0,70] (rb0,2); bruta +0,227. La separacion bruta se reduce 1/3 al controlar y su IC cruza 0.
- Celdas (todas n<=43, 8-26 cl): S_tok>10: TP -0,75 [-1,0;-0,26] (n=22) vs FN +1,45 [+0,27;+2,71] (n=23); multi: TP -0,49 [-0,81;-0,10] (n=43) vs FN +0,50 [-0,22;+1,37] (n=40); solo: TP +0,20 vs FN -0,17 (signo contrario, IC cruzan 0); S_tok 7-10: TP +0,54 vs FN -0,24. El signo FN/TP se invierte entre estratos => es ruido de n pequeno + seleccion por el motor, no una toxicidad estable.
- Por moneda (rb0,2): ETH TP -0,52 [-0,88;-0,14] n=38 vs FN +0,61 [-0,05;+1,34] n=41; SOL TP +0,54 [-0,45;+1,56] n=16 vs FN -0,30 [-0,68;+0,12] n=48; XRP TP -0,20 n=17 vs FN -0,20 n=42 (identicos). Solo ETH separa, SOL va al reves.
- Por dia (rb0,2): 20-Oct +0,16/+0,04 (TP/FN), 21-Oct +0,09/+0,28, 22-Oct -0,75 [-0,99;-0,25]/-0,09, 23-Oct -0,99/-0,24 (TP n=6). Sin consistencia entre dias.
Decide: la toxicidad medida por TP vs FN esta confundida con el tamano del tomador y con la definicion (el motor solo "ve" tx con otros makers). Controlando n_makers/tamano, IC cruza 0; ningun resultado se llama positivo ni toxico. Dato que lo cerraria: mas dias con ordenes reales (solo hay 4) o el tamano del tomador ya en el ledger.

## T2 CINTA WS: separar reloj/emparejado de motor — dictamen: del 0,35 casi nada es reloj/emparejado; ~0,11-0,14 es motor (cola); el resto (~0,5) es no-observabilidad de tx "solo nuestra orden"
Motor passT adaptado, mismas 3.796 ordenes y segmento [t_ini,t_fuera] (verif.py), BASE/OPT (OPT = cola 0). WSI = prints WS incluyendo nuestras filas (check: WSI_BASE == WSBASE_f_q de verif.py, True); WSXS = resta NUESTRO share al print que casa con nuestro tx (solo fills con src ws_match, 85,6-92 %: fuga residual en el resto); WSXD = descarta el print entero.
| variante (n=3.796; reales=202) | sim | tp | precision | recall | recall vida>=1,5 s (n=898, reales 117) |
| chain BASE (previo) | 100 | 71 | 0,710 | 0,351 [0,30;0,41] | 0,359 (prec 0,824) |
| chain OPT | 143 | 85 | 0,594 | 0,421 | 0,419 |
| WSI BASE (con nuestras filas, FUGA) | 112 | 103 | 0,920 | 0,510 [0,46;0,56] | 0,504 (prec 0,983) |
| WSI OPT (FUGA) | 196 | 178 | 0,908 | 0,881 | 0,915 |
| WSXS BASE (limpia) | 82 | 73 | 0,890 [0,83;0,94] | 0,361 [0,31;0,42] | 0,359 (prec 0,977) |
| WSXS OPT (limpia) | 114 | 96 | 0,842 | 0,475 | 0,487 |
| WSXD BASE | 53 | 44 | 0,830 | 0,218 [0,17;0,27] | 0,222 |
| WSXD OPT | 71 | 53 | 0,746 | 0,262 | 0,274 |
Por moneda, recall BASE chain / WSI / WSXS / WSXD: ETH 0,481/0,557/0,405/0,253 (79 reales); SOL 0,250/0,469/0,297/0,172 (64); XRP 0,288/0,492/0,373/0,220 (59).
Lectura: (1) cambiar la fuente de cinta (cadena->WS) sin fuga mueve recall 0,351->0,361 (dentro del IC): RELOJ/EMPAREJADO ~0,01 de recall (pero mejora la precision 0,71->0,89: menos falsos por reloj de bloque). (2) la fuga (prints de nuestros propios rellenos en la cinta) vale +0,15 de recall (0,36->0,51; 0,88 con OPT): cualquier cinta WS incluida la nuestra infla. (3) MOTOR (modelo de cola): BASE->OPT en cinta limpia +0,11 (0,361->0,475). (4) El resto (~0,5): 119/202 reales (59 %) son tx con 1 solo maker (T1): sin print de otro y con el nuestro excluido no hay evento observable; solo L1-drop/cola lo veria. Declaro: parte "motor" <= ~0,11-0,14 de recall; cota "observable" sin fuga ~0,41-0,48; con vida>=1,5 s igual. Limites: precision de WSXS no es de una cinta real fuera de muestra (los prints propios se eliminan solo donde hay ws_match); recall del motor no es EV (ver T1).

## T3 LEDGER — dictamen: 37 = post_rechazada exactos; bloqueos/banda censuran la muestra de forma NO uniforme; soporte muy estrecho
- 3.833 intenciones - 3.796 post_ok = 37 `post_rechazada` (los oid coinciden exactamente; ordenes_b oid == post_ok oid, 3.796 unicos). Los 37: TODOS status 400 "invalid post-only order: order crosses book" (el bid cruzo antes de llegar la GTC post-only). Por dia 6/14/14/3 (20-23 Oct; tasa 1,5/1,2/0,8/0,6 % de intenciones); por moneda ETH 17 (1,24 %), SOL 13 (0,99 %), XRP 7 (0,61 %); hora UTC 06-11Z 29 de 37 (resto 12,14,15,18Z); L 0,10-0,29 (todos los niveles, YES 21/NO 16). Son censura de la muestra solo en el sentido de "orden que no llega": rechazo por movimiento adverso/de libro en ~0,2 s, sin sesgo claro por L.
- 137 `post_abortado_tras_firma` (bid_ajeno_cambio 70 / ask_cambio 67) ocurren ANTES de intencion_post: no estan en las 3.833 pero tambien son colocaciones no hechas (por dia 25/49/51/12).
- 804 `bloqueo_suelo_saldo` = EVENTOS (reintentos), no ordenes: 137 minutos distintos, gap mediano 2,9 s. Por dia 83/267/368/86; hora UTC 6:74, 7:42, 8:188, 9:69, 10:114, 11:133, 12:34, 14:5, 15:66, 16:2, 17:18, 18:51, 19:8. Fraccion bloqueos/(bloqueos+posts) por dia 17/19/17/14 %; por hora 3 % (14Z) a 35 % (19Z, n pequeno), 22-23 % en 08, 10, 11, 15, 18Z frente a 7 % en 07Z. Mecanismo: saldo - comprometido - coste < minimo (saldo-minimo mediana 1,4 USD ~ un coste de orden): bloqueo por presupuesto/suelo, correlacionado con el drawdown intradia (22-Oct max). Moneda y nivel L NO estan en el evento: coste (1,02-1,45, mediana 1,15) es identico al de las ordenes puestas (1,00-1,45, mediana 1,14), pero coste=size*L con size=5 si L>=0,20 y ceil(1/L) si L<0,20, asi que L no es invertible: no se puede decir si el bloqueo sesga por nivel/moneda. Dato que lo cerraria: slug/L/oid en bloqueo_suelo_saldo.
- 477 `cancela_banda` (objetivo siempre None = el objetivo salio de la banda [0,10-0,29]): por dia 55/138/207/77; moneda ETH 166/SOL 157/XRP 154 (12,1/12,0/13,4 por 100 posts); hora 06-11Z 337; nivel cancelado L=0,28-0,29: 272 (57 %), 0,10-0,11: 104 (22 %), resto 101: la censura es en los BORDES de la banda y por la deriva del bid hacia arriba (bid-L de 0 a +3 ticks en 60 %). P(relleno|L) en 0,28-0,29 esta condicionada a que el bid no salga de la banda => sesgo de supervivencia en los niveles de borde.
Soporte exacto del ledger (ordenes_b, n=3.796 post_ok; EV real -0,0042 EUR/orden sin rebate, -16,02 EUR):
| dimension | soporte |
| niveles L | 0,10-0,29 (20 niveles); n por L: 55,158,125,152,138,174,132,185,160,165,182,196,195,208,227,224,275,266,351,228; ETH 0,10 solo (55) y 0,29 solo SOL/XRP; fills por L 0..21 |
| ticks bajo el bid (off_c) | 1: 2.405 (63,4 %), 2: 1.363 (35,9 %), 0: 12, 3: 9, 4: 3, 15: 1, -1/-2: 3 => 99,3 % a 1-2 ticks |
| monedas / lado | ETH 1.357, SOL 1.296, XRP 1.143 (0 BTC); YES 1.927 / NO 1.869; k config eth 2, sol 1, xrp 1 |
| tamano | 5 acc si L>=0,20 (2.352), 6-10 si L<0,20 (1.444); max_vivas 5; n_max 230 y luego 500 |
| vida (t_fuera-t_ini) | p5 0,21 s, p25 0,35, p50 0,66, p75 1,42, p95 4,5, p99 9,4; bins <=0,3 s 712, 0,3-1 1.716, 1-1,5 471, 1,5-3 537, 3-10 331, >10 29 |
| horas UTC / dias | 06-12Z 3.057, 14-19Z 739 (0 ordenes en 00-05, 13, 20-23Z); dias 405/1.121/1.746/524 (20-23 Oct) |
| T restantes | p5 99 s, p50 206 s, p95 284 s; cola profundidad al armar p50 43, p95 165 |
Conclusion de soporte: politicas pegadas al bid (1-2 ticks), 5 acc (6-10 si L<0,20), ETH/SOL/XRP, vida corta (mediana 0,66 s endogena al repeg), 06-19Z, 4 dias. Todo lo demas (niveles profundos, esperas largas, BTC, tamanos distintos, vidas largas) es extrapolacion, no calibrable con este ledger.

## Que cambia en las conclusiones previas
1. FN: "FN no distinguible de 0" se mantiene; ademas la separacion FN/TP es seleccion (69 % vs 39 % de tx de un solo maker); retirar toda lectura de "toxicidad en barridos rapidos" salvo como hipotesis sin soporte (diferencia estandarizada +0,15 [-0,37;+0,71]).
2. Recall 0,35: reloj/emparejado ~0,01 (0,361 con WS limpia); motor/cola ~0,11; ~0,5 es tx solo-nuestra-orden sin evento observable; con WS que incluya nuestras filas el recall sube a 0,51/0,88 por fuga. El motor (con L1-drop) no puede ver el 59 % de los rellenos reales: el EV simulado no representa los rellenos de "primero y unico" en la cola.
3. Soporte del ledger: 37 sin post_ok = rechazos "order crosses book"; bloqueo_suelo_saldo (804 eventos, 137 min) y cancela_banda (477, bordes 0,28-0,29/0,10-0,11) censuran por hora y por borde de banda; tabla de soporte arriba. Sigue sin valer para extrapolar fuera de ese soporte.
