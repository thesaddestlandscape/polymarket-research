# Anatomía de las pérdidas de B (H47-B real), 22-Oct-2026. Estado: EXPLORATORY
Solo lectura. No toca B (`experimento_maker_h47.py` sha c82f5dc5f304b8a6), ni procesos, ni crons, ni config.
**Datos.** `contabilidad_wallet_dedicada/posiciones.csv`: 175 posiciones con `tanda_B` (PnL on-chain), rellenos del 20-Oct 11:40Z al 22-Oct 12:11Z, tandas 1-23, ETH/SOL/XRP.
Rasgos sacados de `datalogs/experimento_h47_B_ledger.jsonl` (puja_post, puja_fin, mercado_fin), Chainlink RTDS `data/prices/chainlink_D.csv` (solo `source=chainlink`, hora de recepción para los rasgos previos al relleno), twap60 oficial (`polybolt_D.csv`) y Binance bookTicker (`datalogs/binance_bookticker_D.csv`: había 1 fila con bytes nulos y se descartó).
Ganador según twap60: coincide con on-chain en 175/175.
Las 275 pujas del ledger (166 rellenas y 109 no rellenas, con desenlace gamma al 100 %) sirven de contrafactual.
**Cómo reproducirlo:** `build.py`, después `analiza.py`, `extra.py` y `reglas.py`, más el bloque de `racimo.txt` (salidas `*.txt` en este directorio).
**Métrica.** EV = Σpnl/Σcoste. El IC90 es bootstrap por CIERRE: las posiciones del mismo cierre son una sola apuesta (correlación intra-cierre 0,20).
Solo hay 3 días, así que no se puede calcular un IC por días y el reparto se da día a día.

## 0. Situación
- **Total.** n=175, 37 ganadas (21,1 %). El precio medio es 0,209, que es justo el acierto de equilibrio.
  - EV −0,012, IC90 (−0,28, +0,29), PnL −2,32 €.
  - Sin las 2 mejores posiciones: −0,105. Sin las 5 mejores: −0,217.
  - Por día: +0,07 (20-Oct), +0,17 (21-Oct), −0,25 (22-Oct, −18,3 €).
- **Curva.** Pico de +28,3 € en la posición 55 y caída hasta −2,3 € (drawdown −30,6 €).
  - La peor racha es de 18 pérdidas seguidas. Con rellenos independientes al 21 % lo esperable es p50 16 y p90 24: es azar.
- **Integridad (hallazgo).** 9 de las 175 posiciones on-chain NO tienen `puja_fin` en el ledger.
  - Son 10,2 € de coste, 1/9 ganadas y −5,18 € (EV −0,51).
  - Son rellenos posteriores a `tick_cambiado`, `mercado_ya_operado_no_reentra` o una parada.
  - `b_postmortem.py` (que lee el ledger) los EXCLUYE, así que su EV sale optimista. Hay que medir siempre sobre on-chain.

## 1. Patrones de pérdida, de más a menos sólido
1. **Selección adversa en el relleno (el más sólido).**
   - Las pujas rellenas aciertan 36/166 = 21,7 % y las no rellenas 41/109 = 37,6 %, con el mismo precio al pujar (0,246 frente a 0,245). Fisher p=0,006; la diferencia tiene IC90 por cierre (+0,06, +0,26).
   - Por moneda: ETH 21 % frente a 53 % (p=0,004); SOL 24 % frente a 37 %; XRP 20 % frente a 27 %.
   - En el último tercio la brecha es 10 % frente a 34 % (p=0,008), pero el «empeora con el tiempo» NO es significativo (interacción p=0,36).
   - Es el mecanismo ya medido en `b_seleccion_adversa` (0,24-0,26 por € en población y simulador).
2. **Las pérdidas son barridos que se ven DESPUÉS del relleno (descriptivo, no accionable antes).**
   - Binance ≥3 bps en contra en los 30 s posteriores: 0/44 ganan, −50,5 €.
   - Chainlink ≥3 bps en contra a 30 s: 1/49, −50,0 €.
   - Markout a 5 s ≤ −0,2: 4/48, −36,8 €.
   - Cada uno de esos cubos ya pierde más que la pérdida neta total. Antes del relleno no hay ningún rasgo que los separe (punto 3).
3. **Racimo: varias monedas del mismo lado en el mismo cierre.**
   - 56 de los 94 cierres tienen 2 o más posiciones (137 posiciones en total) y en 50 de ellos todas son del mismo lado. 34 cierres lo pierden todo.
   - El 2.º/3.er relleno del mismo cierre y lado: EV −0,139 (n=75). El primero: +0,076 (n=100).
   - Se repite los 3 días, pero el IC90 por cierre de la diferencia es (−0,70, +0,31): EXPLORATORY.
   - El 2.º relleno llega una mediana de 25 s después del primero (p25 4 s; solo 7 de 75 en menos de 0,2 s), así que un cancelado de 65 ms llegaría a tiempo.
