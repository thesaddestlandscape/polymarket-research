# F2 «MERCADOS CON MENOS SELECCIÓN ADVERSA» — informe (24-Oct-2026, 12:25Z)
Estado: **DESCUBRIMIENTO / EXPLORATORY** (nada pasa un gate forward). Solo lectura; B, live, crons y módulos intactos. Unidad monetaria: pUSD (~USD), sin convertir a EUR (restaría 10-15 %).
Prereg escrito ANTES de calcular: `PREREG_F2.md` sha256 `6c54ac3ef8d1d4cc4ecc387f70040ed21d925044808c16add6ba4c4f55388288`. Código: `scripts/` (hashes `datos/HASHES_scripts.txt`). Datos intermedios: `/mnt/HC_Volume_106538179/agentes_datos/f2_menos_as/` (`u_<marco>_<día>.csv.gz` unidades, `m_*` maker, `vpv_*` pujas virtuales). Salidas: `datos/celdas.csv` (todas las celdas), `capacidad.csv`, `posthoc.csv`, `coin_banda.csv`, `placebo.json`, `vpv_as.csv`, `makers_concentracion.json`, `cobertura.csv`.

## 0. Respuesta corta
1. **Pregunta**: ¿hay moneda × marco × bucket(0,05) donde el relleno maker NO sufre la AS? **Respuesta: en el 5m barato (0,10-0,30), NO, en ninguna moneda** (medido directo con pujas virtuales: rellenas aciertan −20 a −27 pp menos que las no rellenas en las 6 monedas, IC90 estrechos; la «mejor» es BNB −21,7 pp y la peor BTC −27,4 pp). Donde el EV del relleno es positivo y persiste NO es por falta de AS sino por **otra estructura de precios: el lado FAVORITO** (comprar 0,80-0,99 = vender el boleto del longshot) y las alts finas.
2. **Celdas que sobreviven** (K=240 celdas moneda×marco×bucket 5m/15m; 5 con BH q<0,10 en 18 días; 2 pasan además BH en el HOLD de 9 días): **15m ETH [0,90-0,95)** (EV +0,031, IC90 días +0,021..+0,040, 15/18 días +, DESC +0,032 / HOLD +0,030) y **5m BNB [0,30-0,35)** (+0,118, IC90 +0,066..+0,168, 14/18 d, DESC +0,082 / HOLD +0,161). Las celdas vecinas (ETH 15m 0,80-0,95; BNB 5m 0,35-0,40) son la misma zona.
3. **15m ETH favoritos: «robustos» se confirma con desenlace oficial** (cobertura 100,0 % del coste): [0,80-0,99) EV +0,025 (IC90 días +0,018..+0,031), 16/18 días +, sin 2 mejores días +0,021, 402 makers, **77 % de los makers positivos**, sin el top-1/top-3/top-10 por coste +0,023/+0,023/+0,023, top-1 14 % del coste. Pero: modesto (+2,5 %), HOLD +0,022, y **las primeras 5 acciones de cada unidad rinden +0,005** (el EV está en el resto de la cola, no en llegar primero). Pool TOTAL de todos los makers ≈ 0,48 M pUSD/año; B a 1 %/5 % de cuota: 2,5 k / 24 k (opt). Con la brecha de ejecución medida de B (−0,053) el EV de la celda queda en −0,03: **no llega**.
4. **BTC 5m 0,05-0,30 (56 % del neto de los grandes con 10 % del volumen, según la misión) NO persiste**: EV 18 d +0,039 (IC90 días −0,016..+0,087), DESC +0,091 → HOLD −0,011; 11/18 d +; 15-23-Oct negativo en 0,10-0,20. El resultado «los grandes de BTC ganan» no es de la población de makers en esa banda en las últimas 9 jornadas.
5. **Regla de selección anti-persistente (placebo/inversión)**: top-20 celdas por EV_DESC → HOLD **−0,038**; 20 al azar −0,0003 (p95 +0,019); las 20 peores en DESC → HOLD **+0,041**; P(azar ≥ top)=0,98. Las celdas de mayor EV en 06-14-Oct revierten en 15-23-Oct (régimen/dirección del periodo dominando). Cualquier forward que elija «las mejores celdas del descubrimiento» está sesgado a la baja.
6. **Alts finas (BNB, DOGE)**: positivo en casi todo 0,10-0,40 tanto en 5m como en 15m (BNB+DOGE 5m+15m [0,10-0,40) +0,065 IC90 días +0,021..+0,107, 12/18 d; HOLD +0,086; post-hoc), coherente con menos AS en monedas con menos flujo informado (vpv: BNB gap menor en la regla optimista, −22 pp frente a −37..−40 pp en ETH/SOL/XRP). **Capacidad ridícula**: flujo de todos los makers 9 k pUSD/día en esas celdas; pool total ≈ 0,29 M/año, B al 5 % opt 14 k, cons 0,7 k. HYPE: sin tokens en el registro (no existe en el mapa de mercados capturados; no verificado contra gamma).
7. **60m favoritos [0,70-0,90) BTC/ETH/SOL**: +0,076 (IC90 días +0,042..+0,115, 6/6 días +, sin 2 mejores +0,048, 144 cierres), pool 2,5 M/año; 4h [0,65-0,99) +0,076 (36 cierres). **Solo 6 días (18..23-Oct): NO se puede decir nada** (gate n≥40 cierres y ≥10 días); es el nicho con mejor ratio capacidad×EV y no está en el TP1 congelado. **Falta el dato: 4 días más** (ver §6; el cron `mapa_infra_diario.sh` NO está instalado).
8. **Techo agregado**: suma de celdas defendibles (ETH15 favoritos + BNB/DOGE finas + carry BTC 5m 0,95-0,99): cons ≈ 10 k, base ≈ 29 k, opt ≈ 117 k pUSD/año a 1 %/5 %/5 % de cuota, **todo DESCUBRIMIENTO y con estrés (−0,053) ≤ 0 salvo BNB**; no cuenta como ingreso. **No hay celda menos-AS con capacidad y EV simultáneos para acercarse a 200 k.**

