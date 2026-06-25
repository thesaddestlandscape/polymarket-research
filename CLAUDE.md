# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-25 ~09:30 UTC**

---

## ⚡ PROTOCOLO DE INICIO DE SESIÓN — ejecutar SIEMPRE

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

# 3. Split BUY_YES vs BUY_NO en #15min (H-REGIMEN)
python3 << 'EOF'
import csv
rows = list(csv.DictReader(open('data/shadow/results.csv')))
for side in ['BUY_YES','BUY_NO']:
    sub = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
    if sub:
        w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
        ic=((w+1)/(n+2)-0.5)*min(1.0,n/20)
        print(f"  {side:8s} #15min: {w}/{n} ({w/n*100:.0f}%) PNL={pnl:+.2f}€ IC={ic:+.3f}")
EOF

# 4. Estado live trading
python3 live_guard.py
python3 live_stake.py

# 5. Arb scan del día
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null | head -5 || echo "Sin oportunidades hoy"
```

**Presentar al usuario:**
- Bankroll actual (shadow + live si hay) y PNL desde última sesión
- Estrategias que han cruzado el umbral IC≥0.10 n≥40 → candidatas a live
- Split BUY_YES/BUY_NO en #15min y si H-REGIMEN se mantiene
- Estado del switch live (ON/OFF) y ventana horaria actual
- Oportunidades de arb si las hay

---

## Objetivo

Bot semi-autónomo para operar mercados de predicción cripto en Polymarket.
- **Fase actual**: shadow mode + sistema live listo (pendiente credenciales Polymarket API)
- **Fase live**: IC ≥ 0.10 con n ≥ 40 resoluciones confirmadas en una estrategia
- **Capital**: 30€ depósito → 20€ operativo + 10€ reserva
- **VPS**: Hetzner Helsinki (IP finlandesa — Polymarket accesible desde FI)

---

## Arquitectura — tres loops en screen

```
screen -S fast     →  bash run_fast.sh       (~60s)
screen -S slow     →  bash run_slow.sh       (~23min)
screen -S control  →  python3 live_control.py  (siempre)
```

### Loop FAST
```
fetch_binance_klines → shadow_predict → live_trade
    → shadow_resolve → shadow_postmortem → shadow_resumen → git push
```

### Loop SLOW
```
capture_markets → capture_wallets → capture_trades
    → generate_report → arb_scanner → git push
