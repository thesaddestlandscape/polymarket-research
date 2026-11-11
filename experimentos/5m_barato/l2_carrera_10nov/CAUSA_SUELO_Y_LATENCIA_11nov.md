# CAUSA DEL SUELO DE ~38 ms, OFFSET exchange-local y LATENCIA DE ORDENES (11-Nov-2026, mision 5m barato, programa L2 V2)
Solo lectura de datos + sondeos GET publicos inofensivos (ningun POST/DELETE, ninguna orden, sin autenticacion, sin claves reales, sin tocar procesos/crons/dev/main live/PREREG/ADDENDUM). Todo con `nice -n 19 ionice -c3`, `ulimit -v 1500000`, un fichero cada vez, nunca un dia entero en memoria (se transmite con `zcat | awk` y se guardan histogramas).
Scripts, histogramas y sondeos en `causa_suelo_11nov/` (los scripts conservan las rutas del scratchpad de la sesion: ajustar `SP=`/rutas para reproducir). Definicion usada: `lag = rx - ex` (ms) = hora de recepcion local menos sello del exchange (`t_ev`, columna 2 de las filas `q` del registro ms); "suelo" = p5 (o p1) del lag. Contrato de relojes: CONTRATO_RELOJES.md; no se modifica nada congelado.

## 0. Veredictos (fail loud)
| Tarea | Veredicto |
|---|---|
| 1. Causa del suelo ~38-40 ms de octubre | **Hipotesis mas probable con evidencia, NO causa verificada.** El suelo NO lo causo el Rescale (22-Oct 09:58Z: 37 -> 38 ms, sin efecto). Fue un escalon de +20 ms (19 -> 40 ms) de TODAS las conexiones de datos de mercado de Polymarket a la vez, el 17-Oct a las 08:35Z, que duro hasta el 27-Oct ~11:50Z (9,1 dias, con tramos rapidos intermitentes los dias 17 y 27). No coincide con ningun evento local (reinicio del lector, deploy, reloj, kernel, MTU/IP) y el control de Binance y el RTT REST de ordenes no se movieron: la causa esta aguas arriba del lector, en el camino/pasarela WS de datos de mercado de Polymarket. Que sea red real (+20 ms de ida) o un sello anterior en el servidor es **no determinable** con estos datos. |
| 2. Offset exchange<->local | **Medido con anclas simetricas, con incertidumbre.** CLOB REST (`GET /time`, tick-edge, n=400): servidor - local = **+4 ms, intervalo estadistico [+2, +7] ms**; Binance REST (`serverTime`, n=150): **+1,8 ms (1,3 a 2,8 en los 30 de menor RTT)**; chrony: reloj local a +0,05 ms de NTP (RMS 0,12 ms). Cota dura por asimetria de ruta = RTT/2 (CLOB +-24 ms; Binance +-124 ms), cota realista ~+-5 ms. No se puede afirmar el offset del host que sella el WS (no tiene por que ser el del REST). |
| 3. Latencia de ordenes | **Informativo + palancas.** Red hasta el borde de Cloudflare 1,2-3 ms; el resto del RTT (~48-55 ms en un GET trivial) es Cloudflare->origen. POST de orden de B (n=3.796) p10 66-76 ms, p50 75-110; cancelacion p50 60-70; alta Sonda p50 117 (n=9). Palancas medidas: precarga de tick/neg_risk por token (+15-32 ms en la 1a orden de cada token de B; en PRECIERRE real la fase "firma" tarda p50 28,8 ms frente a 3,4 ms de computo puro, n=50), lectura REST del libro en el camino critico de PRECIERRE (p50 78,5 ms), prioridad/aislamiento de CPU (POST p50 110 -> 75 ms al bajar la carga), IPv4 forzado (-2,0 ms pareado, n=300). Keep-alive: sin penalizacion medible hasta 300 s de inactividad (3.3). Ninguna se implementa aqui. |

