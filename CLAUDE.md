# CLAUDE.md — Polymarket Research Bot

Documento de contexto completo. Léelo al inicio de cada sesión para retomar sin releer historial.
**Última actualización: 2026-06-27 ~11:45 UTC**

---

## 🛠️ Skills disponibles (usar con `/nombre`)

| Skill | Descripción |
|---|---|
| `/inicio` | Protocolo completo de inicio: bankroll, IC, H-REGIMEN, live status, arb |
| `/ic` | Análisis IC detallado por subtipo + horas ORDER_FLOW + progreso hacia live |
| `/hipotesis` | Estado actualizado de todas las hipótesis activas con datos reales |
| `/dev` | Instrucciones para trabajar en el worktree de desarrollo sin tocar producción |

## 🌿 Worktrees

```bash
/root/polymarket-research      # main — BOT EN PRODUCCIÓN, loops corriendo
/root/polymarket-research-dev  # dev  — experimentos, cambios de estrategia
git worktree list              # ver estado
git merge dev --no-ff          # (desde main) promover experimento validado
```

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
| **`data_quality.py`** | **Guardián calidad de datos — 4 capas L1-L4 → data_quality.json** |
| `live_guard.py` | Guardián: switch + ventanas horarias → ¿puede operar? |
| `live_stake.py` | Kelly stake con bankroll completo + 3 niveles de circuit breaker |
| `live_control.py` | Listener Telegram: /on /off /status /help |
| `live_switch.sh` | bash live_switch.sh on/off/status |

---

## Estado de estrategias — 2026-06-27 (sesión madrugada)

### Bankroll simulado: **−4.96€** (−24.96€ PNL total) | 1160 ops | 49.0% WR
### ⚠️ El PNL negativo viene ÍNTEGRAMENTE de estrategias ya desactivadas.
### Con solo las estrategias activas actuales (excl. desactivadas): PNL estimado positivo.

| Estrategia | n | Win% | IC | PNL | Estado |
|---|---|---|---|---|---|
| **BUY_NO #15min (todas pares)** | **40** | **62%** | **+0.119** | **+11.07€** | **🔥 LISTA PARA LIVE — IC≥0.10 n≥40 — bloqueado por credenciales** |
| UPDOWN_GBM#SOL#15min | 36 | 56% | +0.053 | +5.00€ | ⏳ n=36/40 — ETA hoy sáb 27 (4 ops) |
| **UPDOWN_GBM#BTC#60min** | **17** | **65%** | **+0.112** | **+2.00€** | **⏳ mejor IC activo — ETA lun 29** |
| UPDOWN_GBM#ETH#60min | 19 | 57% | +0.068 | +0.56€ | ⏳ ETA dom 28-lun 29 |
| UPDOWN_GBM#BTC#15min | 43 | 56% | +0.056 | +0.64€ | ⚠️ n=43 alcanzado, IC=+0.056 < umbral 0.08 |
| UPDOWN_GBM#ETH#15min | 58 | 55% | +0.050 | +3.33€ | ⚠️ n≥40 pero IC bajo |
| ORDER_FLOW_5M BUY_NO (BTC+SOL) | 425 BUY_NO total | 56% | +0.057 | +33.54€ | ✅ activa (BUY_YES filtrado) |
| BUY_YES #15min (todas pares) | 104 | 52% | +0.019 | −1.29€ | 🔶 Filtro drift_60min activo — mejorando |
| **BTC#15min con drift_15min≥0.3** | **13** | **77%** | **+0.152** | **+5.68€** | **🔥 Filtro activo desde 2026-06-27 — mejora retroactiva +6.81€** |
| **UPDOWN_GBM#5min (todos pares)** | **56** | **33%** | **-0.155** | **~-16€** | **🚫 DESACTIVADA MANUALMENTE 2026-06-27** |
| **UPDOWN_GBM#BTC#5min** | 16 | 31% | -0.133 | -6.30€ | 🚫 DESACTIVADA MANUALMENTE 2026-06-27 |
| **UPDOWN_GBM#ETH#5min** | 12 | 33% | -0.086 | -3.67€ | 🚫 DESACTIVADA MANUALMENTE 2026-06-27 |
| **UPDOWN_GBM#SOL#5min** | 17 | 35% | -0.112 | -4.84€ | 🚫 DESACTIVADA MANUALMENTE 2026-06-27 |
| UPDOWN_OU_5M | 57 | 26% | -0.229 | -13.76€ | 🚫 DESACTIVADA |
| SMART_FLOW_1H | 20 | 20% | -0.273 | -9.86€ | 🚫 DESACTIVADA |
| UPDOWN_GBM#240min | 12 | 9% | -0.171 | ~-5€ | 🚫 DESACTIVADA |

