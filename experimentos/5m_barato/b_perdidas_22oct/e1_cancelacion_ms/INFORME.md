# E1C — ¿Elimina una CANCELACIÓN en ms la selección adversa de B? 24-Oct-2026. EXPLORATORY, solo lectura (B, live, crons, ejecutores intactos)
Prereg congelado ANTES de calcular: `prereg/PREREG_E1C.md` (sha256 9b064af9…, `sha256sum -c prereg/PREREG_E1C.sha256`). Ya visto antes (no ciego):
as_b_trades (AS de rellenas) y cola_posicion/control_b (el nivel se vacía antes del relleno) → la familia DEPTH está motivada por datos vistos.
Forward pasivo: `prereg/PREREG_E1C_FORWARD.md` (sin cron: lo decide el chief).

## Veredicto: **NINGUNA política pasa el gate preregistrado (0/7 familias).** Mejor candidata limpia: **BN_W300_X2** (cancelar si Binance se mueve ≥2 bps en contra en 300 ms) → EXPLORATORY.
| Familia (elegida en TRAIN 20-21 Oct) | TEST 22-Oct ΔPnL (evita/55) | placebo p (α=0,0143) | IC90 cierre | EV€ retenido | ganadores perdidos | TODO 3 días ΔPnL | sin 2 mejores días | tasa disparo en vidas NO rellenas |
|---|---|---|---|---|---|---|---|---|
| BN BN_W300_X2 | **+5,85** (5) | **0,037** FALLA | (+1,30,+11,20) | +0,007 (base −0,099) | 0 | +12,66 (13 de 141), EV −0,016→+0,078 | +1,56 | 0,01 |
| KNIFE5 KN_W300_d1 (ask baja ≥1 tick en 300 ms) | +8,37 (43) | 0,240 | (−14,3,+28,2) | +0,238 | 7 (+28,05 €) | +11,95 | +0,60 | 0,63 |
| L15 L15_W300_c1 (mid 15m ≥1c en contra) | +3,80 (28) | 0,440 | (−16,5,+21,4) | −0,063 | 5 (+20,00 €) | +19,43 | +3,80 | 0,24 |
| TRADE TR_W1000 (print a nivel mejor) | −2,24 (9) | 0,777 | (−13,3,+7,1) | −0,162 | 2 | +6,61 | −2,24 | 0,18 |
| DEPTH AH_f80 (profundidad delante −80 % en 1 s) | +7,86 (42) | 0,246 | (−15,1,+27,9) | +0,188 | 7 (+27,85 €) | +20,46 | −0,35 | 0,50 |
| EDAD ED_A1 (cancelar a 1 s) | −0,15 (25) | 0,653 | (−20,0,+16,0) | −0,184 | 5 | +4,89 | −0,15 | 0,32 |
| COMBO CB_BN+DP (= AH_f80) | +7,86 (42) | 0,248 | (−12,5,+27,7) | +0,188 | 7 | +20,46 | −0,35 | 0,50 |
Las «ganancias» de KNIFE/L15/DEPTH/COMBO son sobre todo **no operar en un día perdedor**: quitan 50-77 % de los rellenos y el placebo que quita la misma
fracción al azar ya da +3/+4 € (p 0,24-0,44). BN es lo único que discrimina (quita 9 % de rellenos, 0 ganadores en TEST, hit−p de los evitados −0,23 vs −0,007), pero
con 13 rellenos: falla Bonferroni (p 0,037), el split inverso no preregistrado (test 20-21) da +6,81 p 0,132 y solo-print-exacto +10,36 p 0,058.
Las 37 configs + 3 combos (K=40) en `datos/e1c_tabla.csv` / `datos/e1c_resultados.txt`; desglose moneda × banda abajo del txt (n 14-31 por celda: sin potencia).

## Por qué no (cuantificado)
1. **Potencia**: TEST = 55 rellenos; SE placebo de ΔPnL 4,1 € (BN) a 7,2 € → MDE (Bonferroni K=7, potencia 0,8) 12,5-21,8 €, frente a efectos observados de +4-8 €/día.
   Para que el MDE de BN baje a su efecto (+5,85) hacen falta ≈(12,5/5,85)² ≈ 4,6× rellenos ≈ 5 días como el 22-Oct (≈250 rellenos de test).
