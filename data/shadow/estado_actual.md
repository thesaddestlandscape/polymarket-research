# Estado del bot — 2026-08-13 03:55 UTC

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
| P&L fiel (stake fijo 1$) | +6054.44 $ |
| P&L sim compuesto | 🟢 +15914.03 $ (ficción Kelly: +62555% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +174.24 $ |
| Operaciones resueltas | 123586 (75740 WIN / 47846 LOSS) — 61.3% |
| Señales abiertas | 409 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12155 | 61.4% | +0.114 | ➡️ estable | +5823.99$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14338 | 60.1% | +0.101 | ➡️ estable | +4909.92$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10954 | 59.9% | +0.099 | 📈 madura (+0.06) | +4402.43$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3917 | 64.3% | +0.143 | ➡️ estable | +1814.24$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1512 | 72.5% | +0.225 | ➡️ estable | +1310.91$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4510 | 55.6% | +0.056 | 📈 madura (+0.05) | +580.87$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 620 | 55.3% | +0.053 | ➡️ estable | +107.93$ | 0.54$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 187 | 75.9% | +0.257 | 📉 agota (-0.07) | +90.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1861 | 50.3% | +0.003 | 📈 madura (+0.07) | +83.73$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 348 | 79.9% | +0.297 | ➡️ estable | +57.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 438 | 43.6% | -0.064 | 📈 madura (+0.11) | +42.38$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 329 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.77$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2669 | 62.0% | +0.120 | ➡️ estable | +6.17$ | 1.20$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 231 | 54.1% | +0.041 | 📈 madura (+0.04) | +4.82$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 204 | 52.9% | +0.029 | ➡️ estable | -0.03$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1120 | 51.2% | +0.012 | 📉 agota (-0.03) | -7.50$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2009 | 54.6% | +0.045 | 📉 agota (-0.18) | -10.62$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 160 | 89.4% | +0.389 | 📈 madura (+0.11) | -13.12$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 409 | 77.8% | +0.276 | 📉 agota (-0.04) | -20.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 375 | 47.2% | -0.028 | ➡️ estable | -22.13$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 708 | 79.0% | +0.289 | 📉 agota (-0.03) | -23.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 156 | 20.5% | -0.291 | 📈 madura (+0.12) | -27.35$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 381 | 31.5% | -0.184 | 📉 agota (-0.06) | -68.45$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3613 | 70.1% | +0.200 | ➡️ estable | -209.81$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4701 | 47.0% | -0.030 | 📈 madura (+0.08) | -732.14$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34553 | 61.4% | +0.114 | ➡️ estable | -1170.62$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16569 | 69.8% | +0.198 | ➡️ estable | -1281.20$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T03:55 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - August 12, 11:30PM-11:45PM ET… | ✅ WIN | +0.39$ |
| 2026-08-13T03:55 | GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | Ethereum Up or Down - August 12, 11:30PM-11:45PM E… | ❌ LOSS | -2.04$ |
| 2026-08-13T03:55 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.24$ |
| 2026-08-13T03:55 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T03:55 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.47$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T03:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,576.86 | 0.1min |  |
| ✅ ETH | $1,884.95 | 0.1min |  |
| ✅ SOL | $76.28 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,577.00 | consenso |  |
| ETH | $1,885.12 | consenso |  |
| SOL | $76.20 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*