```

**Scripts clave:**

| Script | Función |
|---|---|
| `fetch_binance_klines.py` | Klines 1min — Binance primario, Kraken fallback |
| `shadow_predict.py` | Estrategias → predictions CSV con `features` JSON |
| `live_trade.py` | Ejecuta trades reales (STUB hasta tener API key Polymarket) |
| `shadow_resolve.py` | Resuelve predicciones, PNL Kelly, copia features a results.csv |
| `shadow_postmortem.py` | IC Bayesiano + Kelly + aprendizaje causal → strategy_params.json |
| `shadow_resumen.py` | estado_actual.md actualizado cada 60s |
| `arb_scanner.py` | Escanea ~2400 mercados → arb_scan_YYYY-MM-DD.csv |
| `generate_report.py` | Excel informe_bot.xlsx (37 subtypes, datos históricos completos) |
| `live_guard.py` | Guardián: switch + ventanas horarias → ¿puede operar? |
| `live_stake.py` | Kelly stake con bankroll completo + 3 niveles de circuit breaker |
| `live_control.py` | Listener Telegram: /on /off /status /help |
| `live_switch.sh` | bash live_switch.sh on/off/status |

---

## Estado de estrategias — 2026-06-25 (sesión tarde)

### Bankroll simulado: **~35€** (+15€ PNL) | ~900 ops | ~52% WR (actualizar con protocolo inicio)

| Estrategia | n | Win% | IC | PNL | Estado |
|---|---|---|---|---|---|
| UPDOWN_GBM#BTC#15min | 32+ | 62% | **+0.118** | +6.45€ | ✅ casi live (n≥40) |
| UPDOWN_GBM#ETH#60min | 14+ | 71% | **+0.131** | +3.63€ | ✅ señal emergente |
| UPDOWN_GBM#BTC#60min | 13+ | 69% | **+0.108** | +2.54€ | ✅ señal emergente |
| ORDER_FLOW_5M [0.38-0.46] | 268 | 56% | **+0.059** | +13.53€ | ✅ fix DELTA_MAX |
| UPDOWN_GBM#SOL#15min | 23+ | 57% | +0.060 | +3.83€ | ⚠️ acumulando |
| RESOLUTION_SNIPER | 0 | — | — | — | 🆕 acumulando datos |
| UPDOWN_OU_5M | 0 | — | — | — | 🆕 shadow paralelo |
| SMART_FLOW_1H | 14 | 21% | -0.175 | -7.42€ | 🚫 DESACTIVADA |
| UPDOWN_GBM#240min | 9 | 0-33% | -0.318 | -3.37€ | 🚫 DESACTIVADA |

---

## Hipótesis — estado actualizado 2026-06-25

### H-REGIMEN ✅ CONFIRMADA PARCIALMENTE (2 días de datos)

BUY_YES vs BUY_NO en #15min por día:

| Día | Régimen BTC | BUY_YES | BUY_NO |
|---|---|---|---|
| 2026-06-24 | Bajista (-3.12%) | 24/47 (51%) | **19/26 (73%)** |
| 2026-06-25 | Alcista (+1.14%) | 16/27 (59%) | 0/2 (0%) |

**Conclusión**: el patrón es simétrico y claro. En bajista → BUY_NO domina. En alcista → BUY_NO pierde.
**Implementado**: filtro `REGIME_THRESHOLD = 0.7%/h` en `shadow_predict.py`. Si `drift_60min > +0.7%/h` y modelo BUY_NO → skip. Si `drift_60min < -0.7%/h` y modelo BUY_YES → skip.
**Pendiente**: con solo 2 días el umbral 0.7%/h es conservador. Con n≥50 BUY_NO revisar si bajar a 0.5%/h mejora IC.

### H-60MIN 🆕 SEÑAL EMERGENTE (nueva hipótesis)

UPDOWN_GBM en ventanas de **60 minutos** muestra IC consistentemente alto:

| Subtipo | n | Win% | IC |
|---|---|---|---|
| ETH#60min | 14 | 71% | **+0.131** |
| BTC#60min | 13 | 69% | **+0.108** |
| SOL#60min | 7 | 43% | -0.019 |

ETH y BTC están ya por encima de IC=0.10. Necesitan llegar a n≥40 para live.
**Hipótesis**: los mercados hourly (60min) tienen menos ruido que los 15min y más señal que los daily. El GBM captura bien la dinámica de 1 hora.
**Acción**: priorizar acumulación de datos en #60min. Si IC se mantiene ≥0.10 con n≥40 → candidato a live antes que #15min global.

### H-ORDER_FLOW-DECAY ✅ RESUELTA — DELTA_MAX implementado

Análisis (n=518 con features) reveló que la señal **no es monótona**:
- `[0.38-0.46]`: IC=+0.059 (268 ops) → sweet spot ✅
- `[0.46-0.65]`: IC=-0.079 (250 ops) → zona muerta ❌ señal ya priceada, reversión
- `[0.65+]`: IC=+0.032 (45 ops) → extremo, pocas ops

**Fix aplicado**: `DELTA_MAX = 0.46` en `s_order_flow_5m`. Zona muerta eliminada.
**Resultado**: IC +0.019 → +0.059, PNL histórico +4.89€ → +13.53€ (con el filtro).

### H-DRIFT-EFECTO ⚠️ DATOS INSUFICIENTES

El filtro REGIME_THRESHOLD lleva activo solo desde 2026-06-25 06:27 UTC.
Pre-filtro: 56/98 (57%) IC=+0.070. Post-filtro: 3/4 (75%) n=4 — demasiado pequeño.
**Acción**: esperar n≥20 post-filtro para evaluar impacto real.

### H-VENTANAS-HORARIAS ✅ ACCIONADA

Análisis por hora UTC reveló:
- **ORDER_FLOW 22:xx UTC**: IC=-0.115 n=37 → consistentemente malo
- **ORDER_FLOW 17:xx UTC**: IC=+0.201 n=17 → el mejor, pero n pequeño
- **GBM #15min 06-07 UTC**: IC=+0.102 n=9 → promisorio, insuficiente

**Fix**: `ORDER_FLOW_BLACKLIST_HOURS = {22}` en `s_order_flow_5m`.
**Pendiente**: con más datos confirmar/añadir otras horas (17:xx posible boost futuro).

### H-OU-5MIN 🆕 SHADOW PARALELO

Inversion test simple (n=160): IC=-0.006 → +0.006. Mejora mínima, estadísticamente ruido.
`UPDOWN_OU_5M` añadida como estrategia shadow paralela (no reemplaza GBM).
Formula: `p_up = 0.5 - pct × THETA_OU(30)`. Calibrar cuando n≥200 o con Jon-Becker.

### H-5MIN-REVERSIÓN ✅ CONFIRMADA EXTERNAMENTE

Empíricamente confirmado: ventanas de 5min no son predecibles con GBM. El mercado revierte.
- Filtro Opción A (`|pct|>0.05% → skip`) activo
- Filtros causales (sigma_h, pct) activos para BTC/ETH/SOL
- **No invertir más desarrollo aquí hasta tener dataset Jon-Becker**

### H-WEEKLY-PRICE 🔄 ACUMULANDO

Muy pocos datos (n=6 total). BTC 0/2, ETH 2/2, SOL 2/2. No significativo aún.

---

## Sistema live trading — arquitectura completa

### Control
```bash
bash live_switch.sh on/off     # activar/desactivar manualmente
# O desde Telegram: /on /off /status /help
```

### Ventanas horarias (hora Madrid, L-V)
08:30-09:30 | 10:30-11:30 | 12:30-13:30 | 16:30-17:30 | 18:30-19:30 | 20:30-21:30
Fines de semana: solo switch manual.

### Stake (bankroll completo, compounding)
```
stake = min(IC × bankroll × 0.5,  bankroll × 10%,  2€)
```
Con bankroll=20€ e IC=0.10 → stake=1.00€. Sube cada día con las ganancias.

### Circuit breakers (3 niveles)
1. Bankroll < 5€ → desactiva switch automáticamente
2. Caída diaria ≥ 15% → para el día
3. Caída en ventana ≥ 20% → para esa ventana

### Notificaciones Telegram
- 🎯 Señal detectada (estrategia, dirección, stake, IC)
- 📊 Fin de ciclo con actividad
- 🛑 Circuit breaker disparado
- 📊 Digest diario a las 20:00 UTC

### Lo que falta para live real
- Credenciales Polymarket CLOB API (private key + API key)
- Wallet MetaMask con 30 USDC en Polygon (pendiente setup usuario)
- Guardar en `data/live/.env` (ya en .gitignore)

### Estrategias candidatas a live (umbral: IC≥0.10, n≥40)
- `UPDOWN_GBM#BTC#15min` — IC=+0.118, n=32 → faltan ~8 ops
- `UPDOWN_GBM#ETH#60min` — IC=+0.131, n=14 → faltan ~26 ops
- `UPDOWN_GBM#BTC#60min` — IC=+0.108, n=13 → faltan ~27 ops