## 1. Causa del suelo
### 1.1 Datos y metodo
- Fuente principal: `/mnt/HC_Volume_106538179/m5_registro/m5_registro_<D>.csv.gz` (filas `q` = top del libro: `q,t_ex,token,bid,ask,szb,sza,t_rx`; extraido del registro ms por `extraer_registro_5m_barato`; mercados 5m) y `m15_registro` (15m/60m, conexiones distintas). Serie diaria con las primeras 8 M de lineas de cada fichero (7,0-7,7 M filas q por dia; cubre 4-7 h del dia, o el dia entero en 24-Oct, 31-Oct, 03-Nov, 10-Nov; las demas horas no se muestrearon). Lag `rx - ex` en histograma de 1 ms (tope 2.000 ms).
- Contrastes independientes: `libro5_tx` (logger de prints con hash de tx: `t_ev` exchange y `recv` local; 24-Oct..09-Nov, 150.000 primeras filas por fichero y ficheros completos el 26-27 Oct), filas `x` de Binance del mismo registro (`recv - T`), `maker_ms` crudo del 11-Nov, y las calibraciones ya hechas (`out_v2/calib_relojes_*.json`, extractor v2 identico al v1 en 18.255.998 filas).
- Limite: no hay filas crudas anteriores al 15-Oct muestreadas y los `maker_ms` de octubre estan rotados/enlazados al volumen; la unica serie diaria larga es `m5_registro`.

### 1.2 Suelo por dia (q; p5 / p50 en ms; % lag<=28 ms = modo rapido; % 29-60 ms = modo lento; control Binance = p5 / p50 de `recv - T` en filas x)
| dia | n filas q | horas UTC cubiertas | p5 / p50 | % <=28 | % 29-60 | Binance x p5 / p50 |
|---|---|---|---|---|---|---|
| 15-Oct | 7,0 M | 00-04 | 20 / 29 | 49 | 46 | 130 / 138 |
| 16-Oct | 7,6 M | 00-04 | 21 / 25 | 54 | 41 | 128 / 137 |
| 17-Oct | 7,5 M | 00-06 (+ dia entero en 5 min) | 19 / 21 | 85 | 9 | 126 / 136 |
| 18-Oct | 7,6 M | 00-06 | **40 / 43** | 0 | 91 | 131 / 135 |
| 19-Oct | 7,5 M | 00-04 | 40 / 44 | 0 | 86 | 131 / 136 |
| 20-Oct | 7,6 M | 09-14 | 40 / 43 | 0 | 79 | 130 / 139 |
| 21-Oct | 7,7 M | 00-04 (+ dia entero en 5 min) | 40 / 42 | 0 | 86 | 130 / 137 |
| 22-Oct | 7,3 M | 10-14 (+ dia entero en 5 min) | 38 / 41 | 0 | 86 | 127 / 130 |
| 23-Oct | 7,5 M | 00-05 | 37 / 40 | 4 | 88 | 128 / 133 |
| 24-Oct | 7,5 M | 00-23 | 37 / 43 | 2 | 61 | 127 / 134 |
| 25-Oct | 7,5 M | 00-07 | 37 / 40 | 0 | 93 | 127 / 133 |
| 26-Oct | 7,4 M | 00-04 | 37 / 40 | 1 | 92 | 128 / 135 |
| 27-Oct | 7,4 M | 00-05 | 18 / 39 | 10 | 83 | 127 / 133 |
| 28-Oct | 7,4 M | 00-06 | 18 / 20 | 89 | 6 | 138 / 140 |
| 29-Oct | 7,3 M | 00-05 | 18 / 20 | 88 | 8 | 128 / 131 |
| 30-Oct | 6,5 M | 00-03 | 15 / 18 | 87 | 10 | 127 / 130 |
| 31-Oct | 7,5 M | 00-23 | 15 / 17 | 91 | 6 | 126 / 132 |
| 01-Nov | 7,5 M | 09-15 | 15 / 17 | 92 | 5 | 123 / 130 |
| 02-Nov | 7,5 M | 00-05 | 15 / 17 | 92 | 6 | 126 / 132 |
| 03-Nov | 7,4 M | 00-23 | 15 / 17 | 91 | 6 | 127 / 132 |
| 04-Nov | 7,2 M | 00-04 | 16 / 17 | 90 | 7 | 127 / 133 |
| 05-Nov | 7,5 M | 00-05 | 16 / 18 | 89 | 9 | 128 / 133 |
| 06-Nov | 7,4 M | 00-04 | 16 / 18 | 91 | 6 | 128 / 135 |
| 07-Nov | 7,5 M | 00-07 | 15 / 17 | 93 | 5 | 128 / 134 |
| 08-Nov | 7,6 M | 00-07 | 16 / 17 | 92 | 6 | 127 / 131 |
| 09-Nov | 7,3 M | 00-04 | 16 / 18 | 89 | 8 | 128 / 133 |
| 10-Nov | 5,4 M | 00-23 | 15 / 18 | 91 | 7 | 128 / 134 |
| 11-Nov | 4,9 M (00-02Z) y 1,9 M (09-10Z) | 00-02, 09-10 | 16 / 18 (ambos) | - | - | sin x (Binance ya va por `bnreg`) |
Fuente: `causa_suelo_11nov/datos/lag_<D>_pre.txt` + `an_lag.py`/`an_modo.py`. El 11-Nov a las 09-10Z con load 22 sobre 8 vCPU el suelo sigue en 16 ms (n=1,9 M): la carga actual no mueve el suelo. El control propio de B 20-22 Oct (n=4.220 / 7.110 / 11.389 filas q, `anclas_breal_*.json`) da p5 39 / 39 / 37: lo mismo. Nota: `m5_registro` no es cronologico (tramos unidos); el prefijo de 8 M lineas cubre horas distintas segun el dia (columna "horas"). Las de la tabla sin cobertura completa son una muestra de esas horas, no del dia.