## 1. Método y datos (resumen; detalle en el prereg)
- Fuente: rellenos on-chain MAKER (`taker != 0xe111…`), `m5_onchain`/`m15_onchain` 06..23-Oct (18 d; 05-Oct parcial excluido), `m60/m240/m24h_onchain` 18..23-Oct (6 d). Mapa token→mercado = unión `tokens.json` (mapa-escala) + `tokmap/*.k.json` + gamma D (4h/diario). Duplicados (tx,log_index) = 0 en todos los días.
- Unidad: (mercado, lado comprado, bucket 0,05 del precio del lado comprado); venta a q = compra del contrario a 1−q; T al cierre en (60 s, L]. Maker sin fee; **rebate inferido 0,014·(1−pc) por € reportado aparte** (`ev_reb`; no hay pago observado). Misma lógica de extracción que `mapa_escala/s2_celdas.py` (bucket 0,05 en vez de bandas gruesas; reproduce sus cifras: 5m BTC 0,20-0,30 +0,04 aquí frente a +0,060 allí por los 2 días extra negativos; 15m ETH 0,70-0,99 +0,022 frente a +0,025-0,027).
- Desenlace OFICIAL: cache mapa-escala + `maker_ms_desenlaces_cache` + gamma `closed=true` (796 de 802 mids pendientes resueltos). **Cobertura del coste: 5m 100,0 %, 15m 100,0 %, 60m 100,0 %, 4h 100,0 %, diario 95,1 %** (`datos/cobertura.csv`). 503.175 unidades 5m, 194.115 de 15m, 9.195 de 60m, 2.962 de 4h, 885 diario.
- Estadística: EV = Σpnl/Σcoste. IC90 por bootstrap de días (2000) y de cierres (cluster por `fin`, 1000); sin 2 mejores días; sin 5 mejores cierres; DESC = 06..14-Oct, HOLD = 15..23-Oct; K=240 (6 monedas × 20 buckets × {5m,15m}); BH-FDR sobre p unilateral por días (suelo 1/2000). 122 celdas con EV_DESC>0 y ≥20 cierres en cada mitad; **11 «candidatas» por la regla del prereg** (EV_HOLD>0, ≥40 cierres HOLD, sin 2 mejores días HOLD >0 y [IC90 días HOLD lo>0 o BH-HOLD q<0,10]); la regla permite el OR, así que la lectura estricta es la de BH en ambos (2 celdas, Tier A).
- AS directa: `vida_puja_virtual_5m.py` (5m, bid 0,10-0,30, T 60-300 s, 5 acc al final de la cola, vida 60 s), **9 días (15..23-Oct), 181.025 pujas virtuales, desenlace oficial 100 %**. Dos reglas de relleno: `pes` (solo prints que consumen la cola) y `opt` (incluye caídas de profundidad). IC90 por cierre.

