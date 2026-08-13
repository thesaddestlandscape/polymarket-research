# Estado del bot — 2026-08-13 04:44 UTC

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
| P&L fiel (stake fijo 1$) | +6062.52 $ |
| P&L sim compuesto | 🟢 +15944.28 $ (ficción Kelly: +62674% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +204.49 $ |
| Operaciones resueltas | 123867 (75913 WIN / 47954 LOSS) — 61.3% |
| Señales abiertas | 370 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12174 | 61.4% | +0.114 | ➡️ estable | +5826.65$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14354 | 60.2% | +0.101 | ➡️ estable | +4912.95$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10969 | 59.9% | +0.099 | 📈 madura (+0.06) | +4409.92$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3926 | 64.3% | +0.143 | ➡️ estable | +1815.90$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1523 | 72.4% | +0.224 | ➡️ estable | +1316.04$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4523 | 55.6% | +0.056 | 📈 madura (+0.05) | +579.66$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 622 | 55.3% | +0.053 | ➡️ estable | +107.44$ | 0.53$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 188 | 76.1% | +0.258 | 📉 agota (-0.07) | +92.68$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1865 | 50.3% | +0.003 | 📈 madura (+0.07) | +84.29$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 348 | 79.9% | +0.297 | ➡️ estable | +57.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 439 | 43.5% | -0.065 | 📈 madura (+0.11) | +41.87$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2686 | 62.0% | +0.119 | ➡️ estable | +5.46$ | 1.19$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 232 | 54.3% | +0.043 | 📈 madura (+0.03) | +5.06$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 205 | 53.2% | +0.031 | ➡️ estable | +2.23$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1127 | 51.1% | +0.011 | 📉 agota (-0.04) | -8.11$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2011 | 54.5% | +0.045 | 📉 agota (-0.18) | -10.68$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 161 | 89.4% | +0.390 | 📈 madura (+0.11) | -13.05$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 378 | 47.6% | -0.024 | ➡️ estable | -17.92$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 411 | 77.9% | +0.277 | 📉 agota (-0.04) | -18.89$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 709 | 79.0% | +0.289 | 📉 agota (-0.03) | -22.39$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 381 | 31.5% | -0.184 | 📉 agota (-0.06) | -68.45$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3622 | 70.0% | +0.200 | ➡️ estable | -211.15$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4727 | 47.0% | -0.030 | 📈 madura (+0.08) | -727.26$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34626 | 61.4% | +0.114 | ➡️ estable | -1162.45$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16612 | 69.8% | +0.198 | ➡️ estable | -1290.68$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T04:44 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T04:44 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.33$ |
| 2026-08-13T04:44 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T04:44 | BALLENAS_TARDIAS#DOGE#5min | … | ✅ WIN | +0.68$ |
| 2026-08-13T04:44 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T04:41 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,618.93 | 0.1min |  |
| ✅ ETH | $1,887.95 | 0.1min |  |
| ✅ SOL | $76.14 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,618.93 | consenso |  |
| ETH | $1,888.11 | consenso |  |
| SOL | $76.10 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*