### 1.3 Fecha exacta de los cambios de regimen (resolucion 1-5 min)
| Cuando (UTC) | Cambio | Evidencia |
|---|---|---|
| **17-Oct 08:35** | suelo 19 -> 40 ms, en el mismo minuto en `m5_registro` (n=13-20 k filas/min; 08:34 p5=19 y 81 % <=28 ms; 08:36 p5=39 y 0 %) y en `m15_registro` (conexiones distintas: 08:35 23 % <=28 ms; 08:36 p5=40, 0 %) | `datos/win_1017.txt`, `datos/win15_1017.txt` |
| 17-Oct 09:52-10:05 | 13 min de mezcla (28-82 % de filas rapidas por minuto) y vuelta a 40 | idem |
| 21-Oct tarde | deriva suave 39-40 -> 37-38 ms (antes del Rescale) | `datos/bin5_q_2026-10-21.txt` |
| **22-Oct 09:58:31** (arranque tras el Rescale, `uptime -s`) | **sin efecto**: 04:00-09:55 p5 37, p50 40, p90 74 (n=9,7 M); 10:05-15:00 p5 38, p50 41, p90 79 (n=7,6 M); 15:00-24:00 37 / 40 / 67 (n=13,1 M) | `datos/bin5_q_2026-10-22.txt` |
| **27-Oct 08:30-11:50** | 08:30-09:05 inestable; 09:05-09:40 rapido (18); 09:40-11:50 lento (38-40); desde 11:50 rapido estable (20-22) | `libro5_tx` por bines de 5 min (n=539-3.530 por bin); coherente con `m5_registro` del 27-Oct (p5 18, p50 39, 10 % rapido en 00-05Z) |
| 29-30 Oct | 20-22 -> 17-18 -> 15-16 ms (dos escalones de 2-3 ms) | `libro5_tx` (29-Oct pid 3296888 p5=15) y tabla 1.2 |
La premisa "37-39 ms el 20-22 Oct" es un trozo de un regimen de 9,1 dias (17-Oct 08:35 a 27-Oct ~11:50), no un fenomeno de esos tres dias.

