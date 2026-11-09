# DISEÑO: captura independiente del registro Binance (+ L2 + latencia de cancelación) — 09-Nov-2026
Autor: cheap5m-market-data-engineer. SOLO DISEÑO: nada instalado, nada editado salvo este documento. Estado: propuesta para chief/Javi.
Fail loud: lo marcado **[NO VERIFICADO]** es estimación o suposición. Cifras medidas hoy (15:5xZ) con comandos de solo lectura.

## 0. Hechos verificados hoy (base del diseño)
- El registro Binance (`_binance_registro`, libro_estado_ws.py l.1004) corre DENTRO del hijo `libro_estado_ws.py --hijo`, que es proceso hijo de `observadores`
  (pid 3722472 padre, 3722841 hijo). Muere con el padre (EOF en stdin). Escribe filas `b` (bookTicker, solo si cambia bid/ask) y `x` (aggTrade) en el MISMO
  `maker_ms_<día>_<pid>.csv.gz` que h/q/t/l/L/k. Mezcla medida (1,9 h, fichero 3722841): q 6,86 M, h 1,83 M, l 1,28 M, x 257 k, b 132 k, t 63 k, L 35 k.
  Binance ≈ 390 k filas/1,9 h = ~30 MB crudo/1,9 h → **~0,4 GB crudo/día, ~70 MB gz/día [extrapolación de 1,9 h, NO medida a día completo]**.
- Huecos de hoy en `x` (hora de recepción): **10:20:01,6 → 10:20:47,8 = 46 s** (restart_ram) y **14:00:21,8 → 14:02:49,8 = 148 s**: causa NUEVA no listada en el mandato:
  **OOM-killer a las 14:00:29** (`journalctl -k`: "Killed process 3659908 (python) rss 1,16 GB, oom_score_adj 0" = observadores); el watchdog lo vio ausente en su tick
  de las 14:02:08 (logs/watchdog.log:88833) y lo relanzó. Es decir: tres causas de hueco (cron restart_ram, OOM, watchdog) con el mismo mecanismo (el registro vive en observadores).
  27 líneas "Killed process" en `journalctl -k` desde el 26-Oct (no todas son observadores; sin desglosar).
- Un corte de red de Binance también deja hueco silencioso: 08-Nov 21:56:04 "ConnectionClosedError", reconecta a los 3 s (fijo 2 s) y NO deja marca en el fichero.
- Sincronía de reloj local OK: chrony stratum 3, offset 38 µs, RMS 56 µs; zona UTC (timedatectl "synchronized: yes").
- Silencios >2,5 s de BTC aggTrade (39 en 1,9 h): en los 39 las otras 5 monedas SÍ operan (mediana 19 trades dentro) → son calma de BTC, no caídas del feed. Un detector de hueco
  NO puede ser "silencio de un símbolo"; ha de ser silencio de la UNIÓN de símbolos o ids no contiguos (ver §1.5).
- Quién lee `maker_ms_*` (≈45 scripts por grep): todos hacen glob `maker_ms_<día>_*.csv.gz` y filtran por letra de tipo; los verificados (vigia_5m_barato_forward.procesar l.296,
  analisis_maker_cancelacion_binance.leer l.50, extraer_registro_5m_barato l.102, comprimir_data_historica.sh l.220) toleran varios ficheros por día y que a un fichero le falten tipos.
  Hay lectores **pandas** (m15_ms_cache.py l.63 `names=` fijo de 8 columnas; analisis_15m_v4_quien_gana, analisis_5m_maker_banda_deep_peg...): una fila x/b con 9º campo los rompería.
  Los 45 NO se han leído uno a uno: **[NO VERIFICADO]** que ninguno asuma "el fichero 1 del día lleva k" o ordenación por fichero (el test T2 de §7 lo comprueba con 4 lectores).
- Solo `observadores` tiene libro_estado_ws.py en su cierre de imports (`verify_deploy.cierre_imports` sobre todas las SCREENS): editarlo reinicia solo observadores (cascada del watchdog, cooldown 600 s).
- Precedente directo del patrón pedido: screen `logl2` (logger_anticipo_barrido.py: proceso propio, solo lectura, nice 19, ulimit -v 3 GB, sin choom, probe por log, registrado en
  SCREEN_RESTART l.251 / check_screens l.390 / verify_deploy l.124, latido por minuto, retención propia) y `multivenue` (4 bolsas en ms, proceso propio).

