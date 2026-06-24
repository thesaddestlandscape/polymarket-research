# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.

---

## Objetivo del proyecto

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.

- **Fase actual (shadow mode)**: el bot genera predicciones y las anota como si apostara, pero sin dinero real. Acumula resoluciones para medir el Information Coefficient (IC) real de cada estrategia.
- **Fase 2 (live)**: cuando una estrategia alcance IC ≥ 0.10 con n ≥ 50 resoluciones, se activa con dinero real.
- **Capital simulado**: 30 € depósito total → 20 € operativo + 10 € reserva intocable.

---

## Arquitectura — dos loops en paralelo (screen)

```
screen -S fast  →  bash run_fast.sh    (cada ~60s)
screen -S slow  →  bash run_slow.sh    (cada ~23min, capture_markets tarda ~10min)
```

### Loop FAST — `run_fast.sh`

Secuencia por ciclo:

1. **`fetch_binance_klines.py`** — descarga velas 1min de BTC/ETH/SOL/XRP/DOGE/BNB vía Kraken (el script se llama "binance" por herencia histórica, usa Kraken)
2. **`shadow_predict.py`** — genera predicciones en `data/shadow/predictions_YYYY-MM-DD.csv`
3. **`shadow_resolve.py`** — detecta mercados vencidos, resuelve predicciones → `data/shadow/results.csv` + `strategy_accuracy.csv`
4. **`shadow_postmortem.py`** — clasifica pérdidas, calcula IC Bayesiano y Kelly por subtipo, escribe `strategy_params.json` y `performance.csv`
5. **`shadow_resumen.py`** — genera `data/shadow/estado_actual.md` (visible en GitHub, actualizado cada 60s)
6. `git add data/shadow/ && git commit && git push` — solo si hay cambios

### Loop SLOW — `run_slow.sh`

Secuencia por ciclo (~23 min totales):

1. **`capture_markets.py`** — captura ~1800 mercados cripto de Polymarket vía Gamma API. Internamente hace 10 snapshots × 60s ≈ 10 min. También escribe `data/prices/YYYY-MM-DD.csv` vía CoinGecko cada ~60s con precios spot de BTC/ETH/SOL/XRP/DOGE/BNB.
2. **`capture_wallets.py`** — top 75 wallets del leaderboard por PNL+VOL
3. **`capture_trades.py`** — últimas 4h de trades de las top 50 wallets
4. **`generate_report.py`** — genera `data/shadow/informe_bot.xlsx` (Excel con 7 hojas, visible en GitHub)
5. `git add data/prices/ data/wallets/leaderboard_*.csv && git commit && git push`

**IMPORTANTE**: `capture_markets.py` es quien escribe `data/prices/YYYY-MM-DD.csv`. No hay un `capture_prices.py` separado en los loops activos. El archivo `capture_prices.py` existe en el repo pero no está en ningún loop.

---

## Scripts — descripción de cada archivo

### Loop activo (fast)
| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min via Kraken → `data/binance/` (excluido de git) |
| `shadow_predict.py` | Genera predicciones para los 5 modelos activos |
| `shadow_resolve.py` | Resuelve predicciones vencidas, calcula PNL |
| `shadow_postmortem.py` | IC Bayesiano + Kelly → `strategy_params.json` (auto-tuning) |
| `shadow_resumen.py` | Genera `estado_actual.md` con bankroll y tabla de estrategias |

### Loop activo (slow)
| Script | Función |
|---|---|
| `capture_markets.py` | Mercados Polymarket + precios spot intraday |
| `capture_wallets.py` | Leaderboard top 75 wallets |
| `capture_trades.py` | Trades recientes de wallets top |
| `generate_report.py` | Excel unificado (`informe_bot.xlsx`) |

### Scripts auxiliares (no en loops activos)
| Script | Función |
|---|---|
| `shadow_digest.py` | Resumen diario Telegram (vía GitHub Actions, 20:00 UTC) |
| `backtest.py` | Backtesting offline de estrategias |
| `conviction_score.py` | Score de convicción multi-estrategia |
| `insider_detect.py` | Detección de wallets con información privilegiada |
| `price_alerts.py` | Alertas de precio |
| `capture_prices.py` | Captura de precios spot (no activo en loops) |

---

## Estrategias activas (`shadow_predict.py` v8)

Registradas en orden en `ESTRATEGIAS = [...]` al final del script:

### 1. WEEKLY_PRICE
- **Qué hace**: mercados "Will BTC be between $X-$Y on [date]?". Compara spot actual con el bracket.
- **Señal**: si spot IN bracket → BUY_YES; si OUT → BUY_NO. Probabilidad ajustada por `time_scale = sqrt(6/max(horas,6))`.
- **Estado**: señales activas. Primera resolución fue el 24 Jun a las 16:00 UTC.
- **n resoluciones**: 0 (todavía pendiente de resolver en el histórico).

### 2. PRICE_MOMENTUM
- **Qué hace**: tendencia exponencial del precio YES en el historial de mercados (últimas 6h de snapshots).
- **Filtros**: ≥5 snapshots, liq ≥ 500, spread ≤ 0.08, drift ≥ 1.5%, consistencia ≥ 60%.
- **Estado**: da 0 señales por la mañana (mercados quietos hasta ~12:00 UTC). Activo en horario europeo/americano.

### 3. SMART_FLOW_1H
- **Qué hace**: detecta ≥ 3 wallets humanas (no-BOT) comprando el mismo lado en la última 1h, imbalance ≥ 70%.
- **Filtro crítico** (añadido 2026-06-24): excluye mercados Up/Down — `_parse_updown_tipo(question)[0] is not None → return None`. Antes sin este filtro la estrategia operaba slots 5/15min con IC = -0.375.
- **Estado**: IC muy negativo (-0.33, n=12) debido a pérdidas pre-fix en slots. Acumulando datos limpios.

### 4. UPDOWN_GBM ← estrategia principal
- **Qué hace**: Black-Scholes digital `P(S_T > S_ref | spot, σ, T)` para mercados "X Up or Down".
- **Tipos cubiertos**:
  - `daily`: ref = medianoche UTC del día del vencimiento, vol_win = min(240, T*20) min
  - `hourly`: ref = 1h antes del cierre, vol_win = 120 min
  - `slot 5min`: ref = inicio del slot, vol_win = min(60, 20) = 20 min
  - `slot 15min`: ref = inicio del slot, vol_win = min(60, 60) = 60 min
- **Vol**: estimada de `data/prices/YYYY-MM-DD.csv` (resolución ~60s)
- **Filtros**: liq ≥ 2000, spread ≤ 0.05, T ≥ 2 min
- **Descubrimiento directo de slots**: `fetch_slots_directos()` consulta la API cada ciclo para slots 5min (±2 ventanas) y 15min (±1 ventana), sin depender del CSV del slow loop. Cobertura ~100%.
- **Estado**: n=54, IC=+0.019, PNL=-0.14€ global. Los 15min son los ganadores.

### 5. PRICE_TARGET_GBM
- **Qué hace**: GBM para mercados de precio objetivo: "Will BTC reach $70k?", "Will ETH be above $X?".
  - `atexpiry above K`: P(S_T > K) = N(log(S/K) / σ√T)
  - `atexpiry below K`: P(S_T < K)
  - `reach K`: P(toca K) = 2·N(-|log(S/K)| / σ√T) [reflexión del BM]
- **Filtros**: liq ≥ 2000, spread ≤ 0.08, T entre 1h y 30 días
- **Estado**: señales activas (34 señales hoy), sin resoluciones aún (mercados multi-día).

### BINANCE_UPDOWN — RETIRADA
- Usaba momentum de klines para predecir dirección. IC = -0.50. Comentada en `ESTRATEGIAS`.

---

## Sistema de auto-tuning (postmortem → params → predict)

El ciclo de aprendizaje automático funciona así:

```
shadow_resolve.py  →  results.csv
       ↓
shadow_postmortem.py  →  strategy_params.json
       ↓
shadow_predict.py  (lee params al inicio de cada ciclo)
```

### `strategy_params.json` — qué contiene por estrategia/subtipo

```json
{
  "UPDOWN_GBM#15min": {
    "activa": true,
    "edge_minimo": 0.02,
    "ic_bayes": 0.1985,
    "n": 15,
    "apuesta_kelly": 1.99,
    "motivo": "IC_bayes=+0.265 n=15 conf=0.75"
  }
}
```

### Umbrales de desactivación automática

| Condición | Efecto |
|---|---|
| IC < -0.10 con n ≥ 3 | `edge_minimo` sube a 0.04 (más selectivo) |
| IC < -0.20 con n ≥ 5 | `edge_minimo` sube a 0.06 |
| IC < -0.30 con n ≥ 8 | `activa = false` (desactivado) |

### Kelly dinámico (apuesta por operación)

```
si activa y n >= 5 y IC_efectivo > 0:
    apuesta_kelly = min(2.00, max(0.50, 20€ × IC_efectivo × 0.5))
sino:
    apuesta_kelly = 0.50€  (mínimo seguro)
```