4. **El 22-Oct es régimen y azar, no un deterioro estructural demostrado.**
   - Acierto 16,7 % frente a precio 21,1 %: P(≤ observado)=0,24. Desde las 10:00Z: 3/28, P=0,14.
   - Fue un día bajista: Up ganó el 45,4 % de 522 mercados 5m ETH/SOL/XRP, y B compró Up en 47/66 posiciones (el lado barato va contra la tendencia), con un acierto del 12,8 %.
   - Up −0,21 frente a Down +0,26: p familiar 1,0.
   - Las tandas en −1,00 salen así por construcción: una tanda se corta al perder 5 $. No sirven para medir tendencia; la tendencia se mide por orden cronológico.
5. **Celdas que parecen claras pero no sobreviven a la multiplicidad** (56 celdas previas al relleno con n≥15; max-estadístico con permutación dentro del día):

   | Celda | n | EV | IC90 por cierre | Por día | p marginal | p familiar |
   |---|---|---|---|---|---|---|
   | Hora 08-11 UTC | 87 | −0,35 | (−0,67, +0,01) | +0,68 / −0,29 / −0,47 | 0,03 | 0,97 |
   | Precio 0,25-0,30 | 59 | −0,43 | (−0,70, −0,14) | 3/3 días negativos | 0,14 | 0,97 |
   | Spread al pujar >0,02 | 56 | −0,50 | — | — | — | ≥0,98 |

   - Hay 5 celdas con p<0,05 frente a 2,6 esperadas por azar (p95 6): es compatible con ruido.

## 2. Vetos candidatos: cuánto se habría evitado y cuánto ganador se perdía (IN-SAMPLE, 175 posiciones, €)
| Veto (solo para revisión) | Vetadas | Pérdidas evitadas | Ganancias perdidas | NETO | Neto por día (20/21/22) |
|---|---|---|---|---|---|
| V3 spread al pujar >0,02 | 56 (32 %) | +55,7 | −24,7 (7 ganadoras) | **+31,1** | −2,9 / +21,8 / +12,2 |
| V9 solo el 1.er relleno por cierre y lado (cancelar el mismo lado en las demás monedas) | 75 | +65,9 | −54,9 (13) | **+11,0** | +5,3 / +1,7 / +4,0 |
| V1 hora 08-11 UTC | 87 (50 %) | +80,2 | −47,6 (13) | +32,6 | −2,4 / +11,3 / +23,8 |
| V2 precio ≥0,25 | 59 (34 %) | +63,7 | −31,1 (10) | +32,6 | +3,4 / +6,7 / +22,5 |
| V4 sin XRP | 50 | +42,5 | −39,0 (10) | +3,6 | −1,2 / +0,6 / +4,2 |
| V6 sin Up | 101 | +92,4 | −68,8 (18) | +23,6 | +3,4 / −4,1 / +24,4 |

**Descuento honesto:**
- **Walk-forward.** Elegí las 5 peores celdas con el 20-21 Oct y las medí en el 22-Oct.
  - Evitan +5,47 € de media, frente a +5,87 € de 5 celdas al azar (P=0,52): **elegir celdas no tiene habilidad**. En un día perdedor cualquier veto «ahorra».
- **Spread.** Era la hipótesis declarada con 209 pujas (corte 22-Oct 08:57Z) y en el forward falló: la parte «buena» (spread ≤0,02) dio −0,33 (n=25).
  - El veto >0,02 siguió siendo peor (−0,69, n=13 <15), pero en población y en el simulador con libro real el spread «sin efecto robusto» (`b_seleccion_adversa/INFORME.md` §C).
- **Lo más defendible para revisar:**
  - **V9:** tiene un mecanismo a priori (barrido correlado entre monedas), sale positivo 3/3 días y es accionable con cancelación. IC cruza 0, post-hoc.
  - **V3:** en B real va en la misma dirección en descubrimiento y forward, pero contradice a la población.
  - Siguiente paso mínimo: contrastar ambos en el simulador con libro real (`b_seleccion_adversa/datos/simv2`, 17-21 Oct) y en la población, preregistrarlos y seguirlos en forward shadow emparejado. Nada se aplica a B antes de N=500.

## 3. Qué NO se sostiene
- **«XRP es el que pierde».** XRP −0,068 frente a ETH/SOL +0,009, p familiar 1,0; el veto XRP neto es +3,6 €. Lo decide H62 con su preregistro.
- **Cortar pérdidas vendiendo tras un movimiento de Binance en contra.**
  - In-sample suma +9,6/+11 € con Binance ≤ −3 bps a 30 s (n=34, 0 ganadoras vendidas).
  - Pero la venta al bid (11,1 €) vale menos que el valor al mid (13,6 €): la ganancia sale de que no apareció ninguna de las ~2,7 ganadoras esperadas.
  - H40 ya la rechazó 36/36 con n grande. Salir no recupera nada.
- **Sin efecto monótono ni robusto:** tiempo restante o tiempo desde la apertura (en 5m son la misma variable), tamaño, número de repegas, distancia a la referencia, volatilidad 60 s, FV Φ(z) sin calibrar (no monótono), Binance o BTC en los 30 s previos, tendencia 15/60 min, cola.
- **Rasgos de cola, espera y tras_cancel:** son posteriores al relleno, solo descriptivos.
- **La «tendencia de tandas»** (Spearman −0,36) es un artefacto de la regla de parada de 5 $.