## 1. Diseño A: proceso propio del registro Binance
### 1.1 Módulo y screen
- Fichero nuevo `binance_registro_ms.py` (raíz del repo). **Imports: solo stdlib + `websockets`** (sin ningún `import` de módulo local) → su cierre de imports es {sí mismo}:
  el watchdog lo marca STALE solo si se edita ESE fichero, nunca por commits en módulos muy importados (smart_money_tracker, data_api, libro_estado_ws).
- Constantes (símbolos, URL) COPIADAS del hijo, con un test que compare `_SIMB_BN`/`BINANCE_WS` de libro_estado_ws.py con las del módulo (evita deriva; no se importa para no heredar el cierre).
- Screen `bnreg`. Comando (SCREEN_RESTART): `cd {REPO} && ulimit -v 2000000; .venv/bin/python -u binance_registro_ms.py >> logs/binance_registro_ms.log 2>&1`.
  Prioridad: dentro del script `os.setpriority(PRIO_PROCESS,0,-10)` (como el hijo: mejora el sello→recepción medido el 17-Oct). Sin envío de dinero → sin `choom` obligatorio;
  **opcional `choom -n -200`** (RSS esperado <100 MB: perderlo por OOM reabre el problema; decisión Javi, no cambia nada más).
- Probe verify_deploy: `log:logs/binance_registro_ms.log:conectado a Binance spot`.
### 1.2 Salida: mismo formato y ruta (sin migración de lectores)
- Fichero `/root/polymarket-research-datalogs/maker_ms_<día>_<pid>.csv.gz` (mismo patrón que hoy → la retención 4 d local + 30 d volumen de comprimir_data_historica.sh y la
  extracción diaria lo cubren sin tocar nada), cabecera idéntica `tipo,t_ms,id,c1,c2,c3,c4,c5`, gzip nivel 9, volcado cada 5 s, un fichero por arranque y día, tolerancia a final truncado.
- Filas IDÉNTICAS a las actuales y exactamente 8 campos: `x,T,sym,p,q,m,E,recv_ms` y `b,recv_ms,sym,bid,ask,B,A,` (b solo si cambia (bid,ask), como hoy). **No se añaden columnas** (pandas).
- Diccionario de tiempos de esas filas: `T`=hora de la operación en el exchange (ms), `E`=hora del evento en el exchange (ms); `recv_ms`=reloj local UTC (`time.time()`) tomado cuando el
  bucle asyncio recibe el frame (incluye cola asyncio, no es hora de NIC); bookTicker spot NO trae hora de evento: solo `recv_ms` (por eso en `b` la columna 2 es la recepción).
  Medido hoy: recv−E BTC p50 133 ms, p90 140, p99 190 (n=107.496; ETH idéntico): el tramo Binance→VPS es ~133 ms fijos (ver §6); NO restar E a recv como "latencia de nuestro código".
- Integridad (SIN tocar el CSV): ficheros hermanos pequeños, fuera de git:
  - `binance_integridad_<día>.csv` 1 fila/min/símbolo: n_x, a_min, a_max (aggTradeId, contiguo por símbolo → faltantes = a_max−a_min+1−distintos), duplicados, fuera de orden,
    n_b, u_min/u_max (bookTicker updateId, monótono), recv−E p50/p90/p99, conexión (id). ~9 k filas/día (<2 MB).
  - `binance_huecos_<día>.csv`: desconexión/reconexión (t_ms caída, t_ms reconexión, motivo, conn_id), arranque/parada propios, cola llena (descartes). Cada reinicio deja marca (corrige el defecto de logl2).
  - `binance_registro_estado.json` latido cada 10 s (ts, estado, filas/min, último T, conn_id, descartes) — el vigía lee este fichero (§4).
- Retención de los hermanos: 60 d, borrado propio al arrancar y al cambiar de día (patrón logl2). Tamaño total hermanos ≈ 0,1 GB.
### 1.3 Reconexión y vigilancia propia
- Backoff 1→2→4→…→30 s con reinicio a 1 s tras 60 s sanos (hoy 2 s fijo). Marca de hueco en cada caída/reconexión.
- Watchdog interno: si no llega NINGÚN mensaje de la unión de los 12 streams en 10 s → cerrar y reconectar; si lleva >120 s sin conseguir datos → `sys.exit(2)` (la screen
  desaparece y el watchdog de 120 s la relanza; mejor que un proceso colgado vivo). Binance corta cada ~24 h el socket: se espera y se marca como reconexión planificada.