---

## Hipótesis — estado actualizado 2026-06-26

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
| BTC#60min | 16 | 60% | +0.089 | +0.99€ |
| SOL#60min | 7 | 43% | -0.019 | +0.42€ |

ICs estables. Backfill valida la señal.
**Acción**: seguir acumulando. Umbral live: IC≥0.08, n≥40. ETH necesita ~22 ops más (ETA dom 28), BTC ~24 (ETA lun 29).

### H-ORDER_FLOW-DECAY ✅ RESUELTA — DELTA_MAX implementado

Análisis (n=518 con features) reveló que la señal **no es monótona**:
- `[0.38-0.46]`: IC=+0.059 (268 ops) → sweet spot ✅
- `[0.46-0.65]`: IC=-0.079 (250 ops) → zona muerta ❌ señal ya priceada, reversión
- `[0.65+]`: IC=+0.032 (45 ops) → extremo, pocas ops

**Fix aplicado**: `DELTA_MAX = 0.46` en `s_order_flow_5m`. Zona muerta eliminada.
**Resultado**: IC +0.019 → +0.059, PNL histórico +4.89€ → +13.53€ (con el filtro).

### H-DRIFT-EFECTO — MOOT (arquitectura cambiada)

El filtro de 15min fue eliminado (H-REGIMEN refutada). El nuevo filtro (60min+ BUY_NO) es diferente y empieza desde cero. No hay datos post-filtro que analizar. Esperar n≥30 en 60min para evaluar impacto del nuevo filtro.

### H-VENTANAS-HORARIAS ✅ ACTUALIZADA (2026-06-26 mañana)

Con n≥1000 ops en ORDER_FLOW, el patrón horario expandido (6 horas bloqueadas):

| Hora UTC | Madrid | IC | PNL | Estado |
|---|---|---|---|---|
| 17:xx | 19:xx | **+0.208** n=22 | +4.88€ | ✅ mejor hora |
| 19:xx | 21:xx | **+0.143** n=40 | +5.50€ | ✅ muy buena |
| 15:xx | 17:xx | **+0.133** n=28 | +5.03€ | ✅ muy buena |
| 13:xx | 15:xx | **+0.125** n=30 | +6.08€ | ✅ muy buena |
| 10:xx | 12:xx | **−0.190** n=28 | −6.18€ | 🚫 bloqueada (añadida 2026-06-26) |
| 07:xx | 09:xx | **−0.227** n=20 | −5.20€ | 🚫 bloqueada |
| 18:xx | 20:xx | **−0.178** n=16 | −4.15€ | 🚫 bloqueada |
| 13:xx | 15:xx | **+0.112** n=17 | +3.56€ | ✅ activa — ventana live añadida |
| 20:xx | 22:xx | +0.000 n=18 | −0.17€ | 〰️ neutral BTC+SOL (el -0.095 era de pares excluidos) |
| 22:xx | 00:xx | **−0.115** n=37 full / IC=+0.086 n=12 BTC+SOL | — | 🚫 bloqueada (n BTC+SOL insuficiente) |
| 09:xx | 11:xx | **−0.067** n=18 | −1.81€ | 🚫 bloqueada (añadida 2026-06-26) |
| 11:xx | 13:xx | −0.057 n=59 | −5.07€ | 🚫 bloqueada |
| 02:xx | 04:xx | **−0.081** n=20 | −1.96€ | 🚫 bloqueada (añadida 2026-06-26) |

**Fix 1 (2026-06-25)**: `{7, 11, 18}` — mejora retroactiva +14.42€.
**Fix 2 (2026-06-26 mañana)**: ampliado a `{2, 7, 9, 10, 11, 22}` — mejora retroactiva adicional +16.88€ (total acumulado +31.30€).
**Fix 3 (2026-06-26 tarde)**: hora 20 UTC revertida — el IC=-0.095 era de ETH/XRP/DOGE; para BTC+SOL IC=+0.000 n=18. Set queda `{2,7,9,10,11,22}`.
**Fix 4 (2026-06-26 tarde)**: ventana live 15:00-16:00 Madrid (UTC 13h) añadida — OF IC=+0.112 n=17.
**Config live**: ventana mediodia 12:30-13:30 Madrid eliminada (GBM IC=-0.154, OF IC=-0.057 — peor ventana en ambas).

### H-DRIFT60-BUY_YES_15MIN ✅ IMPLEMENTADA — 2026-06-26 tarde

