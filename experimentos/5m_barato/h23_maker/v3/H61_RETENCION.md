# H61 retención (21-Oct) · EXPLORATORY · solo replay (agente alpha-researcher; texto guardado por el chief)
## Definición
- «Retención» del gate H61 (PREREGISTRO_v2.json sha f6eef406) = n_cierres con relleno en C / n en v1, misma celda. Es un recuento de rellenos, NO una fracción del EV.
- El 0,38/0,42 de v2 era estático: 1 − proporción de rellenos r0 con ret1s<0 en el relleno (A 6/16, B 11/26); no contaba cancelación, re-puja ni pérdida de cola. Sale bajo porque X=0 bp dispara con ruido: aggTrade del registro submuestreado (~2,3 trades/s, hueco p50 227 ms, 12 % >1 s; 55 % sin cambio); en 7.007 instantes de cotización 34 % ret1s<0 y 41 % =0.
## Método
Replay dinámico con la regla H23 congelada (cola base 0,5, alta 79 ms, cancelación 60 ms, 2 €, rebate 20 %, desenlace oficial). Instantes = libro ∪ aggTrades por recepción. Validación: v1 = caché v2 en 318/318 filas. Días: DISC 06-12, VAL 13-18, OOS 19-20 (BTC). Familia: X {0;0,5;1;2;3} bps × W {500;1000;3000} ms × {cancelar, solo re-puja} × re-puja {150;1500} × A/B = 120 celdas. Regla de elección fijada antes de mirar: entre las de retención ≥0,60 en DISC, la de mayor ΔPnL. Scripts en `h61/`.
## Resultados (EV ponderado = Σpnl/Σcoste; r150)
| celda | A n / ret / EV / ΔPnL | B n / ret / EV / ΔPnL |
|---|---|---|
| v1 DISC | 14 / — / +0,913 / — | 14 / — / +0,657 / — |
| H61 tal cual W1000 X0 | 7 / 0,50 / +1,513 / +1,72 | 8 / 0,57 / +1,334 / +3,66 |
| **W500 X0,5 (elegida en DISC)** | 11 / 0,79 / +1,261 / +7,41 | 13 / 0,93 / +0,960 / +7,38 |
| W1000 X1 | 12 / 0,86 / +0,934 / −1,66 | 13 / 0,93 / +0,655 / −2,04 |
- H61 tal cual NO pasa el 0,60 (0,50 A / 0,57 B). Pasan todas las de X≥0,5 y W≤1000 en r150; las de X≥1 pierden EV; la mejora sale de ~3 rellenos de los días 10-12. Cancelar y solo-re-puja dan lo mismo.
- Sin 2 mejores días en DISC: v1 +0,350 (A) / +0,215 (B); elegida +1,011 / +0,407; IC90 por días A (+0,81;+1,69), B (+0,26;+1,54) — 7 días ya vistos.
- VAL+OOS: v1 tiene 2 rellenos A y 3 B y la elegida los conserva todos (ret 1,0, ΔPnL≈0, incl. el perdedor de A del 19-Oct). **Sin validación posible.**
- Con re-puja 1500 ms (arnés actual) «sin 2 mejores» es <0 en todas: solo ayudaría con la re-puja 150 ms de v3 (no aprobada).
- Población de prints ≤ nuestra puja (BTC, ms, primer print por cierre): solo 26 cierres A y 44 B en 15 días; dirección coherente, n insuficiente.
## Cementerio / LECCIONES_B nº3
Mismo mecanismo que H26-MS y B-R1 (REJECTED). Medida materialmente distinta: BTC, ventana 0,5 s con hora de recepción en ms, lado s, señal a −60 ms del relleno; la prueba de población usaba alts, hora de bloque ±1,5 s y ventana [−10,−1,5] s, que no resuelve <1 s. Única base para reabrir; el 1/18 real de B sigue en contra. Los días 06-20 están CONTAMINADOS (el preregistro prohibía calcular EV con el corte 06-18): resultado EXPLORATORY, candidata solo para forward ≥22-Oct.
## Candidata preregistrable (congelar antes de ver forward ≥22-Oct; NO ejecutada)
```json
{"nombre":"H61b H23-CANCEL-BIN500-X05","base":"H23 v3 r150 (h23_regla_v3 3eeff503cf0a75c9), brazos A y B",
 "senal":"ret = p_aggTrade(rx<=t-60ms)/p_aggTrade(rx<=t-60ms-500ms)-1, orientado al lado s; hora de RECEPCION; sin dato o trade >5 s -> no dispara",
 "accion":"ret < -0,5 bps -> cancelar/no pujar; re-pujar con el retardo del arnes (150 ms) cuando ret >= -0,5",
 "datos_validos":">= fecha de congelacion, brazo C emparejado con v3 en los mismos cierres",
 "gate":"retencion C/v3 >= 0,60; n_cierres con relleno en C >= 15; dEV pond > 0 con IC90 por dias > 0; ademas gate H23 (n>=40, >=10 d, EV>=+0,10, IC90 d>0, sin 2 mejores>0)",
 "kill":"EV pond de C sin 2 mejores < -0,15 con n>=20",
 "pendiente":"confirmar que el feed live de aggTrade = el del registro (submuestreado); si no, la senal no es la misma (missing)"}
```
Ritmo: ~0,4 rellenos/día entre A y B (13-20 Oct): 15 rellenos en C están a más de 1 mes.
