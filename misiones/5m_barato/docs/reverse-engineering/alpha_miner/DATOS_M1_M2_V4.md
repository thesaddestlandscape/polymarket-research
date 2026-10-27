# DATOS M1 / M2 / V4 - cobertura de entradas (solo lectura, 26-Oct-2026 ~10:10Z)
Autor: especialista de datos. No se ha calculado ningun EV. Preregs: `sha256sum -c PREREG_M1_CONTRA_PERDEDORA.sha256 PREREG_M2_COLCHON_PARIDAD.sha256` -> OK ambos (26-Oct 09:50Z). Hashes de scripts vs preregs: f24 `bb15385e171f5362`, f25 `fb16d8512e85a2cd`, a3 `f3c20057ade669e2` coinciden; a4 = `295f1b030644cf57`; `f20_carga.py` = `a0bc03b189dcf2a1`.
Convencion: los ficheros `m5_onchain_D` son por DIA DE FILL (UTC). Un "dia de cierre" D usa fills de D-1 (ultimos minutos) y D. El dia de cierre 26 NO es evaluable hasta que exista `m5_onchain_2026-10-26` (cron 04:10Z del 27-Oct) y `m5_onchain_2026-10-27` para su cola.

## 1. Existencia e integridad de `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz`
Comprobado en streaming (awk) sobre bloque y ts_est; columnas `tipo,bloque,ts_est,tx,log_index,order_hash,maker,taker,side,token_id,maker_amt,taker_amt,fee`; tipo F = OrderFilled, M = OrdersMatched.
| D | filas (F/M) | primer..ultimo ts_est | bloques | continuidad con el dia previo | salto maximo entre bloques con filas |
|---|---|---|---|---|---|
| 22-Oct | 1.954.490 (1.434.307 / 520.183) | 00:00:00 .. 23:59:58 | 95947888..96005485 | contiguo al 21 (95947887 -> 95947888) | **238 bloques** (bloques 95960038->95960276, ts 05:03:45..05:09:42Z) |
| 23-Oct | 2.179.926 (1.582.593 / 597.333) | 00:00:00 .. 23:59:58 | 96005486..96063085 | contiguo | 14 |
| 24-Oct | 1.888.493 (1.412.225 / 476.268) | 00:00:00 .. 23:59:58 | 96063086..96120685 | contiguo | 10 |
| 25-Oct | 1.824.747 (1.363.742 / 461.005) | 00:00:00 .. 23:59:58 | 96120686..96178285 | contiguo | 12 |
| 26-Oct | NO existe (dia en curso; la extraccion corre a las 04:10Z del 27-Oct) | - | - | - | - |
- Cada fichero cubre exactamente 57.600 bloques (24 h a ~1,5 s/bloque; se mide mediana 1,5 s) = COMPLETO en bordes. 21-Oct (referencia): 95890288..95947887.
- **Hueco real del 22-Oct 05:03:45-05:09:42Z (238 bloques)**: el mismo hueco esta en la FUENTE cruda `datalogs/onchain_fills_2026-10-22.csv.gz` (0 filas entre esos bloques; 769 filas en los bordes) y tambien en `m15_onchain_2026-10-22` (salto 239). Es un hueco de captura (no del extractor; la re-extraccion del 24-Oct dio +6 filas, lo confirma). No recuperable de los ficheros locales; solo re-leyendo Polygon via `polygon_rpc.py` (no hecho, decision del chief). Afecta a unos 1,2 mercados 5m por moneda; para M1 el 22-Oct queda con un agujero de ~6 min (declararlo o excluir esas ventanas); M2 empieza el 24 (no afectado).
- Otro aviso: el manifest `mapa_infra/runs/extract_2026-10-22.json` figura PARTIAL por un maker_ms crudo corrupto (`maker_ms_2026-10-22_986560`); la rejilla de mercados sale completa (ver 2).
- Resolucion temporal on-chain: `ts_est` esta interpolado entre bloques (bloque ~1,5 s); ver seccion 5.