Análisis n=81 BUY_YES #15min con features: drift_60min ∈ [0, +0.5%) es el único rango rentable.

| drift_60min | n | Win% | IC | PNL |
|---|---|---|---|---|
| **[0, +0.5%)** | **22** | **73%** | **+0.208** | **+8.32€** |
| < 0% (bajista) | 33 | 48% | +0.000 | −4.97€ |
| ≥ 0.5% (muy alcista) | 26 | 42% | −0.044 | −2.97€ |

Consistente por par: BTC 7/8 (88%), ETH 6/8 (75%), SOL 3/4 (75%).
Lógica: drift moderado confirma dirección sin estar ya priceado; drift fuerte → el mercado ya lo sabe.
**Implementado en `shadow_predict.py`**: `DRIFT_60_BUY_YES_15M_LO=0.0`, `DRIFT_60_BUY_YES_15M_HI=0.5`
Mejora retroactiva potencial: **+16.26€** (op saltadas: 59, PNL evitado: −7.94€).
**Validar con n≥40 ops en forward** antes de considerar ajuste de umbral.

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
08:30-09:30 | 10:30-11:30 | **15:00-16:00** | 16:30-17:30 | 18:30-19:30 | 20:30-21:30
~~12:30-13:30 eliminada~~ — GBM IC=-0.154, OF IC=-0.057 (peor ventana en ambas estrategias)
**15:00-16:00 añadida** (UTC 13h): ORDER_FLOW IC=+0.112 n=17 — mejor candidata libre
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
[✓] ORDER_FLOW blacklist ampliado {2,7,9,10,11,22} (+16.88€ adicional retroactivo)
[✓] ORDER_FLOW_PAIR_BLACKLIST ampliado: ETH+BNB+XRP+DOGE (IC negativo confirmado)
[✓] Prices CSV dual format: cargar_precios_intraday() soporta old/new/mixed
[✓] fetch_binance_klines.py + capture_markets.py escriben formato correcto
[✓] Equity curve deduplicada en dashboard (LightweightCharts ascending timestamps)
[✓] Dashboard per-bet section completa (renderPerBet JS + HTML)
[✓] Kelly por dirección: postmortem genera apuesta_kelly_BUY_YES/BUY_NO; predict override tras determinar dec
[✓] N_BUCKET_MIN 8→15: patrones causales requieren n≥15 para evitar kelly_boost ruidoso
[✓] Filtro drift_60min en BUY_YES #15min: [0,+0.5%) → IC=+0.208 (n=22); fuera → skip (n=59 ops vacías)
[✓] ORDER_FLOW solo BUY_NO (delta<0): BUY_YES IC=-0.038 eliminado; BUY_NO IC=+0.092 (+4.10€ retroactivo)
[✓] GBM#5min desactivados MANUALMENTE 2026-06-27: BTC/ETH/SOL/XRP/#5min aggregate (IC -0.08 a -0.13, edge_min=0.04 insuficiente para bloquear señales de edge alto)
[✓] data_quality.py 2026-06-27: 4 capas L1-L4, bug LTC→ETH fix, .gitattributes union merge, ventanas fds
[✓] BTC#15min filtro drift_15min≥0.3 (2026-06-27): zona muerta [-1,+0.3] IC=-0.100 eliminada; pasarían IC=+0.152. Mejora retroactiva +6.81€
[ ] Bloquear hora 18h UTC en GBM (IC=-0.148 n=11 — esperar n≥15)
[ ] Cross-asset confirmation: GBM BUY_NO + OF BUY_NO mismo activo → boost ×1.5 (esperar n≥20 OF post-filtro)
[ ] Kelly por hora: boost ×1.2 en 15h/17h/19h UTC (esperar n≥40 por hora)
[~] BUY_NO #15min n=39/40, IC=+0.134 — 1 op para live (bloqueado por credenciales)
[~] SOL#15min n=30/40, IC=+0.062 — ETA sábado 27 Jun
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
**Antes de dinero real**: conectar con Polymarket Paper Trader (ver TOOLS.md) para validar live_trade.py.

### P1 — Primer trade real (esta semana)
**BUY_NO #15min**: n=40, IC=+0.119 → **CUMPLE UMBRAL IC≥0.10 n≥40 — SOLO FALTA CREDENCIAL**
**SOL#15min**: n=36, IC=+0.053 → ETA hoy sáb 27 Jun (4 ops)
**BTC#60min**: n=17, IC=+0.112 → mejor IC activo — ETA lunes 29 Jun (23 ops)
**ETH#60min**: n=19, IC=+0.068 → ETA domingo 28 Jun-lunes 29 (19-21 ops)
**BTC#15min**: n=43, IC=+0.056 → n≥40 alcanzado pero IC<0.08 — monitorear

