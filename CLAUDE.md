# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-24 ~11:15 UTC**

---

## Objetivo

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.

- **Fase actual**: shadow mode — predice y registra como si apostara, sin dinero real. Acumula resoluciones para medir el IC real de cada estrategia.
- **Fase 2 (live)**: IC ≥ 0.10 con n ≥ 50 resoluciones en una estrategia → operar con dinero real.
- **Capital simulado**: 30 € depósito → 20 € operativo + 10 € reserva intocable.

---

## Arquitectura — dos loops en screen

```
screen -S fast  →  bash run_fast.sh    (~60s por ciclo)
screen -S slow  →  bash run_slow.sh    (~23min por ciclo)
```

### Loop FAST — `run_fast.sh`

```
fetch_binance_klines.py  →  shadow_predict.py  →  shadow_resolve.py
    →  shadow_postmortem.py  →  shadow_resumen.py  →  git push
```

1. **`fetch_binance_klines.py`** — klines 1min BTC/ETH/SOL/XRP/DOGE/BNB. **Binance es primario** (da `taker_buy_vol` en columna 7 del JSON, necesario para ORDER_FLOW_5M). Kraken como fallback (6 columnas, sin order flow). Guarda en `data/binance/klines_YYYY-MM-DD.json`.
2. **`shadow_predict.py`** — genera predicciones en `data/shadow/predictions_YYYY-MM-DD.csv`. Incluye columna `features` (JSON) con datos estructurados por estrategia.
3. **`shadow_resolve.py`** — detecta mercados vencidos, resuelve, calcula PNL con Kelly dinámico. Copia columna `features` a `results.csv`.
4. **`shadow_postmortem.py`** — IC Bayesiano + Kelly + aprendizaje causal (filtros + patrones). Escribe `strategy_params.json` y `performance.csv`.
5. **`shadow_resumen.py`** — genera `data/shadow/estado_actual.md` (visible en GitHub, actualizado cada 60s).
6. `git add data/shadow/ && git commit && git push` — solo si hay cambios.

### Loop SLOW — `run_slow.sh`

```
capture_markets.py  →  capture_wallets.py  →  capture_trades.py
    →  generate_report.py  →  git push
```

1. **`capture_markets.py`** — ~1800 mercados cripto Polymarket. Escribe `data/prices/YYYY-MM-DD.csv` vía CoinGecko cada ~60s con precios spot.
2. **`capture_wallets.py`** — top 75 wallets del leaderboard.
3. **`capture_trades.py`** — últimas 4h de trades de top 50 wallets.
4. **`generate_report.py`** — genera `data/shadow/informe_bot.xlsx` (Excel 7 hojas).
5. `git add data/prices/ data/wallets/leaderboard_*.csv && git push`.

---

## Scripts — todos los archivos Python

### Activos en loops
| Script | Loop | Función |
|---|---|---|
| `fetch_binance_klines.py` | fast | Klines 1min con taker_buy_vol (Binance) o OHLCV (Kraken) |
| `shadow_predict.py` | fast | 6 estrategias → predictions CSV con columna features |
| `shadow_resolve.py` | fast | Resuelve predicciones, calcula PNL Kelly, copia features |
| `shadow_postmortem.py` | fast | IC Bayesiano + aprendizaje causal → strategy_params.json |
| `shadow_resumen.py` | fast | estado_actual.md actualizado cada 60s |
| `capture_markets.py` | slow | Mercados Polymarket + precios spot intraday |
| `capture_wallets.py` | slow | Leaderboard top 75 wallets |
| `capture_trades.py` | slow | Trades recientes de wallets top |
| `generate_report.py` | slow | Excel unificado (informe_bot.xlsx) |

### Auxiliares (no en loops)
| Script | Función |
|---|---|
| `shadow_digest.py` | Resumen diario Telegram (GitHub Actions, 20:00 UTC) |
| `backtest.py` | Backtesting offline |
| `conviction_score.py` | Score multi-estrategia |
| `insider_detect.py` | Detección wallets con información privilegiada |
| `price_alerts.py` | Alertas de precio |
| `capture_prices.py` | Captura spot (no activo en loops) |

---

## Las 6 estrategias activas

Registradas en `ESTRATEGIAS = [...]` al final de `shadow_predict.py`.