`shadow_predict.py` lee `apuesta_kelly` del params más específico disponible (jerarquía: `UPDOWN_GBM#BTC#15min` > `UPDOWN_GBM#BTC` > `UPDOWN_GBM#15min` > `UPDOWN_GBM`). Lo escribe en la columna `apuesta` del CSV de predicciones. `shadow_resolve.py` lo usa para calcular el PNL real de cada operación.

---

## Estado actual (2026-06-24 ~08:46 UTC)

### Capital
- Depósito total: 30 €
- Capital operativo: 20 €
- Reserva: 10 €
- **Bankroll simulado actual**: 13.12 € (PNL acumulado: -6.88 € / -34.4% sobre operativo)

### Contexto del PNL negativo
El -6.88 € está explicado casi íntegramente por SMART_FLOW_1H antes del fix:
- SMART_FLOW_1H operaba sobre slots Up/Down 5/15min con wallet flow → IC = -0.286, PNL = -6.74 €
- **Fix aplicado** 2026-06-24: filtro `_parse_updown_tipo` excluye esos mercados de SMART_FLOW_1H
- UPDOWN_GBM sin ese ruido: PNL = -0.14 € sobre 54 ops (prácticamente break-even mientras acumula)

### Resultados por subtipo (UPDOWN_GBM)
| Subtipo | n | Win% | IC | PNL | Apuesta Kelly |
|---|---|---|---|---|---|
| #15min global | 15 | 73% | +0.199 | +7.92€ | **1.99€** |
| BTC#15min | 5 | 80% | +0.214 | +2.65€ | 0.54€ |
| XRP#15min | 2 | 100% | +0.250 | +1.91€ | 0.50€ |
| ETH#15min | 4 | 75% | +0.167 | +1.68€ | 0.50€ |
| SOL#15min | 3 | 67% | +0.100 | +0.88€ | 0.50€ |
| BNB#15min | 1 | 100% | +0.167 | +0.80€ | 0.50€ |
| BTC#5min | 11 | 45% | -0.038 | -1.71€ | 0.50€ |
| ETH#5min | 10 | 40% | -0.083 | -1.83€ | 0.50€ |
| SOL#5min | 12 | 42% | -0.071 | -2.03€ | 0.50€ |

**Conclusión clara**: los slots de 15min son el edge real. Los 5min siguen acumulando datos (no están desactivados aún, umbral en IC < -0.30 con n ≥ 8).

### Señales activas hoy (08:46 UTC)
- UPDOWN_GBM: 81 señales
- WEEKLY_PRICE: 43 señales (resuelven 16:00 UTC)
- PRICE_TARGET_GBM: 34 señales (multi-día)
- SMART_FLOW_1H: 16 señales (post-fix, sin slots)

### Loops
- `screen fast`: corriendo, ciclo ~178
- `screen slow`: corriendo, ciclo ~20

---

## Ficheros clave

### Datos commitados en GitHub
```
data/shadow/predictions_YYYY-MM-DD.csv  — predicciones del día
data/shadow/results.csv                 — resoluciones históricas acumuladas
data/shadow/strategy_accuracy.csv       — IC y stats por estrategia
data/shadow/strategy_params.json        — auto-tuning: activa, edge_min, kelly
data/shadow/performance.csv             — métricas trader: sharpe, drawdown, PF, kelly
data/shadow/postmortem.csv              — clasificación de pérdidas
data/shadow/estado_actual.md            — resumen legible, actualizado cada 60s
data/shadow/informe_bot.xlsx            — Excel completo, actualizado cada ~23min
data/prices/YYYY-MM-DD.csv             — spot BTC/ETH/SOL/XRP/DOGE/BNB cada ~60s
data/wallets/leaderboard_YYYY-MM-DD.csv — top 75 wallets
```

### Datos excluidos de GitHub (.gitignore)
```
data/binance/       — klines re-fetcheables, 25 velas × 6 activos
data/markets/       — 120-131 MB/día (snapshots de mercados)
data/trades/        — 53 MB/día
data/wallets/positions_*.csv  — 58-94 MB
data/live/          — operaciones reales (cuando existan)
data/reports/       — obsoleto, salida movida a data/shadow/
logs/               — fast.log, slow.log
```

---

## APIs utilizadas

| API | Uso | Auth |
|---|---|---|
| Polymarket Gamma API `gamma-api.polymarket.com` | Mercados, precios, eventos | Sin key |
| Polymarket data-api `data-api.polymarket.com` | Trades de wallets | Sin key |
| Kraken OHLC | Klines 1min (en `fetch_binance_klines.py`) | Sin key |
| CoinGecko `simple/price` | Spot prices en `capture_markets.py` | Sin key |

