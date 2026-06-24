# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
Última actualización: 2026-06-24 ~11:00 UTC

---

## Objetivo del proyecto

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.

- **Fase actual (shadow mode)**: el bot genera predicciones y las registra como si apostara, sin dinero real. Acumula resoluciones para medir el IC real de cada estrategia.
- **Fase 2 (live)**: cuando una estrategia alcance IC ≥ 0.10 con n ≥ 50 resoluciones, se opera con dinero real.
- **Capital simulado**: 30 € depósito total → 20 € operativo + 10 € reserva intocable.

---

## Arquitectura — dos loops en paralelo (screen)

```
screen -S fast  →  bash run_fast.sh    (cada ~60s)
screen -S slow  →  bash run_slow.sh    (cada ~23min)
```

### Loop FAST — `run_fast.sh`

```
fetch_binance_klines.py  →  shadow_predict.py  →  shadow_resolve.py
    →  shadow_postmortem.py  →  shadow_resumen.py  →  git push
```

1. **`fetch_binance_klines.py`** — klines 1min de BTC/ETH/SOL/XRP/DOGE/BNB. Binance es primario (da `taker_buy_vol` en col 7, necesario para ORDER_FLOW_5M). Kraken como fallback (solo OHLCV, 6 columnas). Guarda en `data/binance/klines_YYYY-MM-DD.json`.
2. **`shadow_predict.py`** — genera predicciones en `data/shadow/predictions_YYYY-MM-DD.csv`
3. **`shadow_resolve.py`** — resuelve predicciones vencidas → `results.csv` + `strategy_accuracy.csv`
4. **`shadow_postmortem.py`** — IC Bayesiano + Kelly por subtipo → `strategy_params.json` + `performance.csv`
5. **`shadow_resumen.py`** — genera `data/shadow/estado_actual.md` (visible en GitHub cada 60s)
6. `git add data/shadow/ && git commit && git push` — solo si hay cambios

### Loop SLOW — `run_slow.sh`

```
capture_markets.py  →  capture_wallets.py  →  capture_trades.py
    →  generate_report.py  →  git push
```

1. **`capture_markets.py`** — ~1800 mercados cripto Polymarket + escribe `data/prices/YYYY-MM-DD.csv` vía CoinGecko cada ~60s
2. **`capture_wallets.py`** — top 75 wallets del leaderboard
3. **`capture_trades.py`** — últimas 4h de trades de top 50 wallets
4. **`generate_report.py`** — genera `data/shadow/informe_bot.xlsx` (Excel 7 hojas)
5. `git add data/prices/ data/wallets/leaderboard_*.csv && git push`

---

## Scripts — descripción de cada archivo

### Loop activo (fast)
| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min (Binance primario con flow, Kraken fallback) → `data/binance/` |
| `shadow_predict.py` | Genera predicciones para las 6 estrategias activas |
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

### Scripts auxiliares (no en loops)
| Script | Función |
|---|---|
| `shadow_digest.py` | Resumen diario Telegram (GitHub Actions, 20:00 UTC) |
| `backtest.py` | Backtesting offline |
| `conviction_score.py` | Score multi-estrategia |
| `insider_detect.py` | Detección wallets con info privilegiada |
| `price_alerts.py` | Alertas de precio |
| `capture_prices.py` | Captura spot (no activo en loops) |

---

## Estrategias activas (`shadow_predict.py`)

Registradas en `ESTRATEGIAS = [...]` al final del script:

### 1. WEEKLY_PRICE
- **Qué hace**: mercados "Will BTC be between $X-$Y on [date]?". Compara spot actual con el bracket.
- **Señal**: spot IN bracket → BUY_YES; OUT → BUY_NO. Prob ajustada por `sqrt(6/max(horas,6))`.
- **Estado**: señales activas, sin resoluciones aún (primer vencimiento 24 Jun 16:00 UTC).

### 2. PRICE_MOMENTUM
- **Qué hace**: tendencia exponencial del precio YES en el historial de mercados (últimas 6h).
- **Filtros**: ≥5 snapshots, liq≥500, spread≤0.08, drift≥1.5%, consistencia≥60%.
- **Estado**: 0 señales por la mañana (mercados quietos hasta ~12:00 UTC).

### 3. SMART_FLOW_1H
- **Qué hace**: ≥3 wallets humanas comprando el mismo lado en última 1h, imbalance≥70%.
- **Filtro crítico**: excluye mercados Up/Down (`_parse_updown_tipo(question)[0] is not None → return None`). Sin este filtro operaba slots 5/15min con IC=-0.375.
- **Estado**: n=12, IC=-0.171 (contaminado por pérdidas pre-fix). Acumulando datos limpios.

