# CLAUDE.md — Polymarket Research Bot
**Actualizado: 2026-07-06** | Live REABIERTO 06-Jul 06:00 UTC (objetivo: recuperar 8.50€, suelo 1€)

## Reglas de comportamiento
- **Fail Loud**: "completado"/"verificado" es INCORRECTO si algo se asumió sin confirmar explícitamente. Surfacear incertidumbre siempre.
- **Checkpoint**: en tareas ≥3 pasos, resumir tras cada paso qué está verificado y qué queda antes de continuar.
- **Antes de escribir código nuevo** (decisión ladder): ¿ya existe en el codebase? → ¿lo hace la stdlib/requests/csv/json? → ¿una línea? → solo entonces: mínimo viable. Excepción: código de seguridad live (circuit breakers, filtros end_date, Kelly) — no minimizar.

## ⚠️ Manual operativo — errores que NO cometer (escrito para cualquier modelo)
Cada error va con la regla que lo previene. Si dudas entre dos interpretaciones, aplica la regla, no tu intuición.

**Errores de datos:**
1. **Inventar nombres de columna/clave** (`pnl` en vez de `pnl_neto`, `ic_efectivo` en vez de `ic_bayes`). Regla: antes de escribir código que lea un CSV/JSON, verifica el nombre exacto con `head -1 <csv>` o contra la sección "Esquema de datos clave". No escribas ningún lector de datos de memoria.
2. **Concluir con n insuficiente**. Regla: ninguna conclusión de estrategia con n<15; ninguna promoción/desactivación fuera de los umbrales documentados (live: IC≥0.08 n≥40; desactivar: IC<-0.20 n≥8). Todo análisis cita n, IC y fichero fuente.
3. **Confundir shadow con live**. `results.csv` = simulado, `data/live/trades.csv` = dinero real. Regla: al reportar PnL di siempre cuál de los dos es.

**Errores de código:**
4. **"Simplificar" o refactorizar código de seguridad live** (circuit breakers, vetos, Kelly, whitelist, frenos). Regla: ese código solo se toca con petición explícita del usuario, y cada guardia nueva es fail-closed (ante error/dato faltante → NO operar).
5. **Experimentar en producción**. Regla: experimentos en `/root/polymarket-research-dev` (worktree dev). En main solo fixes verificados. Nunca un `python3 -c` inline que escriba en `data/` de producción.
6. **Escribir código que ya existe**. Regla: decisión ladder (arriba) antes de cada función nueva.

**Errores de operación:**
7. **Resolver conflictos git de data/ a mano**. Regla: `git checkout --theirs data/shadow/*.json data/prices/*.csv` — siempre theirs, los loops son la fuente de verdad.
8. **Reiniciar screens/loops como primer reflejo**. Regla: primero diagnostica (`logs/fast.log` — los tracebacks live van ahí, NO a live.log; `data_quality.json`; `screen -ls`). El watchdog ya reinicia solo; si reinicia él y tú, duplicas procesos.
9. **Tocar el weather bot**. `/root/polymarket-weather` es un sistema independiente con su propio CLAUDE.md. Regla: no mezclar datos, código ni params.

**Escalación (cuándo preguntar al usuario):**
- **Preguntar SIEMPRE**: cambios que afectan dinero real (params de riesgo live, stakes, frenos, whitelist, switch on/off), borrar datos históricos, `git push --force`.
- **Autonomía plena**: params shadow, hipótesis custom, análisis, notas, código en dev.
- **Parar y surfacear** (no adivinar): columna/clave que no existe, JSON corrupto, PnL que no cuadra entre ficheros, cualquier número que contradiga a otro.

**Pase de casos límite ANTES de escribir código que toque dinero** (en este orden, siempre —
cada categoría es una cicatriz real del proyecto):
1. ¿El dinero no cuadra? → definir qué hace el sistema (parar, no "log y seguir")
2. ¿La API falla a medias? (orden enviada sin confirmación, auth caduca mid-ciclo) → estado recuperable
3. ¿Se puede ejecutar dos veces? → idempotencia (cf. ledger ya_operados; señal viva reintenta cada 20s)
4. ¿Datos viejos o faltantes? → fail-closed (cf. _cargar_spot silencioso, veto_sin_datos)
5. ¿Límites del exchange? → min $1, decimales, tick size (cf. bug decimales CLOB, min size 03-Jul)
6. ¿Reinicio a mitad? → estado persistente, no en memoria (cf. freno ventana stateless → latch)

