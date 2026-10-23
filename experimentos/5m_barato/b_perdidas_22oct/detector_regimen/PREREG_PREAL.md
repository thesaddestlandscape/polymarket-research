# PREREG P-REAL (23-Oct-2026 ~08:10Z) - H1 de R-TEND con PRECIO EJECUTABLE REAL
Congelado ANTES de extraer ningun precio real ni calcular ningun estadistico con ellos. Lo anadido despues va marcado POST-HOC. `sha256sum -c PREREG_PREAL.sha256`.
Solo lectura: sin ordenes, sin claves, B/ejecutores/modulos compartidos/crontab intactos. Unico acceso de red permitido: GET publico de gamma-api (`closed=true`) para desenlaces que falten en las cachés locales.
Contexto: R-TEND (PREREG_RTEND.md sha 0cbe5e44, enmienda 6d90c029) hallo Delta(CON-CONTRA) < 0 con precio de MODELO q (proxy). Aqui se repite con ASK/BID/PRINT reales del CLOB.

## 1. Fuentes (todas declaradas; lo que no se use se dice en el informe)
- F-A `m5_registro_D.csv.gz` (volumen `/mnt/HC_Volume_106538179/m5_registro/`, 05..21-Oct, 17 dias; filas k/q/t del registro ms): `q` = (t_exchange_ms, token, bid, ask, bidsz, asksz, recepcion_ms), `t` = prints del WS del CLOB (precio, side del TOMADOR, size, recepcion), `k` = mapa token -> (moneda, marco, id gamma, cierre ISO, lado YES/NO; YES=Up). SOLO tokens marco 5min. Reloj de decision = RECEPCION (nunca el timestamp del WS, trampa del CLAUDE.md). 22-Oct: `.tmp` fallido (zlib); 22/23-Oct solo si se recupera de `maker_ms_*` crudo (mismo formato) y entonces se etiqueta forward=descriptivo.
- F-B firehose `polymarket_activity` 03..22-Oct y on-chain `m5_onchain`: SOLO para auditar F-A (cobertura de prints, precio del primer tomador); NO decide (firehose = 2 filas por casacion; ts 1 s; on-chain = bloque ~2,4 s tarde).
- F-C Jon-Becker `/root/jonbecker` 18-Dic..27-Ene: contiene solo `markets` (desenlaces), `blocks` truncado y agregados `coinflip_*` (precios del arranque de ventana, no de T=180). Los trades crudos se borraron el 06-Jul-2026. => NO hay precios de 5m en F-C. Se declara DATA_BLOCKED para precios; recuperarlos exige re-descargar 36 GB (no se hace aqui).
- F-D `prices-history` CLOB: NO se usa (precio medio: trampa documentada; sin utilidad a T=180).
- Regimen/rpre/R: `datos/ventanas_bookticker.csv.gz` (bookTicker de Binance, mismas funciones `regimen_lib`, t_o = tmin*60). Proxy con precio de modelo: `datos/panel_bookticker.csv.gz` (T=180, q) y `datos/panel_y2025.csv.gz` (349 d).
- Desenlace: OFICIAL gamma `closed=true` (cachés `maker_ms_desenlaces_cache.json` + GET gamma para los ids que falten). Up=YES. Unidad sin desenlace = missing (se cuenta, no se imputa). Cobertura exigida >=99 % de las unidades del analisis primario; si <97 % el veredicto es DATA_BLOCKED.

## 2. Estado del libro en la decision (SIN look-ahead)
t_o = cierre - 300 s; decision t_dec = t_o + T con T=180 s (primaria) o 120 s (sensibilidad). Estado = ULTIMO `q` del token con recepcion <= t_dec + lag; lag primario 250 ms (tomador casado medido ~215 ms F1), sensibilidades 0 y 1000 ms. Se guarda edad = t_dec+lag - recepcion. Mercado "vivo" si algun token de la pareja (Up/Down) tiene un `q` con edad <= 30 s; si no, la ventana se excluye y se cuenta (feed caido, NO precio 0). Se descartan libros cruzados (bid > ask) y ask fuera de (0,1); bid ausente = missing (no 0). Print real = primer `t` BUY (tomador compra) del token con recepcion en [t_dec+lag, t_dec+lag+30 s]; sin print = missing.
Aviso de semantica: el `side` de `t` se asume del tomador (CLOB last_trade_price); se audita en F-B (una muestra de dias) y se reporta; si la auditoria lo desmiente, los resultados "print" quedan descartados.

