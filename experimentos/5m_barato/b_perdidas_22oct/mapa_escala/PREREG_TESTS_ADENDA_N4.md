# ADENDA N4 a PREREG_TESTS.md (23-Oct-2026 ~10:30Z; orden de Javi): nicho de MINERIA 5m 0,00-0,10. Congelado ANTES de calcular nada de N4.
Estado: EXPLORATORY. Nada de esto es dinero ni autoriza trading. N1-N3 (PREREG_TESTS.md sha 4ec2741a...) no cambian.
## Que es
N4 = mineria forward y descriptiva de las compras maker 5m con precio de compra equivalente pc en [0,01, 0,10) (pc<0,01 se excluye igual que en s2_celdas.py), T al cierre en [60, 300) s
(bordes por np.digitize, cerrado a la izquierda, como s2_celdas), rellenos MAKER on-chain (taker != 0xe111...), unidad = compra equivalente del lado comprado (venta a q = compra del contrario a 1-q),
desenlace OFICIAL, dedup (tx, log_index), mismas formulas que s2/s4b/s5 del mapa (acc, coste, pnl = acc*gana - coste). EV = EV/EUR ponderado por EUR (sum pnl / sum coste).
**Neto de fee**: el maker no paga fee; el EV del gate es SIN rebate. El rebate maker se reporta aparte como INFERIDO: 0,014*(1-pc)*coste (no hay pago observado).
## Rejilla (fija, no se amplia ni se recorta despues de ver datos)
- Conjuntos de moneda (9): BTC, ETH, SOL, XRP, DOGE, BNB, ALT3 (ETH+SOL+XRP), ETHSOL (ETH+SOL), ALL (6).
- Buckets de pc (11): nueve de 0,01 ([0,01,0,02) ... [0,09,0,10)) + L=[0,01,0,05) + H=[0,05,0,10).
- Tramos de T (5): [60,120) [120,180) [180,240) [240,300) y TODO=[60,300).
- Lado comprado lc (3): YES, NO y AMBOS.  => 9 x 11 x 5 x 3 = 1.485 celdas (solapadas: agregados y desagregados comparten datos; no son independientes).
Una celda es TESTEABLE si en la ventana forward tiene >= 100 cierres (cierre = mercado 5m por su instante de fin, unidad de cluster) y 10 dias VALIDOS (cobertura de desenlace >= 99,5 % del coste, dia COMPLETE).
## Ventana y particiones
- FORWARD (gate): 24-Oct..02-Nov (10 dias), igual que N1-N3. Primera mitad = 24..28, segunda = 29..02 (OOS interno). Dias invalidos no se rellenan: <10 validos tras 02-Nov = INCOMPLETO.
- BACKFILL (solo DESCRIPTIVO, NO cuenta para ningun gate): 06..21-Oct y 22-Oct si queda completo; DESC = 06..13, OOS = 14.. (misma particion que el mapa). Sirve para ver que celdas habria que vigilar con mas atencion, no para decidir.
## Gate de N4 (el nicho "cruza" si AL MENOS UNA celda testeable cumple TODO)
1. EV forward >= +0,02 (ponderado por EUR, sin rebate).
2. IC90 por CIERRE (bootstrap de cierres, 1000, seed 20261024, percentil 5) > 0.
3. >= 7 de 10 dias con pnl > 0.
4. EV sin los 5 MEJORES CIERRES > 0.
5. Multiplicidad: p unilateral H0 EV<=0 por aproximacion normal con error estandar cluster-robusto por cierre (linealizacion del cociente: se = sqrt(sum_i (pnl_i - EV*coste_i)^2) / sum coste), BH sobre TODAS las celdas testeables, q < 0,10. Se reporta tambien Bonferroni (p*m).
6. Concentracion: wallet maker top-1 <= 30 % del coste de la celda; EV sin los 2 mejores DIAS > 0 (se reporta; con el resto de condiciones es requisito).
7. Coherencia de mitades: EV de ambas mitades del forward (24..28 / 29..02) > 0.
Se reportan ademas (informativos): IC90 por dias (bootstrap 2000, seed 20261023), volumen EUR/dia, n de dias, unidades, makers, EV con rebate inferido.
## Hipotesis de referencia (no gatea nada)
5m ETH/SOL 0,05-0,10: en el mapa (16 dias, descubrimiento) sale ~+0,11 con IC90 (-0,12, +0,37) y OOS negativo: NI refutado NI confirmado. En N4 es una celda mas de la rejilla (ETHSOL/H/TODO/AMBOS y desagregados) y paga la misma multiplicidad.
## Operativa
Informe diario corto en datalogs/mapa_tp1/n4_informe_ultimo.txt (top celdas por EV con n_cierres>=100 + celdas que ya incumplen/cumplen cada condicion, y la celda de referencia). Telegram SOLO si una celda cruza el gate completo (una vez por celda, latch). Fuera de eso: sin aviso.
Cualquier cambio de rejilla, umbral o ventana = version nueva con forward nuevo.