## 2. Ranking de celdas (todas: `datos/celdas.csv`)
Columnas: EV pond.; IC90 días / IC90 cierres; sin 2 mejores días / 5 mejores cierres; DESC / HOLD; días +; cierres; top-1 maker; flujo = coste maker medio por día.
**Tier A — pasan prereg + BH en 18 d y en HOLD (2 de 240; con q<0,10 y K=240 el azar permitiría ~0,1·(nº de rechazos) falsos positivos entre las aprobadas, pero las celdas contiguas no son independientes: ETH 0,80-0,95 son 3 celdas, BNB 0,30-0,40 son 2):**
| celda | EV | IC90 días | IC90 cierres | sin2d / sin5c | DESC / HOLD | días + | cierres | top-1 | flujo €/día | EV+rebate |
|---|---|---|---|---|---|---|---|---|---|---|
| 15m ETH [0,90-0,95) | +0,031 | +0,021..+0,040 | +0,018.. | +0,026 / +0,029 | +0,032 / +0,030 | 15/18 | 1.508 | 14,5 % | 16.306 | +0,032 |
| 5m BNB [0,30-0,35) | +0,118 | +0,066..+0,168 | +0,038.. | +0,088 / +0,086 | +0,082 / +0,161 | 14/18 | 1.870 | 23,7 % | 371 | +0,127 |
**Tier B — «candidatas» del prereg que no pasan BH-HOLD o BH-18 d (9)**: 5m BNB [0,35-0,40) +0,095 (HOLD +0,094, q_BH18d 0,024, q_BH-HOLD 0,209); 15m ETH [0,85-0,90) +0,026 (HOLD +0,034; q 0,024/0,252); 5m SOL [0,25-0,30) +0,067 y [0,30-0,35) +0,055 (IC90 días cruza 0; HOLD +0,087/+0,067; q18d 0,48/0,51); 5m BTC [0,95-1,00) +0,006 (IC90 +0,001..+0,011, HOLD +0,010; q18d 0,37, q-HOLD 0,049); 15m BTC [0,50-0,55) +0,031 (sin 5 mejores cierres −0,011: frágil); 15m BNB [0,05-0,10) +0,355, [0,10-0,15) +0,258, [0,25-0,30) +0,139 (flujo 170-420 €/d, IC90 días ≈0 por arriba; q18d 0,47/0,47/0,13).
**Cercanas no candidatas**: 15m ETH [0,80-0,85) q18d 0,024 pero HOLD +0,016 con IC90 −0,007 (q-HOLD 0,62).
**Negativas con IC90 <0 (útiles para descartar)**: 15m ETH [0,10-0,30) **−0,126** (IC90 días −0,167..−0,084; las pujas longshot de ETH 15m son la AS pura mientras sus favoritos ganan: el mismo mecanismo invertido); 5m XRP [0,50-0,70) −0,024; 5m ETH [0,50-0,70) −0,027; 60m ≤0,35 (−0,11 a −0,48, 6 días, 0-3 días +).
**Por moneda y banda gruesa** (todas las monedas, `datos/coin_banda.csv`): longshots 5m [0,10-0,30): BTC +0,038 (HOLD −0,012), ETH +0,058 (HOLD −0,075), SOL +0,071 (IC90 +0,004..+0,141; HOLD +0,055), XRP −0,016, DOGE +0,049 (HOLD +0,124), BNB +0,078 (HOLD +0,093); favoritos 5m [0,90-1,00): +0,002..+0,009 todas (BTC +0,005 IC90 −0,001..+0,012); medio [0,50-0,70) negativo en 5 de 6 monedas.
**Hipótesis de trabajo (no probada)**: la AS por moneda en 5m es casi plana (−21..−27 pp) y el EV de población positivo en alts finas viene sobre todo de FLUJO TOMADOR menos informado (menos Binance-lead), no de ausencia de AS para quien pone una puja en cola.

