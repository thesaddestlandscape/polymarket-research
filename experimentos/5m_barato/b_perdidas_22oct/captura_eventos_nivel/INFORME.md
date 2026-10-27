# Captura pasiva de eventos de nivel del WS del CLOB para el ciclo de vida de las órdenes de W (pspspsps5)

Fecha 24-Oct 12:10Z. Agente cheap5m-execution-engineer. Estado: DISEÑO + PRUEBA EN SECO. Nada instalado, nada reiniciado, B/live/crons/`observadores` intactos.
Todo en `/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/captura_eventos_nivel/`.

## 0. Respuesta corta
1. **El registro que ya existe BASTA para ver la vida de un nivel; no hace falta una captura nueva de niveles.** Es `libro5` (`libro_estado_ws._Libro5`, hijo ya activo, una conexión por moneda#marco, pid 890056 desde 10:20Z): feed crudo de TODOS los tokens 5m vivos con filas `B` (libro completo), `d` (cada `price_change`: lado, precio, tamaño ABSOLUTO del nivel, 0 = vacío), `T` (`last_trade_price`) y `G` (huecos), cada una con hora del exchange (`t_ms`) y de RECEPCIÓN (`recepcion`, p50 exchange→recepción ≈ 40 ms) y `seq`. `maker_ms`/`m5_registro` NO son necesarios (solo traen top-of-book `q`).
2. **Lo que falta no es el nivel sino la CLAVE de alineación y la RETENCIÓN**: (a) `libro5` descarta el campo `transaction_hash` de `last_trade_price`, que sí viene en el WS y coincide con el `tx` on-chain (**732/732** de los tx recibidos en una captura de 150 s el 24-Oct 11:43Z están en `onchain_fills_2026-10-24.csv.gz`); sin él, la alineación fill↔casado es solo por (token, precio, ventana) y es única en 4/22 y 4/40 fills; (b) `libro5` rota por presupuesto (20 GB, ~3,2 GB/día → ~6 días): los días 22-23-Oct de W se borran hacia el 27-28-Oct.
3. **Lo que NINGUNA captura puede dar**: identidad de orden. El WS público no lleva id de orden: el `hash` de `price_change` es de 40 hex (no el `order_hash` EIP-712 de 66), y medido en 218.694 entradas (150 s, 4 tokens) 210.518 hashes distintos, de los cuales solo 1 abarca >1 timestamp: es un hash de evento/lote, no de orden. Una orden de W solo se ve como un salto `+acc` de un nivel AGREGADO y su salida como `−acc` (con `T` = relleno; sin `T` = cancelación de alguien en ese nivel). La atribución a W es probabilística, no determinista.

## 1. Demostración con días reales (22 y 23-Oct) con `ciclo_vida_W.py`
Fills de W de `ordenes_D.csv.gz` (wallet_pspspsps5, con `tx`, `order_hash`, `ts_est`=bloque, p, acc), token por `mapas(d)` de `analisis_5m_barato_quien_gana`, niveles de `libro5`. Solo compras (side 0), p∈[0,03-0,40], acc ≥ 10, muestra aleatoria con semilla (22-Oct 12-14h seed 7; 23-Oct 14-16:30h seed 11). Comandos y salida cruda: `lote_22oct.txt`, `lote_23oct.txt`, `demo_fill_ETH_22oct.txt` (vida completa de un nivel, 304 líneas), `demo_22oct.txt` (5 fills sin filtro de tamaño, con muchas órdenes de 5 acc).

| Medida (22-Oct n=22 · 23-Oct n=40) | 22-Oct | 23-Oct |
|---|---|---|
| fills con ≥1 `T` del mismo precio en [−6 s, +0,5 s] del bloque | 21/22 | 38/40 |
| … con EXACTAMENTE 1 `T` (alineación única sin tx) | 4/22 | 4/40 |
| `T` con tamaño == acc (±2 %) | 3/22 | 5/40 |
| «alta» del nivel de tamaño == acc en los 120 s previos (ALTA_EXACTA) | 8/22 | 20/40 |
| placebo: mismo nivel, tamaño ×1,37 | 0/22 | 0/40 |
| placebo: nivel p+0,01, tamaño acc | 2/22 | 2/40 |
| caída del nivel == acc en ±300 ms del `T` (relleno visible) | 7/22 | 12/40 |
| reposo alta→`T` entre ALTA_EXACTA (p10 / p50 / p90) | 0,61 / 6,2 / 15,9 s (n=8) | 0,52 / 2,3 / 77 s (n=20) |
| offset `T` − ts_est (solo alineación única, n=4+4) | −3,0 / −2,3 / −1,7 s | −5,6 / −1,5 / −1,4 s |

Lectura (EXPLORATORY, n=62 fills, un solo trader, sin gates):
- **Sí se reconstruye la vida de un nivel**: alta, bajas con y sin `T`, tamaños, reposo, huecos `G`. En `demo_fill_ETH_22oct.txt` (ETH 13:03:31Z, p 0,03, nivel de ~900 acc) se ven en 2 min cientos de altas/bajas de tamaños repetidos (33,34 / 40 / 80 / 170 / 300 acc) re-colocadas cada 0,1-1 s sin `T`: recotizadores. Esa es la información de «retirada antes de rellenarse» pero para el NIVEL, no para W.
- **La orden de W aparece como alta de su tamaño en ~45 % de los fills** (28/62) frente a 0/62 (tamaño falso) y 4/62 (nivel vecino): señal por encima del azar, pero en el otro 55 % la orden estaba antes de la ventana de 120 s, tiene tamaño parcial o el nivel está enterrado en ruido. Para W la vida entre el alta y el relleno sale de p50 2-6 s con cola larga (p90 16-77 s): coherente con «un fill por bloque», NO prueba que retire/recoloque.
- El bloque on-chain llega ~1,4-3 s después del casado (offset `T`−ts_est p50 −1,5/−2,3 s), de acuerdo con la hipótesis ±2,4 s. Con 4 casos únicos esa estimación es débil: con tx saldría exacta.
- **Límites que hay que declarar**: el nivel agregado no distingue W de otros con el mismo clip; la clasificación «baja con T/sin T» usa ±1 s y mezcla casados de otros tamaños; el `T` del WS lleva el tamaño del casado del taker, no el de cada maker; un fill de W es el barrido por bloque, no su orden entera.

## 2. Qué se captura y alineación (diseño)
- **Ya capturado (libro5)**: B/d/T/G con exchange y recepción para 5m de todas las monedas. Formato 8 columnas `tipo,t_ms,token,c1,c2,c3,recepcion,seq` (ver docstring de `_Libro5`). No tocar.
- **A añadir (mínimo cambio, SIN aplicar)**: fila `X,t_ms,token,<tx_hash>,,,recepcion,seq` justo tras cada `T` (mismo mensaje, seq consecutivo). Es un tipo nuevo de fila: los lectores que despachan por `c[0]` (p. ej. `a6_detector_vivo/r5k_io.py`) la ignoran; las filas B/d/T/G no cambian. Parche: `parche_libro5_tx.diff` (3 hunks en `libro_estado_ws.py`: `operacion()` y `_texto()`). Comprobado en copia: `py_compile` OK y `tests/test_libro5_registro.py` pasa con el módulo parcheado (`OK todos`, `OK presupuesto`); no se ha ejecutado contra el WS vivo con el parche.
- **Clave de alineación** con W (de `ordenes_D`/`fills`): `tx` ⇒ fila `X` ⇒ el `T` anterior (mismo token, mismo `t_ms` de exchange) ⇒ instante exacto del casado en ms; después, el nivel `(token del fill, precio)` en `d` justo antes/después. Sin `X` (histórico y hasta que se despliegue): `(token o gemelo a 1−p, precio, ventana [−6 s,+0,5 s] del bloque)` ⇒ ambiguo (único en 8/62). Si hay varios `T` candidatos el script lo dice (`alineacion: VENTANA`, `T_matches`).
- La fila `d` lleva el `t_ms` del exchange del mensaje (sello de lote: ordenar por `seq`/recepción, no por `t_ms`; trampa documentada en CLAUDE.md).

## 3. Volumen y retención
- `libro5` hoy: ≈3,2 GB/día gz (22-Oct ≈3,2; 23-Oct ≈3,2; sdb 70 %, 64 GB libres), 37 ficheros / 19 GB, presupuesto propio 20 GB ⇒ **retención efectiva ≈6 días** (los 3 últimos nunca se borran). Excede el «<1 GB/día» pedido, pero ya existe y no se toca.
- **Parche `X`**: ≤ ~15 MB/día gz (las filas `T` son ~0,2 % de las líneas: 6.290 `T` en 3 M de líneas; una fila `X` de ~115 B por `T`). Sin impacto en CPU del hijo (un `isinstance` y un append).
- **Extracto de niveles bajos para W** (`extraer_libro5_bajos.sh`): conserva `T` y `G` íntegras, `d` solo de bids con precio ≤ 0,20 y `B` recortado a bids ≤ 0,20; MISMO formato (ciclo_vida_W lo lee sin cambios). En un trozo de 3 M líneas: 46,8 MB → 4,85 MB (≈10 %). Día completo 22-Oct medido: 8 ficheros origen (≈3,15 GB) → **363 MB** (11,5 %), 8 m 27 s de pared con load 12-19 (7 m 54 s de CPU). Retención propuesta 14 d en el volumen sdb (≈5 GB). Cubre la mayor parte de los fills de W (95,7 % de sus fills <0,10 según INFORME de W).
- Vaciado del gzip cada 30 s: NO aplica al parche (reutiliza el escritor de libro5). Observación: `libro5_ms_2026-10-23_478607.csv.gz` termina truncado («unexpected end of file», cierre sin vaciar en el reinicio de las 22:20Z); `zcat` entrega todo lo anterior y `ciclo_vida_W` lo tolera, pero se pierden los últimos segundos antes de cada reinicio. Un `flush()` periódico con `Z_SYNC_FLUSH` en el hilo escritor de `_Libro5` lo acotaría (no incluido en el parche: toca el escritor compartido).

## 4. Herramientas entregadas (todas solo lectura, sin red, sin órdenes)
- `ciclo_vida_W.py` — dado un fill (`--tx`, `--order-hash` o muestra `--n/--seed/--pmin/--pmax/--min-acc/--hora-*`) imprime la vida del nivel (ventana `--ventana-ant 120 / --ventana-post 20`), clasifica ALTA_EXACTA/ALTA_AMBIGUA/SIN_ALTA_VISIBLE, alinea con `T` (modo TX si hay filas `X`, si no VENTANA), calcula placebos y con `--lote` las agregadas. Memoria acotada (filtro en streaming por token/precio/ventana; `ulimit -v 3000000` OK), `grep -F -f` + `zcat`. ≈2-5 min por consulta en la máquina cargada (load 12-19) por zcat de un fichero de ~1,8 GB; con el extracto del día (363 MB) sigue tardando ≈2 min (zcat + `mapas()` con load alto), no segundos. Selecciona el fichero libro5 por hora; para el extracto: `LIBRO5_DIR=/mnt/HC_Volume_106538179/libro5_bajos`.
- `test_ciclo_vida_W.py` — test sintético (nivel con alta/cancelación/relleno, `X`↔tx, ventana, hueco G, fuera de ventana): `OK test_ciclo_vida_W`.
- `extraer_libro5_bajos.sh` — extracto diario idempotente (`.tmp` + `mv`; no sobrescribe).
- `parche_libro5_tx.diff` — NO aplicado.
- Uso: `nice -n 19 ionice -c3 python3 -I ciclo_vida_W.py --dia 2026-10-22 --tx 0x83b1b2e9…`

## 5. Propuesta de arranque / cron (NO instalada; exige OK de Javi y, para el parche, /code-review)
1. **Ya, una sola vez, antes de que rote** (fuera de 06-09Z, nice 19): `for d in 2026-10-22 2026-10-23 2026-10-21 2026-10-20; do nice -n 19 ionice -c3 /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/captura_eventos_nivel/extraer_libro5_bajos.sh $d; done` (un día a la vez; ≈10 min cada uno con la máquina cargada).
2. **Cron diario** (00:35Z, tras el cierre de los ficheros del día; fuera del racimo 06-09Z): `35 0 * * * ulimit -v 3000000; nice -n 19 ionice -c3 /…/captura_eventos_nivel/extraer_libro5_bajos.sh $(date -u -d yesterday +\%F) >> /root/polymarket-research/logs/extraer_libro5_bajos.log 2>&1; find /mnt/HC_Volume_106538179/libro5_bajos -name 'libro5_bajos_*.csv.gz' -mtime +14 -delete` — con `|| aviso` si falla (regla de cron con Telegram) y alta en `vigia_loggers_silenciosos` si Javi lo quiere.
3. **Parche `X`** (`parche_libro5_tx.diff`): toca `libro_estado_ws.py`, módulo de la cadena de imports de `observadores_fase0` ⇒ el watchdog lo reiniciará y se pierde el histórico ms en memoria. Aplicar solo en una de las ventanas ya reservadas a reinicios (03:20, 10:20 o 22:20 UTC), con `/code-review` y OK de Javi, y verificar en los 5 min posteriores que aparecen filas `X` (`zcat … | grep -m3 '^X,'`) y que `verify_deploy.py` no sale STALE.
4. Tras 3-5 días con `X`: correr `ciclo_vida_W.py --lote` sobre esos días ⇒ alineación TX en ~100 % de los fills de W y distribución del reposo/retirada con casado exacto.

## 6. Prueba del extractor sobre un día completo
Ejecutado una vez: `/mnt/HC_Volume_106538179/libro5_bajos/libro5_bajos_2026-10-22.csv.gz` (363 MB; log `extraccion_22oct.log`; único artefacto persistente creado, borrable). Comprobación cruzada: el fill ETH 0x83b1b2e9… dio con el extracto EXACTAMENTE el mismo resultado que con libro5 completo (480 eventos de nivel, 179 altas / 191 bajas / 139 sin T, ALTA_EXACTA reposo 15,903 s, T a −1677 ms con tamaño 20, caída 20,0). Para otros días: 23-Oct no extraído.

## 7. Riesgos
- Parche `X`: reinicio de observadores (histórico ms perdido); cambio de formato aditivo (fila nueva) — lectores que asuman solo B/d/T/G y no filtren por tipo fallarían; revisado `r5k_io.py` (despacha por `c[0]`), no revisados los otros ~25 lectores de `libro5` (lista: `grep -rl libro5 --include=*.py`).
- El extracto recorta asks y niveles >0,20: no sirve para estudiar makers de precios altos de W; subir `PMAX` aumenta tamaño (≈ +4 puntos por cada +0,10).
- CPU: el extractor lee ~3,2 GB gz/día (~7 min de CPU); con load 12-19 puede tardar >15 min en pared. Nice 19 + ionice -c3; nunca 06-09Z.
- Disco: sdb 70 % (64 GB libres); +5 GB de extractos. El disco raíz sda (79 %) no se toca.
- Interpretación: la vida del NIVEL no es la vida de la ORDEN de W. Cualquier conclusión sobre «W retira antes de rellenarse» será indirecta (alta de su tamaño visible ~45 %), debe llevar placebo (tamaño falso, nivel vecino) y unidades = fills por mercado, no por evento de nivel; no hay n para gates (n=62).
- Ningún dato aquí sustenta que W tenga edge replicable ni valida ninguna estrategia.

## 8. Respuesta final entregada (resumen)
libro5 YA contiene el ciclo de vida de los niveles (B/d/T/G con exchange+recepción) y basta; reconstruido en 22 y 23-Oct (n=62 fills de W: alta de su tamaño visible en 28/62 vs placebos 0/62 y 4/62; alineación solo única en 8/62). Falta (a) `transaction_hash` del `last_trade_price` (732/732 coinciden con on-chain) -> `parche_libro5_tx.diff`, NO aplicado, requiere /code-review + OK Javi + reinicio de observadores; (b) retención: libro5 rota a ~6 d -> `extraer_libro5_bajos.sh` (11,5 % del tamaño, 22-Oct ya extraído) + cron 00:35Z propuesto. Identidad de orden: imposible con datos públicos del WS.
