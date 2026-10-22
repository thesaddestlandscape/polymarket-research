# INFORME contabilidad wallet dedicada (0x659a40FF...) -- generado 2026-10-22T11:58:55Z

Saldo on-chain 21.9067 pUSD (bloque 95976628, 2026-10-22T11:58:33Z); depositado neto 19.00; saldo - capital = +2.91.
PnL realizado total +3.06 (n=185 filas, 174 posiciones); no realizado MTM +0.00; ganadoras por redimir 0.15; comisiones 0.0428.
Por experimento: F1 medir_camino_caliente (15-Oct): PnL realizado +0.59 (filas 3, EV pond. +0.029/EUR) | H47-A: PnL realizado +0.00 (filas 0, EV pond. n/d/EUR) | H47-B: PnL realizado +2.47 (filas 182, EV pond. +0.013/EUR). Tandas B en resumen_por_experimento.md.
CUADRE: CIERRA (dif 0.0 pUSD; sin motivo pendiente). Detalle en estado_dashboard.json::cuadre.comprobaciones.
Fuente/cobertura: pUSD Transfer (eth_getLogs, completo_desde_bloque_0, bloque 0..95976628, 225 movimientos) + data-api /activity (224 filas) + gamma (desenlaces 174/174).
Conciliacion ledger H47-B vs on-chain: 887.572391 vs 903.977794 acciones, 4 discrepancias. No atribuido: 0 fills.
Sin sesgo de supervivencia: cada fill se resuelve con desenlace oficial (gamma); sin desenlace = abierta/pendiente (aparte, valorada a curPrice).
Rewards/rebates: ninguna entrada distinta de deposito/redencion; no verificable si se pagan fuera o con retraso.

Reproducir: `nice -n 19 ionice -c3 ulimit -v 2500000; python3 experimentos/5m_barato/contabilidad_wallet_dedicada/actualizar.py` (idempotente; `--sin-red` recompone de la cache estado/).

## Esquema estado_dashboard.json (schema_version 1, escritura atomica tmp+rename)
- saldo{pusd_onchain,bloque,ts_utc,suma_movimientos}; capital{depositos,retiradas,depositado_neto}
- pnl{realizado_total,no_realizado_mtm,total_efectivo_mas_posiciones,saldo_menos_capital_neto,ganadoras_por_redimir_pusd,comisiones_pagadas,n_filas_fill,n_posiciones,euro_por_fila_liquidada,euro_por_posicion_liquidada,ev_ponderado_por_euro}
- por_experimento[] y tandas_B[]: n_filas,n_posiciones,n_posiciones_liquidadas,ganadoras_posiciones,perdedoras_posiciones,acciones,coste_total,coste_liquidado,payout_liquidado,pnl_realizado,comisiones,coste_abierto_pendiente,valor_mtm_abierto,pnl_no_realizado_mtm,ev_ponderado_por_euro,euro_por_fila,euro_por_posicion (+experimento | tanda,inicio_utc,fin_utc)
- posiciones_abiertas{n_filas,coste,valor_mtm,valor_data_api_value,detalle[]}; cuadre{ok,diferencia_pusd,motivo,tolerancia_pusd,comprobaciones[]}
- cobertura{onchain,actividad_data_api,desenlaces_gamma,rewards_y_rebates,conciliacion_ledger_B}; ultimos_movimientos[50]; serie_diaria[{fecha,saldo_cierre_pusd,depositos_acum,pnl_liquidado_dia,pnl_liquidado_acum,n_movimientos}]; no_atribuido{}
- Valores desconocidos = null (nunca 0). Campos nuevos solo se anaden; un cambio incompatible sube schema_version.
