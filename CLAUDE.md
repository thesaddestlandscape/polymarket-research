# CLAUDE.md — Polymarket Research Bot
**Versión corta desde 2026-09-30** (OK Javi). La narrativa histórica íntegra (hallazgos con fecha, cifras, citas textuales) está en la memoria nativa `reference_claude_md_completo_30sep` — **"archivo"** en este documento — y en `git log -- CLAUDE.md`. Aquí solo quedan reglas y una línea por pieza. **Regla de mantenimiento: al añadir algo nuevo, aquí va la regla + una línea (script, fichero, gate); el relato va a una memoria enlazada. Este fichero no debe pasar de 100k caracteres.**

## Reglas de comportamiento
- **Fail Loud**: "completado"/"verificado" es INCORRECTO si algo se asumió sin confirmar explícitamente. Surfacear incertidumbre siempre.
- **Checkpoint**: en tareas ≥3 pasos, resumir tras cada paso qué está verificado y qué queda antes de continuar.
- **Antes de escribir código nuevo** (decisión ladder): ¿ya existe en el codebase? → ¿lo hace la stdlib/requests/csv/json? → ¿una línea? → solo entonces: mínimo viable. Excepción: código de seguridad live (circuit breakers, filtros end_date, Kelly) — no minimizar.
- **Antes de concluir, promocionar, refutar o construir**: repasar la sección "🪤 Trampas ya cazadas" de este fichero (está siempre cargada). Para las cifras históricas de una pieza concreta, su memoria enlazada y el archivo.

## Protocolo de arranque de sesión (obligatorio, antes de responder nada)
Petición explícita de Javi (17-Jul, reforzada muchas veces). En cada conexión, ANTES de atender cualquier petición y sin que se pida. Permanente, no expira. Todo lo que se revisa se **reporta en el mensaje de arranque**, no basta con mirarlo internamente.

1. **Personalidad + calendario + misión, LO PRIMERO, fundamento de toda la sesión** (Javi 10-Ago: *"la personalidad que se te ha dado es la que va a llevarnos a cumplir los objetivos, misiones y el calendario"*; *"tu personalidad tiene que estar activa siempre, en todas las sesiones"*). Leer cada sesión, en este orden:
   - `feedback_personalidad_ingeniero_senior_tiburon_03ago` — ingeniero senior "tiburón": rentabilidad real, rigor sin alucinar, picaresca, nunca abandonar una idea sin datos, revisar Telegram a fondo. No es tono: es el filtro de cada propuesta, de cada barrido y de cada línea de código, de principio a fin de la sesión.
   - `project_calendario_200k_11ago2027` — calendario con gates falsificables (Stages 0-4 cierran 31-Oct-2026, Stage 5 arranca 01-Nov, sin recargas planificadas, 200.000 € el 11-Ago-2027). **Checkpoint DIARIO**: recalcular con datos reales de hoy (trades/día, PnL, bankroll) contra la trayectoria mensual; decir en qué fase estamos y si se cumple.
   - Obsidian `/root/second-brain/02_projects/polymarket-research.md` ("Misión y objetivo") + `project_mision_sistema` → `project_plan_escalonado_200k_23jul` → `feedback_obsesion_busqueda_constante_23jul` + `feedback_todo_alineado_al_objetivo_23jul` (citar SIEMPRE qué Stage empuja cada propuesta).
   - Es el **proyecto de vida del usuario**: toda decisión va alineada a esos objetivos (200k €/año año 1, 300k año 2…, las 8 cualidades del sistema).
2. **Barrido de salud — eres el médico del proyecto, no un lector de dashboards** (Javi 05-Ago: *"revisas a fondo absolutamente todo, con precisión y profundidad absoluta, detectas cualquier lag, bug, error o falta de optimización y lo solucionas siempre con la prioridad de tener el sistema sano 100%"*). Buscar activamente lo que NINGÚN vigía mira todavía. Con comandos reales, no de memoria:
   - `python3 verify_deploy.py` (screens STALE; skill `/verify-deploy`).
   - `data/shadow/salud_sistema_diaria.json` (ver pt.18).
   - `uptime` + `ps aux --sort=-%cpu | head -15` — `load5/nproc > 3` sostenido = sobresuscripción real. También `free -m` (swap) y `df -h /` (disco). Vigías: `vigia_carga_sistema.py` (cron 15 min) + `analisis_diario_salud_sistema.py`.
   - `git rev-list --count origin/main..HEAD` (sin fetch) — si crece, el push está roto.
   - `screen -ls` contra `pipeline_watchdog.py`/`inventario_sistema.py` — nada corriendo fuera de cron/screen registrado.
   - **⭐ Auditoría de LÓGICA DE DECISIÓN e integridad de datos, obligatoria cada sesión** (ahí han vivido los fallos más caros):
     - **Claves de features fantasma**: toda estrategia que lea `features.get("clave")` — comprobar con `grep` cruzado que la clave existe en el diccionario que la genera (un docstring puede mentir).
     - **Estado absorbente**: `strategy_params.json::activa=False` sin `ACUMULAR_SHADOW_AUNQUE_DESACTIVADA` y sin haber estado en `pares_permitidos_live` → atrapada para siempre. Mirar sobre todo n=8-15. Mismo patrón en cualquier simulador con "suelo" que no se resetea.
     - **Filtros/gates degenerados en veto total**: para cada `filtro_causal`/gate automático, ¿qué % de las observaciones REALES de hoy cubre? Si cubre 85-100 %, ya no filtra: veta.
   - Si algo está roto: **arreglarlo en la misma sesión con la prioridad más alta** y convertirlo en código que se audite solo. Excepción: el motor de decisión COMPARTIDO por estrategias live (aplicación de `filtros_causales` en `shadow_predict.py`/`shadow_postmortem.py`) exige diseño cuidadoso + `/code-review` antes de commitear.
   - Nunca tocar `fast`/`slow`/`control`/ejecutores con `DRY_RUN=False` al deprioritizar procesos (`nice`). Subir el VPS o consolidar procesos = decisión de Javi.
   - Historial e incidentes: archivo pt.2; memorias `feedback_medico_proyecto_barrido_profundo_05ago`, `project_push_roto_carga_cpu_resuelto_05ago`, `project_checkpoint_sesion_05ago_noche_candidatas_filtros_causales`.
