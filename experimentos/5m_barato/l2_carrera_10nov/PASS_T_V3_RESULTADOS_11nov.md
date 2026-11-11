# PASS_T_V3 RESULTADOS (11-Nov-2026, 11:40-13:05Z). TRAIN 26-Oct..09-Nov (15 dias). HOLD >=10-Nov NO leido (solo libro5_tx del 10-Nov para fechar tx del 09-Nov, como passT_v2). 0 ordenes. PREREG_L2_V2 (573dae38) y ADDENDUM_A1 (13249423) intactos (sha verificado 13:04Z).
Estado: **COMPLETE** para tareas 1-6 (15/15 dias; 3 abortos por MemoryError del 09-Nov, reintentados con ulimit 3,7-4 GB; ver log). Nada se llama rentable: todo es simulacion in-sample con motor.

## 0. Ficheros (todos NUEVOS en l2_carrera_10nov/; engine.py de dev y v2 sin editar)
engine_v3.py (fill_segment_v3 + DayEngV3), stamp_v3.py (sello por firma), passT_v3.py (STAMP v2|v3, ENG orig|dd), passT_cxb_v3.py (familia CXB/F5 con motor), prep_fills_v3.py, concat_v3.py, paso0_lib_v3.py (fix `cargar`), paso0_run_v3.py (ev/e1n1/x1),
l2_triggers_v3.py, condicion1_v3.py, verif_v3.py + verif_v3_analiza.py, doble_conteo_v3.py, analiza_cxb_v3.py, run_v3_train.sh, chain_v3.sh, test_v3.py (13 tests; test_relojes 6 OK). Salidas: out_v3/ (RT_/SEGT_/CX_*.pkl, paso0_v3dd/*.json, analiza_cxb_v3dd.txt/.json, doble_conteo_v3.json, condicion1_v3_*.json, logs run_v3.log/chain_v3.log), verif_real/out_v3/.
Reproduccion: `bash run_v3_train.sh && bash chain_v3.sh` (nice 19, ulimit 3,7 GB, espera 06-09Z; el 09-Nov necesita >=3,7 GB y MemAvailable >2,5 GB: shadow_postmortem de 12:51Z lo mato dos veces). Tests: `ulimit -v 3000000; python3 -m pytest -q test_v3.py test_relojes.py` (con ulimit 1,5 GB falla test_relojes por memoria, no por logica).
Nota: el commit automatico del repo ya ha incluido estos ficheros (git los marca M); no hice commit.

## 1. Sello v3 (stamp_v3.py, passT_v3.py) y doble conteo
- Regla: firma exacta unica (token+precio+tamano del tx, +-1.500 ms EX, reuso de la logica de `emparejado.py`) y d_ex en [-50,300] -> tm = ex(fila)-1; si ambigua/sin firma/fuera de guardia -> t_ev - c_dia - 1 (c_dia = p50 de d_ex de las unicas npr=1 del dia: 18-21 ms, 15 dias); sin t_ev -> legacy recv-63. Relojes: EX para el evento/mecanica, RX para decisiones (K view), sin mezclar.
- TRAIN, 770.143 eventos (token,tx): firma unica sellada 61,0 % (470.062), ambigua 25,2 %, sin firma 12,0 %, fuera de guardia 1,1 %, sin t_ev 0,6 %. Ramas de los 4.601 rellenos G0: sig 3.217, amb 869, nosig 436, guard 43, sinev 15, nomatch 21.
- Regresion: `passT_v3.py v2 orig` reproduce fila a fila out_v2/RT_causal 03-Nov (9.365 filas, todas las variantes, q/tf/pnl/ftype/canc/tf_rx identicos).
- **Doble conteo en fill_segment BASE: REAL en codigo, PEQUENO medido.** Test que lo demuestra (`test_doble_conteo_demostrado`): cola 20, consumo de 10 (fila 20->10 + print de 10) y un 2o consumo de 5 que NO nos llega; original: relleno fantasma de 5 si el print va sellado en/tras la fila, 0 si va antes; dedupe=True da 0 en los tres sellados; dedupe=False == original (400 casos aleatorios). Fix: prints agrupados por sello cuya suma == caida de szb de una fila en (t_print-100 ms, t_print] se procesan antes de esa fila; solo cambia el ORDEN; tf conserva el sello del print (test).
  Medido sobre 15 dias (doble_conteo_v3.json): con sellos VIEJOS, G0 12/4.630 rellenos fantasma (0,26 %; pnl -4,3 EUR), CXB150 33/1.736 (1,9 %); con sellos v3, G0 0/4.601 y CXB150 5/1.210 (0,4 %). Con el sello correcto el doble conteo practicamente desaparece; el error grande era la REGLA DE CAIDA, no la cola.
  Limitacion: las pickles v3dd (TRAIN) se generaron ANTES del parche de tf: 21 de 4.601 rellenos G0 ('nomatch') llevan tf = hora de la fila en vez del sello del print (<=100 ms antes). Control: E1/N1/X1 con v3orig (sin dedupe, tf exacto) dan las mismas conclusiones (E1 todos KILL, X1 12/12 Delta<0, N1 muere con 0,8628). Pnl/cantidades de CX no dependen de tf.
- Efecto del sello v2->v3 sobre G0 (15 d): 4.630 -> 4.601 rellenos (pnl -518,3 -> -527,8 EUR; EV -0,151 segun CAUSALIDAD_187MS para 4.616 -> -0,154: G0 casi no cambia); sobre CXB150 con motor: 1.736 -> 1.205 rellenos, pnl -84,5 -> -1,7 EUR (el reloj viejo hacia que CXB "evitara" mal). Corrige tf: dtf v3-original p50 +26-29 ms, p5 -1..-3, p95 +282..+334 (40-48 % difiere >50 ms).

## 2. `cargar` (paso0_lib_v3.py) y regresion
Causa del RuntimeError de run_C.log: no eran rellenos sin segmento sino **3 rellenos con segmento y bidL=NaN** (XRP 26-Oct 02:15Z: sin bid vivo en g-300). v2 los contaba con `bidL.isna()`. v3: indicador de merge (sin segmento -> RuntimeError), `n_bidL_nan` aparte (geo6=False como el original). `modo='legacy'` == `paso0_lib.cargar` (test con datos reales, guard del original anulado para no escribir en eval_log.jsonl). Log propio eval_log_v3.jsonl (15 dias, ninguno HOLD).

## 3. verif_v3 (20-23 Oct, 202 reales de 3.796 ordenes B, ledger)  [verif_v3_analiza.py]
| BASE (cinta de otros makers) | sim | tp | precision (IC90 Wilson) | recall (IC90) |
|---|---|---|---|---|
| v2o (regla vieja; == V_<D>.pkl, verificado) | 100 | 71 | 0,710 (0,631-0,778) | 0,351 (0,299-0,408) |
| v3 sello (orig o dedupe: IDENTICOS) | 82 | 70 | **0,854 (0,778-0,907)** | 0,347 (0,294-0,403) |
| OPT v2o / v3 | 143 / 115 | 85 / 84 | 0,594 / 0,730 | 0,421 / 0,416 |
Por moneda (BASE v2o -> v3): ETH prec 0,745->0,881, recall 0,481->0,468 (n real 79); SOL 0,762->0,889, 0,250->0,250 (64); XRP 0,607->0,773, 0,288->0,288 (59). Por dia v3: precision 0,85/0,92/0,91/0,55; recall 0,30/0,47/0,25/0,38. Vida>=1,5 s (117 reales): precision 0,824->0,909, recall 0,359->0,342.
Lectura: **v3 quita 22 falsos positivos (de 100 a 82) sin perder verdaderos (71->70): sube la precision, el recall NO se mueve.** El recall ~0,35 sigue acotado por lo ya visto (59 % de los rellenos reales = tx con un solo maker, nuestra propia orden: sin print ajeno). Dedupe: 0 cambios en 3.796 ordenes. EV: sim v3 -0,222 (82 rellenos, coste 91 EUR) vs real -0,061 (coste 221 EUR): el motor sigue sin reproducir el EV real (no es un test de EV). Cobertura emparejado WS 82-88 %; 6.781-12.212 eventos/dia sin emparejado WS caen a legacy (bloque-2,25 s-63): en 20-23 Oct esto es mas ruidoso que en TRAIN (libro5_tx no existe).

## 4. TRAIN con v3 (motor: dedupe; fills G0 v3dd). Fuente: out_v3/paso0_v3dd/*.json
- **G0 incondicional**: 47.470 colocaciones, 4.601 rellenos, coste 3.422 EUR, pnl rb0,2 -527,8 EUR, EV ponderado -0,154 (IC90 por dias [-0,259,-0,046]), sin 2 mejores dias -0,223, dias+ 3/15 (pnl/colocacion -0,0111). v2 causal: 4.616 / -0,151: igual. Por moneda (EV): ETH -0,056 (n 2.163), SOL -0,223 (1.558), XRP -0,276 (880). Por L: 0,10 -0,213, 0,13 -0,151, 0,16 -0,147, 0,19 -0,140.
- **E1: KILL se mantiene** (16 configuraciones Lambda 150/310/500/560 x G0/GEO6 x rb 0/0,2): p placebo de grupo = 1,0 en todas; Lambda 150 G0: Delta +242 EUR vs placebo medio +425 (v2 original: +238 vs +423).
- **X1: KILL se mantiene** (12/12 variantes Delta<0; base M<=1500: Delta -24,1 EUR, n 506 coberturas, 301 cierres, IC90 cierre inf -0,37, p placebo 0,13; original -40,2/427). Ninguna pasa etapa 0.
- **N1: pasa de borderline a muerte**: 144 celdas, 10 armadas, cobertura de coste no armado 0,8628 >= 0,85 (veto total); original 0,850/11 armadas. In-sample sum_delta +348,8 (sin 2 mejores +140,6, dias+ 11/15) pero la validacion cronologica (celdas de 26-Oct..02-Nov evaluadas 03-09: 6 armadas) da +192,6, sin 2 mejores +25,2, dias+ 57 %.
- **Condicion 1 (03-07 Nov, 1.487 rellenos)**: aceptacion original 1.350 / -0,2447 (pnl -245,76); causal v2 1.345 / -0,2396; **v3: 1.337 / -0,2368 (pnl -235,25)**. No reproduce el criterio +-1 EUR de A1 (esperable: tf cambia); mismas conclusiones de signo.
- Que cambia en los KILL: **nada se levanta**. E1/X1 siguen KILL; N1 queda peor. El unico efecto del reloj corregido esta en reglas que dependen de tf (CXB, ver 5).

## 5. CXB-true con MOTOR (re-armado, cola, rem), sello v3, TRAIN 15 d  [analiza_cxb_v3.py; out_v3/analiza_cxb_v3dd.txt]
Regla CXB(l): cancelar cuando el libro (recepcion) muestre bid<L (o ya lo muestre al llegar), efectiva en t_rx+l; re-armado normal (colocacion solo si bid(t-300 ms) >= L+1 tick). Control con IGUAL colocacion: GEO1 (G0 y bid(t-300)>=L+1 tick, sin cancelar): 4.346 rellenos, EV -0,146.
| variante (l ms) | rellenos / coste EUR | pnl EUR | EV/EUR | IC90 dias | Bonf. inf | IC90 cierre | sin 2 mejores | dias+ |
|---|---|---|---|---|---|---|---|---|
| CXB60 | 882 / 594 | +80,3 | **+0,135** | (-0,002, +0,282) | -0,067 | (-0,068, +0,336) | +0,040 | 8/15 |
| CXB100 | 1.025 / 702 | +34,2 | +0,049 | (-0,104, +0,210) | -0,180 | (-0,132, +0,236) | -0,059 | 7/15 |
| CXB150 | 1.205 / 838 | -1,7 | -0,002 | (-0,160, +0,169) | -0,225 | (-0,165, +0,168) | -0,124 | 5/15 |
Incremental vs GEO1 (pnl evitado por la regla, misma colocacion): CXB60 +552,9 EUR (IC90 por dias +18,0..+56,1 por dia, Bonferroni inf +7,4; 13/15 dias+; quita 82 % del coste), CXB100 +506,7 (inf Bonf +6,1; 12/15), CXB150 +470,9 (+6,7; 12/15). **El efecto de PALANCA (evitar rellenos perdedores) es robusto a l en-muestra; el EV neto >0 solo aparece con l=60 y se cae con +40 ms (+0,135 -> +0,049 -> -0,002).**
Placebo de igual cobertura (S=20 semillas: cancelacion en instante uniforme del segmento donde la regla dispararia; mismo n de cancelaciones +-15 %): EV placebo -0,141 (p5-p95 -0,158..-0,126) para todos los CXB: cancelar al azar no sirve; observado +0,135 -> exceso +0,276; p por variante y p de familia (max-statistic sobre K=10) = 0,0476 = **cota de resolucion** de 20 semillas (el max z observado 30,2 es >>; faltan semillas para un p mas fino, no mas efecto).
Por moneda (CXB60): ETH +0,051 (n 582, coste 392), SOL +0,322 (191, 127), XRP +0,259 (109, 75); a l=100 ETH -0,015. Por L (CXB60): 0,10 +0,223, 0,13 +0,051, 0,16 +0,287, 0,19 +0,010 (n 210-234 por celda, solo descriptivo). Concentracion: el mejor dia (26-Oct) aporta +40,1 de +80,3 EUR; sin el, +40,2 EUR (EV +0,075); dias+ 8/15.
Nota de honestidad: la comparacion de placebo condiciona en el futuro (cancela solo en segmentos donde luego hay bid<L), igual que el PCXB previo; por eso el criterio duro es la columna EV absoluto + IC por dias/cierre + sin 2 mejores dias, no el exceso sobre placebo.
**Veredicto CXB-true: palanca real de mitigacion de seleccion adversa (+470..+550 EUR evitados en 15 d, IC por dias > 0 incluso con Bonferroni), EV>0 NO demostrado: IC90 por dias cruza 0 (-0,002) a l=60, por cierre cruza, sin 2 mejores dias +0,04 y dependiente de una cancelacion efectiva <=60 ms (n=4 anclas Sonda, 32-46 ms exchange)**. Etiqueta: EXPLORATORY in-sample.

## 6. Variantes, F5/M2 y combinacion (K=10 probadas + 3 controles; nada mas se miro)
Probadas (declaradas ANTES de ver resultados): CXB60/100/150 (l = sensibilidad de latencia, no parametro libre), TOP60 (cancelar si bid<=L: salir al llegar el precio a nuestro nivel), CXB60r (idem CXB60 + colocar solo si bid(t) actual >= L+1 tick = "no recotizar mientras el libro este debajo"), F5A (no colocar/cancelar en tercil ALTO de F5 en el instante de decision; cortes congelados C0=3,5264, C1=4,7174 de PREREG_FWD_V2), F5B (solo tercil BAJO), F5A+CXB60/100/150. Controles: G0, GEO1, GEO1_F5A. **Multiplicidad: max-statistic sobre K=10 + IC por dias con Bonferroni (quantil 0,05/10).**
NO exploradas (y por que): l por moneda/nivel (seria fishing con n 100-200 por celda; se informa solo descriptivo), tamano vivo (EV/EUR casi no cambia con el tamano; sin dato de cola por nivel), tiempo de vida maximo, "solo celdas con cola" (el registro barato solo trae top of book; exige L2/libro5), recotizar = mover a otro L (los 4 niveles ya corren a la vez).
| variante | rellenos / coste | pnl | EV | IC90 dias | Bonf inf | IC90 cierre | sin 2 mejores | dias+ | placebo EV (exceso) |
|---|---|---|---|---|---|---|---|---|---|
| TOP60 | 464 / 342 | +36,1 | +0,106 | (-0,035,+0,261) | -0,111 | (-0,143,+0,357) | +0,024 | 9/15 | -0,141 (+0,246) |
| CXB60r | 814 / 549 | +63,6 | +0,116 | (-0,024,+0,265) | -0,090 | (-0,085,+0,320) | +0,028 | 9/15 | -0,130 (+0,246) |
| F5A | 3.607 / 2.667 | -322,8 | -0,121 | (-0,224,-0,017) | | | -0,180 | 5/15 | -0,067 (**-0,054**: peor que placebo) |
| F5B | 1.512 / 1.122 | -98,2 | -0,088 | (-0,235,+0,058) | | | -0,170 | 5/15 | -0,051 (-0,036) |
| F5A+CXB60 | 625 / 430 | +88,6 | **+0,206** | (+0,046,+0,380) | -0,033 | (-0,018,+0,452) | +0,106 | 10/15 | -0,050 (+0,256) |
| F5A+CXB100 | 745 / 522 | +43,2 | +0,083 | (-0,085,+0,262) | -0,163 | (-0,119,+0,300) | -0,038 | 6/15 | |
| F5A+CXB150 | 871 / 617 | -5,3 | -0,009 | (-0,164,+0,159) | -0,238 | | -0,125 | 6/15 | |
- **F5/M2 como filtro de colocacion/cancelacion en el instante de DECISION no funciona**: F5A solo (-0,121) no mejora a G0 (-0,154) ni al placebo (-0,067); el gradiente por tercil en NUESTROS rellenos G0 es bajo -0,182 (n 2.518) / medio -0,087 (1.577) / ALTO -0,225 (506): no monotono y el alto es el peor solo por poco (sin 2 mejores -0,456, 4/15 dias+); el gradiente poblacional (+0,132/+0,048/-0,033) se mide en tau = r-100 ms (PREREG, "la senal vive en los ultimos 100-200 ms antes de RECIBIR el print", desaparece a >=250 ms): no es una variable que podamos leer antes de colocar.
- **La combinacion no anade nada demostrable**: F5A+CXB60 vs CXB60: +8,2 EUR en 15 d (IC90 por dias [-2,2,+3,1] por dia, 9/15 dias+); su IC90-dias inferior >0 (+0,046) cae a -0,033 con Bonferroni y por cierre cruza 0; es el maximo de 10 variantes: no tomarlo como hallazgo.

## 7. Regla candidata (pseudocodigo, CONGELABLE solo para prerreg propio; NO validada; no reabre E1/X1 por renombrado)
```
REGLA B-CXB60 v1  (universo ETH/SOL/XRP, mercados 5m, T restante en (61 s, 300 s], niveles L en {0,10; 0,13; 0,16; 0,19}, 5 acc, GTC post-only BUY; maker-only)
cada 500 ms, por (token, L), con features por RECEPCION (ultimo mensaje con rx<=t):
  ENTRADA : G0(b15,vol30,hora) AND ask_rx > L AND bid_rx(t-300ms) >= L+0,01 AND restante_por_llenar > 0
  ENVIO   : orden viva desde t+68 ms (LAT_POST), hasta salida
  SALIDA  : (a) bid_otros_rx < L  -> cancelar YA (efectiva t_rx + l, l=60 ms supuesto; ver 'que falta')
            (b) G0 falso en la siguiente rejilla -> cancelar a +60 ms
            (c) T restante <= 61 s -> cancelar
  REARME  : tras cancelar, no recolocar hasta que bid_rx(t-300ms) >= L+0,01 (misma regla de entrada)
  "bid_otros": el libro SIN nuestra orden; con la orden en el libro real el nivel L muestra nuestro tamano: bid_otros < L <=> mejor bid visible == L con size <= nuestra parte restante (no medido; ver abajo)
  NO incluir F5 (no demostrado); NO usar l por moneda/nivel.
```
Criterio de decision propuesto (prerreg futuro, HOLD >=10-Nov, forward): EV ponderado por EUR > 0 con IC90 por CIERRE inf > 0, sin 2 mejores dias > 0, >=10 dias, y el EV con l medido (no supuesto) y con l+40 ms >= 0; p placebo con >=100 semillas.

## 8. Lo NO verificado / limites (fail loud)
1. **l real de cancelacion**: l=60 ms es supuesto (anclas Sonda n=4: 32-46 ms hasta sello exchange, RTT 56-66; B Oct n=9; epoca-dependiente). Sin n>=30 cancelaciones reales con latencia deteccion->envio->aceptacion, el EV>0 es condicional a ese supuesto. Sensibilidad: -0,086 EUR/EUR por cada +40 ms.
2. Visibilidad de "bid sin nosotros<L" con NUESTRA orden dentro del libro: no medida; si el feed solo muestra bid==L con nuestro tamano hay que restarlo (sabemos nuestro tamano; la reconstruccion del nivel L exige delta/d, no solo top-of-book).
3. 38 % de los eventos usan sello de fallback (amb/nosig/guard): error del fallback = d_ex - c (p5..p95 de d_ex 16..76 ms contra c~20): hasta +56 ms de adelanto del print; no he probado un sello pesimista alternativo.
4. La verificacion con ordenes reales (verif_v3) es de 4 dias de B (202 reales) y NO contiene ninguna cancelacion al ver bid<L: valida la mecanica de relleno (precision), no la politica CXB. Cobertura de emparejado WS 82-88 % (sin libro5_tx antes del 24-Oct).
5. Placebo S=20 (p minimo 0,048); condiciona en futuro (ver arriba). Los 15 dias comparten regimen (mes de oct-nov); n efectivo por cierre 511 pero 15 dias independientes; mejor dia = 50 % del pnl de CXB60.
6. G0 v3dd tiene 21 tf de la fila (ya parcheado en engine_v3 con test; TRAIN no regenerado; control v3orig sin cambios de conclusion). CX (pnl) no afectado.
7. EV del motor vs real en verif: sim -0,222 vs real -0,061: el motor no es un estimador de nivel de EV real, solo de ordenacion.
8. Heredado: libro5_tx t_ev == sello del mensaje last_trade_price (no cruzado con las filas 't' de maker_ms); fills de tomadores contra el complementario (mint) fuera de la cinta side=0.

## 9. Siguiente (en orden) y especialistas
1. **data-integrity-authority**: auditar v3 antes de tomar nada por bueno (sello por firma 38 % fallback; paridad CX G0 == passT G0 es exacta; parche de tf; guardias d_ex; HOLD no tocado).
2. **statistical-validator**: n efectivo (cierre/dia), 100+ semillas de placebo, prueba por dias de CXB60 - GEO1 y de l (60/100/150) como curva dosis-respuesta, concentracion (dia 26-Oct).
3. **execution-engineer (mock/shadow, sin firmar/enviar)**: instrumentar decision->send->ack de una cancelacion simulada para medir l en condiciones reales, y la reconstruccion "bid sin nosotros" en el ejecutor dry-run F2; medir n>=30.
4. **alpha-miner**: NO hasta que se cumplan las condiciones de coordinacion (CXB-true supera placebo SI; G0 con IC por dias >0: NO (G0 -0,154); sin 2 mejores dias >0 de la regla: +0,040 solo). Propuesta: prerreg propio de B-CXB60 sobre HOLD con la condicion de l medido.
5. Datos que faltan: l real (n>=30), libro con nuestra orden dentro, mas dias (HOLD >=10-Nov y forward), L2/libro5 por nivel para "solo celdas con cola".