- Cola acotada (200 k líneas como hoy); si el disco va lento se descarta y se cuenta (nunca se frena el socket).
### 1.4 Un solo escritor (flock) y habilitación
- Lock `/root/polymarket-research-datalogs/.binance_registro.lock` con `fcntl.flock(LOCK_EX|LOCK_NB)`. Lo toma quien ESCRIBE Binance; el kernel lo libera al morir el proceso.
- **bnreg** escribe solo si existe el fichero centinela `/root/polymarket-research-datalogs/BNREG_HABILITADO` (si no: bucle ocioso, sin lock, sin conexión). Motivo: registrar la screen en
  el watchdog ANTES del traspaso la haría arrancar sola con el hijo VIEJO (sin lock) aún escribiendo → doble escritor. El centinela es además el **kill-switch** (borrarlo → bnreg suelta el lock).
- **Hijo (cambio mínimo en libro_estado_ws.py)**: antes de cada `_binance_registro` intenta el mismo lock; si no lo consigue, queda en reserva: reintenta cada 5 s y lo registra UNA vez en log.
  Con bnreg vivo el hijo no escribe Binance; si bnreg cae por OOM/bug el hijo (si vive) asume en ≤5 s (hueco ≤5 s en vez de 120 s); si el hijo muere, bnreg toma el lock en ≤1 s.
  El hijo conserva el código de registro (marcha atrás sin redeploy: quitar el centinela).
### 1.5 Cómo medir huecos (definición para los tests)
Hueco = silencio de la UNIÓN de las 6 monedas en `x` > 3 s, O faltantes de aggTradeId en `binance_integridad`, O fila en `binance_huecos`. Nunca silencio de un solo símbolo (§0).

## 2. Despliegue sin pérdida (un único reinicio de observadores)
Restricciones: fuera de 06:00-09:15Z y de horario USA (restart_ram ya está en 22:20Z = 18:20 ET); editar libro_estado_ws.py marca STALE solo a observadores; el watchdog (tick ~120 s;
ver `logs/watchdog.log`) lo reiniciaría por su cuenta → hacer TODO en una secuencia corta justo tras un tick.
Pre-requisitos (en dev, revisados): módulo nuevo; parche libro_estado_ws.py (lock reserva); entradas SCREEN_RESTART/check_screens/verify_deploy; vigía; script de traspaso.
Orden exacto (script de fichero `scripts/traspaso_bnreg_once.sh`, no `bash -c` ni heredoc; sin el nombre de los .py en su propia cmdline; **sin pgrep/pkill -f**: usar ps+awk o /proc):
 0. Hoy-o-antes, sin efecto: copiar a main `binance_registro_ms.py` y editar `verify_deploy.py::SCREENS` y `pipeline_watchdog.py` (SCREEN_RESTART + check_screens); reiniciar el
    watchdog A MANO (trampa documentada: no se autorreinicia). bnreg arrancará ocioso (centinela ausente). Ni verify_deploy ni pipeline_watchdog están en el cierre de observadores.
 1. T0 = justo tras un tick del watchdog (+10 s). Tomar `flock /tmp/restart_ram_fase0.lock` (bloquea cron y guard_ram durante el traspaso).
 2. `cp` libro_estado_ws.py nuevo a main (observadores pasa a STALE; margen de ~100 s hasta el siguiente tick).
 3. Matar la screen observadores por PID (como `verify_deploy.reiniciar`: quit por pid + espera 1 s) → el hijo viejo muere por EOF. Confirmar con ps que no queda ningún
    `libro_estado_ws.py --hijo` (esperar ≤5 s).
 4. `touch BNREG_HABILITADO` → bnreg (ya vivo, ocioso) toma el lock y conecta (<1-2 s). **Hueco Binance esperado ≈ 2-5 s, UNA vez [NO medido]**. (Hoy: 46-148 s por evento.)
 5. `verify_deploy.py --restart observadores` (arranca con el código nuevo; el hijo nuevo ve el lock tomado y queda en reserva). Probe 45-120 s.
 6. Comprobar: `maker_ms_<día>_<pid_bnreg>.csv.gz` con x/b nuevos; el fichero del hijo nuevo SIN x/b; `binance_integridad` sin faltantes salvo la marca del traspaso.
 Marcha atrás: borrar el centinela (≤5 s: el hijo, si vive, asume); si el hijo no vive, `verify_deploy --restart observadores`.
- Consecuencia a documentar en DECISION_LOG: observadores sigue perdiendo su histórico ms en memoria y su libro Polymarket en cada reinicio (ver §5-bis).

