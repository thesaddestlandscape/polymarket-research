# Estado del bot — 2026-07-09 01:35 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **34.91 $** |
| P&L real total | 🟢 **+9.47 $** |
| P&L real hoy | +2.23 $ |
| P&L real 7 días | +6.08 $ |
| Fees pagados (real) | 5.72 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +357.08 $ |
| P&L sim compuesto | 🟢 +651.84 $ (ficción Kelly: +2562% s/ operativo) |
| P&L sim hoy (2026-07-09) | 🟢 +6.35 $ |
| Operaciones resueltas | 5864 (3122 WIN / 2742 LOSS) — 53.2% |
| Señales abiertas | 149 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2323 | 61.3% | +0.112 | +737.03$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1555 | 51.3% | +0.013 | +16.96$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 28 | 67.9% | +0.167 | +4.54$ | 1.67$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 129 | 34.1% | -0.156 | -0.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 85 | 51.8% | +0.017 | -0.88$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11 | 45.5% | -0.021 | -1.29$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 160 | 48.1% | -0.019 | -7.34$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 141 | 34.0% | -0.157 | -9.44$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | -18.89$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 144 | 52.1% | +0.021 | -20.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1146 | 47.6% | -0.024 | -32.53$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-09T01:34 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 8, 9:15PM-9:30PM ET… | ❌ LOSS | -1.75$ |
| 2026-07-09T01:32 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 8, 9:15PM-9:30PM ET… | ❌ LOSS | -1.46$ |
| 2026-07-09T01:26 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 8, 9:20PM-9:25PM ET… | ✅ WIN | +1.56$ |
| 2026-07-09T01:18 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 8, 9:10PM-9:15PM ET… | ❌ LOSS | -1.34$ |
| 2026-07-09T01:16 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - July 8, 9:10PM-9:15PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-09T01:34 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,298.75 | 0.0min |  |
| ✅ ETH | $1,743.60 | 0.0min |  |
| ✅ SOL | $77.96 | 0.0min |  |
| ✅ XRP | $1.09 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,306.60 | consenso |  |
| ETH | $1,743.60 | consenso |  |
| SOL | $78.07 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*