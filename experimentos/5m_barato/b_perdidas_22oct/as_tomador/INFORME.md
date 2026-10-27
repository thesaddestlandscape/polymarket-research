# INFORME AS-TOMADOR (OLA 8) - cierre 24-Oct-2026

Etiqueta global: **REJECTED como palanca validada; EXPLORATORY (residual) para R_W y para el set "informados 09-18" sobre B.** Ningun gate primario (prereg) se cumple. No autoriza nada live.

## 1. Hipotesis
La seleccion adversa del maker (AS -0,04..-0,14 por tramo) procede de QUIEN rellena: tomadores persistentemente informados. Si es asi, una lista de tomadores "informados" identificada en un periodo previo y saltada (no cotizar contra ellos / cancelar) en un periodo posterior mejora el EV del maker (EXCESO = EV_ret - EV_total > 0).

## 2. Diseno (PREREG.md sha en PREREG.sha256, ADENDA1.md; congelados ANTES del test)
- Poblacion de prueba: `/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl` (rellenos de OTROS makers ETH/SOL/XRP 5m, pc (0,10-0,30], T 60-300 s, primeras 5 acc por maker-mercado-lado), n=113.918 unidades; EV ponderado por EUR (sum pnl / sum coste); cierre = cluster.
- SEL (tomadores) = 09-11 Oct (DESVIACION declarada: 5-8 Oct no disponible en cache; 3 dias en vez de 7). TEST = 12-21 Oct (21 parcial; se reporta con/sin).
- S_A (primario, todas las bandas, n>=100, coste>=200, neto/coste>=+0,02, >0 en >=2/3 dias); S_B (secundario, solo pc 0,10-0,30). K=2, alfa 0,025.
- Adenda 1 (post-hoc, K total 4, alfa 0,0125): R_W = walk-forward en vivo (tk_score = ROI bruto acumulado del tomador con dias anteriores al relleno, n>=30, c>=50; bandera tk_score>=+0,02; cobertura 87,9 %), dosis-respuesta y visibilidad (V_mkt: print previo del tomador en el mismo mercado a >=4 s; V_5: cualquier mercado de la moneda en 300 s).
- Descriptivos adicionales (a4/a5/a6, post-hoc, no cuentan para decidir): persistencia SEL->TEST, concentracion del bin perdedor, rellenos REALES de B (wallet dedicada).
- Scripts: `scripts/a1..a6`; salidas `datos/a2_resultados.json`, `a3_resultados.json`, `a4_stdout.txt`, `a5_stdout.txt`, `a6_stdout.txt`.

## 3. Resultados por gate (TEST 12-21 Oct, n=84.200 unidades aprox. de las que se banderan 7-42 %)

| Conjunto | n bandera (unid.) | % EUR | EV_total | EV_IN | EV_OUT | EXCESO | IC90 por CIERRE | p perm (1000-5000) | monedas EXC>0 | top wallet | mitades EXC>0 | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S_A (primario) | 6.101 (51 tomadores) | 7,1 % | +0,0182 | -0,0286 | +0,0218 | **+0,0036** | (-0,0021, +0,0089) | 0,010 | ETH+ SOL+ XRP- (2/3 OK) | 16,7 % OK | -0,003/+0,005/+0,013 (2/3 OK) | **FALLA (1)**: IC90 incluye 0 |
| S_B (secundario) | 4.872 (50) | 5,7 % | +0,0182 | +0,1557 | +0,0098 | **-0,0083** | (-0,0137, -0,0032) | 1,0 | 0/3 | 20,9 % | 0/3 | **FALLA (1)(2)(3)(5)**: signo contrario; contra los tomadores S_B el maker GANA (EV_IN +0,156), asi que saltarlos empeora |
| R_W (post-hoc, K=4) | 33.954 (589 tomadores) | 42,4 % | +0,0182 | -0,0035 | +0,0341 | +0,0160 | (-0,0006, +0,0320) | 0,001 (minimo resoluble) | ETH+ SOL+ XRP- (2/3) | 12,6 % | -0,003/+0,023/+0,033 (2/3) | **FALLA el limite inferior del IC90 por muy poco** (alfa de p 0,0125 cumplido) |