### 1.4 Contraste de cada hipotesis
| Hipotesis | Evidencia | Estado |
|---|---|---|
| Rescale del VPS (22-Oct 09:58Z, 4 vCPU/7,6 GB -> 8 vCPU/15 GB) | El escalon es 5 dias ANTES; en el Rescale el suelo pasa de 37 a 38 ms y p50/p90 no mejoran (74 -> 79). Si mejoro la cola de las ordenes (3.1), no el suelo del feed | **Descartada** como causa del suelo |
| Saturacion de CPU local | Carga 07:57Z (`salud_sistema_historico.json`): ratio5 1,6-5,1 sobre 4 vCPU (15-22 Oct) frente a 0,4-0,8 sobre 8 (23-Oct..); hoy, con ratio ~2,8, el suelo es 16 ms; el escalon es seco (en un minuto) y simultaneo en todas las conexiones, no gradual; el nice -10 del lector (commit 17-Oct 22:15Z, reinicio 22:16:44Z) llego 14 h DESPUES del escalon | Descartada para el escalon (la CPU si infla p50/p90: 15-16 Oct p50 25-29 ms) |
| Reinicio del lector WS / observadores | `watchdog.log`: reinicios de observadores el 17-Oct a las 10:32:22Z y 22:16:44Z; `guard_ram`: 09:10, 12:10, 18:05; NINGUNO a las 08:35, 09:52 ni 10:05; el 27-Oct no hay reinicio entre 08:30 y 11:50 (el pid 1965189 de `libro5_tx` cruza los cambios) | Descartada |
| Version del extractor | tres tuberias distintas muestran lo mismo (`m5_registro`, `m15_registro`, `libro5_tx`) y v2 reproduce v1 en 18.255.998 filas | Descartada |
| Reloj local / NTP (salto) | un salto de +20 ms en el reloj local moveria tambien el control de Binance (`recv - T` de filas x): p5 131 -> 125-126 el 17-Oct (-5 ms), p50 134 sin cambio; chrony no guarda logs de octubre, el control lo excluye de forma indirecta | Descartada (indirecta) |
| Kernel | corre 7.0.0-38 desde el arranque del 22-Oct 09:58:31Z; el 7.0.0-42 se instalo el 15-Oct pero no se arranco (`/boot`, `apt/history.log`) | Descartada para el 17-Oct (kernel previo al 22-Oct no verificable al 100 %) |
| MTU / IP local | eth0 mtu 1500, IPv4 37.27.249.72, IPv6 2a01:4f9:c014:df39::1; sin historial de cambios (journal solo desde el 31-Oct, dmesg desde el arranque) | No verificable; improbable (no explica un cambio simultaneo y sincronizado, ni su vuelta el 27-Oct) |
| Camino de ORDENES (REST) | RTT de cancelacion de B (n=3.737, DELETE) p10 55-60 / p50 60-70 ms en el regimen lento frente a RTT de cancelacion de Sonda el 04-Nov (rapido) 56, 56, 61, 66 ms (n=4) y GET /time 48-55 hoy: el REST de ordenes NO se movio ~+40 ms de RTT cuando el feed WS si se movio +20 ms de ida | Indica que no es un cambio general de la ruta Hetzner->Cloudflare; apunta a la distribucion WS de datos de mercado |
| Cambio del feed / Polymarket / Cloudflare | simultaneo en 5m y 15m (conexiones distintas), con hora exacta, reversible el 27-Oct tras 9,1 dias y con escalones de 2-3 ms; el changelog oficial (`vigia_actualizaciones_polymarket.log`) no anuncia cambios el 17-18 Oct; el feed publico de incidentes de Cloudflare solo cubre desde el 27-Oct (incidentes el 27-Oct a las 11:38 y 12:28Z, sin relacion demostrable con el cambio de las 11:50) | **Hipotesis mas probable** (externa); no verificable |

### 1.5 Veredicto 1 y alcance
- Hipotesis mas probable con evidencia: cambio externo en la distribucion WS de datos de mercado de Polymarket (pasarela, enrutado o sellado; coincide en 5m y 15m, no en Binance ni en el REST de ordenes). Sin acceso a Polymarket/Cloudflare, **la causa exacta no es determinable**. No se puede separar "+20 ms de red real" de "sello del servidor 20 ms anterior".
- Consecuencias para el programa: el desfase rx-ex NO es estacionario entre regimenes (~16-18 ms hoy; ~38-43 ms del 17-Oct 08:35 al 27-Oct ~11:50). Toda simulacion con datos de ese tramo (anclas B 20-23 Oct, `libro5_ms` del 26-27 Oct, dias del extractor del 26-27 Oct) debe usar la constante de SU epoca o el lag por evento (la regla R7 del contrato ya lo pide). El % de filas rapidas por dia (tabla 1.2) es el indicador de epoca.
- Pendiente barato (no implementado): vigia del suelo (p5 rx-ex por hora) para detectar el siguiente escalon en el momento.