## 3. Placebo / inversión y multiplicidad
- Selección DESC→HOLD: `datos/placebo.json` (k=20 de 240 elegibles): top −0,0376, azar −0,0003 (p95 +0,019), bottom +0,0412, p_placebo=0,983. **El ranking de descubrimiento es inversamente predictivo.**
- BH-FDR: K=240; 5 celdas con q18d<0,10 (BNB 5m 0,30-0,40; ETH 15m 0,80-0,95), 2 con q-HOLD<0,10 además. Las celdas contiguas no son independientes (corr alta), así que la multiplicidad efectiva es menor que K pero las 5 son ~2 hallazgos (una zona BNB 5m, una zona ETH 15m favoritos).
- Los grupos agregados (PH1-PH12 en `posthoc.csv`, ej. «ETH 15m [0,80-0,99)», «BNB+DOGE», «BTC 5m [0,05-0,30)») se miraron DESPUÉS de ver las celdas: **post hoc, no cuentan para K ni como confirmados**.

## 4. Selección adversa medida (solo 5m, banda 0,10-0,30; resto = DATO QUE FALTA)
Pujas virtuales de 5 acc al final de la cola; diferencia de ACIERTO rellenas − no rellenas (pp), IC90 por cierre (`datos/vpv_as.csv`, 9 días 15..23-Oct, n pujas 181.025, 2.591 cierres):
| moneda | n rellenas / no (pes) | acierto rellenas / no | **gap pes (pp)** IC90 | gap opt (pp) IC90 | EV puja rellena pes / opt |
|---|---|---|---|---|---|
| ALL | 85.161 / 95.857 | 13,4 % / 33,3 % | **−19,9** (−20,7,−19,2) | −28,7 (−29,6,−27,8) | −0,358 / −0,027 |
| BTC | 24.390 / 3.558 | 17,9 / 45,3 | **−27,4** (−29,3,−25,5) | −37,8 (−41,0,−34,7) | −0,182 / −0,061 |
| ETH | 19.180 / 10.561 | 14,1 / 37,3 | **−23,2** (−24,6,−21,7) | −40,0 (−42,4,−37,3) | −0,339 / −0,045 |
| SOL | 16.042 / 14.375 | 13,3 / 38,0 | **−24,7** (−26,0,−23,4) | −38,2 (−40,5,−36,0) | −0,353 / +0,054 |
| XRP | 11.542 / 19.307 | 9,0 / 32,5 | **−23,4** (−24,8,−22,1) | −36,6 (−38,4,−34,6) | −0,539 / −0,053 |
| DOGE | 7.671 / 24.390 | 8,1 / 30,9 | **−22,9** (−24,3,−21,5) | −29,1 (−30,7,−27,6) | −0,583 / −0,000 |
| BNB | 6.336 / 23.666 | 8,2 / 29,9 | **−21,7** (−23,1,−20,4) | −22,2 (−23,5,−20,8) | −0,582 / −0,066 |
Por bucket de 0,05 (BTC y ALT3, pes): gap −26 a −29 pp (BTC), −20 a −23 pp (ALT3) en los cuatro buckets 0,10-0,30. **Ninguna moneda ni bucket del 5m barato tiene una AS cercana a 0**; BNB es la menos mala solo en la regla optimista (y por ser un mercado fino con poco flujo, no por ser «seguro»). Lectura: el EV de población (+0,05 en 5m 0,10-0,30 ALL, 18 d) y el de la puja en cola (−0,03 a −0,36 según regla; B real −0,072) difieren por dónde estás en la cola, coherente con la brecha de B.
**No existe esta medición para 15m/60m/4h/diario** (no hay pujas sin relleno en on-chain; `l2_15m` existe pero no se ha explotado). La pregunta «¿tienen los favoritos de 15m ETH AS menor para una puja en cola?» **no está medida**: lo único medido es el EV de la población que SÍ se rellenó (+0,025), que ya incluye la AS del mercado pero no la de la posición de B en la cola.