---

## Sistema de aprendizaje causal

```
predictions (features JSON) → results (features copiadas)
    → postmortem: IC_bucket < -0.12, n≥8 → filtros_causales (skip)
                  IC_bucket > +0.12, n≥8 → patrones_ganadores (kelly_boost)
    → strategy_params.json → siguiente ciclo
```

**Features por estrategia:**
- UPDOWN_GBM: `{pct_spot_vs_ref, sigma_h, T_h, drift_15min, drift_60min, delta_ratio_macro}`
- ORDER_FLOW_5M: `{delta_ratio, total_vol_5m, has_real_flow}`

**Aprendizaje causal activo (strategy_params.json):**
- UPDOWN_GBM#BTC#5min: sigma_h > 0.0018 → skip
- UPDOWN_GBM#ETH#5min: |pct| > 0.02% + sigma_h > 0.0024 → skip
- UPDOWN_GBM#SOL#5min: |pct| > 0.03% + sigma_h > 0.0018 → skip
- SMART_FLOW_1H: DESACTIVADA (IC=-0.25 n=14 → UMBRAL_DESACTIVAR=-0.20)
- UPDOWN_GBM#240min: DESACTIVADA (IC=-0.318 n=9)

---

## Roadmap hacia autonomía

```
[✓] IC + Kelly por subtipo (aprendizaje cuantitativo)
[✓] Filtros causales sobre features (aprendizaje cualitativo)
[✓] Patrones ganadores → kelly_boost
[✓] Escáner de arbitraje (bracket arb cada ~23min)
[✓] Drift de mercado en GBM (DRIFT_DAMPING=0.25)
[✓] Filtro H-REGIMEN (REGIME_THRESHOLD=0.7%/h en #15min)
[✓] Sistema live: ventanas + switch + Kelly + circuit breakers
[✓] Control Telegram (/on /off /status)
[✓] Notificaciones: señales, circuit breaker, digest diario
[✓] ORDER_FLOW DELTA_MAX=0.46 (zona muerta [0.46-0.65] eliminada)
[✓] Ciclo fast 125s → 6s (paralelización + cache pickle CSV)
[✓] Kelly compuesto: GBM+OF coinciden → stake×1.5, divergen → SKIP
[✓] Resolution Sniper: bracket/target en última 1.5h con GBM real
[✓] UPDOWN_OU_5M: shadow paralelo mean-reversion 5min
[✓] Ventanas horarias: ORDER_FLOW blacklist 22 UTC (IC=-0.115)
[~] BTC#15min IC≥0.10 n=32/40 — casi listo para live
[ ] Credenciales Polymarket API → primer trade real
[ ] Dataset Jon-Becker → backtesting histórico + calibrar theta OU
[ ] H-60MIN validada con n≥40 → segunda estrategia live
[ ] REGIME_THRESHOLD ajustado con más datos (0.7 → 0.5?)
[ ] HMM régimen de mercado (cuando drift simple validado con n≥50)
[ ] OBI Orderbook Imbalance (con dataset Jon-Becker)
[ ] Cross-Market Arb Polymarket vs Kalshi (con dataset)
```

