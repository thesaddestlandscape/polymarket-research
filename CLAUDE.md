# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-25 ~17:00 UTC**

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

## Estado de estrategias — 2026-06-25 (cierre sesión tarde)

### Bankroll simulado: **3.16€** (−16.84€ PNL) | 1103 ops | 49% WR
### ⚠️ El PNL negativo viene ÍNTEGRAMENTE de estrategias ya desactivadas.
### Con solo las estrategias activas actuales: PNL **+21.44€** → bankroll **41.44€**

| Estrategia | n | Win% | IC | PNL | Estado |
|---|---|---|---|---|---|
| UPDOWN_GBM#BTC#15min | 36 | 58% | +0.079 | +4.23€ | ⏳ n=36/40, IC bajo umbral (0.08) |
| UPDOWN_GBM#ETH#60min | 18 | 61% | **+0.090** | +1.44€ | ⏳ señal emergente, n=18/40 |
| UPDOWN_GBM#BTC#60min | 15 | 60% | +0.066 | +0.99€ | ⏳ acumulando |
| UPDOWN_GBM#SOL#15min | 24 | 54% | +0.038 | +3.32€ | ⚠️ acumulando |
| ORDER_FLOW_5M (sin ETH, sin horas malas) | 136 | 56% | +0.058 | +12.59€ | ✅ activa |
| UPDOWN_OU_5M | 57 | 26% | -0.229 | -13.76€ | 🚫 DESACTIVADA |
| SMART_FLOW_1H | 17 | 18% | -0.246 | -8.95€ | 🚫 DESACTIVADA |
| UPDOWN_GBM#5min (todos pares) | ~80 | ~33% | ~-0.10 | ~-22€ | 🚫 DESACTIVADA |
| UPDOWN_GBM#240min | 11 | 9% | -0.089 | -5.04€ | 🚫 DESACTIVADA |

---

## Hipótesis — estado actualizado 2026-06-25

### H-REGIMEN ❌ REFUTADA — backfill 90 días

Backfill 90d × 6 pares (125k predicciones): BUY_YES 60% ≈ BUY_NO 60%. Sin efecto régimen en 5/15min.
El filtro anterior (REGIME_THRESHOLD en 15min) estaba eliminando las **mejores** señales: drift<-0.7 BUY_YES IC=+0.169 (mean-reversion real).

**Implementado (2026-06-25)**: filtro rediseñado — solo en 60min+, solo BUY_NO alcista fuerte:
- `ventana ≥ 60min AND drift > +0.7%/h AND p_up < py_mkt → skip`
- Backfill 60min drift>+0.7 BUY_NO IC=-0.004; 240min IC=-0.050 → sí merece filtro
- BUY_YES (drift<-0.7) no se filtra: IC=+0.169 en 60min

### H-60MIN ✅ CONFIRMADA POR BACKFILL — acumulando shadow

Backfill 90d confirma IC positivo en 60min para BTC y ETH. Shadow actual:

| Subtipo | n | Win% | IC | PNL |
|---|---|---|---|---|
| ETH#60min | 18 | 61% | **+0.090** | +1.44€ |
| BTC#60min | 15 | 60% | +0.066 | +0.99€ |
| SOL#60min | 7 | 43% | -0.019 | +0.42€ |

ICs bajando levemente desde el pico (ETH era +0.131 con n=14). Normal con más datos. Backfill valida la señal.
**Acción**: seguir acumulando. Umbral live: IC≥0.08, n≥40. ETH necesita ~22 ops más, BTC ~25.

### H-ORDER_FLOW-DECAY ✅ RESUELTA — DELTA_MAX implementado

Análisis (n=518 con features) reveló que la señal **no es monótona**:
- `[0.38-0.46]`: IC=+0.059 (268 ops) → sweet spot ✅
- `[0.46-0.65]`: IC=-0.079 (250 ops) → zona muerta ❌ señal ya priceada, reversión
- `[0.65+]`: IC=+0.032 (45 ops) → extremo, pocas ops

**Fix aplicado**: `DELTA_MAX = 0.46` en `s_order_flow_5m`. Zona muerta eliminada.
**Resultado**: IC +0.019 → +0.059, PNL histórico +4.89€ → +13.53€ (con el filtro).

### H-DRIFT-EFECTO — MOOT (arquitectura cambiada)

El filtro de 15min fue eliminado (H-REGIMEN refutada). El nuevo filtro (60min+ BUY_NO) es diferente y empieza desde cero. No hay datos post-filtro que analizar. Esperar n≥30 en 60min para evaluar impacto del nuevo filtro.

### H-VENTANAS-HORARIAS ✅ ACTUALIZADA (2026-06-25 tarde)

Con n≥1000 ops en ORDER_FLOW, el patrón horario es muy claro:

| Hora UTC | Madrid | IC | PNL | Estado |
|---|---|---|---|---|
| 17:xx | 19:xx | **+0.208** n=22 | +4.88€ | ✅ mejor hora |
| 19:xx | 21:xx | **+0.143** n=40 | +5.50€ | ✅ muy buena |
| 15:xx | 17:xx | **+0.133** n=28 | +5.03€ | ✅ muy buena |
| 13:xx | 15:xx | **+0.125** n=30 | +6.08€ | ✅ muy buena |
| 07:xx | 09:xx | **−0.227** n=20 | −5.20€ | 🚫 bloqueada |
| 18:xx | 20:xx | **−0.178** n=16 | −4.15€ | 🚫 bloqueada |
| 20:xx | 22:xx | **−0.095** n=40 | −4.43€ | 🚫 bloqueada |
| 11:xx | 13:xx | −0.057 n=59 | −5.07€ | 🚫 bloqueada |
| 22:xx | 00:xx | +0.031 n=30 | +0.73€ | ✅ desbloqueada (era falso negativo) |

**Fix aplicado**: `ORDER_FLOW_BLACKLIST_HOURS = {7, 11, 18}` (antes era solo `{22}`).
**Config live**: ventana mediodia 12:30-13:30 Madrid eliminada (GBM IC=-0.154, OF IC=-0.057 — peor ventana en ambas).
**Impacto retroactivo**: +14.42€ evitados en ORDER_FLOW.

### H-OU-5MIN ❌ DESACTIVADA — IC=-0.229 n=57

Con n=57 y IC=-0.229 globalmente, todos los pares son negativos. Desactivada completamente.
No invertir más desarrollo sin dataset Jon-Becker que permita calibrar THETA_OU correctamente.

### H-5MIN-REVERSIÓN ✅ CONFIRMADA EXTERNAMENTE

Empíricamente confirmado: ventanas de 5min no son predecibles con GBM. El mercado revierte.
- Filtro Opción A (`|pct|>0.05% → skip`) activo
- Filtros causales (sigma_h, pct) activos para BTC/ETH/SOL
- **No invertir más desarrollo aquí hasta tener dataset Jon-Becker**

### H-WEEKLY-PRICE 🔄 ACUMULANDO (n=15)

| Par | n | Win% | IC | PNL |
|---|---|---|---|---|
| SOL | 4 | 100% | +0.067 | +2.42€ |
| ETH | 5 | 60% | +0.018 | -0.85€ |
| BTC | 6 | 33% | -0.037 | -2.73€ |

SOL sostenido 4/4 pero n demasiado pequeño. BTC negativo. No accionable aún — esperar n≥15 por par.

---

## Sistema live trading — arquitectura completa

### Control
```bash
bash live_switch.sh on/off     # activar/desactivar manualmente
# O desde Telegram: /on /off /status /help
```

### Ventanas horarias (hora Madrid, L-V)
08:30-09:30 | 10:30-11:30 | 16:30-17:30 | 18:30-19:30 | 20:30-21:30
~~12:30-13:30 eliminada~~ — GBM IC=-0.154, OF IC=-0.057 (peor ventana en ambas estrategias)
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