### 1. WEEKLY_PRICE
- **Qué**: mercados "Will BTC be between $X-$Y on [date]?". Compara spot con bracket.
- **Señal**: spot IN → BUY_YES; OUT → BUY_NO. Prob ajustada por `sqrt(6/max(horas,6))`.
- **Estado**: activa, sin resoluciones aún (primer vencimiento 24 Jun 16:00 UTC).

### 2. PRICE_MOMENTUM
- **Qué**: tendencia exponencial del precio YES en historial de mercados (últimas 6h).
- **Filtros**: ≥5 snapshots, liq≥500, spread≤0.08, drift≥1.5%, consistencia≥60%.
- **Estado**: 0 señales antes de mediodía (mercados quietos). Activo 12:00-22:00 UTC.

### 3. SMART_FLOW_1H
- **Qué**: ≥3 wallets humanas comprando el mismo lado en última 1h, imbalance≥70%.
- **Filtro crítico**: excluye mercados Up/Down — `_parse_updown_tipo(question)[0] is not None → return None`. Sin este filtro operaba slots con IC=-0.375.
- **Estado**: n=12, IC=-0.171 (datos contaminados pre-fix). Acumulando datos limpios.

### 4. UPDOWN_GBM ← estrategia principal con edge real
- **Qué**: Black-Scholes digital `P(S_T > S_ref | spot, σ, T)` para mercados "X Up or Down".
- **Tipos**: daily (ref=medianoche UTC), hourly (ref=1h antes cierre), slot 5min, slot 15min.
- **Vol**: estimada de `data/prices/` CSV (~60s resolution).
- **Filtros base**: liq≥2000, spread≤0.05, T≥2min.
- **Filtro 5min (Opción A)**: `if ventana_min==5 and abs(pct_spot_vs_ref)>0.05% → return None`. Mean-reversion empírico.
- **Filtros causales aprendidos** (en `strategy_params.json`, auto-actualizados):
  - SOL#5min: `|pct_spot_vs_ref| > 0.03%` → skip (IC_malo=-0.286, n=12)
  - ETH#5min: `|pct_spot_vs_ref| > 0.02%` → skip (IC_malo=-0.200, n=8)
- **Descubrimiento directo**: `fetch_slots_directos()` consulta API Polymarket por slug para cobertura ~100% de slots.
- **Features guardadas**: `{pct_spot_vs_ref, sigma_h, T_h}` en columna `features` del CSV.
- **Estado**: **#15min es el edge real** — IC=+0.239, n=21, Kelly=2.00€, 75-83% win rate.

### 5. PRICE_TARGET_GBM
- **Qué**: GBM para "Will BTC reach $70k?", "Will ETH be above $X?".
  - `atexpiry above K`: P(S_T > K); `below K`: P(S_T < K); `reach K`: 2·N(-|log(S/K)|/σ√T)
- **Filtros**: liq≥2000, spread≤0.08, T entre 1h y 30 días.
- **Estado**: señales activas, sin resoluciones (mercados multi-día).

### 6. ORDER_FLOW_5M ← nueva (2026-06-24)
- **Hipótesis**: el flujo de órdenes en Binance precede al reajuste de Polymarket en 30s-3min.
- **Qué**: cumulative delta (taker_buy_vol - taker_sell_vol) últimas 5 velas. Si `|delta_ratio| > 0.20` Y precio YES en Polymarket entre 0.38-0.62 → señal de dirección.
- **Delta real**: col 9 Binance (`taker_buy_base_asset_volume`), guardado como col 7 en el JSON.
- **Delta estimado (Kraken fallback)**: close-location en rango H-L.
- **Solo**: slots 5min Up/Down, activos BTC/ETH/SOL/XRP/DOGE/BNB.
- **Features guardadas**: `{delta_ratio, total_vol_5m, has_real_flow}`.
- **Estado**: n=16, IC=-0.089, PNL=-3.80€. Underperforming. El postmortem lo analizará automáticamente conforme acumule datos.

### BINANCE_UPDOWN — RETIRADA
IC=-0.50. Usaba momentum de klines para predecir dirección. Comentada en `ESTRATEGIAS`.

---

## Sistema de auto-tuning y aprendizaje causal

### El ciclo completo (cada 60s)