2. **Latencia**: el valor de BN vive en 90-150 ms antes del print: ΔPnL con antelación exigida 90 ms +12,66 (13) → 150 ms +7,21 (8) → 250 ms +2,31 (4) → 400 ms +0,01.
   Es el hueco del taker delay (~145 ms): solo sirve si Binance→decisión→cancelación cabe en ~100 ms; con cancelación de 120 ms el efecto se reduce a la mitad.
   KNIFE5 y DEPTH, en cambio, ganan más con 150-250 ms de antelación (+21,8 / +17,6): no dependen de ms, dependen de no estar en mercados que caen.
3. **Réplica poblacional (EXTRA no preregistrado, `datos/e1c_pob.txt`)**: 25.917 rellenos de bid 0,10-0,30 ETH/SOL/XRP (1.900 mercado-lado, 479 cierres, 20-22 Oct, desenlace
   oficial `maker_ms_desenlaces_cache.json`). Con bandera BN (look 1 s) los rellenos son 4× más frecuentes (10,5 % vs 2,5 % placebo desplazado ±30-120 s: Binance SÍ dispara
   rellenos) pero NO pierden más: EV€ +0,077 con bandera vs +0,047 sin, dif IC90 por cierre (−0,27,+0,40); look 3 s igual (+0,058 vs +0,048). El efecto de B (13 rellenos) no se
   ve en la población → probable ruido o específico de la colocación de B. (Proxy: unidad = print, sin vida de orden ni cola; 22-Oct casi vacío en mk.)
4. **Base**: las 141 órdenes rellenas evaluables (de 186 con print, 215 on-chain) dan −2,37 € / 145,27 € = **−0,016 €/€** (20-Oct −0,057, 21-Oct +0,085, 22-Oct −0,099), menos
   negativa que b_cola completo (−9,00/178,88 = −0,050) y que el −0,0724 de B: la cobertura NO es aleatoria (35 rellenos sin print localizado, 7 sin pnl). En este subconjunto
   hit−p de las rellenas es −0,003: el «−18 pp» es relativo a las NO rellenas; entre rellenas hay poca separación que una cancelación pueda explotar.

## Método y supuestos (límites)
- Contrafactual SUSTRACTIVO sobre órdenes REALES de B (`DL/cola_posicion/ordenes_b.json`, 3.272; 3.195 con token en L2, 3.160 evaluables, 20-Oct 11:40Z → 22-Oct ~14:40Z),
  no el simulador: `simulador_calibrado` es NO_REPRODUCE puja a puja (κ 0,46) y no sirve para palancas de ±0,05-0,10 €/€; `analisis_maker_cancelacion_binance.py` no se usó por lo mismo
  (la base aquí es el PnL real de B, no simulado).
- Señales por RECEPCIÓN (libro5 L2 `DL/cola_vs_cruce/mk`; Binance aggTrade c[7] y 15m q c[7] de `maker_ms_*`), rejilla 10 ms, libros cruzados descartados (libro y 15m),
  cancelación +60 ms, casado = t_print − 30 ms. Solo QUITA rellenos: no modela la recolocación tras cancelar (cancelar una orden no rellenada cuesta 0) ni rebates.
- Cobertura Binance: 13 de 16 ficheros maker_ms truncados al final («unexpected end of file», PIDs reiniciados); en la vida de las órdenes el último aggTrade tiene >2 s en el
  20,5 % de los instantes de media (mediana 0, p75 22 %; mezcla de huecos y sequía real de SOL/XRP). Huecos = NO disparo (missing ≠ 0: sesga BN hacia menos cancelaciones).
- Bug cazado y corregido en la sesión: la 1ª extracción del 15m guardaba la moneda y no el token (L15 vacío); re-extraído (`x2_extrae_q15.sh`), v1 archivada `senales_v1_sinL15.csv.gz`.
- 3 días, TEST de 1 día perdedor; «sin 2 mejores días» deja 1 día.

## €/año y escala (si BN fuera real; NO validado)
+12,66 € en ≈2,1 días efectivos ≈ +6 €/día ≈ 2,2 k€/año a la escala de B (5 acc/orden, ~65 rellenos/día). Mejora +0,094 €/€ sobre el volumen relleno: para 200 k€/año harían falta
≈2,1 M€/año rellenos en la banda (≈5,8 k€/día), capacidad no medida. Coste: tasa de disparo 1 % en vidas no rellenas (casi no recoloca).