## 2. Offset real exchange <-> local
### 2.1 Metodo y datos
Una conexion TLS keep-alive por host, peticiones espaciadas con fase aleatoria, tiempos con `time.time_ns()` (reloj local, chrony). `GET https://clob.polymarket.com/time` devuelve segundos enteros del servidor (`cf-cache-status: DYNAMIC`, `cf-ray ...-HEL`: llega al origen); `GET https://api.binance.com/api/v3/time` devuelve `serverTime` en ms. Punto medio local `m = (t_envio + t_primer_byte) / 2`.
- Binance (directo): offset = serverTime - m. n=150, RTT min 248,6 / p50 251,5 ms; offset de los 30 de menor RTT: mediana +1,8 ms (1,3 a 2,8). Cota estricta +-RTT/2 = +-124 ms; la dispersion entre las muestras de menor RTT es 1,5 ms.
- CLOB (tick-edge, solo hay segundos): para cada muestra S = floor(reloj_servidor); se busca el theta (paso 1 ms) que minimiza los desajustes `floor(m + theta) != S`; muestras filtradas al 50 % de menor RTT (n=200, 0 desajustes): theta = **+4,5 ms, region consistente [+2, +7]**; con las 400 muestras [+2, +6]; con el 25 % de menor RTT [+2, +18] (menos muestras). RTT keep-alive HTTP/1.1: min 48,0, p1 48,3, p10 51,0, p50 55,4, p90 62,4, p99 131,9 ms (n=400). Cota estricta +-RTT/2 = +-24 ms.
- Validacion del metodo: aplicado a Binance con el serverTime truncado a segundos da [-18, +10] ms (n=150, mejor: centro -4), que contiene el valor directo +1,8 ms; el tick-edge es fiable a ~+-10 ms con RTT de 250 ms y mejor con 55 ms.
- chrony (11-Nov 09:49Z): reloj local 0,05 ms "fast" de NTP, last offset +0,12 ms, RMS 0,12 ms, skew 0,09 ppm, root delay 41 ms, root dispersion 1,4 ms (cota formal ~+-22 ms); las tres fuentes ps5 (seleccionadas) coinciden en 0,1 ms; las dos ps6 estan a -6,3 y -8,1 ms: la asimetria de ruta entre grupos de servidores NTP es de 6-8 ms, asi que el "0,2 ms" del contrato es offset RELATIVO a NTP, no error absoluto; el error absoluto realista del reloj local es ~+-5 ms.
- Consistencia cruzada: Binance WS (`recv - T` suelo 123-131 ms) ~ RTT/2 REST (124 ms) + 1,8 ms; el reloj local esta a ~2 ms del de Binance y a ~4 ms del del REST de Polymarket.

### 2.2 Resultado
- Offset (reloj servidor REST de Polymarket - reloj local) = **+4 ms, [+2, +7] estadistico, ~+-5 ms practico, +-24 ms cota dura (asimetria de ruta)**.
- Si el sello del WS vive en un host con el mismo reloj, el desfase rx-ex medido (suelo 15-16 ms hoy) = ida real - offset => **ida real ~20 ms** (16 + 4, +-5), frente a RTT/2 de /time = 24-27 ms (plausible: pasarela WS mas cerca que el origen REST). En el regimen lento (suelo 38-40) la ida seria ~43-44 ms.
- NO verificado: el offset del host que sella el WS (puede ser otro que el del REST), la etapa del pipeline donde se toma el sello (puede ser anterior a la salida), la asimetria de ruta real. Anclas propias: sello del canal de usuario menos sello publico = -1 ms (n=1, Sonda) y rx-ex del canal de usuario 15-28 ms = igual que el feed publico.

