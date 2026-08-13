# Estado del bot — 2026-08-13 03:22 UTC

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
| P&L fiel (stake fijo 1$) | +6059.52 $ |
| P&L sim compuesto | 🟢 +15893.75 $ (ficción Kelly: +62475% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +153.96 $ |
| Operaciones resueltas | 123365 (75611 WIN / 47754 LOSS) — 61.3% |
| Señales abiertas | 427 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12139 | 61.4% | +0.114 | ➡️ estable | +5812.93$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14323 | 60.2% | +0.102 | ➡️ estable | +4904.68$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10940 | 59.9% | +0.099 | 📈 madura (+0.06) | +4389.27$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3907 | 64.4% | +0.144 | ➡️ estable | +1820.30$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1499 | 72.5% | +0.225 | ➡️ estable | +1299.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4505 | 55.6% | +0.056 | 📈 madura (+0.05) | +578.61$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 617 | 55.6% | +0.056 | ➡️ estable | +110.52$ | 0.62$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 185 | 76.2% | +0.259 | 📉 agota (-0.06) | +90.08$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1857 | 50.4% | +0.003 | 📈 madura (+0.07) | +83.22$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 347 | 80.1% | +0.299 | ➡️ estable | +59.49$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 438 | 43.6% | -0.064 | 📈 madura (+0.11) | +42.38$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 329 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.77$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2659 | 62.0% | +0.120 | ➡️ estable | +8.79$ | 1.20$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 231 | 54.1% | +0.041 | 📈 madura (+0.04) | +4.82$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 204 | 52.9% | +0.029 | ➡️ estable | -0.03$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1114 | 51.2% | +0.012 | 📉 agota (-0.03) | -7.41$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2006 | 54.6% | +0.046 | 📉 agota (-0.18) | -9.99$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 160 | 89.4% | +0.389 | 📈 madura (+0.11) | -13.12$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 409 | 77.8% | +0.276 | 📉 agota (-0.04) | -20.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 375 | 47.2% | -0.028 | ➡️ estable | -22.13$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 706 | 78.9% | +0.288 | 📉 agota (-0.03) | -24.67$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 156 | 20.5% | -0.291 | 📈 madura (+0.12) | -27.35$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 379 | 31.4% | -0.185 | 📉 agota (-0.06) | -68.43$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3601 | 70.0% | +0.200 | ➡️ estable | -210.07$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4683 | 46.9% | -0.031 | 📈 madura (+0.09) | -733.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34503 | 61.4% | +0.114 | ➡️ estable | -1162.59$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16534 | 69.8% | +0.198 | ➡️ estable | -1277.00$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T03:21 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.35$ |
| 2026-08-13T03:21 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.21$ |
| 2026-08-13T03:21 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T03:21 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-13T03:21 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 12, 11:05PM-11:10PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T03:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,513.00 | 0.1min |  |
| ✅ ETH | $1,881.00 | 0.1min |  |
| ✅ SOL | $76.05 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,511.00 | consenso |  |
| ETH | $1,881.56 | consenso |  |
| SOL | $76.08 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*