## 2. Mapa token -> (mercado 5m, lado, moneda, cierre)
- `mapa_escala/tokens.json` (= `/root/polymarket-research-datalogs/mapa_escala/tokens.json`, 82.716 tokens, 60.024 de 5m) **llega a cierre 22-Oct completo (3.456 tokens 5m/dia) y al 23-Oct solo hasta 01:50Z (110)**. `mapa_escala/des.json` (52.547 mercados, mid max 6.016.022) igual. Cualquier script que lea esos dos ficheros trunca en silencio desde el 23-Oct.
- Fuente vigente que si cubre 22..25: (a) `agentes_datos/mapa_infra/tokmap/*.k.json` (cache de filas `k` de los `maker_ms_*` crudos, formato `token -> [moneda, marco, mid, cierre_epoch, YES|NO]`; YES = Up, NO = Down) generada por `experimentos/5m_barato/b_perdidas_22oct/mapa_escala/infra/tokmap.py::tokens_dia(D)` (union D-1,D,D+1 de crudos + `m15_registro`); (b) las filas `k` de `VOL/m5_registro/m5_registro_D.csv.gz` y `VOL/m15_registro/m15_registro_D.csv.gz` (hasta 25-Oct existen; usadas por `analisis_5m_barato_quien_gana.mapas(d)` que ya tolera D+1 ausente). `tokmap` aun no tiene 25-Oct completo (lo hace el cron 12:15Z de hoy); lo cubre `m15_registro_2026-10-25`.
- Union comprobada (tokmap + k de m15_registro 24/25): **3.456 tokens 5m por dia de cierre = 6 monedas x 288 mercados x 2 lados, 22/23/24/25-Oct sin hueco** (26-Oct solo 104 aun). Cobertura de mapa en EUR de fills (maker, todos los precios) = 100 % en todas las monedas y dias (circular en 22-24, porque el extractor filtra por ese mismo mapa; la prueba independiente es la rejilla 288/288).
- Fichero listo para sustituir a `tokens.json` sin cambiar su formato (creado en scratchpad, solo lectura; regenerable con `/tmp/claude-0/-root-polymarket-research/5413e25f-f837-4f30-bd32-3a7c92fe5d04/scratchpad/mk_tokens.py`): `/tmp/claude-0/-root-polymarket-research/5413e25f-f837-4f30-bd32-3a7c92fe5d04/scratchpad/tokens_5m_22_26oct.json` (13.928 tokens: 22-25 completos). Debe moverse a un sitio estable si el chief lo aprueba.

## 3. Tabla dia x moneda x cobertura (fills maker de m5_onchain_D, `taker != exchange`, dedup tx+log_index = 0 duplicados; EUR = capital "compra equivalente": compra=USDC, venta=acc-USDC)
Desenlace = `maker_ms_desenlaces_cache.json` (60.903 mercados, solo YES/NO, mtime 26-Oct 05:20Z) U `mapa_tp1/des.json`. cobMapa = EUR con token en el mapa; cobDes = EUR con desenlace.
| D | moneda | tokens con fill | EUR | cobMapa | cobDes |
|---|---|---|---|---|---|
| 22 | BTC | 594 | 7.213.246 | 1,0000 | 1,0000 |
| 22 | ETH | 580 | 405.475 | 1,0000 | 1,0000 |
| 22 | SOL | 578 | 168.810 | 1,0000 | 1,0000 |
| 22 | XRP | 577 | 63.517 | 1,0000 | 1,0000 |
| 22 | DOGE | 574 | 45.553 | 1,0000 | **0,9697** (16 mercados sin desenlace en cache) |
| 22 | BNB | 555 | 19.280 | 1,0000 | **0,9264** (30 mercados) |
| 23 | BTC / ETH / SOL / XRP / DOGE / BNB | 581 / 579 / 578 / 576 / 564 / 548 | 7.316.122 / 426.370 / 176.882 / 79.485 / 32.893 / 19.951 | 1,0000 | 1,0000 todas |
| 24 | BTC / ETH / SOL / XRP / DOGE / BNB | 582 / 579 / 577 / 576 / 568 / 547 | 6.364.035 / 397.235 / 156.278 / 63.767 / 23.648 / 14.773 | 1,0000 | 1,0000 todas |
| 25 | BTC / ETH / SOL / XRP / DOGE / BNB | 583 / 578 / 581 / 575 / 567 / 491 | 6.229.933 / 329.236 / 122.254 / 49.939 / 17.185 / 9.254 | 1,0000 | 1,0000 todas |
- Los 46 mercados del 22-Oct sin desenlace en cache (01:55-23:50Z, 16 DOGE + 30 BNB) **resuelven en gamma `closed=true`**: sonda de solo lectura (1 peticion publica, sin escribir cache) -> 46/46 (26 YES, 20 NO). Cierra con `desenlaces(set(mids))` de `analisis_maker_cancelacion_binance.py` (escribe el cache; lo hace `f20_carga.cargar()` por si solo, o el chief). TP1 (`mapa_tp1`) marca el 24-Oct "cob=0,987" en N4: es SU celda de pc 0,01-0,10 con otra definicion, no este cuadro.
- Limites: cobertura "en EUR" mide el capital de los fills conocidos; no prueba que no falten fills (hueco 22-Oct) ni que el mapa tenga tokens de mercados sin fill. 25-Oct: desenlaces del 25 estan en cache porque gamma ya cerro; el cache NO distingue "resuelto" de "pendiente" (solo guarda YES/NO).