---

## Constantes importantes

### `shadow_predict.py`
```python
HORIZONTE_MIN_HORAS = 0.05   # 3 min (cubre slots 5min)
HORIZONTE_MAX_HORAS = 365*24
EDGE_MINIMO         = 0.02   # mínimo base; sube por postmortem si IC < 0
SLIPPAGE_ESTIMADO   = 0.02
```

### `shadow_resolve.py`
```python
APUESTA_SIMULADA = 0.90  # stake base fallback (se sobreescribe por Kelly en predictions)
SLIPPAGE         = 0.02
```

### `shadow_postmortem.py`
```python
APUESTA_SHADOW    = 0.90
UMBRAL_SUBIR_EDGE = (-0.10, 3)   # (IC_umbral, n_mínimo)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.30, 8)
```

### `generate_report.py`
```python
DEPOSITO_TOTAL    = 30.0
CAPITAL_OPERATIVO = 20.0
RESERVA           = 10.0
BANKROLL_INICIAL_SHADOW = CAPITAL_OPERATIVO  # = 20€
```

---

## Decisiones tomadas y por qué

### BINANCE_UPDOWN retirada (IC = -0.50)
Usaba momentum de klines (últimas 20 velas) para predecir dirección en 5min. El momentum de corto plazo no persiste en crypto. Reemplazada por UPDOWN_GBM con precio de referencia real + GBM.

### Filtro slots 5min → re-habilitado
Se desactivaron manualmente en un momento, luego se re-habilitaron porque el postmortem gestiona los subtypes automáticamente con los umbrales de IC. BTC#5min sigue sin datos suficientes para decidir; SOL y ETH están en IC ≈ -0.07, cerca del umbral de subir edge.

### SMART_FLOW_1H filtro Up/Down (fix crítico 2026-06-24)
La estrategia no tenía filtro para excluir mercados Up/Down de 5/15min. El flujo de wallets en slots de tan corto plazo es ruido puro. Se añadió `if _parse_updown_tipo(question)[0] is not None: return None` al inicio de `s_smart_flow_1h`. Las 12 pérdidas pre-fix están en el histórico pero ya no se acumulan.

### `fetch_slots_directos()` — cobertura 100% de slots
El fast loop solo leía el CSV de mercados escrito por el slow loop, que se actualiza solo el 43% del tiempo. Si un slot de 5min abría en el gap, el fast loop no lo veía. La función consulta directamente la API de Polymarket por slug (`{asset}-updown-5m-{timestamp}`) para los slots actuales y próximos.

