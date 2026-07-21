# Estado del bot — 2026-07-21 12:13 UTC

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
| P&L fiel (stake fijo 1$) | +3335.45 $ |
| P&L sim compuesto | 🟢 +6294.44 $ (ficción Kelly: +24742% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -121.04 $ |
| Operaciones resueltas | 26695 (16096 WIN / 10599 LOSS) — 60.3% |
| Señales abiertas | 117 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6499 | 60.0% | +0.100 | ➡️ estable | +2124.28$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3695 | 63.8% | +0.138 | 📉 agota (-0.03) | +2053.60$ | 1.38$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3672 | 59.0% | +0.090 | ➡️ estable | +1223.35$ | 0.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 965 | 67.0% | +0.170 | ➡️ estable | +445.45$ | 1.70$ | ✅ activa |
| UPDOWN_GBM | 2048 | 52.7% | +0.027 | 📈 madura (+0.11) | +170.29$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4610 | 68.7% | +0.187 | ➡️ estable | +86.31$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 253 | 58.5% | +0.084 | 📉 agota (-0.07) | +30.08$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 576 | 62.8% | +0.128 | 📉 agota (-0.03) | +16.67$ | 1.28$ | ✅ activa |
| GBM_LATE_5M | 247 | 50.6% | +0.006 | 📉 agota (-0.12) | +15.13$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 248 | 51.6% | +0.016 | 📉 agota (-0.16) | +11.76$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 219 | 81.7% | +0.314 | ➡️ estable | +11.66$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 192 | 51.6% | +0.015 | 📉 agota (-0.21) | +9.20$ | 0.50$ | ✅ activa |
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
| 2026-07-21T12:12 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 21, 4:00AM-8:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T12:08 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 21, 7AM ET… | ❌ LOSS | -1.29$ |
| 2026-07-21T12:05 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 7:55AM-8:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T12:05 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 7:45AM-8:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T12:05 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 21, 7:45AM-8:00AM ET… | ✅ WIN | +1.06$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T12:11 UTC | rechazos 1h: 5 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,329.60 | 0.1min |  |
| ✅ ETH | $1,933.66 | 0.1min |  |
| ✅ SOL | $78.40 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,329.60 | consenso |  |
| ETH | $1,933.66 | consenso |  |
| SOL | $78.33 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:5 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*