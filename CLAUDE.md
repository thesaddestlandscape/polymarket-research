# CLAUDE.md — Polymarket Research Bot
**Actualizado: 2026-06-30** | Live activo desde hoy (cron ON 13:00 UTC)

## Reglas de comportamiento
- **Fail Loud**: "completado"/"verificado" es INCORRECTO si algo se asumió sin confirmar explícitamente. Surfacear incertidumbre siempre.
- **Checkpoint**: en tareas ≥3 pasos, resumir tras cada paso qué está verificado y qué queda antes de continuar.

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

**Flujo sesión**: `/inicio` → `/decision` (si alertas) → `/analizar X` (n≥30) → `/calibrar` (c/50 ops nuevas)

## Worktrees
```
/root/polymarket-research      # main — PRODUCCIÓN (loops corriendo)
/root/polymarket-research-dev  # dev  — experimentos
git merge dev --no-ff          # promover desde main
```

---

## Objetivo
Bot semi-autónomo para mercados cripto Polymarket.
- **Fase actual**: live activo — primer trade real hoy 30-Jun
- **Capital**: 25.44€ operativo live (30€ depósito, 10€ reserva)
- **Umbral live**: IC≥0.10, n≥40 resoluciones confirmadas
- **VPS**: Hetzner Helsinki (IP finlandesa — Polymarket accesible desde FI)
- **Estrategia live activa**: BUY_NO #15min (IC=+0.133, n=58) ✅

---

## Arquitectura — 3 loops en screen
```
screen fast    → run_fast.sh   (~20s): klines→predict→live_trade→resolve→postmortem→resumen→push
screen slow    → run_slow.sh  (~23min): markets→wallets→trades→report→arb→push
screen control → live_control.py (Telegram: /on /off /status /help)
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

---

## Sistema live trading
```bash
bash live_switch.sh on/off/status   # o Telegram: /on /off /status
```
**Ventanas (hora Madrid, L-V)**: 08:30-09:30 | 10:30-11:30 | 15:00-16:00 | 16:30-17:30 | 18:30-19:30 | 20:30-21:30
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
| H-OU-5MIN | ❌ DESACTIVADA | IC=-0.229 — sin Jon-Becker no avanzar |
| H-5MIN-REVERSIÓN | ✅ CONF | GBM#5min todos pares desactivados |
| H-WEEKLY-PRICE | ⏳ n=57 | SOL sostenido; BTC neg; esperar n≥15/par |
| H-GBM-18H | ⏳ AUTO | hypothesis_tracker auto-aplica cuando n≥15 IC<-0.08 |
| H-CROSS-ASSET | ⏳ n→20 | GBM+OF BUY_NO mismo activo → boost ×1.5 |
| H-KELLY-HORA | ⏳ AUTO | Solo H=17h sólido; esperar n≥40/hora |
| H-BLACKLIST-02H/07H | ⏳ AUTO | OF BTC+SOL; revisar n≥20 por hora |

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
| P12 | Smart money wallets + trade size feature | Descargar Jon-Becker (`s3.jbecker.dev/data.tar.zst` 36GB) |

---

## Constantes clave

### shadow_predict.py
```python
DRIFT_DAMPING = {5:0.30, 15:0.20, 60:0.05, 240:0.10}  # backfill 90d
REGIME_BUY_NO_THRESHOLD = 0.7    # %/h — solo ≥60min, solo BUY_NO
DRIFT_60_BUY_YES_15M_LO = 0.0   # BUY_YES #15min: drift_60min mínimo
DRIFT_60_BUY_YES_15M_HI = 0.5   # BUY_YES #15min: drift_60min máximo
# BTC#15min: skip si drift_15min*100 < 0.3
EDGE_MINIMO = 0.02 | SLIPPAGE_ESTIMADO = 0.02
DELTA_MIN = 0.38 | DELTA_MAX = 0.46  # OF solo BUY_NO (delta<0)
KELLY_COMPUESTO_BOOST = 1.5 | KELLY_COMPUESTO_MAX = 2.00
ORDER_FLOW_BLACKLIST_HOURS = {2,7,9,10,11,22}  # UTC — evaluado sobre BTC+SOL
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
max_pct_bankroll=0.10 | max_stake_eur=2.00
freno_ventana=0.20 | freno_diario=0.15 | bankroll_min=5.00
```

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
