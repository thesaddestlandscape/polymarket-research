# F3 «CARRY ≥0,90 MAKER» — informe (25-Oct-2026 ~11:50Z). DESCUBRIMIENTO; dev/shadow, nada a real.
Prereg `PREREG_F3.md` sha256 `9ec4ba36200f7b61bf8077ad419ff0a68b71f075a1ab31eeeb0570f040b1ca6e` (escrito antes de calcular). Código `scripts/` (hashes `datos/HASHES_scripts.txt`); salidas `datos/` (celdas.csv, vpv_celdas.csv, placebo.json, racimos.json, cobertura.csv, logs). Intermedios en `/mnt/HC_Volume_106538179/agentes_datos/f3_carry/`. Reproducir: `scripts/run_extrae.sh`, `scripts/f3_des.py`, `scripts/f3_analisis.py`, `scripts/run_vpv.sh`, `scripts/f3_vpv_analisis.py`.

## Veredicto
**NO validado; REJECTED como motor de capital.** El EV de POBLACIÓN (rellenos de todos los makers) es ≥0 y pequeño, pero la puja propia al final de la cola (vpv, regla pesimista primaria) pierde: AB agregado 5m+15m EV **−0,047** (IC90 cierres −0,055..−0,039, n=45.631 rellenas, 3.778 cierres, 10 días, 0/10 días +), acierto−precio **−4,4 pp**, gap rellenas−no rellenas **−8,8 pp** (−9,4..−8,1). Falsador del prereg (hit−p<0 / EV<+0,005 pes) cumplido -> cierre.

## P1 población (on-chain maker, 06..23-Oct = 18 d + 24-Oct forward; cobertura desenlace oficial 100,0 % del coste en todos los marcos, missing=0)
- 24 celdas K (6 monedas × 5m/15m × [0,90-0,95)=A/[0,95-1,00)=B); 3 pasan gate P1 (BH q<0,10): **15m ETH A** EV +0,032 (IC90 días +0,022..+0,041; sin 2 mejores días +0,027; DESC +0,033/HOLD +0,031/FWD 24-Oct +0,033; 15/18 d+; 1.508 cierres; fallos 7,5 % vs equilibrio 8,0 %), 15m SOL B +0,014 (HOLD +0,012), 5m XRP B +0,009 (HOLD +0,003, FWD −0,002). Reproduce F2 (ETH15 0,90-0,95 +0,031).
- Agregados: 5m ALL AB +0,003 (IC90 −0,002..+0,008), 15m ALL AB +0,007 (−0,001..+0,014); BTC 5m/15m ≈0. Pc≥0,99 (excluido por F2): −0,004 (5m, 6,9 M€) / −0,0002 (15m). Placebo/inversión: top-8 DESC→HOLD +0,0106 vs azar +0,0072 (p95 +0,0134) vs peores +0,0066, p=0,25: el ranking no ordena. 3 de 24 con q<0,10 ≈ lo esperable tras multiplicidad con celdas contiguas.
- 60m/4h/24h (6 días, NO en K, sin libro -> sin vpv): 60m ALL AB +0,015 (IC90 días −0,007..), ETH 60m +0,038, SOL −0,016; 4h +0,037; 24h ruido. No concluyen.
- Cola: 5m: 1.008 de 5.136 cierres (19,6 %) tienen ≥1 unidad ≥0,90 fallada y 354 (6,9 %) ≥2 monedas a la vez (racimo); 15m 397/1.728 y 140. Un fallo = −100 % del coste: peor unidad 822 € (15m ETH A, de un maker grande), peor cierre −821 €, peor día −382 € en esa celda. A escala B (stake ≤2 €): un fallo −2 €, ocurre en ~8 % de las fills de A y ~3 % de B; EV de +0,03 equivale a ~+0,06 € por fill.

