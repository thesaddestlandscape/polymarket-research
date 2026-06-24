# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-24 ~13:30 UTC**

---

## ⚡ PROTOCOLO DE INICIO DE SESIÓN — ejecutar SIEMPRE

**Claude: al leer esto, ejecuta inmediatamente antes de responder nada más:**

```bash
# 1. Estado del sistema
cat data/shadow/estado_actual.md

# 2. Resultados completos con IC por subtipo
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

# 3. Arb scan del día
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null | head -5 || echo "Sin oportunidades hoy"
```

**Presentar al usuario:**
- Bankroll actual y PNL desde última sesión
- Nuevas resoluciones y su impacto por estrategia
- Estado H3 (BTC#5min momentum): n actual y si patrón persiste
- Oportunidades de arb detectadas si las hay
- Hipótesis que se han confirmado o descartado

**Seguimiento obligatorio — hipótesis bajo vigilancia:**
- **H3 BTC#5min momentum**: pct WIN=0.054% vs LOSS=0.023% — opuesto a ETH/SOL. Reportar n actual. Activar filtro inverso si n≥20 y IC>+0.10.
- **ORDER_FLOW_5M**: monitorear si IC>+0.10 con n≥50 → candidato a live.
- **UP vs DOWN en #15min**: comprobar si BUY_NO tiene peor win rate que BUY_YES.

---

## Objetivo

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.
- **Fase actual**: shadow mode — predice y registra, sin dinero real.
- **Fase 2 (live)**: IC ≥ 0.10 con n ≥ 50 resoluciones en una estrategia.
- **Capital**: 30 € depósito → 20 € operativo + 10 € reserva.

---

## Arquitectura — dos loops en screen

```
screen -S fast  →  bash run_fast.sh    (~60s)
screen -S slow  →  bash run_slow.sh    (~23min)
```

### Loop FAST
```
fetch_binance_klines → shadow_predict → shadow_resolve
    → shadow_postmortem → shadow_resumen → git push
```

### Loop SLOW
```
capture_markets → capture_wallets → capture_trades
    → generate_report → arb_scanner → git push
```

**Scripts clave:**

| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min — Binance primario (col 7 = taker_buy_vol), Kraken fallback |
| `shadow_predict.py` | 6 estrategias → predictions CSV con columna `features` JSON |
| `shadow_resolve.py` | Resuelve, PNL Kelly, copia `features` a results.csv |
| `shadow_postmortem.py` | IC Bayesiano + Kelly + aprendizaje causal → strategy_params.json |
| `shadow_resumen.py` | estado_actual.md actualizado cada 60s |
| `arb_scanner.py` | Escanea ~2400 mercados → arb_scan_YYYY-MM-DD.csv |
| `generate_report.py` | Excel informe_bot.xlsx actualizado cada ~23min |

---

## Las 6 estrategias activas

### 1. WEEKLY_PRICE
Mercados "Will BTC be between $X-$Y?" — spot vs bracket → BUY_YES/BUY_NO.
Primera resolución: 24 Jun 16:00 UTC. Sin resoluciones aún.

### 2. PRICE_MOMENTUM
Tendencia exponencial del precio YES (últimas 6h). 0 señales antes del mediodía.

### 3. SMART_FLOW_1H
≥3 wallets humanas comprando el mismo lado, imbalance≥70%. Excluye mercados Up/Down.
n=12, IC=-0.171 (datos contaminados pre-fix). Acumulando datos limpios.

### 4. UPDOWN_GBM ← edge principal confirmado
Black-Scholes digital para mercados "X Up or Down". Daily/hourly/15min/5min.

**Filtros activos:**
- Opción A: `if ventana_min==5 and abs(pct_spot_vs_ref)>0.05% → return None`
- Filtros causales aprendidos (auto-actualizados en strategy_params.json):
  - BTC#5min: `sigma_h > 0.0018` → skip
  - ETH#5min: `|pct|>0.02%` + `sigma_h > 0.0024` → skip
  - SOL#5min: `|pct|>0.03%` + `sigma_h > 0.0018` → skip

**Features guardadas**: `{pct_spot_vs_ref, sigma_h, T_h}`

**Estado actual (13:30 UTC, 24 Jun):**
| Subtipo | n | Win% | IC | PNL | Kelly |
|---|---|---|---|---|---|
| #15min global | 23 | ~70% | +0.220 | **+6.43€** | **2.00€** |
| ETH#15min | 8 | 62% | +0.075 | +1.53€ | 0.75€ |
| SOL#15min | 5 | 60% | +0.018 | +1.32€ | 0.50€ |
| BTC#15min | 11 | 55% | +0.061 | +0.68€ | 0.61€ |

### 5. PRICE_TARGET_GBM
GBM para "Will BTC reach $70k?". Sin resoluciones (mercados multi-día).

### 6. ORDER_FLOW_5M ← sorpresa positiva del día
Cumulative delta Binance (taker_buy - taker_sell) últimas 5 velas.
Señal: `|delta_ratio| > 0.38` Y precio YES en 0.38-0.62.

**Estado actual:** n=84, 47W/37L (56%), IC=+0.058, PNL=**+7.78€**
Es la segunda estrategia mejor del sistema. Necesita n≥50 con IC≥0.10 para live.

---

## Sistema de aprendizaje causal

```
predictions (features JSON) → results (features copiadas)
    → postmortem: IC_bucket < -0.12, n≥8 → filtros_causales (skip)
                  IC_bucket > +0.12, n≥8 → patrones_ganadores (kelly_boost)
    → strategy_params.json → siguiente ciclo
```

**FEATURE_RULES actuales:**
- 5min y 15min: `pct_spot_vs_ref` (abs_gt/abs_lt) + `sigma_h` (gt/lt)
- ORDER_FLOW_5M: `delta_ratio` (abs_lt/abs_gt)

**Kelly dinámico:**
```
n≥5 y IC>0: apuesta = min(2€, max(0.50€, 20€ × IC × 0.5))
sino: apuesta = 0.50€
+ patrones_ganadores: apuesta += kelly_boost
```

---

## Estado actual (2026-06-24 13:30 UTC)

### Capital
| | |
|---|---|
| Bankroll actual | **9.95 €** |
| PNL acumulado | **-10.05 €** |
| Loops | fast ciclo ~383, slow ciclo ~35 |

### Desglose honesto del PNL

| Fuente | PNL | Estado |
|---|---|---|
| ORDER_FLOW_5M | **+7.78€** | ✅ IC positivo, acumulando |
| UPDOWN_GBM #15min | **+6.43€** | ✅ Edge confirmado |
| UPDOWN_GBM #60min/otros | +0.91€ | ✅ Positivo |
| UPDOWN_GBM #5min (pre-filtros) | -14.81€ | Filtros aplicados, ya no sangra |
| SMART_FLOW_1H (pre-fix slots) | -6.74€ | Bug corregido |
| UPDOWN_GBM #5min (post-filtros) | ~-4.62€ | Mejorando con filtros causales |

---

## ⚡ PRIORIDADES PARA PRÓXIMA SESIÓN

### PRIORIDAD 1 — Explorar dataset Jon-Becker (HACER PRIMERO)

**Repo**: `github.com/Jon-Becker/prediction-market-analysis` (3.6k stars, 497 forks)
**Dataset**: 36GB comprimido — trades históricos de Polymarket + Kalshi desde 2022+

**Por qué es crítico**: resuelve el mayor bloqueador de todo el sistema.
Con este dataset podemos:
- Backtestear ORDER_FLOW_5M con miles de slots históricos (tenemos solo 84)
- Backtestear la hipótesis de ventanas horarias con años de datos reales
- Construir dataset de entrenamiento para HMM, CNN, GP (requieren n≥5000)
- Analizar si existe cross-platform arb entre Polymarket y Kalshi históricamente

**Pasos**:
1. `git clone https://github.com/Jon-Becker/prediction-market-analysis`
2. Verificar qué contiene exactamente (¿trades o L2 orderbook?)
3. Si tiene datos de slots 5/15min → backtestear ORDER_FLOW_5M
4. Si tiene L2 depth → desbloquea OBI (Orderbook Imbalance)

---

### PRIORIDAD 2 — Evaluar candidatos a live

Con ORDER_FLOW_5M en IC=+0.058 (n=84) y #15min en IC=+0.220 (n=23):

**Umbral para live**: IC ≥ 0.10 con n ≥ 50

- `UPDOWN_GBM#15min`: IC=+0.220, n=23. **Faltan ~27 ops.** Con 3-4 ops/hora activa, en 1-2 días más.
- `ORDER_FLOW_5M`: IC=+0.058, n=84. Necesita subir IC. Vigilar si sigue mejorando.

**Cuando ambos superen el umbral**: decidir recapitalización y estrategia de entrada a live.

---

### PRIORIDAD 3 — Análisis de WEEKLY_PRICE (si ya resolvió)

Los mercados WEEKLY_PRICE del 24 Jun resolvieron a las 16:00 UTC.
Analizar: ¿qué predicciones teníamos? ¿cuántas acertamos? ¿cuál es el IC inicial?

```bash
python3 -c "
import csv
rows = [r for r in csv.DictReader(open('data/shadow/results.csv')) if r['strategy']=='WEEKLY_PRICE']
print(f'WEEKLY_PRICE: {len(rows)} resoluciones')
for r in rows: print(f'  {r[\"acierto\"]} | {r[\"pnl_neto\"]} | {r.get(\"question\",\"\")[:50]}')
"
```

---

### PRIORIDAD 4 — Verificaciones rápidas de hipótesis

**H3 BTC#5min momentum**: comprobar n actual y si pct WIN>LOSS sigue siendo opuesto a ETH/SOL.
**UP vs DOWN en #15min**: comprobar si BUY_NO tiene peor win rate.
**Ventanas horarias**: con más datos, re-ejecutar el análisis horario.

---

## Arbitraje — `arb_scanner.py`

Detecta BRACKET_ARB: mercados de precio-rango (mutuamente excluyentes) donde suma YES < 0.97.
Ejemplo real: "ETH price June 28" — 8 brackets, suma=0.926, profit potencial 5.4%.
**Riesgo**: precio fuera del rango cubierto → todos los brackets pierden.
Corre cada ~23min en slow loop. Guarda en `data/shadow/arb_scan_YYYY-MM-DD.csv`.

---

## Roadmap hacia autonomía

```
[✓] Aprende CUÁNTO pierde  — IC + Kelly por subtipo
[✓] Aprende POR QUÉ pierde — filtros_causales sobre features
[✓] Aprende POR QUÉ gana  — patrones_ganadores → kelly_boost
[✓] Escáner de arbitraje   — bracket arb cada ~23min
[ ] PRÓXIMO: Explorar dataset Jon-Becker → backtesting histórico
[ ] Verificar UP>DOWN en #15min
[ ] Slippage floor          — antes del primer trade real en live
[ ] Resolution Sniper / Expiry Fade — tras analizar WEEKLY_PRICE
[ ] OBI (Orderbook Imbalance) — si el dataset tiene L2 depth
[ ] Cross-Market Arb (Polymarket vs Kalshi) — con el dataset
[ ] LP Rewards (market making) — cuando estemos en live
[ ] Live trading           — IC ≥ 0.10, n ≥ 50, recapitalizar
```

---

## Investigación pendiente — por orden de impacto

### [PRÓXIMA SESIÓN] Dataset Jon-Becker
Ver PRIORIDAD 1 arriba. Desbloquea todo lo demás.

### [PENDIENTE — observar con más datos] Ventanas horarias de alta reversión
09:00-10:30 UTC mostró 25% win rate en primer día (n=4-8, insuficiente).
NYSE open (13:30-14:30 UTC) y close (20:30-21:30 UTC) sin datos propios aún.
Implementar skip cuando tengamos n≥15 por franja en 7+ días.
```python
# Propuesta: SKIP_HOURS_UTC = [(9,10), (13,14)] en shadow_predict.py
```

### [PENDIENTE — media prioridad] Kalman + HMM para sigma_h
Kalman: sigma_h como estado continuo que evoluciona suavemente.
HMM: regímenes discretos latentes (vol baja/normal/crisis) sin etiquetado manual.
Librería: `hmmlearn`. Emisión: sigma_h rolling, pct_spot_vs_ref, delta_ratio, hora UTC.
**Extensión**: samplear N valores de sigma_h → distribución de p_up → entropía = incertidumbre.
(Inspirado en PredACGAN, Kim & Lee 2023: Sharpe 0.236→1.054 filtrando por incertidumbre.)
Activar cuando n≥50 en #15min y modelo base validado.

### [PENDIENTE — media prioridad] Opción B — OU para slots 5min
Cuando n≥100 post-filtro A. Hipótesis: proceso mean-reverting, no GBM.
```python
theta = 2.0  # calibrar con MLE
p_up_mr = 0.5 - (spot/ref - 1) * theta * T_h
```

### [PENDIENTE] Kelly compuesto — convergencia ORDER_FLOW + UPDOWN_GBM
Si ambas coinciden en dirección → boost. Si divergen → skip.

### [PENDIENTE] Resolution Sniper / Expiry Fade
Última 1-2h antes de vencimiento: si modelo da p≥0.92 y mercado está en 0.80 → edge real.
Caso natural: WEEKLY_PRICE en la última hora. Analizar tras resolución de hoy.

### [PENDIENTE] OBI (Orderbook Imbalance)
Ratio bid/ask depth como señal. Necesita `best_bid_size` y `best_ask_size`.
Si dataset Jon-Becker tiene L2 → implementar inmediatamente.
Fórmula: `OBI = (V_bid - V_ask) / (V_bid + V_ask)` → `P_micro = P_mid + OBI × (spread/2)`

### [PENDIENTE — baja] SMART_FLOW_1H refinements
One-hit wonder filter (>30% PNL de un solo trade) + profit factor ≥1.5x.
Activar cuando SMART_FLOW_1H tenga n≥30 datos limpios y IC real confirmado.

### [PENDIENTE — baja] CNN sobre precio (Re-Imaging Price Trends)
Jiang, Kelly, Xiu 2020. Convertir series de precios YES en imágenes → CNN predice dirección.
Necesita n≥5000. El dataset Jon-Becker puede darnos ese histórico.

### [PENDIENTE — futuro] Métodos astro-statistics
GP (celerite2/tinygp) para sigma_h, Matched Filtering (LIGO) para ORDER_FLOW,
ZTF classification pipelines para filtros causales, Bayesian Blocks para detección régimen.
Activar cuando modelo base validado.

### [REFERENCIA] Agentic Design Patterns (Gulli/Google 2025)
Patrones útiles: Ch20 Prioritization + Ch21 Exploration/Discovery.
Leer antes de implementar el meta-learner LLM completo.

---

## Validación empírica externa

**"Five months building a Bitcoin 5-min trading bot"**: win_rate debe superar entry_price.
- 5min: win rate 31-45% vs ~49.5% necesario → pérdidas inevitables sin filtros
- 15min: win rate 55-70% vs ~52% necesario → edge real ✅
- Mean-reversion en 5min confirmada empíricamente. No hay señal predictiva en el momento de entrada.
- **"The edge lives in a less efficient market."** Nuestros 15min son ese mercado.

---

## Constantes importantes

### `shadow_predict.py`
```python
HORIZONTE_MIN_HORAS = 0.05
EDGE_MINIMO = 0.02
SLIPPAGE_ESTIMADO = 0.02
DELTA_MIN = 0.38   # ORDER_FLOW_5M (subido de 0.20)
LAG_MAX   = 0.12
```

### `shadow_postmortem.py`
```python
IC_FILTRO_MIN  = -0.12; IC_PATRON_MIN = +0.12; N_BUCKET_MIN = 8
UMBRAL_SUBIR_EDGE = (-0.10, 3); UMBRAL_SUBIR_MAS = (-0.20, 5); UMBRAL_DESACTIVAR = (-0.30, 8)
```

### `arb_scanner.py`
```python
UMBRAL_ARB = 0.97; LIQ_MIN = 200; N_MIN = 3; FEE_PAYOUT = 0.02
```

### `generate_report.py`
```python
DEPOSITO_TOTAL = 30.0; CAPITAL_OPERATIVO = 20.0; RESERVA = 10.0
```

---

## Ficheros clave (commitados en GitHub)
```
data/shadow/predictions_YYYY-MM-DD.csv  — columna 'features' JSON
data/shadow/results.csv                 — columna 'features' copiada
data/shadow/strategy_params.json        — IC, Kelly, filtros_causales, patrones_ganadores
data/shadow/estado_actual.md            — actualizado cada 60s
data/shadow/informe_bot.xlsx            — Excel, actualizado cada ~23min
data/shadow/arb_scan_YYYY-MM-DD.csv    — oportunidades de arbitraje
data/shadow/hipotesis_YYYY-MM-DD.md    — hipótesis con evidencia
data/prices/YYYY-MM-DD.csv             — spot cada ~60s
data/wallets/leaderboard_YYYY-MM-DD.csv
```

---

## Diagnósticos comunes

**PRICE_MOMENTUM 0 señales por la mañana**: normal, necesita drift ≥1.5% en 6h.
**SMART_FLOW_1H 0 señales al inicio**: trades se cargan ~15min después del slow loop.
**Conflictos git con el fast loop**: `git stash && git pull --rebase origin main && git stash pop && git push`.
**prices CSV en conflicto**: `git checkout --theirs data/prices/YYYY-MM-DD.csv`.

---

## Reiniciar loops si caen
```bash
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh
```