## Reproducir
`cd experimentos/5m_barato/b_perdidas_22oct/e1_cancelacion_ms/scripts && nice -n 19 ionice -c3 ./x1_extrae.sh && nice -n 19 ionice -c3 ./x2_extrae_q15.sh && nice -n 19 ionice -c3 bash run_e1c.sh && nice -n 19 ionice -c3 python3 e1c_pob.py`
(fuera de 06-09Z; RSS máx 1,8 GB senales / 0,3 GB pob, medido con /usr/bin/time -v; ~1,5 min cada uno). Manifiesto `datos/run_manifest.json` (COMPLETE), checkpoint idempotente por
mercado `DL/e1_cancelacion_ms/senales_parcial.jsonl`, log `DL/e1_cancelacion_ms/e1c_senales.log`, extracciones `DL/e1_cancelacion_ms/maker_ms_*.{x,q2}.gz`.

## Siguiente (para el chief / validador / red team)
1. Forward pasivo de BN_W300_X2 con `PREREG_E1C_FORWARD.md` sobre días nuevos de B/dry-run + réplica poblacional (necesita L2 mk de días ≥23-Oct: extraer de libro5/m5_registro antes de que rote).
2. Red team: comprobar que t_print (print L2 casado por talla) no adelanta ni retrasa el casado real >30 ms (5 de 141 con print aproximado) y que la ventaja de 90-150 ms no es un sesgo de reloj Binance vs CLOB.
3. La vía «cancelar por libro propio» (KNIFE/DEPTH/L15) no discrimina más que no operar: no seguir sin un mecanismo nuevo.

---
# E1D (24-Oct ~11:20Z) — validación poblacional de BN_W300_X2 y «cuándo operar / cuándo no»
Prereg congelado ANTES de calcular: `prereg/PREREG_E1D.md` (sha en `prereg/PREREG_E1D.sha256`). Fuente nueva: VOL/m5_registro 05-23 Oct (19 días) → `x3_extrae_registro.sh`
→ `e1d_pob.py` → `e1d_eval.py` (+ control post hoc `e1d_r1_robustez.py`). Población: **329.998 rellenos de bid 0,10-0,30, 5m ETH/SOL/XRP, desenlace oficial 100 %**
(caché maker_ms + `desenlaces_extra.json` + 251 mercados pedidos a gamma closed=true en `DL/e1_cancelacion_ms/desenlaces_e1d.json`; desviación del prereg: este
fichero local, mismo origen). 05-Oct parcial (2.118 filas malas). Σcoste medio de la banda 39.692 $/día (todas las makers); EV€ poblacional por día −0,32..+0,39.

## H1 — BN_W300_X2 en la población: **REJECTED**
Días ≠ 20-22 Oct (16 días, 17.450 mercado-lado, 4.413 cierres; 8,7 % de rellenos marcados):
- EV€ con bandera **+0,136** vs sin bandera +0,066: dif **+0,070**, IC90 por cierre (−0,041, +0,183) → los rellenos tras un salto de Binance en contra NO son peores, si acaso mejores.
- Quitar los marcados: ΔPnL −6.605 $ frente a −4.795 $ del placebo (misma fracción al azar): EXCESO **−1.810 $, p=0,81**. Días con dif<0: 8/16. ETH/SOL/XRP: +0,10/+0,07/+0,02.
- **Latencia real**: con disparo en el segundo previo (9,1 % de rellenos), lead p10/p25/p50/p75 = 150/240/460/800 ms: el **96 % llegaría a tiempo** (≥90 ms = 30 lag + 60 cancelación),
  el 91 % con 150 ms. No falla por llegar tarde: falla porque la señal no separa rellenos malos. El +12,66 € de E1C en B (13 rellenos) era ruido o propio de B.

