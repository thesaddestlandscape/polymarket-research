# Estado del bot — 2026-08-13 06:59 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **5.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6080.20 $ |
| P&L sim compuesto | 🟢 +16027.71 $ (ficción Kelly: +63002% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +287.92 $ |
| Operaciones resueltas | 124510 (76316 WIN / 48194 LOSS) — 61.3% |
| Señales abiertas | 425 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12225 | 61.4% | +0.114 | ➡️ estable | +5841.71$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14393 | 60.2% | +0.102 | ➡️ estable | +4940.59$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11011 | 60.0% | +0.100 | 📈 madura (+0.07) | +4452.05$ | 1.96$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3942 | 64.1% | +0.141 | ➡️ estable | +1812.36$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1564 | 72.4% | +0.224 | ➡️ estable | +1343.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4537 | 55.6% | +0.056 | 📈 madura (+0.05) | +586.24$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 635 | 55.3% | +0.053 | ➡️ estable | +105.16$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1873 | 50.3% | +0.003 | 📈 madura (+0.07) | +84.33$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1740 | 51.5% | +0.015 | ➡️ estable | +18.47$ | 0.59$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2717 | 62.2% | +0.122 | ➡️ estable | +13.78$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 234 | 54.7% | +0.047 | 📈 madura (+0.05) | +6.45$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 167 | 94.0% | +0.435 | ➡️ estable | -0.38$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1144 | 51.1% | +0.011 | ➡️ estable | -7.94$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2016 | 54.5% | +0.045 | 📉 agota (-0.18) | -13.13$ | 0.50$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 388 | 47.7% | -0.023 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 711 | 78.9% | +0.288 | 📉 agota (-0.03) | -23.75$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 383 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3647 | 70.1% | +0.200 | ➡️ estable | -212.55$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4764 | 47.0% | -0.030 | 📈 madura (+0.08) | -727.25$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34799 | 61.4% | +0.114 | ➡️ estable | -1179.32$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16713 | 69.8% | +0.198 | ➡️ estable | -1310.61$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T06:58 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.43$ |
| 2026-08-13T06:58 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:58 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:58 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.68$ |
| 2026-08-13T06:58 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T06:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,805.62 | 0.1min |  |
| ✅ ETH | $1,895.41 | 0.1min |  |
| ✅ SOL | $76.47 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,807.30 | consenso |  |
| ETH | $1,895.92 | consenso |  |
| SOL | $76.34 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*