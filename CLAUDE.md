# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-24 ~16:00 UTC**

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

# 3. Split BUY_YES vs BUY_NO en #15min (hipótesis H-BUYNO)
python3 << 'EOF'
import csv
rows = list(csv.DictReader(open('data/shadow/results.csv')))
for side in ['BUY_YES','BUY_NO']:
    sub = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
    if sub:
        w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
        print(f"  {side:8s} #15min: {w}/{n} ({w/n*100:.0f}%) PNL={pnl:+.2f}€")
EOF

# 4. Arb scan del día
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null | head -5 || echo "Sin oportunidades hoy"
```

**Presentar al usuario:**
- Bankroll actual y PNL desde última sesión
- Nuevas resoluciones y su impacto por estrategia
- Split BUY_YES vs BUY_NO en #15min y si el patrón H-BUYNO persiste o se invirtió
- Que las nuevas features (drift_15min, drift_60min, delta_ratio_macro) están presentes en predicciones recientes
- Oportunidades de arb detectadas si las hay

**Seguimiento obligatorio — hipótesis bajo vigilancia:**
- **H-BUYNO #15min**: BUY_NO tiene 100% win rate hoy (n=11) pero es día bajista (-3.12% BTC). ¿Se invierte en días alcistas? Reportar split BUY_YES/BUY_NO actualizado.
- **H-REGIMEN**: el mercado tuvo 70% de slots NO en #15min hoy. ¿El drift_60min en el GBM mejora la calibración? Comparar p_up pre y post-cambio cuando haya datos.
- **H3 BTC#5min momentum**: features ahora se guardan. Verificar cuando n≥10 con features.
- **ORDER_FLOW_5M**: IC=+0.063 (n=124). El bloque #94-124 bajó del pico 71% al 58%. ¿Tendencia o ruido?

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
Primera resolución: 24 Jun 16:00 UTC. 1 resolución con acierto, PNL=+0.13€ (ETH bracket correcto).

### 2. PRICE_MOMENTUM
Tendencia exponencial del precio YES (últimas 6h). 0 señales antes del mediodía.

### 3. SMART_FLOW_1H
≥3 wallets humanas comprando el mismo lado, imbalance≥70%. Excluye mercados Up/Down.
n=13, IC=-0.195. **Candidata a desactivar** — supera umbral de desactivación (-0.30, n=8) pero el postmortem no la ha desactivado aún. Revisar.

### 4. UPDOWN_GBM ← edge principal confirmado
Black-Scholes digital para mercados "X Up or Down". Daily/hourly/15min/5min.

**Cambio clave sesión 2026-06-24 tarde**: el modelo ahora incorpora drift de mercado.
```
d2 = (log(spot/ref) + mu_h × T_h) / (sigma_h × sqrt(T_h))
mu_h = drift_60min_por_hora × DRIFT_DAMPING(0.25)
```
Con BTC bajando -0.82%/h, `mu_h = -0.00206/h` → reduce p_up ~5-15pp en señales marginales.

**Filtros activos:**
- Opción A: `if ventana_min==5 and abs(pct_spot_vs_ref)>0.05% → return None`
- Filtros causales aprendidos (auto-actualizados en strategy_params.json):
  - BTC#5min: `sigma_h > 0.0018` → skip
  - ETH#5min: `|pct|>0.02%` + `sigma_h > 0.0024` → skip
  - SOL#5min: `|pct|>0.03%` + `sigma_h > 0.0018` → skip

**Features guardadas (actualizadas)**: `{pct_spot_vs_ref, sigma_h, T_h, drift_15min, drift_60min, delta_ratio_macro}`

**Estado actual (16:00 UTC, 24 Jun):**
| Subtipo | n | Win% | IC | PNL |
|---|---|---|---|---|
| #15min global | 33 | 63% | +0.220 | **+9.92€** |
| BTC#15min | 13 | 54% | +0.022 | +2.51€ |
| ETH#15min | 10 | 60% | +0.075 | +3.37€ |
| SOL#15min | 7 | 71% | +0.058 | +3.09€ |
| #5min global | ~45 | ~33% | ~-0.11 | ~-14.81€ |

**ATENCIÓN**: en sesión 2026-06-24 tarde se descubrió que el 63% de #15min está sesgado por un día bajista (70% slots NO). BUY_NO fue 11/11 hoy. Verificar en días futuros si el patrón es simétrico o hay edge estructural.

### 5. PRICE_TARGET_GBM
GBM para "Will BTC reach $70k?". Sin resoluciones (mercados multi-día).

### 6. ORDER_FLOW_5M
Cumulative delta Binance (taker_buy - taker_sell) últimas 5 velas.
Señal: `|delta_ratio| > 0.38` Y precio YES en 0.38-0.62.

**Estado actual:** n=124, 70W/54L (56%), IC=+0.063, PNL=**+12.75€**
Evolución: #1-31 (39%) → #32-62 (58%) → #63-93 (71% pico) → #94-124 (58%).
BUY_NO domina: 59/92 (64%) vs BUY_YES 11/33 (33%). Misma explicación que #15min: día bajista.

---

## Sistema de aprendizaje causal

```
predictions (features JSON) → results (features copiadas)
    → postmortem: IC_bucket < -0.12, n≥8 → filtros_causales (skip)
                  IC_bucket > +0.12, n≥8 → patrones_ganadores (kelly_boost)
    → strategy_params.json → siguiente ciclo