3. **Contexto completo antes de hablar**: `MEMORY.md` entero, los cierres/checkpoints más recientes, datos reales (`estado_actual.md`, `hipotesis_auto.md`, `trades.csv`) y el vault de Obsidian, **ya clonado de forma permanente en `/root/second-brain`** (cron `run_sync_obsidian.sh` cada 15 min; NO reclonar nunca; si hace falta, `git -C /root/second-brain pull --rebase --autostash`). Empezar por `_index/00_INDEX.md`.
4. **Recitar los pendientes sin cerrar** de sesiones anteriores, proactivamente (checkpoint más reciente en memoria; punto de partida histórico `project_revision_pendiente_08jul`).
5. **`logs/vigia_sigma_patrones.log`**: ¿algún patrón `sigma_*` nuevo (n≥40, `data/live/vigia_sigma_patrones_latch.json`) merece acción? Regla general al auditar cualquier vigía con latch: la firma NO debe incluir un valor recalculado cada ciclo (umbral, IC exacto) — ver `feedback_bug_latch_umbral_vigia_causal_fillable_28jul`.
6. **Reportar**: (a) hipótesis nuevas desde la última sesión ("Estrategias nuevas sugeridas" de `hipotesis_auto.md` + `hipotesis_custom.json`/`llm_hypothesis.py`); (b) mensajes de TODOS los vigías con avisos nuevos.
7. **Análisis diario de ballenas + postmortem** (Javi 20-Jul: *"encuentra debilidades que podamos explotar… minarlas nosotros primero"*): cruzar los datos nuevos (`ballenas_timing_history.csv`, `wallet_edge_tracker`/`wallet_edge_score_por_marco.json`, `smart_money_consensus.json`, `wallet_contraparte_tracker`) contra trades/horarios/franjas/PnL/edges reales. Revisar el postmortem (`strategy_params.json::filtros_causales`/`patrones_ganadores`, `hipotesis_auto.md`) y decir qué ha aprendido el sistema.
8. **Ballenas = la lente por defecto** (Javi 21-Jul): cualquier análisis de estrategia en la sesión (candidata, selección adversa, fill-ability, pausa, promoción) se cruza contra TODA la infraestructura de ballenas antes de concluir: `ballenas_timing_state.json`/`ballenas_dentro_banda`, `ballenas_executor_5min.py`/`ballenas_executor_btc15m.py`, `wallet_edge_tracker.py`, `smart_money_consensus.json`, `wallet_contraparte_tracker.py`. Mapa: `project_mapa_cobertura_fuentes_ballenas_20jul`.
9. **Franja milimétrica de ballenas — PRIORITARIO, recordar a diario**: `python3 analisis_franja_milimetrica_ballenas.py` (bucket 0,05; ballenas + shadow + dinero real por activo/marco → `data/shadow/franja_milimetrica_ballenas.json`). Reportar (a) mejor bucket fino por activo/familia con su n (n<40 por bucket = exploratorio, NO gate; no proponer cortes con eso); (b) huecos (`ballenas_n>=50`, `hit>=70%`, `shadow_n<15`). Cortar solo con n≥40 y gate riguroso propio (Wilson+shuffle+bootstrap). Clasificar SIEMPRE por arquetipo (`project_dos_patrones_edge_bandera_21jul`): A = edge de modelo propio, fill-ability mala (6-36 %, selección adversa); B = edge coin-específico correlado con ballenas, fill-ability buena (53-61 %).
10. **Punto de confirmación 95 % por (moneda,marco)**: `data/shadow/punto_confirmacion_YYYY-MM-DD.csv` (hilo `punto_confirmacion_logger.py`); n por cada una de las 7 combinaciones y fill-ability (objetivo n≥30-40). El edge en shadow no implica fill-ability. Memoria `idea_punto_confirmacion_95pct_por_moneda_21jul` (25-Sep: refutado al ask real en 7 combos, ver `project_checkpoint_sesion_25sep_manana_protocolo`).
11. **Candidatas live + hipótesis + cementerio explotable**: (a) `candidatos_evaluacion_live` (fill-ability, gates); (b) `hipotesis_auto.md`, custom, tracker; (c) ¿algo del cementerio se puede revivir con hallazgos nuevos (ballenas/franja/punto de confirmación)? Incluye re-correr `analisis_wallet_quirurgico_precio_timing_22jul.py` según crezca el roster de `vigia_wallet_edge_forward.py`.
12. **`data/shadow/gate_bucket_propio.json`** (cron 07:03 → `vigia_gate_bucket_propio.py`, Telegram solo veredictos nuevos): (a) buckets que cruzaron rigor (n≥15, shuffle p<0,05, split-half) desde la última sesión, `malo_confirmado` y `bueno_confirmado`; (b) cuántos siguen `sin_concluir` por tupla (sobre todo 60min/5min). Los ejecutores de tupla live EXIGEN `bueno_confirmado` (ver "Veto de micro-bucket"). `ballenas_banda_fina_gate.py::vetaria_fase1` NO se usa para nada operativo. Memoria `project_gate_bucket_propio_activo_28jul`.
13. **Loggers de "solo captura" — revisar madurez cada sesión y mantener esta lista** (un logger que no decide nada es invisible al resto del protocolo):
    - `pfinish` (`photo_finish_logger.py`) — refutada 28-Jul, sin acción.
    - `punto_confirmacion_logger.py` — pt.10.
    - `favorito_ultimosegundo_5min.py` → `data/shadow/favorito_ultimosegundo_YYYY-MM-DD.csv`; n por activo, aviso al cruzar n≥15.
    - `fetch_polymarket_activity_ws.py` → `polymarket_activity_YYYY-MM-DD.csv`; comparar fidelidad con `ballenas_timing_history.csv` antes de conectarlo (`idea_rtds_activity_trades_gratis_28jul`).
    - `fetch_chainlink_prices.py` — alimenta la resolución oficial, no es huérfano.
    - `resolution_sniper_observer.py` → `resolution_sniper_obs_YYYY-MM-DD.csv`; n≥40 por combo para gate (`project_resolution_sniper_multimoneda_disenado_28jul`).
    - `p22_cola_posicion_fase0.py` → `p22_cola_posicion_fase0.csv` (P22 refutado 04-Ago).
    - `fetch_binance_perp_cvd_oi.py` (cron 5 min) → `binance_perp_cvd_oi_YYYY-MM-DD.csv`; pendiente comparar CVD perp vs spot (`idea_amt_spot_vs_perp_cvd_20jul`).
    - `vigia_p31_wallets_forward.py` (cron `35 */3`) → `data/shadow/p31_forward_validacion.json`; combos con n≥15 forward y veredicto; primero `XRP#15m#fade` (`idea_p31_fade_wallets_sistematicamente_malas_11ago`). La watchlist `p31_wallets_watchlist.json` no se reescribe.
    - `fade_depth_universal_fase0.py` → `fade_depth_universal_fase0.csv`, fuente de verdad de cualquier fade. `gbmlate_fade_depth_fase0.py` muerto a propósito (`idea_gbmlate_fade_refutado_datos_frescos_16ago`).
    - `resolution_sniper_fade_depth_fase0.py` — fade REFUTADO 19-Ago, no reabrir sin repetir el gate con más n (`idea_resolution_sniper_fade_refutado_19ago`). La variante NAIVE sí se confirmó: `resolution_sniper_naive_executor_dryrun.csv`.