## 3. Latencia de nuestras ordenes (informativo)
### 3.1 Descomposicion del camino VPS -> CLOB (todo medido en lectura; ninguna orden)
| Tramo | Valor | Fuente / n |
|---|---|---|
| DNS (stub local) | 0,5-1,3 ms; con cliente reutilizado = 0 | `curl -w`, n=6 |
| ICMP VPS -> borde Cloudflare (HEL) | min 1,2-1,5 ms (mtr, 10 paquetes: media 5,5, max 14); IPv4 e IPv6 al mismo colo (`cf-ray ...-HEL`) | ping/mtr |
| TCP connect | 1,8-3,1 ms | `curl -w` n=6 |
| TLS 1.3 (tras TCP) | +6-10 ms (conexion completa python: 7,4 ms) | `curl -w`, `probe_time` |
| GET trivial con conexion caliente (HTTP/1.1) | p50 55,4 (min 48,0; p90 62,4; p99 131,9) | n=400 |
| Idem HTTP/2 (httpx, como `py-clob-client`) | p50 56,2 (defecto, IPv6) / 53,9 (IPv4 forzado) / 55,2 (IPv6 forzado); min 46,6-48,7 | n=150 cada una |
| A/B intercalado IPv4 vs IPv6 (HTTP/2, 2 conexiones, orden aleatorio) | IPv4 p50 53,1 (p10 48,7 / p90 58,5) frente a IPv6 p50 55,4 (50,8 / 60,6); diferencia pareada mediana +2,0 ms para IPv6 (IC90 bootstrap 1,4 a 2,8) | n=300 pares, un solo momento del dia |
| => Cloudflare -> origen -> Cloudflare | ~46-54 ms (RTT total menos ~2-3 ms al borde); suelo duro de cualquier peticion | por diferencia |
| Firma EIP-712 `build_order` (clave aleatoria desechable, solo computo) | p50 3,4 ms (min 3,2; max 4,6) | `bench_sign.py`, n=60 |
| POST de orden de B real, `t_ret - t_call0` (firma + red + origen) | p10 66-76 / p50 75-110 / p90 140-318 segun dia (n=405/1.121/1.746/524 el 20/21/22/23-Oct) | `experimento_h47_B_ledger.jsonl` (3.796 post_lat) |
| Cancelacion de B real (DELETE) | p10 55-60 / p50 60-70 / p90 116-169 (n=392/1.096/1.725/524) | idem (cancel_lat ok) |
| Alta de Sonda1 04-Nov, RTT POST | p50 117, min 64, max 232 (n=9) | `anclas_sonda_2026-11-04.json` |
| Sello exchange del alta - envio | B Oct: p50 ~56 (48-113, n=9); Sonda Nov: p50 79 (42-175, n=9) | `anclas_*.json` |
| Sello exchange de la cancelacion - envio | p50 35 (32-46, n=4) | Sonda |
| Ack - sello exchange | p50 31 (22-76, n=9) | Sonda |
Lectura: red pura hasta el exchange ~24-27 ms de ida (RTT/2 de /time), de la que solo ~1-2 ms es del VPS al borde. La cancelacion (DELETE) cuesta casi lo mismo que un GET (RTT 60-70 frente a 55): el procesado en el exchange de una cancelacion es ~5-15 ms. El alta tarda ~15-20 ms mas que la cancelacion en el mejor caso (p10 66-76 frente a 55-60: firma 3,4 ms + validacion/insercion) y su cola (p90 140-318) depende de la carga local y de la 1a orden de cada token. Sonda es una muestra pequena (n=9), con ordenes cada 25+ min: sin IC. De los 79 ms de la mediana de Sonda hasta el sello, ~27 son de ida de red y ~50 (18 en el mejor caso: 42 - 24) son tiempo en el exchange antes de sellar; la vuelta (ack - sello 31 ms) es otra ida de red (~24-27) + ~5. Esta descomposicion supone ruta simetrica: **no se pueden separar red y proceso al ms**; las cifras son compatibles, no una prueba.
- Efecto de la carga local en B: del 20 al 23-Oct (23-Oct = tras Rescale, 8 vCPU, ratio ~0,75 frente a 3-5 antes) POST p50 110 -> 96 -> 86 -> 75, p90 318 -> 277 -> 205 -> 140; cancelacion p50 70 -> 65 -> 66 -> 60, p90 169 -> 135 -> 132 -> 116. Independiente del suelo del feed (mismo suelo de ~40 ms los 4 dias). Ojo: 23-Oct tiene n=524 y mezcla otros efectos del mismo dia.
- `LAT_POST=68` del motor: coincide con p10-p50 de B, es conservador frente a Sonda (p50 117) y optimista en la mitad de los casos de Sonda (n=9); sin cambio propuesto (coherente con NOTA_A2).

