# Estado del bot — 2026-08-13 03:47 UTC

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
| P&L fiel (stake fijo 1$) | +6049.85 $ |
| P&L sim compuesto | 🟢 +15900.07 $ (ficción Kelly: +62500% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +160.28 $ |
| Operaciones resueltas | 123524 (75701 WIN / 47823 LOSS) — 61.3% |
| Señales abiertas | 402 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12150 | 61.4% | +0.114 | ➡️ estable | +5818.05$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14332 | 60.1% | +0.101 | ➡️ estable | +4904.93$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10949 | 59.9% | +0.099 | 📈 madura (+0.06) | +4400.57$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3914 | 64.3% | +0.143 | ➡️ estable | +1814.51$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1508 | 72.5% | +0.225 | ➡️ estable | +1310.98$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4508 | 55.6% | +0.056 | 📈 madura (+0.05) | +579.41$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 619 | 55.4% | +0.054 | ➡️ estable | +109.16$ | 0.57$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 187 | 75.9% | +0.257 | 📉 agota (-0.07) | +90.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1859 | 50.3% | +0.003 | 📈 madura (+0.07) | +82.20$ | 0.76$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 348 | 79.9% | +0.297 | ➡️ estable | +57.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 438 | 43.6% | -0.064 | 📈 madura (+0.11) | +42.38$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 329 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.77$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2666 | 62.0% | +0.120 | ➡️ estable | +7.84$ | 1.20$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 231 | 54.1% | +0.041 | 📈 madura (+0.04) | +4.82$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 204 | 52.9% | +0.029 | ➡️ estable | -0.03$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1117 | 51.2% | +0.012 | 📉 agota (-0.03) | -6.96$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2008 | 54.5% | +0.045 | 📉 agota (-0.18) | -11.01$ | 0.50$ | ✅ activa |
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
| UPDOWN_OU_5M | 380 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.94$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3610 | 70.0% | +0.200 | ➡️ estable | -210.78$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4696 | 47.0% | -0.030 | 📈 madura (+0.09) | -732.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34541 | 61.4% | +0.114 | ➡️ estable | -1171.27$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16563 | 69.8% | +0.198 | ➡️ estable | -1281.56$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T03:46 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-08-13T03:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-08-13T03:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-13T03:46 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.57$ |
| 2026-08-13T03:46 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T03:44 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,509.83 | 0.2min |  |
| ✅ ETH | $1,882.13 | 0.2min |  |
| ✅ SOL | $76.15 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,519.80 | consenso |  |
| ETH | $1,882.13 | consenso |  |
| SOL | $76.15 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*