14. **`logs/vigia_log_growth.log`** (`vigia_log_growth.py`, cron `30 * * * *`): grep `payout inverso`/`aviso enviado` y cruzar con `data/live/vigia_log_growth_latch.json` (`avisado: true`): ¿alguna tupla latcheada sigue en `pares_permitidos_live` sin decisión? Una alerta de Telegram enviada una sola vez se pierde si nadie la busca.
15. **`python3 inventario_sistema.py`** — clasifica TODOS los .py: (A) screen, (B) cron con umbral derivado de su horario, (C) infraestructura recurrente SIN screen ni cron = "se me olvidó conectarlo", (D) análisis puntual. Revisar (C) explícitamente y arreglar en la sesión. Ojo con falsos positivos de (B): scripts que solo loguean cuando hay algo nuevo (`smart_exit_logger.py`, `wallet_contraparte_tracker.py`, `maker_pilot_sim.py`) — correrlos a mano antes de concluir. Toda screen nueva va a `pipeline_watchdog.py` (`SCREEN_RESTART` + `check_screens()`) y a `verify_deploy.py::SCREENS`.
16. **Auditoría de madurez de TODO lo "solo observacional"** (loggers, observers, ejecutores DRY_RUN, boosts inactivos, simuladores), con n fresco: tabla pieza → qué mide → madurez hoy → siguiente paso. Cruzar contra `inventario_sistema.py` (C), la lista del pt.20 y los hilos de `observadores_fase0.py`/`ejecutores_dryrun_fase0.py`/`vigias_frecuentes_fase0.py` para no dejar ninguno fuera. **Nunca reportar una cifra agregada sin verificar que el subconjunto REALMENTE accionable la sostiene.** Ejemplo: `project_auditoria_observacional_29jul`.
17. **Desagregar SIEMPRE por moneda × marco × micro-bucket de precio (paso 0,05-0,10)** en todo análisis, gate, sizing o veredicto (Javi 29-Jul: *"hay que hilar muy muy fino"*). El agregado es un resumen posterior, nunca el primer ni único corte. Un gate que agrupa por familia sin desagregar por moneda es un bug. Memorias `feedback_desagregar_por_activo_siempre`, `idea_kelly_precio_desagregado_por_moneda_29jul`.
18. **`data/shadow/salud_sistema_diaria.json` + `logs/analisis_diario_salud_sistema.log`** (`analisis_diario_salud_sistema.py`, cron 07:57): duración del pipeline vs línea base, procesos colgados (>180 s), screens STALE, disco, RAM, trades reales OPEN con `end_date` pasado >20 min, caídas de filas en `trades.csv`/`results.csv`. Incluye `medir_vigias_rotos()` (cola de todos los `logs/vigia_*.log` de 48 h: `TimeoutExpired`/`Traceback`/"murió:") — cada `🚨 vigía roto` es un JSON que puede llevar días sin regenerarse. Revisarlo aunque no haya habido aviso; ante anomalía, `py-spy dump` y comparar con el histórico de 90 días. Todo vigía con timeout fijo corre riesgo según crecen sus datos.
19. **`logs/vigia_zonas_validadas_externas.log`** (`analisis_zonas_validadas_externas_post_twap_10ago.py`, cron 06:30 vía `vigia_zonas_validadas_externas.py` → `data/shadow/zonas_validadas_externas.json`): reportar cambios ENTRA/SALE. **Regla permanente**: nunca concluir fill-ability contra `libro_snapshots.csv` genérico si la tupla tiene ejecutor/observer dedicado de baja latencia (`feedback_contrastar_fuente_correcta_por_tupla_19ago`).
20. **Trackear día a día toda candidata con mecanismo de seguimiento propio** (Javi 25-Ago) y reportarla en el arranque. Lista viva — **una línea por pieza; contexto, cifras base y trampas en archivo pt.20 y en la memoria citada**. Salvo que se diga otra cosa, los ficheros están en `data/shadow/` y el gate para decidir es n≥40 con días independientes; nada pasa a real sin checklist de 6 categorías + `/code-review` + OK de Javi.
    - **A3 "ganarles al entrar"**: `saltos_chainlink_fase0.py` (→ `saltos_chainlink_fase0.csv`) + `fetch_binance_bookticker.py`; `vigia_saltos_ask_real.py` (07:45 → `vigia_saltos_ask_real.json`); `vigia_a3_candidata_diaria.py` (08:03). A3 general REFUTADO al ask real 28-Sep; solo se vigila "segundo salto + BTC + Up". La simulación al último trade NO cuenta. `idea_a3_exploracion_exhaustiva_cerrada_28sep`.
    - **A3b Binance manda**: `binance_jump_leadlag_fase0.py` → datalogs `binance_jump_leadlag_fase0.csv`; correr `analisis_binance_jump_leadlag.py`; n≥40 eventos/celda y ≥3 días. El libro reacciona en <0,3 s.
    - **Wallets "primera compra"**: `wallet_first_buy_fwd_tracker.py` (07:52 → `wallet_first_buy_fwd.json`) + `wallet_first_buy_follow_fase0.py` (→ datalogs `wallet_first_buy_follow_fase0.csv`) + `wallet_first_buy_longshot_executor_dryrun.csv`. `project_wallet_first_buy_resto_pendiente_28sep`.
    - **Precierre multi-instante**: `precierre_multioffset_fase0.py` → datalogs `precierre_multioffset_fase0.csv`; sección del resumen 07:25 (`vigia_precierre_naive_twap.py`); n≥40 y ≥3 días (forward 25-29 Sep: +0,01 €/€, no el +0,089 in-sample).
    - **PRECIERRE y NAIVE modo TWAP (LIVE)**: `vigia_precierre_naive_twap.py` (07:25): aciertos reales vs esperado, 15min, kill-switches (`precierre_twap_kill.json`, `naive_twap_kill.json`), revalidar offset/banda con TWAP oficial (`analisis_precierre_twap_ventana_24sep.py`). `project_precierre_modo_twap_live_24sep`.
    - **Predicciones GBM con regla TWAP**: `vigia_predicciones_twap.py` (07:35). El arquetipo A solo se considera superado con €/trade fillable >0, n≥40 y días independientes, medido con el primer snapshot POSTERIOR a la señal (`idea_gbm_late_reactivo_lookahead_refutado_23sep`).
    - **⭐⭐ Tomadores persistentes (30-Sep, Javi: "controlar todo el universo y solo fiarnos de las mejores")**: `seleccion_tomadores_persistentes.py` (cron 07:17, Telegram diario → `tomadores_persistentes_universo.json` + `tomadores_persistentes_informe.json`): universo DIARIO de tomadoras agresivas con neto de fee >0 y ≥5/6 días positivos (ventana rodante de 6 días, caché por día), su forward propio día a día y el EV de copiarlas al ask real con NUESTRA latencia, que captura `tomadores_persistentes_fase0.py` (hilo de `observadores`, → datalogs `tomadores_persistentes_fase0_YYYY-MM-DD.csv`). Gate: celda con n≥40, ≥10 días, EV≥+0,10, IC90 por días >0, wallet top ≤30 %. Contexto y por qué: `project_como_ganan_las_wallets_ganadoras_30sep`. Herramientas de diagnóstico: `analisis_ganadores_alpha_vs_ejecucion_30sep.py`, `analisis_perfil_entrada_por_estrategia_30sep.py` (¿entramos antes, durante o después del movimiento?).
    - **`vigia_twap_fuente_polybolt_diario.py`** (09:20, Telegram diario → `vigia_twap_fuente_polybolt.json`): ¿puede precierre/naive vivir sin RTDS? Compara el método de hoy (ticks RTDS) con uno solo-PolyBolt (spot Pyth corregido por su sesgo + referencia `twap60` oficial) contra el desenlace real. Gate para proponer el cambio de fuente en el ejecutor: ≥10 días e IC90 por días de la diferencia ≥ −0,5 pp (margen ≥2 bps). Proyección y referencia deben salir de la MISMA fuente: cambiar solo la referencia a la oficial no mejora. `project_polybolt_spot_es_pyth_failover_30sep`.
    - **`vigia_precierre_z_marco_diario.py`** (08:40): EV al ask real por bin de z a T-45 s; 15min z[1,0-1,8) → proponer `Z_MIN_TWAP` por marco si n≥40, ≥10 días, IC90>0.
    - **PERPS**: `project_perps_pendientes_25sep` (6 pendientes, recitar y avanzar el de más valor) + `project_perps_estado_y_plan_22sep`. Fetchers por cron: `fetch_polymarket_perps_leaderboard.py`, `fetch_polymarket_perps_market.py`, `fetch_polymarket_perps_wallet_fills.py`, `fetch_polymarket_perps_fills_full.py`, `fetch_perps_tickers.py`. La unidad estadística es la POSICIÓN, no el fill. Encargo cloud `informes/perps_cloud_brief_25sep.md`. Solo dry-run.
    - **`vigia_wallet_mirror_entrada_baja.py`** (07:41): WM con entrada <0,20 por celda.
    - **CSV WM reconstruido** `wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv`: pendiente decisión de Javi sobre qué consumidores lo leen.
    - **Zonas forward P-GALLINA**: `zonas_forward_pgallina.py` (8 zonas en dry-run desde 24-Sep) + `vigia_zonas_forward_pgallina.py` (07:22). `project_zonas_forward_pgallina_stage0_23sep`.
    - **Micro-buckets con edge REAL al ask real**: `analisis_microbuckets_ask_real_sostenidos.py` (06:35 → `microbuckets_ask_real_sostenidos.json`) + `vigia_microbuckets_forward.py` (08:50; watchlist congelada `microbuckets_watchlist.json`, cutoff 2026-09-29T09:29Z; confirmado = n≥20, ≥5 días, EV≥+0,10, IC lo>0). `director_200k.py` usa esto, no pnl_fiel.
    - **`stink_bids_fase0.py`** + `vigia_stink_bids_diario.py` (08:55) → `stink_bids_fase0.csv`/`_seguimiento.csv`; `analisis_stink_bids_fase0.py`; n≥40 eventos, ≥10 días.
    - **`ya_decidido_universal_fase0.py`** (cron */10) + `ya_decidido_ws_fase0.py` + `vigia_ya_decidido_diario.py` (09:00) → `ya_decidido_universal_fase0.csv`, `ya_decidido_ws_fase0.csv`; gate n≥40 resueltos y acierto ≥99 %.
    - **`sniper_listados_fase0.py`** + `vigia_sniper_listados_diario.py` (09:05) → `sniper_listados_fase0*.csv`; `analisis_sniper_listados_fase0.py`; n≥40, ≥10 días.
    - **`libro_estado_ws.py`** — núcleo de micro-latencia (libro L2 por WS, histórico 100 ms, `en()`, `pedir()`, `ultimo()`, `trades()`, `hist_rango()`). Reiniciar `observadores` pierde el histórico en memoria: evitar reinicios innecesarios.
    - **`precierre_libro_ms_fase0.py`** → `/root/polymarket-research-datalogs/precierre_libro_ms_YYYY-MM-DD.csv.gz` (retención 5 d); simulación maker-con-cancelación pendiente con 3-5 días.
    - **`wallets_nuevas_fase0.py`** + `vigia_wallets_nuevas_diario.py` (09:10) → `wallets_nuevas_fase0*.csv`, `wallets_nuevas_conocidas.json`; `analisis_wallets_nuevas_fase0.py`.
    - **`macro_release_ms_fase0.py`** + `macro_calendario.json` → `macro_release_ms_fase0.csv`; añadir eventos a mano (BLS/JOLTS sin fuente).
    - **`barreras_touch_ms_fase0.py`** → `barreras_touch_ms_fase0.csv`.
    - **`escaleras_arbitraje_ms_fase0.py`** → `escaleras_arbitraje_ms_fase0.csv`; **`colas_escaleras_ws_fase0.py`** → datalogs `colas_escaleras_ws_YYYY-MM-DD.csv.gz` (14 d); `escaleras_cierre_ws_fase0.py`; vigía `vigia_macro_barreras_diario.py` (09:15).
    - **`gbm_late_imbalance_fase0.py`** + `vigia_gbm_late_imbalance_diario.py` (08:35) → `gbm_late_imbalance_fase0.csv` (preferir `imb*_senal`); `analisis_gbm_late_imbalance.py`; n≥40 por celda, ≥10 días.
    - **Sports radar**: `vigia_radar_estabilidad_temporal.py` (08:10 → `data/sports/radar_estabilidad_temporal.json`); aprobaciones manuales de Javi en `data/sports/wallet_mirror_aprobaciones_manuales.json` + `wallet_mirror_aprobaciones_kill.json`. `project_punto_medio_riesgo_y_edge_sostenido_24sep`.
    - **Sports fade extremas**: `vigia_sports_fade_extremas_forward.py` (cron `20 */6` → `data/sports/fade_extremas_forward.json`); 3 hipótesis congeladas (cutoff 2026-09-24T08:00); confirmado = n≥40, ≥10 días, wallet top ≤30 %, pnl ≥0,10, CI90 por días >0, ambas mitades >0.
    - **Edge quirúrgico**: `edge_quirurgico_rolling.py --resumen` + `vigia_edge_quirurgico.py` (carril `quirurgico`, cada 3 h → `edge_quirurgico_zonas.json`, `edge_quirurgico_historial.jsonl`): zonas operables/estrictas, LIVE vs dormidas, cobertura; promoción = operable ≥3 días distintos + fill-ability en esa zona exacta. Pendiente extender a TODO el universo (Javi: *"alcanzarlo todo y minarlo todo"*). `project_quirurgico_universal_22sep`.
    - **`momentum_ibs_ballena_reactivo_fase0.csv`** (segunda consulta a +3 s): degradación detección→decisión (`idea_momentum_ibs_ballena_familia_espejismo_confirmado_15sep`). **`momentum_ibs_ballena_botconsenso_dryrun_fase0.csv`**: filtro bot_consenso en SOL 5M/15M y BNB 15M.
    - **`resolution_sniper_freeze_estado_fase0.py`** (screen `freezeestado`) → `resolution_sniper_freeze_estado_fase0.csv` (instante exacto en que se dejan de aceptar órdenes).
    - **`resolution_sniper_precierre_depth_fase0.csv`**: informe DIARIO explícito (Javi 01-Sep): n, hit por activo, profundidad/ratio vs stake.
    - **Bot wallets P-GALLINA**: `bot_wallets_gate_bucket_historico.csv` (`vigia_bot_wallets_gate_bucket.py`, 07:24); `dispersed_bot_executor_dryrun.py` + `vigia_dispersed_bot_progreso_diario.py` (08:18, informe diario pedido por Javi). No fiarse del gate sin verificación cruzada independiente y sin 2-3 días de veredicto estable. `project_bot_wallets_colapso_confirmaciones_explicado_23sep`.
    - **Candidata 9** (`bot_consenso_*` en `shadow_predict.py::_bots_consenso()`): `candidata9_bot_consenso_executor.py` + `vigia_candidata9_executor_progreso_diario.py` (08:21), gate `candidata9_10_gate_bucket.json` (`project_candidata9_gate_conectado_08sep`; retirada de live, ver checkpoint 25-Sep). **Candidata 10**: re-correr `analisis_candidata10b_crossactivo_baseline_propio_25ago.py`. `idea_gallina_huevos_oro_candidatas_25ago`.
    - **`bot_consenso` × dirección de señal live** (`idea_portfolio_edges_cripto_25ago`): repetir el cruce, desagregar con n≥15 por moneda.
    - **Sports**: hipótesis sin script de cruce (timing relativo al evento; correlación entre mercados del mismo `event_slug`) y `Wallet Mirror#LoL` (`idea_portfolio_edges_sports_25ago`); `vigia_sports_categoria_sin_clasificar.py` (07:51; NCAAF sin regex propio); paridad Wallet Mirror: `analisis_sports_wallet_mirror_gate_bucket_fino.py` + `vigia_sports_wallet_mirror_gate_bucket_fino.py` (07:54) + `analisis_sports_wallet_mirror_concentracion.py`. **Fee de sports = 0,05, no 0,07.**
    - **Rondas de propuestas vivas — repasar enteras cada sesión**: `idea_10_propuestas_cross_repo_27ago`, `idea_ronda2_propuestas_profundas_27ago`, `idea_ronda3_evidente_y_profundo_27ago` (día de la semana; triple websocket DEPRIORIZADO por Javi), `project_10_estrategias_gallinas_pendientes_29sep`, `project_10_estrategias_ronda2_28sep`, `project_10_estrategias_ronda3_28sep`. **Taker Rebate Program** (`idea_taker_rebate_program_descubierto_27ago`): pendiente tracking de wV/tier como KPI.
    - **`H-FUNDING-NEGATIVE-BUYYES`** × fill-ability del reactivo: repetir el cruce hasta que haya solape (`idea_hfunding_cruce_reactivo_esperando_overlap_26ago`).
    - **`LIQUIDACIONES_5M`/`LIQUIDACIONES_60M`**: sin observador de profundidad; en cuanto un bucket cruce n≥40 en `gate_bucket_propio.json`, instrumentar (patrón `favorito_confirmado_depth_fase0.py`) antes de evaluar promoción.
    - **Weather** (repo aparte, protocolo propio): `idea_portfolio_edges_weather_25ago`.
    - **20b. Arquetipo A reactivo**: `gbm_late_reactivo_fase0.py` (WS spot Binance). Candidatas `GBM_LATE#DOGE#15min#BUY_YES` y filtro `gap_sigma_implicita` RESTO. **El +0,307 €/tr del 22-Sep era look-ahead (23-Sep): NO promocionar.** `idea_gbm_late_reactivo_desplegado_25ago`, `feedback_verificar_fuente_fillability_correcta_antes_refutar_26ago`.