### Kelly dinámico en apuestas
Antes: apuesta fija de 0.90 € siempre. Ahora: `apuesta = min(2€, max(0.50€, 20€ × IC_efectivo × 0.5))`. La estrategia con mejor IC (#15min global, IC=0.20) apuesta 1.99€. El resto apuesta 0.50€ mínimo hasta confirmar edge. El tamaño de apuesta se guarda en cada fila del CSV de predicciones y lo usa shadow_resolve para calcular el PNL.

### Salida Excel movida a `data/shadow/`
Antes en `data/reports/` (en .gitignore, nunca commiteado). Movida a `data/shadow/informe_bot.xlsx` para que sea visible en GitHub y se commitee automáticamente.

### `estado_actual.md` — visibilidad en tiempo real
Generado por `shadow_resumen.py` al final de cada ciclo fast. Permite ver el estado del bot en GitHub sin descargar nada ni conectarse al servidor.

---

## Pendiente / Próximos pasos

1. **Acumular más resoluciones UPDOWN_GBM#15min**: n=20, IC=+0.20. Meta: n≥50 para considerar operar en real.
2. **WEEKLY_PRICE**: primera resolución 24 Jun 16:00 UTC. Hacer postmortem.
3. **PRICE_TARGET_GBM**: sin resoluciones aún. Mercados multi-día (resuelven en semanas).
4. **SMART_FLOW_1H post-fix**: datos anteriores contaminados por slots. IC real desconocido aún.
5. **Umbral IC para live**: IC ≥ 0.10 con n ≥ 50 resoluciones por estrategia.
6. **Gestión de riesgo para live**: Kelly fraction, max apuesta = 5% del capital por trade, max exposure simultánea = 30%.

---

## Investigación pendiente — mejoras de modelo

### [IMPLEMENTADO 2026-06-24] Opción A — Filtro spot_vs_ref en slots 5min

**Problema empírico confirmado (n=68 resoluciones)**:
- Edge >10% en slots 5min (|spot_vs_ref| > 0.05%) → **21% win rate** — modelo sobreconfiado
- Edge 2-10% en slots 5min (spot ≈ ref)            → **83% win rate** — edge real

Causa: **mean reversion a corto plazo**. El GBM asume que el movimiento pasado continúa,
pero en ventanas de 5min el precio revierte hacia el nivel de referencia. Cuando spot se ha
movido +0.20% desde la referencia, el modelo dice p_up=0.95 pero el mercado (correctamente)
sigue valorando YES a 0.50.

**Fix en `s_updown_gbm`** (`shadow_predict.py`):
```python
if tipo == 'slot' and ventana_min == 5 and abs(pct) > 0.05:
    return None
```
Solo apostamos en 5min cuando spot está muy cerca del precio de referencia,
donde el edge procede de una pequeña mala valoración del mercado, no del momentum.

---

### [PENDIENTE] Opción B — Modelo mean-reversion explícito para 5min

**Cuándo activar**: cuando tengamos n≥100 resoluciones en slots 5min post-filtro A,
con IC estable para confirmar que el efecto mean-reversion es real y no ruido.

**Hipótesis**: en ventanas de 5min el proceso subyacente no es GBM (drift libre)
sino Ornstein-Uhlenbeck (mean-reverting). Si spot > ref → p_up < 0.50, no > 0.50.
Esencialmente: **usar la señal del GBM al revés** cuando el movimiento es grande.

**Implementación propuesta** (en `s_updown_gbm`, rama `tipo=='slot' y ventana_min==5`):
```python
# En lugar de: p_up = _gbm_p_up(spot, ref, sigma_h, T_h)
theta = 2.0  # velocidad de reversión — calibrar con datos reales
pct_norm = (spot / ref - 1)
p_up_mr = 0.5 - pct_norm * theta * T_h   # señal contraria al movimiento
p_up_mr = max(0.05, min(0.95, p_up_mr))
```
El parámetro `theta` debe estimarse por MLE o grid-search sobre el histórico.
Condición de activación: señal inversa con IC > +0.10 sostenido en backtesting.

---

## Comandos útiles para retomar

```bash
# Ver si los loops están corriendo
screen -ls

# Logs en tiempo real
tail -f logs/fast.log
tail -f logs/slow.log

# Estado del bot en texto (también en GitHub)
cat data/shadow/estado_actual.md

# Métricas actuales por estrategia
cat data/shadow/strategy_accuracy.csv

# Parámetros de auto-tuning actuales
python3 -c "import json; d=json.load(open('data/shadow/strategy_params.json')); [print(k, '→ activa:', v['activa'], 'IC:', v['ic_bayes'], 'kelly:', v.get('apuesta_kelly','?'), '€') for k,v in d['estrategias'].items()]"

# Últimas resoluciones
python3 -c "
import csv
rows = list(csv.DictReader(open('data/shadow/results.csv')))
for r in rows[-10:]:
    ts = r['resolution_timestamp'][:16]
    print(ts, r['strategy'], r.get('subtype',''), 'WIN' if r['acierto']=='1' else 'LOSS', r['pnl_neto'])
"

# Reiniciar loops si caen
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh

# Generar Excel manualmente
.venv/bin/python generate_report.py

# Git estado
git log --oneline -5
git status
```

---

## Diagnósticos conocidos

### PRICE_MOMENTUM da 0 señales por la mañana
Normal. Requiere drift ≥ 1.5% en el precio YES de un mercado en las últimas 6h. A las 5-10 AM UTC los mercados de predicción están quietos. Se activa entre 12:00-22:00 UTC.

### SMART_FLOW_1H da 0 señales al inicio del slow loop
El slow loop tarda ~15 min en completar capture_trades. Hasta entonces el contexto `trades_1h` está vacío y todas las señales devuelven None.

### Slots 5min: "expirados sin resolver" en logs
Normal. Los oráculos UMA tardan minutos a horas en confirmar el outcome. `shadow_resolve.py` los detecta por `closed=True` y `outcomePrices != ["0.5","0.5"]`. Salta los que tienen `end_date > ahora + 2h` para no hacer llamadas API innecesarias.

### Shadow_resolve optimización (2026-06-24)
Reducidas las consultas API de ~111 a ~23 por ciclo. Los mercados de PRICE_TARGET y WEEKLY_PRICE con vencimiento en días no se consultan cada 60s (solo los que vencen en < 2h).
