# Q5 identidad/tamano del tomador grande ANTES del casado (05-Nov, exploratorio, 0 ordenes)
**Veredicto: NO VIABLE** como senal previa al casado con fuentes autorizadas/baratas. Una pieza residual (S_wallet como estado de dia, no de instante) queda INSUFFICIENT.

## Evidencia (onchain_fills_2026-10-29..11-05.csv.gz, script /tmp/claude-0/q5/b.py, <10 min, nice 19, ulimit 3 GB)
Unidad aqui = (tx, token); agresor = campo `taker` de las filas cuyo taker != contrato 0xe111...; "grande" = >=3 makers distintos en la tx (proxy S_orden/S_wallet). NO restringido a ETH/SOL/XRP 5m ni a cierres: es descriptivo, sin IC por cierre.
- n 5,59 M (tx,token), 1,06 M grandes. Agresores grandes: 36.504 wallets; top1 2,2 %, top5 7,0 %, top20 15,6 %. Wallets con >=10 grandes: 10.754 (93 % de los grandes). Es un enjambre de bots, no unas pocas ballenas: no hay una identidad a vigilar.
- Recurrencia: 86-94 % de los grandes de cada dia vienen de wallets ya vistas grandes en dias previos (nprev 12.5k-34.8k). Sesgo: el conjunto "previo" crece y se define por ser grande; el contraste con no-grandes (47-50 %, solo dias 11-03..05) es tautologico. Saber QUIEN es no dice CUANDO.
- Precursor intra-mercado (S_wallet): agresor con fill previo >=1 s antes en el mismo token: grandes 41,2 % (n 1.061.101) frente a no-grandes 71,1 % (n 4.524.631). El grande NO anuncia huella previa; es incluso al reves (inversion). Sin mejora sobre geometria T/L/bid-L (Q11).

## Fuentes
- Mempool/pending Polygon: estructural NO. El casado lo decide el matcher off-chain de Polymarket; la tx solo se publica DESPUES (bloque ~2,4 s tras el casado, trampas CLAUDE.md). Un pending visible es posterior al casado y a la actualizacion del libro (<0,3 s). No se ha consultado nodo (polygon_rpc.py no expone mempool; no se ha medido, es argumento, no resultado).
- Orden en cola CLOB/WS (S_orden): el libro WS muestra ordenes de reposo; la orden agresora nunca reposa, solo aparece como print tras el casado. Identidad no existe en el WS publico.
- Saltos de Binance: ya cerrado en Q11 (precursores Binance/Chainlink p_max>=0,11 a tf-300 ms) y en trampas (ask se mueve +2/3,6c en <300 ms).
- Hash de orden/EIP-712 solo existe tras firmar; no hay canal publico previo.

## Limites
Datos 10-29..11-05 ya usados como evidencia en Q11; esto no es confirmatorio. Sin mapeo a cierres 5m ni a escalera G.

## Siguiente paso minimo (unico)
No invertir mas en identidad/mempool. Si se quiere cerrar el cabo S_wallet: cruzar `A_all.pkl` (barrido_corr) con la lista de wallets agresoras por cierre y comprobar si la racha intra-dia (n fills previos del mismo agresor en el mismo cierre, <=tf-300 ms) mejora el AUC de PG_O50; criterio de refutacion: delta AUC OOS <0,02 frente a placebo. Esperado nulo por la inversion de arriba.
