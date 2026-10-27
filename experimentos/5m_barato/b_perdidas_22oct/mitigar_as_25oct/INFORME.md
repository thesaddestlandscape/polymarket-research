# MITIGAR LA AS DEL MAKER — mapa de mecanismos no probados + A1 ejecutado (25-Oct-2026, 12:20Z). Validado: 0 €. Nada a real.
Solo lectura; B, crons, procesos y F2 intactos. nice 19 / ionice idle / ulimit 3 GB; RSS máx. 1,3 GB; todo fuera de 06-09Z (11:41-12:14Z).
Prereg `PREREG_A1.md`, sha256 `30ed117f…4553` (`sha256sum -c PREREG_A1.sha256`), escrito ANTES de extraer. Hashes de scripts: `datos/HASHES_scripts.txt`.

## 1. Mapa priorizado (prob. de que funcione × €/año honesto × coste del test). No repite lo cerrado de MISION_CLICK_B ni F7/F8/E1/H1/H4.
| # | Mecanismo (qué ataca de la AS) | Estado | P | €/año honesto si sale | Coste | Nota |
|---|---|---|---|---|---|---|
| M0 | **Calibrar la etiqueta virtual** contra rellenos on-chain reales de B 20-24 Oct y su instante/nivel de armado (~1,5c bajo el mejor bid) | prerrequisito (aviso del coordinador por F8: P(relleno) 51 % virtual vs 5,1 % real) | alta (habilita) | 0 directo | bajo (`ordenes_b.json` 3.272 + on-chain + `vpv_f8.py`) | Sin esto, ningún resultado de AS en vidas VIRTUALES vale. A1 NO depende de ello (usa prints reales) |
| M1 | **(a) Libro L1 dinámico ≤2 s antes del relleno** (spread, imbalance, cambio de cola propia, velocidad del mid, tamaño del ask, actividad, edad del top, T) en población real | **EJECUTADO (A1)** | — | ver §3 | hecho | F5 pasa el prereg; frágil en latencia |
| M2 | **Disparador de recotización rival**: cancelar el bid cuando el ask del propio token baja a bid+1c con tamaño grande en los últimos ≤150 ms (lo que A1 detecta) | nuevo, sale de A1 | 0,25 | B: ≤0,7 k; techo poblacional ~280 k$ (de TODAS las makers, no nuestro) | bajo: forward pasivo con la regla A1 congelada en días ≥24-Oct + réplica BTC/DOGE/BNB | Exige reaccionar ≤100-150 ms desde la recepción del q |
| M3 | **Nivel de armado** (al mejor bid vs por debajo): en población 09-23 Oct los rellenos por debajo del mejor bid (barridos) dan EV€ +0,12/+0,20 y al mejor bid +0,02 (descriptivo, `datos/a1_post_sub.txt`), pero B arma abajo y pierde | contradicción abierta | 0,2 | 0-3 k | bajo, solo lectura con walk-forward | Comprobar con prereg; b_vs_poblacion veía barridos −0,01 en 20-22 Oct (periodo) |
| M4 | **(d) Mercados con menos AS** (5m BNB [0,30-0,40), 15m ETH [0,90-0,95), DOGE fina) a tamaño ínfimo | F2 descubrimiento | 0,2 | 1-14 k (flujo BNB ~371 €/día; ETH15 favoritos −0,053 de brecha propia ⇒ ≤0) | cron + días | 60m favoritos puja propia ya REJECTED (rellenas −0,0575) |
| M5 | **(b) Clip/vida de la puja** | no medible con datos públicos sin condicionar al tamaño final (trampa 19-Oct) | 0,15 | 0-2 k | A/B aleatorizado DENTRO de B (dinero real ⇒ Javi) | ED_A1 (cancelar a 1 s) ya ≈0 |
| M6 | Cotización continua a dos lados con inventario acotado (tintero #2) | sin test | 0,1 | 1-4 k | 60-80 k tokens | Ataca la pata suelta, no el relleno |
| M7 | (c) Régimen T-restante×precio | **cerrado aquí** para L1 (F8 de A1, T: exceso +2.374, IC90 días cruza 0) | — | 0 | — | R1-vol ya PROMISING/confusor en E1D |
| M8 | (e) Cartera de piezas pequeñas positivas | suma honesta 0-40 k€/año NO validados (tintero) + M2 a escala B ≤0,7 k | — | ≤40 k | — | Ninguna pieza validada; no se suma lo no validado |

## 2. Qué se ejecutó: A1 (M1) — rasgos L1 en los 2 s previos al print, por RECEPCIÓN
- Población: rellenos de bid de E1D (q∈(0,10;0,30], 5m ETH/SOL/XRP, últimos 300 s, desenlace oficial), **322.911 prints, 736 k$ de coste, 06-23 Oct (18 d); test walk-forward 09-23 Oct (15 d)**; terciles y lado elegidos SOLO con días anteriores; placebo = quitar la misma fracción de € al azar; K=8.
- Fuente: filas q de VOL/m5_registro (bid, ask, tamaños, recepción c[7]), extraídas a `DL/mitigar_as_25oct/q_D.gz` (`scripts/x1_extrae_q.sh`); rasgos `scripts/a1_rasgos.py`, evaluación `scripts/a1_eval.py` → `datos/a1_resultados.json`, `datos/a1_eval.stdout`. Cobertura de rasgos 98,8-100 %.
| Rasgo (τ = r−100 ms) | exceso 15 d ($) | IC90 días | p (Bonf. 0,00625) | qBH | sin 2 mejores | días + | IC90 cierre | inversión | EV€ retenido − total | gate |
|---|---|---|---|---|---|---|---|---|---|---|
| **F5 log tamaño del ask del token propio (tercil ALTO)** | **+11.445** | **(+411, +1.115)/día** | **0,0009** | 0,008 | +7.800 | 13/15 | (+5.937, +16.312) | −9.701 | +0,028 (+0,016, +0,040) | **PASA 7/7** |
| F2 imbalance tb/(tb+ta) (tercil bajo) | +6.008 | (+131, +670) | 0,0101 | 0,040 | +2.665 | 12/15 | >0 | −5.818 | +0,014 | falla Bonferroni |
| F1 spread | +9.952 | (+43, +1.284) | 0,040 | 0,108 | +3.604 | 12/15 | >0 | −5.268 | +0,021 | falla (2) |
| F3 Δcola propia, F4 vel. mid, F6 actividad, F7 edad del top, F8 T | −2.605..+4.306 | cruzan 0 | ≥0,14 | ≥0,28 | — | 7-8/15 | cruzan 0 | — | ≈0 | no |
F5: EV€ de los marcados −0,013 vs retenidos +0,086 (población, cuyo EV total es +0,055 en este periodo, no −0,03 como B). Tasa de disparo: 29 % de los prints vs 24 % en instantes de control (casi no anticipa CUÁNDO llega el relleno; filtra calidad, con ~24 % del tiempo fuera).

## 3. Controles post hoc (NO preregistrados, declarados) — cambian la lectura
- **Perfil de latencia** (`datos/a1_post_eval.txt`): F5 exceso +11.445 (100 ms) → +9.268 (150) → +6.638 (200, IC apenas >0) → **+2.255 (250, IC cruza 0) → negativo a 400-5.000 ms**. La señal vive en los últimos 100-200 ms antes de RECIBIR el print: es el ask que baja sobre nuestro bid justo antes del relleno (Δask 1.000→100 ms: baja en el 45,5 %; ask(τ) ≤ q+1c en el 68,8 %), es decir, **recotización de makers más rápidos**, no un estado del libro estable. Mismo hueco que el taker delay (~145 ms) ya visto en E1C.
- Estratificado moneda × bucket 0,05 de q: +13.631, IC90 (+630, +1.188), 14/15 días → no es composición de precio/moneda. Por moneda: ETH +11.304 (14/15), SOL +2.081 (11/15), XRP +234 (IC cruza 0): **casi todo ETH**.
- Por nivel: rellenos AL mejor bid +7.528 (IC>0; marcados −0,073 vs retenidos +0,021); **rellenos por DEBAJO del mejor bid (tipo B) +2.640, IC90 cruza 0** (marcados +0,125 vs +0,195). Para la colocación actual de B, no hay efecto demostrado.
- Límites: unidad = print (no orden con cola); placebo sustractivo (no modela recolocación); empates de mismo ms ordenados por valor (no por llegada); la factibilidad exige q recibido ≥100-150 ms antes del casado + cancelación 60 ms: sin medir con órdenes propias.

## 4. Veredicto y €/año honesto
**A1/F5 = PROMISING (población), frágil**: pasa el gate preregistrado a 100 ms, pero (i) desaparece a ≥250 ms, (ii) es ETH, (iii) no se ve en rellenos por debajo del mejor bid (los de B). €/año: **validado 0**. A escala B (≈65 €/día de coste relleno, +0,028 €/€) ≈ **0,7 k€/año** y solo si B cotizara al mejor bid con cancelación ≤100 ms; B seguiría ≈0 o negativo. Techo poblacional ≈763 $/día (≈280 k$/año) es de TODAS las makers de la banda, no capacidad nuestra.

## 5. Siguientes 3 (elegido el 1)
1. **M2 forward pasivo de F5 congelado** (regla y cortes de A1 sin tocar) en días nuevos ≥24-Oct de m5_registro + réplica BTC/DOGE/BNB (extraer q de esas monedas): resuelve si es real con coste de minutos/día; gate = el de PREREG_A1 con ≥10 días nuevos (≈04-Nov). Valor de la información alto: es la única señal de AS que pasa en población con 15 días.
2. M0 calibración virtual↔real (habilita todo lo virtual).
3. M3 nivel de armado con prereg (contradicción B vs población).
Reproducir: `cd scripts && nice -n 19 ionice -c3 ./x1_extrae_q.sh && ulimit -v 3000000 && nice -n 19 ionice -c3 python3 a1_rasgos.py && python3 a1_eval.py && python3 a1_post_lags.py && python3 a1_post_eval.py && python3 a1_post_sub.py` (~25 min extracción + ~6 min).