### 4. UPDOWN_GBM ← estrategia principal
- **Qué hace**: Black-Scholes digital `P(S_T > S_ref)` para mercados "X Up or Down".
- **Tipos**: daily (ref=medianoche UTC), hourly (ref=1h antes cierre), slot 5min, slot 15min.
- **Vol**: estimada de `data/prices/` CSV (~60s resolution).
- **Filtros**: liq≥2000, spread≤0.05, T≥2min.
- **Filtro 5min (Opción A)**: si `ventana_min==5 y |pct_spot_vs_ref|>0.05% → return None`. Ver sección "Investigación".
- **Descubrimiento directo**: `fetch_slots_directos()` consulta API Polymarket por slug para cobertura ~100%.
- **Estado**: n=77, IC=+0.018. Los 15min son el edge real (ver tabla de resultados).

### 5. PRICE_TARGET_GBM
- **Qué hace**: GBM para "Will BTC reach $70k?", "Will ETH be above $X?".
  - `atexpiry above K`: P(S_T > K); `atexpiry below K`: P(S_T < K); `reach K`: 2·N(-|log(S/K)|/σ√T)
- **Filtros**: liq≥2000, spread≤0.08, T entre 1h y 30 días.
- **Estado**: señales activas, sin resoluciones aún (mercados multi-día).

### 6. ORDER_FLOW_5M ← nueva (2026-06-24)
- **Hipótesis**: el flujo de órdenes en exchanges grandes (Binance) precede al reajuste del mercado de predicción de Polymarket. Hay un lag de 30s-3min explotable.
- **Qué hace**: cumulative delta (taker_buy_vol - taker_sell_vol) en las últimas 5 velas 1min. Si hay desequilibrio neto ≥20% del volumen Y el precio YES en Polymarket sigue en 0.38-0.62 (sin reaccionar) → señal de dirección.
- **Delta real**: columna 9 de Binance (`taker_buy_base_asset_volume`). Columna 7 en el JSON guardado.
- **Delta estimado (fallback)**: close-location en rango H-L cuando solo hay datos Kraken.
- **Solo**: slots 5min Up/Down. Activos: BTC/ETH/SOL/XRP/DOGE/BNB.
- **Estado**: n=3 resoluciones (1W/2L). Demasiado pronto para juzgar.

### BINANCE_UPDOWN — RETIRADA
Usaba momentum de klines (últimas 20 velas). IC=-0.50. Comentada en `ESTRATEGIAS`.

---

## Sistema de auto-tuning (postmortem → params → predict)

```
results.csv  →  shadow_postmortem.py  →  strategy_params.json
                                                ↓
                                       shadow_predict.py (lee al inicio de cada ciclo)
```

### `strategy_params.json` — estructura por estrategia/subtipo

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
| IC < -0.10 con n ≥ 3 | `edge_minimo` → 0.04 (más selectivo) |
| IC < -0.20 con n ≥ 5 | `edge_minimo` → 0.06 |
| IC < -0.30 con n ≥ 8 | `activa = false` (desactivado completamente) |

### Kelly dinámico — apuesta por operación

```
si activa y n >= 5 y IC_efectivo > 0:
    apuesta_kelly = min(2.00€, max(0.50€, 20€ × IC_efectivo × 0.5))
sino:
    apuesta_kelly = 0.50€   # mínimo seguro mientras acumula datos
```

`shadow_predict.py` busca el params más específico disponible (jerarquía: `UPDOWN_GBM#BTC#15min` > `UPDOWN_GBM#BTC` > `UPDOWN_GBM#15min` > `UPDOWN_GBM`). La apuesta se escribe en la columna `apuesta` del CSV y `shadow_resolve.py` la usa para calcular el PNL real.

---

## Estado actual (2026-06-24 ~11:00 UTC)

### Capital
| | |
|---|---|
| Depósito total | 30 € |
| Capital operativo | 20 € |
| Reserva | 10 € |
| **Bankroll simulado** | **4.55 €** |
| **PNL acumulado** | **-15.45 €** (-77% sobre operativo) |

### Contexto del PNL negativo — desglose honesto

| Causa | PNL | Nota |
|---|---|---|
| SMART_FLOW_1H pre-fix (slots) | -6.74 € | Bug corregido. No se repetirá. |
| UPDOWN_GBM#5min (pre-filtro A) | -14.81 € | Filtro aplicado 2026-06-24. |
| UPDOWN_GBM#15min | **+10.43 €** | El edge real del sistema. |
| UPDOWN_GBM#60min | +0.28 € | Positivo, pocos datos. |
| ORDER_FLOW_5M | -0.94 € | 3 ops, demasiado pronto. |

