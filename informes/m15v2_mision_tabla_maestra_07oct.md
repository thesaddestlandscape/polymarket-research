# MISIÓN DEFINITIVA 15M v2 (Javi 07-Oct tarde, 66 puntos) — reglas y tabla maestra

## Reglas nuevas respecto a la v1 (informes/m15_mision_definitiva_07oct.md sigue siendo el registro de §3-35)
- **El 15M es el centro económico.** Toda hipótesis se clasifica: 15M-DIRECT · 15M-CROSS-MARKET · 15M-INFORMATIONAL ·
  15M-HEDGED · 15M-HYBRID · NOT-15M. **NOT-15M no entra en el TOP 10** (5m/1h/diario/Binance que ganan por sí solos).
- **Cada afirmación sobre Polymarket**: DOCUMENTED / OBSERVED / INFERRED / ASSUMED (minimizar ASSUMED).
- **No reabrir** B1 reactivo, FV puro, segundo movimiento (§24), Binance direccional simple, rewards maker 15M, wallets
  falsadas — salvo evidencia, mecanismo, estructura de ejecución o fuente de PnL NUEVOS (cambiar un umbral no cuenta).
- **Reducción de pérdidas ≠ alpha** (A2, cancelación). **Teórico / ejecutable / conservador**: decidir solo con los dos últimos.
- Gates de operación (§49): mecanismo, reconciliación, ≥100 oportunidades independientes, días y regímenes, OOS, sin
  mejor día, sin top 1 %, fills conservadores, latencia real, estrés +25/+50/+100 ms, sin rebates no confirmados,
  capacidad compatible. Dry-run → paper → micro-live. Observabilidad por `cycle_id`.
- Output final (§56): TOP 10 15M con 31 campos; decisión por € netos × capacidad × robustez × ejecutabilidad × riesgo.

## Hechos de infraestructura (§63)
| Hecho | Etiqueta | Fuente |
|---|---|---|
| Comisión tomador cripto 0,07·p·(1−p), maker 0 | DOCUMENTED + OBSERVED | gamma `feeSchedule` (rate 0.07, takerOnly) 07-Oct |
| Rebate maker 20 % de la comisión del tomador | DOCUMENTED (campo) / no reconciliado en dinero | `rebateRate 0.2` |
| Rewards de liquidez en 15M | OBSERVED: **no activos** (0 de 18.414 mercados con bote) | /rewards/markets/current 07-Oct |
| Taker delay en 15M | DOCUMENTED `itode: true`, 150 ms (changelog 04-Sep) | clob-markets, changelog |
| El retraso afecta a FOK aunque NO crucen | OBSERVED (contradice la doc) | GTC 69 ms vs FOK 216 ms, n=20/30 |
| GTC post-only alta 69 ms, cancel 60 ms (ida y vuelta) | OBSERVED | medir_latencia_ordenes_15m, 07-Oct |
| FOK marketable 242 ms P50 (n=4) | OBSERVED | ídem; 1 de 5 se llenó |
| Libro espejo (mint/merge) → ask_y+ask_n ≥ 1 | DOCUMENTED (matching) + OBSERVED (0 violaciones reales) | §17 |
| Origen del CLOB fuera de Helsinki (~55 ms ida y vuelta desde el borde) | OBSERVED; ubicación INFERRED (Londres/Dublín) | §5 |
| 1h resuelve con vela Binance; 15m/5m/4h con TWAP Chainlink [e−62, e−3] | OBSERVED (02-Oct) | CLAUDE.md |
| deferExec | ASSUMED nada (sin documentación) | cliente v2 |

