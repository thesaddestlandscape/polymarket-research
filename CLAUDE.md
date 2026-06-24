# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-24 ~12:15 UTC**

---

## ⚡ PROTOCOLO DE INICIO DE SESIÓN — ejecutar SIEMPRE al arrancar

**Claude: al leer esto, ejecuta inmediatamente antes de responder nada más:**

1. `cat data/shadow/estado_actual.md` — bankroll y PNL actual
2. Análisis WIN vs LOSS por subtipo (extraer features de razon si no hay columna features)
3. Leer `data/shadow/hipotesis_*.md` — hipótesis anteriores y su estado
4. Leer `data/shadow/arb_scan_*.csv` del día — oportunidades de arbitraje detectadas
5. Presentar:
   - Bankroll actual y PNL desde última sesión
   - Nuevas resoluciones y su impacto
   - Estado de hipótesis bajo vigilancia (especialmente H3 BTC#5min)
   - Oportunidades de arb detectadas si las hay

**Seguimiento obligatorio cada sesión — hipótesis bajo vigilancia:**
- **H3 BTC#5min momentum** (2026-06-24): pct WIN=0.054% vs LOSS=0.023% — patrón opuesto a ETH/SOL. Reportar n actual y si el patrón persiste. Activar filtro inverso si n≥20 y IC>+0.10.

---

## Objetivo

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.

- **Fase actual**: shadow mode — predice y registra, sin dinero real.
- **Fase 2 (live)**: IC ≥ 0.10 con n ≥ 50 resoluciones en una estrategia.
- **Capital simulado**: 30 € depósito → 20 € operativo + 10 € reserva.

---

## Arquitectura — dos loops en screen

```
screen -S fast  →  bash run_fast.sh    (~60s por ciclo)
screen -S slow  →  bash run_slow.sh    (~23min por ciclo)
```

### Loop FAST — `run_fast.sh`

```
fetch_binance_klines  →  shadow_predict  →  shadow_resolve
    →  shadow_postmortem  →  shadow_resumen  →  git push
```

1. **`fetch_binance_klines.py`** — klines 1min. **Binance es primario** (columna 7 = `taker_buy_vol` para ORDER_FLOW_5M). Kraken fallback (6 columnas, sin order flow).
2. **`shadow_predict.py`** — 6 estrategias → predictions CSV con columna `features` (JSON).
3. **`shadow_resolve.py`** — resuelve, calcula PNL Kelly, copia columna `features` a results.
4. **`shadow_postmortem.py`** — IC Bayesiano + Kelly + aprendizaje causal → `strategy_params.json`.
5. **`shadow_resumen.py`** — genera `data/shadow/estado_actual.md`.
6. `git push` si hay cambios.

### Loop SLOW — `run_slow.sh`

```
capture_markets  →  capture_wallets  →  capture_trades
    →  generate_report  →  arb_scanner  →  git push
```

1. **`capture_markets.py`** — ~1800-2400 mercados + precios spot intraday en `data/prices/`.
2. **`capture_wallets.py`** — top 75 wallets del leaderboard.
3. **`capture_trades.py`** — últimas 4h de trades de top 50 wallets.
4. **`generate_report.py`** — Excel `data/shadow/informe_bot.xlsx` (7 hojas).
5. **`arb_scanner.py`** — escanea ~2400 mercados buscando bracket arb → `data/shadow/arb_scan_YYYY-MM-DD.csv`.
6. `git push` con precios, leaderboard, hipótesis, arb_scan.

---

## Scripts — todos los archivos Python

### Activos en loops
| Script | Loop | Función |
|---|---|---|
| `fetch_binance_klines.py` | fast | Klines 1min con taker_buy_vol (Binance) o OHLCV (Kraken) |
| `shadow_predict.py` | fast | 6 estrategias → predictions CSV con columna features |
| `shadow_resolve.py` | fast | Resuelve, PNL Kelly, copia features a results |
| `shadow_postmortem.py` | fast | IC Bayesiano + aprendizaje causal → strategy_params.json |
| `shadow_resumen.py` | fast | estado_actual.md actualizado cada 60s |
| `capture_markets.py` | slow | ~2400 mercados Polymarket + precios spot intraday |
| `capture_wallets.py` | slow | Leaderboard top 75 wallets |
| `capture_trades.py` | slow | Trades recientes de wallets top |
| `generate_report.py` | slow | Excel unificado (informe_bot.xlsx) |
| `arb_scanner.py` | slow | Escáner de arbitraje bracket → arb_scan_YYYY-MM-DD.csv |

### Auxiliares (no en loops)
| Script | Función |
|---|---|
| `shadow_digest.py` | Resumen diario Telegram (GitHub Actions, 20:00 UTC) |
| `llm_hypothesis.py` | Meta-learner LLM (manual; ver sección LLM) |
| `backtest.py` | Backtesting offline |
| `conviction_score.py` | Score multi-estrategia |
| `insider_detect.py` | Detección wallets con info privilegiada |

---

## Las 6 estrategias activas

### 1. WEEKLY_PRICE
- **Qué**: "Will BTC be between $X-$Y on [date]?". Spot vs bracket → BUY_YES/BUY_NO.
- **Estado**: activa, primeras resoluciones el 24 Jun 16:00 UTC.

### 2. PRICE_MOMENTUM
- **Qué**: tendencia exponencial del precio YES (últimas 6h de snapshots).
- **Estado**: 0 señales antes de mediodía. Activo 12:00-22:00 UTC.

### 3. SMART_FLOW_1H
- **Qué**: ≥3 wallets humanas comprando el mismo lado en 1h, imbalance≥70%.
- **Filtro crítico**: excluye mercados Up/Down (`_parse_updown_tipo` → `return None`).
- **Estado**: n=12, IC=-0.171 (contaminado pre-fix). Acumulando datos limpios.

### 4. UPDOWN_GBM ← estrategia principal con edge real
- **Qué**: Black-Scholes digital `P(S_T > S_ref)` para mercados "X Up or Down".
- **Tipos**: daily, hourly, slot 5min, slot 15min.
- **Filtro 5min (Opción A)**: `if ventana_min==5 and abs(pct_spot_vs_ref)>0.05% → return None`.
- **Filtros causales aprendidos** (auto-actualizados por postmortem):
  - BTC#5min: `sigma_h > 0.0018` → skip
  - ETH#5min: `|pct|>0.02%` + `sigma_h > 0.0024` → skip
  - SOL#5min: `|pct|>0.03%` + `sigma_h > 0.0018` → skip
- **Features guardadas**: `{pct_spot_vs_ref, sigma_h, T_h}` en columna `features`.
- **Estado**: **#15min es el edge real** — IC=+0.239, n=21+, Kelly=2.00€, 75%+ win rate.

### 5. PRICE_TARGET_GBM
- **Qué**: GBM para "Will BTC reach $70k?", "Will ETH be above $X?".
- **Estado**: señales activas, sin resoluciones aún (mercados multi-día).

### 6. ORDER_FLOW_5M ← nueva (2026-06-24)
- **Qué**: cumulative delta (taker_buy - taker_sell) últimas 5 velas de Binance.
- **Señal**: `|delta_ratio| > 0.38` Y precio YES en 0.38-0.62 → BUY.
- **Features guardadas**: `{delta_ratio, total_vol_5m, has_real_flow}`.
- **Estado**: n=16+, IC≈-0.09. El postmortem subirá edge_minimo automáticamente si no mejora.

---

## Sistema de aprendizaje causal (ciclo completo)

```
shadow_predict  →  predictions CSV (columna 'features' JSON)
       ↓
shadow_resolve  →  results.csv (columna 'features' copiada)
       ↓
shadow_postmortem  →  agrupa por (strategy×subtype×feature_bucket) vs outcome
                       IC_bucket < -0.12 con n≥8  →  filtros_causales (EVITAR)
                       IC_bucket > +0.12 con n≥8  →  patrones_ganadores (AMPLIFICAR + kelly_boost)
                       Escribe todo en strategy_params.json
       ↓
siguiente shadow_predict  →  aplica filtros_causales (skip) + patrones_ganadores (kelly_boost)
```

### FEATURE_RULES — qué features analiza el postmortem

```python
FEATURE_RULES = {
    "UPDOWN_GBM#5min":     [("pct_spot_vs_ref", "abs_gt", "abs_lt"),
                            ("sigma_h",          "gt",     "lt")],
    "UPDOWN_GBM#BTC#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#ETH#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#SOL#5min": [("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#15min":    [("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#BTC#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#ETH#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "UPDOWN_GBM#SOL#15min":[("pct_spot_vs_ref", "abs_gt", "abs_lt"), ("sigma_h", "gt", "lt")],
    "ORDER_FLOW_5M":        [("delta_ratio",     "abs_lt", "abs_gt")],
}
```

### Kelly dinámico

```
si activa y n >= 5 y IC_efectivo > 0:
    apuesta_kelly = min(2.00€, max(0.50€, 20€ × IC_ef × 0.5))
sino:
    apuesta_kelly = 0.50€

+ patrones_ganadores: apuesta += kelly_boost (si feature en rango ganador)
```

---

## Estado actual (2026-06-24 ~12:15 UTC)

### Capital simulado
| | |
|---|---|
| Depósito | 30 € |
| Operativo | 20 € |
| Reserva | 10 € |
| **Bankroll actual** | **~1.68 €** (ver estado_actual.md para dato en tiempo real) |

### Contexto del PNL negativo
- SMART_FLOW_1H pre-fix en slots: **-6.74 €** (bug corregido)
- UPDOWN_GBM#5min pre-filtros: **-14.81 €** (filtros aplicados)
- UPDOWN_GBM#15min: **+9.77 €** (el edge real del sistema)
- Los filtros causales automáticos (sigma_h, pct) están reduciendo las pérdidas de #5min

### Estrategia con edge confirmado
| Subtipo | n | Win% | IC_ef | Kelly |
|---|---|---|---|---|
| UPDOWN_GBM#15min global | 21+ | ~73% | +0.239 | **2.00€** |
| UPDOWN_GBM#BTC#15min | 8 | 75% | +0.080 | 0.80€ |
| UPDOWN_GBM#ETH#15min | 6 | 83% | +0.075 | 0.75€ |

---

## Arbitraje — `arb_scanner.py`

### Qué detecta

**BRACKET_ARB**: eventos con múltiples mercados de precio-rango mutuamente excluyentes donde la suma de YES < 0.97.

Ejemplo real detectado (2026-06-24 mañana, ya expiró):
- "Ethereum price on June 28?" — 8 brackets $1,300-$2,200
- Suma YES = 0.926 → profit neto 5.4% después de 2% fee en el bracket ganador
- **RIESGO**: si ETH sale de $1,300-$2,200, todos los brackets pierden

**¿Por qué no es arb puro?** No hay brackets para todos los rangos posibles. El profit viene de apostar implícitamente que el precio estará DENTRO del rango total cubierto.

### Cómo actuar cuando aparece una oportunidad

1. Comprobar que los brackets son EXHAUSTIVOS para el rango cubierto (sin gaps)
2. Verificar que el rango es creíble para el plazo (spot actual ±margen razonable)
3. Calcular liq_min — es el capital máximo que puedes desplegar por leg
4. En shadow mode: registrar señal pero NO generar predicción automática
5. En live mode (futuro): apostar `liq_min` en cada bracket simultáneamente

### Estado del escáner
- Corre cada ~23 min en el slow loop
- Guarda en `data/shadow/arb_scan_YYYY-MM-DD.csv`
- LIQ_MIN = 200 (bracket mínimo de $200 en liquidez)
- UMBRAL_ARB = 0.97 (suma YES < esto para trigger)

---

## Investigación pendiente

### [IMPLEMENTADO] Opción A — filtro mean-reversion 5min
Edge >10% (|pct|>0.05%) → 21% win rate. Filtro manual en `s_updown_gbm`.

### [IMPLEMENTADO] sigma_h como filtro en 5min
ETH: sigma WIN=0.0024 vs LOSS=0.0035 (Δ=46%). BTC similar. En FEATURE_RULES.
Filtros causales descubiertos automáticamente: BTC sigma>0.0018, ETH sigma>0.0024, SOL sigma>0.0018.

### [IMPLEMENTADO] ORDER_FLOW_5M umbral 0.38
WIN_avg delta=0.445 vs LOSS_avg=0.384. Subido de 0.20 a 0.38.

### [PENDIENTE] Opción B — Ornstein-Uhlenbeck para 5min
Cuando n≥100 en 5min post-filtros. Hipótesis: proceso mean-reverting, no GBM.
Implementación: `p_up_mr = 0.5 - pct_norm × theta × T_h` (theta a calibrar).

### [PENDIENTE] Kelly compuesto — convergencia ORDER_FLOW + UPDOWN_GBM
Si ambas coinciden en dirección → boost. Si divergen → skip.

### [PENDIENTE] Expiry Fade
Fading de precios extremos en la última hora antes del vencimiento.
Caso natural: WEEKLY_PRICE 16:00 UTC. Analizar hoy si hay sesgo detectable.

### [PENDIENTE] LP Rewards — market making como capa adicional en live

Polymarket paga recompensas USDC a quienes ponen órdenes límite dentro de la banda δ (half-width) del programa LP, independientemente del resultado del mercado.

**Cuándo activar**: cuando estemos en live con capital real.
**Cómo**: en mercados donde ya tenemos señal de predicción, poner simultáneamente una orden límite en el lado contrario para cobrar LP rewards. El spread + recompensas reducen el break-even.
**Riesgo clave**: adverse selection — alguien te llena porque tiene info que tú no tienes.
**Mitigación**: fill cooldowns + mid-price jump filter + pausar si hay inventario abierto.
**Requiere**: CLOB API (wallet + firma de transacciones), distinta de la Gamma API actual.
**Referencia**: github.com/lihanyu81/polymarket_lp_tool (gestión automática de órdenes límite).

### [PENDIENTE] Resolution Sniper — vincular con Expiry Fade y WEEKLY_PRICE

Cuando un mercado está en los últimos 60-90 minutos antes de resolver y el modelo GBM
da p≥0.95 pero el precio de mercado está en 0.85-0.90 → edge real de 5-10%.

**Caso natural**: mercados WEEKLY_PRICE en la última hora. Si BTC está en $62,500
y el bracket es $62k-$64k con 45 min restantes, p_GBM ≈ 0.98, precio ≈ 0.90 → 8% edge.
Es una versión más agresiva de WEEKLY_PRICE concentrada en el tramo final.

**Implementación propuesta**: añadir a `s_weekly_price` un multiplicador de confianza
cuando `T_h < 1.5` y `p_modelo > 0.92`. O estrategia separada `RESOLUTION_SNIPER`.
**Cuando activar**: tras analizar los WEEKLY_PRICE que resuelven hoy 16:00 UTC.
**Referencia**: github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits — strategy #7.

---

### [PENDIENTE] Orderbook Imbalance (OBI) — señal sin datos externos

Ratio bid/ask depth como señal de dirección, 100% interno a Polymarket, sin feeds externos.

**Lógica**: si hay más liquidez en el lado bid que en el ask → presión compradora → bias YES.
```python
obi = (best_bid_depth - best_ask_depth) / (best_bid_depth + best_ask_depth)  # [-1, +1]
```
**Problema actual**: `capture_markets.py` guarda `best_bid` y `best_ask` como PRECIO,
no como tamaño/profundidad. Necesitaría añadir `best_bid_size` y `best_ask_size` a la captura.
**Cuando activar**: cuando modifiquemos `capture_markets.py` para capturar profundidad.
Añadir `delta_obi` a FEATURE_RULES para UPDOWN_GBM y ORDER_FLOW_5M.
**Alternativa sin modificar captura**: usar APIs externas de datos de orderbook:
  - **Marketlens** — datos históricos tick-level de Polymarket (bid/ask depth histórico)
  - **Probalytics** — API REST, 200-500M actualizaciones orderbook/día en tiempo real
  Ambos darían `best_bid_size` y `best_ask_size` sin tocar `capture_markets.py`.
**Referencia**: strategy #8 HarrierOnChain; Marketlens + Probalytics en Awesome-PM-Tools.

---

### [PENDIENTE] On-Chain Whale Signal — upgrade de SMART_FLOW_1H

Leer el blockchain de Polygon directamente para detectar posiciones de whales
**3-30 segundos antes** de que aparezcan en la API pública (vs nuestros ~15 min de delay).

**Cómo**: suscripción a bloques de Polygon + decodificar ABI calldata de transacciones
de Polymarket para inferir posiciones en tiempo real.
**Requiere**: nodo RPC Polygon (Alchemy/Infura) o acceso a eventos WebSocket.
**Cuando activar**: cuando SMART_FLOW_1H tenga IC > +0.05 con n≥30 datos limpios
y queramos reducir el delay de señal de 15min a <30s.
**Referencia**: strategy #10.

---

### [PENDIENTE — baja prioridad] SMART_FLOW_1H refinements

Cuando SMART_FLOW_1H tenga n≥30 resoluciones limpias (post-fix) y IC real confirmado,
revisar estos dos filtros adicionales de `github.com/MrFadiAi/Polymarket-bot`:

1. **Excluir one-hit wonders**: descartar wallets donde >30% del PNL total viene de
   una sola operación. Evita copiar a alguien con un golpe de suerte, no edge real.
   Implementación: en `capture_wallets.py`, calcular concentración de PNL por trade.

2. **Profit factor ≥1.5x**: ratio ganancias_totales / pérdidas_totales. Más robusto
   que win rate solo porque captura el tamaño de las operaciones.

**Por qué no ahora**: IC actual es -0.171 con datos contaminados pre-fix. No merece
optimizar el filtrado de wallets hasta validar el IC base con datos limpios.

### [PENDIENTE] Cross-Market Arb (Polymarket vs Kalshi)

Misma pregunta en dos plataformas con precios distintos → comprar en la más barata,
vender en la más cara, profit garantizado del spread.
**Requiere**: CLOB API en ambas plataformas + capital real.
**Cuando activar**: junto con LP rewards, al ir a live.
**Referencia**: strategy #3 — "lock the spread, not the direction".

---

### [PENDIENTE] LLM hypothesis diario
`llm_hypothesis.py` existe pero requiere ANTHROPIC_API_KEY.
Alternativa: pedir análisis al inicio de cada sesión aquí en Claude Code (gratis con Pro).

---

## Ficheros clave

### Commitados en GitHub
```
data/shadow/predictions_YYYY-MM-DD.csv  — predictions con columna 'features' JSON
data/shadow/results.csv                 — resoluciones con 'features' copiada
data/shadow/strategy_accuracy.csv
data/shadow/strategy_params.json        — IC, Kelly, filtros_causales, patrones_ganadores
data/shadow/performance.csv
data/shadow/postmortem.csv
data/shadow/estado_actual.md            — actualizado cada 60s
data/shadow/informe_bot.xlsx            — Excel, actualizado cada ~23min
data/shadow/arb_scan_YYYY-MM-DD.csv    — oportunidades de arbitraje bracket
data/shadow/hipotesis_YYYY-MM-DD.md    — hipótesis con evidencia
data/prices/YYYY-MM-DD.csv             — spot cada ~60s
data/wallets/leaderboard_YYYY-MM-DD.csv
```

### Excluidos (.gitignore)
```
data/binance/   data/markets/   data/trades/
data/wallets/positions_*.csv   data/live/   logs/
```

---

## Constantes clave

### `shadow_predict.py`
```python
HORIZONTE_MIN_HORAS = 0.05   # 3 min
EDGE_MINIMO = 0.02
SLIPPAGE_ESTIMADO = 0.02
# ORDER_FLOW_5M:
DELTA_MIN = 0.38
LAG_MAX   = 0.12
```

### `shadow_postmortem.py`
```python
IC_FILTRO_MIN  = -0.12   # umbral para filtros_causales
IC_PATRON_MIN  = +0.12   # umbral para patrones_ganadores
N_BUCKET_MIN   =  8
UMBRAL_SUBIR_EDGE = (-0.10, 3)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.30, 8)
```

### `arb_scanner.py`
```python
UMBRAL_ARB  = 0.97   # suma YES < esto → BRACKET_ARB
UMBRAL_OVER = 1.02   # suma YES > esto → OVERROUND
LIQ_MIN     = 200    # liq del bracket más pequeño
N_MIN       = 3      # mínimo de brackets
FEE_PAYOUT  = 0.02   # fee 2% sobre el payout ganador
```

### `generate_report.py`
```python
DEPOSITO_TOTAL    = 30.0
CAPITAL_OPERATIVO = 20.0
RESERVA           = 10.0
```

---

## Roadmap hacia autonomía

```
[✓] Aprende CUÁNTO pierde  — IC + Kelly por subtipo
[✓] Aprende POR QUÉ pierde — filtros_causales sobre features
[✓] Aprende POR QUÉ gana  — patrones_ganadores → kelly_boost
[✓] Escáner de arbitraje   — bracket arb en ~2400 mercados cada ~23min
[ ] Kelly compuesto        — combinar ORDER_FLOW + UPDOWN_GBM
[ ] Opción B (OU model)    — mean-reversion explícito para 5min (n≥100)
[ ] Expiry Fade            — fading de precios extremos pre-vencimiento
[ ] Resolution Sniper      — analizar tras WEEKLY_PRICE 16:00 UTC hoy
[ ] OBI (Orderbook Imbalance) — añadir profundidad bid/ask a capture_markets
[ ] On-Chain Whale Signal  — upgrade SMART_FLOW_1H con Polygon RPC (cuando IC>+0.05)
[ ] Cross-Market Arb       — Polymarket vs Kalshi (cuando estemos en live)
[ ] LP Rewards (market making) — apilar sobre predicción en live
[ ] Live trading           — IC ≥ 0.10, n ≥ 50, bankroll recapitalizado
```

---

## Comandos para retomar

```bash
screen -ls
cat data/shadow/estado_actual.md
tail -f logs/fast.log
tail -f logs/slow.log

# Resultados completos
python3 << 'EOF'
import csv, json
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
n = len(rows)
print(f"{n} ops | {wins}W/{n-wins}L ({wins/n*100:.1f}%) | PNL={pnl:+.2f}€ | Bankroll={20+pnl:.2f}€")
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    print(f"  {k:32s} {d['win']}/{d['n']} ({d['win']/d['n']*100:.0f}%)  PNL={d['pnl']:+.2f}  IC={ic:+.3f}")
EOF

# Arb scan del día
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null || echo "Sin scan hoy aún"

# Filtros causales activos
python3 -c "
import json
d = json.load(open('data/shadow/strategy_params.json'))
for k,v in d['estrategias'].items():
    for f in v.get('filtros_causales',[]):
        print(f'✗ {k}: |{f[\"feature\"]}|>{f[\"umbral\"]}  IC_malo={f[\"ic_malo\"]:+.3f}')
    for g in v.get('patrones_ganadores',[]):
        print(f'✓ {k}: {g[\"condicion\"]} {g[\"feature\"]} {g[\"umbral\"]}  boost=+{g[\"kelly_boost\"]}€')
"

# Reiniciar loops
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh

# Git cuando hay conflictos con el fast loop
git stash && git pull --rebase origin main && git stash pop && git push origin main
```

---

## Diagnósticos comunes

### PRICE_MOMENTUM 0 señales por la mañana
Normal. Necesita drift ≥1.5% en últimas 6h. Activo 12:00-22:00 UTC.

### SMART_FLOW_1H 0 señales al inicio
Normal. Trades se cargan ~15min después de arrancar el slow loop.

### Conflictos git con el fast loop
El fast loop pushea cada 60s. Resolución: `git stash && git pull --rebase && git stash pop && git push`.
Si conflicto en prices CSV: `git checkout --theirs data/prices/YYYY-MM-DD.csv`.

### arb_scanner no detecta nada
Normal la mayor parte del tiempo. Las oportunidades bracket duran horas o días, no minutos.
El OVERROUND (suma>1.02) se registra siempre como observación aunque no sea accionable.
