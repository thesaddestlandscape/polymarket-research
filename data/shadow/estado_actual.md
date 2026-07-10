# Estado del bot — 2026-07-10 07:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.01 $** |
| P&L real total | 🟢 **+0.57 $** |
| P&L real hoy | -5.44 $ |
| P&L real 7 días | +2.82 $ |
| Fees pagados (real) | 7.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +674.33 $ |
| P&L sim compuesto | 🟢 +1027.47 $ (ficción Kelly: +4039% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +115.53 $ |
| Operaciones resueltas | 7283 (3958 WIN / 3325 LOSS) — 54.3% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2787 | 61.4% | +0.114 | ➡️ estable | +917.03$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 266 | 66.2% | +0.160 | ➡️ estable | +97.11$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 334 | 55.4% | +0.054 | 📈 madura (+0.12) | +42.04$ | 0.54$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 112 | 58.9% | +0.088 | 📈 madura (+0.07) | +11.00$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 215 | 37.7% | -0.122 | 📈 madura (+0.10) | +7.12$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LEADLAG_BTC_XRP_15M | 18 | 50.0% | +0.000 | — | -0.20$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1207 | 48.5% | -0.015 | ➡️ estable | -1.96$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T07:22 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 3:00AM-3:15AM ET… | ✅ WIN | +4.23$ |
| 2026-07-10T07:22 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 3:00AM-3:15AM ET… | ✅ WIN | +1.68$ |
| 2026-07-10T07:22 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 10, 3:00AM-3:15AM ET… | ❌ LOSS | -0.66$ |
| 2026-07-10T07:16 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 3:00AM-3:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-10T07:16 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 3:00AM-3:15AM ET… | ✅ WIN | +1.19$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-10T07:22 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,895.32 | 0.0min |  |
| ✅ ETH | $1,773.87 | 0.0min |  |
| ✅ SOL | $79.03 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,895.32 | consenso |  |
| ETH | $1,773.87 | consenso |  |
| SOL | $79.00 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*