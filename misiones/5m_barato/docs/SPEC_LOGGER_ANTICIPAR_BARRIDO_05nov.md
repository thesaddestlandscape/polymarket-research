# SPEC (NO lanzar; pendiente OK Javi + /code-review medium): logger de anticipación del barrido (propuesta alpha-miner), 05-Nov
Objetivo: datos para anticipar el salto/barrido ANTES de que llegue al libro 5m. Solo lectura; sin claves, sin ordenes.
## Contenido (3 salidas, un solo proceso hijo, fuera de observadores_fase0 para no tocar su cadena de imports)
1. L2 5m, lado barato (bid/ask del token con mejor precio < 0,30 de cada mercado 5m BTC/ETH/SOL/XRP en ventana viva + el siguiente): 5 niveles por lado, precio+tamano, fila SOLO si cambia el top-5; reloj de RECEPCION (ms) y el del exchange en columna aparte (trampa: timestamp WS no es hora del evento). Fuente: libro_estado_ws (WS CLOB), una conexion por moneda#marco como el lector hijo existente.
2. aggTrade perp Binance (BTC/ETH/SOL/XRP USDT-M, wss fstream): agregado en rejilla de 1 s por recepcion: n_trades, vol_compra, vol_venta (por lado agresor m), vwap, high, low, primer/ultimo precio. No se guardan ticks.
3. Liquidaciones perp (forceOrder): fila por evento (T, simbolo, lado, precio, qty, recepcion) + total por segundo en la misma rejilla de 1 s.
## Formato / retencion
CSV.gz diario en /mnt/HC_Volume_106538179/datalogs_auto/ con symlink en /root/polymarket-research-datalogs (patron maker_ms): anticipo_l2_D.csv.gz, anticipo_perp_1s_D.csv.gz; escritura append con flush por bloque + cierre atomico a medianoche; retencion 21 d (cron 03:00 que borra >21 d); en .gitignore; nunca en data/ ni en git.
## Estimacion (a verificar con 10 min de piloto antes de dejar activo)
L2: ~4 M filas/dia x ~60 B -> 250 MB crudo, ~50-70 MB gz. Perp 1 s: 4 simbolos x 86.400 x ~60 B = 21 MB crudo, ~5 MB gz. Liquidaciones: <1 MB. Total ~60-80 MB/dia gz -> 1,3-1,7 GB con 21 d. Volumen /mnt tiene 176 GB libres; / (7 GB libres, 91 %) NO se toca.
CPU/RAM: 1 proceso python, ~3-5 % de un nucleo (parseo JSON de ~80-150 msg/s) y <200 MB RAM; nice 19; sin cargas en 06-09:30Z mas alla de lo que ya hace el lector. choom no necesario (no envia).
## Guardas / pruebas obligatorias
Detectar huecos (silencio >2 s o reconexion -> fila marcador gap), libros cruzados descartados y marcados, sin NaN-si-no-hay-datos (fuga R10): rejilla con 0 explicito solo cuando el WS estuvo vivo. Test de reinicio idempotente y de cobertura por dia antes de dar valido un dia. Vigia de silencio (vigia_loggers_silenciosos) con familia sin PID.
## Uso previsto (offline, preregistrado aparte)
Predecir P(salto en 3 s | L2, flujo perp, liquidaciones) y evaluarlo contra los fills tóxicos T1 (place-gate); no se decide nada con estos datos hasta >=10 dias y IC por cierre.
