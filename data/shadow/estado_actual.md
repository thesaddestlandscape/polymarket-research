# Estado del bot — 2026-08-13 04:13 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **7.08 $** |
| P&L real total | 🔴 **-44.14 $** |
| P&L real hoy | -1.07 $ |
| P&L real 7 días | -4.82 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6050.20 $ |
| P&L sim compuesto | 🟢 +15921.81 $ (ficción Kelly: +62586% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +182.02 $ |
| Operaciones resueltas | 123700 (75804 WIN / 47896 LOSS) — 61.3% |
| Señales abiertas | 393 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12162 | 61.4% | +0.114 | ➡️ estable | +5819.41$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14344 | 60.2% | +0.101 | ➡️ estable | +4913.72$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10960 | 59.9% | +0.099 | 📈 madura (+0.06) | +4405.92$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3921 | 64.3% | +0.143 | ➡️ estable | +1815.87$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1518 | 72.5% | +0.224 | ➡️ estable | +1315.47$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4517 | 55.6% | +0.056 | 📈 madura (+0.05) | +580.71$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 621 | 55.4% | +0.054 | ➡️ estable | +108.46$ | 0.56$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 188 | 76.1% | +0.258 | 📉 agota (-0.07) | +92.68$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1863 | 50.3% | +0.003 | 📈 madura (+0.07) | +82.16$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 348 | 79.9% | +0.297 | ➡️ estable | +57.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 439 | 43.5% | -0.065 | 📈 madura (+0.11) | +41.87$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2675 | 62.0% | +0.120 | ➡️ estable | +8.77$ | 1.20$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 232 | 54.3% | +0.043 | 📈 madura (+0.03) | +5.06$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 205 | 53.2% | +0.031 | ➡️ estable | +2.23$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1122 | 51.1% | +0.011 | 📉 agota (-0.04) | -8.52$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2009 | 54.6% | +0.045 | 📉 agota (-0.18) | -10.62$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 161 | 89.4% | +0.390 | 📈 madura (+0.11) | -13.05$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 411 | 77.9% | +0.277 | 📉 agota (-0.04) | -18.89$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 377 | 47.5% | -0.025 | ➡️ estable | -19.47$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 709 | 79.0% | +0.289 | 📉 agota (-0.03) | -22.39$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 381 | 31.5% | -0.184 | 📉 agota (-0.06) | -68.45$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3617 | 70.0% | +0.200 | ➡️ estable | -211.62$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4709 | 47.0% | -0.030 | 📈 madura (+0.08) | -735.32$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34580 | 61.4% | +0.114 | ➡️ estable | -1171.12$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16584 | 69.8% | +0.198 | ➡️ estable | -1285.72$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T04:12 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | … | ✅ WIN | +0.00$ |
| 2026-08-13T04:12 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T04:12 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 12, 11:55PM-12:00AM ET… | ✅ WIN | +0.47$ |
| 2026-08-13T04:12 | UPDOWN_GBM#XRP#5min | XRP Up or Down - August 12, 11:55PM-12:00AM ET… | ✅ WIN | +0.47$ |
| 2026-08-13T04:12 | UPDOWN_GBM#ETH#5min | Ethereum Up or Down - August 12, 11:55PM-12:00AM E… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T04:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,577.00 | 0.1min |  |
| ✅ ETH | $1,885.15 | 0.1min |  |
| ✅ SOL | $76.22 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,577.00 | consenso |  |
| ETH | $1,885.15 | consenso |  |
| SOL | $76.17 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*