## 4. Entradas de los scripts para dias nuevos sin tocar su logica
Todos ejecutar con `cd <dir> && ulimit -v 3000000 && nice -n 19 ionice -c3 ...`, fuera de 06:00-09:30Z, load5<4 (ahora ~5,2).
### M2 (f24/f25) - cadena `poblacion_D -> feat_D -> ext_D -> lado_D` en `/root/polymarket-research-datalogs/wallet_pspspsps5/` (symlink al volumen; y `.../senales_externas/`)
- Hoy existen ext/lado/feat/poblacion 05..12 y 17..23-Oct. **Faltan 24 y 25** (y 13-16 que no se usan; f25 excluye el 13). `f20_carga.cargar()` lee TODOS los `ext_2026-*.csv.gz`, junta `lado_D` y llama a `desenlaces()`.
- Scripts (cada uno idempotente: salta si ya existe la salida; la lista de dias es argv):
  `scripts/f7_poblacion.py D` (m5_onchain_D + `mapas(D)` = m5/m15_registro D-1,D,D+1) -> `scripts/f13_features.py D` (binance_bookticker prev/D/next) -> `senales_externas/scripts/f18_ext_features.py D` (feat_D, chainlink_prev/D/next de `data/prices`, filtra `source==chainlink`; bookticker) -> `senales_externas/scripts/f19_otro_lado.py D` (m5_onchain_D + `mapas(D)`).
- Ficheros de entrada y su estado: m5_onchain 24,25 OK; m5_registro/m15_registro 24,25 OK (26 aun no: `mapas` lo tolera; el ultimo mercado de cada dia, cierre 00:00 del dia siguiente, se completa con el D+1); `binance_bookticker_2026-10-2{4,5,6}.csv` OK (26 parcial); `data/prices/chainlink_2026-10-2{4,5,6}.csv` OK (26 parcial). Ninguno rotado (los mas antiguos disponibles: bookticker 24-Sep, chainlink 10-Oct, onchain_fills 19-Oct).
- **Dos puntos que NO son de lista de dias y hay que decidir antes**: (a) `f25_gap_robustez.py` linea `P = P[P.gap.notna() & (P.dia != "2026-10-13") & (P.dia != "2026-10-24")]`: el 24 estaba excluido porque entonces solo tenia la cola del 23; para M2 hay que quitar esa exclusion y ademas restringir a `dia >= "2026-10-24"` (OOS, prereg) y `dia <= "2026-10-25"` (el dia de cierre 26 que arrastra `ext_25` queda con 1 mercado/moneda); f24 usa `per in {DESC,HOLD}` (todo >=17 es HOLD). (b) El prereg exige EV por mercado-lado y bootstrap por dia con semilla 20261026 y la regla `esW` (wallet 0xb0f85baa...) igual: f25 ya excluye W de la poblacion (`Q = P[~P.esW]`).
- Mejor: copiar f24/f25 a un directorio nuevo con solo ese cambio de lista y comparar hash del resto.
### M1 (a3/a4 + comun.py) - NO corre tal cual sobre dias nuevos
- `comun.py`: `DIAS=[2026-10-06..2026-10-21]` (16 dias), `DES` desde `mapa_escala/des.json` (hasta mid 6.016.022, ~22-Oct), lectura de `agentes_datos/wallets_ballenas_b/{M,T}_D.pkl` (existen 06..21, mtime 25-Oct 11:11Z). a3/a4 iteran `for d in range(7,16)` = indices de DIAS (13..21-Oct); la ventana walk-forward es D-7..D-1 (dias 15..21 ya estan; para evaluar 22.. hace falta ampliar DIAS y el rango).
- Generacion de M_/T_: `experimentos/5m_barato/b_perdidas_22oct/wallets_ballenas_b/scripts/e1_extrae.py [D ...]` (argv = dias, idempotente), que lee `m5_onchain_D` y **`mapa_escala/tokens.json`** (truncado desde 23-Oct 01:50Z: M_/T_ del 23, 24, 25 saldrian incompletos SIN error). Sustituir esa ruta por el mapa de la seccion 2 (cambio de entrada, no de logica) y tambien `DES` por la union cache+des.json (cobertura 22-Oct tras `desenlaces()`).
- a3 contiene la definicion de perdedoras (`elig`: z<=-2, ev<0, N>=20, nd>=3, C>=100 sobre D-7..D-1) pero NO el disparador/ventana [t+5,t+60] s, T 60-300 s, control 0,70-0,95 ni placebo del PREREG M1: eso es codigo nuevo, no "solo lista de dias". a4 (R7) tampoco lo contiene. Entradas de M1 que no estan en rotacion: M_/T_ pkl persistidos (volumen); no dependen de ficheros rotados.
- Dependencia no relacionada: a3 linea 60 lee `data/shadow/ballenas_timing_history.csv` (solo para un contraste de rango), no esencial.

