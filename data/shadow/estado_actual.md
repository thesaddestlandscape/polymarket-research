# Estado del bot — 2026-08-10 00:23 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.06 $** |
| P&L real total | 🔴 **-41.16 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.45 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6055.58 $ |
| P&L sim compuesto | 🟢 +14387.85 $ (ficción Kelly: +56556% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +12.38 $ |
| Operaciones resueltas | 101480 (62252 WIN / 39228 LOSS) — 61.3% |
| Señales abiertas | 465 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10808 | 62.1% | +0.121 | ➡️ estable | +5275.53$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13232 | 60.2% | +0.102 | ➡️ estable | +4453.85$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10111 | 59.1% | +0.091 | 📈 madura (+0.04) | +3682.11$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3531 | 66.2% | +0.162 | ➡️ estable | +1806.35$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 777 | 72.8% | +0.228 | 📈 madura (+0.06) | +653.37$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4014 | 55.9% | +0.059 | 📈 madura (+0.07) | +562.31$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 708 | 77.5% | +0.275 | 📈 madura (+0.17) | +309.93$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 141 | 76.6% | +0.262 | 📉 agota (-0.04) | +76.61$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 310 | 80.6% | +0.304 | ➡️ estable | +60.89$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1563 | 48.7% | -0.013 | 📈 madura (+0.03) | +38.59$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1181 | 64.1% | +0.141 | 📈 madura (+0.03) | +35.36$ | 1.41$ | ✅ activa |
| GBM_LATE_60M | 400 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.72$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 661 | 52.6% | +0.026 | ➡️ estable | +8.46$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 129 | 52.7% | +0.027 | 📈 madura (+0.08) | +2.77$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 123 | 53.7% | +0.036 | 📈 madura (+0.09) | +1.35$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 134 | 94.0% | +0.434 | 📈 madura (+0.06) | -0.10$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 41 | 24.4% | -0.244 | 📉 agota (-0.10) | -8.76$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 635 | 79.8% | +0.297 | 📉 agota (-0.04) | -11.00$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 109 | 40.4% | -0.095 | ➡️ estable | -13.25$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 73 | 32.9% | -0.167 | 📈 madura (+0.04) | -13.43$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1836 | 54.7% | +0.047 | 📉 agota (-0.16) | -17.07$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 127 | 86.6% | +0.360 | 📈 madura (+0.11) | -17.26$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 329 | 76.9% | +0.267 | 📉 agota (-0.08) | -24.01$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 343 | 32.4% | -0.175 | 📉 agota (-0.03) | -59.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2701 | 70.1% | +0.201 | 📉 agota (-0.04) | -176.54$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2734 | 42.3% | -0.077 | ➡️ estable | -651.82$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 27909 | 61.9% | +0.119 | 📉 agota (-0.04) | -701.67$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12622 | 69.9% | +0.199 | ➡️ estable | -938.12$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T00:21 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T00:21 | GBM_LATE_15M#ETH#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T00:21 | UPDOWN_GBM_15M_TARDIO#BTC#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T00:21 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | … | ✅ WIN | +0.37$ |
| 2026-08-10T00:21 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.14$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T00:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,083.49 | 0.1min |  |
| ✅ ETH | $1,919.86 | 0.1min |  |
| ✅ SOL | $76.65 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,083.49 | consenso |  |
| ETH | $1,919.86 | consenso |  |
| SOL | $76.63 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*