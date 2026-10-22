# H23 real: ensayo en seco, fecha estimada del gate y lista de verificacion para el OK (20-Oct-2026)

Paquete: `sha=602d5a2debb42cc0 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d contabilidad=0a41bc39108cdf82 shadow=43373dd4affe3181 kill=59437e2037321aed`
(`experimento_maker_h23.py --imprimir-sha` desde dev). NO se ha editado `experimento_maker_h23.py` ni `h23_regla.py`. Sin dinero real, sin commits, sin tocar screens.
Despliegue en dev: ver `DESPLIEGUE_DEV.md` (`desplegar_dev.sh`; 75 tests pasan en dev: `75 passed in 3.38s`).
Recursos: todo con `nice -n 19 ionice -c3`, `ulimit -v 3000000`, lanzado solo con load5<20 y MemAvailable>2,5 GB (el lanzador esperaba y arranco a las 18:19Z y 18:35Z), fuera de 06-09Z.

## 1. Ensayo en seco: que se hizo y salidas reales
Scripts (solo scratchpad, no tocan el paquete): `.../scratchpad/lanzar_seco.sh`, `forzado_B.py`, `lanzar_forzado.sh`, `puertas_y_rearme.py` (scratchpad de la sesion).
| prueba | resultado real |
|---|---|
| A. Seco BTC 5m brazo A, 15 min (18:19:31-18:34:31Z, `ensayo_A.log`) | config OK (`variante H23-A`, `umbral 0.05`, `hash_regla 46eff953...`, `codigo_sha_h23 602d5a2d...`, dependencias OK, `kill_brazo_v3` presente, escalon H23, N=40); par_refs (ref15 82573,17 / ref5 82518,33 -> lado Up); el 5m cerro por `tick_cambiado` a T=82 s; **0 pujas, 0 ordenes** |
| B. Seco FORZADO brazo B, 10 min (18:35:30-18:45:31Z): umbral B y `mq` relajados EN MEMORIA desde un script externo (ledger aparte `..._seco_H23FORZADO_B_ledger.jsonl`) para ejercer puja/cancelacion | etiquetas `H23-B`/`H23B`/`brazo B`/`hash_regla` correctas en config, par_refs, mercado_fin; el 5m cerro por `tick_cambiado` a T=55,5 s; **0 pujas, 0 ordenes** |
| C. Puertas por CLI | `--confirmo-dinero-real` solo -> "real exige --ok-final-javi"; con texto -> "falta .../H23_OK_JAVI.txt: no se envia nada" (rc=1); `--rearmar-kill-brazo` y `--aceptar-linea-ilegible-brazo` sin real -> "exige --confirmo-dinero-real" (rc=1) |
| D. Puertas en proceso (OK de prueba en el scratchpad, NO en datalogs; ledger H47-B real en solo lectura) | OK con sha y dependencias correctos + ledger H47-B real -> **RECHAZA: "H47-B no ha terminado: tras su ultimo `config` real no hay `fin_ejecucion`"**; OK con sha equivocado -> rechaza; OK sin `h47=/pares=/contabilidad=/shadow=` -> rechaza |
| E. `--rearmar-kill-brazo` / `--aceptar-linea-ilegible-brazo` (rutas en tmp, puertas anuladas, Exp23 prohibido) | rearme escribe `kill_brazo_rearmado` y 2o rearme -> "no hay kill de brazo pendiente"; motivo vacio rechazado; linea cortada en ledger hermano -> `LedgerBrazoIlegible` (fail-closed), tras la confirmacion `ACEPTAR LINEA ILEGIBLE BRAZO A` -> evento `h23_linea_ilegible_aceptada` y el estado acumulado vuelve a leerse |
| F. `--imprimir-sha` | sha y deps coinciden con los del informe (ronda 3) |
| G. Aislamiento | tras los ensayos: `experimento_h47.KILL` NO existe; `experimento_h47_A_ledger.jsonl` mismo sha256 que antes; 0 lineas con "H23" en `experimento_h47_B_ledger.jsonl`; `experimento_h47.lock` de lo real no tomado (el seco usa `experimento_h47_seco.lock/.KILL`); el ledger seco H23 no encaja en el patron estricto `experimento_h47_H23[B]_ledger[_tandaN].jsonl` (no entra en el acumulado del kill) |

