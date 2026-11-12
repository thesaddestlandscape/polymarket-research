# PREREG_CXB_MULTIVARIANTE_FORWARD — CONGELADO 12-Nov-2026 (statistical-validator, misión 5m barato)
**Dry-run puro. No autoriza ningún envío, ni real ni de prueba. El EV del dry-run es un ÍNDICE, no una previsión de euros.**
Sustituye a `PREREG_CXB60_FORWARD.md` (borrador v1, sha256 96db5ac9…) y a `PREREG_CXB_MULTIVARIANTE_SPEC_12nov.md` (borrador, sha256 f0a9058c…). Evidencia previa: TRAIN 26-Oct..09-Nov (motor v3, EXPLORATORIO): CXB60 +0,135/€, IC90 por días cruza 0, +0,040 sin los 2 mejores días. Los días ≥10-Nov son HOLD. Este forward es la primera prueba confirmatoria.

## 0. Conjunto congelado (referencia: `dryrun/HASHES_CONGELADOS.json`, sha256 534b476093a8294bf28f7ebf62e3e825dcbd57bb98d43dd9fa6a7bc844d03c0b, creado 2026-11-12T10:46:35Z)
Lo ejecuta el runner, que aborta con exit 3 si algo difiere: frozen/engine.py a7b8431a…, frozen/capt.py 3fe09524…, frozen/relojes.py 6c89b853…, frozen/engine_clock.py 4196fbf6…, frozen/engine_v3.py b1bf34a1…, cxb60_core.py 40b1099f…, cxb60_io.py 0f8bb536…, cxb60_dryrun_fase0.py 6f743e2f… (VERSION cxb60_dryrun_v3), l_pool_emp.json fafab554….
Informativos (el runner NO los vigila; quedan congelados por este prereg): cxb60_resolve.py c0ef9125…, cxb60_informe.py 13934151…. Los hashes completos están en el JSON; `congelar_hashes_cxb60.py --verificar` dio rc=0 el 12-Nov 11:2xZ.
Ops (trazabilidad, NO son parte del contraste): lanzar_cxb60_dryrun.sh 44cc8560…, cron_resolve_cxb60.sh 62622c58…, vigia_cxb60_heartbeat.py f58e6361…, c6/watchdog_verify_cxb60.patch 71af67a6….
Parámetros = manifiesto del runner (por defecto): L ∈ {0,10; 0,13; 0,16; 0,19}, 5 acciones, GTC post-only virtual, gate G0, re-armado, TMIN, LAT_POST, SETTLE 2 s, c_print 19 (primario) + c_print 59 en paralelo (OUT/c59), 100 semillas PLC60, rebate maker 0,2·0,07·L(1−L), cobertura mínima 0,95. Sin ventanas de tuning.
Benchmark previo al congelado (scratchpad bench, slice 11-Nov 20-23Z, 4 monedas, 108 variantes, c19+c59): rc=0, STOPPED_COMPLETE, 474 cierres, 0 q_dup/parse_err/fuera_de_orden, RSS pico 663 MB, cpu_advance p50 3,7 ms / p90 25 ms / p99 401 ms (n=1.268), hash_check ok, ningún fichero congelado modificado. No se leyó ningún EV.

## 1. Hipótesis (jerarquía fija; gatekeeping de secuencia fija, sin dividir α)
- **H1 (primaria, única confirmatoria de la población principal)**: en ETH+SOL+XRP 5m (cada token = unidad de mercado), CXB60 (cancelación a rx del disparo `bid_otros_rx < L` + 60 ms) tiene EV|fill ponderado por € (Σpnl/Σcoste, rebate incluido) > 0, mejor que su control de igual colocación GEO1 y mejor que el placebo de igual cobertura PLC60.
  Por qué CXB60 y no CXBEMP: las 1.153 anclas indirectas dan l p50 ≈ 63 ms (p90 ≈ 140); el pool de CXBEMP (p50 41 + d_proc 3 ms SUPUESTO; anclas directas n=4) es optimista, no conservador. CXB60 es el centro realista; CXB100 es la prueba de estrés (G8).
