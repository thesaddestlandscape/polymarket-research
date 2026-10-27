# CONTRAPUNTO INFORMADO — ¿los makers ganan contra no informados y a B le rellenan los informados? (25-Oct-2026)
Etiqueta: **REJECTED como palanca validada (BTC: la hipótesis no se sostiene; ALT: signo compatible, IC por días cruza 0) ·
EXPLORATORY el hallazgo nuevo sobre B (le faltan los tomadores «no informados», no le sobran los informados).** 7 días de
medida (≤21 ⇒ EXPLORATORY por norma). Solo lectura, nice 19 / ionice 3 / ulimit -v 3 GB, fuera de 06-09Z, nada a real, sin crons.
Prereg `PREREG.md` (sha256 7d5c7602…, `sha256sum -c PREREG.sha256`) escrito ANTES de calcular ningún EV por clase.

## Datos y método
- `agentes_datos/f6/{T,M}_D.parquet` (de VOL/m5_onchain, 5m, 6 monedas, maker y tomador explícitos). Desenlace oficial:
  maker_ms_desenlaces_cache ∪ mapa_escala/des.json ∪ b_vs_poblacion/des_gamma.json → cobertura en € 100 % (22-Oct 99,96 %).
- Clase del tomador EX ANTE, walk-forward por día natural: historia D−7..D−1 (nada del día medido), PnL tomador a SU precio de
  ejecución neto de fee. INF = ≥30 órdenes, ≥200 $, ≥3 días, ROI≥+0,02 y ≥60 % de días positivos; DES = ídem con ROI≤−0,02 y
  ≥60 % negativos; MIX = activo resto; NUEVO = poca historia. Grupos (días previos) y medida (día D) siempre en días distintos.
- Medida 17-23 Oct: rellenos maker-compra p∈[0,05,0,30] de OTROS makers (n=1.384.350, 2,60 M€) y de B (0x659a40ff…, n=215, 221 €,
  20-23 Oct). pnl maker sin fee; rebate aparte (+0,011 €/€ en todas las clases). Scripts `scripts/s1..s4`, salidas `datos/s*_salida.txt`.

## 1. EV del maker según la clase del tomador que le rellena (población, 17-23 Oct, `datos/s2_salida.txt`)
| universo | INF | MIX | DES | NUEVO | TODOS |
|---|---|---|---|---|---|
| BTC cuota € | 7,2 % | 57,5 % | 17,6 % | 17,8 % | 2,33 M€ |
| BTC EV/€ | −0,012 | −0,056 | −0,029 | −0,010 | **−0,040** (IC90 días −0,112..+0,031; 2/7 días >0) |
| ALT cuota € | 11,2 % | 56,2 % | 18,5 % | 14,1 % | 0,27 M€ |
| ALT EV/€ | **−0,166** (IC90 cierre −0,30..−0,004; días −0,41..+0,18) | −0,051 | +0,007 | **+0,143** (IC90 días +0,034..+0,270; 5/7) | −0,026 |
- **Premisa del chief no presente en el periodo**: la población perdió en 17-23 Oct (BTC −0,040, ALT −0,026 antes de rebate);
  el «+0,03..+0,08» es de 12-21 Oct. La AS de la población por clase es ≤1 pp (BTC −0,1/−0,9/−0,4/+0,2 pp), lejos de −18..−33 pp.
- **H1 (DES−INF>0) FALLA en ambos.** BTC: dif **−0,017** (signo contrario; IC90 días −0,118..+0,103; mitades +0,032/−0,030;
  placebo p=0,61). ALT: dif **+0,173** (IC90 días −0,150..+0,332; cierre −0,035..+0,381; mitades +0,20/+0,12; sin 2 mejores días
  −0,124; placebo entre wallets p=0,23; tomador top 16 %, maker top 13 %). Dosis-respuesta por quintil de ROI previo: BTC plana
  (−0,021/−0,038/−0,024/−0,085/−0,057); ALT solo el quintil más perdedor es bueno para el maker (+0,077; resto −0,06..−0,13).
- Desvío declarado: la «inversión» del prereg (clase con signo cambiado) es tautológica (= −dif); se sustituye por la dosis-respuesta.

## 2. B (`datos/s2_salida.txt`, `s3_salida.txt`, descriptivo, post-hoc en s3/s4)
- B 20-23 Oct: EV −0,072 (IC90 cierre −0,32..+0,19; 112 cierres). Exposición vs la población en el mismo moneda×día×banda 0,05:
  **INF 10,3 % vs 8,0 % esperado (obs−esp IC90 cierre −0,011..+0,055: NO sobreexpuesto de forma demostrable)**;
  **DES+NUEVO 9,9 % vs 26,2 % (IC90 −0,195..−0,129: le FALTAN los no informados)**; MIX 79,9 % vs 65,8 % (+0,10..+0,18).
- Contribución al EV de B: INF −0,072 (IC90 −0,113..−0,022; 24 rellenos, 11 tomadores, uno 47 % del €), DES −0,048, MIX −0,009,
  NUEVO +0,056. B sin sus rellenos INF: EV −0,001 (IC90 −0,27..+0,28). Con n=24 y concentración 47 % esto es una pista, no prueba.