### Fallos / hallazgos
1. **El ensayo vivo NO ejercio puja, cancelacion a 60 ms, reaccion rapida ni kill V3 acumulado.** Solo el cierre de BTC 5m con `C % 900 == 0` es cotizable (1 ventana por 15 min); en las 2 ventanas
   vistas (18:25-18:30 y 18:40-18:45) hubo 0 pujas, tambien con regla relajada. El mercado se cerro por `tick_cambiado` (el 5m paso a extremo de precio, tick 0,001) a T=82 s y T=55 s.
   `ms_evento_a_cancel`, `ms_cancel_rtt` y `ult_poll_rest_ms` NO se han medido (0 eventos `h23_cancela`). Esos caminos solo estan cubiertos por los 75 tests con cliente falso + `X.post`/`X.cancelar` reales.
   Con la tasa del replay (43 cotizaciones A en 13 dias = 3,3/dia) un ensayo de 15 min casi nunca ve una; un ensayo vivo con pujas necesita ~1 dia de seco continuo (o un simulador de libro).
2. **Observabilidad: el codigo no registra POR QUE no puja** en la ventana (ni `bloqueo_*` ni motivo de `_objetivo`->None). En el ensayo forzado no se puede distinguir "bid5 ajeno ausente / tick /
   frescura / puerta" sin depurar. Recomendacion (no aplicada, cambiaria el sha y exige re-review): un contador de motivos por mercado en `mercado_fin` (como los de `ya_decidido`).
3. `tick_cambiado` cierra el mercado para siempre (H47: el tick dinamico cambia cerca de extremos); en el replay no se modela y puede restar cotizaciones reales a las 43/63 esperadas. A medir en el seco largo.
4. Imports/rutas: sin fallos. `h23_regla` y `h23_shadow` se resuelven por `AQUI/experimentos/5m_barato/h23_maker`; `a6_detector_vivo`/`h43_unidades` NO hacen falta. Con `python -I` hay que meter dev en `sys.path` (el ejecutable lo hace).
5. Nota para la linea del OK: el informe escribe `sha=sha=602d...` (doble prefijo) en la ronda 3; el valor correcto es `sha=602d5a2debb42cc0`. Copiar SIEMPRE la salida de `--imprimir-sha`, no el informe.
6. Contexto de la puerta H47-B: el ledger real de B tiene 13 `config` hoy, 2 kills ("cancelacion no confirmada", ya rearmados) y 33 `puja_fin` de 230 (14 %) a las 18:20Z; un `config` repetido de B tras un `fin_ejecucion` con
   `parada` NO cuenta. `h47_tandas_supervisor.py` relanza B cuando cae sin kill: **al terminar B (230) habria que parar el supervisor (`h47_tandas_supervisor.STOP`) antes de H23**, porque comparte `experimento_h47.lock` y wallet.
7. Carga: load5 17-23 durante todo el ensayo y `nice 19`: cualquier latencia medida entonces estaria inflada; no concluir nada de ms con este ensayo.