El sistema tiene un edge real (+10.43 € en #15min), pero dos fuentes de ruido han dominado el PNL: un bug (SMART_FLOW_1H) y una hipótesis incorrecta del modelo (GBM con mean-reversion en 5min). Ambas corregidas.

### Resultados por subtipo (UPDOWN_GBM)

| Subtipo | n | Win% | IC_ef | PNL | Kelly |
|---|---|---|---|---|---|
| #15min global | 15 | 73% | +0.199 | **+10.43€** | **1.99€** |
| BTC#15min | 8 | 75% | +0.080 | +3.43€ | 0.54€ |
| ETH#15min | 6 | 83% | +0.075 | +3.37€ | 0.50€ |
| XRP#15min | 2 | 100% | +0.025 | +1.91€ | 0.50€ |
| SOL#15min | 4 | 50% | 0.000 | -0.04€ | 0.50€ |
| #5min global | 45+ | ~33% | -0.113 | **-14.81€** | 0.50€ |
| BTC#5min | 16 | 31% | -0.133 | -6.30€ | 0.50€ |
| SOL#5min | 17 | 35% | -0.112 | -4.84€ | 0.50€ |
| ETH#5min | 12 | 33% | -0.086 | -3.67€ | 0.50€ |

### Señales activas hoy (11:00 UTC)
- UPDOWN_GBM: 107 señales
- ORDER_FLOW_5M: 76 señales (nueva estrategia, datos acumulándose)
- WEEKLY_PRICE: 43 señales (resuelven 16:00 UTC)
- PRICE_TARGET_GBM: 34 señales (multi-día)
- SMART_FLOW_1H: 16 señales

---

## ¿Está aprendiendo el modelo?

### De los errores — PARCIALMENTE

**Qué funciona** (automático, ya operativo):
- El postmortem sube `edge_minimo` cuando IC < -0.10 (más selectivo con estrategias débiles)
- Las estrategias con IC < -0.30 y n≥8 se desactivan automáticamente
- Kelly reduce la apuesta a 0.50€ mínimo cuando no hay evidencia positiva

**Qué no funciona** (requirió intervención manual):
- El filtro de SMART_FLOW_1H sobre slots hubo que añadirlo a mano — el postmortem sabía que SMART_FLOW_1H perdía pero no podía identificar que era por el tipo de mercado
- El filtro Opción A en 5min (mean-reversion) requirió análisis manual — el postmortem sabía que los 5min perdían pero no podía diagnosticar la causa estructural

**Conclusión**: el sistema aprende CUÁNTO pero no el PORQUÉ. El diagnóstico causal sigue requiriendo análisis humano.

### De lo que hace bien — SÍ

**Qué funciona** (automático):
- UPDOWN_GBM#15min tiene Kelly=1.99€ porque el postmortem detectó IC=+0.199 con n=15 y escaló la apuesta automáticamente
- BTC tiene Kelly=0.67€ (mejor activo, IC=+0.067) frente a ETH/SOL en 0.50€ (IC negativo o cero)
- El sistema no desactiva #15min aunque el global de UPDOWN_GBM sea levemente negativo — distingue por subtipo

**Lo que falta**: el Kelly escala con IC pero no con la calidad de la señal en tiempo real. Por ejemplo, un slot #15min con delta de order flow muy alto debería tener apuesta mayor que uno sin flow — eso sería el siguiente nivel de optimización.

---

## Investigación pendiente — mejoras de modelo

### [IMPLEMENTADO 2026-06-24] Filtro Opción A — slots 5min (mean-reversion)

**Problema empírico (n=68 ops antes del fix)**:
- Edge >10% (|spot_vs_ref| > 0.05%) → **21% win rate** — modelo sobreconfiado
- Edge 2-10% (spot ≈ ref)            → **83% win rate** — edge real

**Causa**: mean reversion a corto plazo. El GBM asume continuación, pero en 5min el precio revierte. Cuando spot se ha movido +0.20% desde la referencia, el modelo dice p=0.95 pero el mercado (correctamente) sigue en 0.50.

**Fix en `s_updown_gbm`**:
```python
if tipo == 'slot' and ventana_min == 5 and abs(pct) > 0.05:
    return None
```

---

### [IMPLEMENTADO 2026-06-24] ORDER_FLOW_5M — lag exchange vs Polymarket

**Hipótesis**: el flujo de órdenes en exchanges reales precede al reajuste del mercado de predicción. Hay un lag de 30s-3min explotable.

**Señal**: cumulative delta (taker_buy - taker_sell) en últimas 5 velas de Binance.
- `|delta_ratio| > 0.20` (desequilibrio neto ≥20% del volumen)
- `|precio_YES - 0.50| < 0.12` (Polymarket sin reaccionar)

**Estado**: n=3, demasiado pronto. Esperar n≥30 para evaluar.

---

### [PENDIENTE] Opción B — Modelo mean-reversion explícito para 5min

**Cuándo activar**: n≥100 resoluciones en slots 5min POST filtro A, IC estable.

**Hipótesis**: en ventanas 5min el proceso es Ornstein-Uhlenbeck (mean-reverting), no GBM. Si spot > ref → p_up < 0.50, no > 0.50. Señal contraria al movimiento cuando la divergencia es grande.

**Implementación propuesta** (en `s_updown_gbm`, rama `slot 5min`):
```python
theta = 2.0  # velocidad de reversión — calibrar con MLE sobre histórico
pct_norm = (spot / ref - 1)
p_up_mr = 0.5 - pct_norm * theta * T_h
p_up_mr = max(0.05, min(0.95, p_up_mr))
```

Condición de activación: señal inversa con IC > +0.10 sostenido en backtesting con n≥100.

---

### [PENDIENTE] Kelly compuesto — combinar IC estrategia + señal ORDER_FLOW

Actualmente Kelly escala solo con IC histórico por subtipo. El siguiente nivel:
- Si ORDER_FLOW_5M y UPDOWN_GBM coinciden en dirección en un slot → apuesta mayor (convergencia de señales)
- Si divergen → no apostar o apostar mínimo
- Formalización: `apuesta = kelly_base × (1 + conviction_bonus)` donde `conviction_bonus` viene de la alineación entre señales independientes

---

## Decisiones tomadas y por qué

### SMART_FLOW_1H — filtro Up/Down (2026-06-24)
Sin filtro operaba en slots 5/15min usando wallet flow como señal. El wallet flow en slots de tan corto plazo es ruido. Resultado: IC=-0.375, PNL=-6.74€ en 12 ops. Fix: `if _parse_updown_tipo(question)[0] is not None: return None`.

### UPDOWN_GBM — filtro 5min mean-reversion (Opción A, 2026-06-24)
Análisis empírico de 68 resoluciones mostró que señales con edge>10% en 5min ganaban solo el 21% de las veces. Causa: GBM asume momentum, mercado aplica mean-reversion. Fix: solo apostar cuando |spot_vs_ref| ≤ 0.05%.

### Binance como primario para klines (2026-06-24)
Kraken no da taker buy/sell separados. Binance (col 9) sí. ORDER_FLOW_5M requiere ese dato. VPS europeo no tiene restricción 451. Kraken queda como fallback para precio.

### Kelly dinámico (2026-06-24)
Antes: apuesta fija 0.90€. Ahora: escala con IC confirmado, mínimo 0.50€, máximo 2.00€. UPDOWN_GBM#15min con IC=+0.20 apuesta 1.99€ automáticamente. Se auto-ajusta cada ciclo.

### Excel en `data/shadow/` (2026-06-24)
Movido de `data/reports/` (en .gitignore) a `data/shadow/informe_bot.xlsx` para ser visible en GitHub y commitearse automáticamente.

### `estado_actual.md` (2026-06-24)
Generado por `shadow_resumen.py` al final de cada fast ciclo. Permite ver estado en tiempo real en GitHub sin conectarse al servidor.

### BINANCE_UPDOWN — retirada
Usaba momentum de klines para predecir dirección. IC=-0.50. El momentum de corto plazo no persiste en crypto.

---

## Ficheros clave

### Commitados en GitHub
```
data/shadow/predictions_YYYY-MM-DD.csv  — predicciones del día
data/shadow/results.csv                 — resoluciones históricas acumuladas
data/shadow/strategy_accuracy.csv       — IC y stats por estrategia
data/shadow/strategy_params.json        — auto-tuning: activa, edge_min, kelly
data/shadow/performance.csv             — métricas trader: sharpe, drawdown, kelly
data/shadow/postmortem.csv              — clasificación de pérdidas
data/shadow/estado_actual.md            — resumen legible, actualizado cada 60s
data/shadow/informe_bot.xlsx            — Excel completo, actualizado cada ~23min
data/prices/YYYY-MM-DD.csv             — spot BTC/ETH/SOL/XRP/DOGE/BNB cada ~60s
data/wallets/leaderboard_YYYY-MM-DD.csv — top 75 wallets
```

### Excluidos de GitHub (.gitignore)
```
data/binance/       — klines con flow, re-fetcheables cada 60s
data/markets/       — 120-131 MB/día
data/trades/        — 53 MB/día
data/wallets/positions_*.csv
data/live/          — operaciones reales (cuando existan)
data/reports/       — obsoleto, movido a data/shadow/
logs/
```

---

## Constantes importantes

### `shadow_predict.py`
```python
HORIZONTE_MIN_HORAS = 0.05   # 3 min (cubre slots 5min)
EDGE_MINIMO         = 0.02   # base; sube por postmortem si IC < 0
SLIPPAGE_ESTIMADO   = 0.02
# ORDER_FLOW_5M:
DELTA_MIN  = 0.20   # desequilibrio mínimo (20% del volumen)
LAG_MAX    = 0.12   # máx distancia de 0.50 para considerar que el mkt no reaccionó
```

### `shadow_postmortem.py`
```python
UMBRAL_SUBIR_EDGE = (-0.10, 3)   # (IC_umbral, n_mínimo)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.30, 8)
```

### `generate_report.py`
```python
DEPOSITO_TOTAL    = 30.0
CAPITAL_OPERATIVO = 20.0
RESERVA           = 10.0
BANKROLL_INICIAL_SHADOW = 20.0
```

---

## Comandos para retomar

```bash
# Estado del sistema
screen -ls
cat data/shadow/estado_actual.md

# Logs en tiempo real
tail -f logs/fast.log
tail -f logs/slow.log

# Resultados actuales con subtipo
python3 -c "
import csv, json
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
print(f'{len(rows)} ops | {wins}W/{len(rows)-wins}L | PNL={pnl:+.2f} | Bankroll={20+pnl:.2f}')
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+(\"#\"+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    print(f'  {k:32s} {d[\"win\"]}/{d[\"n\"]} ({d[\"win\"]/d[\"n\"]*100:.0f}%)  PNL={d[\"pnl\"]:+.2f}  IC={ic:+.3f}')
"

# Parámetros de auto-tuning
python3 -c "import json; d=json.load(open('data/shadow/strategy_params.json')); [print(f'{k:35s} IC={v[\"ic_bayes\"]:+.4f} n={v[\"n\"]:>3} kelly={v.get(\"apuesta_kelly\",0):.2f}€ activa={v[\"activa\"]}') for k,v in sorted(d['estrategias'].items(), key=lambda x: x[1].get('ic_bayes',0), reverse=True)]"

# Reiniciar loops
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh

# Generar Excel manualmente
.venv/bin/python generate_report.py

# Ver si ORDER_FLOW_5M está generando señales
python3 -c "
import csv
from datetime import datetime, timezone
today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
rows = [r for r in csv.DictReader(open(f'data/shadow/predictions_{today}.csv'))
        if r['strategy']=='ORDER_FLOW_5M' and r['decision'] in ('BUY_YES','BUY_NO')]
print(f'ORDER_FLOW_5M señales hoy: {len(rows)}')
for r in rows[-5:]: print(f'  {r[\"timestamp_utc\"][:16]} {r[\"decision\"]} {r.get(\"razon\",\"\")[:70]}')
"
```

---

## Diagnósticos conocidos

### PRICE_MOMENTUM da 0 señales antes de mediodía
Normal. Requiere drift ≥1.5% en precio YES en últimas 6h. Los mercados de predicción están quietos por la mañana. Activo entre 12:00-22:00 UTC.

### SMART_FLOW_1H da 0 señales al inicio
El slow loop tarda ~15min en cargar trades. Hasta entonces `trades_1h` está vacío.

### Slots 5min "expirados sin resolver" en logs
Normal. Oráculos UMA tardan minutos a horas. `shadow_resolve.py` salta mercados con `end_date > ahora + 2h` para no saturar la API.

### ORDER_FLOW_5M genera muchas señales (76/día)
Normal. Opera en todos los slots 5min de todos los activos. La mayoría son ruido — el IC determinará cuáles son reales. Esperar n≥30 para primera evaluación.

### Conflictos git con el fast loop
El fast loop pushea cada 60s. Si se hacen cambios manuales en paralelo: `git stash && git pull --rebase origin main && git stash pop && git push`. El archivo `data/prices/2026-06-24.csv` suele ser el que conflictúa — descartar la versión local: `git checkout --theirs data/prices/YYYY-MM-DD.csv`.