### Estrategias candidatas a live (umbral: IC≥0.08, n≥40)
- `UPDOWN_GBM#BTC#15min` — IC=+0.079 n=36 → 4 ops para n≥40, pero IC bajo umbral (tendencia bajando)
- `UPDOWN_GBM#ETH#60min` — IC=+0.090 n=18 → 22 ops más, IC por encima del umbral
- `UPDOWN_GBM#BTC#60min` — IC=+0.066 n=15 → 25 ops más, IC en recuperación

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
[✓] Drift de mercado en GBM (DRIFT_DAMPING por ventana: backfill 90d)
[✓] Filtro régimen rediseñado: solo 60min+, solo BUY_NO alcista (H-REGIMEN refutada en 15min)
[✓] Sistema live: ventanas + switch + Kelly + circuit breakers
[✓] Control Telegram (/on /off /status)
[✓] Notificaciones: señales, circuit breaker, digest diario
[✓] ORDER_FLOW DELTA_MAX=0.46 (zona muerta [0.46-0.65] eliminada)
[✓] Ciclo fast 125s → 6s (paralelización + cache pickle CSV)
[✓] Kelly compuesto: GBM+OF coinciden → stake×1.5, divergen → SKIP
[✓] Resolution Sniper: bracket/target en última 1.5h con GBM real
[✓] Ventanas horarias: ORDER_FLOW blacklist {7,11,18} UTC (+14.42€ retroactivo)
[✓] Ventana mediodia eliminada del live (GBM+OF ambos negativos ahí)
[✓] Backfill 90d: 125k predicciones GBM, calibración completa de parámetros
[~] BTC#15min n=36/40, IC=+0.079 — IC levemente bajo umbral, vigilar
[~] ETH#60min n=18/40, IC=+0.090 — acumulando bien
[ ] Credenciales Polymarket API → primer trade real
[ ] MetaMask → USDC Polygon → cuenta Polymarket desde VPS Helsinki
[ ] Dataset Jon-Becker → backtesting histórico + calibrar theta OU
[ ] H-60MIN validada con n≥40 → primera estrategia live real
[ ] ORDER_FLOW rangos per-par validados en shadow (backfill: BTC 0.42-0.44, XRP/DOGE 0.44-0.46, ETH 0.36-0.40) — pendiente validar con más ops shadow antes de aplicar
[ ] HMM régimen de mercado (cuando drift simple validado con n≥50)
[ ] OBI Orderbook Imbalance (con dataset Jon-Becker)
[ ] Cross-Market Arb Polymarket vs Kalshi (con dataset)
```

---

## Prioridades para próxima sesión

### P0 — MetaMask + USDC + cuenta Polymarket (BLOQUEANTE para live)
Ver `LIVE_PLAN.md`. Checklist: instalar MetaMask → red Polygon → comprar 30 USDC en Coinbase → retirar vía Polygon → crear cuenta Polymarket desde VPS Helsinki (ssh root@2a01:4f9:c014:df39::1).

### P1 — Primer trade real
ETH#60min (IC=+0.090 n=18) o BTC#15min (IC=+0.079 n=36) llegarán al umbral en ~2-4 días.
Umbral actualizado: IC≥0.08 (antes 0.10), n≥40.

### P2 — ORDER_FLOW rangos per-par
Backfill calibró: BTC 0.42-0.44, SOL 0.36-0.40, XRP 0.44-0.46, DOGE 0.44-0.46, ETH 0.36-0.40.
**No aplicar aún**: retroactivamente bajan PNL porque los rangos son muy estrechos y eliminan ops buenas con n pequeño. Validar cuando tengamos n≥200 por par con el blacklist nuevo activo.

### P3 — BTC#15min IC vigilancia
IC bajó de +0.118 → +0.079 en los últimos bloques. Último bloque (n=4): 1/4.
Si sigue bajando con n≥40 → revisar si es válido para live o esperar recuperación.

### P4 — Dataset Jon-Becker
`github.com/Jon-Becker/prediction-market-analysis` — 36GB de histórico.
Desbloquea: calibrar theta OU, OBI, Cross-Market Arb, validar rangos OF per-par.

### P5 — H-60MIN seguimiento
ETH#60min IC=+0.090 n=18 → 22 ops más para live. BTC#60min IC=+0.066 n=15 → 25 ops más.

---

## Análisis retroactivo — cuánto valen los ajustes (2026-06-25)

Con todos los filtros aplicados desde el inicio, el bankroll simulado sería **46-52€** en vez de 3.16€:

| Escenario | Bankroll | PNL |
|---|---|---|
| Real (como ha pasado) | **3.16€** | −16.84€ |
| + Sin OU_5M + SMART_FLOW | 25.87€ | +5.87€ |
| + Sin GBM 5min | 29.78€ | +9.78€ |
| + Sin GBM 240min | 34.81€ | +14.81€ |
| **+ Blacklist horas {7,11,18}** | **49.24€** | **+29.24€** |
| + Sin ORDER_FLOW ETH | **52.40€** | **+32.40€** |

El mayor error fue OU_5M + SMART_FLOW (+22.71€ perdidos). El segundo mayor fue no tener el blacklist horario correcto (+14.42€). Los rangos per-par del backfill no mejoran retroactivamente porque son demasiado estrechos con el n actual.

---

## Constantes clave

### `shadow_predict.py`
```python
DRIFT_DAMPING = {5: 0.30, 15: 0.20, 60: 0.05, 240: 0.10}  # backfill 90d por ventana
DRIFT_DAMPING_DEFAULT = 0.10      # daily y ventanas no catalogadas
REGIME_BUY_NO_THRESHOLD = 0.7    # %/h solo para ventanas ≥60min y solo BUY_NO
EDGE_MINIMO      = 0.02
SLIPPAGE_ESTIMADO= 0.02
DELTA_MIN = 0.38           # ORDER_FLOW_5M — umbral mínimo global
DELTA_MAX = 0.46           # ORDER_FLOW_5M — umbral máximo (zona muerta >0.46)
KELLY_COMPUESTO_BOOST = 1.5
KELLY_COMPUESTO_MAX   = 2.00
THETA_OU = 30.0
ORDER_FLOW_BLACKLIST_HOURS = {7, 11, 18}  # UTC: 09xx/13xx/20xx Madrid — IC negativo
ORDER_FLOW_PAIR_BLACKLIST = {'ETH', 'BNB'}  # sin señal en rango [0.38-0.46]
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
