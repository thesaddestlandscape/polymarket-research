# Estado del bot — 2026-08-12 17:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.26 $** |
| P&L real total | 🔴 **-41.96 $** |
| P&L real hoy | -1.91 $ |
| P&L real 7 días | -7.21 $ |
| Fees pagados (real) | 15.41 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5958.65 $ |
| P&L sim compuesto | 🟢 +15539.69 $ (ficción Kelly: +61084% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +284.04 $ |
| Operaciones resueltas | 119968 (73520 WIN / 46448 LOSS) — 61.3% |
| Señales abiertas | 551 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11908 | 61.4% | +0.114 | ➡️ estable | +5717.45$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14128 | 60.2% | +0.102 | ➡️ estable | +4848.77$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10768 | 59.8% | +0.097 | 📈 madura (+0.06) | +4253.16$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3821 | 64.7% | +0.147 | ➡️ estable | +1811.08$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1337 | 72.7% | +0.227 | ➡️ estable | +1159.95$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4402 | 55.6% | +0.056 | 📈 madura (+0.05) | +579.16$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 549 | 55.2% | +0.052 | 📉 agota (-0.05) | +107.59$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 178 | 75.8% | +0.256 | 📉 agota (-0.05) | +84.23$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1790 | 50.0% | +0.000 | 📈 madura (+0.08) | +66.63$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2452 | 62.7% | +0.127 | ➡️ estable | +34.98$ | 1.27$ | ✅ activa |
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
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 399 | 77.9% | +0.278 | 📉 agota (-0.07) | -18.62$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 124 | 34.7% | -0.151 | 📈 madura (+0.08) | -20.78$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 696 | 78.9% | +0.288 | ➡️ estable | -25.07$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 360 | 46.7% | -0.033 | ➡️ estable | -26.07$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 217 | 37.8% | -0.121 | 📉 agota (-0.04) | -32.49$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 405 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.62$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 374 | 31.3% | -0.186 | 📉 agota (-0.06) | -68.14$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3479 | 70.0% | +0.200 | ➡️ estable | -207.75$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4356 | 46.5% | -0.035 | 📈 madura (+0.08) | -725.84$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33596 | 61.5% | +0.115 | ➡️ estable | -1097.57$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15989 | 69.7% | +0.197 | ➡️ estable | -1259.78$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T17:09 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-12T17:09 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - August 12, 12:50PM-12:55PM ET… | ✅ WIN | +0.83$ |
| 2026-08-12T17:09 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.57$ |
| 2026-08-12T17:09 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.26$ |
| 2026-08-12T17:09 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T17:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,450.00 | 0.1min |  |
| ✅ ETH | $1,888.94 | 0.1min |  |
| ✅ SOL | $75.71 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,450.00 | consenso |  |
| ETH | $1,889.00 | consenso |  |
| SOL | $75.71 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*