### 3.2 Hallazgos sobre el envio (lectura del codigo y de CSV ya existentes)
- `py-clob-client` (v1) y `py_clob_client_v2` usan un `httpx.Client(http2=True)` global: conexion reutilizada, sin DNS/TCP/TLS por orden mientras siga viva. `create_order`/`create_market_order` hacen GET de `tick-size` (cache TTL 300 s por token), `neg-risk` (cache por token) y, en v1, `fee-rate` (v2: `version`) **si no estan en cache**: cada GET ~55 ms. Nuestros tokens son nuevos cada 5/15 min.
- Dato medido en B: la primera orden de cada token (n=364 de 3.796) tarda mas: p50 138 / 133 / 105 / 89 ms frente a 106 / 93 / 85 / 74 ms del resto los dias 20/21/22/23-Oct (diferencia +15 a +32 ms). En PRECIERRE real la fase de firma (`t_firma_ms` de `data/shadow/resolution_sniper_precierre_executor_v2.csv`, disparos reales desde 01-Oct, n=50): p10 10,8 / p50 28,8 / p90 62,9 ms; 34 de 50 por encima de 20 ms, 15 por encima de 40 y un maximo de 312 ms, frente a 6-8 ms en los 15 intentos dry-run y 3,4 ms de computo puro: ~20-55 ms por orden son, muy probablemente, GET de cache fria dentro de la firma (inferencia por la distribucion, no leida de una traza).
- Camino critico de PRECIERRE real (n=50): lectura del libro REST `t_lectura_ms` p50 78,5 (p10 48,9; p90 164,3), firma 28,8, total p50 409 ms (p10 334; p90 527); el POST FOK paga ademas el retraso del tomador (~145 ms) y el RTT.
- Sonda1 ya precarga tick y neg_risk (`precargar` en `sonda1.py`). `experimento_maker_h47.py` (dev) y el ejecutor de PRECIERRE (main) no mostraron una precarga equivalente en lo que se leyo; verificarlo es tarea de quien implemente.

### 3.3 Sondeo de inactividad (conexion persistente HTTP/1.1 frente a conexion nueva), GET /time
33 peticiones persistentes (huecos 0,3 s a 300 s; 2-3 por hueco), cada una seguida de una conexion nueva. Persistente: p50 53,7 ms; solo 2 de 33 por encima de 80 ms (143 ms tras 2 s y 128 ms tras 60 s: sin relacion con el hueco; con 90, 120, 180 y 240 s: 48-56 ms). Ningun corte de la conexion en 300 s. Conexion nueva (connect+TLS 5-10 ms, mediana 7,6; primera peticion p50 55,4). Tras 300 s (n=2): persistente 74 y 63 ms y connect+TLS mediana 22,7 ms: indicio de enfriamiento a ~5 min, sin n. Limite: mi propio trafico (la conexion nueva tras cada hueco) mantenia caliente el pool de Cloudflare->origen, asi que un enfriamiento real con inactividad de verdad >5 min no queda medido. `idle_probe.json`.

