# VERIFICACION INDEPENDIENTE de AS-TOMADOR (revisor adversarial, 24-Oct-2026 09:1x-09:22Z)
Datos: m5_onchain_2026-10-09..21 CRUDO + token map de las filas `k` de m5_registro + desenlaces gamma (`maker_ms_desenlaces_cache.json`); NO se usan datos/*.json, scripts a1-a6, kmap, fills_D.parquet ni tab.pkl (tab.pkl y sets.json solo se abren al final para COMPARAR). Solo lectura, nice 19/ionice idle, RSS max 781 MB (v2; superior al tope 500 MB por la carga de 13 dias, avisar).
Reproducir (en este directorio): `bash run_all.sh` (v1 extraccion + v2 + v4 + v3; correr tras 09:00Z), luego `TEST_END=20 python3 -I v2_analisis.py` (variante sin 21-Oct) y `python3 -I v5_sel7.py` (tras `run2.sh` que extrae 05-08). Salidas: v2_stdout*.txt, v3_stdout.txt, v4_stdout.txt, v5_stdout.txt, v2_resultados*.json, v3_resultados.json.

## Veredicto del revisor
El veredicto REJECTED (palanca no validada, 0 EUR/anio) **se mantiene y sale reforzado** (con SEL de 7 dias el EXCESO de S_A es negativo). Pero hay 2 cifras del INFORME que NO reproducen y deben corregirse (B real y 21-Oct), mas un hallazgo que el informe subestima (B real).

## Hallazgos (por severidad)
- **MAJOR - Seccion 5 (B real) usa datos incompletos y obsoletos.** El INFORME dice 198/215 fills, 102 cierres, coste 204,46, EV_total -0,0302, pnl -6,18 $. Con el fichero m5_onchain_2026-10-23 (ya existente; a5 lo reporto "falta") se casan **215/215** (0 tx con >1 tomador, 0 desajuste size/coste vs ledger, 112 cierres, coste 221,30, **EV_total -0,0724, pnl -16,02 $**; ETH +0,032, SOL -0,081, XRP -0,212). Los 17 fills omitidos (23-Oct) pierden -9,84 $. a6 sigue leyendo b_real_fills_taker.csv (198) pese a que el INFORME se edito a las 08:15 de hoy. Consecuencia: "sin ellos B habria dado +8,0 $ (EV +4,5 %)" NO reproduce (con 215: -0,73 $, EV -0,4 %).
- **MAJOR - "28 de 198 fills contra 28 tomadores" NO reproduce: son 29 fills contra 9 tomadores (25 cierres).** Dos tomadores concentran el 82 % de la perdida banderada (0xc87ad643... 11 fills -6,87 $; 0x424eb20f... 5 fills -5,64 $); su peso en EUR banderado ~39 % (> tope 30 % del prereg, criterio 4). Perdida banderada por dia: 20-Oct +0,08, 21 -6,75, 22 -7,49, 23 -1,14. Esto hace que "hipotesis para pre-registrar" sea aun mas fragil (efecto de 2 wallets, 2 dias).
- **MODERATE - TEST 21-Oct truncado.** tab.pkl tiene 3.318 unidades el 21-Oct; el dia completo tiene 7.960 (EV +0,158, dia muy bueno para el maker). Dias 12-20 coinciden exactamente (n identico; c difiere 0,04 % por redondeo de pc). TEST completo: n=88.826, 2.880 cierres, EV_total +0,0301 (informe +0,0182). Con 21 completo, R_W IC90 cierre (-0,0010,+0,0308); sin 21 (+0,0014,+0,0333): **el limite inferior de R_W cruza 0 solo segun la inclusion del 21-Oct parcial/completo**. El informe lo presenta "por muy poco" y es post-hoc (K=4, alfa .0125) -> sigue sin validar, pero la frase "FALLA el limite inferior" depende de un dia.
- **MODERATE - Persistencia (-0,19, n=33) reproduce solo con submuestra no representativa.** Mi version con la def. del autor: n=34, Spearman -0,26 (p=0,14), Pearson -0,34 (p=0,05) [full] / -0,23 (p=0,20) [sin 21]. Definicion mixta (ROI sobre coste del maker, unidades first-5 en celda). Con TODOS los fills por tomador, n>=100 en ambos periodos: **n=416, Spearman +0,092 (p=0,060), Pearson +0,068; quintiles monotonos** (ROI bruto SEL -0,110/-0,022/+0,001/+0,027/+0,131 -> TEST -0,011/-0,005/-0,005/+0,018/+0,027): hay persistencia debil POSITIVA (~20 % se conserva). Para los tomadores de S_A (n=66): ROI bruto SEL +0,107 -> TEST +0,002 (vuelve a ~0, neto de fee negativo). "Regresion a la media, no persistencia" es cierto para el top-seleccionado (winner's curse) pero "la identidad no persiste" es excesivo; el bin <-0,02 (perdedores persistentes, EV maker +0,12..+0,14) si persiste. No cambia el veredicto.
- **MODERATE - Multiplicidad subestimada.** La hipotesis ya se habia explorado antes (tab.pkl lleva tk_score/inf120; b_seleccion_adversa, b_lecciones_wallets); el K=4 solo cuenta prereg+adenda. Ademas variantes de conjunto en B cambian mucho el resultado (ver abajo), asi que el "K efectivo 5" del informe es corto.
- **MODERATE - Contraste que el informe no hizo: en B, "informados" por ROI BRUTO>=2 % (370 tomadores, 24 en B, 105 fills, 50 % del EUR)** da EXCESO_B +0,267 (IC90 cierre (+0,039,+0,515), p taker-perm 0,003, p fill-perm 0,029), EV_flag -0,335 vs +0,194. Post-hoc (mi variante, 3.a sobre el mismo B; Bonferroni x3 ~0,01 sobre p taker) pero contradice la lectura "efecto minimo": en los fills REALES de B la AS por identidad es grande, mientras que en la poblacion de otros makers es ~0,004. Sugiere AS especifica de B (cola/precio) o ruido de 112 cierres; **no invalida REJECTED en poblacion, pero la frase "no hay mejora a la vista" debe matizarse: el siguiente paso es el contrafactual en shadow sobre B con set congelado**.
- **MINOR** - Prereg dice "congelado ~12:05Z"; mtime PREREG.md 12:02:47, sets.json 12:02:59 (orden correcto, solo la hora escrita difiere). Scripts/datos de as_tomador sin commit (untracked).
- **MINOR** - USD tratado como EUR (declarado). Fee tomador 0,07*sh*p(1-p) verificada contra la columna `fee` on-chain (105.229 filas, error relativo mediano 2e-5; max abs 8,8 en algun registro). Maker fee 0, rebate no sumado (declarado).

## Tabla de cifras del INFORME
| Cifra | Estado | Mi valor / nota |
|---|---|---|
| SEL = 09-11 Oct sin fuga (pedido decia 5-11) | REPRODUCE (SEL=09-11, 3 dias; el prereg declara la desviacion) | sets S_A identicos (75=75 en SEL; 51 en TEST); S_B 59 vs 60 (56 comunes). TEST 12-21 sin solape con SEL; R_W usa solo dias previos |
| Variante SEL 05-11 (mi robustez, post-hoc) | NUEVO | S_A 7d (>=2 dias+): 141 tomadores (87 en test) EXCESO **-0,0033** (IC90 (-0,0101,+0,0029), placebo p_emp 0,80); >=4/7 dias: -0,0036; sin condicion: -0,0008 -> el efecto de S_A se debe a la seleccion de 3 dias |
| Desenlaces: cobertura oficial | REPRODUCE | 11.263 mercados 12-21 y 09-21: cobertura 100 %, 0 discrepancias vs precierre_desenlaces_cache (slug) y 0 vs precio on-chain T-30 s (2.143 comparables); 0 mercados sin desenlace -> sin sesgo de supervivencia |
| Unidad TEST n=84.200 (aprox) | NO REPRODUCE (21-Oct parcial) | dias 12-20 identicos (80.866); con 21 completo 88.826 unidades, 2.880 cierres, 2.452 tomadores |
| EV_total +0,0182 | NO REPRODUCE a TEST completo | +0,0301 (full) / +0,0177 (sin 21) |
| S_A: 6.101 unid., 51 tomadores, 7,1 % EUR | REPRODUCE | 6.366 (full) / 5.923 (sin 21); 51 tomadores; 7,10 % |
| S_A EV_IN -0,0286 / EV_OUT +0,0218 | REPRODUCE | -0,0195 / +0,0338 (full); -0,0229 / +0,0209 (sin 21) |
| S_A EXCESO +0,0036, IC90 cierre (-0,0021,+0,0089) | REPRODUCE | +0,0038 (-0,0012,+0,0087) full; +0,0031 (-0,0022,+0,0085) sin 21; IC90 por dia (-0,0011,+0,0103) |
| S_A p_perm 0,010 | REPRODUCE (anticonservador) | 0,008; permutacion a nivel unidad ignora cluster de tomador/mercado. A nivel TOMADOR (pool de 348 activos, 2.000 sorteos): p_emp **0,28** (informe 0,214) |
| S_A monedas ETH+ SOL+ XRP- ; top wallet 16,7 % | REPRODUCE | +0,0075/+0,0034/-0,0117; top 16,2 % |
| S_A mitades -0,003/+0,005/+0,013 | REPRODUCE | -0,0044/+0,0041/+0,0140 |
| S_A sin 2 mejores dias | NO en informe | **-0,0004** (full) / -0,0017: sin sus 2 mejores dias el EXCESO desaparece |
| S_B: EXCESO -0,0083, IC90 (-0,0137,-0,0032), p 1,0, 0/3 monedas, 0/3 mitades, EV_IN +0,156 | REPRODUCE | -0,0069 (-0,0126,-0,0017), p 0,9985, 0/3, 0/3, EV_IN +0,138 |
| R_W: 33.954 unid., 589 tomadores, 42,4 % EUR, cobertura 87,9 % | REPRODUCE | 35.897 (full), 603 tomadores, 42,5 %, cobertura 87,8 % |
| R_W EXCESO +0,0160, IC90 (-0,0006,+0,0320), p 0,001 | REPRODUCE (borde sensible) | +0,0146 (-0,0010,+0,0308), p 0,002 full; sin 21: +0,0176 (+0,0014,+0,0333) |
| R_W sin 2 mejores dias +0,0091; 7/10 dias>0; monedas ETH+ SOL+ XRP- | REPRODUCE aprox. | +0,0052; 6/10; ETH +0,029 SOL +0,005 XRP -0,017 |
| Dosis-respuesta bin<-0,02 +0,120 (n=13.088, 15,4 %) | REPRODUCE aprox. | +0,141 (n=13.843, 15,4 %) full; +0,124 sin 21. Por moneda ETH +0,188/SOL +0,027/XRP +0,091 (informe ETH +0,18/SOL +0,004/XRP +0,007: **NO REPRODUCE SOL/XRP**; sin 21: SOL +0,006, XRP +0,038). "Cebo solo ETH" exagerado |
| Persistencia -0,19 (n=33) | NO REPRODUCE exacto / engañosa | ver MODERATE arriba |
| B: 198 fills, 102 cierres, EV -0,0302 | NO REPRODUCE | 215, 112, **-0,0724** |
| B S_A: EXCESO +0,0025, IC90 (-0,059,+0,060) | REPRODUCE aprox. | -0,0010 (-0,057,+0,048), p 0,54 (14 fills, 6 tomadores) |
| B informados 09-18: 238 tomadores, EXCESO +0,076, IC90 (-0,004,+0,156), p 0,104 | REPRODUCE (EXCESO) / NO (composicion) | 238 reproduce; EXCESO +0,069 (-0,003,+0,140), p fill 0,11, p taker 0,075-0,14; flagged = 29 fills, 9 tomadores, 25 cierres; sin 1 peor cierre +0,059; sin 3 +0,044; por unidad de posicion +0,078 |
| Valor B informados ~+1.730 $/anio | REPRODUCE (EXCESO igual) pero NO VERIFICABLE como ahorro real | 25k*(0,863*(-0,0038)+0,0724)=+1.730; no hay sustitucion de fills |
| Visibilidad A2 (V_mkt/V_5, gap 263 s/119 s), valor 3-5 % nicho, nocional anual 25 k$ | NO VERIFICABLE (no recomputado) | |
| Placebo de seleccion S_A p_emp 0,214 | REPRODUCE aprox. | 0,28 con pool de tomadores activos (348) |

## Respuestas a la lista del encargo
1. Fuga SEL->TEST: no la hay (SEL 09-11, TEST 12-21, tk_score de R_W solo con dias previos). SEL es de 3 dias, no 5-11; con 7 dias el efecto se invierte.
2. EXCESO S_A/S_B, IC90 por cierre, permutacion, placebo, n: reproducen (tabla). S_A no cumple (1) ni sobrevive a placebo a nivel tomador ni a quitar 2 dias.
3. Persistencia: ver MODERATE (conclusion exagerada).
4. B real: ver MAJOR (215 fills, no 198).
5. Cobertura oficial 100 %, sin sesgo de supervivencia (mercados sin desenlace = 0).
6. Unidad: la poblacion es (maker, mercado, lado) con primeras 5 acc; fills agregados; IC por cierre OK; permutacion a nivel unidad anticonservadora (el placebo por tomador la corrige). B: fills 215 en 202 posiciones; EV ponderado por EUR (-0,0724) vs media por posicion (-0,0174). Fee real verificada.
