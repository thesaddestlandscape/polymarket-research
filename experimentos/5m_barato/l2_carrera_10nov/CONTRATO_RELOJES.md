# CONTRATO DE RELOJES (programa L2 V2, 11-Nov-2026) -- borrador, no congelado
Mandato de Javi: los relojes NO se mezclan; cada uno separado, con sus usos, calibrado, y la diferencia exchange->recepcion se mide como ventaja o riesgo, no como ruido.
Este documento NO modifica PREREG_L2_V2 ni ADDENDUM_A1 (congelados). Es la base de NOTA_A2_RELOJES.md. Las cifras medidas van en NOTA_A2 y en out_v2/*.json (fuente), no aqui.

## 1. Los tres dominios de tiempo
| Dominio | Sufijo | Que es | Para que SI sirve | Para que NO sirve |
|---|---|---|---|---|
| EXCHANGE | `_ex` | Sello que pone el servidor del CLOB/Binance al evento (`timestamp` del WS, `t_ev`, `T`/`E` de Binance, `ts_ex_ms` del canal de usuario, hora de bloque on-chain) | Cuando OCURRIO el evento en el exchange: orden fisico de eventos (cola por delante, barridos, relleno vs llegada de NUESTRA orden), ventana W real del edge, antiguedad real de un precio | Decidir: no es lo que sabiamos. Si una regla usa un precio con `_ex <= t` como si lo conociesemos en `t` mira ~15-60 ms al futuro (peor en rafagas) |
| RECEPCION | `_rx` | Hora de NUESTRO reloj (UTC, chrony 0,2 ms de offset medido 11-Nov) a la que llego el mensaje al proceso (`_T_RECV` en `libro_estado_ws`, `recv` en libro5_tx/b40, ticks Binance `recv`) | TODA simulacion de decision causal: features, disparos de cancelacion, gates, lo que podiamos saber y cuando | Fechar cuando ocurrio algo en el exchange (lo retrasa lag = rx-ex, y en lotes mucho mas) |
| LOCAL-PROPIO | `_loc` | Horas de NUESTRAS ordenes en nuestro reloj: `t_envio_ms`, `t_ack_ms`, `t_pre_ms`, `t_resp_ms`, `t_call0`, `t_ret`, `t_dec` de la rejilla | Definir cuando decidimos/enviamos; mismo dominio que RX (misma maquina, mismo reloj) | Compararlo directamente con un `_ex` sin etiquetar la suposicion `reloj local = UTC = reloj exchange` |

Conversiones permitidas (siempre explicitas y etiquetadas en el nombre de la funcion/columna):
- `rx -> ex`: NO existe como transformacion; se estima por evento si hay pareja (misma fila q/t trae ambos) o se declara la constante calibrada (`DELTA_RX_EX_P50`, `_P90`) y se etiqueta `_est`.
- `loc(envio) -> ex(llegada)`: `t_arr_ex = t_envio_loc + subida`, con `subida` DESCONOCIDA salvo por anclas (ver NOTA_A2). El motor (engine.LAT_POST = 68 ms = RTT completo del POST) usa el valor conservador `t_arr = t_dec + 68` comparado con sellos EX: supuesto declarado, no medido.
- Nunca: restar un `_ex` de un `_rx` o `_loc` sin que el resultado se llame `lag_...`/`..._rx_menos_ex` y se interprete como lag (red + offset + lote), no como duracion de un proceso.

## 2. Campo de cada logger -> dominio
| Fuente | Fila / campo | Dominio | Nota |
|---|---|---|---|
| maker_ms (`libro_estado_ws`, registro ms) | `q,t_ev,tok,bid,ask,szb,sza,recv` | col 2 = EX, col 8 (`c5`) = RX | cambio del top del libro; v1 (`ms_extract.py`, `sa_ms/ms_D.npz`) guardaba SOLO col 2 (`q_t` = EX) |
| | `t,t_ev,tok,price,side,size,recv,` | col 2 = EX, col 7 (`c4`) = RX | trade WS |
| | `l,t_ev,tok,niveles ask 1-3,recv` / `L,...,recv` | col 2 = EX, ultima = RX | ask nivel 1-3 / ask completo, solo ultimos 305 s del 5m |
| | `x,T,sym,px,qty,m,E,recv` | T, E = EX (Binance), col 8 = RX | aggTrade Binance. `q11/barrido_multi/bfeat.py` y passT usan `recv` = RX (correcto) |
| | `b,t,sym,bid,ask,bq,aq,` | sin RX | bookTicker muestreado (no es tick a tick): no usar para ms |
| | `h,...` | EX sin RX | historico 100 ms del libro |
| libro5_ms / libro5_b40 | `d,t_ms,tok,side,p,s,rx,seq`; `B`; `G`; `T` | col 2 = EX, col 7 = RX, `seq` = orden de escritura | `l2_triggers.py` ordena por (rx, seq): correcto para decision |
| libro5_tx | `t_ev,token,tx,recv` | col 1 = EX del casado, col 4 = RX (reparacion 02-Nov) | `tx_ws` toma `recv` -> la cinta chain (`tape_D.pkl::t_ws_ms`) es RX; con `src='bloque'` (sin tx_ws) es hora de bloque + offset (otro reloj: cadena) |
| cinta passT (`RT_`/`SEGT_`) | `tf`, `tm` | MEZCLA (v1): caida L1 en `D.qt` (EX) o `t_print_rx - 63` (RX con constante) | arreglado en `passT_v2.py` (modos `legacy`/`causal`/`rx`) |
| ordenes propias Sonda1 (`cancel_evid_*.jsonl`) | `alta.t_envio_ms/t_ack_ms`, `cancel_try.t_pre_ms/t_resp_ms` | LOC | |
| | `user_order/user_trade.ts_ex_ms` | EX (canal de usuario) | |
| | `user_order.t_recv_ms` | RX (canal de usuario) | |
| B real (`experimento_h47_B_ledger.jsonl`) | `post_lat.t_call0/t_ret` (s epoch), `visto.t` | LOC (`visto` = RX del WS propio del ejecutor) | `ts` ISO = reloj local al escribir el ledger |
| passT / engine | `g` (rejilla), `t_dec`, `t_arr = t_dec + 68`, `t_end` | LOC | `t_end` cancelacion en `g_j + 60` = LOC |

## 3. Reglas (cada funcion nueva las cumple o no entra)
R1. Todo timestamp lleva sufijo `_ex`, `_rx` o `_loc` (o su columna lo declara). Sin sufijo = defecto, no se mezcla.
R2. Las FEATURES DE DECISION (bid/ask a `t`, b15, vol30, gate, saltos Binance, disparos de cancelacion por libro) se leen en RX: el ultimo mensaje con `rx <= t`.
R3. La MECANICA DE RELLENO (libro vigente en la llegada, cola por delante, cancelaciones de terceros que la consumen, prints que atraviesan el nivel, `tf`) se mide en EX: es lo que paso en el exchange. Se compara con `t_arr = t_dec_loc + subida` bajo el supuesto etiquetado `loc == ex` (chrony 0,2 ms; offset del exchange desconocido: acotado por anclas).
R4. `tf` es SIEMPRE EX (instante fisico del relleno). Quien necesite "cuando lo supimos" usa `tf_rxb` (RX de la caida L1 que lo evidencia) o `tf_rxp` (RX del print); ambos se guardan en `RT_<modo>`.
R5. Una ventana/medida del tipo "la reduccion de L precede al print en X ms" es X en UN reloj; se calcula con los dos campos del MISMO mensaje o del MISMO dominio, nunca `sa_ms.q_t` (v1, EX) contra `tape.t_ws_ms` (RX).
R6. Ordenar eventos de dos fuentes por sello EX es valido solo si ambas traen sello EX (caida L1 vs print `t_ev` de libro5_tx). Ordenar por RX es valido para "orden de llegada". Mezclar = invalido.
R7. Lote: el sello EX de un mensaje puede ser anterior al instante real del evento (sello de lote). El suelo de red (p5 de `rx-ex` por hora/tipo) es el desfase estable; el exceso sobre el suelo por encima de ~100 ms se trata como RAFAGA/LOTE y no como latencia de red ni como ventaja.
R8. Un informe de resultados declara el modo de reloj (`legacy` = v1, `causal`, `rx`) y el fichero de origen. `legacy` solo para regresion.

## 4. Implementacion (esta ronda)
- `ms_extract_v2.py` -> `datalogs/sa_ms2/ms2_D.npz` con `q_t_ex`, `q_t_rx`, `t_t_ex`, `t_t_rx` (sin pisar `sa_ms/`), manifest por dia.
- `relojes.py::Day2(d, clock)` vistas `ex` / `rx` con `qt_otro` alineado; `engine_clock.py::DayEngClock(modo)`.
- `passT_v2.py MODO DIA`; `prep_fills_v2.py`, `l2_triggers_v2.py`, `paso0_lib_v2.py` (assert real + conteo de rellenos sin segmento + `x1_dia(clock, fuente)`).
- `calib_relojes.py`, `anclas_relojes.py`, `condicion1.py`, `regresion_extractor.py`, `test_relojes.py`.
- NO se editan: PREREG_L2_V2, ADDENDUM_A1, l2eval.py, paso0_lib.py, paso0_run.py, passT_copia/passT.py, ms_extract.py, dev, main live, crons, procesos.