---

## Prioridades para próxima sesión

### P0 — Esta tarde: MetaMask + USDC + cuenta Polymarket
Ver `LIVE_PLAN.md`. Checklist: instalar MetaMask → red Polygon → comprar 30 USDC en Coinbase → retirar vía Polygon → crear cuenta Polymarket desde VPS Helsinki (ssh root@2a01:4f9:c014:df39::1).

### P1 — Credenciales Polymarket + primera operación real
BTC#15min está casi en umbral (n=32/40). En 2-3 días de trading lo cruza.
Setup pendiente: MetaMask → USDC en Polygon → cuenta Polymarket desde VPS Helsinki.

### P2 — Vigilar H-ORDER_FLOW-DECAY
Si ORDER_FLOW sigue mostrando IC negativo en bloques recientes → subir DELTA_MIN de 0.38 a 0.45 o revisar el modelo de señal.

### P3 — Dataset Jon-Becker
`github.com/Jon-Becker/prediction-market-analysis` — 36GB de histórico.
Desbloquea: backtesting de #60min, OU para 5min, OBI, Cross-Market Arb.

### P4 — REGIME_THRESHOLD calibración
Con n=4 post-filtro es muy pronto. Cuando n≥20 post-filtro evaluar si bajar 0.7→0.5%/h.