- El déficit de no informados no lo explica ni T ni banda (`s4_salida.txt`): en la población son el 22-32 % del € en cada tramo;
  en B el 5-11 % salvo T 180-240 (24 %). Mismo tamaño de relleno (mediana 5 acc). Inferencia (no probada): las pujas de B las
  barren sobre todo bots activos (MIX) antes de que llegue el flujo minorista.

## 3. Política «no exponerse cuando se predice informado» (entreno 17-19, una evaluación 20-23; unidad cierre; cota superior sin sustitución)
Rasgos con ts ≤ t−5 s (bloque ±2,4 s): $ tomador en el mismo mercado en [t−33,t−5) y [t−130,t−33) total y por clase, T, banda,
moneda, hora, lado. Logit.
| política | AUC test | ΔPnL 20-23 | IC90 días | IC90 cierre | sin 2 mejores días | placebo p | oráculo (clase real) |
|---|---|---|---|---|---|---|---|
| BTC saltar top-20 % P̂(INF) | 0,554 | −7.617 € | (−53.825, +37.620) | (−57.213, +36.666) | −27.164 | 0,39 | −8.252 € |
| BTC exponer solo top-50 % P̂(DES) | 0,540 | +11.926 € | (−19.967, +39.852) | (−71.553, +94.843) | −10.865 | 0,000 | **−23.962 €** |
| ALT saltar top-20 % P̂(INF) | 0,586 | +3.238 € | (−10.498, +17.209) | (−4.702, +11.372) | −5.366 | 0,000 | +3.644 € |
| ALT exponer solo top-50 % P̂(DES) | 0,602 | −8.795 € | (−20.326, +3.548) | (−17.851, +636) | −11.820 | 1,000 | +506 € |
- **Ninguna pasa el gate** (IC90 por días cruza 0 en las cuatro; sin 2 mejores días negativo en las cuatro; BH-FDR irrelevante).
- En BTC hasta el ORÁCULO pierde: saltar a los INF reales cuesta −8,3 k€ (sus rellenos daban +0,022 en 20-23). La mejora de
  «exponer DES» sale de T/T² (coeficientes dominantes), no del tipo: el oráculo de la misma regla da −24 k€ (= control de F6).
- En ALT el modelo sí apunta al tipo (s33inf +0,18; precisión 10,9 % vs base 6,6 %) y el oráculo +3,6 k€ ≈ modelo +3,2 k€,
  pero 2/4 días y el IC cruza. Hilo vivo, no palanca.
- Rasgos de libro y Binance: **missing** (on-chain no los tiene; libro5/registro ms no cruzados por presupuesto).

## 4. Veredicto y €/año honesto
La hipótesis «los makers ganan siendo contrapunto de no informados y a B le rellenan los informados» **no se sostiene en BTC**
(ni orden por clase ni AS por clase) y en ALT tiene el signo correcto sin significación (IC90 días cruza 0, placebo p=0,23).
Lo que sí aparece en B es lo inverso de la palanca supuesta: B no está demostrablemente sobreexpuesto a INF, pero recibe un
tercio de los no informados que recibe la población en el mismo moneda×día×banda. **€/año validado: 0 €.** Cota exploratoria de
la mejor política (ALT saltar INF, +2 pp sobre el € retenido) a la escala de B (~136 €/día): ≈1 k€/año, IC cruza 0.

## 5. Qué lo refutaría / siguiente (coste 0, sin tocar B)
1. Re-medir con ≥10 días más (24-Oct+) la cuota DES+NUEVO de B vs población y el EV ALT por clase (gate H1 del prereg, sin cambios).
   Refuta el hallazgo de B: cuota DES+NUEVO de B ≥ esperada −5 pp con IC90 por cierre.
2. Diagnóstico de POR QUÉ B no recibe no informados: tiempo desde que B coloca la puja hasta el relleno y clase del que la barre
   (etiquetado pasivo de B ya registra la vida de la puja desde 24-Oct). Si las pujas recién colocadas las barren MIX en <2 s,
   la palanca sería «cuándo/cómo colocar» (A/B aleatorizado de `b_vs_poblacion`), no «a quién evitar».
3. Añadir libro5/Binance como rasgos de H3 en ALT solo si 1 confirma el signo.

## 6. Reproducir
`cd experimentos/5m_barato/b_perdidas_22oct/contrapunto_informado && (ulimit -v 3000000; ARROW_DEFAULT_MEMORY_POOL=system nice -n 19 ionice -c3 python3 scripts/s1_construye.py)`
→ `python3 scripts/s2_eval.py > datos/s2_salida.txt` → `s3_b_extra.py`, `s4_donde_nuevo.py`. Datos intermedios en
`/mnt/HC_Volume_106538179/agentes_datos/contrapunto_informado/{U,daily}.pkl`. Hashes en `HASHES.txt`.
## Limitaciones
7 días (EXPLORATORY); ALT con pocos tomadores por clase (placebo p95 +0,35); clase por wallet (bots con varias wallets cuentan
como NUEVO: sesgo conocido); unidad = relleno con IC por cierre/día (no unidad maker-mercado-lado); maker sin sustitución en H3;
umbral 50 % de la variante DES fijado en el script antes de ejecutar (el prereg no lo fijaba); 24-Oct no extraído.
