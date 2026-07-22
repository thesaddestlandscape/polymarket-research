# CLAUDE.md — Polymarket Research Bot
**Actualizado: 2026-07-22** | Live REABIERTO 06-Jul 06:00 UTC (objetivo: recuperar 8.50€, suelo 1€) — circuit breaker disparado 17-Jul (bankroll<1€), segunda recarga completada y switch ON de nuevo desde 21-Jul ~13:57 UTC

## Reglas de comportamiento
- **Fail Loud**: "completado"/"verificado" es INCORRECTO si algo se asumió sin confirmar explícitamente. Surfacear incertidumbre siempre.
- **Checkpoint**: en tareas ≥3 pasos, resumir tras cada paso qué está verificado y qué queda antes de continuar.
- **Antes de escribir código nuevo** (decisión ladder): ¿ya existe en el codebase? → ¿lo hace la stdlib/requests/csv/json? → ¿una línea? → solo entonces: mínimo viable. Excepción: código de seguridad live (circuit breakers, filtros end_date, Kelly) — no minimizar.

## Protocolo de arranque de sesión (obligatorio, antes de responder nada)
Petición explícita de Javi, 2026-07-17. En cada conexión, ANTES de atender cualquier petición del usuario, y sin que se pida:
1. **Leer la misión y los objetivos** — vault de Obsidian `/root/second-brain/02_projects/polymarket-research.md` (sección "Misión y objetivo", la versión narrativa que Javi lee/edita) + memoria nativa `project_mision_sistema.md` y `project_roadmap_150k.md` (`/root/.claude/projects/-root-polymarket-research/memory/`, detalle operativo/gates cuantitativos). Este proyecto es **el proyecto de vida del usuario**: toda decisión de la sesión, grande o pequeña, tiene que ir alineada sin excepción a cumplir esos objetivos (€150-200k/año, las 8 cualidades del sistema). No es una tarea más entre otras — es el criterio de fondo de todo lo demás.
2. **Barrido de salud del sistema**: comprobar que no haya bugs, fallos, sangrados silenciosos o evidentes, ni cables desconectados (procesos/screens, cron, config↔código, datos, logs, dinero real, git) — mismo rigor que un barrido de coherencia completo (ver el del 17-Jul en el historial de commits como referencia de profundidad), no un vistazo superficial. No hace falta rehacerlo entero si ya se hizo hace poco y nada cambió, pero ante cualquier duda o señal de alerta, repetirlo.
3. **Revisar contexto completo antes de hablar**: `MEMORY.md` entero (memoria nativa), los cierres/checkpoints de sesión más recientes, el estado real de los datos (`estado_actual.md`, `hipotesis_auto.md`, `trades.csv`) y el vault de Obsidian — **ya clonado de forma permanente en `/root/second-brain`** (cron `run_sync_obsidian.sh` cada 15min lo mantiene sincronizado con `git pull --rebase --autostash` + push; no reclonar nunca, solo `git -C /root/second-brain pull --rebase --autostash` si hace falta refrescar) — para saber exactamente de qué se habló antes de responder a nada. Empezar por `_index/00_INDEX.md`.
4. **Retomar y recitar los pendientes sin cerrar** de sesiones anteriores, proactivamente, sin que el usuario los pida (checklist vigente en memoria, p.ej. `project_revision_pendiente_08jul.md`, o el checkpoint más reciente que lo sustituya).
5. **Revisar `logs/vigia_sigma_patrones.log`** (petición explícita Javi, 2026-07-18) y exponer los resultados — ver si algún patrón `sigma_*` nuevo (n≥40, `data/live/vigia_sigma_patrones_latch.json`) merece acción. Ojo: a 18-Jul este vigía tiene un bug de dedup conocido (la firma incluye el `umbral` exacto, que dosdea con cada recálculo del postmortem → reenvía el mismo patrón por Telegram muchas veces) — filtrar el ruido por clave/feature antes de reportar, no tomar el conteo de avisos al pie de la letra.
6. **Reportar explícitamente en el mensaje de arranque** (petición explícita Javi, 2026-07-20): (a) qué nuevas hipótesis se han generado desde la última sesión — sección "Estrategias nuevas sugeridas" de `hipotesis_auto.md` + cualquier hipótesis custom nueva en `hipotesis_custom.json`/`llm_hypothesis.py`; (b) los mensajes de los vigías (`vigia_sigma_patrones.log` del punto 5, y cualquier otro vigía con avisos nuevos desde la sesión anterior) — no basta con revisarlo internamente, hay que decírselo a Javi sin que lo pida.
7. **Análisis diario de ballenas + postmortem** (petición explícita Javi, 2026-07-20, textual: "todos los días, con los nuevos datos de las ballenas que operan en crypto, dedícate a analizar todos los datos, que cruces trades, horarios, franjas, pnls de las ballenas, edges, todo — encuentra debilidades que podamos explotar. Estudia todo de arriba abajo, contrástalo con nuestra información, estrategias, hipótesis. Necesitamos encontrar ventajas y minarlas nosotros primero"): cada sesión (o cada día si hay varias), cruzar los datos nuevos de ballenas (`ballenas_timing_history.csv`, `wallet_edge_tracker`/`wallet_edge_score_por_marco.json`, `smart_money_consensus.json`, `wallet_contraparte_tracker`) contra trades/horarios/franjas/PnL/edges reales — buscar debilidades explotables, no solo confirmar lo ya sabido. Además, **revisar el postmortem** (`strategy_params.json::filtros_causales`/`patrones_ganadores`, `hipotesis_auto.md`) y reportar qué ha aprendido el sistema de lo que hacemos bien y mal. Reportar los hallazgos en el mensaje de arranque, igual que el punto 6 — no es opcional ni bajo demanda.
8. **Ballenas = la lente por defecto, no un módulo aparte** (corrección seria de Javi, 2026-07-21, dos avisos en la misma sesión: "hemos montado una infraestructura para ir donde van los ganadores... tienes que mirarlo siempre en cada estrategia que se toque" y "es la fuente de la sabiduría, tienes que revisar todos los datos de ballenas para contrastar con nuestras estrategias en cada inicio de sesión"): no basta con el análisis diario puntual del punto 7 — **cualquier análisis de estrategia durante la sesión** (candidata nueva, selección adversa, fill-ability, pausa, promoción) tiene que cruzarse contra TODA la infraestructura de ballenas antes de concluir nada, no solo una pieza: `ballenas_timing_state.json`/`ballenas_dentro_banda` (banda de precio), `ballenas_executor_5min.py`/`ballenas_executor_btc15m.py` (ejecutores DRY_RUN de timing real, no precio), `wallet_edge_tracker.py`, `smart_money_consensus.json`, `wallet_contraparte_tracker.py` — mapa completo en memoria `project_mapa_cobertura_fuentes_ballenas_20jul`. Fallo real que motivó esto: analizar selección adversa BUY_NO#15min a fondo sin cruzar `ballenas_dentro_banda` (que resultó ser señal mucho más fuerte), y concluir "5min sigue roto" sin revisar que `ballenas_executor_5min.py` llevaba 3 días acumulando señales DRY_RUN sin que nadie midiera su win-rate.

