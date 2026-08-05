# Estado del bot — 2026-08-05 23:38 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.14 $** |
| P&L real total | 🔴 **-40.08 $** |
| P&L real hoy | -0.76 $ |
| P&L real 7 días | -10.37 $ |
| Fees pagados (real) | 14.38 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6043.77 $ |
| P&L sim compuesto | 🟢 +13040.82 $ (ficción Kelly: +51261% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +689.42 $ |
| Operaciones resueltas | 76630 (47037 WIN / 29593 LOSS) — 61.4% |
| Señales abiertas | 389 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9289 | 62.9% | +0.129 | ➡️ estable | +4648.22$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11921 | 60.2% | +0.102 | ➡️ estable | +3866.61$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9195 | 58.3% | +0.083 | ➡️ estable | +3021.39$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3258 | 66.8% | +0.167 | ➡️ estable | +1703.23$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 3799 | 56.0% | +0.060 | 📈 madura (+0.08) | +540.34$ | 0.60$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 410 | 54.6% | +0.046 | 📉 agota (-0.18) | +94.41$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 277 | 81.6% | +0.314 | ➡️ estable | +62.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 94 | 79.8% | +0.292 | 📈 madura (+0.10) | +61.71$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1409 | 48.2% | -0.018 | ➡️ estable | +34.42$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 364 | 41.5% | -0.085 | 📈 madura (+0.08) | +23.66$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1710 | 51.2% | +0.012 | ➡️ estable | +12.04$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 27 | 74.1% | +0.224 | — | +6.32$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 569 | 80.1% | +0.300 | 📉 agota (-0.04) | -1.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 12 | 33.3% | -0.086 | — | -1.83$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 73 | 91.8% | +0.407 | 📉 agota (-0.05) | -3.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 230 | 78.7% | +0.284 | 📉 agota (-0.04) | -8.64$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 86 | 83.7% | +0.330 | 📈 madura (+0.04) | -15.31$ | 2.00$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1655 | 55.4% | +0.054 | 📉 agota (-0.15) | -41.22$ | 0.54$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1433 | 71.9% | +0.218 | 📉 agota (-0.06) | -83.08$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 1073 | 47.3% | -0.027 | 📉 agota (-0.22) | -93.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 19446 | 62.4% | +0.124 | 📉 agota (-0.06) | -428.69$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7643 | 70.2% | +0.202 | ➡️ estable | -491.29$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T23:37 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.33$ |
| 2026-08-05T23:37 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.35$ |
| 2026-08-05T23:37 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.84$ |
| 2026-08-05T23:37 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.43$ |
| 2026-08-05T23:37 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T23:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,636.00 | 0.1min |  |
| ✅ ETH | $1,907.88 | 0.1min |  |
| ✅ SOL | $73.99 | 0.1min |  |
| ✅ XRP | $1.06 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,654.30 | consenso |  |
| ETH | $1,908.38 | consenso |  |
| SOL | $73.97 | consenso |  |
| XRP | $1.06 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*