```
shadow_predict  →  predictions CSV con columna 'features' (JSON)
                    {pct_spot_vs_ref, sigma_h, T_h} para UPDOWN_GBM
                    {delta_ratio, total_vol_5m} para ORDER_FLOW_5M
       ↓
shadow_resolve  →  results.csv con 'features' copiado del prediction
       ↓
shadow_postmortem →  agrupa (strategy×subtype×feature_bucket) vs outcome
                     IC_bucket < -0.12 con n≥8 → filtros_causales (EVITAR)
                     IC_bucket > +0.12 con n≥8 → patrones_ganadores (AMPLIFICAR)
                     Escribe todo en strategy_params.json
       ↓
siguiente shadow_predict → aplica filtros_causales (skip) + patrones_ganadores (kelly_boost)
```

### Lo que aprende automáticamente

| Trigger | Acción automática |
|---|---|
| IC_subtipo < -0.10, n≥3 | `edge_minimo` → 0.04 |
| IC_subtipo < -0.20, n≥5 | `edge_minimo` → 0.06 |
| IC_subtipo < -0.30, n≥8 | `activa = false` |
| IC_feature_bucket < -0.12, n≥8 | `filtros_causales` → skip cuando feature en ese rango |
| IC_feature_bucket > +0.12, n≥8 | `patrones_ganadores` → `apuesta += kelly_boost` |
| IC_subtipo > 0, n≥5 | `apuesta_kelly = min(2€, max(0.5€, 20€×IC×0.5))` |

### `strategy_params.json` — estructura de una entrada

```json
{
  "UPDOWN_GBM#15min": {
    "activa": true,
    "edge_minimo": 0.02,
    "ic_bayes": 0.2391,
    "n": 21,
    "apuesta_kelly": 2.00,
    "filtros_causales": [],
    "patrones_ganadores": [],
    "motivo": "IC_bayes=+0.239 n=21 conf=1.00"
  },
  "UPDOWN_GBM#SOL#5min": {
    "filtros_causales": [
      {"feature": "pct_spot_vs_ref", "condicion": "abs_gt", "umbral": 0.03,
       "ic_malo": -0.286, "n_malo": 12, "ic_bueno": 0.214, "n_bueno": 5}
    ],
    "patrones_ganadores": []
  }
}
```

### FEATURE_RULES — qué features analiza el postmortem por estrategia

```python
FEATURE_RULES = {
    "UPDOWN_GBM#5min":     [("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#BTC#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#ETH#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#SOL#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#15min":    [("pct_spot_vs_ref", "abs_gt", "abs_lt"),
                            ("sigma_h",          "gt",     "lt")],
    "UPDOWN_GBM#BTC#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#ETH#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "UPDOWN_GBM#SOL#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt")],
    "ORDER_FLOW_5M":        [("delta_ratio",     "abs_lt", "abs_gt")],
}
```

---

## Estado actual (2026-06-24 ~11:15 UTC)

### Capital simulado

| | |
|---|---|
| Depósito total | 30 € |
| Capital operativo | 20 € |
| Reserva | 10 € |
| **Bankroll actual** | **1.68 €** |
| **PNL acumulado** | **-18.32 €** |

### Desglose honesto del PNL

| Fuente | PNL | Causa | Estado |
|---|---|---|---|
| UPDOWN_GBM #15min | **+9.77 €** | Edge real, modelo correcto | Activo, acumulando |
| UPDOWN_GBM #60min | +0.28 € | Edge positivo, pocos datos | Activo |
| SMART_FLOW_1H pre-fix | **-6.74 €** | Bug: operaba slots Up/Down | Corregido |
| UPDOWN_GBM #5min pre-filtro | **-14.81 €** | GBM asume momentum, mkt revierte | Filtros activos |
| ORDER_FLOW_5M | -3.80 € | Nuevo, 16 ops, early | Acumulando |