```

**FEATURE_RULES actuales (actualizado 2026-06-24):**
- 5min y 15min: `pct_spot_vs_ref` + `sigma_h` + `drift_60min` + `delta_ratio_macro`
- ORDER_FLOW_5M: `delta_ratio`

**Kelly dinámico:**
```
n≥5 y IC>0: apuesta = min(2€, max(0.50€, 20€ × IC × 0.5))
sino: apuesta = 0.50€
+ patrones_ganadores: apuesta += kelly_boost
```

---

## Estado actual (2026-06-24 ~16:00 UTC)

### Capital
| | |
|---|---|
| Bankroll simulado real | **~16.06€** (varía cada ciclo) |
| PNL acumulado | **~-3.94€** |
| Nota | `estado_actual.md` muestra menos porque no contabiliza ORDER_FLOW_5M — bug en shadow_resumen.py |

### Desglose honesto del PNL

| Fuente | PNL | Estado |
|---|---|---|
| ORDER_FLOW_5M | **+12.75€** | ✅ IC positivo, creciendo |
| UPDOWN_GBM #15min | **+9.92€** | ✅ Edge confirmado (verificar en días alcistas) |
| UPDOWN_GBM #60min/otros | +0.91€ | ✅ Positivo |
| UPDOWN_GBM #5min (todos) | ~-14.81€ | Filtros aplicados, mejorando |
| SMART_FLOW_1H | **-7.66€** | ⚠️ IC=-0.195, candidata a desactivar |

---

## ⚡ PRIORIDADES PARA PRÓXIMA SESIÓN

### PRIORIDAD 1 — Verificar efecto del drift en el modelo

Desde el ciclo 456+ las predicciones UPDOWN_GBM incluyen `drift_15min`, `drift_60min`, `delta_ratio_macro` en features. Comprobar:

```bash
python3 << 'EOF'
import csv, json
rows = list(csv.DictReader(open('data/shadow/predictions_2026-06-24.csv')))
gbm = [r for r in rows if r['strategy']=='UPDOWN_GBM' and r.get('features','') not in ('','{}')]
print(f"UPDOWN_GBM con nuevas features: {len(gbm)}")
if gbm:
    f = json.loads(gbm[-1]['features'])
    print(f"Últimas features: {f}")
    tiene_drift = sum(1 for r in gbm if 'drift_60min' in (r.get('features') or ''))
    print(f"Con drift_60min: {tiene_drift}")
EOF
```

También: ¿el drift está cambiando decisiones BUY_YES → BUY_NO en señales marginales?

### PRIORIDAD 2 — Hipótesis H-BUYNO con más días

¿El 11/11 BUY_NO de hoy es artefacto del día bajista o hay edge estructural?
Analizar split BUY_YES/BUY_NO en días anteriores (si hay datos) y en los próximos días.

```bash
python3 << 'EOF'
import csv
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
by_day_side = defaultdict(lambda: {'n':0,'w':0})
for r in rows:
    if r.get('subtype','').endswith('15min') and r['strategy']=='UPDOWN_GBM':
        dia = r.get('resolution_timestamp','')[:10]
        side = r.get('decision','')
        key = (dia, side)
        by_day_side[key]['n']+=1; by_day_side[key]['w']+=int(r['acierto'])
for (dia,side),d in sorted(by_day_side.items()):
    n=d['n']; w=d['w']
    if n: print(f"  {dia} {side:8s}: {w}/{n} ({w/n*100:.0f}%)")
