# Estado del bot — 2026-08-07 14:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.99 $** |
| P&L real total | 🔴 **-41.23 $** |
| P&L real hoy | +0.70 $ |
| P&L real 7 días | -7.21 $ |
| Fees pagados (real) | 14.63 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5913.93 $ |
| P&L sim compuesto | 🟢 +13606.68 $ (ficción Kelly: +53485% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +134.13 $ |
| Operaciones resueltas | 86628 (52938 WIN / 33690 LOSS) — 61.1% |
| Señales abiertas | 395 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9787 | 62.8% | +0.128 | ➡️ estable | +4946.25$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12468 | 60.1% | +0.101 | ➡️ estable | +4138.15$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9629 | 58.5% | +0.085 | ➡️ estable | +3263.59$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3476 | 66.5% | +0.164 | ➡️ estable | +1803.48$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 3978 | 56.0% | +0.060 | 📈 madura (+0.07) | +564.96$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 386 | 69.7% | +0.196 | 📉 agota (-0.05) | +265.38$ | 1.96$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1499 | 48.5% | -0.015 | 📈 madura (+0.04) | +44.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 82 | 68.3% | +0.179 | 📉 agota (-0.14) | +11.33$ | 1.79$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 250 | 52.0% | +0.020 | 📉 agota (-0.05) | +0.26$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 72 | 50.0% | +0.000 | 📈 madura (+0.11) | -0.28$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 59 | 50.8% | +0.008 | 📈 madura (+0.11) | -0.76$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 97 | 92.8% | +0.419 | ➡️ estable | -2.40$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 60 | 40.0% | -0.097 | 📈 madura (+0.12) | -7.34$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 102 | 86.3% | +0.356 | 📈 madura (+0.04) | -13.68$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 279 | 77.8% | +0.276 | 📉 agota (-0.07) | -14.52$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 82 | 13.4% | -0.357 | ➡️ estable | -23.61$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1729 | 54.7% | +0.047 | 📉 agota (-0.16) | -41.06$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 289 | 32.9% | -0.170 | 📈 madura (+0.05) | -50.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1961 | 69.8% | +0.198 | 📉 agota (-0.06) | -153.19$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 1730 | 42.3% | -0.077 | 📉 agota (-0.18) | -271.23$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22817 | 61.9% | +0.119 | 📉 agota (-0.06) | -571.42$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9643 | 69.5% | +0.195 | ➡️ estable | -732.46$ | 1.95$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T14:15 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T14:15 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T14:15 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T14:15 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T14:15 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T14:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,776.00 | 0.2min |  |
| ✅ ETH | $1,911.10 | 0.2min |  |
| ✅ SOL | $73.73 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,800.20 | consenso |  |
| ETH | $1,912.64 | consenso |  |
| SOL | $73.78 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*