## H2 — «cuándo operar» (regla conocida en la APERTURA de la ventana, walk-forward por día, 16 días de test 08-23 Oct, 13.815 ventanas, K=7, α=0,0143)
| Rasgo (saltar el tercil/nivel peor del entrenamiento) | ΔPnL vs operar siempre | EXCESO vs azar (p) | IC90 cierre | sin 2 mejores días | INVERSIÓN | ret€ | gate | B 20-22 Oct (base −9,00 €) |
|---|---|---|---|---|---|---|---|---|
| **R1 vol Binance 15 min previos (tercil bajo)** | **+7.780 $** | **+16.639 $ (0,0035)** | **(+4.699, +28.127)** | **+6.796** | −19.063 | 0,67 | **PASA** | **+17,85 €** |
| R2 vol 60 min | +2.539 | +15.292 (0,031) | (−3.259, +32.095) | +3.024 | −18.164 | 0,73 | FALLA (p, IC) | +4,06 |
| R3 \|deriva\| 15 min | +2.924 | +13.437 (0,053) | (+565, +27.197) | +1.075 | +10.640 | 0,67 | FALLA (p, inversión) | −3,94 |
| R4 hora (bloque 4 h) | −3.205 | +3.625 (0,33) | (−7.579, +13.952) | −3.107 | −869 | 0,85 | FALLA | −21,20 |
| R5 moneda (salta XRP) | −1.308 | +12.350 (0,099) | (+1.421, +24.096) | +3.306 | +22.188 | 0,91 | FALLA | +5,94 |
| R6 EV maker de los 6 mercados previos | −15.474 | −728 (0,54) | (−16.077, +14.894) | −8.644 | +10.447 | 0,67 | FALLA | +12,61 |
| R7 flujo (prints en banda, 6 previos) | −2.706 | +12.867 (0,10) | (−716, +26.335) | +3.679 | −2.035 | 0,85 | FALLA | +15,89 |
«Operar siempre» = 0; «azar con la misma tasa» = placebo (EXCESO 0 por construcción). R1 eligió el tercil bajo en 15/16 días; EXCESO > 0 en **13/16 días**; el 20-Oct aporta
6.799 $ (41 %), sin los 2 mejores días queda +6.796 $. Control post hoc de huecos del grabador (no prereg): excluir ventanas con >5 % de puntos Binance de más de 10 s
(5 % de ventanas) deja EXCESO +14.902 $, 12/16 días, sin 2 mejores +5.564 $ (`datos/e1d_r1_robustez.txt`). Por moneda (descriptivo, tercil propio): ETH −0,024/−0,041/**+0,209**,
SOL −0,019/+0,069/+0,101, XRP ≈0 en los tres → el efecto es ETH y SOL; dicho de otro modo, la maker barata gana sobre todo cuando Binance se mueve, y en ventanas quietas pierde.
R6 («los mercados previos fueron malos») no predice nada: el EV maker no tiene memoria de corto plazo. D-FUERTE (detector_regimen) y spread NO se probaron (fuera del prereg/tiempo).

## Veredicto E1D y €/año (sin validar: R1 es **PROMISING**, pasa un gate walk-forward de 16 días en población, pendiente de forward nuevo)
- R1 sobre la población: +7.780 $ en 16 días frente a operar siempre (≈ +486 $/día) y +1.040 $/día frente a azar, sobre ~39,7 k$/día de coste de TODAS las makers de la banda.
  Eso es un techo poblacional (≈ 177 k$/año vs siempre): solo es nuestro en proporción a nuestra cuota de rellenos, no capacidad propia.
- Escala B: +17,85 € en 183 rellenos de 20-22 Oct (179 € de coste) → B pasaría de −9,00 € a ≈ +8,85 €: ≈ +8,5 €/día ≈ **3 k€/año a la escala actual de B** (n pequeño, descriptivo).
  A 200 k€/año (≈548 €/día) con ≈0,14 €/€ de mejora harían falta ≈3,9 k€/día de coste relleno, ~65× B y ≈10 % de toda la banda (cuota no medida; no plausible solo con esta regla).
- Diferencia clave: la población de makers en la banda gana (+0,066 €/€ sin marcar) y B pierde (−0,05/−0,07): R1 recorta la peor parte de B pero el resto del hueco de B es de
  colocación/selección (dónde y cuándo puja dentro de la ventana), no del régimen.
- Forward pasivo preregistrado: `prereg/PREREG_E1D_FORWARD_R1.md` (≥10 días nuevos, ≈ 03-Nov; sin cron: lo decide el chief). BN_W300_X2: cerrada (REJECTED en población).

## Reproducir E1D
`cd experimentos/5m_barato/b_perdidas_22oct/e1_cancelacion_ms/scripts && nice -n 19 ionice -c3 ./x3_extrae_registro.sh && nice -n 19 ionice -c3 python3 e1d_desenlaces.py && nice -n 19 ionice -c3 python3 e1d_pob.py && nice -n 19 ionice -c3 python3 e1d_eval.py && nice -n 19 ionice -c3 python3 e1d_r1_robustez.py`
(~7 min de extracción, 19 días; RSS máx 0,77 / 0,31 / 1,26 GB; checkpoint por día `DL/e1_cancelacion_ms/e1d_dia_D.pkl`, log `DL/e1_cancelacion_ms/e1d.log`; resultados `datos/e1d_resultados.txt`).
Para el red team: (1) convención de relleno (SELL=bid de s; BUY=bid del opuesto) sin identidad de maker: confirmar con on-chain que no hay doble conteo en la banda;
(2) R1 mezcla monedas en un solo corte (ETH domina el tercil bajo): repetir con cortes por moneda; (3) que la vol baja no sea un proxy de horas con menos competencia (R4 no lo explica).