9. **Franja milimétrica de ballenas por moneda/marco, cada sesión — PRIORITARIO, recordar a diario sin que se pida** (petición explícita Javi, 2026-07-21, reforzada el mismo día: "esto es prioritario, tienes que recordarmelo diariamente para evaluarlo"): correr `python3 analisis_franja_milimetrica_ballenas.py` y reportar el resultado igual que los puntos 6/7 — no basta con la banda agregada `[0.70,0.90)` que usa `ballenas_dentro_banda`/`veto_ballenas` hoy, hay textura real dentro de ella (ver hallazgo 21-Jul: dentro de esa banda hay tramos buenos y malos mezclados, y fuera hay tramos tan buenos como los mejores de dentro). El script cruza a resolución fina (bucket 0.05) tres fuentes por (activo,marco): ballenas (`ballenas_timing_history.csv`, histórico completo de mercado, no solo donde disparamos señal), shadow (`results.csv`) y dinero real (`trades.csv`). Reportar: (a) qué bucket fino tiene mejor pnl/trade por activo/familia y su n (con el caveat de que n<40 por bucket es exploratorio, NO gate riguroso — no proponer cambios de corte solo con esto, es el mismo error que sizing por IC con n bajo ya diagnosticado 21-Jul), (b) huecos de cobertura nuevos (`ballenas_n>=50` y `hit>=70%` pero `shadow_n<15` — zonas de precio donde las ballenas saben algo y nosotros casi no operamos ahí). Objetivo: dejar que n crezca día a día y cortar con precisión quirúrgica solo cuando algún bucket cruce n≥40 con gate riguroso propio (Wilson+shuffle+bootstrap, mismo criterio que `analisis_filtro_banda_ballenas_20jul.py`), no antes. Marco conceptual a aplicar SIEMPRE al leer estos resultados (memoria `project_dos_patrones_edge_bandera_21jul`): arquetipo A (edge de modelo propio, generaliza cross-coin, ej. `GBM_LATE_15M`) tiende a fill-ability MALA (6-36%, selección adversa — el edge y el libro vacío coinciden en el tiempo); arquetipo B (edge coin-específico correlado con ballenas, ej. `FAVORITO_CONFIRMADO`) tiende a fill-ability BUENA (53-61%) — clasificar antes de ilusionarse con un pnl/trade alto en shadow.
10. **Punto de confirmación 95% por (moneda,marco) — mismo nivel de prioridad que el punto 9, revisar junto a él** (petición explícita Javi, 2026-07-21): revisar `data/shadow/punto_confirmacion_YYYY-MM-DD.csv` (screen `puntoconf`, `punto_confirmacion_logger.py`) — cuánto ha crecido n por cada una de las 7 combinaciones (`ETH/SOL#5min`, `BTC/ETH/SOL/XRP#15min`, `ETH#60min`) y si alguna ya tiene fill-ability concluyente (objetivo n≥30-40 por combo). Hallazgo base: hay un punto (precio,tiempo-restante-al-cierre) por cada combinación donde el límite inferior de un IC de Wilson al 95% ya supera 95% de acierto con edge real (precio<0.90) — pero varía muchísimo por moneda (BTC solo se confirma al último minuto, XRP a los 2 minutos de abrir), y el edge en shadow (`ballenas_timing_history.csv`) no implica fill-ability (mismo principio del punto 9). SOL#15min es la pista más prometedora hoy (69.8% fillable con dato parcial). Detalle completo en memoria `idea_punto_confirmacion_95pct_por_moneda_21jul`.
11. **Update de candidatas live + hipótesis + cementerio explotable, cada inicio de sesión** (petición explícita Javi, 2026-07-22): reportar en el mensaje de arranque, igual que los puntos 6/7 — (a) estado de las candidatas live (`candidatos_evaluacion_live`, fill-ability y gates según vayan madurando); (b) cómo van las hipótesis (`hipotesis_auto.md`, custom, tracker); (c) si algo del **cementerio de hipótesis refutadas** puede explotarse ahora con hallazgos nuevos (cruzar refutaciones viejas contra ballenas/franja milimétrica/punto de confirmación — a veces una hipótesis muere por fill-ability y un ángulo nuevo la revive, ver patrón `idea_ballenas_precio_domina_timing_matiz_19jul`). Incluye seguir observando/re-corriendo `analisis_wallet_quirurgico_precio_timing_22jul.py` (memoria `idea_wallet_quirurgico_precio_timing_22jul`) según crezca el roster de `vigia_wallet_edge_forward.py` — no se cerró con hallazgo, se dejó en watch.