## 3. Dependencias e imports (que el watchdog no reinicie bnreg de más)
Sin imports locales (ver 1.1): STALE solo por edición de su propio .py. No va en el cierre de observadores ni de vigiasfreq; restart_ram_fase0.sh y guard_ram_fase0.py (solo `observadores`/`vigiasfreq`)
NO lo tocan. Si en el futuro se quiere compartir código (p. ej. un helper de gzip), copiarlo dentro del módulo, no importarlo.

## 4. Registros
- `pipeline_watchdog.py::SCREEN_RESTART["bnreg"]` (comando de §1.1 + comentario datado) y su nombre en la lista de `check_screens()` (l.390); reiniciar el watchdog a mano.
- `verify_deploy.py::SCREENS["bnreg"] = {"entry":"binance_registro_ms.py","probe":"log:logs/binance_registro_ms.log:conectado a Binance spot"}`.
- `inventario_sistema.py`: clasifica solo (A) por SCREENS; verificar que no sale en (C).
- Vigía de silencio: `vigia_loggers_silenciosos` va por horas (MIN_H 3,0) y la familia `maker_ms` seguiría viva por los h/q (el hueco de Binance quedaría INVISIBLE). Añadir un chequeo del
  latido: `binance_registro_estado.json` con `ts` >120 s o `estado`≠activo (y centinela presente) → aviso; y revisar `binance_integridad` (faltantes≠0 fuera de marcas) una vez al día.
  Patrón ya existente: `_libro5_en_pausa` con libro5_estado.json. Rotación del log: añadir `logs/binance_registro_ms.log` a la rotación del watchdog.
- Doc: MAPA_ARTEFACTOS (ruta nueva), DECISION_LOG, y nota en el docstring de libro_estado_ws (el registro Binance ya no es suyo salvo reserva).

## 5. L2 (aviso 16-17 Nov)
### 5.1 Lo que YA existe (no duplicar)
- **libro5_ms** (hijo, `/mnt/HC_Volume_106538179/libro5_ms`): feed CRUDO de todos los 5m de las 6 monedas: B (libro completo), d (price_change), T (trade), G (huecos con motivo), con
  recepción y seq. 19 GB en disco (presupuesto 20 GB; ficheros de 0,1-1,9 GB/día; retención ≤14 d por comprimir_data_historica.sh l.205). Es la fuente L2 de la carrera para 5m.
- Filas `l` (3 niveles ask) y `L` (libro ask completo, solo BTC 5m que cierra con 15m, último tramo) en maker_ms.
- `libro_l2_15m_fase0.py` (cron cada minuto): REST `/books` ~1 s, 10 niveles, 15m de 6 monedas, 38-46 MB/día en el volumen, 60 d. **REST a 1 s no resuelve una carrera de 150 ms.**
- logl2 NO es el L2 de libro (es perp Binance + liquidaciones; su docstring dice que el L2 de Polymarket es libro5).
### 5.2 Lo que falta y lo que NO es observable
- Falta: profundidad por WS para 15m/60m/4h (solo existe top q/h/t) y continuidad de libro5 a través de reinicios (G marca el hueco; tras él no hay estado hasta el siguiente B).
- No observable con APIs públicas: hora de creación/envío de una orden ajena, orden de llegada de dos órdenes al motor, cola real a nuestro nivel por orden individual (solo agregada por nivel),
  hora de llegada del libro al exchange. El print T (hora del exchange) ocurre DESPUÉS del taker delay de 150 ms; la hora de bloque on-chain es ~2,4 s posterior. La "ventana W del tomador"
  solo se acota por arriba con prints (analisis_ventana_w_binance_polymarket.py). El `timestamp` del WS es sello de lote (no hora de evento): ordenar por recepción/seq.
### 5.3 Propuesta
1. **Piloto 10 min, solo lectura, offline, sin proceso nuevo** (el chief decide ahora): comprobar que libro5 basta para la carrera en 5m: reproducir B+d en orden de seq de una ventana de 10 min
   (p. ej. 12:00-12:10Z, nunca 06:00-09:15Z, nice 19, ulimit -v 3 GB) y comparar el top reconstruido con las filas `q` de maker_ms del mismo token/instante: % de coincidencia, nº de G, nº de tramos sin B.
   Criterio de suficiencia: coincidencia ≥99 % del top y 0 gaps sin marcar. [NO EJECUTADO]
