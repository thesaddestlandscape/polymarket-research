# Estado del bot — 2026-08-06 01:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.82 $** |
| P&L real total | 🔴 **-40.40 $** |
| P&L real hoy | -1.08 $ |
| P&L real 7 días | -10.69 $ |
| Fees pagados (real) | 14.41 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6026.14 $ |
| P&L sim compuesto | 🟢 +13031.36 $ (ficción Kelly: +51224% s/ operativo) |
| P&L sim hoy (2026-08-06) | 🟢 +0.44 $ |
| Operaciones resueltas | 77024 (47268 WIN / 29756 LOSS) — 61.4% |
| Señales abiertas | 331 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9308 | 62.9% | +0.129 | ➡️ estable | +4643.28$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11945 | 60.1% | +0.101 | ➡️ estable | +3862.77$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9205 | 58.3% | +0.083 | ➡️ estable | +3021.63$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3271 | 66.7% | +0.167 | ➡️ estable | +1703.59$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 3804 | 56.0% | +0.060 | 📈 madura (+0.08) | +541.86$ | 0.60$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 411 | 54.7% | +0.047 | 📉 agota (-0.18) | +94.91$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 95 | 80.0% | +0.294 | 📈 madura (+0.11) | +63.55$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 278 | 81.3% | +0.311 | ➡️ estable | +60.61$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1414 | 48.2% | -0.018 | ➡️ estable | +34.94$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 366 | 41.8% | -0.082 | 📈 madura (+0.09) | +24.52$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| ORDER_FLOW_5M | 1712 | 51.3% | +0.013 | ➡️ estable | +13.76$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 36 | 72.2% | +0.211 | ➡️ estable | +6.85$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 571 | 80.2% | +0.301 | 📉 agota (-0.04) | -0.44$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 15 | 40.0% | -0.066 | — | -1.16$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 74 | 91.9% | +0.408 | 📉 agota (-0.05) | -3.11$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 235 | 79.1% | +0.289 | 📉 agota (-0.04) | -5.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 86 | 83.7% | +0.330 | 📈 madura (+0.04) | -15.31$ | 2.00$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1658 | 55.5% | +0.055 | 📉 agota (-0.15) | -34.13$ | 0.55$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1458 | 71.7% | +0.216 | 📉 agota (-0.06) | -86.26$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 1111 | 46.8% | -0.032 | 📉 agota (-0.22) | -92.56$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 19583 | 62.4% | +0.124 | 📉 agota (-0.06) | -427.72$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7731 | 70.2% | +0.202 | ➡️ estable | -508.34$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-06T01:08 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:08 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:08 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.80$ |
| 2026-08-06T01:08 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - August 5, 8:45PM-9:00PM ET… | ❌ LOSS | -1.53$ |
| 2026-08-06T01:08 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - August 5, 8:45PM-9:00PM ET… | ✅ WIN | +1.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-06T01:07 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,529.81 | 0.2min |  |
| ✅ ETH | $1,907.11 | 0.2min |  |
| ✅ SOL | $73.95 | 0.2min |  |
| ✅ XRP | $1.06 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,539.70 | consenso |  |
| ETH | $1,907.11 | consenso |  |
| SOL | $73.95 | consenso |  |
| XRP | $1.06 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*