21. **10 propuestas de alfa por sesión, generadas por mí** (Javi 25-Ago: *"cada sesión deberías darme 10 propuestas para generar gallinas de los huevos de oro… constante y sin parar"*). Concretas, accionables y ancladas en infraestructura/datos YA existentes. La generación no se delega a subagentes (verificar con datos sí). Pueden refinarse entre sesiones; el hábito no se salta. Seguir Candidata 3 (`analisis_candidata3_confluencia_gbmlate_fillable_25ago.py`).
    - **21b. 10 + 10** (Javi 01-Sep), listas separadas y adicionales: 10 para explotar MÁS el edge YA capturado (tuplas live/candidatas: más rendimiento, no perder operaciones válidas, ampliar cobertura) y 10 para minar edge que TODAVÍA NO capturamos.
    - **21c. Micro-latencia, detección rapidísima y requotes = el foco de toda propuesta** (Javi 29-Sep: *"No puedes perder eso de foco"*). Antes de diseñar un observador/ejecutor: (1) fuente push (WS CLOB, RTDS, Binance bookTicker), no polling/CSV; (2) dónde se pierde latencia; (3) ventana real del edge en ms; (4) requote/cancelación rápida; (5) timestamps en ms. Una medición con latencia de segundos NO refuta una idea de velocidad. `feedback_microlatencia_deteccion_requotes_foco_29sep`.
22. **Archivo vivo de lecciones** `project_lecciones_aprendidas_estrategias` (por qué fallan P1-P8, por qué funcionan F1-F5). Leerlo entero cada sesión y **antes de proponer o construir cualquier estrategia/filtro/gate**; actualizarlo cada vez que algo se confirme o refute con datos.
23. **10 propuestas para cerrar el gap contra el "PnL fiel v2 fill-ability real"** (Javi 01-Sep: *"Se puede minar pasta, es un hecho"*): `shadow_pnl_fiel.py` → `data/shadow/pnl_fiel_por_estrategia.json` (regenerar si es viejo). Usar SOLO tuplas con `pnl_fiel_eur_sin_suelo`>0 que no estén en `pares_permitidos_live` o estén infra-explotadas; el total agregado NO es el número a perseguir. Anclar en los números del día y citar las limitaciones de la cabecera del script (vetos de ejecución no modelados). Lista adicional a 21/21b.
24. **Buscador de edge perdido** (Javi 21-Sep: *"buscar dónde está el edge cueste lo que cueste"*): cuando una tupla pierde su edge, recorrer todas las dimensiones (zona fina de precio, hora/día, marco, moneda, lado, wallets, tamaño, latencia, confluencia, cross-activo) con el rigor forward de siempre, sin relajarlo. `project_estrategia_buscador_edge_perdido_21sep`, `project_buscador_edge_perdido_v1_22sep`.

Obsidian (`/root/second-brain`) es parte fundamental: se lee siempre y se escribe ahí (decisiones/estado narrativo en `02_projects/` + `03_decisions/`; nunca a mano en `09_estrategias/`/`10_hipotesis/`, que genera `sync_obsidian.py`).

## ⚠️ Manual operativo — errores que NO cometer (escrito para cualquier modelo)
Cada error va con la regla que lo previene. Si dudas entre dos interpretaciones, aplica la regla, no tu intuición.

**Errores de datos:**
1. **Inventar nombres de columna/clave** (`pnl` en vez de `pnl_neto`, `ic_efectivo` en vez de `ic_bayes`). Regla: antes de escribir código que lea un CSV/JSON, verifica el nombre exacto con `head -1 <csv>` o contra "Esquema de datos clave". No escribas ningún lector de datos de memoria.
2. **Concluir con n insuficiente**. Regla: ninguna conclusión de estrategia con n<15; ninguna promoción/desactivación fuera de los umbrales documentados (live: IC≥0.08 n≥40; desactivar: IC<-0.20 n≥15). Todo análisis cita n, IC y fichero fuente.
3. **Confundir shadow con live**. `results.csv` = simulado, `data/live/trades.csv` = dinero real. Regla: al reportar PnL di siempre cuál de los dos es.
3b. **Contar FILAS de `libro_snapshots.csv` como si fueran señales**. Una señal genera una fila por cada reintento (~20 s): contar filas subestima la fill-ability 4-8x. Regla: **la fill-ability se mide colapsando por `market_id`**; el script canónico `analisis_fills.py` ya lo hace (lista `PRIORIDAD`). No recalcular ad-hoc. Antes de declarar que una métrica central está mal, comprobar cómo la calcula el script canónico.
3c. **Medir con el precio de la señal o con el precio final.** `results.csv` mide a `precio_yes_mercado` (desfasado, infla +0,3/+0,7 €/tr). Regla: ningún gate/promoción nuevo se mide con `precio_yes_mercado`; siempre con `ask_real.py`. Y nunca usar el precio final del mercado ni un snapshot posterior a la decisión (look-ahead: `feedback_lookahead_bias_precio_final_no_es_edge_05ago`).

**Errores de código:**
4. **"Simplificar" o refactorizar código de seguridad live** (circuit breakers, vetos, Kelly, whitelist, frenos). Regla: solo con petición explícita del usuario, y cada guardia nueva es fail-closed (ante error/dato faltante → NO operar).
5. **Experimentar en producción**. Regla: experimentos en `/root/polymarket-research-dev`. En main solo fixes verificados. Nunca un `python3 -c` inline que escriba en `data/` de producción. El watchdog auto-reinicia ejecutores live al cambiar su .py: preparar en dev, revisar y copiar a main de una vez (`feedback_watchdog_autodespliega_ejecutores_live_24sep`).
6. **Escribir código que ya existe**. Regla: decisión ladder antes de cada función nueva.
6b. **Logger nuevo sin plan de disco**: gz diario + retención + fuera de git (`feedback_disco_nuevos_loggers_gz_retencion_29sep`).

**Errores de operación:**
7. **Resolver conflictos git de data/ a mano**. Regla: `git checkout --theirs data/shadow/*.json data/prices/*.csv` — siempre theirs, los loops son la fuente de verdad. No hacer git manual en horario live si se puede evitar; el `index.lock` lo toma el commit automático del loop: esperar y reintentar, no borrar.
8. **Reiniciar screens/loops como primer reflejo**. Regla: primero diagnostica (`logs/fast.log` — los tracebacks live van ahí, NO a live.log; `data_quality.json`; `screen -ls`). El watchdog ya reinicia solo; si reinicia él y tú, duplicas procesos.
9. **Tocar el weather bot**. `/root/polymarket-weather` es independiente, con su propio CLAUDE.md. No mezclar datos, código ni params.

**Escalación (cuándo preguntar al usuario):**
- **Preguntar SIEMPRE**: cambios que afectan dinero real (params de riesgo live, stakes, frenos, whitelist, switch on/off), borrar datos históricos, `git push --force`.
- **Autonomía plena**: params shadow, hipótesis custom, análisis, notas, código en dev.
- **Parar y surfacear** (no adivinar): columna/clave que no existe, JSON corrupto, PnL que no cuadra entre ficheros, cualquier número que contradiga a otro.

**Pase de casos límite ANTES de escribir código que toque dinero** (en este orden, siempre — cada categoría es una cicatriz real):
1. ¿El dinero no cuadra? → definir qué hace el sistema (parar, no "log y seguir")
2. ¿La API falla a medias? (orden enviada sin confirmación, auth caduca mid-ciclo) → estado recuperable
3. ¿Se puede ejecutar dos veces? → idempotencia (ledger ya_operados; la señal viva reintenta cada 20 s)
4. ¿Datos viejos o faltantes? → fail-closed (_cargar_spot silencioso, veto_sin_datos)
5. ¿Límites del exchange? → min $1, min_order_size 5 shares, decimales, tick size
6. ¿Reinicio a mitad? → estado persistente, no en memoria (freno ventana stateless → latch)