### 3.4 Palancas (informativas; sin implementar aqui)
1. **Precargar por mercado tick-size, neg-risk (y fee-rate/version) al conocer el token, antes de t0**, y pasar `PartialCreateOrderOptions(tick_size, neg_risk)` a `create_order`: ahorro medido 15-32 ms en B (primeras ordenes, n=364) y ~20-55 ms en la firma de PRECIERRE real (n=50). Sin riesgo de precio; fail-closed ya existe en `precargar` de Sonda.
2. **Sacar la lectura REST del libro (p50 78,5 ms) del camino critico de PRECIERRE** si el libro en memoria del WS (`libro_estado_ws`) es lo bastante fresco: requiere decision de diseno (las trampas dicen que un libro REST leido ~1,5 s antes no acota la liquidez; el WS tiene su propio retraso de 16-18 ms hoy). No es una mejora gratuita.
3. **Prioridad/aislamiento de CPU del proceso con envio real** (nice negativo o afinidad de nucleo) y analisis pesados fuera de 06-09Z: la carga local explica ~35 ms de p50 y ~180 ms de p90 de la POST de B entre el 20 y el 23-Oct (n=3.796). Hoy load 10-22 sobre 8 vCPU.
4. **IPv4 forzado** (el defecto es IPv6): -2,0 ms pareados (IC90 1,4-2,8; n=300 pares; un solo momento del dia; mismo colo HEL). Pequeno pero medible; verificar que no hay efectos laterales (geobloqueo, familia de la conexion de otros clientes) antes de aplicar.
5. **Mantener caliente la ruta** solo si un sondeo con inactividad real >5 min muestra penalizacion (3.3: no demostrado): un `GET /time` barato por la misma conexion.
6. Firmar con antelacion ordenes de limite conocido: ahorra como maximo 3,4 ms; solo merece la pena en FOK de PRECIERRE con precio fijado de antemano.
7. No mejorable desde aqui: ~46-54 ms de Cloudflare->origen (el origen esta a ~25 ms de ida del borde HEL), el taker delay de ~145 ms de FOK/FAK y los 16-18 ms del feed. Mover el VPS esta descartado por Javi.
Las palancas 1-4 las puede implementar `cheap5m-execution-engineer` con `/code-review` obligatorio (tocan ejecutores con dinero real o su arnes) y OK de Javi antes de cualquier despliegue.

## 4. Que NO se pudo verificar (fail loud)
- La causa exacta del escalon de +20 ms del 17-Oct y de su vuelta del 27-Oct (sin datos del lado Polymarket/Cloudflare, sin logs de chrony/journal anteriores al 31-Oct, sin traceroute historico). Cobertura horaria parcial por dia en `m5_registro` (4-7 h; dia entero solo el 24-Oct, 31-Oct, 03-Nov y 10-Nov; 17, 21 y 22-Oct en bines de 5 min).
- Series anteriores al 15-Oct (no muestreadas) y no se cubre el dia 22-Oct 00:00-09:58 con prefijo; si con bines de 5 min.
- Offset exacto del host que sella el WS; asimetria real de la ruta; etapa del pipeline del sello; si el escalon es red real o sello.
- Division red/proceso en ms de la alta de orden (supone ruta simetrica); anclas propias n=9 (Sonda) + 9 (B publica) + 4 (cancelaciones): sin IC.
- La causa de los 20-55 ms de la firma en PRECIERRE real es una inferencia por distribucion.
- El ledger de B solo cubre 20-23 Oct (3.796 POST): no hay POST reales de B en el regimen rapido; Sonda (9 altas) es la unica ancla de alta del regimen actual.
- Efecto de inactividad >5 min en la ruta Cloudflare->origen (el propio sondeo la mantenia caliente) y estabilidad horaria del A/B IPv4/IPv6 (un solo momento).

## 5. Siguiente especialista
- `cheap5m-execution-engineer` (palancas 1-4; `/code-review` obligatorio al tocar ejecutores/arnes y OK de Javi): medir antes/despues con las mismas anclas (`t_firma_ms`, `post_lat`, ack-sello), sin tocar lo congelado.
- `cheap5m-market-data-integrity` (esta area): vigia barato del suelo rx-ex por hora (p5 por tipo de mensaje; alerta si sube o baja >=5 ms) y etiqueta de "epoca de reloj" por dia para los simuladores (17-Oct 08:35 a 27-Oct ~11:50 = lento).
- `cheap5m-statistical-validator`: comprobar que ninguna conclusion del programa L2 mezcle epocas (20-23 Oct y 26-27 Oct = lento; 03-09 Nov = rapido).

## 6. Ficheros (todos bajo causa_suelo_11nov/)
`lag2.awk` `lag3.awk` `lag3b.awk` `win.awk` `win15.awk` `run_lag.sh` (histogramas de lag en streaming), `an_lag.py` `an_modo.py` `an_bin5.py` `an_hour.py` (tablas), `probe_time.py` `an_offset.py` (offset), `probe_idle.py` `probe_h2.py` `probe_ab.py` (latencia), `an_ledger.py` (POST/cancel de B), `bench_sign.py` (firma); `datos/` con histogramas, `pt_clob_time.json`, `pt_bn_time.json` (n=400/150) e `idle_probe.json`.