### P2 — ✅ COMPLETADO — Dirección como feature de live (BUY_NO vs BUY_YES)
Implementado 2026-06-26: postmortem trackea BUY_YES/BUY_NO separado en strategy_params.
shadow_predict aplica Kelly específico por dirección tras determinar dec.
BUY_YES #15min: stake mínimo 0.50€. BUY_NO #15min: stake 1.34€ (IC=+0.134).

### P3 — ✅ COMPLETADO — Filtro drift_60min en BUY_YES #15min
Implementado 2026-06-26 noche: solo operar BUY_YES #15min cuando drift_60min ∈ [0, +0.5%).
IC fuera: ≈0 (n=59, PNL=-7.94€). IC dentro: +0.208 (n=22, PNL=+8.32€). Mejora: +16.26€ retroactivo.
**Próxima acción**: monitorear n forward. Con n≥20 ops nuevas revisar si IC se sostiene ≥0.15.
Con n≥40 revisar si el umbral superior (0.5%) es óptimo o cabe subir a 0.7%.

### P4 — ✅ COMPLETADO — ORDER_FLOW solo BUY_NO (delta negativo)
Implementado 2026-06-26 noche: `if delta_ratio > 0: return None` en `s_order_flow_5m`.
Análisis n=271 BTC+SOL: BUY_NO IC=+0.092 PNL=+8.64€ vs BUY_YES IC=−0.038 PNL=−4.10€.
Razón: presión compradora ya visible → priceada en Polymarket; presión vendedora silenciosa → lag.
Mejora retroactiva: +4.10€ eliminados + IC sweet spot +0.058→+0.092.
**Monitorear**: con n≥40 nuevas ops verificar IC≥0.08. Si cae → revisar DELTA_MIN.

### P5 — PENDIENTE — Bloquear hora 18h UTC en GBM
GBM a las 18h UTC: IC=−0.148, n=11, PNL=−2.83€. Ya bloqueada para ORDER_FLOW.
**Acción cuando n≥15**: añadir `GBM_BLACKLIST_HOURS = {18}` en shadow_predict.py,
check en `s_updown_gbm` justo antes de calcular p_up. Posible extensión a `{7, 18}`.
**No implementar antes de n≥15** — con n=11 e IC=−0.148 aún podría ser ruido.

### P6 — PENDIENTE — Cross-asset confirmation (reemplaza Kelly compuesto muerto)
El Kelly compuesto actual (mismo market_id) nunca dispara: GBM=15min, OF=5min, solo 5 solapamientos.
**Nueva lógica**: GBM BUY_NO en ASSET#15min + OF BUY_NO en ASSET#5min en misma ventana → boost ×1.5.
En `_aplicar_kelly_compuesto`: buscar coincidencia por `subtype.split('#')[0]` (activo) en vez de market_id.
**Esperar**: n≥20 ops BUY_NO OF post-filtro para calibrar frecuencia de coincidencia temporal.

### P7 — PENDIENTE — Kelly por hora (boost en ventanas de alta rentabilidad)
Horas top en activas: 15h UTC IC=+0.147 (n=32), 17h IC=+0.107 (n=26), 19h IC=+0.151 (n=41).
Idea: apuesta ×1.2 en esas horas, ×0.8 en horas neutras (IC ∈ [−0.05,+0.05]).
**No implementar antes de**: n≥40 por hora confirmado estable en forward.

### P8 — PENDIENTE — ORDER_FLOW rangos per-par
Backfill calibró: BTC 0.42-0.44, SOL 0.36-0.40. No aplicar aún (n<200 con nuevo filtro BUY_NO activo).
Validar cuando BTC+SOL tengan n≥200 cada uno con blacklist {2,7,9,10,11,22} + BUY_NO-only.

### P9 — PENDIENTE — Dataset Jon-Becker
`github.com/Jon-Becker/prediction-market-analysis` — 36GB histórico.
Desbloquea: calibrar theta OU, OBI, Cross-Market Arb, validar rangos OF per-par.

---

## Análisis retroactivo — cuánto valen los ajustes (2026-06-26)

Con todos los filtros aplicados desde el inicio, el bankroll simulado sería **60-68€** en vez de 5.17€:

