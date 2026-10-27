# Frente 3 - F5 de A1: ¿moneda, hora/día, o sobrevive a ambos? (27-Oct-2026)
Script `f5_desagrega.py` (reutiliza `mitigar_as_25oct/scripts/a1_rasgos.py` -> `DL/mitigar_as_25oct/r_DIA.pkl`; prints REALES de la población, q real de m5_registro, desenlace oficial; sin etiqueta generativa). Salida `f5_resultados.json`, `f5_stdout.txt`. Mismo walk-forward del PREREG_A1: test 09-23 Oct (15 días, n=254.984 prints, 585 k$ coste, EV€ población +0,055), terciles y tercil marcado elegidos con el train. Franjas UTC de 6 h. POST HOC / exploratorio (no preregistrado).
Reproducción: pooled = +11.445 $, IC90 días (411,1115)/día, 13/15, sin 2 mejores +7.800, **sin 3 mejores +6.260** (cuadra con A1).

| Variante (exceso 15 d, placebo sustractivo de misma fracción de €) | exceso $ | IC90 días (por día) | días + | sin 2 mejores | sin 3 | EV€ marcados / retenidos | inversión |
|---|---|---|---|---|---|---|---|
| Pooled (A1) | +11.445 | (411,1115) | 13/15 | +7.800 | +6.260 | -0,016 / +0,085 | -9.701 |
| Umbral por moneda, placebo por moneda | +13.811 | (657,1184) | 13/15 | +10.422 | +8.896 | -0,038 / +0,089 | -5.305 |
| **Umbral y placebo dentro de moneda x franja** (quita composición moneda/hora) | **+10.309** | **(464,911)** | **14/15** | **+7.499** | **+6.463** | -0,009 / +0,080 | -6.661 |
| Permutación (F5 barajado dentro de moneda x franja x día, 100 perm.) | real 10.309 vs perm. media -33, sd 2.800, p95 3.862 | | | | | | p=0,0099 (mín. alcanzable con 100 perm.) |

Por moneda (regla pooled): ETH +8.391 (13/15, coste 399 k$ = 68 % del coste), SOL +2.756 (12/15, IC>0), XRP +298 (cruza 0). Con umbral por moneda: ETH +9.457, SOL +3.711 (IC>0), XRP +642 (cruza 0). **Sin ETH: +3.270, IC90 (70,366), 10/15 días, sin 2 mejores +1.920.** El "99 % ETH" no se sostiene en este corte: ETH ≈ 68-73 % del exceso, proporcional a su 68 % del coste; SOL aporta ~24-27 %.
Por franja UTC (regla pooled): 18-24 h +5.259 (14/15, IC>0, sin 3 mejores +3.027), 00-06 +2.454, 06-12 +1.630, 12-18 +2.101 (IC cruzan 0). Por hora, solo 2, 18, 20, 21 h tienen IC90>0; varias horas ~0 o negativas (0, 8, 10 h) -> el efecto se concentra en la tarde-noche pero no desaparece al neutralizar franja. Celdas moneda x franja (12): IC90>0 en 4 (ETH 12-18 y 18-24, SOL 00-06 y 18-24); sin corrección por multiplicidad -> solo descriptivas.
Subconjuntos (regla moneda x franja): rellenos AL mejor bid +5.240 (IC>0, 11/15); **POR DEBAJO del mejor bid (tipo B) +3.242, IC90 (3,429), 9/15, sin 2 mejores +1.025** (EV€ marcados +0,125 vs retenidos +0,192; límite). Latencia τ=250 ms (A1 pooled: cruzaba 0): aquí +5.544, IC>0, 12/15, pero EV€ marcados +0,044 vs +0,060 retenidos: efecto pequeño.

## Veredicto
El efecto F5 **no lo explican la moneda ni la franja/día**: sobrevive a neutralizar ambas (-10 % respecto al pooled), 14/15 días, sin 3 mejores días +6.463, inversión negativa, y la permutación intra-celda da p≈0,01. Pero A1 sigue siendo población (prints, no cola propia), el efecto es 68-73 % ETH por peso de coste, se concentra 18-24 h, el tipo B (bajo el mejor bid) es marginal (IC90 inferior +3 $/día) y vive en los últimos 100-250 ms (recotización de makers más rápidos). Como ganancia para B: sin demostrar (€/año validado 0). Límites: unidad = print, placebo sustractivo/permutación sin modelar cola; 15 días de test, una sola ventana (06-23 Oct); forward M2 (PREREG_FWD) es el árbitro.
