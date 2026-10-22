# Resumen por experimento -- wallet dedicada 0x659a40FF9920fEBc5a66836213040924343d297F

Generado 2026-10-22T11:58:55Z por actualizar.py. Fuente: pUSD on-chain (hasta bloque 95976628) + data-api + gamma + ledgers. Cifras en pUSD (~ USD).

Saldo on-chain 21.906677 (2026-10-22T11:58:33Z); capital depositado neto 19.00; cuadre OK (dif 0.0).

## PnL por experimento (PnL realizado = mercados con desenlace oficial: payout - coste incl. comision; abiertas aparte, nunca en el realizado)

| experimento | filas | posiciones (liq.) | ganadoras/perdedoras | coste liq. | payout liq. | PnL realizado | PnL sin 2 mejores pos. | EV pond. por EUR | EUR/fila | comisiones | abiertas/pend.: coste | MTM abierto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 medir_camino_caliente (15-Oct) | 3 | 3 (3) | 3/0 | 20.41 | 21.00 | +0.59 | +0.20 | +0.029 | +0.196 | 0.0428 | 0.00 | 0.00 |
| H47-B | 182 | 171 (171) | 37/134 | 188.81 | 191.28 | +2.47 | -15.33 | +0.013 | +0.014 | 0.0000 | 0.00 | 0.00 |
| H47-A | 0 | 0 (0) | 0/0 | 0.00 | 0.00 | +0.00 | n/d | n/d | n/d | 0.0000 | 0.00 | 0.00 |

PnL realizado sin las 2 mejores posiciones = trampa 'PnL concentrado en 1-2 episodios' (CLAUDE.md raiz): una muestra de pocos aciertos baratos domina el total.

## H47-B por tanda (la tanda de cada fill sale de su hora frente a los suelo_reiniciado del ledger; el PnL de una posicion se imputa a la tanda en que se rellenó)