**El edge del sistema es real (+9.77€ en #15min)**. Las pérdidas vienen de dos bugs ya corregidos y una estrategia nueva aún sin datos suficientes.

### Resultados por subtipo

| Subtipo | n | Win% | IC_ef | PNL | Kelly |
|---|---|---|---|---|---|
| UPDOWN_GBM#15min (global) | 21 | 71% | +0.239 | **+9.77€** | **2.00€** |
| UPDOWN_GBM#BTC#15min | 8 | 75% | +0.080 | +3.43€ | 0.80€ |
| UPDOWN_GBM#ETH#15min | 6 | 83% | +0.075 | +3.37€ | 0.75€ |
| UPDOWN_GBM#XRP#15min | 2 | 100% | +0.025 | +1.91€ | 0.50€ |
| UPDOWN_GBM#SOL#15min | 4 | 50% | 0.000 | -0.04€ | 0.50€ |
| ORDER_FLOW_5M | 16 | 37% | -0.089 | -3.80€ | 0.50€ |
| UPDOWN_GBM#BTC#5min | 16 | 31% | -0.133 | -6.30€ | 0.50€ |
| UPDOWN_GBM#SOL#5min | 17 | 35% | -0.112 | -4.84€ | 0.50€ |
| SMART_FLOW_1H | 12 | 17% | -0.171 | -6.74€ | 0.50€ |

### Señales activas hoy (11:15 UTC)
- UPDOWN_GBM: 108 | ORDER_FLOW_5M: 91 | WEEKLY_PRICE: 43 | PRICE_TARGET_GBM: 34 | SMART_FLOW_1H: 16

### Loops
- `screen fast`: corriendo desde 05:01 UTC
- `screen slow`: corriendo desde 05:01 UTC

---

## Decisiones tomadas y por qué

### SMART_FLOW_1H — filtro Up/Down (2026-06-24)
Sin filtro operaba en slots 5/15min. El wallet flow en slots de tan corto plazo es ruido. IC=-0.375. Fix: `if _parse_updown_tipo(question)[0] is not None: return None`.

### UPDOWN_GBM — filtro Opción A (mean-reversion 5min, 2026-06-24)
Análisis empírico (n=68): edge>10% (|pct_spot_vs_ref|>0.05%) → 21% win rate. Edge<10% → 83%. El GBM asume continuación del movimiento pero en 5min el mercado revierte. Fix: `if tipo=='slot' and ventana_min==5 and abs(pct)>0.05: return None`.

### Binance como primario para klines (2026-06-24)
Kraken no da taker buy/sell separados. Binance (col 9) sí. ORDER_FLOW_5M requiere ese dato. El VPS europeo no tiene restricción 451. Kraken queda como fallback.

### Kelly dinámico (2026-06-24)
Antes: apuesta fija 0.90€. Ahora: `min(2€, max(0.5€, 20€×IC_ef×0.5))`. #15min con IC=+0.239 apuesta 2.00€ automáticamente.

### Aprendizaje causal simétrico (2026-06-24)
El postmortem ahora aprende TANTO por qué pierde COMO por qué gana, usando las `features` estructuradas guardadas en el momento de la predicción. Activa filtros (skip) para condiciones malas y boosts de Kelly para condiciones ganadoras.

### Salida Excel en `data/shadow/` (2026-06-24)
Movido de `data/reports/` (en .gitignore) a `data/shadow/informe_bot.xlsx`.

### BINANCE_UPDOWN — retirada
IC=-0.50. Momentum de klines no predice dirección en crypto a corto plazo.

---

## Investigación pendiente

### [PENDIENTE] Opción B — Ornstein-Uhlenbeck para slots 5min

**Cuándo activar**: n≥100 resoluciones en 5min POST filtro A, IC estable.

**Hipótesis**: en ventanas 5min el proceso es mean-reverting (OU), no GBM. Si spot > ref → p_up < 0.50. Usar la señal del GBM AL REVÉS cuando la divergencia es grande.

**Implementación propuesta**:
```python
# En s_updown_gbm, rama tipo=='slot' y ventana_min==5
theta = 2.0  # velocidad de reversión — calibrar con MLE sobre histórico
pct_norm = (spot / ref - 1)
p_up_mr = 0.5 - pct_norm * theta * T_h
p_up_mr = max(0.05, min(0.95, p_up_mr))
```
Condición: señal inversa con IC > +0.10 sostenido en backtesting n≥100.

---

### [PENDIENTE] Kelly compuesto — convergencia de señales

Si ORDER_FLOW_5M y UPDOWN_GBM coinciden en dirección en el mismo slot → boost adicional. Si divergen → no apostar o mínimo.

```python
# Formalización:
apuesta_final = apuesta_kelly + boost_patron_causal
if order_flow_alineado:
    apuesta_final = min(2.00, apuesta_final * 1.25)
```

---

### [PENDIENTE] Patrones ganadores automáticos (esperando datos)

Los `patrones_ganadores` en `strategy_params.json` están vacíos porque ningún bucket "bueno" tiene aún n≥8 con IC>+0.12. Se descubrirán solos cuando haya suficientes datos. Estrategias más cercanas:
- UPDOWN_GBM#SOL#5min: bucket bueno (|pct|≤0.03) tiene IC=+0.214 pero n=5. Necesita 3 más.
- UPDOWN_GBM#15min: analiza pct_spot_vs_ref y sigma_h, necesita n=21 en bucket concreto.

---

### [PENDIENTE] ORDER_FLOW_5M — evaluar en n≥30

Con 16 ops y IC=-0.089, el postmortem pronto subirá el `edge_minimo` a 0.04. Evaluar si:
- El problema es la estimación de delta (threshold 0.20 muy bajo, ruido de mercado)
- El lag Polymarket-Binance varía demasiado según la hora del día
- Segmentar por `has_real_flow=1` (Binance) vs `0` (Kraken estimado)

---

## Ficheros clave

### Commitados en GitHub
```
data/shadow/predictions_YYYY-MM-DD.csv   — predicciones (con columna 'features' JSON)
data/shadow/results.csv                  — resoluciones (con columna 'features' copiada)
data/shadow/strategy_accuracy.csv        — IC y stats por estrategia
data/shadow/strategy_params.json         — IC, Kelly, filtros_causales, patrones_ganadores
data/shadow/performance.csv              — sharpe, drawdown, kelly, profit_factor
data/shadow/postmortem.csv               — clasificación de pérdidas
data/shadow/estado_actual.md             — resumen legible, actualizado cada 60s
data/shadow/informe_bot.xlsx             — Excel 7 hojas, actualizado cada ~23min
data/prices/YYYY-MM-DD.csv              — spot cada ~60s (BTC/ETH/SOL/XRP/DOGE/BNB)
data/wallets/leaderboard_YYYY-MM-DD.csv  — top 75 wallets
```

### Excluidos de GitHub (.gitignore)
```
data/binance/    — klines con taker_buy_vol, re-fetcheables cada 60s
data/markets/    — 120-131 MB/día
data/trades/     — 53 MB/día
data/wallets/positions_*.csv
data/live/       — operaciones reales (cuando existan)
data/reports/    — obsoleto
logs/
```

---

## Constantes importantes

### `shadow_predict.py`
```python
HORIZONTE_MIN_HORAS = 0.05   # 3 min (cubre slots 5min)
EDGE_MINIMO         = 0.02   # base; sube automáticamente si IC < 0
SLIPPAGE_ESTIMADO   = 0.02
# ORDER_FLOW_5M:
DELTA_MIN = 0.20             # desequilibrio mínimo (20% del volumen)
LAG_MAX   = 0.12             # precio YES máximo alejado de 0.50
```

### `shadow_postmortem.py`
```python
IC_FILTRO_MIN  = -0.12   # IC bucket para activar filtro causal
IC_PATRON_MIN  = +0.12   # IC bucket para activar patrón ganador
N_BUCKET_MIN   =  8      # mínimo de obs en cualquier bucket
UMBRAL_SUBIR_EDGE = (-0.10, 3)
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

### `shadow_resolve.py`
```python
APUESTA_SIMULADA = 0.90   # fallback si la predicción no tiene columna 'apuesta'
SLIPPAGE         = 0.02
```

---

## Comandos para retomar

```bash
# Estado general
screen -ls
cat data/shadow/estado_actual.md

# Logs en tiempo real
tail -f logs/fast.log
tail -f logs/slow.log

# Resultados con subtipo
python3 << 'EOF'
import csv, json
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
n = len(rows)
print(f"{n} ops | {wins}W/{n-wins}L ({wins/n*100:.1f}%) | PNL={pnl:+.2f} | Bankroll={20+pnl:.2f}")
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    print(f"  {k:32s} {d['win']}/{d['n']} ({d['win']/d['n']*100:.0f}%)  PNL={d['pnl']:+.2f}  IC={ic:+.3f}")
EOF

# Filtros y patrones causales activos
python3 -c "
import json
d = json.load(open('data/shadow/strategy_params.json'))
for k,v in d['estrategias'].items():
    for f in v.get('filtros_causales',[]):
        print(f'✗ {k}: |{f[\"feature\"]}|>{f[\"umbral\"]}  IC_malo={f[\"ic_malo\"]:+.3f} n={f[\"n_malo\"]}')
    for g in v.get('patrones_ganadores',[]):
        print(f'✓ {k}: {g[\"condicion\"]} {g[\"feature\"]} {g[\"umbral\"]}  IC={g[\"ic_patron\"]:+.3f} boost=+{g[\"kelly_boost\"]}€')
"

# Kelly actual por subtipo
python3 -c "
import json
d = json.load(open('data/shadow/strategy_params.json'))
for k,v in sorted(d['estrategias'].items(), key=lambda x: x[1].get('apuesta_kelly',0), reverse=True)[:10]:
    print(f'{k:35s} IC={v[\"ic_bayes\"]:+.4f} n={v[\"n\"]:>3} kelly={v.get(\"apuesta_kelly\",0):.2f}€ activa={v[\"activa\"]}')
"

# Reiniciar loops si caen
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh

# ORDER_FLOW_5M señales recientes
python3 -c "
import csv
from datetime import datetime, timezone
today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
rows = [r for r in csv.DictReader(open(f'data/shadow/predictions_{today}.csv'))
        if r['strategy']=='ORDER_FLOW_5M' and r['decision'] in ('BUY_YES','BUY_NO')]
print(f'ORDER_FLOW_5M hoy: {len(rows)} señales')
for r in rows[-5:]: print(f'  {r[\"timestamp_utc\"][:16]} {r[\"decision\"]} {r.get(\"razon\",\"\")[:70]}')
"

# Git (cuando el loop está pusheando constantemente)
git stash && git pull --rebase origin main && git stash pop && git push origin main
```

---

## Diagnósticos comunes

### PRICE_MOMENTUM da 0 señales antes de mediodía
Normal. Necesita drift ≥1.5% en precio YES en últimas 6h. Mercados quietos hasta ~12:00 UTC.

### SMART_FLOW_1H da 0 señales al inicio
El slow loop tarda ~15min en cargar trades. Hasta entonces `trades_1h` está vacío.

### Slots 5min "expirados sin resolver" en logs
Normal. Oráculos UMA tardan minutos a horas. `shadow_resolve.py` salta mercados con `end_date > ahora + 2h`.

### Conflictos git con el fast loop
El fast loop pushea cada 60s. Si se hacen cambios manuales:
```bash
git stash && git pull --rebase origin main && git stash pop && git push origin main
```
Si hay conflicto en `data/prices/YYYY-MM-DD.csv`: `git checkout --theirs data/prices/YYYY-MM-DD.csv && git add data/prices/ && git rebase --continue`.

### `estado_actual.md` desactualizado
Si muestra timestamps viejos, el fast loop puede estar caído. Comprobar con `screen -ls` y `tail -f logs/fast.log`.

### ORDER_FLOW_5M genera muchas señales (90+/día)
Normal por ahora. Opera en todos los slots 5min de todos los activos. El postmortem irá subiendo `edge_minimo` automáticamente si el IC no mejora.

---

## Roadmap hacia autonomía

```
[✓] Aprende CUÁNTO pierde  — IC por subtipo, Kelly escala automáticamente
[✓] Aprende POR QUÉ pierde — filtros_causales sobre features (pct_spot_vs_ref, etc.)
[✓] Aprende POR QUÉ gana  — patrones_ganadores → kelly_boost automático
[ ] Kelly compuesto        — combinar ORDER_FLOW + UPDOWN_GBM en misma señal
[ ] Opción B (OU model)    — mean-reversion explícito para 5min (necesita n≥100)
[ ] Nuevas features        — añadir a FEATURE_RULES cuando surja hipótesis
[ ] Live trading           — cuando IC ≥ 0.10 con n ≥ 50 en al menos una estrategia
```

**Lo que necesitará ajuste manual periódico** (no más de una vez a la semana):
- Añadir features nuevas a `FEATURE_RULES` cuando tengas una hipótesis
- Revisar que los filtros/patrones aprendidos tienen sentido económico
- Decidir cuándo pasar a live y con qué capital
- Diagnosticar si una nueva estrategia tiene edge real o es ruido

**Todo lo demás se gestiona solo**: IC, Kelly, filtros causales, desactivaciones, patrones ganadores.
