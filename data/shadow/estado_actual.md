# Estado del bot — 2026-08-07 11:36 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.94 $** |
| P&L real total | 🔴 **-42.28 $** |
| P&L real hoy | -0.36 $ |
| P&L real 7 días | -8.27 $ |
| Fees pagados (real) | 14.60 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5957.22 $ |
| P&L sim compuesto | 🟢 +13616.01 $ (ficción Kelly: +53522% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +143.45 $ |
| Operaciones resueltas | 85861 (52488 WIN / 33373 LOSS) — 61.1% |
| Señales abiertas | 387 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9733 | 62.8% | +0.128 | ➡️ estable | +4943.20$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12420 | 60.1% | +0.101 | ➡️ estable | +4126.68$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9604 | 58.5% | +0.085 | ➡️ estable | +3246.21$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3462 | 66.5% | +0.165 | ➡️ estable | +1801.36$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 3968 | 55.9% | +0.059 | 📈 madura (+0.07) | +555.56$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 368 | 69.8% | +0.197 | 📉 agota (-0.04) | +258.44$ | 1.97$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 124 | 76.6% | +0.262 | 📉 agota (-0.05) | +69.56$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 298 | 80.9% | +0.307 | ➡️ estable | +59.80$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1494 | 48.4% | -0.016 | 📈 madura (+0.03) | +39.18$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30 | 66.7% | +0.156 | 📉 agota (-0.12) | +3.88$ | 1.56$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 218 | 51.8% | +0.018 | ➡️ estable | -0.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 66 | 50.0% | +0.000 | 📈 madura (+0.09) | -0.28$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 57 | 50.9% | +0.008 | 📈 madura (+0.15) | -0.92$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 94 | 92.6% | +0.417 | ➡️ estable | -2.77$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 57 | 36.8% | -0.127 | ➡️ estable | -8.73$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 100 | 86.0% | +0.353 | 📈 madura (+0.04) | -13.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 275 | 77.5% | +0.273 | 📉 agota (-0.08) | -17.11$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 75 | 14.7% | -0.344 | ➡️ estable | -20.04$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1721 | 54.6% | +0.046 | 📉 agota (-0.16) | -43.28$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 273 | 32.6% | -0.173 | ➡️ estable | -48.80$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1923 | 69.8% | +0.198 | 📉 agota (-0.06) | -147.53$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 1674 | 42.4% | -0.076 | 📉 agota (-0.18) | -255.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22592 | 62.0% | +0.120 | 📉 agota (-0.06) | -535.91$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9507 | 69.6% | +0.196 | ➡️ estable | -711.41$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T11:35 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.29$ |
| 2026-08-07T11:35 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.39$ |
| 2026-08-07T11:35 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.26$ |
| 2026-08-07T11:35 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.43$ |
| 2026-08-07T11:35 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T11:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,004.86 | 0.2min |  |
| ✅ ETH | $1,915.01 | 0.2min |  |
| ✅ SOL | $73.56 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,010.00 | consenso |  |
| ETH | $1,915.01 | consenso |  |
| SOL | $73.55 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*