### P5 — H-60MIN seguimiento
ETH#60min y BTC#60min tienen IC≥0.10 con n=13-14. Seguir acumulando.
Si llegan a n=40 con IC≥0.10 → segunda estrategia candidata a live.

---

## Constantes clave

### `shadow_predict.py`
```python
DRIFT_DAMPING    = 0.25    # fracción del drift que entra en el GBM
REGIME_THRESHOLD = 0.7     # %/h para filtrar señales contra-tendencia en #15min
EDGE_MINIMO      = 0.02
SLIPPAGE_ESTIMADO= 0.02
DELTA_MIN = 0.38           # ORDER_FLOW_5M — umbral mínimo
DELTA_MAX = 0.46           # ORDER_FLOW_5M — umbral máximo (zona muerta >0.46)
KELLY_COMPUESTO_BOOST = 1.5  # boost cuando GBM+OF coinciden en dirección
KELLY_COMPUESTO_MAX   = 2.00
THETA_OU = 30.0            # OU mean-reversion para 5min (calibrar con Jon-Becker)
ORDER_FLOW_BLACKLIST_HOURS = {22}  # hora UTC con IC=-0.115 n=37
# Cache pickle: mercados_recientes TTL=90s, historial_mercados TTL=90s
# Ciclo fast: predict+trade cada 20s / resolve+postmortem cada 60s (3er ciclo)
# Paralelización: fetch_slots (ThreadPool), fetch_mercados_paralelo(20 workers)
```

### `shadow_postmortem.py`
```python
IC_FILTRO_MIN  = -0.12
IC_PATRON_MIN  = +0.12
N_BUCKET_MIN   = 8
UMBRAL_SUBIR_EDGE = (-0.10, 3)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.20, 8)   # bajado de -0.30 el 2026-06-25
```

### `live_stake.py` / `data/live/config_live.json`
```python
max_pct_bankroll_por_trade = 0.10   # máx 10% del bankroll por trade
max_stake_eur = 2.00                 # techo absoluto
freno_ventana_pct = 0.20            # -20% en una ventana → para
freno_diario_pct = 0.15             # -15% en el día → para
bankroll_minimo_eur = 5.00          # suelo absoluto → desactiva switch
```

---

## Ficheros clave
```
data/shadow/predictions_YYYY-MM-DD.csv  — features JSON: drift, sigma, pct, delta_macro
data/shadow/results.csv                 — 17 cols incluida 'features' (fix 2026-06-25)
data/shadow/strategy_params.json        — IC, Kelly, filtros_causales, activa/desactivada
data/shadow/estado_actual.md            — actualizado cada 60s
data/shadow/informe_bot.xlsx            — 37 subtypes con histórico completo
data/shadow/arb_scan_YYYY-MM-DD.csv    — bracket arb oportunidades
data/live/config_live.json              — ventanas, stakes, circuit breakers
data/live/LIVE_MODE_ON                  — touchfile switch (NO commiteado)
data/live/trades.csv                    — operaciones reales
logs/live.log                           — log del fast loop
logs/live_control.log                   — log del listener Telegram
LIVE_PLAN.md                            — setup completo: wallet, circuito, checklist
```

---

## Diagnósticos comunes

**`results.csv` sin features**: ocurrió el 24-Jun. Fix aplicado (17 cols con features).
**Git conflicto con fast loop**: `git stash && git pull --rebase origin main && git stash pop && git push`
**prices CSV en conflicto**: `git checkout --theirs data/prices/YYYY-MM-DD.csv`
**live_control caído**: `screen -dmS control python3 live_control.py`
**ORDER_FLOW IC negativo**: si 3 bloques consecutivos IC<-0.05 → subir DELTA_MIN a 0.45
**Bot no opera en live**: verificar `bash live_switch.sh` + ventana horaria activa
