# Estado del bot — 2026-07-21 09:48 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3339.55 $ |
| P&L sim compuesto | 🟢 +6263.45 $ (ficción Kelly: +24620% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -152.03 $ |
| Operaciones resueltas | 26475 (15979 WIN / 10496 LOSS) — 60.4% |
| Señales abiertas | 107 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6461 | 60.1% | +0.100 | ➡️ estable | +2114.22$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3657 | 63.9% | +0.139 | ➡️ estable | +2047.05$ | 1.39$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3634 | 59.1% | +0.091 | ➡️ estable | +1215.15$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 959 | 66.9% | +0.169 | 📉 agota (-0.03) | +439.02$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2045 | 52.7% | +0.027 | 📈 madura (+0.11) | +167.92$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 207 | 63.3% | +0.132 | ➡️ estable | +102.28$ | 1.32$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4574 | 68.7% | +0.187 | ➡️ estable | +77.42$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 240 | 52.1% | +0.021 | 📉 agota (-0.11) | +18.70$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 563 | 62.9% | +0.128 | 📉 agota (-0.03) | +17.40$ | 1.28$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 100 | 79.0% | +0.284 | ➡️ estable | +16.34$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 247 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.27$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 215 | 81.9% | +0.316 | ➡️ estable | +11.52$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 166 | 53.0% | +0.030 | 📉 agota (-0.24) | +11.35$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T09:47 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 5:35AM-5:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T09:47 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 21, 5:35AM-5:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T09:47 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 5:30AM-5:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T09:47 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 5:30AM-5:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T09:47 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 5:30AM-5:45AM ET… | ✅ WIN | +1.11$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T09:47 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,282.93 | 0.1min |  |
| ✅ ETH | $1,940.12 | 0.1min |  |
| ✅ SOL | $78.47 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,282.93 | consenso |  |
| ETH | $1,940.12 | consenso |  |
| SOL | $78.38 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*