**Barra de calidad por entregable (checkeable, no adjetivos):**
- Cambio de código: `python3 -m py_compile <fichero>` pasa + `python3 verify_deploy.py` sin STALE (si toca proceso persistente, `--restart <screen>`) + el commit no mezcla código con ficheros de `data/`.
- **Código que toca dinero** (`live_trade.py`, `live_stake.py`, `live_guard.py`, `config_live.json`, cualquier ejecutor con envío real): además, `/code-review` adversarial ANTES de commitear — sin excepción.
- Análisis: incluye n, IC, periodo y comando/fichero de origen reproducible.
- Cambio de config: valor antes→después + quién lo aprobó + fecha, en el commit o en una nota `_pares_*` de `config_live.json`.
- Reporte de estado: cada afirmación "hecho/funciona" apunta a la salida de un comando de esta sesión.
- **Promoción a `pares_permitidos_live`** (Javi 31-Jul): gates estadísticos (n≥40, IC≥0.08, Wilson no cruza 0.5, shuffle p<0.05, PnL bootstrap CI90% no cruza cero, fill-ability real, `analisis_log_growth.py` con g>0 a f=10 %, pnl medio ≥0,10 €/tr al ask real) + tabla de conexión de la tupla exacta contra TODO el inventario (6 categorías: ballenas, gates propios, aprendizaje causal, selección adversa/fill-ability, payout/sizing, checks estructurales) — plantilla en `project_checklist_conexion_promocion_live_31jul`. Cada "no conectado pero aplica" es una acción previa. Nunca atajos (`feedback_zonas_no_saltan_protocolo_live_24sep`); esperar 2-3 días de veredicto estable antes de un flip a real.
- **Veto de micro-bucket de precio — mecanismo único, `gate_bucket_propio.py::evaluar(tupla_str, py)`, obligatorio en TODO ejecutor de tupla live** (Javi 05-Ago: *"tiene que vetar lo malo y exigir operar en lo bueno, tiene que aprender"*):
  - NO crear tablas de zonas hardcodeadas por ejecutor.
  - Tupla en `pares_permitidos_live` → exigir `veredicto == "bueno_confirmado"` (fail-closed; vetar solo `malo_confirmado` es insuficiente). Los candidatos DRY_RUN observan sin restricción.
  - El estado se regenera solo a diario (`analisis_gate_bucket_propio_28jul.py`; Wilson n≥15 + shuffle + split-half + BH-FDR por familia+moneda). Fuentes ADITIVAS que solo promueven un `sin_concluir`, nunca pisan un veredicto propio: `_ZONAS_VALIDADAS_EXTERNAMENTE` y `gate_bucket_fino.json` (`analisis_gate_bucket_fino.py`, ventana deslizante con permutación max-statistic; cron 07:18 vía `vigia_gate_bucket_fino.py`).
  - **4º veto, ASK REAL** (24-Sep): `ask_real_por_senal.py` (cron 05:40 → `ask_real_por_senal.csv`, `gate_bucket_ask_real.json`), lector `ask_real.py`; `_veto_ask_real()`: un bueno solo sobrevive con ≥+0,10 €/tr al ask, n≥15 e IC90 por días >0. `kelly_precio_gate._cargar()` caduca a las 48 h.
  - Tupla recién promocionada sin n≥15 propio por bucket: gate riguroso previo (fee real, `gross_win=(1-p)/p`, precio en el CRUCE real del umbral) contra, por orden, histórico externo → `data/markets/*.csv` × `outcome_real` → `results.csv`; cruzar SIEMPRE contra `franja_milimetrica_ballenas.json`/`punto_confirmacion`. Herramienta: `analisis_gate_microbucket_precio.py`. Ejemplos: `idea_veto_microbucket_ballenas_eth5min_05ago`, `idea_veto_microbucket_favorito_confirmado_btc_05ago`.
  - Un gate por filas no mide días independientes ni concentración de wallet: exigir ambos (`idea_precierre_bnb30_y_sniper_btc15_cluster_dias_20sep`).

**⚠️ NO "arreglar" el timestamp de `predictions.csv`** (`idea_caducidad_senales_filtro_protector_28jul`): `shadow_predict.py` calcula `ts` una vez por ciclo y las señales llegan a `live_trade` por encima de `SENAL_MAX_LATENCIA_SEG=100`. Parece un bug y no lo es: las caducadas que sí eran ejecutables dan pnl/trade NEGATIVO en 11 de 12 tuplas (−96,46 €). Actúa como filtro contra la selección adversa. Quien proponga tocarlo debe replicar antes ese desagregado por libro.

## 🪤 Trampas ya cazadas — siempre delante, no en el archivo
Cada línea es un error real del proyecto. Antes de concluir, promocionar, refutar o construir, comprobar que no se está repitiendo ninguna. Al cazar una trampa nueva: **añadir aquí su línea en la misma sesión** (el relato, a memoria).

**Medición y precio**
- `results.csv` mide al precio de la SEÑAL: de 49 `bueno_confirmado` solo 4 sobrevivían al ask real. Medir siempre con `ask_real.py`.
- Look-ahead, tres veces: precio final del mercado como entrada; snapshot de libro posterior a la decisión (el +0,307 €/tr del reactivo GBM, 22-Sep); último trade en lugar de ask (A3 "+0,2/+0,7 €/tr" → negativo al ask real).
- Precio de trades posteriores como proxy del ask tras un salto de Binance: OPTIMISTA (backtest +2,6/+13,9 % por € vs −6 % al ask real a +0,3 s). Tras un salto el ask sube 1,3-3,6c en <300 ms; lo que se imprime son fills sobre órdenes viejas. Y Polymarket aplica un taker delay de 150 ms: con ~250 ms de camino de orden llegamos a ~400 ms. Todo edge que exija comprar en <300 ms tras un evento público está cerrado para un tomador.
- Un prior tomado del último trade puede estar rancio (A3b: el "+22-30c a 4 s" era eso; con libro real el ask ya se movió a +0,3 s).
- Agrupar eventos por activo en vez de por `slug` de mercado, o usar `ts_epoch` = apertura de la ventana en vez del timestamp real, fabricó un EV positivo falso (A3 BTC+Up segundo salto).
- Backtest in-sample ≠ forward: precierre multi-instante +0,089 in-sample → +0,01 forward; ventanas finas elegidas con todos los datos, solo 37 % positivas fuera de muestra; los micro-buckets no persisten solos. Lo único que ha mantenido el signo en walk-forward es la estabilidad temporal (positivo en todos los tramos + días independientes).
- Precio medio ≠ BID/ASK ejecutable (colas de escaleras, stink bids): medir al lado que de verdad se cruza.
- Una medición con latencia de segundos no refuta una idea de velocidad; y a la inversa, un edge medido con snapshots de 10-20 s no demuestra que sea capturable.
- PolyBolt `price.crypto` (nuestro canal `spot` en `polybolt_*.csv`) es de **Pyth**, no de Chainlink (campo `source`; 0 % de coincidencias exactas, mediana 0,2-0,5 bps, máx 45 bps). Solo `twap60` es Chainlink. El failover de `fetch_polybolt_prices.py` escribe ese spot Pyth en `chainlink_*.csv` con `source=polybolt_fallback`: filtrarlo antes de medir o decidir algo que dependa del oráculo de resolución.
- La regla real de resolución es TWAP60 de cierre vs TWAP60 de apertura (Chainlink), no spot vs spot (88-95 % de coincidencia) ni klines Binance/Kraken (en gaps estrechos invierten el orden: roturas de garantía del nested arb).
- Fee: cripto 0,07, sports 0,05 (F1 0,03). No copiar el fee entre repos/modelos; usar el fee real del mercado.
- `gross_win=(1-p)/p`, nunca `(1-p)`.