## Tabla maestra (§37) — mecanismos agrupados (ids de informes/m15_s34_s35_mecanismos_top10_07oct.md)
| Mecanismo | Clase 15M | Estado | Evidencia | OOS | Próxima acción |
|---|---|---|---|---|---|
| Maker pasivo / dentro del spread / con muro / por cola (9,17,25-32,41) | 15M-DIRECT | REFUTADA | §8-10: markout −5,5/−6,2 c a 5 s; EV/orden −0,6/−1,0 c | VALID+FINAL+OOS | No reabrir |
| Maker EV(estado) L1+Binance+CL (43-44,67) | 15M-INFORMATIONAL | REFUTADA | §14: Ridge ≈0 por no rellenar, GBM sobreajusta | VALID/FINAL | Reabrir solo con L2 |
| Maker que cancela CL+BN / A2 (42,45) | 15M-INFORMATIONAL | REDUCCIÓN DE PÉRDIDAS (no alpha) | A3 −4,4 → −0,4 $/merc; BTC +0,72 sin n | parcial | Rastrear BTC con días nuevos (registro 14 d) |
| Maker en ambas patas / maker A + taker B (57-58,64) | 15M-DIRECT | REFUTADA (estructural) | §16: par 3-4 %, pata suelta 24 % → −1,3/−2,1 c | VALID/FINAL | No reabrir |
| Inventario de pares acuñados + venta maker con skew (59,62,139) | 15M-HYBRID | REFUTADA POR EQUIVALENCIA (INFERRED) | Con libro espejo (DOCUMENTED) vender YES del inventario al ask a = misma exposición que pujar NO a 1−a → es el maker en ambas patas de §16 (misma selección adversa ~6 c) | — | No reabrir salvo skew con información nueva (L2) |
| Profundidad L2 (19-24) | 15M-INFORMATIONAL | BLOQUEADA POR DATOS | captura desde 07-Oct 09:05Z; cerca del cierre (imb5) REFUTADA | — | Evaluar con 3-5 días |
| Tomador continuo / FV / Binance direccional / segundo movimiento (49-51,53-54,65) | 15M-DIRECT | REFUTADA | r1-r3, §24 (OOS2 −7 %) | sí | No reabrir |
| PRECIERRE TWAP 15m (75, banda alta 0,85) | 15M-DIRECT (resolución) | VIVA (dinero real) | en real; banda alta desde 06-Oct | forward | Revisar con 10 días (pt.20) |
| 15m barato frente al 4h anidado (inverso de 15m>4h) | 15M-CROSS-MARKET | REFUTADA (capacidad ≈0) | valor_relativo_anidado_v2 01-06 Oct, muestra cada 10 s: 12.067 muestras, inv_margen mediana −0,45, P99 0,00; ≥3 c solo 2 veces en 6 días. El 15m no queda rancio frente al 4h (es el más líquido) | 6 días | No reabrir |
| 15m frente al 5m (bid5 implicado − ask15, "LARGA") | 15M-CROSS-MARKET | REFUTADA | B2: LARGA −0,22 €/€ | sí | No reabrir |
| B2 pata 5m barata | **NOT-15M** | VIVA (vigía) | PRE n=3 | 08-Oct | Sigue el vigía, fuera del TOP 10 15M |
| 1h vela Binance / diario Up/Down / perps | NOT-15M | VIVA/captura | — | — | Fuera del TOP 10 15M |
| Arbitraje matemático YES+NO / mint-merge (3,137) | 15M-DIRECT | REFUTADA | §17 libro espejo | — | No reabrir |
| Pre-posición en la ventana siguiente (171-172) | 15M-DIRECT | BLOQUEADA → datos L2 incluyen la siguiente | — | — | Evaluar con L2 |
| Cotización rancia en la APERTURA del 15m (+5..+30 s, |dist_ref| ≥ P90 DISC = 4,9 bps, mid 0,40-0,60) | 15M-DIRECT (taker selectivo) | REFUTADA | m15_maestro 06/07 Oct, ask real +215 ms, 1 por mercado: DISC +0,49 (n=11) → FINAL −0,08 (n=11), OOS2 −0,001 (n=51, IC90 ±0,24); a +215 ms el ask ya es 0,58 (el libro se reprecia antes de llegar) | sí (OOS2) | No reabrir |
| Salto BTC → 15m de alts con su Binance quieto (101) | 15M-INFORMATIONAL | REFUTADA (taker y defensiva) | m15_maestro 06/07 Oct, BTC 1 s ≥ P99 DISC (1,4 bps), alt ≤ su mediana, ask real +215 ms: OOS2 n=503 resolución −0,16 (IC<0), ida y vuelta −10 %; el mid del 15m de la alt se mueve −0,9/+0,1 c en 5 s tras el salto → libros de alts NO rancios frente a BTC (tampoco sirve para cancelar: toxicidad típica ~6 c) | sí (OOS2) | No reabrir |
| Flujo on-chain limpio (85,177-178,184) | 15M-INFORMATIONAL | BLOQUEADA (retención 4 d) | — | — | Diseñar captura larga |

## Estado v2 al cierre del 07-Oct
Todo lo probable con los datos actuales en el 15M está falsado bajo estas condiciones (taker a +215 ms con fee real, maker con cola
real y latencia medida, OOS2 06-07 Oct). Mecanismos vivos 15M: **PRECIERRE** (resolución, en real) · **A3 BTC** (reducción de
pérdidas; rastrear para ver si BTC es positivo con días nuevos) · **profundidad L2** y **pre-posición en la ventana siguiente**
(bloqueados, captura desde 07-Oct 09:05Z) · **flujo on-chain limpio** (bloqueado, retención 4 d). La investigación continúa
cuando entren esos datos.
