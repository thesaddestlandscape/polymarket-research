# CLAUDE.md — Polymarket Research Bot

Contexto completo del proyecto para retomar sin releer historial. Actualizar al final de cada sesión importante.

---

## Objetivo

Bot semi-autónomo (fase actual: shadow mode) → autónomo para operar mercados cripto en Polymarket.
- **Fase 1 (ahora)**: acumular resoluciones en shadow mode, calcular IC por estrategia, validar
- **Fase 2**: operar con dinero real cuando IC ≥ 0.10 con n ≥ 50 resoluciones por estrategia

---

## Arquitectura — dos loops en paralelo (screen)

```
screen -S fast  →  bash run_fast.sh   (cada ~60s)
screen -S slow  →  bash run_slow.sh   (cada ~15min, capture_markets tarda 10min internamente)
```

### Fast loop (`run_fast.sh`)
1. `fetch_binance_klines.py` — klines 1min BTC/ETH/SOL/XRP/DOGE/BNB via Kraken
2. `shadow_predict.py` — genera predicciones en `data/shadow/predictions_YYYY-MM-DD.csv`
3. `shadow_resolve.py` — detecta resoluciones, actualiza `data/shadow/results.csv` + `strategy_accuracy.csv`
4. `git add data/shadow/ && git commit && git push origin main` — solo si hay cambios

### Slow loop (`run_slow.sh`)
1. `capture_markets.py` — ~1800 mercados cripto Polymarket (también captura precios spot cada ~60s en `data/prices/`)
2. `capture_wallets.py` — top 75 wallets por PNL+VOL del leaderboard
3. `capture_trades.py` — últimas 4h de trades de top 50 wallets
4. `git add data/prices/ data/wallets/leaderboard_*.csv && git commit && git push origin main`

**IMPORTANTE**: `capture_markets.py` es quien escribe `data/prices/YYYY-MM-DD.csv` (cada ~60s, vía CoinGecko). NO hay un `capture_prices.py` separado en los loops activos.

---

## Estrategias activas (shadow_predict.py v8)

### 1. WEEKLY_PRICE
- **Qué**: "Will BTC be between $X-$Y on [Date]?" → compara spot actual con bracket
- **Señal**: si spot IN bracket → BUY_YES con prob ajustada; si OUT → BUY_NO
- **time_scale**: `sqrt(6/max(horas,6))` — señales más conservadoras en mercados largos
- **Status**: generando señales, primeras resoluciones el 24 Jun a las 16:00 UTC

### 2. PRICE_MOMENTUM
- **Qué**: tendencia exponencial del precio YES en historial de mercados (últimas 6h)
- **Filtros**: ≥5 snapshots, liq≥500, spread≤0.08, drift≥1.5%, consistencia≥60%
- **Status**: 0 señales a las 5 AM UTC (mercados quietos en madrugada); activo en horario europeo/americano

### 3. SMART_FLOW_1H
- **Qué**: ≥3 wallets humanas (no BOT) comprando el mismo lado en la última 1h, imbalance ≥70%
- **Datos**: trades CSV del slow loop
- **Status**: 0 señales cuando el slow loop acaba de arrancar (datos de trades vacíos)

### 4. UPDOWN_GBM ← NUEVA (implementada 2026-06-24)
- **Qué**: Black-Scholes digital P(S_T > S_ref | spot, σ, T) para mercados "X Up or Down"
- **Tipos**: daily (medianoche UTC como ref), hourly (1h antes del cierre), slot 5/15min (inicio del slot)
- **Vol**: estimada de últimas 2h de `data/prices/` CSV (~60s resolution)
- **Referencia**: `_precio_en(activo, ref_time, precios_intraday, tol_min)`
- **Filtros**: liq≥2000, spread≤0.05, T≥2min
- **Status**: primera predicciones a las 05:30 UTC, 13 señales activas (BTC/ETH/SOL daily + slots)

---

## .gitignore — archivos excluidos de GitHub

```
data/binance/       # klines re-fetcheables, cambian cada 60s
data/markets/       # 120-131 MB/día, excede límite GitHub 100MB
data/trades/        # 53 MB/día
data/wallets/positions_*.csv  # 58-94 MB
data/funding/, data/alerts/, data/live/, data/reports/
logs/               # no necesitan backup en git
```

**Solo se commitean**: `data/shadow/`, `data/prices/`, `data/wallets/leaderboard_*.csv`, código Python

---

## APIs utilizadas

- Polymarket Gamma API: `https://gamma-api.polymarket.com`
- Polymarket data-api: `https://data-api.polymarket.com`  
- Kraken OHLC (klines): endpoint público, no requiere API key
- CoinGecko simple/price: para spot prices en prices CSV

---

## Ficheros clave de datos