## 2. Cuantos dias faltan para n>=40 (replay `datalogs_analisis_caches/h23_maker/`, BTC, 13 dias 06..18-Oct)
Fuente: `/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/h23_2026-10-*.csv` (`analisis_h23.txt`), reanalisis con universo ejecutable p en [0,10; 0,60], T>=12 s,
1 relleno por cierre, tamano real (5 acc o ceil(1 USD/p)) y desenlace oficial (missing=0); script `scratchpad/gate_fecha.py`. Tasa = rellenos ejecutables / 13 dias; IC90 de Poisson.
| variante (cola base, alta 79 ms, cancel 60 ms) | cotizados (13 d) | rellenos ejecutables | dias con relleno | tasa/dia (IC90) | dias para n=40 (rango IC90) | EV pond. (tam. real) | sin 2 mejores dias |
|---|---|---|---|---|---|---|---|
| **A join_r** (el que aplica) | 43 | 10 | 5 | 0,77 (0,42-1,32) | **52 (30-95)** | +0,393 (a 2 EUR +0,595) | -0,001 (3 dias restantes) |
| **B join_r** (el que aplica) | 63 | 9 | 3 | 0,69 (0,36-1,22) | **58 (33-110)** | +0,515 (informe: +0,440; metodo de escalado parcial distinto) | -0,168 (1 dia restante) |
| A join (sim-fiel, no aplica al arnes) | 43 | 14 | 7 | 1,08 | 37 | +0,805 | +0,425 |
| B join (idem) | 63 | 21 | 8 | 1,62 | 25 | +0,620 | +0,337 |
Sensibilidad (A/B join_r): cancel 150 ms -> 35 / 32 dias; cola optimista (alta 79/cancel 60) -> 35 / 32 dias; cola conservadora = base.
Lectura: la regla pierde el edge del EV al quitar los 2 mejores dias (A -0,001, B -0,168 con 1-3 dias): con n=9-10 NO hay significacion; es el limite del replay, no una prueba.
**Fecha estimada.** Una sola wallet y un solo `experimento_h47.lock`: los dos brazos corren en tandas alternas, no a la vez. Cada tanda real (N=40 intenciones, presupuesto 5 USD) da ~9 posiciones (A) o ~6 (B).
- Inicio posible: tras terminar H47-B (33/230 hoy; con 3-18 pujas/h cuando esta activo son >=12-24 h de marcha continua, con 2 kills y paradas por suelo hoy: no se puede fechar mejor que "no antes del 22-24-Oct") + /code-review + OK de Javi.
- Si arranca ~24-Oct: **A join_r n>=40 ~15-Dic-2026 (rango 23-Nov a 27-Ene)**; B join_r ~21-Dic (27-Nov a 12-Feb) si se le dedica el tiempo entero. **Ambos a la vez por tandas alternas: ~110 dias, ~12-Feb-2027** (los dos a n=40).
  Escenario optimista (cancel 150 ms/cola optima): A ~28-Nov, B ~25-Nov (solo uno).
- La cadencia depende de `tick_cambiado`, frescura de libro y del suelo de saldo, no modelados en el replay: lo mas probable es que el real sea mas lento. 4-5 tandas por brazo.

## 3. Lista de verificacion final para el OK de Javi
Antes (el chief, no el agente):
1. H47-B terminado de verdad: ultimo `config` con `escalon B`, `n_max>=230`, `t_stop 60`, `codigo_sha=439a70e9262ef38c`; despues `fin_ejecucion` con `pujas>=n_max`, `kill null`, `parada` vacia, `abiertas_sin_verificar 0`;
   ningun `kill` sin `kill_rearmado`. Parar el supervisor (`h47_tandas_supervisor.STOP` o `screen -S h47sup -X quit`) y comprobar que no hay `h47B` vivo (lock libre). Comando: ver tail de `experimento_h47_B_ledger.jsonl`.
2. Desplegar y comprobar sha: `bash .../paquete_real/desplegar_dev.sh` y `cd /root/polymarket-research-dev && /root/polymarket-research/.venv/bin/python experimento_maker_h23.py --imprimir-sha`;
   debe dar `sha=602d5a2debb42cc0 regla=46eff95337902549 h47=439a70e9262ef38c pares=5e116f619887345d contabilidad=0a41bc39108cdf82 shadow=43373dd4affe3181 kill=59437e2037321aed`. Si h47/pares/contabilidad
   de dev han cambiado (parches al B real) el OK cambia: reemitirlo, y revisar el diff.
