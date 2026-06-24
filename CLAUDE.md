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

## Estado actual (actualizado 2026-06-24 ~06:36 UTC)

### Git
- Branch: `main`, sincronizado con origin
- Historia limpiada el 2026-06-24 (squash de 800+ commits de ciclos individuales)

### Loops
- Fast: corriendo, ciclo ~76+, klines OK
- Slow: corriendo, ciclo 4+ completado

### Shadow mode
- **predictions_2026-06-23.csv**: 124 filas, solo WEEKLY_PRICE
- **predictions_2026-06-24.csv**: 63+ señales UPDOWN_GBM activas (39×5min ya resueltas, 17×15min, 5×daily/hourly) + WEEKLY_PRICE
- **results.csv**: 36 resoluciones UPDOWN_GBM ya acumuladas (06:34 UTC)
- **Primera resolución WEEKLY_PRICE**: 16:00 UTC hoy

### Resultados UPDOWN_GBM — primeras 36 resoluciones (06:34 UTC)
| Duración | Win rate | PNL | n |
|----------|----------|-----|---|
| **5 min** | **44%** | **-3.68** | 25 |
| **15 min** | **88.9%** | **+6.17** | 9 |
| 60 min | 50% | -0.68 | 2 |
- IC_simple global: 0.0556 | IC_pearson: 0.05 | PNL neto: +1.82
- BTC: 72.7% acierto (mejor activo, BUY_NO dominante)
- SOL/ETH: 40-45% (peores, sobreconfiados en 5min)
- Señales high-edge (>30%) → solo 36.4% aciertos → modelo sobreconfiado en slots cortos

### Fix aplicado: slots 5min desactivados
- El GBM con ventana de vol de 20min y T≈2-4min genera probs extremas (0.85-0.95) para SOL/ETH
- El mercado valora correctamente esos slots en ~0.50 → edge aparente es ilusorio
- **Cambio en shadow_predict.py**: `if tipo == 'slot' and ventana_min <= 5: return None`
- Slots de 15min se mantienen (88.9% win rate, 9 resoluciones)

### Señales UPDOWN_GBM pendientes (daily/hourly)
- SOL/BTC/ETH Daily: resuelven a medianoche UTC
- Hourly: se van resolviendo cada hora

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

## Diagnóstico adicional — UPDOWN_GBM slots 5min

### Por qué los 5min fallan (análisis empírico 2026-06-24)
- Ventana de vol: solo 20min → si hay spike reciente, vol se dispara
- T muy pequeño (1-4min restantes al generar señal) + spot ligeramente arriba de ref → GBM da p_up≈0.90
- Mercado dice 0.50 → edge "41%" es ilusión
- SOL especialmente afectado: más volátil, más señales extremas
- **Fix**: filtrar `ventana_min ≤ 5` en s_updown_gbm

### Por qué los 15min funcionan bien
- Ventana de vol: 60min (más estable)
- T ≈ 5-12min al generar señal → prob más moderada
- El precio de referencia tiene más historia antes de que el spot cambie

---

## Pendiente / Próximos pasos

1. **16:00 UTC hoy**: primeras resoluciones de WEEKLY_PRICE (mercados 24 Jun). Hacer postmortem.
2. **UPDOWN_GBM 15min**: acumular más resoluciones (ahora n=9, muy prometedor). Meta: n≥30.
3. **UPDOWN_GBM daily/hourly**: primera resolución diaria a medianoche. Verificar referencia de precio.
4. **PRICE_MOMENTUM en horario activo**: revisar señales entre 14:00-20:00 UTC.
5. **IC mínimo para operar**: IC ≥ 0.10 con n ≥ 50 resoluciones por estrategia.
6. **Gestión de riesgo**: cuando pasar a real, definir `APUESTA_REAL` y Kelly fraction.
7. **UPDOWN_GBM mejoras potenciales** (cuando n≥50):
   - Añadir drift estimado de las últimas 24h (pequeño pero no nulo)
   - Filtrar señales donde T_h < 3min (muy cerca del vencimiento)
   - Solo operar slots con liq ≥ 5000 (slots pequeños tienen spread implícito alto)