```
data/shadow/predictions_YYYY-MM-DD.csv  — predicciones del día (una fila por mercado×estrategia)
data/shadow/results.csv                 — resoluciones históricas acumuladas
data/shadow/strategy_accuracy.csv       — IC y stats por estrategia (actualizado por shadow_resolve)
data/shadow/strategy_params.json        — LEGACY, no lo usa v8; estrategias hardcoded en shadow_predict
data/prices/YYYY-MM-DD.csv             — spot BTC/ETH/SOL/XRP/DOGE/BNB/etc cada ~60s (CoinGecko)
data/wallets/leaderboard_YYYY-MM-DD.csv — top 75 wallets
data/binance/klines_YYYY-MM-DD.json    — 25 velas 1min, cada asset por separado
```

---

## Estado actual (actualizado 2026-06-24 ~05:45 UTC)

### Git
- Branch: `main`, sincronizado con origin
- Historia limpiada el 2026-06-24 (squash de 800+ commits de ciclos individuales)
- Último commit: `feat: estrategia UPDOWN_GBM`

### Loops
- Fast: corriendo, ciclo ~8+, klines OK
- Slow: ciclo 4 completado, push OK a las 05:33 UTC

### Shadow mode
- **predictions_2026-06-23.csv**: 124 filas, solo WEEKLY_PRICE
- **predictions_2026-06-24.csv**: ~135+ filas, WEEKLY_PRICE (90 BUY) + UPDOWN_GBM (13 señales)
- **results.csv**: NO existe aún (ningún mercado resuelto todavía)
- **Primera resolución esperada**: 16:00 UTC hoy (mercados WEEKLY_PRICE del 24 Jun)

### Señales UPDOWN_GBM activas más importantes
- SOL Daily BUY_NO: modelo 0.60 vs mercado 0.75, edge=12.7% — la más grande
- BTC/ETH Daily BUY_NO: modelo ~0.60 vs mercado 0.675, edge ~5%
- BTC/ETH/SOL/XRP slots 5-15min: varios BUY_YES con edges 3-41%

### Advertencia sobre daily BUY_NO
El modelo asume drift=0. Si el mercado "Up or Down on June 24?" usa como referencia la medianoche UTC, nuestro cálculo es correcto. Si usa otro precio de referencia (ej. 4PM ET del día anterior), la señal podría ser espuria. El shadow mode lo revelará tras las primeras resoluciones.

---

## Diagnóstico de estrategias

### Por qué PRICE_MOMENTUM da 0 señales por la mañana
- Requiere drift ≥1.5% en el precio YES de un mercado en las últimas 6h
- A las 5 AM UTC los mercados de predicción están quietos
- Se espera actividad en horario 12:00-22:00 UTC

### Por qué SMART_FLOW_1H da 0 señales al inicio
- Depende de datos de trades del slow loop
- El slow loop tarda ~10 min en completar capture_trades
- Después del arranque hay ~15 min de warm-up

### Por qué BINANCE_UPDOWN fue desactivada (IC=-0.50)
- Usaba momentum de klines (últimas 20 velas) para predecir dirección FUTURA en 5min
- Momentum de corto plazo no persiste → señal sin edge real
- Reemplazada por UPDOWN_GBM que usa precio de referencia real + GBM

---

## Comandos útiles

```bash
# Ver estado
screen -ls
bash status.sh        # si existe, muestra logs rápidos
tail -f logs/fast.log
tail -f logs/slow.log

# Reiniciar loops (si caen)
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh

# Verificar predicciones activas
python3 -c "
import csv; rows = list(csv.DictReader(open('data/shadow/predictions_2026-06-24.csv')))
buys = [r for r in rows if r['decision'] in ('BUY_YES','BUY_NO')]
print(f'{len(buys)} señales activas por estrategia:')
from collections import Counter; print(Counter(r['strategy'] for r in buys))
"

# Ver resoluciones (cuando haya)
cat data/shadow/results.csv
cat data/shadow/strategy_accuracy.csv

# Git status
git log --oneline -5
git status
```

---

## Pendiente / Próximos pasos

1. **16:00 UTC hoy**: primeras resoluciones de WEEKLY_PRICE (mercados 24 Jun). Hacer postmortem.
2. **UPDOWN_GBM calibración**: verificar que la referencia de precio es correcta comparando resoluciones reales.
3. **PRICE_MOMENTUM en horario activo**: revisar señales entre 14:00-20:00 UTC.
4. **IC mínimo para operar**: IC ≥ 0.10 con n ≥ 50 resoluciones por estrategia.
5. **Gestión de riesgo**: cuando pasar a real, definir `APUESTA_REAL` y Kelly fraction.
6. **UPDOWN_GBM mejoras potenciales**:
   - Añadir drift estimado de las últimas 24h (pequeño pero no nulo)
   - Mejorar detección del precio de referencia para slots (timing preciso)
   - Solo operar slots con liq ≥ 5000 (slots pequeños tienen spread implícito alto)