## P2 selección adversa directa (pujas virtuales 5 acc fin de cola, bid favorito [0,90-0,99], vida 60 s, 10 días 15..24-Oct, 195.865 pujas, 5m y 15m, desenlace oficial)
| celda (pes) | rellenas | cierres | EV con rebate | IC90 cierres | hit−p | gap pp |
|---|---|---|---|---|---|---|
| 5m A [0,90-0,95) ALL | 17.960 | 2.760 | −0,071 | −0,084..−0,060 | −6,6 | −12,5 |
| 5m B ALL | 8.067 | 1.999 | −0,035 | −0,047..−0,024 | −3,5 | −6,2 |
| 15m A ALL | 11.119 | 949 | −0,038 | −0,055..−0,020 | −3,5 | −6,9 |
| 15m B ALL | 8.485 | 874 | −0,020 | −0,034..−0,008 | −2,0 | −4,2 |
| **15m ETH A** (la pista de F2) | 2.952 | 703 | **−0,003** | −0,023..+0,022 | −0,35 | −5,3 |
| 15m BTC B | 2.763 | 571 | −0,006 | −0,023..+0,010 | −0,6 | −2,2 |
| 15m BTC A / ETH B | 3.458 / 2.371 | 755 / 553 | −0,015 / −0,013 | cruzan 0 | −1,5 / −1,3 | −5,5 / −3,4 |
| alts finas 5m A (SOL, XRP, DOGE, BNB) | 874-3.784 | 489-1.610 | −0,07 a −0,19 | todos <0 | −7 a −18 | −14 a −22 |
Todas las 24 celdas moneda×marco×bucket (regla pes) tienen EV central ≤0; ninguna con IC90 inferior >0; las únicas que no son significativamente negativas son BTC 15m (A, B) y ETH 15m (A, B), todas con IC90 que cruza 0. Regla optimista (cota: cuenta caídas de profundidad/cancelaciones como relleno, 80 % de fill): AB agregado **+0,009** (IC90 +0,004..+0,014), 15m ETH A +0,027 (+0,011..+0,044), 5m XRP B +0,012; incluso así el gap rellenas−no rellenas es −4,6 pp (selección adversa presente en cualquier regla). La verdad está entre ambas; el techo (opt) ya es ≤ +0,027 por € en la mejor celda.
La AS crece con la ilíquidez de la moneda (BTC −2 a −10 pp, DOGE/BNB −10 a −22 pp) y hacia el bucket A: quien se rellena en la cola es el vendedor informado del favorito.

## Capacidad (€/año, honesta)
- Pool poblacional de las 3 celdas gate1 (EV HOLD, cuota 1 %/5 %×0,28/5 %): 15m ETH A cons 1.039 / base 2.574 / opt 9.194 pUSD; SOL15 B 0/370/1.321; XRP5 B 0/85/302 -> total cons ≈1,0 k, base ≈3,0 k, opt ≈10,8 k pUSD/año, **todo con EV de población**; con el EV de la puja en cola (pes) es ≤0 y con estrés de B (−0,053) negativo. Aunque se usase la cota opt (+0,027) a escala B (2 €/fill, ≲20 fills/día): ≲0,4 k €/año. Cartera ≥0,90 agregada al EV opt +0,009 con capital de 20 pUSD: ~3 k/año como mucho. **Aporta ≈0 € a 200 k.**

## Límites / qué falta
- Días 06..23-Oct ya vistos a nivel agregado por F2: P1 es descubrimiento; solo 24-Oct es no visto (1 día). vpv 10 días (15..24-Oct); 5 acc, vida 60 s, relleno por consumo de cola (A+B puede doble contar un mismo cruce -> pes no es estrictamente pesimista en el instante, sí en la cola).
- Sin vpv para 60m/4h/24h (sin registro de libro); 60m ≥0,90 sin puja medida: el 60m [0,70-0,90) ya está REJECTED por el coordinador y el ≥0,90 de 60m es n pequeño (137 cierres A+B, 6 días).
- Rebate inferido (0,014·(1−pc)), no observado; ≤0,0007 por € a p=0,95, irrelevante.
- No se mira T<60 s ni colocación con vida mayor/cancelación; no hay reverificación independiente desde datos crudos (pendiente red team). Dependencia entre pujas superpuestas mitigada con cluster por cierre; sensibilidad primera-puja-por-mercado-lado (ev_1ra) coherente (−0,044 AB).
- Qué cambiaría el veredicto: relleno medido con órdenes reales mínimas (F5, decisión de Javi) o libro L2 con IDs de orden para posición de cola real.