**Barra de calidad por entregable (checkeable, no adjetivos):**
- Cambio de código: `python3 -m py_compile <fichero>` pasa + `python3 verify_deploy.py` sin STALE (si toca proceso persistente, restart con `--restart <screen>`) + el commit no mezcla código con ficheros de `data/`.
- **Código que toca dinero** (live_trade.py, live_stake.py, live_guard.py, config_live.json): además de lo anterior, `/code-review` adversarial ANTES de commitear — sin excepción. Historia que lo justifica: bug decimales CLOB, freno ventana stateless, whitelist cartesiana — todos escritos por un agente convencido de que estaban bien; la auditoría del 01-Jul cazó ~20 bugs.
- Análisis: incluye n, IC, periodo y comando/fichero de origen reproducible.
- Cambio de config: valor antes→después + quién lo aprobó + fecha, anotado en el propio commit o en CLAUDE.md.
- Reporte de estado: cada afirmación "hecho/funciona" apunta a la salida de un comando de esta sesión.

**Test de humo para un modelo nuevo** (si respondes mal alguna, relee este manual antes de tocar nada):
1. El shadow ganó +100€ hoy. ¿Cuánto de eso es cobrable en live? → *No extrapolable: el shadow no mide fill-ability; la conversión medida ronda el 8% y las señales vetadas por profundidad aciertan MÁS que las ejecutadas (selección adversa).*
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
| `/verify-deploy` | Tras editar cualquier .py: ¿los procesos persistentes corren lo del disco? (`verify_deploy.py`, restart+probe) |

**Flujo sesión**: `/inicio` → `/decision` (si alertas) → `/analizar X` (n≥30) → `/calibrar` (c/50 ops nuevas)

## Worktrees
```
/root/polymarket-research      # main — PRODUCCIÓN (loops corriendo)
/root/polymarket-research-dev  # dev  — experimentos
git merge dev --no-ff          # promover desde main
```

## ⚠️ Sistema hermano INDEPENDIENTE: weather bot
`/root/polymarket-weather` (repo `polymarket-weather`, PRIVADO) — mercados de
temperatura, shadow puro, cron propio cada 3h. **NO mezclar**: datos, código,
params y métricas separados; este CLAUDE.md no aplica allí (tiene el suyo).
Solo comparten metodología (IC, shadow-first, umbral live).

---