- **H2 (secundaria, se contrasta SOLO si H1 = PASS)**: lo mismo en BTC (población aparte, `--coins BTC --clave-valido dia_valido_btc`). Sin evidencia TRAIN. **DATA_BLOCKED hoy**: el gmap de sa_r1 no trae BTC (0 de 870 mercados el 10 y el 11-Nov). H2 solo se puede evaluar si, antes del primer día contable, existe una fuente de desenlace OFICIAL de BTC con el mismo esquema (`{slug: {id, toks, des}}`) en un directorio que se pasa con `--gmap-dir`, sin tocar ningún fichero congelado. Si llega más tarde, H2 cuenta desde el primer día completo con esa fuente. Si H1 no pasa, BTC se informa como EXPLORATORIO (no como REJECTED).
- **Descriptivo, nunca puerta**: CXBEMP, CXB35, CXB45, CXB150, G0, el desglose por L y por moneda, el Spearman EV~l y c59 por moneda. Se espera que ETH con c59 quede ≈0 (declarado de antemano; no es un fallo).

## 2. Unidades y definiciones
- Unidad de inferencia: el **CIERRE** (`fin`: todos los tokens, monedas y L que cierran juntos = una sola apuesta) y el **DÍA UTC**. El n de rellenos NO es n independiente. La concentración por wallet no aplica (órdenes virtuales propias, no hay selección de wallets).
- Métrica de las puertas: `ev_cond_fill_ponderado_eur` del informe (Σpnl/Σcoste). Se reportan aparte, sin que sean puerta: EV incondicional (Σpnl/Σcoste_potencial), P(fill), EV por unidad y pnl por mercado procesado.
- IC90: el bootstrap del informe (razón de sumas, remuestreo de clústeres, B=2.000, semilla 12345, percentiles 5/95). Con 10-20 clústeres por día es anticonservador; lo compensan G4 y G9.
- No se multiplica el EV por ningún factor: ni corrección δ, ni €/año, ni escalado por stake. El nivel del EV es un índice.

## 3. Calendario, días válidos y cutoff
- Cutoff = hora de este congelado (sha256 en `PREREG_CXB_MULTIVARIANTE_FORWARD.sha256`). Nada anterior al cutoff cuenta.
- **Fecha de inicio D_dep** = fecha UTC del primer `run_manifest`/heartbeat RUNNING de VERSION cxb60_dryrun_v3 con `hash_check.sha256_referencia` = 534b4760…, posterior al cutoff, en `/root/polymarket-research-datalogs/cxb60_dryrun/`. **Primer día contable = D_dep+1** (D_dep es parcial). El informe se corre con `--desde D_dep+1`. Si no se ha desplegado antes del 2026-11-19 23:59Z, el prereg caduca: se vuelven a verificar los hashes y se congela de nuevo con una fecha nueva.
- **Día válido** (todo a la vez): `coverage_<D>.json` con `dia_valido` = true (día completo y cada una de ETH, SOL y XRP con cobertura ≥ 0,95; en BTC, `dia_valido_btc`); existe el gmap oficial del día; la cobertura de desenlace de los rellenos de la población ese día es ≥ 0,95. Un día no válido no cuenta y se lista; nunca se rellena con ceros.
- Calidad agregada (si falla, el resultado es INSUFFICIENT, no se excluye nada): cobertura de desenlace de la población ≥ 0,99, calculada por el validador desde los `res_<D>.csv.gz` (filas con q > 1e-9 y coin ∈ población: proporción con pnl no nulo). **El campo `cobertura_desenlace_rellenos` del informe NO sirve para esto**: cuenta los rellenos de BTC sin resolver dentro de la población primaria (bug de informe: `excl` se suma antes del filtro de moneda; no afecta al EV porque la exclusión va por tok/L/var). Además: mercados con `hueco_feed` ≤ 5 % de los procesados de la población (se INCLUYEN en el EV, sin exclusión a posteriori).