EOF
```

### PRIORIDAD 3 — SMART_FLOW_1H: desactivar o no

IC=-0.195, n=13. El postmortem tiene umbral de desactivación en (-0.30, n=8) — ¿por qué no la desactivó? Revisar strategy_params.json.

### PRIORIDAD 4 — Dataset Jon-Becker

**Repo**: `github.com/Jon-Becker/prediction-market-analysis` (3.6k stars, 497 forks)
**Dataset**: 36GB comprimido — trades históricos de Polymarket + Kalshi desde 2022+
Desbloquea backtesting de todo el sistema con miles de slots históricos.

### PRIORIDAD 5 — WEEKLY_PRICE análisis completo

Resolver a las 16:00 UTC hoy. Analizar IC inicial.

---

## Arbitraje — `arb_scanner.py`

Detecta BRACKET_ARB: mercados de precio-rango (mutuamente excluyentes) donde suma YES < 0.97.
Hoy solo detectó OVERROUNDs (suma > 1.0, desfavorables). Sin oportunidades reales.
**Riesgo**: precio fuera del rango cubierto → todos los brackets pierden.
Corre cada ~23min en slow loop. Guarda en `data/shadow/arb_scan_YYYY-MM-DD.csv`.

---

## Roadmap hacia autonomía

```
[✓] Aprende CUÁNTO pierde  — IC + Kelly por subtipo
[✓] Aprende POR QUÉ pierde — filtros_causales sobre features
[✓] Aprende POR QUÉ gana  — patrones_ganadores → kelly_boost
[✓] Escáner de arbitraje   — bracket arb cada ~23min
[✓] Drift de mercado en GBM — mu_h = drift_60min × DRIFT_DAMPING (2026-06-24)
[ ] PRÓXIMO: Verificar efecto drift + hipótesis H-BUYNO con más días
[ ] Dataset Jon-Becker → backtesting histórico
[ ] Slippage floor          — antes del primer trade real en live
[ ] Resolution Sniper / Expiry Fade — tras analizar WEEKLY_PRICE
[ ] OBI (Orderbook Imbalance) — si el dataset tiene L2 depth
[ ] HMM para régimen de mercado — tras validar drift simple
[ ] Cross-Market Arb (Polymarket vs Kalshi) — con el dataset
[ ] LP Rewards (market making) — cuando estemos en live
[ ] Live trading           — IC ≥ 0.10, n ≥ 50, recapitalizar
```

---

## Investigación pendiente — por orden de impacto

### [PRÓXIMA SESIÓN] Verificar drift + H-BUYNO
Ver PRIORIDADES 1 y 2 arriba.

### [PRÓXIMA SESIÓN] Dataset Jon-Becker
Ver PRIORIDAD 4. Desbloquea todo lo demás.

### [PENDIENTE — media prioridad] Kalman + HMM para régimen de mercado
El drift simple (implementado hoy) es la versión básica. HMM detectaría regímenes latentes
(vol baja/normal/crisis) sin etiquetado manual.
Librería: `hmmlearn`. Emisión: sigma_h, drift_15min, delta_ratio_macro, hora UTC.
Activar cuando n≥50 en #15min y el drift simple validado.

### [PENDIENTE — observar con más datos] Ventanas horarias de alta reversión
09:00-10:30 UTC mostró 25% win rate en primer día (n=4-8, insuficiente).
NYSE open (13:30-14:30 UTC) y close (20:30-21:30 UTC) sin datos propios aún.

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

### [PENDIENTE] OBI (Orderbook Imbalance)
Ratio bid/ask depth como señal. Necesita `best_bid_size` y `best_ask_size`.
Si dataset Jon-Becker tiene L2 → implementar inmediatamente.

### [PENDIENTE — baja] SMART_FLOW_1H refinements
One-hit wonder filter + profit factor ≥1.5x. Cuando n≥30 datos limpios.

### [PENDIENTE — baja] CNN sobre precio (Re-Imaging Price Trends)
Necesita n≥5000. El dataset Jon-Becker puede darnos ese histórico.

### [PENDIENTE — futuro] Métodos astro-statistics
GP (celerite2/tinygp), Matched Filtering (LIGO), Bayesian Blocks.
Activar cuando modelo base validado.

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
DELTA_MIN = 0.38       # ORDER_FLOW_5M (subido de 0.20)
LAG_MAX   = 0.12
DRIFT_DAMPING = 0.25   # fracción del drift observado que entra en el GBM (añadido 2026-06-24)
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
data/shadow/predictions_YYYY-MM-DD.csv  — columna 'features' JSON (ahora incluye drift y delta_macro)
data/shadow/results.csv                 — columna 'features' copiada
data/shadow/strategy_params.json        — IC, Kelly, filtros_causales, patrones_ganadores
data/shadow/estado_actual.md            — actualizado cada 60s (OJO: no incluye ORDER_FLOW en bankroll)
data/shadow/informe_bot.xlsx            — Excel, actualizado cada ~23min
data/shadow/arb_scan_YYYY-MM-DD.csv    — oportunidades de arbitraje
data/shadow/sesion_YYYY-MM-DD-*.md     — recaps de sesiones anteriores
data/prices/YYYY-MM-DD.csv             — spot cada ~60s (fuente de drift_Nmin)
data/wallets/leaderboard_YYYY-MM-DD.csv
```

---

## Diagnósticos comunes

**PRICE_MOMENTUM 0 señales por la mañana**: normal, necesita drift ≥1.5% en 6h.
**SMART_FLOW_1H 0 señales al inicio**: trades se cargan ~15min después del slow loop.
**estado_actual.md muestra bankroll bajo**: no contabiliza ORDER_FLOW_5M — usar script Python del protocolo de inicio.
**features vacías en predictions antiguas**: bug preexistente resuelto con `_normalizar_pred()` en resolve y postmortem.
**Conflictos git con el fast loop**: `git stash && git pull --rebase origin main && git stash pop && git push`.
**prices CSV en conflicto**: `git checkout --theirs data/prices/YYYY-MM-DD.csv`.

---

## Reiniciar loops si caen
```bash
screen -dmS fast bash /root/polymarket-research/run_fast.sh
screen -dmS slow bash /root/polymarket-research/run_slow.sh
```
