# Estado del bot — 2026-08-13 06:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **6.11 $** |
| P&L real total | 🔴 **-45.11 $** |
| P&L real hoy | -2.04 $ |
| P&L real 7 días | -5.79 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6095.09 $ |
| P&L sim compuesto | 🟢 +16042.22 $ (ficción Kelly: +63059% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +302.43 $ |
| Operaciones resueltas | 124455 (76291 WIN / 48164 LOSS) — 61.3% |
| Señales abiertas | 432 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12220 | 61.4% | +0.114 | ➡️ estable | +5848.65$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 14391 | 60.2% | +0.102 | ➡️ estable | +4939.19$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11008 | 60.0% | +0.100 | 📈 madura (+0.07) | +4447.87$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3940 | 64.1% | +0.141 | ➡️ estable | +1814.50$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1560 | 72.5% | +0.225 | ➡️ estable | +1345.43$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4537 | 55.6% | +0.056 | 📈 madura (+0.05) | +586.24$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 633 | 55.3% | +0.053 | ➡️ estable | +106.00$ | 0.53$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1873 | 50.3% | +0.003 | 📈 madura (+0.07) | +84.33$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1740 | 51.5% | +0.015 | ➡️ estable | +18.47$ | 0.59$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2713 | 62.1% | +0.121 | ➡️ estable | +11.31$ | 1.21$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 234 | 54.7% | +0.047 | 📈 madura (+0.05) | +6.45$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 167 | 94.0% | +0.435 | ➡️ estable | -0.38$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1143 | 51.1% | +0.011 | ➡️ estable | -8.42$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2015 | 54.5% | +0.045 | 📉 agota (-0.18) | -12.11$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 385 | 47.5% | -0.025 | ➡️ estable | -19.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 711 | 78.9% | +0.288 | 📉 agota (-0.03) | -23.75$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 383 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3647 | 70.1% | +0.200 | ➡️ estable | -212.55$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4760 | 47.1% | -0.029 | 📈 madura (+0.09) | -722.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34784 | 61.4% | +0.114 | ➡️ estable | -1180.53$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16704 | 69.8% | +0.198 | ➡️ estable | -1303.97$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T06:49 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T06:49 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.84$ |
| 2026-08-13T06:49 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.47$ |
| 2026-08-13T06:49 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.74$ |
| 2026-08-13T06:49 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T06:46 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,717.24 | 0.2min |  |
| ✅ ETH | $1,891.66 | 0.2min |  |
| ✅ SOL | $76.29 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,717.24 | consenso |  |
| ETH | $1,891.97 | consenso |  |
| SOL | $76.29 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*