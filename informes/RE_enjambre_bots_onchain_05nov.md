# RE enjambre de bots + ángulo on-chain (05-Nov) — INTERINO, 2 días (04-05 Nov), solo BTC 5m/15m
Autor: cheap5m-wallet-intelligence-analyst (informe pegado por el chief; pendiente validator). Scripts/resultados: `experimentos/5m_barato/re_enjambre_05nov/` (re_enjambre2.py, tb.py, re_2026-11-04/05.json).

**Datos/relojes.** On-chain `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz` (M=OrdersMatched del agresor; F con taker≠exchange = rellenos de maker; reloj `ts_est` = bloque interpolado, error <1,5 s). Libro/prints `m5_registro_D`,`m15_registro_D` por RECEPCIÓN c[7], ordenado, sin libros cruzados. Desenlace oficial `maker_ms_desenlaces_cache.json` (0 sin desenlace). Unidad = posición (wallet,token). EV ponderado por € (Σpnl/Σcoste), IC90 bootstrap por mercados (~285/día). Fee tomador 0,07·p(1−p), rebate maker 20 %. Ventas netas excluidas. Solo 2 días: sin IC por días.

## H1 Arquetipos (reglas fijadas antes de ver desenlaces; wallets ≥10 órdenes agresoras/día)
~7.900 agresores/día, mayor 3,5-4,3 % de los $. Reparto $ 05-Nov: MIXTO 47,5 %, PARES 22 %, HIBRIDO_MAKER 12 %, SNIPER_TARDIO_FAV 6,4 %, APERTURA 5,6 %, VENDEDOR 2,9 %, LONGSHOT 0,4 %, cola 3,3 %.
| Arquetipo | EV/€ 04-Nov [IC90] | 05-Nov [IC90] |
|---|---|---|
| APERTURA | −0,151 [−0,198,−0,101] | −0,089 [−0,143,−0,032] |
| VENDEDOR | +0,084 [+0,019,+0,154] | +0,082 [+0,016,+0,144] |
| PARES (n≈31-34k pos.) | −0,017 [−0,027,−0,009] | +0,005 [−0,010,+0,024] |
| BTC todos, mitad de precio | −0,052 | −0,024 |
- APERTURA: REJECTED (no se elige la contraparte). VENDEDOR: INSUFFICIENT (2 d; encaja con «salida limpia» de Q11; medir con reglas propias, sin seleccionar por wallet). PARES tomador: REJECTED.
- Concentración: 95,0 % de órdenes ≥p95 (~56 $) vienen de wallets ya vistas ese día (21.343/22.471; 22.354/23.551).

## H2 Dónde nos pisan (maker compra ≤0,20 BTC por arquetipo del agresor)
Signo cambia por día (APERTURA −52 % 05-Nov vs +100 % 04-Nov): manda la dirección del día → REJECTED como discriminador. Por franja, maker barato pierde en 8/8 celdas (−18..−59 %): selección adversa de B confirmada en toda la población.

## H3 Maker que compra favorito ≥0,80 (todos los makers on-chain)
| Franja | 04-Nov [IC90] | 05-Nov [IC90] |
|---|---|---|
| 30-120 s | +0,055 [+0,009,+0,097] | +0,088 [+0,057,+0,120] |
| 120-240 s | +0,025 [+0,007,+0,043] | +0,038 [+0,020,+0,054] |
| 240-300 s | +0,010 | +0,005 (cruza 0) |
INSUFFICIENT: 2 días; es rendimiento de la población de makers, no de nuestra cola (sin P(relleno) ni AS propios). Política propuesta NO congelada: GTC post-only sobre favorito ≥0,80, BTC 5m, t+30..t+240 s, cancelando ante salto de Binance. Refutación: EV≤0 con IC90 por días que cruce 0 en ≥10 d, o nada sin los 5 mejores cierres.

## H4 Retraso on-chain como señal
22.471/23.232 y 23.551/24.556 órdenes grandes BTC (~96 %) emparejadas con print WS por token+tamaño. `ts_est − recepción WS`: p10 1,5 s, p50 2,40-2,47 s, p90 3,2-3,3 s (supuesto log recibido 1 s tras bloque). Mid entre WS+0,3 s y llegada on-chain a favor de la orden: BTC5 +0,05/+0,17c, BTC15 +0,05/+0,14c, ETH5 +0,01/+0,08c. 30 s tras llegada: BTC15 +0,21c [−0,03,+0,44] y +0,26c [+0,01,+0,51]; BTC5 ≈0; ETH5 +0,3c (cruza 0). BTC15 PARES +0,53/+0,73c (IC90>0), APERTURA −0,36/−0,68c. Wallet vista vs nueva: sin diferencia.
REJECTED como señal tomadora (< spread+fee ~1,75c). INSUFFICIENT como inclinación de cotización maker 15m (mid, no ejecutable; ~16 celdas/día → multiplicidad).

## H5 Binance
Órdenes grandes siguen el retorno Binance de los 5 s previos: +0,26/+0,30 bps [+0,22,+0,36]. Magnitud mínima, nada explotable.

**No medido:** reposición/tamaño por nivel (L2 por wallet), 4h, monedas ≠ETH, bid15 como condición. **Riesgos:** arquetipos con comportamiento del mismo día; ts_est interpolado; rebate igual para todos; EV maker no ejecutable por nosotros.

## QA validator (06-Nov)
- H3: cifras reproducidas exactas (+0,0881, +0,0376); fuga GREEN; unidad GREEN; supervivencia GREEN; sin 5 mejores cierres +0,080/+0,034 (YELLOW, 2 días). **RED novedad:** es CARRY-FAV (F3 25-Oct: población BTC 5m ≥0,90 ≈0 en 18 d, puja propia −0,035/−0,071; fav60 −0,0575; prereg CF1 d74fae89 nunca ejecutado). Los TOMADORES en las mismas celdas también ganan (120-240 s [0,80-0,90) +0,089); sin franja temporal ALL|BTC|≥0,80 da −0,003/+0,007 → franja elegida a posteriori, 2 días de régimen, no es edge del maker.
- H1 VENDEDOR: RED, no interpretable (excluye 10,8-11,7k ventas netas, ignora rellenos maker y split/merge, clasifica con conducta del mismo día).
- Siguiente: alpha-miner corre CF1 tal cual + tb.py por día en m5_onchain 08-Oct..05-Nov (29 d), IC90 por días y sin 2 mejores días.