## 5. Capacidad y €/año a escala B (todo DESCUBRIMIENTO; `datos/capacidad.csv`; pUSD/año)
Fórmulas: flujo = coste maker medio/día de la celda (techo absorbido por TODOS los makers); cons = 1 % del flujo × max(0, min(IC90-lo días HOLD, sin2d HOLD)); base = 5 % × 0,28 (retención) × EV_HOLD; opt = 5 % × EV_HOLD; estrés = 5 % × (EV_HOLD − 0,053); 5acc = «primeras 5 acc de cada unidad» × EV de esa variante. Para 60m/4h HOLD = los 6 días (no hay partición).
| celda | días | flujo €/día | EV HOLD | IC90-lo días / sin2d | EV 5 acc | cons | base | opt | estrés | 5 acc/unidad | pool total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH 15m [0,80-0,99) | 18 | 59.024 | +0,022 | +0,012 / +0,015 | +0,004 | 2.500 | 6.713 | 23.974 | −33.117 | 2.466 | 479.478 |
| BNB 5m [0,30-0,40) | 18 | 810 | +0,128 | +0,060 / +0,086 | +0,080 | 176 | 529 | 1.890 | +1.106 | 10.021 | 37.794 |
| BNB+DOGE 5m+15m [0,10-0,40) (post hoc) | 18 | 9.155 | +0,086 | +0,021 / +0,032 | +0,062 | 716 | 4.009 | 14.318 | +5.462 | 56.349 | 286.353 |
| BTC 5m [0,95-0,99) carry | 18 | 445.960 | +0,010 | +0,004 / +0,007 | +0,012 | 6.584 | 22.132 | 79.043 | −352.312 | 4.450 | 1.580.863 |
| 5m ALL [0,90-0,99) carry | 18 | 879.168 | +0,010 | +0,001 / +0,005 | +0,002 | 4.654 | 45.126 | 161.163 | −689.212 | 5.374 | 3.223.254 |
| BTC 5m [0,05-0,30) (zona «B-like») | 18 | 302.999 | −0,011 | −0,095 / −0,079 | −0,012 | 0 | −16.790 | −59.964 | −353.040 | −6.594 | −1.199.288 |
| ALT3 5m [0,10-0,30) (zona de B) | 18 | 32.922 | −0,044 | −0,149 / −0,093 | +0,015 | 0 | −7.398 | −26.422 | −58.266 | 16.735 | −528.438 |
| 60m BTC/ETH/SOL [0,70-0,90) (**6 d**) | 6 | 88.408 | +0,076 | +0,042 / +0,048 | +0,031 | 13.632 | 34.400 | 122.859 | +37.346 | 11.689 | 2.457.177 |
| 4h [0,65-0,99) (**6 d, 36 cierres**) | 6 | 22.668 | +0,076 | +0,016 / +0,015 | +0,016 | 1.219 | 8.796 | 31.413 | +9.487 | 3.464 | 628.252 |
- **Suma sin solape de lo defendible hoy** (ETH15 favoritos + BNB 5m + BNB/DOGE fino sin duplicar BNB 5m 0,30-0,40 ≈ restar 529/1.890 + carry BTC 5m 0,95-0,99): cons ≈ 2,5+0,7+6,6 = **≈ 10 k**, base ≈ 6,7+4,0+22,1 = **≈ 33 k**, opt ≈ 24+14+79 = **≈ 117 k**; con estrés de B −0,053 solo BNB/DOGE queda >0 (+5 k). 60m y 4h serían +13,6/34/123 k (60m) pero con 6 días. **Hueco a 200 k: > 83 k incluso en el optimista y sin estrés.**
- Capital: no limita (posiciones ≤15 min; mapa-escala: exposición p95 de toda la población 0,7-1,3 k en estas celdas; a 5 % de cuota 35-70 €).
- Qué cambiaría el número: (i) una brecha propia ≈ 0 en favoritos 15m/60m (T-REAL, decisión de Javi); (ii) que 60m [0,70-0,90) aguante 10 días (pool 2,5 M); (iii) K>5 con cola medida (TP2).

