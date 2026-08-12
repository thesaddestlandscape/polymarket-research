# Estado del bot — 2026-08-12 16:49 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.26 $** |
| P&L real total | 🔴 **-41.96 $** |
| P&L real hoy | -1.91 $ |
| P&L real 7 días | -7.21 $ |
| Fees pagados (real) | 15.39 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5946.77 $ |
| P&L sim compuesto | 🟢 +15511.27 $ (ficción Kelly: +60972% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +255.61 $ |
| Operaciones resueltas | 119799 (73411 WIN / 46388 LOSS) — 61.3% |
| Señales abiertas | 588 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11897 | 61.4% | +0.114 | ➡️ estable | +5720.77$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14118 | 60.2% | +0.102 | ➡️ estable | +4845.87$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10758 | 59.7% | +0.097 | 📈 madura (+0.06) | +4241.67$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3816 | 64.7% | +0.147 | ➡️ estable | +1811.80$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1330 | 72.6% | +0.226 | ➡️ estable | +1151.44$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4398 | 55.6% | +0.056 | 📈 madura (+0.05) | +577.96$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 778 | 77.9% | +0.278 | 📈 madura (+0.14) | +339.89$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 548 | 55.1% | +0.051 | 📉 agota (-0.05) | +106.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1789 | 50.0% | -0.000 | 📈 madura (+0.08) | +66.13$ | 0.73$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2440 | 62.6% | +0.126 | ➡️ estable | +28.46$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 221 | 53.8% | +0.038 | ➡️ estable | +5.09$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 191 | 51.8% | +0.018 | 📉 agota (-0.04) | -3.58$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1060 | 51.2% | +0.012 | ➡️ estable | -6.40$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1982 | 54.7% | +0.047 | 📉 agota (-0.17) | -7.73$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 69 | 21.7% | -0.275 | 📉 agota (-0.09) | -17.18$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 399 | 77.9% | +0.278 | 📉 agota (-0.07) | -18.62$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 124 | 34.7% | -0.151 | 📈 madura (+0.08) | -20.78$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 696 | 78.9% | +0.288 | ➡️ estable | -25.07$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 358 | 46.4% | -0.036 | ➡️ estable | -27.38$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 217 | 37.8% | -0.121 | 📉 agota (-0.04) | -32.49$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 404 | 44.1% | -0.059 | 📉 agota (-0.09) | -33.11$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 374 | 31.3% | -0.186 | 📉 agota (-0.06) | -68.14$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3476 | 70.0% | +0.200 | ➡️ estable | -207.50$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4340 | 46.5% | -0.035 | 📈 madura (+0.08) | -720.89$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33539 | 61.5% | +0.115 | ➡️ estable | -1100.03$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15965 | 69.7% | +0.197 | ➡️ estable | -1255.37$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T16:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.39$ |
| 2026-08-12T16:49 | BALLENAS_TARDIAS#BNB#5min | … | ✅ WIN | +0.99$ |
| 2026-08-12T16:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.41$ |
| 2026-08-12T16:49 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.68$ |
| 2026-08-12T16:49 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.54$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T16:46 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,428.22 | 0.2min |  |
| ✅ ETH | $1,889.87 | 0.2min |  |
| ✅ SOL | $75.55 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,453.10 | consenso |  |
| ETH | $1,890.01 | consenso |  |
| SOL | $75.55 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*