# Estado del bot — 2026-08-12 15:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.81 $** |
| P&L real total | 🔴 **-42.41 $** |
| P&L real hoy | -2.36 $ |
| P&L real 7 días | -7.66 $ |
| Fees pagados (real) | 15.39 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5915.19 $ |
| P&L sim compuesto | 🟢 +15432.09 $ (ficción Kelly: +60661% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +176.43 $ |
| Operaciones resueltas | 119347 (73124 WIN / 46223 LOSS) — 61.3% |
| Señales abiertas | 510 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11868 | 61.4% | +0.114 | ➡️ estable | +5709.04$ | 0.54$ | ✅ activa |
| GBM_LATE_15M | 14092 | 60.2% | +0.102 | ➡️ estable | +4825.79$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10737 | 59.7% | +0.097 | 📈 madura (+0.06) | +4222.05$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3808 | 64.8% | +0.148 | ➡️ estable | +1813.00$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1311 | 72.6% | +0.226 | ➡️ estable | +1132.48$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4385 | 55.6% | +0.056 | 📈 madura (+0.05) | +578.43$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 537 | 54.7% | +0.047 | 📉 agota (-0.08) | +103.24$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1784 | 49.9% | -0.001 | 📈 madura (+0.08) | +62.49$ | 0.73$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2418 | 62.7% | +0.127 | ➡️ estable | +32.06$ | 1.27$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 220 | 53.6% | +0.036 | ➡️ estable | +3.58$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 190 | 51.6% | +0.016 | 📉 agota (-0.04) | -3.89$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1057 | 51.3% | +0.013 | ➡️ estable | -5.86$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1978 | 54.8% | +0.048 | 📉 agota (-0.17) | -6.02$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 397 | 77.8% | +0.277 | 📉 agota (-0.07) | -19.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 695 | 78.8% | +0.288 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 358 | 46.4% | -0.036 | ➡️ estable | -27.38$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 403 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.60$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 212 | 36.3% | -0.136 | 📉 agota (-0.08) | -34.97$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 372 | 31.5% | -0.184 | 📉 agota (-0.06) | -67.12$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3459 | 70.0% | +0.200 | ➡️ estable | -210.06$ | 1.97$ | ✅ activa |
| BALLENAS_TARDIAS | 4297 | 46.3% | -0.037 | 📈 madura (+0.08) | -740.72$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33429 | 61.5% | +0.115 | ➡️ estable | -1081.88$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15893 | 69.7% | +0.197 | ➡️ estable | -1252.46$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T15:21 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.33$ |
| 2026-08-12T15:21 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-08-12T15:21 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.21$ |
| 2026-08-12T15:21 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T15:21 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T15:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,430.15 | 0.2min |  |
| ✅ ETH | $1,891.97 | 0.2min |  |
| ✅ SOL | $75.73 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,442.30 | consenso |  |
| ETH | $1,892.42 | consenso |  |
| SOL | $75.73 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*