# Estado del bot — 2026-08-06 20:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.30 $** |
| P&L real total | 🔴 **-41.92 $** |
| P&L real hoy | -2.60 $ |
| P&L real 7 días | -12.21 $ |
| Fees pagados (real) | 14.54 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6011.08 $ |
| P&L sim compuesto | 🟢 +13415.29 $ (ficción Kelly: +52733% s/ operativo) |
| P&L sim hoy (2026-08-06) | 🟢 +384.37 $ |
| Operaciones resueltas | 82124 (50231 WIN / 31893 LOSS) — 61.2% |
| Señales abiertas | 390 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9556 | 62.8% | +0.128 | ➡️ estable | +4813.23$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12221 | 60.1% | +0.101 | ➡️ estable | +4043.34$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9428 | 58.4% | +0.084 | ➡️ estable | +3167.48$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3407 | 66.6% | +0.166 | ➡️ estable | +1790.60$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 3921 | 55.9% | +0.059 | 📈 madura (+0.08) | +550.14$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 214 | 72.4% | +0.222 | 📈 madura (+0.08) | +135.92$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 427 | 55.3% | +0.052 | 📉 agota (-0.13) | +102.32$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 108 | 77.8% | +0.273 | ➡️ estable | +65.95$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 283 | 81.3% | +0.311 | ➡️ estable | +60.94$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1475 | 48.4% | -0.016 | ➡️ estable | +39.30$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 375 | 42.4% | -0.076 | 📈 madura (+0.11) | +22.72$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 313 | 56.5% | +0.065 | 📉 agota (-0.11) | +20.90$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1717 | 51.4% | +0.014 | ➡️ estable | +16.38$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 326 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.52$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 108 | 52.8% | +0.027 | 📈 madura (+0.09) | +0.96$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 587 | 80.4% | +0.303 | 📉 agota (-0.04) | +0.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 41 | 51.2% | +0.012 | 📈 madura (+0.38) | -0.66$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 86 | 93.0% | +0.420 | 📉 agota (-0.04) | -1.60$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 254 | 79.5% | +0.293 | ➡️ estable | -2.54$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 47 | 44.7% | -0.051 | 📉 agota (-0.06) | -2.71$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 55 | 38.2% | -0.114 | 📈 madura (+0.09) | -7.71$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 54 | 31.5% | -0.179 | 📉 agota (-0.03) | -10.59$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 37 | 13.5% | -0.346 | 📈 madura (+0.04) | -12.37$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 95 | 85.3% | +0.345 | 📈 madura (+0.04) | -14.45$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1695 | 54.9% | +0.049 | 📉 agota (-0.16) | -33.17$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 196 | 34.2% | -0.157 | 📈 madura (+0.11) | -33.39$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1715 | 70.1% | +0.201 | 📉 agota (-0.08) | -125.45$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 1501 | 41.8% | -0.082 | 📉 agota (-0.20) | -220.08$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 21277 | 62.1% | +0.121 | 📉 agota (-0.06) | -494.02$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 8711 | 69.6% | +0.196 | ➡️ estable | -632.97$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-06T20:29 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.41$ |
| 2026-08-06T20:29 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.65$ |
| 2026-08-06T20:29 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.71$ |
| 2026-08-06T20:29 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.84$ |
| 2026-08-06T20:29 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.65$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-06T20:28 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,435.71 | 0.1min |  |
| ✅ ETH | $1,906.01 | 0.1min |  |
| ✅ SOL | $72.86 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,438.70 | consenso |  |
| ETH | $1,906.77 | consenso |  |
| SOL | $72.80 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*