| tanda | inicio UTC | fin UTC | filas | pos. liq. | gan/perd | coste liq. | PnL realizado | EV pond./EUR | EUR/fila | abiertas coste | MTM |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-10-20T11:39:45Z | 2026-10-20T16:38:46Z | 5 | 5 | 1/4 | 5.92 | +0.08 | +0.014 | +0.016 | 0.00 | 0.00 |
| 2 | 2026-10-20T16:38:46Z | 2026-10-20T17:02:20Z | 4 | 4 | 2/2 | 5.00 | +5.00 | +1.000 | +1.250 | 0.00 | 0.00 |
| 3 | 2026-10-20T17:02:20Z | 2026-10-20T17:35:32Z | 5 | 4 | 0/4 | 4.45 | -4.45 | -1.000 | -0.891 | 0.00 | 0.00 |
| 4 | 2026-10-20T17:35:32Z | 2026-10-20T18:09:14Z | 12 | 10 | 3/7 | 10.65 | +9.35 | +0.878 | +0.779 | 0.00 | 0.00 |
| 5 | 2026-10-20T18:09:14Z | 2026-10-20T18:44:47Z | 8 | 8 | 1/7 | 9.62 | -4.62 | -0.480 | -0.578 | 0.00 | 0.00 |
| 6 | 2026-10-20T18:44:47Z | 2026-10-21T06:04:22Z | 6 | 6 | 1/5 | 7.35 | -2.35 | -0.320 | -0.392 | 0.00 | 0.00 |
| 7 | 2026-10-21T06:04:22Z | 2026-10-21T09:13:55Z | 25 | 25 | 7/18 | 29.08 | +18.26 | +0.628 | +0.730 | 0.00 | 0.00 |
| 8 | 2026-10-21T09:13:55Z | 2026-10-21T09:46:59Z | 5 | 4 | 0/4 | 4.83 | -4.83 | -1.000 | -0.966 | 0.00 | 0.00 |
| 9 | 2026-10-21T09:46:59Z | 2026-10-21T10:09:16Z | 8 | 7 | 1/6 | 7.34 | -2.34 | -0.319 | -0.293 | 0.00 | 0.00 |
| 10 | 2026-10-21T10:09:16Z | 2026-10-21T10:38:11Z | 12 | 9 | 2/7 | 8.78 | -2.34 | -0.266 | -0.195 | 0.00 | 0.00 |
| 11 | 2026-10-21T10:38:11Z | 2026-10-21T11:06:25Z | 4 | 4 | 0/4 | 5.00 | -5.00 | -1.000 | -1.250 | 0.00 | 0.00 |
| 12 | 2026-10-21T11:06:25Z | 2026-10-21T11:53:15Z | 10 | 10 | 4/6 | 9.95 | +6.51 | +0.655 | +0.651 | 0.00 | 0.00 |
| 13 | 2026-10-21T11:53:15Z | 2026-10-22T07:13:23Z | 13 | 13 | 4/9 | 13.40 | +2.75 | +0.205 | +0.211 | 0.00 | 0.00 |
| 14 | 2026-10-22T07:13:23Z | 2026-10-22T07:35:56Z | 7 | 7 | 2/5 | 7.57 | -0.74 | -0.098 | -0.106 | 0.00 | 0.00 |
| 15 | 2026-10-22T07:35:56Z | 2026-10-22T07:55:13Z | 6 | 6 | 3/3 | 6.80 | +8.20 | +1.206 | +1.367 | 0.00 | 0.00 |
| 16 | 2026-10-22T07:55:13Z | 2026-10-22T08:37:00Z | 13 | 12 | 2/10 | 12.72 | -2.72 | -0.214 | -0.210 | 0.00 | 0.00 |
| 17 | 2026-10-22T08:37:00Z | 2026-10-22T09:05:31Z | 4 | 4 | 0/4 | 4.70 | -4.70 | -1.000 | -1.175 | 0.00 | 0.00 |
| 18 | 2026-10-22T09:05:31Z | 2026-10-22T10:02:03Z | 9 | 9 | 1/8 | 9.69 | -4.70 | -0.485 | -0.522 | 0.00 | 0.00 |
| 19 | 2026-10-22T10:02:03Z | 2026-10-22T10:37:17Z | 5 | 4 | 0/4 | 4.59 | -4.59 | -1.000 | -0.918 | 0.00 | 0.00 |
| 20 | 2026-10-22T10:37:17Z | 2026-10-22T11:21:36Z | 10 | 10 | 3/7 | 11.45 | +5.61 | +0.490 | +0.561 | 0.00 | 0.00 |
| 21 | 2026-10-22T11:21:36Z | 2026-10-22T11:42:11Z | 7 | 6 | 0/6 | 4.98 | -4.98 | -1.000 | -0.711 | 0.00 | 0.00 |
| 22 | 2026-10-22T11:42:11Z | abierta | 4 | 4 | 0/4 | 4.92 | -4.92 | -1.000 | -1.230 | 0.00 | 0.00 |

## Cuadre

- OK  saldo_movimientos_vs_balanceOf_mismo_bloque: {"diferencia_pusd": 0.0}
- OK  identidad_efectivo_vs_suma_por_fills(PnL): {"diferencia_pusd": -0.0}
- OK  redenciones_onchain_vs_payout_ganadoras_redimidas: {"diferencia_pusd": 0.0}
- OK  importes_onchain_vs_actividad_por_tx: {"anomalias": []}
- OK  actividad_sin_transferencia_onchain: {"n": 0}
- OK  valoracion_abiertas_vs_data_api_value(informativo): {"diferencia_pusd": -0.151909}
- OK  sin_ventas_ni_otros_tipos_no_modelados: {}
- OK  fills_sin_atribuir: {"n": 0}

## Conciliacion ledger H47-B vs on-chain (acciones por mercado)

Mercados con fill: ledger 167, on-chain 171; acciones ledger 887.572391 vs on-chain 903.977794; discrepancias 4.
- eth-updown-5m-1792566300: ledger None vs on-chain 5.0
- eth-updown-5m-1792654200: ledger None vs on-chain 5.0
- sol-updown-5m-1792654200: ledger None vs on-chain 5.0
- xrp-updown-5m-1792577700: ledger None vs on-chain 1.405403

## Limites

- Atribucion a tanda por hora del fill (la actividad on-chain no lleva el oid); H47-A y F1 por ventana/tx_hash de ledger.
- Rol maker/tomador INFERIDO por la comision (maker no paga); F1 tomador por ledger.
- ninguna entrada de pUSD distinta de depositos y redenciones observada; si Polymarket paga rebates/rewards de maker fuera de esta wallet o con retraso NO es verificable aqui.
- Posiciones abiertas valoradas al curPrice de data-api (precio medio del mercado, no realizable): fuera del PnL realizado.