2. Si el criterio se cumple: no hay logger L2 nuevo para 5m; la carrera CXJ150/H-LAT se modela con libro5 + x/b (bnreg) + latencias de §6.
3. Para 15m BTC (si la misión lo pide): **piloto de 10 min en dev** (script de lectura WS pública, 1 conexión, solo BTC 15m viva+siguiente, salida a `/mnt/.../scratch`, nice 19): mide bytes/min y
   mensajes/min por token. Si procede, ampliar el filtro de libro5 (`_Libro5.grabable`) a esos tokens en la misma edición de libro_estado_ws del §2 (menos reinicios; sube el riesgo del review).
   Volumen: **[NO MEDIDO]**; cota de orden de magnitud: 15m BTC genera ≤1/3 de los mensajes de 5m BTC → un orden de ≤0,2-0,3 GB/día gz (hipótesis a confirmar con el piloto).
### 5-bis. Fase 2 opcional (decisión Javi, NO recomendada aún)
Los huecos del lado Polymarket (h/q/t/l/L y libro5) siguen ligados a observadores (mismas 3 causas). Sacar también el hijo exigiría un grabador propio con SUS conexiones al CLOB
(las de observadores seguirían para el estado en memoria): dobla conexiones (hoy ~15/moneda#marco; el servidor corta por "slow consumer" por conexión; límites de conexiones **[NO VERIFICADO]**)
y necesita universo propio (REST gamma). Decidir tras medir cuántos G/día hay en libro5 y si el análisis de la carrera los necesita.
### 5.4 Plan de disco (cifras de hoy)
- `/` (sda1): 75 G, 67 G usados (93 %), 5,5 G libres; watchdog avisa cada 2 min. datalogs local 12 G (maker_ms reales 1,4 G + polymarket_activity 1,24 + onchain_fills 0,45 + bookticker 0,44...).
- `/mnt/HC_Volume_106538179` (sdb): 394 G, 230 G usados, 147 G libres (62 %). libro5_ms 19 G (presupuesto 20, ≤14 d), maker_ms_crudo 15 G (30 d), multivenue_ms 14 G, l2_15m 1,4 G (60 d), libro5_bajos 4,6 G.
- bnreg: mismos ~70 MB/día gz de hoy en `/` (ya retenidos 4 d y movidos a sdb a 30 d por el script existente) → **0 GB netos nuevos**; hermanos ~0,1 GB; nada nuevo en `/` que no sea ya de hoy.
- L2 15m WS (si se hace): al volumen, con presupuesto propio como libro5 (gz, fuera de git, retención ≤14 d, tope en GB); con +0,3 GB/día × 14 d ≈ 4 GB (estimación); sdb lo absorbe, `/` no se toca.
- Nunca ficheros nuevos en `data/` ni en git (trampa CSV >100 MiB del 19-Oct); todo `.gitignore`/datalogs.

## 6. Latencia de cancelación: dónde se pierde
Cadena para "cancelar cuando Binance salta" (todas las cifras con su origen):
 a) Binance evento (E) → recepción local: **p50 133 ms, p90 140, p99 190 (BTC, n=107.496, maker_ms_2026-11-09_3722841, x: c7−c6, reloj NTP ±0,06 ms)**. Es el tramo dominante y es distancia física
    (Helsinki↔matching de Binance; origen exacto del 133 ms **[NO VERIFICADO]**). Con el VPS actual (VPS cerca del CLOB descartado por Javi) es suelo, no software.
 b) Decisión en Python: no medida **[NO VERIFICADO]**; esperado ≤ pocos ms (el docstring de F2 cita p90 0,41 ms para B inline).
 c) Cancelación REST: DELETE con cabeceras HMAC (no EIP-712: se puede preparar), ack 60 ms ida y vuelta (medido 07-Oct, CLAUDE.md; `medir_latencia_ordenes_15m.py` T1 GTC post-only 68 ms).
    Ese script ENVÍA ÓRDENES REALES (T1/T2 a 0,01, no cuestan; T4 FOK muertas) → requiere OK Javi + /code-review; no lo ejecuto ni propongo ejecutarlo hoy.
 d) Ventaja estructural: el tomador paga 145-150 ms de taker delay (FOK 213 ms vs GTC 68 ms). Y una orden tomadora retenida en el delay NO se puede cancelar (14-Oct): solo gana quien cancela antes de que su orden case.
 e) "150 ms valen ~54 €" (RE-THRU1 EXPEDIENTE l.62): cancelar a 150 ms tras el salto frente a 1 s, 10 días, 5 acciones, exploratorio, validado 0 €, CROSS (el ask toca L antes de salto+150 ms) SIN medir.
    Con a)+b)+c): 133 ms ya van dentro de "recepción+150 ms"; el presupuesto de software+red de salida es ~150 ms − (b + medio RTT ≈ 30 ms) ≈ holgura ~100 ms **[estimación, NO medida end-to-end]**.
    La cota real no es nuestro software sino si el tomador reacciona más rápido que nosotros (misma geografía que Binance → sus 133 ms también) + 150 ms: eso lo dice L2 + x/b (libro5 + bnreg), no más optimización.