3. Tests: `nice -n 19 ionice -c3 bash -c 'ulimit -v 3000000; /root/polymarket-research/.venv/bin/python -m pytest -q -p no:cacheprovider /root/polymarket-research-dev/experimentos/5m_barato/h23_maker/paquete_real/test_experimento_maker_h23.py'` -> 75 passed.
4. `/code-review` MEDIUM del fichero con ese sha (ronda 3 hecha; paquete congelado: otro cambio = ronda nueva + OK nuevo). Decisiones pendientes: observabilidad del motivo de no-puja (hallazgo 2); `EDAD_TOKEN_MAX_S` 120 s, `VIGILAR_SALDO_VIVA_S` 10 s; tope de tanda no persistente; 1a tanda con poca ventana de observacion (~1 cotizacion cada 7 h).
5. Presupuesto: wallet dedicada con tope de pruebas 5 EUR, stake live max 2 EUR (H23 usa 5 acc o ceil(1 USD/p), <=3 USD/orden): confirmar con Javi que el tamano de H47/H23 entra en ese tope; sin recargas.
6. Crear `/root/polymarket-research-datalogs/H23_OK_JAVI.txt` con `sha=602d5a2debb42cc0 regla=46eff95337902549 h47=... pares=... contabilidad=... shadow=... kill=59437e2037321aed` (copiado de `--imprimir-sha`) + fecha + motivo.
Comando real (solo tras 1-6, dentro de una screen nueva pedida a la sesion principal, con `choom -n -500 --`):
`cd /root/polymarket-research-dev && /root/polymarket-research/.venv/bin/python experimento_maker_h23.py --brazo A --confirmo-dinero-real --ok-final-javi "$(cat /root/polymarket-research-datalogs/H23_OK_JAVI.txt)"`
(brazo B: `--brazo B`, ledger `experimento_h47_H23B_ledger.jsonl`, nunca A y B a la vez.) Rearme del kill: `--brazo A --confirmo-dinero-real --ok-final-javi "..." --rearmar-kill-brazo "motivo"`.
El dia D (primeros 15 min y cada tanda):
- Primera linea: `ENSAYO EN SECO` NO debe salir; debe salir `REAL H23 brazo A`, `puerta H47-B ok`.
- Ledger `experimento_h47_H23_ledger.jsonl`: `config` con `real true`, `variante H23-A`, `umbral 0.05`, `hash_regla 46eff953...`, `codigo_sha_h23=602d5a2d...`, `dependencias` iguales al OK, `kill_brazo_v3`.
- Todas las filas `puja_*/h23_*/mercado_fin/kill_brazo` con `variante`/`brazo`/`umbral`/`hash_regla`; ninguna escritura en `experimento_h47_B_ledger.jsonl`; `experimento_h47.KILL` ausente.
- Precios de puja siempre en [0,10; 0,60], T>=12 s, tamano 5 acc o ceil(1 USD/p), <=3 USD/orden; no mas de 1 puja viva por 5m y max 2 vivas.
- Primer `h23_cancela`: leer `ms_evento_a_cancel`, `ms_cancel_rtt`, `camino_ack`, `ult_poll_rest_ms` (hoy sin medir; el replay asume alta 79 ms y cancelacion 60 ms) y compararlos con 60/79; si p50 >> 150 ms el EV del replay no aplica.
- `h23_revalida_aborta` y `bloqueo_suelo_saldo`: contarlos; `kill`/`tope_tanda`/`sin_desenlace`: cero o explicar; rellenos: comprobar el desenlace oficial por gamma y el cuadre on-chain al cierre de tanda (`fin_ejecucion.abiertas_sin_verificar 0`).
- Registrar por tanda: cotizaciones (intenciones), rellenos, dias, EV ponderado por EUR y sin los 2 mejores dias; el gate n>=40 por variante es n>=40 posiciones con desenlace oficial acumuladas en TODOS los ledgers del brazo.
Limites: ninguna cifra de este documento valida la estrategia; el replay solo da cota de cadencia (n=9-10 por brazo, 13 dias).
