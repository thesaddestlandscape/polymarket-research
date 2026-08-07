# Estado del bot — 2026-08-07 12:47 UTC

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
| P&L fiel (stake fijo 1$) | +5958.80 $ |
| P&L sim compuesto | 🟢 +13642.97 $ (ficción Kelly: +53628% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +170.42 $ |
| Operaciones resueltas | 86195 (52699 WIN / 33496 LOSS) — 61.1% |
| Señales abiertas | 402 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9757 | 62.8% | +0.128 | ➡️ estable | +4946.70$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12441 | 60.1% | +0.101 | ➡️ estable | +4128.84$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9616 | 58.5% | +0.085 | ➡️ estable | +3252.44$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3468 | 66.5% | +0.165 | ➡️ estable | +1803.74$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 3974 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.98$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 378 | 69.8% | +0.197 | 📉 agota (-0.03) | +263.12$ | 1.97$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1495 | 48.4% | -0.016 | 📈 madura (+0.03) | +39.46$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 50 | 66.0% | +0.154 | 📉 agota (-0.04) | +4.97$ | 1.54$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 57 | 50.9% | +0.008 | 📈 madura (+0.15) | -0.92$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 233 | 51.5% | +0.015 | 📉 agota (-0.04) | -0.95$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 68 | 48.5% | -0.014 | ➡️ estable | -1.30$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 96 | 92.7% | +0.418 | ➡️ estable | -2.50$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 57 | 36.8% | -0.127 | ➡️ estable | -8.73$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 102 | 86.3% | +0.356 | 📈 madura (+0.04) | -13.68$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 277 | 77.6% | +0.274 | 📉 agota (-0.08) | -15.81$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 78 | 14.1% | -0.350 | ➡️ estable | -21.57$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1725 | 54.7% | +0.047 | 📉 agota (-0.16) | -40.65$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 281 | 32.7% | -0.171 | ➡️ estable | -49.89$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1937 | 70.0% | +0.200 | 📉 agota (-0.06) | -144.71$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 1699 | 42.5% | -0.075 | 📉 agota (-0.17) | -253.89$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22690 | 62.0% | +0.120 | 📉 agota (-0.06) | -546.60$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9563 | 69.6% | +0.196 | ➡️ estable | -710.52$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T12:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T12:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T12:46 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T12:46 | FAVORITO_CONFIRMADO#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T12:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.37$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T12:44 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,147.00 | 0.1min |  |
| ✅ ETH | $1,928.93 | 0.1min |  |
| ✅ SOL | $73.77 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,111.30 | consenso |  |
| ETH | $1,928.12 | consenso |  |
| SOL | $73.74 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*