## 6. Qué forward pasivo congelar (coste 0; requiere instalar `mapa_infra_diario.sh`, hoy NO instalado → sin cron el 24-Oct no se computa)
Reglas fijadas aquí antes de ver datos futuros; unidad mercado+lado+bucket, desenlace oficial, EV ponderado por €, IC90 por día y por cierre, sin 2 mejores días, ≥10 días y ≥40 cierres; sin retocar:
- **FW-60M**: 60m BTC/ETH/SOL, comprado en [0,70-0,90), T∈(60,3600] s. Gate EV ≥ +0,03, IC90 días lo > 0, ≥7/10 días +, sin 5 mejores cierres >0. Los 6 días 18..23-Oct son DESC (no se re-usan para el gate); forward desde 24-Oct. **Es el candidato de mayor valor de la información** (pool 2,5 M, B 1 % = 25 k) y no está en el TP1 congelado (N1 5m BTC 0,20-0,30; N2 15m ETH 0,70-0,99; N3 5m 0,90-0,99).
- **FW-ETH15-FAV**: 15m ETH [0,80-0,99) (subcelda de N2 con la que ya estamos): gate EV ≥ +0,01, IC90 días lo > 0, y **informe separado de EV de 5 primeras acc** (la variante de B), gate ≥ 0.
- **FW-ALTFINAS**: BNB 5m [0,30-0,40) y BNB+DOGE 15m [0,10-0,40) (sin mezclar con 5m): gate EV ≥ +0,03, IC90 días lo > 0. Es una sonda de mecanismo (AS menor en monedas finas), no una fuente de ingresos (capacidad < 15 k pUSD/año).
- **FW-4H**: 4h [0,65-0,99): gate ≥ 40 cierres (hoy 36 en 6 días: 6/día → 40 el día 7) y ≥ 10 días.
- **FW-AS (logger pasivo ya existente)**: `vida_puja_virtual_5m.py` diario (≈ 3 min/día, solo lectura de `m5_registro`) para seguir el gap por moneda; extenderlo a 15m (registro `m15_registro`/`l2_15m`) es lo que falta para medir la AS de los favoritos 15m.
- No congelar: BTC 5m 0,05-0,30 (no persiste), selección «top celdas del DESC» (inversamente predictiva), 15m BNB/DOGE longshots (flujo < 500 €/día).

## 7. Límites y lo que falta
- 18 días de un régimen; las dos jornadas 22-23-Oct movieron el signo de BTC 5m; DESC/HOLD de 9 días cada uno → ICs de HOLD anchos.
- EV de **población** ≠ EV de una puja en la cola de B: la brecha medida de B (−0,053, n=202, IC90 por cierre −0,32..+0,20) es solo estrés. **Para los favoritos 15m/60m esa brecha no está medida.**
- Rebate inferido, no observado. Fee de maker = 0.
- 60m solo BTC/ETH/SOL (XRP/DOGE/BNB 60m no capturados, no verificado en gamma); HYPE sin tokens; diario cobertura 95 %.
- La ventana T∈(60,L] copia la de mapa-escala; no se miró T≤60 s ni el perfil por T dentro del 15m.
- El resultado BNB 5m 0,30-0,40: 109 makers, EV +0,107 (muestra completa 7.660 fills), top-1 21 % del coste y 21 % del PnL; sin top-1 +0,107, sin top-3 +0,097 (por PnL). No es un maker/bot: pero son 88 pUSD/día de PnL para todos los makers juntos.
- No se re-verificó desde datos CRUDOS por otro agente (regla del flujo): la extracción reutiliza la lógica de `mapa_escala/s2_celdas.py` y su cache de desenlaces; **pendiente reverificación independiente** de Tier A y 60m.
- Ejecución: una corrida extra (BNB/ETH concentración por maker) se lanzó concurrente a otra pesada de esta sesión (nice 19, <1 GB); load medio 16-20 por trabajos de otros agentes.