Permanente, no expira, se aplica en cada conexión — no solo la primera vez. Obsidian (`/root/second-brain`) es parte fundamental del proyecto, no una referencia ocasional: se lee siempre, y se escribe ahí (decisiones/estado narrativo en `02_projects/`+`03_decisions/`, nunca a mano en `09_estrategias/`/`10_hipotesis/` que son generadas por `sync_obsidian.py`) igual que se escribe en la memoria nativa.

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
- **Umbral live**: IC≥0.08, n≥40 resoluciones confirmadas (valor real en `data/live/config_live.json::riesgo.min_ic_para_live`) **+ desde 17-Jul, además**: `python3 analisis_log_growth.py <strategy> <subtype> <decision>` con g>0 a f=10% — gate de crecimiento logarítmico (Kelly), complementario al IC. Un IC/EV positivo puede convivir con crecimiento compuesto negativo ("payout inverso": hit-rate alto, pérdidas grandes y poco frecuentes se comen el compounding) — caso confirmado: `FAVORITO_CONFIRMADO#{BTC,SOL,ETH}#15min#BUY_NO` (06-Jul) y `FAVORITO_CONFIRMADO#ETH#60min#BUY_NO` (21-Jul, pausada). Ninguna candidata nueva se promociona sin pasar ambos gates. **21-Jul**: `vigia_log_growth.py` (cron `30 * * * *`) vigila el gate sobre las tuplas YA en `pares_permitidos_live` — antes solo se comprobaba a mano al promocionar, sin nada que detectara que una tupla live cayera en payout inverso *después*; avisa por Telegram (latch, una vez por tupla) si alguna cae en g<0, decisión de pausar siempre de Javi.
- **VPS**: Hetzner Helsinki (IP finlandesa — Polymarket accesible desde FI)
- **Estrategias live activas** (`pares_permitidos_live` real a 21-Jul — ojo, vive en el nivel TOP del JSON, no dentro de `riesgo`): **8 tuplas, 7 BUY_YES + 1 BUY_NO**:
  | Tupla | Dirección | Desde | Nota en config_live.json |
  |---|---|---|---|
  | FAVORITO_CONFIRMADO#SOL#15min | BUY_YES | 14-Jul | `_pares_sol_promocion_nota_2026-07-14` |
  | FAVORITO_CONFIRMADO#SOL#60min | BUY_YES | 14-Jul | `_pares_sol60min_promocion_nota_2026-07-14` |
  | FAVORITO_CONFIRMADO#BTC#60min | BUY_NO | 14-Jul | `_pares_btc60min_buyno_promocion_nota_2026-07-14` |
  | UPDOWN_GBM_15M_TARDIO#BTC#15min | BUY_YES | 15-Jul | `_pares_updowngbm_tardio_btc_promocion_nota_2026-07-15` |
  | FAVORITO_CONFIRMADO#ETH#15min | BUY_YES | 15-Jul | `_pares_favoritoeth15min_promocion_nota_2026-07-15` |
  | BALLENAS_TARDIAS#BTC#15min | BUY_YES | 17-Jul | `_pares_ballenas_tardias_btc15m_promocion_nota_2026-07-17` |
  | GBM_LATE_15M#ETH#15min | BUY_YES | 17-Jul (pausada 14→reactivada 17) | `_pares_gbm_eth15min_reactivacion_nota_2026-07-17` |
  | FAVORITO_CONFIRMADO#BTC#60min | BUY_YES | **20-Jul** | `_pares_btc60min_buyyes_promocion_nota_2026-07-20` |

  **Pausadas/retiradas (no descartadas, siguen en `candidatos_evaluacion_live` acumulando fill-ability)**: `GBM_LATE_15M#SOL#15min#BUY_YES` (pausada 16-Jul, racha real negativa) | `GBM_LATE_15M_ESPACIO_ATR#SOL#15min#BUY_YES` y `#BTC#15min#BUY_YES` (pausadas **20-Jul**, selección adversa confirmada con shuffle p=0.000, gap -46pp/-41pp; cruce con ballenas descartó que el timing de ESPACIO_ATR explique/arregle el hueco — su entrada real no solapa con la ventana de ballenas en BTC#15m) — ver `_pares_espacioatr_sol_btc_pausa_nota_2026-07-20` | `FAVORITO_CONFIRMADO#ETH#60min#BUY_NO` (pausada **21-Jul**, IC seguía pasando pero gate de crecimiento logarítmico da g=-0.00237 con n=149 — payout inverso, mismo patrón que los `#15min#BUY_NO`) — ver `_pares_ethbuyno60min_pausa_nota_2026-07-21`.

  **Fuera de live, solo shadow**: XRP retirado 10-Jul (racha de pérdidas). Todos los BUY_NO #15min retirados 06-Jul por selección adversa direccional, vuelven vía filtro fill-ability con n≥30. `ORDER_FLOW_5M` y `GBM_LATE_60M` (refutada, ic_bayes negativo en los 3 activos) fuera de whitelist, acumulando shadow-only.

  Histórico completo de cada promoción/pausa (n, IC, Wilson, p_shuffle, fill-ability) vive en las notas `_pares_*`/`_candidatos_*` de `config_live.json` (citadas arriba) y en Obsidian `03_decisions/` — no duplicar aquí, este resumen es solo el estado actual.
- **Protecciones live añadidas 2026-07-03**: re-quote contra libro al ejecutar (aborta si edge<0.02 con el ask actual) | techo 2 posiciones abiertas misma dirección (correlación multi-par) | freno diario prospectivo (pérdida+stake+**stakes abiertos**≤15%, fix tras -6.54€ el 03-Jul) | veto patrón causal si IC propio del subtype <0 | **latch freno ventana** (disparo → `freno_ventana_latch.json`, no reabre hasta la siguiente ventana; antes se rearmaba solo al recuperar PnL) | **veto CLV** (tupla con clv_medio<0 y n≥20 en ventana 7d → no ejecuta; guardia sobre el IC, no sustituto) | slippage real → `notas` (`slip_real=`) para calibrar SLIPPAGE_ESTIMADO con n≥30 | **veto profundidad libro** (ratio<5x stake o consulta fallida → aborta; XRP/SOL entraron contra libros vacíos con slip +0.04/+0.085) | **whitelist por tupla** `pares_permitidos_live` STRATEGY#SUBTYPE#DIRECTION (el producto cartesiano coló UPDOWN_GBM#SOL/BTC#15min) | suelo prospectivo bankroll_minimo (8→3€ el 04-Jul, 1€ desde 06-Jul) | override freno diario con fecha (`freno_diario_pct_override`, solo aplica el día indicado) | **suelo stake 1.05€** (CLOB rechaza marketable BUY <$1 "min size: 1"; 2 señales perdidas 03-Jul con Kelly 0.94/0.98€ tras caer el bankroll) + guardia fail-closed en live_trade si llega <$1

---

## Arquitectura — 3 loops en screen
```
screen fast    → run_fast.sh   (~20s): klines→predict→live_trade→resolve→postmortem→resumen→push
screen slow    → run_slow.sh  (~23min): markets→wallets→trades→report→arb→push
screen control → live_control.py (Telegram: /on /off /status /help)
screen pfinish → photo_finish_logger.py (captura photo finish c/frontera 5min)
screen chainlink → fetch_chainlink_prices.py (precios Chainlink en vivo, fuente de resolución oficial)
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
| `fetch_chainlink_prices.py` | Screen `chainlink` (20-Jul): captura continua vía websocket público de Polymarket (RTDS, sin auth) de precios Chainlink BTC/ETH/SOL/XRP — fuente de resolución OFICIAL de los mercados Up/Down (`resolutionSource` en gamma-api), distinta de Binance/Kraken → `data/prices/chainlink_YYYY-MM-DD.csv`. Origen: diagnóstico de 13 roturas de garantía en `nested_arb_sim.csv` (ver nota en `analisis_nested_arb_gate.py`/memoria) — `nested_arb_scanner.py` estimaba o_inner/o_outer con klines Binance/Kraken, y el ruido normal Binance-vs-Chainlink bastaba para invertir el orden percibido en gaps estrechos, rompiendo una garantía que en teoría es matemáticamente segura. Solo lectura, no toca dinero ni ninguna decisión todavía. |
| `analisis_franja_milimetrica_ballenas.py` | (21-Jul, ver CLAUDE.md protocolo punto 9) Cruce a resolución fina (bucket 0.05, no la banda única `[0.70,0.90)`) de ballenas (`ballenas_timing_history.csv`, histórico completo de mercado) + shadow (`results.csv`) + dinero real (`trades.csv`) por activo/marco → `data/shadow/franja_milimetrica_ballenas.json`. Correr cada inicio de sesión, dejar madurar n antes de cortar bandas más finas. Solo lectura. |

---

## Sistema live trading
```bash
bash live_switch.sh on/off/status   # o Telegram: /on /off /status
```
**Ventanas (hora Madrid, L-V)**: 08:30-09:30 | 10:30-11:30 | 15:00-23:00 (fusionada 2026-07-02, extendida 21-Jul de 21:30→23:00 para cubrir hora 20 UTC, GATE OK n=95 pnl+0.375€ + fill-ability 47.1%) | 01:00-02:00 (prueba, ≈23h UTC) | 06:00-07:00 (asia, confirmada IC+0.131 n=177)
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

**Auto-apply**: DESACTIVADO desde 15-Jul (petición Javi, tras `/code-review` de UPDOWN_GBM_15M_TARDIO que encontró un bucket contaminado auto-aplicado sin revisión). H-GBM-18H y H-KELLY-HORA ya NO escriben `meta.gbm_blacklist_hours_auto`/`meta.hora_boost_factor` solos — `hypothesis_tracker.py::_auto_apply` solo avisa por Telegram cada ciclo (~23min) hasta que alguien lo aplica a mano; el aviso de H-KELLY-HORA exige IC≥0.15 por hora (más estricto que el ≥0.10 de "confirmada" en `hipotesis_auto.md`).

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
| **P19** ⭐prioridad Javi 21-Jul | **Gap sigma implícita (Polymarket) vs realizada — filtro nuevo para familia GBM**. Invirtiendo la fórmula GBM que ya usamos (`_gbm_p_up`) con el precio real de Polymarket en vez de `sigma_h`, se obtiene la volatilidad que el mercado está precian do implícitamente — análogo directo a la prima de riesgo de varianza (VRP) de opciones (inspirado en paper SSRN 6712647, Ito 2025, adaptado por Claude 21-Jul). `gap = sigma_implicita - sigma_h`: tercil bajo (mercado infravalora vol vs lo realizado) n=443 hit=53.3% NO CONCLUYENTE (Wilson cruza 50%, split-half plano en ambas mitades) vs resto n=886 hit=69.8% GATE OK limpio (CI90%=[+0.368,+0.502]). Afecta a `UPDOWN_GBM`/`GBM_LATE_15M`/hermanas — 2 tuplas ya en live (`UPDOWN_GBM_15M_TARDIO#BTC#15min`, `GBM_LATE_15M#ETH#15min`). Detalle completo en memoria `idea_gap_sigma_implicita_realizada_gbm_21jul`. NO implementado. | Repetir el corte con gate riguroso por familia/activo por separado (hoy agregado) + fill-ability del subconjunto "gap bajo" excluido + instrumentar como feature observacional (`pred_features`, patrón `ballenas_dentro_banda`) antes de tocar ningún filtro/decisión real. `/code-review` + aprobación explícita de Javi antes de cambiar `prob_yes` o cualquier gate |
| **P20** ⭐prioridad Javi 21-Jul, extiende P19 | **Meta-modelo de confianza sobre estructura temporal de volatilidad** — inspirado en paper SSRN 4666899 (Sheikh Sadik, rotación SVOL/VIXY con modelo primario + meta-modelo que evalúa si el primario está funcionando y reduce exposición hacia neutral cuando la confianza baja). Ya tenemos 3 piezas de este patrón DISPERSAS: `vigia_degradacion_live.py` (avisa si degradación shadow→real reciente), `vigia_log_growth.py` (avisa si una tupla live cae en payout inverso), `cooldown_factor_streak` (`live_stake.py`, único que AJUSTA algo automático — reduce stake tras 2 derrotas seguidas, pero es un contador de racha, no un meta-modelo real). Ninguno usa estructura temporal de volatilidad. La extensión natural: comparar el gap de P19 (sigma implícita vs realizada) a través de los 5 marcos (5/15/60/240min/weekly) del mismo activo — el análogo a la curva VIX term structure del paper — y usarlo para modular stake automáticamente, no solo avisar por Telegram. | No implementar sin generalizar primero `cooldown_factor_streak` o diseñar el mecanismo de ajuste automático con Javi — toca sizing de dinero real, `/code-review` + aprobación explícita antes de cualquier cambio en `live_stake.py`. Empezar por P19 (la pieza base) antes de construir la estructura temporal completa |
| **P18** ⭐prioridad Javi 16-Jul | **Smart Exit — STOP-LOSS** (lado perdedor, espejo del take-profit original). 16-Jul: simulación sobre 27 pérdidas reales con historial en `smart_exit_prices.csv` (precio MID, sin spread/fee de venta — optimista): umbral -0.30€ dispara en 27/27, pnl real -39.52€ → con stop-loss -26.92€ (mejora +12.61€, -32% de la pérdida). Mayoría de pérdidas pasan varios minutos en meseta a precio intermedio antes de caer a 0 — sí hay ventana real para vender. Detalle completo en memoria `idea_smart_exit.md`. Gate de datos (≥50 trades live) ya cumplido (n=199). | Repetir la simulación con **bid real del CLOB** (no mid) + **fee de venta** descontado — si la mejora sobrevive, implementar como `_check_early_exit` con 2 umbrales (take-profit + stop-loss). Toca ejecución de dinero real: `/code-review` + aprobación explícita de Javi antes de tocar código live |
| P6 | Cross-asset: GBM+OF BUY_NO mismo activo → ×1.5 | n≥20 ops OF BUY_NO post-filtro |
| P7 | Kelly por hora boost h=15/17/19 UTC | n≥40/hora forward (hypothesis_tracker vigila) |
| P8 | OF rangos per-par (BTC 0.42-0.44, SOL 0.36-0.40) | n≥200 con filtros actuales |
| P10 | ETH#15min reversion drift<-1 → boost ×1.1 | n≥20, IC≥0.08 sostenido |
| P11 | Revisar OF blacklist 02h/07h (BTC+SOL solo) | n≥20 por hora |
| P12 | Smart money wallets + trade size feature | Descargar Jon-Becker (`s3.jbecker.dev/data.tar.zst` 36GB) — ver P16, versión ligera ya con dato real vía API gratis, no necesita el dataset |
| P16 | **Ponderar `smart_money_consensus` por desviación del patrón propio de cada wallet** (no consenso poblacional plano, ya refutado n=2494). 11-Jul: reconstruido histórico real de 47 wallets vía `data-api.polymarket.com/activity` (gratis, misma API que `wallet_pnl_diario.py`), n=9819 posiciones. Apuesta ≥2× la mediana propia de esa wallet → 73.7% win vs 64.6% si ≤0.5×; activo fuera de sus 2 habituales → 76.1% vs 67.1%. **12-Jul: sesgo de redención VERIFICADO al 100% (54 wallets, n=15618)** con heurístico corregido (vendido sin redimir a precio≥0.70 → tratado como WIN, no LOSS): el corte de **TAMAÑO SOBREVIVE y se refuerza** (69.2%→73.6% vs 51.4%→52.8%, gap crece 17.8→20.8pp) — real, no artefacto. El corte de **ACTIVO HABITUAL SE EVAPORA** (gap 64.1/60.0=+4.1pp con heurístico viejo → 65.9/65.3=+0.6pp corregido): las wallets venden más pronto sus ganadoras en su activo habitual (más gestión activa) que en uno nuevo — el hallazgo de "novedad de activo" era en gran parte el sesgo de redención, no señal real. **12-Jul: IMPLEMENTADO** (`7652c1eda`) — `smart_money_tracker.py` computa mediana de apuesta por wallet "smart" (vía `/activity`, cache 24h) y pesa cada trade por `min(usd/mediana, 5.0)` en vez de 1 voto plano → `smart_money_consensus_ponderado` en `smart_money_consensus.json`, logueado junto al plano en `shadow_predict.py` (`pred_features`), sin tocar `prob_yes` ni ninguna decisión. Ver `analisis_p16_redencion_corregido.py` + `data/shadow/p16_redencion_corregido.json` para la verificación que motivó la implementación. Puramente shadow/observacional. | n≥40 forward comparando `smart_money_consensus_ponderado` vs el plano actual antes de plantear boost/veto |
| P17 | **Meta-score regularizado (Ridge) sobre GBM_LATE_15M BUY_YES** combinando `d_gbm`+`sigma_h`+`drift_ventana_pct`+`hora_utc`+`restante_min`+`T_h` en vez de solo `norm_cdf(d_gbm)`. 11-Jul: walk-forward 70/30 (n=1580), AUC=0.670. **18-Jul: IMPLEMENTADO** (`entrenar_meta_score_gbm_late_p17.py` + `shadow_predict.py::_meta_score_gbm_late`, commit `33f8164121`) — reentrenado con n=2605, AUC walk-forward=0.683 (replica de sobra el 0.670 original), modelo guardado en `data/shadow/meta_score_gbm_late_model.json`, logueado como feature `meta_score_gbm_late` en cada predicción de `_s_gbm_late` (afecta a los 5 hermanos: 15M/60M/TARDIO/ESPACIO_ATR/PYCONFIRMADO, no solo GBM_LATE_15M base — dato extra gratis). 100% informativo, `git diff` verificado sin ningún otro cambio de comportamiento. Empezó a loguear el 18-Jul ~09:13 UTC — el reloj de ≥2 semanas/n≥300 forward arranca esa fecha. | **Toca la probabilidad de la estrategia live principal — no cambiar `prob_yes` sin aprobación explícita de Javi + `/code-review`, ni siquiera en shadow-primero sin que el logueo lleve ≥2 semanas / n≥300 forward (empezó 18-Jul) |
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
ORDER_FLOW_PAIR_BLACKLIST  = {'BTC'}  # 11-Jul: ETH/BNB/XRP/DOGE reabiertos (aprobado Javi, shadow puro, 93% del histórico que los bloqueó era una ráfaga 24-25jun); BTC bloqueado ese mismo día por no batir control zero-intelligence (p_shuffle=0.51)
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