## 5. V4: ?se puede saber con on-chain si un nivel de ask se consumio antes de t0+215 ms?
- `m5_onchain`/`onchain_fills` tienen `bloque`, `log_index`, `tx`, `order_hash`, `ts_est`, maker/taker. `log_index` ordena eventos DENTRO de un bloque/tx; `ts_est` es el tiempo del bloque interpolado (diferencia mediana entre bloques 1,5 s, valores a 0,1 s), y el casado ocurre en el CLOB antes de la inclusion (notas del proyecto: bloque ~2,4 s despues del casado). Ningun campo da hora de casado a ms.
- Por tanto **NO**: on-chain solo puede decir "un fill de ese token/precio/tamano existio en un bloque cuyo ts_est esta en [t0-X, t0+Y]" con incertidumbre de ~1,5-4 s; no distingue consumo antes/despues de t0+215 ms. Dentro del mismo bloque, `log_index` solo ordena entre fills on-chain, no respecto a nuestro t0.
- Para V4 la cuestion de "nivel consumido antes de t0+215 ms" se responde con el registro ms (`maker_ms_*`, filas t con hora de exchange y de recepcion) y el libro WS; on-chain aporta identidad maker/tomador y confirmacion cruzando por token+precio+tamano (y solo hacia atras: un fill con bloque anterior al t0 prueba consumo previo; uno posterior no lo descarta ni lo confirma). Crudos maker_ms disponibles: 22 (con uno corrupto), 23, 24, 25 (rotan ~4-5 d: el 22-Oct sale ~27-Oct).

## 6. Lista exacta de comandos (no ejecutados salvo lectura)
```
# 0 integridad de preregs
cd /root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/alpha_miner && sha256sum -c PREREG_M1_CONTRA_PERDEDORA.sha256 PREREG_M2_COLCHON_PARIDAD.sha256
# 1 completar desenlaces 22-Oct (46 mercados BNB/DOGE; escribe maker_ms_desenlaces_cache.json)  [lo ejecuta f20_carga.cargar() igualmente]
# 2 M2: extender la cadena a 24 y 25-Oct (cada uno ~1-3 min, de uno en uno)
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallet_pspspsps5 && ulimit -v 3000000 && for d in 2026-10-24 2026-10-25; do nice -n 19 ionice -c3 python3 scripts/f7_poblacion.py $d && nice -n 19 ionice -c3 python3 scripts/f13_features.py $d && nice -n 19 ionice -c3 python3 senales_externas/scripts/f18_ext_features.py $d && nice -n 19 ionice -c3 python3 senales_externas/scripts/f19_otro_lado.py $d; done
# 2b M2: f24/f25 sobre copias con solo la lista de dias cambiada (dia>=24 y <=25, sin la exclusion del 24)
# 3 M1: e1_extrae con mapa corregido (tokens_5m_22_26oct.json) para 22..25; ampliar DIAS/rango en una copia de comun.py/a3/a4 + codigo del disparador del prereg
cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/wallets_ballenas_b/scripts && ulimit -v 3000000 && nice -n 19 ionice -c3 python3 e1_extrae.py 2026-10-22 2026-10-23 2026-10-24 2026-10-25   # SOLO tras sustituir la ruta de tokens.json
# 4 cobertura por dia (el awk + cov2.py del scratchpad): .../scratchpad/tokvol.sh D ; .../scratchpad/cov2.py
```
Scripts de auditoria: `/tmp/claude-0/-root-polymarket-research/5413e25f-f837-4f30-bd32-3a7c92fe5d04/scratchpad/{tokvol.sh,cov2.py,probe.py,mk_tokens.py}`.