| Escenario | Bankroll | PNL |
|---|---|---|
| Real (como ha pasado) | **5.17€** | −14.83€ |
| + Sin OU_5M + SMART_FLOW | 27.88€ | +7.88€ |
| + Sin GBM 5min | 31.79€ | +11.79€ |
| + Sin GBM 240min | 36.82€ | +16.82€ |
| + Blacklist horas {7,11,18} | 51.24€ | +31.24€ |
| + Sin ORDER_FLOW ETH+BNB+XRP+DOGE | 54.40€ | +34.40€ |
| **+ Blacklist ampliado {2,7,9,10,11,22}** | **~68€** | **~+48€** |

El mayor error fue OU_5M + SMART_FLOW (+22.71€ perdidos). El segundo mayor fue no tener el blacklist horario completo (total +31.30€ retroactivo con ambas expansiones). Los rangos per-par del backfill no mejoran retroactivamente porque son demasiado estrechos con el n actual.

---

## Constantes clave

### `shadow_predict.py`
```python
DRIFT_DAMPING = {5: 0.30, 15: 0.20, 60: 0.05, 240: 0.10}  # backfill 90d por ventana
DRIFT_DAMPING_DEFAULT = 0.10      # daily y ventanas no catalogadas
REGIME_BUY_NO_THRESHOLD = 0.7    # %/h solo para ventanas ≥60min y solo BUY_NO
DRIFT_60_BUY_YES_15M_LO = 0.0   # BUY_YES #15min: drift_60min mínimo (%/h)
DRIFT_60_BUY_YES_15M_HI = 0.5   # BUY_YES #15min: drift_60min máximo (%/h)
# BTC#15min: solo operar cuando drift_15min ≥ +0.3%/h (2026-06-27)
# drift<0.3 → IC=-0.100 n=23 (zona muerta); drift≥0.3 → IC=+0.152 n=13
EDGE_MINIMO      = 0.02
SLIPPAGE_ESTIMADO= 0.02
DELTA_MIN = 0.38           # ORDER_FLOW_5M — umbral mínimo global
DELTA_MAX = 0.46           # ORDER_FLOW_5M — umbral máximo (zona muerta >0.46)
# Solo delta<0 (BUY_NO): BUY_YES IC=-0.038 eliminado (implementado 2026-06-26 noche)
KELLY_COMPUESTO_BOOST = 1.5
KELLY_COMPUESTO_MAX   = 2.00
THETA_OU = 30.0
ORDER_FLOW_BLACKLIST_HOURS = {2, 7, 9, 10, 11, 22}  # UTC: IC negativo (evaluado sobre BTC+SOL)
# 07h IC=-0.083 n=10 | 10h IC=-0.028 n=34 | 11h IC=+0.038 n=24 (mejoró, mantener hasta n≥40)
# 02h IC=+0.000 n=14 | 09h IC=-0.054 n=5 | 22h IC=+0.086 n=12 (mantener hasta n≥20)
# 20h ELIMINADO: IC=+0.000 n=18 BTC+SOL (el -0.095 era de ETH/XRP/DOGE)
# 18h: no incluido — IC=-0.018 n=5 BTC+SOL (insuficiente, monitorear)
# Mejora retroactiva acumulada vs {7,11,18}: +16.88€
ORDER_FLOW_PAIR_BLACKLIST = {'ETH', 'BNB', 'XRP', 'DOGE'}  # IC negativo conf=1.00
# ETH: n=112 IC=-0.026 | XRP: n=119 IC=-0.004 | DOGE: n=83 IC=-0.006 | BNB: backfill negativo
# Cache pickle: mercados_recientes TTL=90s, historial_mercados TTL=90s
# Ciclo fast: predict+trade cada 20s / resolve+postmortem cada 60s (3er ciclo)
# Paralelización: fetch_slots (ThreadPool), fetch_mercados_paralelo(20 workers)
# Prices CSV: formato nuevo (asset,price_usd por fila) desde 2026-06-26
# cargar_precios_intraday() soporta ambos formatos + filas mixtas
```

### `shadow_postmortem.py`
```python
IC_FILTRO_MIN  = -0.12
IC_PATRON_MIN  = +0.12
N_BUCKET_MIN   = 15   # subido de 8 el 2026-06-26: n<15 → kelly_boost demasiado ruidoso
UMBRAL_SUBIR_EDGE = (-0.10, 3)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.20, 8)   # bajado de -0.30 el 2026-06-25
# Kelly por dirección (2026-06-26): calcular_params genera apuesta_kelly_BUY_YES / apuesta_kelly_BUY_NO
# shadow_predict aplica el específico tras determinar dec → evita overstakear BUY_YES con IC bajo
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