## 3. Unidades
- U1 (PRIMARIA, ejecutable): (moneda, t_o, token Up|Down) con ask en [0,10, 0,30) en el estado de la decision (T=180, lag 250), estado vivo y desenlace conocido. Monedas primarias ETH, SOL, XRP (las de B); replicas BTC, BNB, DOGE (por separado, no deciden).
- U2 (PAREADA, calibracion): las unidades del proxy (`panel_bookticker`, T=180, q en [0,10, 0,30), lado perdedor segun Binance) que tienen estado real del token perdedor. Sirve para comparar modelo vs real en las MISMAS unidades.
- CON/CONTRA: signo del lado (Up=+1, Down=-1) por rpre (bps, `ventanas_bookticker`): CON si signo*rpre >= 7,7; CONTRA si <= -7,7; NEUTRO resto (excluido de Delta). Umbral 7,7 fijo (W1); sin reoptimizar.
- Precio de compra y PnL por accion (1 accion): TOMADOR al ask: coste c = p(1+0,07(1-p)), pnl = gana - c (identico a `comision_cripto.pnl_por_euro`). BID (cota optimista de pujar en reposo, SIN condicionar al relleno, fee 0, rebate no sumado): coste = bid, pnl = gana - bid. PRINT: como tomador al precio del print. El EV es ponderado por EUR: Sum pnl / Sum coste.

## 4. Hipotesis y criterios (unica familia primaria; el resto es descriptivo)
H1-REAL: Delta_ask = EV_ask(CON) - EV_ask(CONTRA) en U1, monedas primarias agrupadas, T=180, lag 250. **H1 SE SOSTIENE AL ASK REAL ("SOSTENIDA")** solo si TODO: Delta<0; IC90 por CIERRE (bootstrap de cierres, 2.000, seed 20261026) con limite superior <0; placebo (permutar CON/CONTRA dentro de dia x moneda x cubo de ask 0,05, 1.000 perm., una cola) p<0,05; Delta<0 en >=60 % de los dias; Delta sin los 2 dias mas negativos sigue <0. "PARCIAL": Delta<0 e IC90 cierre sup<0 pero falla placebo o dias o el IC90 por DIA (bootstrap de dias) incluye 0. En otro caso "NO SOSTENIDA". Siempre se reporta ademas el IC90 por dia y se dice cual de los dos sostiene la conclusion.
H2-REAL (interaccion): I_R = Delta(TREND) - Delta(REVERT) en U1 (clases R de `ventanas_bookticker`; NA excluido). Una prueba, bootstrap de cierres (2.000) y de dias; "consistente" si I_R<0 e IC90 cierre sup<0; no se corrige por multiplicidad (se dice).
H3-REAL (regla en PnL total, descriptivo): para cada regla congelada R0 (saltar CON>=7,7), R1 (CON>=7,7 & TREND), R2 (CON>=7,7 & TREND|MIXTO): dP = -Sum pnl de las unidades saltadas (al ask, EUR por accion y por 5 acc); IC90 por cierre; placebo (mismo n de saltos al azar entre las CON>=7,7 dentro de dia x moneda x cubo); dias con dP>0; sin los 2 mejores dias; Bonferroni x3 (p<0,0167).
Replicas no decisorias: por moneda; T=120; lag 0/1000; precio bid y print; tercil de ask; cada mitad de los 17 dias (05-13 vs 14-21).

## 5. Calibracion modelo -> real y conversion de la proxy larga
C1: en U2, por tramo de q (0,05) x clase (CON/CONTRA/NEUTRO): n, q medio, ask medio, bid medio, tasa de acierto oficial, EV a precio de modelo (Sum(gana-q)/Sum q), EV al ask real (con fee), desvio ask-q.
C2: Delta_modelo vs Delta_ask en las MISMAS unidades U2 (diferencia pareada, IC90 por cierre).
C3 (EXPLORATORIO, extrapolacion): en `panel_y2025` (349 d, T=180, q en [0,10,0,30)), sustituir q por c_hat(tramo q, clase) = coste medio al ask (con fee) observado en U2; pnl_est = gana_proxy - c_hat. Delta_est(S_D) e I_R,est con IC90 por doble bootstrap (dias de S_D y dias de U2 para c_hat). Celdas con n<20 en U2 se agrupan por tramo de q. Supuestos que NO se verifican: que el mapa q->ask de oct-2026 vale para 2025 (el mercado no existia) y que el acierto proxy-oficial (97,6 %) es igual en CON y CONTRA. Etiqueta: EXPLORATORY. NO sustituye al ask real.

## 6. Cobertura y calidad (se reportan siempre)
Por dia: ventanas esperadas (288 x 6), con estado vivo, con cruzado, sin desenlace, unidades U1/U2, edad p50/p90 del `q`, % de prints. "Missing" nunca es 0.

## 7. Forward
Etiquetador diario `scripts/preal_extrae.py DIA` (estado de libro en la decision para TODA ventana x moneda x token, T in {120,180} x lag in {0,250,1000}, y primer print) -> `datalogs/preal/ask_t0_DIA.csv.gz` (retencion 400 d, ~pocos MB/dia, fuera de git), resolvedor `preal_resolver.py` (gamma closed=true), evaluador `preal_evaluar.py`. Cron propuesto, NO instalado (lo decide el chief). El gate forward replica el criterio SOSTENIDA de la seccion 4 con >=10 dias forward NUEVOS (desde 23-Oct) y n(CON)>=300.