## 4. Puertas de H1 (PASS = todas; ninguna se relaja después de ver datos)
- G1: n_rellenos(CXB60) ≥ 40, n_cierres_con_relleno ≥ 30 y ≥ 10 días válidos.
- G2: EV ponderado > 0, con extremo inferior del IC90 > 0 tanto por días como por cierres.
- G3: Δpnl diario CXB60 − GEO1 > 0, con extremo inferior del IC90 por días > 0 (`G3_incremental_vs_GEO1_dias.ic90_inferior`).
- G4: EV ponderado sin los 2 mejores días > 0.
- G5: placebo con semillas ≥ 100 y p = (1+#{EV_PLC ≥ EV_CXB60})/(1+S) **≤ 0,025** (0,05 repartido entre las 2 miradas de §6). El `ok` del informe usa S ≥ 20 y 0,05: no vale; el validador aplica esta regla.
- G6: ninguna moneda > 60 % del coste de CXB60 y ningún día > 25 % del pnl positivo. En BTC solo se aplica la parte del día.
- G7: signo(EV CXB60 con c59) = signo(EV con c19), sobre el agregado de la población.
- G8: EV(CXB100) ≥ −0,05.
- G9 (split-half cronológico): con los días válidos partidos en dos mitades por orden (la primera se queda con el día impar sobrante), EV ponderado de CXB60 > 0 en cada mitad (informe con `--desde/--hasta`).
- H2 (BTC): G1-G9 sobre la población BTC, con G6 solo por día.

## 5. Resultado y etiquetas
- **PASS** → `DRY_RUN_VALIDATED` (índice). No autoriza nada en live. Solo permite proponer a Javi un micro-ensayo con tope, tras: red team independiente, l directo con n ≥ 30 anclas de exchange, d_proc medido en bucle y /code-review del emisor.
- **FAIL** (`REJECTED` para esta especificación), solo si se cumple G1 y además: extremo superior del IC90 por días del EV de CXB60 < 0, o placebo con p ≥ 0,50 (CXB60 no mejora la mediana del placebo).
- **INSUFFICIENT** cualquier otro caso. La puerta sigue abierta: una variante nueva necesita un prereg nuevo y un OOS nuevo.

## 6. Miradas, parada y kill
- Mirada 1: al cumplirse el 10.º día válido. Si lo único que falla es la parte de n de G1, se pospone hasta que se cumpla, como mucho hasta el 20.º día válido (el disparador es n, no el resultado).
- Mirada 2 (solo si la 1 da INSUFFICIENT, no FAIL): con 20 días válidos acumulados y todas las puertas. Después, si no hay PASS ni FAIL: INSUFFICIENT_FINAL. No hay una tercera mirada con este prereg.
- Plazo: si a D_dep+35 días naturales no se ha llegado a la mirada que toca, INSUFFICIENT_OPERATIVO.
- Entre miradas no se calculan puertas. El seguimiento diario es solo de operación y calidad (§7); el EV diario no se lee para decidir.
- Kill de integridad (invalida desde ese día; si cambia el código congelado, todo el forward): cambio de un fichero de §0 (el runner aborta con exit 3 y el día se pierde), otra VERSION, dos instancias escribiendo en el mismo OUT, o editar el informe o el resolvedor. Arreglar un bug del informe o del resolvedor exige congelar de nuevo ANTES de la siguiente mirada y reportar las dos versiones. No hay kill por PnL: es un dry-run, sin dinero.

## 7. Seguimiento diario obligatorio (lo lee el vigía o el chief; no decide)
Heartbeat < 5 min con status RUNNING; lag del flujo < 600 s; RSS < 3.000 MB; días válidos y no válidos (con su motivo); cobertura por moneda; mercados `incompleto_arranque` y con `hueco_feed`; cobertura de desenlace por población (calculada desde res_); gmap de sa_r1 de D-1 presente; contador de días válidos y fecha prevista de la mirada; `sello_print` = ws_ex-19-1 (c19) y ws_ex-59-1 (c59) en todo informe. Aviso por Telegram si falla cualquiera de estos o si el resolvedor o el informe fallan.