## Objetivo
Bot semi-autónomo para mercados cripto Polymarket.
- **Fase actual**: live REABRE lunes 06-Jul 06:00 UTC (at job) tras congelación 03-05 Jul — objetivo recuperar 8.50€, para solo sin dinero (suelo 1€)
- **Capital**: 25.44€ operativo live (30€ depósito, 10€ reserva)
- **Umbral live**: IC≥0.08, n≥40 resoluciones confirmadas (valor real en `data/live/config_live.json::riesgo.min_ic_para_live`)
- **VPS**: Hetzner Helsinki (IP finlandesa — Polymarket accesible desde FI)
- **Estrategias live activas** (`pares_permitidos_live` real a 14-Jul noche, sesión siguiente): 7 tuplas — 5 BUY_YES en 3 monedas: `GBM_LATE_15M#SOL#15min#BUY_YES` (la original), `FAVORITO_CONFIRMADO#SOL#15min#BUY_YES` (post-embargo n=150 hit=73.3% pnl=+9.63€), `GBM_LATE_15M_ESPACIO_ATR#SOL#15min#BUY_YES` (post-embargo n=66 hit=59.1% pnl=+55.04€) y `GBM_LATE_15M_ESPACIO_ATR#BTC#15min#BUY_YES` (post-embargo n=138 hit=58.7% pnl=+77.56€ — primera vez que BTC opera dinero real) — ver notas `_pares_sol_promocion_nota_2026-07-14` y `_pares_btceth_espacioatr_promocion_nota_2026-07-14` en config_live.json para el diagnóstico completo — y **AÑADIDA 14-Jul noche** `FAVORITO_CONFIRMADO#SOL#60min#BUY_YES` (primer par 60min en vivo; IC=0.2143 n=40 sin contaminación de embargo — la estrategia nació el mismo 10-Jul; fill-ability 68.8% de 32 snapshots pasa veto 5x, mejor que el resto del sistema; solape temporal 100% con las SOL#15min pero el histórico real nunca superó 2 posiciones simultáneas, dentro del techo de correlación existente — ver nota `_pares_sol60min_promocion_nota_2026-07-14`) (mismo código ya probado — `s_gbm_late_15min_espacio_atr` reutiliza `_s_gbm_late()`, la función que SOL usa desde 03-Jul; fill-ability proxy ~29% calibrado contra el 6% real de SOL, CLV real positivo +0.16/+0.17; techo de correlación simulado con Monte Carlo sobre datos reales, solo ~0.07% de ejecuciones bloqueadas, no hace falta subirlo de 2). Más **1 BUY_NO, AÑADIDA 14-Jul noche (sesión posterior)**: `FAVORITO_CONFIRMADO#BTC#60min#BUY_NO` — primera tupla BUY_NO de vuelta en live desde que se retiraron todas el 06-Jul por selección adversa direccional; post-embargo n=40, hit=67.5%, IC=+0.167, Wilson=[0.545,0.782], p_shuffle=0.021, PnL post-embargo +7.08€, CLV post-embargo +0.0725 (positivo, la métrica que detectaría el mecanismo de selección adversa que sacó a los BUY_NO — sale limpia), fill-ability 67.4% de 46 snapshots. No comparte cupo de correlación con las 6 BUY_YES (`max_posiciones_abiertas_misma_direccion` cuenta por dirección). Requirió antes el fix direction-aware de `activa` (commit `cc8cf7897f`, mismo día) para que el veto live mirara solo el IC de BUY_NO y no el mixto. Ver nota `_pares_btc60min_buyno_promocion_nota_2026-07-14` en config_live.json. Pendiente: primer trade real, vigilar CLV/fill-ability en vivo. Más **2ª BUY_NO, AÑADIDA 14-Jul noche (misma sesión posterior)**: `FAVORITO_CONFIRMADO#ETH#60min#BUY_NO` — post-embargo n=42, hit=66.7%, IC=+0.159, Wilson=[0.540,0.773], p_shuffle=0.023, PnL post-embargo +4.16€, CLV post-embargo +0.0473 (positivo). Fill-ability 63.0% de 46 snapshots. Comparte cupo de correlación BUY_NO con `FAVORITO_CONFIRMADO#BTC#60min#BUY_NO` (`max_posiciones_abiertas_misma_direccion=2`, cuenta por dirección) — 2ª tupla en ese cupo, lo llena. Ver nota `_pares_ethbuyno_promocion_nota_2026-07-14` en config_live.json. Pendiente: primer trade real, vigilar CLV/fill-ability en vivo. **`GBM_LATE_15M_ESPACIO_ATR#ETH#15min#BUY_YES` PAUSADA 14-Jul (sesión siguiente)** — decisión Javi tras análisis fillable-vs-no-fillable (cruce libro real vs outcome shadow): el gap de selección adversa MÁS GRANDE de las 8 tuplas vivas de ese momento (fillable n=31 hit=19.4% pnl=-30.83€ vs no-fillable n=74 hit=79.7% pnl=+100.16€, gap=60.3pp). Hallazgo más amplio: las tuplas #15min tienen gaps de 26-60pp (PnL fillable siempre negativo) vs las #60min con gaps de solo 2.6-12pp (PnL fillable positivo) — coincide con que el 100% de la racha real perdedora 09-14Jul (-28.20€, n=64) fue en tuplas #15min. Retirada a `candidatos_evaluacion_live` (no descartada, sigue acumulando fill-ability). Ver nota `_pares_espacioatr_eth_pausa_nota_2026-07-14` en config_live.json. PENDIENTE general: vigilar si el resto de #15min (que siguen en whitelist, decisión explícita de no pausarlas todas de golpe) confirma el mismo patrón con más dato, y si los 60min (todavía 0 trades reales) sostienen el fillable-PnL positivo cuando empiecen a operar. **ETH#BUY_YES (GBM_LATE_15M, no ESPACIO_ATR) PAUSADA 14-Jul** (decisión Javi, diagnóstico degradación en vivo): últimos 30 ejecutados en negativo (hit=36.7%, -0.067€/trade) pese a shadow normal (últimos 50 hit=54.0%) — no es mercado plano, no es slippage, no es hora, es selección adversa taker concentrada por varianza (n=27, ver nota `_pares_eth_pausa_selectiva_nota_2026-07-14` en config_live.json para el diagnóstico completo). RE-AÑADIR cuando el filtro causal nuevo (`sigma_ewma_delta_pct<7.386`, hoy n=3 en vivo) acumule n≥15 propio y confirme, o últimos 30 vuelvan a positivo sostenido — decisión explícita de Javi en ambos casos. **Revisar viernes 2026-07-17** (petición Javi). XRP retirado de whitelist el 10-Jul (racha de pérdidas + decisión Javi, ver `project_state_2026-07-10`) — ya no opera dinero real, solo se mide en shadow. Todos los BUY_NO retirados del live 06-Jul (decisión Javi): **selección adversa direccional** — live BUY_NO 31% hit −16.33€ n=35 (todas las tuplas negativas) vs BUY_YES 53% +9.08€ n=36; el ask del NO lo cotiza flujo informado. Los BUY_NO siguen midiéndose en shadow (IC a plan positivo) y vuelven vía filtro fill-ability (`analisis_fills.py`: veto_profundidad 24/24 hit a plan, decisión formal con n≥30). ORDER_FLOW_5M fuera de whitelist. GBM_LATE_60M refutada (n=323, ic_bayes=-0.1123 hoy, negativa en los 3 activos BTC/ETH/SOL; sigue acumulando shadow-only vía `ACUMULAR_SHADOW_AUNQUE_DESACTIVADA` — el mismo mecanismo de GBM_LATE_15M no transfiere a 60min).
- **Protecciones live añadidas 2026-07-03**: re-quote contra libro al ejecutar (aborta si edge<0.02 con el ask actual) | techo 2 posiciones abiertas misma dirección (correlación multi-par) | freno diario prospectivo (pérdida+stake+**stakes abiertos**≤15%, fix tras -6.54€ el 03-Jul) | veto patrón causal si IC propio del subtype <0 | **latch freno ventana** (disparo → `freno_ventana_latch.json`, no reabre hasta la siguiente ventana; antes se rearmaba solo al recuperar PnL) | **veto CLV** (tupla con clv_medio<0 y n≥20 en ventana 7d → no ejecuta; guardia sobre el IC, no sustituto) | slippage real → `notas` (`slip_real=`) para calibrar SLIPPAGE_ESTIMADO con n≥30 | **veto profundidad libro** (ratio<5x stake o consulta fallida → aborta; XRP/SOL entraron contra libros vacíos con slip +0.04/+0.085) | **whitelist por tupla** `pares_permitidos_live` STRATEGY#SUBTYPE#DIRECTION (el producto cartesiano coló UPDOWN_GBM#SOL/BTC#15min) | suelo prospectivo bankroll_minimo (8→3€ el 04-Jul, 1€ desde 06-Jul) | override freno diario con fecha (`freno_diario_pct_override`, solo aplica el día indicado) | **suelo stake 1.05€** (CLOB rechaza marketable BUY <$1 "min size: 1"; 2 señales perdidas 03-Jul con Kelly 0.94/0.98€ tras caer el bankroll) + guardia fail-closed en live_trade si llega <$1

---

## Arquitectura — 3 loops en screen
```
screen fast    → run_fast.sh   (~20s): klines→predict→live_trade→resolve→postmortem→resumen→push
screen slow    → run_slow.sh  (~23min): markets→wallets→trades→report→arb→push
screen control → live_control.py (Telegram: /on /off /status /help)
screen pfinish → photo_finish_logger.py (captura photo finish c/frontera 5min)
cron */5       → watchdog_fast.sh (9 checks, restart screens, alerta disco)
```

**Scripts clave:**
| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min — Binance primario, Kraken fallback |
| `shadow_predict.py` | Estrategias → predictions CSV con features JSON |
| `live_trade.py` | Trades reales via py-clob-client (CLOB API activa desde 29-Jun) |
| `shadow_resolve.py` | Resuelve preds, PNL Kelly, cierra trades live |
| `shadow_postmortem.py` | IC Bayesiano + Kelly + aprendizaje causal → strategy_params.json |
| `shadow_resumen.py` | estado_actual.md cada 60s |
| `arb_scanner.py` | ~2400 mercados → arb_scan_YYYY-MM-DD.csv |
| `data_quality.py` | 4 capas L1-L4 → data_quality.json |
| `live_guard.py` | Switch + ventanas horarias → ¿puede operar? |
| `live_stake.py` | Kelly stake + 3 circuit breakers |
| `hypothesis_tracker.py` | 14 hipótesis builtin + custom JSON → auto-apply strategy_params |
| `pipeline_watchdog.py` | 9 checks, restart screens, rotación logs, alerta disco |
| `dashboard_server.py` | http://37.27.249.72:8888 (polling 1s, LightweightCharts) |
| `nested_arb_scanner.py` | Arb de contención ventanas anidadas (cron 1min) → nested_arb_YYYY-MM-DD.csv + **sim ejecución FOK** (05-Jul) → nested_arb_sim.csv (entrada a asks reales, cierre con outcome oficial, `garantia_ok`; paso a live: n≥30 con garantía ~100%) |
| `maker_sim.py` | Sim entrada maker vs taker (invocado por shadow_resolve) → maker_sim.csv |
| `photo_finish_logger.py` | Screen `pfinish`: libro del lado rezagado a T-10s en photo finishes (|dist|<0.15%) + outcome oficial → photo_finish_YYYY-MM-DD.csv (H-CUSTOM-PHOTO-FINISH-SNIPER, solo captura) |

---

## Sistema live trading
```bash
bash live_switch.sh on/off/status   # o Telegram: /on /off /status
```
**Ventanas (hora Madrid, L-V)**: 08:30-09:30 | 10:30-11:30 | 15:00-21:30 (fusionada 2026-07-02, sin huecos) | 01:00-02:00 (prueba, ≈23h UTC)
**Stake**: `min(IC × bankroll × 0.5, bankroll × 10%, 2€)` — compounding automático
**Circuit breakers**: bkr<5€→OFF | caída diaria≥15%→para día | caída ventana≥20%→para ventana
**Credenciales**: `data/live/.env` (POLY_PRIVATE_KEY + API_KEY + SECRET + PASS) ✅
**Notificaciones Telegram**: señal detectada | circuit breaker | digest diario 20:00 UTC

---

## Hipótesis — estado resumido
Estado live en `data/shadow/hipotesis_auto.md` (actualizado cada postmortem ~23min).

| Hipótesis | Estado | Acción / Config activa |
|---|---|---|
| H-REGIMEN | ❌ REFUTADA | Filtro solo 60min+ BUY_NO drift>0.7%/h |
| H-60MIN | ✅ CONFIRMADA | Acumulando — BTC n=32 ETH n=32 IC≈+0.059 |
| H-ORDER_FLOW-DECAY | ✅ IMPL | DELTA_MAX=0.46 (zona muerta [0.46-0.65] eliminada) |
| H-VENTANAS-HORARIAS | ✅ IMPL | OF_BLACKLIST_HOURS={2,7,9,10,11,22} UTC |
| H-DRIFT60-BUY_YES_15MIN | ✅ IMPL | BUY_YES #15min: drift_60min∈[0,+0.5%) |
| H-DRIFT15-MOMENTUM | ✅ IMPL | BTC#15min: skip si drift_15min<0.3%/h |
| H-BTC-ETH-MOMENTUM-REVERSION | 🔬 TRACKING | ETH drift<-1 → n≥20 → boost ×1.1 |
| H-OU-5MIN | ❌ DESACTIVADA | IC=-0.229 — confirmada 09-Jul con fills Jon-Becker (test causal sin lookahead, n=67k, nulo) |
| H-5MIN-REVERSIÓN | ✅ CONF | GBM#5min todos pares desactivados |
| H-WEEKLY-PRICE | ⏳ n=57 | SOL sostenido; BTC neg; esperar n≥15/par |
| H-GBM-18H | ⏳ AUTO | hypothesis_tracker auto-aplica cuando n≥15 IC<-0.08 |
| H-CROSS-ASSET | ⏳ n→20 | GBM+OF BUY_NO mismo activo → boost ×1.5 |
| H-KELLY-HORA | ⏳ AUTO | Solo H=17h sólido; esperar n≥40/hora |
| H-BLACKLIST-02H/07H | ⏳ AUTO | OF BTC+SOL; revisar n≥20 por hora |
| STRUCT_NO_15M | ⚠️ **NO PROMOCIONAR** | ic_bayes agregado -0.1985 n=15 (ya negativo en shadow forward). Además 09-Jul: recontrastado con fills reales Polymarket (n=6372, 14× el backtest original) → calibración casi perfecta en la zona [0.47,0.50) que usa como gate, SIN el +5.6pp de mispricing que motivó su creación. Antes de cualquier propuesta de whitelist, leer memoria `idea_structno_no_replica_fills` |
| LEADLAG-BTC-XRP | ⚠️ TRACKING, expectativa BAJA | Hallazgo offline con fills reales (Jon-Becker, z=2.4-2.8 split-half) — pero 09-Jul: validado con API real de Polymarket (n=1342, 14d, timestamps reales) y salió NULO (z≈0). Probable causa: granularidad (fills tick-a-tick vs muestreo ~20s/1min). El tracker en shadow (`LEADLAG_BTC_XRP_15M`) usa la misma cadencia gruesa que la validación fallida → probablemente también nulo. Se deja corriendo (gratis, shadow puro) pero NO tratar como candidata cercana; revisar con n≥40 sin sesgo de expectativa |

**Hipótesis custom en `data/shadow/hipotesis_custom.json`** (editar sin tocar código):
GBM-17H-BTC | OF-MADRUGADA | GBM-SIGMA-ALTO/BAJO | OF-02H/07H-BTCSOL | GBM-60MIN-BUYYES/NO | GBM-18H | BUYYES-15MIN-POSTFILTRO | BTC15-TENDENCIA | DRIFT15-ZONA-MUERTA | DRIFT15-MOMENTUM | ETH15-REVERSION | LONGSHOT-BIAS

**Auto-apply**: H-GBM-18H → `meta.gbm_blacklist_hours_auto` | H-KELLY-HORA → `meta.hora_boost_factor`

---

## Aprendizaje causal
```
predictions (features JSON) → postmortem:
  IC_bucket < -0.12, n≥15 → filtro_causal (skip en predict)
  IC_bucket > +0.12, n≥15 → patron_ganador (kelly_boost)
→ strategy_params.json → siguiente ciclo
```
**Features GBM**: `{pct_spot_vs_ref, sigma_h, T_h, drift_15min, drift_60min, delta_ratio_macro, hora_utc, ibs_15}`
**Features OF**: `{delta_ratio, total_vol_5m, has_real_flow}`

---

## Prioridades pendientes
| P | Tarea | Condición de activación |
|---|---|---|
| **P-LIVE** | **Monitorear primer trade real** | **Ventana 15:00 Madrid (13:00 UTC)** |
| P6 | Cross-asset: GBM+OF BUY_NO mismo activo → ×1.5 | n≥20 ops OF BUY_NO post-filtro |
| P7 | Kelly por hora boost h=15/17/19 UTC | n≥40/hora forward (hypothesis_tracker vigila) |
| P8 | OF rangos per-par (BTC 0.42-0.44, SOL 0.36-0.40) | n≥200 con filtros actuales |
| P10 | ETH#15min reversion drift<-1 → boost ×1.1 | n≥20, IC≥0.08 sostenido |
| P11 | Revisar OF blacklist 02h/07h (BTC+SOL solo) | n≥20 por hora |
| P12 | Smart money wallets + trade size feature | Descargar Jon-Becker (`s3.jbecker.dev/data.tar.zst` 36GB) — ver P16, versión ligera ya con dato real vía API gratis, no necesita el dataset |
| P16 | **Ponderar `smart_money_consensus` por desviación del patrón propio de cada wallet** (no consenso poblacional plano, ya refutado n=2494). 11-Jul: reconstruido histórico real de 47 wallets vía `data-api.polymarket.com/activity` (gratis, misma API que `wallet_pnl_diario.py`), n=9819 posiciones. Apuesta ≥2× la mediana propia de esa wallet → 73.7% win vs 64.6% si ≤0.5×; activo fuera de sus 2 habituales → 76.1% vs 67.1%. **12-Jul: sesgo de redención VERIFICADO al 100% (54 wallets, n=15618)** con heurístico corregido (vendido sin redimir a precio≥0.70 → tratado como WIN, no LOSS): el corte de **TAMAÑO SOBREVIVE y se refuerza** (69.2%→73.6% vs 51.4%→52.8%, gap crece 17.8→20.8pp) — real, no artefacto. El corte de **ACTIVO HABITUAL SE EVAPORA** (gap 64.1/60.0=+4.1pp con heurístico viejo → 65.9/65.3=+0.6pp corregido): las wallets venden más pronto sus ganadoras en su activo habitual (más gestión activa) que en uno nuevo — el hallazgo de "novedad de activo" era en gran parte el sesgo de redención, no señal real. **12-Jul: IMPLEMENTADO** (`7652c1eda`) — `smart_money_tracker.py` computa mediana de apuesta por wallet "smart" (vía `/activity`, cache 24h) y pesa cada trade por `min(usd/mediana, 5.0)` en vez de 1 voto plano → `smart_money_consensus_ponderado` en `smart_money_consensus.json`, logueado junto al plano en `shadow_predict.py` (`pred_features`), sin tocar `prob_yes` ni ninguna decisión. Ver `analisis_p16_redencion_corregido.py` + `data/shadow/p16_redencion_corregido.json` para la verificación que motivó la implementación. Puramente shadow/observacional. | n≥40 forward comparando `smart_money_consensus_ponderado` vs el plano actual antes de plantear boost/veto |
| P17 | **Meta-score regularizado (Ridge) sobre GBM_LATE_15M BUY_YES** combinando `d_gbm`+`sigma_h`+`drift_ventana_pct`+`hora_utc`+`restante_min`+`T_h` en vez de solo `norm_cdf(d_gbm)`. 11-Jul: walk-forward 70/30 (n=1580 BUY_YES histórico), AUC=0.670 vs AUC≈0.53 si se agrupan BUY_YES+BUY_NO en un solo modelo (mezclar direcciones invierte el signo de `d_gbm` y destruye la señal — lección de método, no solo resultado). BUY_NO más débil y con posible interacción no lineal (Random Forest 0.619 > Ridge 0.586) — no incluir en la primera versión. Implementación: loguear el score del modelo como feature adicional (`meta_score_gbm_late`, puramente informativo) varios días, comparar su AUC/calibración forward contra `norm_cdf(d_gbm)` actual antes de proponer sustituirlo. | **Toca la probabilidad de la estrategia live principal — no cambiar `prob_yes` sin aprobación explícita de Javi + `/code-review`, ni siquiera en shadow-primero sin que el logueo lleve ≥2 semanas / n≥300 forward |
| P13 | Arb de contención ventanas anidadas → live | **Análisis 05-Jul: 157 opps/4d con profit>1% y depth≥$10, mediana +14%.** Sim ejecución activa (nested_arb_sim.csv); a live con n≥30 cerradas y garantia_ok~100% |
| ~~P14~~ | **RESUELTO 2026-07-03: quedarse taker.** maker_sim n=375: fill 53.6%, EV taker +0.147€/señal vs maker -0.21€/señal (selección adversa). maker_sim sigue acumulando por si cambia con más liquidez | — |
| P15 | **Doble-conteo de boosts horarios en el stake** (no en prob/edge: la ruta de IC está limpia). Boosts multiplicativos de "hora buena" se apilan: hardcoded 24H `{5,6,7,15,16,17,18,19}` (`shadow_predict.py:2695`) × meta `hora_boost_factor` (`:2664`) × posible bucket causal sobre `hora_utc` → cuenta el mismo fenómeno 2-3×. **Impacto live HOY = 0** (max_stake pinned 1,05€). Arreglo = colapsar en una sola fuente de verdad. Mapeado en shadow (read-only) para ver si los buckets sobre-boosteados rinden peor. | **Al despinnar max_stake_eur del suelo** (tras validar maker / más bankroll) |

---

## Constantes clave

### shadow_predict.py
```python
DRIFT_DAMPING = {5:0.30, 15:0.20, 60:0.05, 240:0.10}  # backfill 90d
REGIME_BUY_NO_THRESHOLD = 0.7    # %/h — solo ≥60min, solo BUY_NO
DRIFT_60_BUY_YES_15M_LO = 0.0   # BUY_YES #15min: drift_60min mínimo
DRIFT_60_BUY_YES_15M_HI = 0.25  # BUY_YES #15min: drift_60min máximo (05-Jul, antes 0.5)
BUY_YES_15M_TH_MAX = 0.2  # BUY_YES #15min SOLO tardío (06-Jul: temprana IC=-0.062 n=404 vs tardía +0.123; el loop re-evalúa y la señal entra sola en zona tardía)
# BTC#15min: skip si drift_15min*100 < 0.3
EDGE_MINIMO = 0.02 | SLIPPAGE_ESTIMADO = 0.02 (dinámico desde 03-Jul: mediana slip_real live si n≥30, clamp [0.005, 0.02])
GBM_LATE_DRIFT_VENT_MIN_PCT = 0.02  # photo finish (05-Jul): GBM_LATE skip si |drift_ventana|<0.02%
DELTA_MIN = 0.38 | DELTA_MAX = 0.46  # OF solo BUY_NO (delta<0)
KELLY_COMPUESTO_BOOST = 1.5 | KELLY_COMPUESTO_MAX = 2.00
ORDER_FLOW_BLACKLIST_HOURS = {2,7,9,22}  # UTC BTC+SOL. 07-Jul: quitadas h10/h11 (blacklist invertido — eran BUENAS en BUY_NO; el IC malo previo era del BUY_YES OF, muerto desde 26-Jun). scan_blacklist_hours.py
ORDER_FLOW_PAIR_BLACKLIST  = {'ETH','BNB','XRP','DOGE'}
# Longshot: BUY_NO py_mkt<0.20 → ×1.1
# poly_drift_5obs: confluencia→×1.1 | divergencia fuerte→×0.85
```

### shadow_postmortem.py
```python
IC_FILTRO_MIN=-0.12 | IC_PATRON_MIN=+0.12 | N_BUCKET_MIN=15
UMBRAL_DESACTIVAR=(-0.20, 8)  # IC<-0.20 en n≥8 ciclos → desactivar
# Kelly por dirección: apuesta_kelly_BUY_YES / apuesta_kelly_BUY_NO separados
```

### live_stake.py / data/live/config_live.json
```python
max_pct_bankroll=0.10 | min_stake_eur=1.05 (CLOB exige ≥$1 en marketable BUY) | max_stake_eur=1.05 (07-Jul: des-pineado 1.05→1.75 por la mañana, pero RE-PINEADO 1.75→1.05 el mismo día tarde — el des-pineo salió en contra en forward, corr(stake,acierto)=-0.32 en BUY_YES n=50; Gate #1 no reabrir hasta n≥15 trades des-pineados limpios, sigue sin cumplirse)
freno_ventana=0.20 | freno_diario=0.30 (05-Jul, antes 0.15) | bankroll_min=1.00 (05-Jul) | racha=4
# ⚠️ SELECCIÓN ADVERSA TAKER (03-Jul): fills live 19% hit vs 83% señales vetadas por profundidad
# (mismas tuplas/día; shadow pierde los MISMOS mercados a precio plan → no es slippage, es fill-ability).
# data/live/libro_snapshots.csv registra libro de cada señal en fase de ejecución (motivo:
# ejecutada/veto_profundidad/veto_sin_datos/abort_requote/fok_kill/no_viable_stake — este último
# captura señales bloqueadas por el suelo/freno, para que el dataset acumule con el live congelado).
# `python3 analisis_fills.py` = criterio de reapertura: hit shadow por motivo, decide con n≥30.
# 05-Jul: libro_snapshots acumula 24/7 (motivo fuera_ventana, mismos filtros IC/whitelist, desde
# live_trade._snapshots_fuera_ventana) — antes solo dentro de ventana y el dataset no crecía.
# maker_sim segmentado por tupla (n=1270): EV maker NEGATIVO en las 10 tuplas → maker descartado
# también condicional; la reapertura va por filtro fill-ability, no por maker.
# REAPERTURA 06-Jul (decisión usuario 05-Jul): at job toca LIVE_MODE_ON lunes 06:00 UTC.
# Objetivo: recuperar con los 8.50€; solo para al quedarse sin dinero (breaker a 1€ apaga y avisa).
# Congelado 03→05-Jul: el suelo era 8€→3€ (04-Jul) y el switch quedó OFF.
```

---

## Esquema de datos clave (nombres exactos de columnas)
```
results.csv:       pnl_neto (NO "pnl") | acierto | strategy | subtype | decision | precio_yes_mercado | prob_yes_modelo
strategy_params.json: ic_bayes (NO "ic_efectivo") | n | activa | apuesta_kelly | ic_BUY_NO | ic_BUY_YES | n_BUY_NO | n_BUY_YES
trades.csv:        pnl_neto_eur | stake_eur | entry_price | status (OPEN/CLOSED/STUB) | direction
                   ⚠️ edge_neto SIEMPRE en perspectiva YES: en filas BUY_NO el edge a favor es −edge_neto
                   (la ejecución usa edge_dir con signo resuelto; el CSV registra el crudo de predictions)
```
**Git conflicto en data/ CSV**: siempre `git checkout --theirs data/shadow/*.json data/prices/*.csv`

---

## Ficheros clave
```
data/shadow/predictions_YYYY-MM-DD.csv  — features JSON por predicción
data/shadow/results.csv                  — historial completo (17 cols + features)
data/shadow/strategy_params.json         — IC, Kelly, filtros_causales, activa/desactivada
data/shadow/estado_actual.md             — estado bot (actualizado c/60s) ← leer en /inicio
data/shadow/hipotesis_auto.md            — hipótesis + patrones causales activos (c/23min)
data/shadow/hipotesis_custom.json        — hipótesis custom editables sin tocar código
data/shadow/arb_scan_YYYY-MM-DD.csv     — oportunidades arb del día
data/live/.env                           — POLY_PRIVATE_KEY + API credentials (gitignored)
data/live/trades.csv                     — trades reales ejecutados
data/live/LIVE_MODE_ON                   — touchfile switch (no commiteado)
logs/live.log                            — fast loop log
LIVE_SETUP_2026-06-29.md                — setup live: MetaMask, USDC, CLOB (completado)
```

---

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