Notas de lectura:
- El nulo de la permutacion (S_A p95 0,0024) esta por debajo del EXCESO observado 0,0036 (p=0,010): hay una senal estadistica NOMINAL, pero de magnitud ~0,4 puntos de EV. El **placebo de seleccion** (200 sets aleatorios de tomadores del mismo tamano y coste elegidos en SEL) da media +0,0018 y p95 +0,0046; el EXCESO de S_A tiene p_emp = **0,214** contra ese placebo: elegir 51 tomadores al azar rinde el mismo orden de magnitud. S_B: p_emp 1,0.
- S_A sin el dia 21: +0,0036 (igual). Mejor corte: sin los 2 mejores dias, R_W cae de +0,0160 a **+0,0091**; EXC>0 en 7/10 dias (a4). Por moneda: todo el efecto viene de ETH (R_W ETH +0,033, SOL +0,004, XRP -0,021); XRP con signo contrario en los tres sets.
- Dosis-respuesta (a3, R_W): EV de la poblacion por bin de tk_score previo: <-0,02: **+0,120** (n=13.088, 15,4 % EUR); [-0,02,0): -0,019; [0,0,02): -0,003; [0,02,0,05): +0,005; >=0,05: -0,028; sin historial: +0,036. El unico bin con senal real es el de tomadores que PIERDEN (donde el maker gana), no el de los "informados" (+0,02..0,05+ -> EV maker ~0..-0,03). No es monotona ni sostiene "mas informado, peor para el maker" salvo en el extremo >=0,05 (-0,028). El bin <-0,02 es robusto a top-1 (6,2 % de los takers; sin top1 +0,107) pero concentrado en ETH (+0,18; SOL +0,004, XRP +0,007) y 9/10 dias >0 -> es un "cebo" ETH, no el mecanismo buscado.
- [FE DE ERRATAS 24-Oct, VERIFICACION.md] TEST 12-21: el 21-Oct de tab.pkl estaba truncado (3.318 de 7.960 unidades; EV de ese dia +0,158); con el dia completo n=88.826, 2.880 cierres, EV_total +0,0301 (antes +0,0182); S_A +0,0038 (IC90 cierre -0,0012,+0,0087), R_W +0,0146 (-0,0010,+0,0308; sin el 21: +0,0176 (+0,0014,+0,0333)), asi que el limite inferior de R_W cruza 0 segun la inclusion del 21-Oct. S_A sin sus 2 mejores dias: -0,0004. Con SEL de 7 dias (05-11) el EXCESO de S_A es negativo (-0,0033). Veredicto sin cambios.
- [FE DE ERRATAS persistencia] La cifra de abajo (rho -0,19, n=33) usa una submuestra mixta; con TODOS los fills por tomador y n>=100 en ambos periodos (n=416) el verificador obtiene Spearman +0,092 (p=0,060), quintiles monotonos (ROI bruto SEL -0,110..+0,131 -> TEST -0,011..+0,027): persistencia debil POSITIVA (~20 %); para los tomadores de S_A (n=66) ROI bruto +0,107 -> +0,002 (winner's curse). 'La identidad no persiste' es excesivo; 'el top seleccionado regresa a la media' es correcto. Veredicto sin cambios.
- Persistencia (a4, descriptivo, version original): ROI del tomador SEL -> TEST en la celda, 33 tomadores con coste>=100 en ambos: Spearman **-0,19** (p=0,29), Pearson -0,21 (p=0,24). Por quintiles de ROI_SEL, el ROI_TEST de los mejores quintiles es -0,084 (q4) y el de los peores +0,025 (q0): **regresion a la media, no persistencia**. Esto es consistente con que S_A no discrimine: la identidad del tomador no persiste en 3-10 dias.

## 4. Visibilidad antes del relleno (accionabilidad; 12-18 Oct, fills parquet)
Ts on-chain = bloque (~2,4 s tras el casado, +-1,5 s): no se afirma ventana en ms; el criterio de visibilidad exige print previo >=4 s antes, asi que solo usa informacion que ya existia en el momento de cotizar. Mediana del hueco al ultimo print previo del tomador: S_A 263 s (p10 13 s), R_W 119 s (p10 7,5 s) -> hay tiempo para una politica por lista; el obstaculo no es la latencia sino la prediccion.

| Conjunto | % banderadas visibles (V_mkt / V_5) | EV banderadas visibles | EV no visibles | EV no banderadas | EXCESO saltando solo visibles (V_mkt / V_5) | retencion EUR |
|---|---|---|---|---|---|---|
| S_A (n=5.048) | 34,0 % / 55,0 % | **+0,118** | -0,017 | +0,0386 | **-0,0021 / -0,0011** | 97,4 % / 95,7 % |
| R_W (n=25.512) | 47,3 % / 69,4 % | +0,027 | +0,021 | +0,0483 | **+0,0028 / +0,0075** | 79,7 % / 70,2 % |

- S_A: las banderadas VISIBLES son rentables para el maker (+0,118 como EV poblacional) -> saltarlas empeora (-0,002). La AS no esta en los tomadores a los que podemos "ver".
- R_W: EXCESO visible +0,003 (mismo mercado) a +0,0075 (misma moneda 300 s); sin IC por cierre calculado (descriptivo, post-hoc). Perdiendo 20-30 % del volumen. Es el unico resultado accionable y es pequeno.

## 5. Rellenos REALES de B (wallet dedicada, 20-23 Oct; a5/a6, post-hoc, descriptivo) - CORREGIDA 24-Oct con VERIFICACION.md
Correccion: la version anterior usaba `m5_onchain_2026-10-23` como si faltase (198 de 215 fills, 102 cierres, EV -0,0302, pnl -6,18 $). Con el fichero completo se casan **215 de 215 compras a un unico tomador on-chain** (0 tx con >1 tomador; size y coste coinciden con el ledger; desenlace oficial 215/215, 0 discrepancias), **112 cierres**, coste **221,30 $**, **EV_total = -0,0724** (ponderado por EUR; media por posicion -0,0174), **pnl = -16,02 $** (ETH +0,032, SOL -0,081, XRP -0,212). Los 17 fills del 23-Oct omitidos perdian -9,84 $. Fuente: `verificacion/v3_stdout.txt`.

| Bandera | n flag (fills / cierres / tomadores) | % EUR | pnl banderado | pnl no banderado | EV_flag | EV_noflag | EXCESO_B | IC90 por cierre | p perm |
|---|---|---|---|---|---|---|---|---|---|
| S_A (prereg, sets del revisor) | 14 / 12 / 6 | 7,2 % | -0,96 | -15,06 | -0,060 | -0,073 | -0,0010 | (-0,057, +0,048) | 0,54 (fill) / 0,53 (tomador) |
| "Informados 09-18" NETO >=2 % (n>=100, c>=200; 238 tomadores; POST-HOC) | 29 / 25 / 9 | 13,7 % | **-15,30** | -0,73 | -0,505 | -0,004 | +0,069 | (-0,003, +0,140) | 0,111 (fill) / 0,075 (tomador B) / 0,141 (pool activos) |
| "Informados 09-18" BRUTO >=2 % (370 tomadores; POST-HOC, hallazgo del revisor) | 105 / 72 / 24 | 50,3 % | -37,36 | +21,34 | -0,335 | +0,194 | **+0,267** | (**+0,039, +0,515**) | 0,029 (fill) / 0,003 (tomador B) / 0,020 (pool activos) |

Lectura (corregida): (a) el set S_A prereg sigue indistinguible de cero en B. (b) El set neto 09-18 NO son "28 fills contra 28 tomadores" sino **29 fills contra 9 tomadores / 25 cierres**; dos tomadores (0xc87ad643... 11 fills -6,87 $; 0x424eb20f... 5 fills -5,64 $) concentran el 82 % de la perdida banderada y ~39 % del EUR banderado (> tope 30 % del prereg), y la perdida banderada cae casi toda el 21-22 Oct (20-Oct +0,08; 21 -6,75; 22 -7,49; 23 -1,14). La frase anterior "sin ellos B habria dado +8,0 $ (EV +4,5 %)" NO reproduce (con 215 fills: -0,73 $, EV -0,4 %). (c) La variante por ROI **bruto** (no recogida antes) da EXCESO_B +0,267 con IC90 por cierre > 0 y p de permutacion a nivel tomador 0,003-0,020, sobre 24 tomadores y la mitad del EUR de B; es **post-hoc (3.a variante sobre el mismo B, K efectivo > 5 contando las variantes del informe y del revisor), una sola muestra de 4 dias y 112 cierres, solapada en regimen con perdidas de 2 dias**: HIPOTESIS A REPLICAR en dias nuevos (contrafactual shadow: `contrafactual/PREREG.md`), no hallazgo. Contrasta con la poblacion de otros makers (EXCESO ~ +0,004): sugiere AS especifica de B (cola/precio) o ruido de 112 cierres; no invalida el veredicto REJECTED en poblacion. Sin el peor cierre banderado el EXCESO bruto baja a +0,252, sin los 3 peores a +0,235.
Estado de B (24-Oct): sin fills desde el 23-Oct 08:56Z (wallet con ~3,41 pUSD); un contrafactual solo sobre B no acumula n sin relanzar B.

## 6. Valor en EUR/ano
Formula (prereg): dPnL = N * (ret * EV_ret - EV_total), N nocional anual; ret = fraccion de EUR retenida. Cota superior (sin sustitucion de fills ni efecto sobre la cola de cotizacion). Cifras en USD tal como salen de a3.

| Escenario | N = 25 k$ (B) | N = 255 k$ (3 % nicho) | N = 424 k$ (5 % nicho) | Estado |
|---|---|---|---|---|
| S_A (poblacion TEST) | +51 $ | +522 $ | +868 $ | no validado (IC90 incl. 0; placebo p 0,21) |
| R_W (poblacion TEST) | +37 $ | +382 $ | +635 $ | exploratorio (IC90 inf. -0,0006) |
| R_W solo visibles V_5 (aprox. N*EXCESO_V) | ~+190 $ | ~+1.900 $ | ~+3.200 $ | exploratorio, sin IC, 12-18 Oct |
| Informados 09-18 en B real (ret 0,857, EV_ret +0,0455 vs EV_total -0,0302) | ~+1.730 $ | n/a | n/a | exploratorio, p=0,10, 1 muestra de 3 dias de B |

- **Validado: 0 EUR/ano.** Exploratorio (todo, mejor caso, B): ~0,05-1,7 k$/ano frente a 25 k$/ano de nocional de B, es decir hasta ~+7 % del nocional solo en el caso de B real (que es su propia muestra pequena); en poblacion general <1 % del nocional.
- **Aporte al hueco de 200 k EUR: validado 0 %; mejor caso exploratorio (nicho 5 %, R_W visibles) ~3 k$ = ~1,5 % del objetivo;** B real ~0,9 % del objetivo. No cierra ningun hueco; a lo sumo reduce la perdida de B (EV -3 %) hacia cero, que es un objetivo distinto (no perder) del de ganar 200 k.

## 7. Sesgos y limites (todos declarados)
- Poblacion de prueba = rellenos de OTROS makers (primeras 5 acc), con EV_total +0,018; B real tiene -0,030: no son la misma poblacion ni el mismo orden de cola. El EXCESO se transfiere a B solo por analogia.
- Seleccion con 3 dias (desviacion declarada) y tk_score sobre ROI BRUTO para R_W (el umbral +0,02 del prereg era neto). Esto favorece que R_W incluya muchos tomadores (42 % EUR) y diluya.
- IC por cierre; no se calculo bloque por dia ni se controlo el regimen BTC compartido. Los cierres de un dia comparten regimen; el IC real es probablemente mas ancho.
- Efecto sustitucion no medido: saltar un fill no devuelve su dinero a otro fill con EV medio; en la cola real la posicion se ocuparia por otro tomador (peor o mejor).
- Multiplicidad: K=4 declarado (alfa 0,0125) para prereg+adenda; los cortes por moneda/dia/visibilidad/B son descriptivos. El bloque B (informados 09-18) es un 5.o contraste.
- Persistencia del tomador: ver fe de erratas de la seccion 3 (n=416: debil positiva; el top seleccionado regresa a la media).

## 8. Veredicto y siguiente paso
- Prereg: **REFUTADO** (S_A falla criterio 1; S_B signo contrario). El mecanismo "identidad persistente del tomador explica la AS" **no se sostiene** a esta escala: EXCESO +0,004 sobre EV 0,018, p_emp vs placebo 0,21, persistencia SEL->TEST negativa, XRP en contra.
- Residual exploratorio: R_W (walk-forward diario) con EXCESO +0,016 (IC90 -0,0006..+0,032, p 0,001), concentrado en ETH, +0,009 sin los 2 mejores dias, y "informados 09-18" sobre B real.
- Siguiente paso minimo si Javi quiere seguir (sin gastar B): congelar en un prereg nuevo R_W-neto solo ETH con umbral y set fijados, y evaluar en dias NUEVOS (22-31 Oct) con IC90 por dia y placebo de selecciones aleatorias en el mismo periodo; en paralelo, contrafactual diario shadow sobre B ya pre-registrado en `contrafactual/PREREG.md` (SET_I y SET_V bruto, gates n>=40 cierres banderados, >=10 dias, IC90, sin 2 mejores dias, placebo). No hay mejora a la vista que cierre la brecha de 200 k EUR por esta vía.