**Estadística**
- n pequeño que parece señal y se evapora: wallets nuevas (+0,034 con n=369 → nada con n=1.910); `SNIPER#BTC#15min[0.10,0.15)` (gate n=49 bueno, verificación independiente n=13 con g negativo).
- Buscar entre muchas celdas/ventanas y testear la mejor con shuffle simple infla falsos positivos (p=0,0073 → 0,262 con max-statistic; sports H2 p=0,010 con 27 celdas miradas). Corregir por multiplicidad (max-statistic, BH-FDR, Bonferroni).
- Un gate por FILAS no mide días independientes, ni mercados distintos, ni concentración de wallet: un "edge" puede ser un bot (DOGE 5min), una wallet (0x1b41, 0x4f29) o un día. Exigir días, mercados y wallet top ≤30 %.
- Los veredictos de gate revierten: 26-Ago, 6 de 8 el mismo día; bot wallets, 184 confirmaciones → 0 (espejismo previo). Esperar 2-3 días estables.
- El agregado engaña: `resolution_sniper_observer` 96-100 % agregado, subconjunto accionable n=4-21 y margen marginal; Kelly-precio por familia habría dado a XRP un boost que no tenía; `CANDIDATA10_CONFIRMACION_CRUZADA` positivo solo por artefacto de stake-Kelly.
- El grid fijo de 0,05 puede diluir un edge más estrecho (BALLENAS_TARDIAS#ETH#5min: edge en [0,05-0,09), la cola [0,09-0,10) perdía el 100 %).
- IC/hit alto no es dinero: payout inverso (FAVORITO_CONFIRMADO BUY_NO 15min, ETH 60min; `FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION` con ic_bayes +0,14/+0,23 y −85/−181 € por moneda). Pasar siempre `analisis_log_growth.py`.
- Join aproximado entre fuentes crea señales falsas (P26: 27,4 % vs 15,2 % desapareció con join exacto).
- Muestra sesgada por un proceso en inanición (resolver de sports: 3 buckets "reales" eran sesgo; A3 × ballenas con cobertura del 17 %).
- Un resultado espectacular es, primero, un bug: `shadow_pnl_fiel` +13.148 $ era un estado absorbente (real −2.637,94 €).

**Fill-ability y selección adversa**
- El universo de bots (`bot_wallets_universo_25ago.json`) está FIJO desde el 24-Ago y el de Wallet Mirror elige por acierto frente al 50 %, no por PnL neto: de 90 tomadoras que ganaban de forma persistente solo 7 y 6 estaban dentro. Seleccionar wallets por neto de fee y con validación forward.
- Copiar a las ganadoras tarde no captura nada: el precio sube ~5,7c en los 5 s ANTERIORES a su compra y solo ~1c después; con ~8 s de retraso la copia dio −3,8 % por €. Medir siempre el perfil de precio alrededor de la entrada (`analisis_perfil_entrada_por_estrategia_30sep.py`): si en los 2 s previos ya no se mueve, llegamos tarde; si venía CAYENDO hacia nuestra entrada, compramos el cuchillo.
- Comprar ambos lados (pares) con órdenes quietas pierde: como tomador −2/−5c por mercado, como maker pasivo −6/−10c (la pata suelta es casi siempre la perdedora). Las wallets pasivas son el peor grupo del mercado (−2,28 % del volumen). Sin cancelación/recotización rápida no es replicable.
- Las señales vetadas por profundidad aciertan MÁS que las ejecutadas; cuando el libro recupera profundidad el hit cae 20-46 pp (P22). Esperar al libro no rescata nada.
- Filtros que funcionan en shadow se invierten en el subconjunto fillable (P25, P27 candidata 2, 3 de 5 confirmaciones del gate fino).
- Maker pasivo: los rellenos aciertan 71-77 % frente a 90 % del total (selección adversa desde el otro lado).
- Fill-ability contra `libro_snapshots.csv` genérico (ciclo ~20 s) es FALSA para tuplas con ejecutor de baja latencia; usar el observer/ejecutor dedicado. Y comprobar la fecha de despliegue del observador antes de cruzar.
- Contar filas de `libro_snapshots.csv` subestima la fill-ability 4-8x (colapsar por `market_id`).
- El libro público con profundidad perfecta no implica que se acepten órdenes: post-cierre, 59/59 órdenes reales rechazadas ("trading is disabled"); a T-2 s también hubo rechazo. El corte real del exchange es ~T+1,5 s y a T-2 s casi no hay asks del ganador (los ask 0,01 pierden).
- Subir el stake fuerza el libro: el des-pineo 1,05→1,75 dio corr(stake,acierto) = −0,32.
- Entrar caro mata: breakeven = precio de entrada. FAVORITO 60min BUY_YES entraba con 29-66 min restantes, donde "confirmado" no confirma nada.
- Un régimen cambia y borra un edge de latencia (fade del sniper tras el fix TWAP: 12-47 % → 89-90 % de acierto naive).

**Lógica de decisión y código**
- Clave de feature que no existe → estrategia muerta en silencio (`GBM_LATE_15M_MULTIHORIZONTE`, con docstring que afirmaba lo contrario).
- Estados absorbentes: 38/43 estrategias desactivadas sin poder acumular; `suelo_disparado` que nunca se resetea.
- Filtros causales que pasan a cubrir el 85-100 % de los casos reales (17/104).
- Vocabulario distinto entre módulos: `BUY_Up/BUY_Down` invisible a código que solo conoce `BUY_YES/BUY_NO`.
- Tablas hardcodeadas por ejecutor, producto cartesiano en la whitelist, decimales del CLOB, min size $1 y 5 shares, freno de ventana sin estado: todos escritos por un agente convencido de que estaban bien → `/code-review` siempre.
- Dedup permanente `(wallet, mercado)` descartaba convicción repetida de wallets ya validadas.
- `edge_dir=None` en un re-quote se saltaba el aborto por edge evaporado; un ejecutor sin re-chequeo de circuit breaker justo antes de disparar. Revisar ambos en todo ejecutor nuevo.
- Boosts horarios apilados cuentan el mismo fenómeno 2-3 veces (P15). Blacklist horaria invertida por mezclar direcciones (h10/h11 eran buenas en BUY_NO).
- Auto-apply aplicó un bucket contaminado sin revisión: por eso está desactivado.
- Una fuente ADITIVA nunca abre una zona dentro de un bucket `malo_confirmado`; decidirlo con Javi, no forzarlo.
- El "bug" del timestamp de `predictions.csv` protege contra la selección adversa: no arreglarlo.
- Guardia de `ballenas_executor_15min.py`: descartar activos cuya banda operativa favorezca NO en vez de YES.

**Operación e infraestructura**
- Vigías con latch cuya firma incluye un valor recalculado cada ciclo → spam (737 avisos en 5 días), dos veces.
- Vigías con timeout fijo mueren al crecer los datos; uno bloqueó el gate de un ejecutor REAL durante horas. Un vigía que compara contra la clave equivocada nunca detecta nada: probarlo con un cambio simulado antes de fiarse.
- Avisos de Telegram enviados una vez y nunca atendidos (tuplas en payout inverso sangrando semanas). Loggers acumulando 23 días sin que nadie mirase su criterio ya cumplido.
- Screens sin registrar en watchdog/`verify_deploy` no se reinician si caen.
- CPU: load 9,6-15 en 2 cores rompió el push 4 h en silencio (~1.650 commits sin backup). Cada proceso nuevo consume presupuesto.
- OOM: cargar `results.csv` entero, `list(DictReader)` en resolvers, `.tmp` dentro de `data/`. Postmortem atascado >10 min por un fit que se volvió O(n²): 3 trades reales sin cerrar.
- Disco: loggers sin rotación llevaron el disco al 100 %. `results.csv` fuera de git por el límite de 100 MB.
- `index.lock` huérfano = `git add` del lote automático; no borrar, esperar.
- Reiniciar `observadores` pierde el histórico ms en memoria y las fotos pendientes.
- Recalcular a mano algo que un proceso ya mantiene en vivo (`ballenas_observer.py`): mirar el inventario antes.
- Proponer como "nuevo" algo que ya está en el pipeline; declarar muerta una idea sin agotar el toolkit; refutar con la fuente de fill-ability equivocada.
- Perps: los fills no son unidades independientes (363 cierres por apertura); la API da 429 con 360 consultas/hora.
- Mercados "ya decididos": un solo fallo es −100 %; hace falta acierto ≥99 % medido, no supuesto.

**Test de humo para un modelo nuevo** (si respondes mal alguna, relee este manual antes de tocar nada):
1. El shadow ganó +100€ hoy. ¿Cuánto es cobrable en live? → *No extrapolable: el shadow no mide fill-ability; la conversión medida ronda el 8% y las señales vetadas por profundidad aciertan MÁS que las ejecutadas (selección adversa).*
2. Un bucket muestra IC=+0.30 con n=12. ¿Se promociona o se filtra? → *Ni lo uno ni lo otro: n<15 no concluye nada. Y si el resultado es espectacular, la primera hipótesis es un bug.*
3. Quieres el PnL de results.csv y el IC de strategy_params. ¿Qué columnas/claves? → *`pnl_neto` (no "pnl") e `ic_bayes` (no "ic_efectivo"). Si dudaste, `head -1` antes de escribir código.*
4. Una señal live llega y la consulta del libro falla. ¿Se ejecuta? → *No. Fail-closed: sin datos → no operar. Nunca al revés.*

---

## Skills (`/nombre`)
| Skill | Descripción |
|---|---|
| `/inicio` | Estado general: bankroll, IC, alertas, live, arb |
| `/ic` | IC detallado por subtipo, tendencia ult20, progreso live |
| `/hipotesis` | Estado hipótesis: veredicto + próxima acción |
| `/decision` | Plan de acción priorizado con cambios exactos |
| `/analizar <estrategia>` | Features por bucket, umbrales óptimos (usar cuando n≥30) |
| `/calibrar` | Revisar BLACKLIST_HOURS, DELTA_MIN/MAX, drift thresholds (cada 50+ ops) |
| `/dev` | Worktree dev sin tocar producción |
| `/verify-deploy` | Tras editar cualquier .py: ¿los procesos persistentes corren lo del disco? |

**Flujo sesión**: `/inicio` → `/decision` (si alertas) → `/analizar X` (n≥30) → `/calibrar` (c/50 ops nuevas)

## Worktrees
```
/root/polymarket-research      # main — PRODUCCIÓN (loops corriendo)
/root/polymarket-research-dev  # dev  — experimentos
git merge dev --no-ff          # promover desde main
```

## ⚠️ Sistema hermano INDEPENDIENTE: weather bot
`/root/polymarket-weather` (repo privado) — mercados de temperatura, cron propio. **NO mezclar** datos, código, params ni métricas; este CLAUDE.md no aplica allí. Tampoco mezclar dinero de sports con cripto (`feedback_no_mezclar_dinero_sports_cripto_03sep`).

---

## Objetivo
Bot semi-autónomo para mercados cripto de Polymarket. **200.000 €/año limpios por modelo (Cripto, Sports, Weather), año 1**; crecimiento orgánico, operando todos los días, mentalidad fría/calculadora/competitiva. 6 stages con gates falsificables (0 cerrar el gap modelo↔realidad → 1 ventanas horarias → 2 despinear stake → 3 mercados más profundos → 4 portfolio de motores no correlacionados → 5 compounding). Mecánica: `project_plan_escalonado_200k_23jul`; fechas: `project_calendario_200k_11ago2027`. **Cada sesión: situar en qué Stage está el sistema y qué gate falta, con datos frescos — nunca citar cifras de memoria.**
- **Capital / PnL real**: leer `data/shadow/estado_actual.md` y `data/live/trades.csv` (cualquier cifra escrita aquí caduca).
- **Umbral live**: IC≥0.08, n≥40 (`config_live.json::riesgo.min_ic_para_live`) **+** `python3 analisis_log_growth.py <strategy> <subtype> <decision>` con g>0 a f=10 % (un IC/EV positivo puede convivir con crecimiento compuesto negativo: "payout inverso").
- **VPS**: Hetzner Helsinki (IP finlandesa, Polymarket accesible).
- **Tuplas live**: la ÚNICA fuente de verdad es `config_live.json::pares_permitidos_live` (nivel TOP del JSON, no dentro de `riesgo`). Historia de cada promoción/pausa/retirada: notas `_pares_*`/`_candidatos_*` del mismo JSON, Obsidian `03_decisions/` y archivo (sección "Objetivo"). No mantener aquí ninguna tabla.
- **Regla de fondo confirmada con dinero real**: en apuesta binaria el breakeven ES el precio de entrada. Entrar barato (~0,39) da ratio W/L ~1,5; entrar caro (0,58-0,68) da 0,40-0,72 y exige un hit-rate que cualquier degradación mata. Priorizar candidatas de entrada a precio bajo (`project_drenajes_live_barrido_28jul`).
- **Protecciones live** (no tocar sin petición explícita, regla 4): re-quote contra el libro (aborta si edge<0,02) · techo 2 posiciones abiertas misma dirección · freno diario prospectivo (incluye stakes abiertos) · veto patrón causal si IC del subtype <0 · latch del freno de ventana (`freno_ventana_latch.json`) · veto CLV (clv_medio<0, n≥20, 7 d) · `slip_real=` en `notas` · veto de profundidad (ratio <5x stake o consulta fallida) · whitelist por tupla STRATEGY#SUBTYPE#DIRECTION · suelo prospectivo `bankroll_minimo` · `freno_diario_pct_override` con fecha · suelo de stake 1,05 € y guardia fail-closed <$1 · kill-switches propios de precierre/naive.

---

## Arquitectura
```
screen fast    → run_fast.sh   (~20s): klines→predict→live_trade→resolve→postmortem→resumen→push
screen slow    → run_slow.sh  (~23min): markets→wallets→trades→report→arb→push
screen control → live_control.py (Telegram: /on /off /status /help)
screen fetchers     → fetchers_fase0.py (1 hilo por fetcher: chainlink, liquidaciones, libro ambos lados,
                      activity WS, kalshi, PolyBolt TWAP oficial, binance bookTicker)
screen observadores → observadores_fase0.py (todos los observadores FASE 0, solo lectura)
screen vigiasfreq   → vigias_frecuentes_fase0.py
screen ejeclive     → ejecutores con envío real      screen ejecdryrun → ejecutores_dryrun_fase0.py
screen precierre / curvacierre → resolution_sniper_precierre_executor.py (PRECIERRE + NAIVE camino rápido)
screen walletmirror, sportsfase0, freezeestado, dryrunmc, nestedarb, mantenimiento, watchdog, dash
cron */5       → watchdog_fast.sh (checks, restart screens, alerta disco)
cron diarios   → vigías y análisis (horas UTC verificadas contra crontab el 30-Sep); `crontab -l` es la fuente de verdad
```
La lista real de screens y su frescura la da `python3 verify_deploy.py`; el mapa completo de scripts, `python3 inventario_sistema.py`. Qué hace cada fetcher/observador histórico: archivo (sección "Arquitectura").

**Scripts clave:**
| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min — Binance primario, Kraken fallback |
| `shadow_predict.py` | Estrategias → predictions CSV con features JSON |
| `live_trade.py` | Trades reales vía py-clob-client |
| `shadow_resolve.py` | Resuelve preds, PNL Kelly, cierra trades live |
| `shadow_postmortem.py` | IC bayesiano + Kelly + aprendizaje causal → `strategy_params.json` |
| `shadow_resumen.py` | `estado_actual.md` cada 60 s |
| `arb_scanner.py` | ~2400 mercados → `arb_scan_YYYY-MM-DD.csv` |
| `data_quality.py` | 4 capas L1-L4 → `data_quality.json` |
| `live_guard.py` | Switch + ventanas horarias → ¿puede operar? |
| `live_stake.py` | Kelly stake + circuit breakers (+ `kelly_precio_gate.py`, desagregado por familia×activo#marco×bucket) |
| `hypothesis_tracker.py` | Hipótesis builtin + custom JSON (auto-apply DESACTIVADO desde 15-Jul: solo avisa por Telegram) |
| `pipeline_watchdog.py` | Checks, restart screens, rotación de logs, alerta de disco |
| `dashboard_server.py` | http://37.27.249.72:8888 |
| `nested_arb_scanner.py` | Arb de contención de ventanas anidadas + sim FOK → `nested_arb_sim.csv` (P13) |
| `maker_sim.py` | Sim maker vs taker → `maker_sim.csv` |
| `fetch_chainlink_prices.py` | Precios Chainlink (resolución OFICIAL, distinta de Binance/Kraken) → `data/prices/chainlink_YYYY-MM-DD.csv` |
| `analisis_franja_milimetrica_ballenas.py` | pt.9 |
| `analisis_diario_ballenas_ejecutor.py` (06:21), `wallet_especialistas_observer.py` (06:33), `analisis_diario_franja_15min.py` (06:51) | Análisis diarios de ballenas/wallets, solo lectura → `data/shadow/*.json` |
| `gate_bucket_propio.py`, `analisis_gate_bucket_fino.py`, `ask_real.py` | Veto de micro-bucket (ver barra de calidad) |
| `analisis_fills.py` | Fill-ability canónica (colapsa por `market_id`) |
| `vigia_actualizaciones_polymarket.py` (06:42) | Cambios de reglas/fees/resolución de Polymarket (changelog + snapshot gamma-api) |
| `csv_incremental` (helper), `shuffle_chunked.py` | Lecturas incrementales de CSV grandes: usar siempre en vez de cargar `results.csv` entero (OOM) |

**Otras piezas vivas (índice; detalle en archivo):**
- Ejecutores: `ballenas_executor_5min.py`, `ballenas_executor_btc15m.py`, `ballenas_executor_15min.py`, `favorito_confirmado_btc60min_buyno_executor.py`, `favorito_altaconviccion_executor_15min.py`, `momentum_ibs_ballena_executor.py`, `wallet_mirror_sniper.py`, `wallet_mirror_executor_dryrun.py` (+ `wallet_mirror_clv.py`), `sports_wallet_mirror_sniper.py`, `resolution_sniper_naive_executor_dryrun.py`, `dispersed_bot_executor_dryrun.py`, `candidata9_bot_consenso_executor.py` (+ `candidata9_gate_bucket.py`).
- Fetchers/observadores: `fetch_kalshi_btc.py` (→ `data/prices/kalshi_btc15m_*.csv`, `kalshi_btchourly_*.csv`; Kalshi NO lidera, `idea_kalshi_lidera_binance_leadlag_19ago`), `fetch_libro_ambos_lados.py`, `ballenas_observer.py` (cruce de ballenas en vivo: no recalcularlo a mano), `candidatas_sin_fillability_depth_fase0.py`, `sol5min_contrario_fase0.py` (no replicó forward, `idea_sol5min_contrario_no_replica_forward_04ago`).
- Vigías/gates: `vigia_gate_bucket_fino.py`, `vigia_slippage_kill_switch.py` (06:15, solo alerta), `vigia_causal_vs_fillable.py`, `analisis_kelly_precio_gate_29jul.py` (→ `kelly_precio_gate.json`, re-ejecutar a mano), `analisis_nested_arb_gate.py`, `scan_blacklist_hours.py`, `entrenar_meta_score_gbm_late_p17.py` (→ `meta_score_gbm_late_model.json`).

---

## Sistema live trading
```bash
bash live_switch.sh on/off/status   # o Telegram: /on /off /status
```
**Ventanas (hora Madrid)** — fuente de verdad `config_live.json::ventanas_lunes_viernes`/`ventanas_fin_de_semana` (verificado 30-Sep). L-V: 08:30-09:30 | 10:30-11:30 | 15:00-23:00 | 01:00-02:00 | 02:00-06:00 (madrugada, abierta para FAVORITO#BTC#60min) | 06:00-07:00. Fin de semana: 15-16 | 17-18 | 19-20 | 21-22 | 23:00-23:59 | 01-02 | 06-07. `live_guard.py` no maneja cruce de medianoche (por eso 23:59). `RESOLUTION_SNIPER_PRECIERRE` opera sin ventanas.
**Stake**: `min(IC × bankroll × 0.5, bankroll × 10%, max_stake)` — valores reales en `config_live.json::riesgo`.
**Circuit breakers**: bankroll bajo el mínimo → OFF | caída diaria → para el día | caída de ventana → para la ventana (umbrales en `config_live.json`).
**Credenciales**: `data/live/.env` (gitignored).
**Telegram**: señal detectada | cada orden real (ejecutada o rechazada) | circuit breaker | digest diario 20:00 UTC.

---

## Hipótesis — estado resumido
Estado vivo en `data/shadow/hipotesis_auto.md` (cada postmortem).

| Hipótesis | Estado | Acción / Config activa |
|---|---|---|
| H-REGIMEN | ❌ REFUTADA | Filtro solo 60min+ BUY_NO drift>0.7%/h |
| H-60MIN | ✅ CONFIRMADA | Acumulando |
| H-ORDER_FLOW-DECAY | ✅ IMPL | DELTA_MAX=0.46 |
| H-VENTANAS-HORARIAS | ✅ IMPL | OF_BLACKLIST_HOURS |
| H-DRIFT60-BUY_YES_15MIN | ✅ IMPL | BUY_YES #15min: drift_60min∈[0,+0.25%) |
| H-DRIFT15-MOMENTUM | ✅ IMPL | BTC#15min: skip si drift_15min<0.3%/h |
| H-BTC-ETH-MOMENTUM-REVERSION | 🔬 TRACKING | ETH drift<-1 → n≥20 → boost ×1.1 |
| H-OU-5MIN | ❌ DESACTIVADA | IC=-0.229 |
| H-5MIN-REVERSIÓN | ✅ CONF | GBM#5min desactivados |
| H-WEEKLY-PRICE | ⏳ | esperar n≥15/par |
| H-GBM-18H, H-KELLY-HORA, H-BLACKLIST-02H/07H | ⏳ AVISO | solo avisan por Telegram, aplicar a mano |
| H-CROSS-ASSET | ⏳ n→20 | GBM+OF BUY_NO mismo activo → boost ×1.5 |
| H-CUSTOM-PHOTO-FINISH-SNIPER | ❌ REFUTADA 28-Jul | — |
| STRUCT_NO_15M | ⚠️ **NO PROMOCIONAR** | leer `idea_structno_no_replica_fills` antes de proponer whitelist |
| LEADLAG-BTC-XRP | ⚠️ TRACKING, expectativa BAJA | revisar con n≥40 sin sesgo |

**Hipótesis custom** en `data/shadow/hipotesis_custom.json` (editar sin tocar código).

## Aprendizaje causal
```
predictions (features JSON) → postmortem:
  IC_bucket < -0.12, n≥15 → filtro_causal (skip en predict)
  IC_bucket > +0.12, n≥15 → patron_ganador (kelly_boost)
→ strategy_params.json → siguiente ciclo
```
**Features GBM**: `{pct_spot_vs_ref, sigma_h, T_h, drift_15min, drift_60min, delta_ratio_macro, hora_utc, ibs_15, ref_es_twap, meta_score_gbm_late, bot_consenso_*}`
**Features OF**: `{delta_ratio, total_vol_5m, has_real_flow}`

---

## Prioridades pendientes
Una línea por ítem; evidencia completa en archivo (sección "Prioridades pendientes") y en la memoria citada.
| P | Tarea | Estado / condición |
|---|---|---|
| P19 | Gap sigma implícita vs realizada como filtro GBM | Acumular forward. Solo los 7 combos robustos, nunca BTC. `/code-review` + OK Javi antes de tocar `prob_yes`. `idea_gap_sigma_replicado_por_familia_activo_22jul` |
| P20 | Meta-modelo de confianza sobre term-structure de vol | PAUSADO (Javi 23-Jul) hasta que P19 madure |
| P18 | Smart Exit (SL+TP) | SL implementado e inactivo. TP: NO en `FAVORITO_CONFIRMADO`; `GBM_LATE_15M` vigilado por `vigia_touch_vs_win_p18.py`. Bloqueo por min_order_size=5 (`project_smart_exit_bloqueado_min_shares_clob_17sep`) |
| P24 | Wallet Mirror micro-bucket | Ver pt.20 y `project_masterizar_wallet_mirror_sniper_disperso_29sep` (veto CLV listo para `/code-review` + OK) |
| P28 | Payout/varianza (5 hilos) | Kelly exacto y HRP sin integrar; `/code-review` antes de `live_stake.py`. `project_decisiones_payout_varianza_23jul` |
| P29 | Backlog Moon Dev | Stage 0 hecho; Box Builder y Spread-Harvest REFUTADOS; Corridor Collector = P13. `idea_moondev_10_hallazgos_priorizados_28jul` |
| P21 | LP farming / rewards | REABIERTO 29-Sep: `idea_rewards_liquidez_mercados_sin_competencia_29sep`; prueba real solo con OK Javi |
| P13 | Nested arb → live | NO promocionar: la garantía rompe 18,7 % (−10 $/trade). Siguiente: cruzar roturas con `chainlink_*.csv`. `idea_p13_nested_arb_corridor_collector_reanalisis_04ago` |
| P17 | Meta-score Ridge sobre GBM_LATE (`meta_score_gbm_late`, solo logueo) | No cambiar `prob_yes` sin OK Javi + `/code-review` |
| P15 | Doble conteo de boosts horarios en el stake | Relevante ya: `max_stake_eur`=2.0, no pineado al suelo |
| P35 | Kalshi como segundo venue (Stage 4) | No antes de cerrar Stage 0-3 salvo decisión de Javi |
| P6, P8, P10, P11 | Cross-asset ×1.5 · OF rangos per-par · ETH#15min reversión · blacklist OF 02h/07h | Esperando n (≥20 / ≥200 / ≥20 / ≥20 por hora) |
| Cerrados, no reabrir sin evidencia radicalmente nueva | P14 (quedarse taker), P16, P22, P23, P25, P26, P27, P7 (mergeado), P12 (→P16) | — |

---

## Constantes clave
Los valores reales están en el código/JSON; verificar antes de citar.
### shadow_predict.py
```python
DRIFT_DAMPING = {5:0.30, 15:0.20, 60:0.05, 240:0.10}
REGIME_BUY_NO_THRESHOLD = 0.7    # %/h — solo ≥60min, solo BUY_NO
DRIFT_60_BUY_YES_15M_LO = 0.0 | DRIFT_60_BUY_YES_15M_HI = 0.25
BUY_YES_15M_TH_MAX = 0.2         # BUY_YES #15min solo tardío
EDGE_MINIMO = 0.02 | SLIPPAGE_ESTIMADO = 0.02 (dinámico: mediana slip_real si n≥30, clamp [0.005, 0.02])
GBM_LATE_DRIFT_VENT_MIN_PCT = 0.02
DELTA_MIN = 0.38 | DELTA_MAX = 0.46  # OF solo BUY_NO
KELLY_COMPUESTO_BOOST = 1.5 | KELLY_COMPUESTO_MAX = 2.00
ORDER_FLOW_BLACKLIST_HOURS = {2,7,9,22}  # UTC
ORDER_FLOW_PAIR_BLACKLIST  = {'BTC'}
```
### shadow_postmortem.py
```python
IC_FILTRO_MIN=-0.12 | IC_PATRON_MIN=+0.12 | N_BUCKET_MIN=15
UMBRAL_DESACTIVAR=(-0.20, 15)  # subido de 8 a 15 el 01-Sep
```
### live_stake.py / data/live/config_live.json
```python
max_pct_bankroll_por_trade | min_stake_eur=1.05 | max_stake_eur=2.0 (verificado 30-Sep en config; leer `_max_stake_nota` antes de tocarlo)
freno_ventana=0.20 | freno_diario → ver config (0.40 desde 22/24-Sep) | bankroll_min=1.00 | racha=4
Z_MIN_TWAP=1.8 (precierre, global)
# SELECCIÓN ADVERSA TAKER: los fills live aciertan mucho menos que las señales vetadas por profundidad.
# data/live/libro_snapshots.csv registra el libro de cada señal (motivos: ejecutada/veto_profundidad/
# veto_sin_datos/abort_requote/fok_kill/no_viable_stake/fuera_ventana). `python3 analisis_fills.py`.
# Maker descartado (EV negativo en todas las tuplas medidas con snapshots); con ms está en captura (pt.20).
```

## Esquema de datos clave (nombres exactos de columnas)
```
results.csv:       pnl_neto (NO "pnl") | acierto | strategy | subtype | decision | precio_yes_mercado | prob_yes_modelo
strategy_params.json: ic_bayes (NO "ic_efectivo") | n | activa | apuesta_kelly | ic_BUY_NO | ic_BUY_YES | n_BUY_NO | n_BUY_YES
trades.csv:        timestamp_utc | pnl_neto_eur | stake_eur | entry_price | status (OPEN/CLOSED/STUB) | direction | fee_eur | slip_real
                   ⚠️ edge_neto SIEMPRE en perspectiva YES: en filas BUY_NO el edge a favor es −edge_neto
```

## Ficheros clave
```
data/shadow/predictions_YYYY-MM-DD.csv  — features JSON por predicción (rotación 12 días)
data/shadow/results.csv                  — historial completo. Gitignored; backup diario scripts/backup_results_csv.sh
data/shadow/strategy_params.json         — IC, Kelly, filtros_causales, activa/desactivada
data/shadow/estado_actual.md             — estado del bot (c/60s)
data/shadow/hipotesis_auto.md            — hipótesis + patrones causales activos
data/shadow/hipotesis_custom.json        — hipótesis custom editables
data/live/config_live.json               — riesgo, pares_permitidos_live, candidatos_evaluacion_live
data/live/.env                           — credenciales (gitignored)
data/live/trades.csv                     — trades reales
data/live/libro_snapshots.csv            — libro de cada señal en fase de ejecución
data/live/LIVE_MODE_ON                   — touchfile switch
logs/fast.log                            — tracebacks live (NO live.log)
/root/polymarket-research-datalogs/      — loggers pesados fuera de git (gz + retención)
```

## Diagnósticos comunes
```
Git conflicto fast loop:            git stash && git pull --rebase && git stash pop && git push
prices CSV conflicto:               git checkout --theirs data/prices/YYYY-MM-DD.csv
live_control caído:                 screen -dmS control python3 live_control.py
dashboard caído:                    screen -dmS dash python3 dashboard_server.py
Bot no opera live:                  bash live_switch.sh status + verificar ventana horaria
OF IC negativo (3 bloques, IC<-0.05): subir DELTA_MIN a 0.45
strategy_params corrupto:           watchdog lo detecta; validar JSON + clave 'estrategias'
```