Mejoras viables SIN tocar ejecutores con dinero real:
 1. Medir en lugar de mutar: descomponer recv−E por símbolo/hora (ya sale gratis de `binance_integridad`); sondeo de 60 s por endpoint público (stream.binance.com:9443, :443, data-stream.binance.vision)
    para ver si alguno baja de 133 ms [NO VERIFICADO que lo haya]. Comparar con las bolsas de `multivenue_ms` (bybit/coinbase/kraken/bitstamp, ya grabadas, con su E) por si alguna ve el movimiento antes que Binance en este VPS.
 2. Para el futuro ejecutor (requiere OK + /code-review, fuera de este diseño): sesión HTTP/2 caliente y keep-alive con ping, DNS fijado, cabeceras HMAC precalculadas, DELETE en lote (`/orders`) por mercado,
    lector Binance en el mismo proceso/loop que decide (sin cola), uvloop, GC en pausa en el camino crítico, cancelar ANTES de rearmar. Todo [NO medido aquí].
 3. Registrar en ms nuestra propia latencia de cancelación cuando exista un ejecutor real (hash EIP-712 ↔ orderID permite casar acuse con eco del WS).

## 7. Riesgos, pruebas de aceptación, aprobaciones
Riesgos: (R1) doble escritor → lock + centinela; (R2) deriva de formato → test T2; (R3) bnreg muere por OOM → reserva en el hijo ≤5 s + watchdog 120 s + choom opcional; (R4) perder el histórico ms
en memoria de observadores en el traspaso (igual que un restart_ram; 1 vez); (R5) lectores que asuman fichero único [NO VERIFICADO los 45]; (R6) +1 proceso (≈3-5 % de un núcleo; load5 hoy 7,5 en 8 núcleos → asumible pero es presupuesto);
(R7) Binance corta el socket a las 24 h (marca planificada); (R8) edición de libro_estado_ws.py dispara cascada del watchdog si el traspaso no es inmediato → script + tick.
Pruebas de aceptación:
 T1 unitaria (dev): dos procesos, un solo escritor con el lock; centinela on/off; reserva del hijo.
 T2 compatibilidad: tomar 1 hora real de maker_ms, separar x/b a un fichero aparte y comparar salida idéntica de `analisis_maker_cancelacion_binance.leer`, `vigia_5m_barato_forward.procesar` (copia en dev, sin tocar el congelado),
    `extraer_registro_5m_barato` y una lectura pandas de `m15_ms_cache`.
 T3 sombra 24 h en dev (salida a scratch, NO a datalogs, con el hijo actual escribiendo en paralelo): cobertura de bnreg ≥99,9 % de las filas x del hijo por (T,sym,p,q,m); recv−recv mediana ≤5 ms; ids contiguos.
 T4 en dev, restart simulado: lanzar `libro_estado_ws.py` (modo padre con LIBRO_WS_REGISTRO_DIR/LIBRO5_DIR de scratch) + bnreg; matar el padre -9 y relanzar 3 veces: **ningún hueco >10 s en la unión de símbolos de bnreg**, y con bnreg parado el hijo asume en ≤5 s.
 T5 en prod, 1er restart_ram posterior (22:20Z): hueco Binance ≤10 s; 24 h de `binance_integridad` sin faltantes salvo marcas; max inter-llegada de la unión por hora UTC ≤10 s en 24/24 h ("H1" = hora UTC).
Qué necesita /code-review (medium) y OK de Javi:
 - /code-review: `binance_registro_ms.py` (reconexión, flock, cola, gz), parche de libro_estado_ws.py (módulo compartido del motor de observadores), script de traspaso, cambios de watchdog/verify_deploy/vigía.
 - OK de Javi (decisiones, no auto-aprobables): proceso nuevo permanente; reinicio de observadores (pérdida de histórico ms); `choom` opcional; fase 2 del lado Polymarket; cualquier medida con órdenes reales (§6c).
Entregables posteriores (execution-engineer, tras OK): módulo + tests T1/T2/T4 en dev; script de traspaso; parche; registros; piloto §5.3.
