# Estado del bot — 2026-09-13 10:04 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |
| Fees pagados (real) | 19.70 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +13142.17 $ |
| P&L sim compuesto | 🟢 +55411.20 $ (ficción Kelly: +217811% s/ operativo) |
| P&L sim hoy (2026-09-13) | 🟢 +827.99 $ |
| Operaciones resueltas | 526220 (300282 WIN / 225938 LOSS) — 57.1% |
| Señales abiertas | 244430 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_TARDIO | 27262 | 64.2% | +0.142 | 📈 madura (+0.06) | +15883.20$ | 1.72$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 28362 | 59.3% | +0.093 | ➡️ estable | +14179.39$ | 0.74$ | ✅ activa |
| GBM_LATE_15M | 30042 | 58.4% | +0.084 | 📉 agota (-0.03) | +12005.17$ | 0.73$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 14773 | 67.0% | +0.170 | ➡️ estable | +10613.71$ | 1.69$ | ✅ activa |
| CANDIDATA10_CONFIRMACION_CRUZADA | 10204 | 45.1% | -0.049 | 📈 madura (+0.06) | +4335.91$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_TARDIO | 11629 | 51.3% | +0.013 | 📉 agota (-0.11) | +3538.95$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 7139 | 60.1% | +0.100 | 📈 madura (+0.07) | +2799.28$ | 1.35$ | ✅ activa |
| UPDOWN_GBM | 25612 | 53.2% | +0.032 | ➡️ estable | +1682.29$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 3929 | 61.4% | +0.114 | 📈 madura (+0.07) | +1422.27$ | 1.21$ | ✅ activa |
| MOMENTUM_IBS_5M_BALLENA | 50820 | 42.7% | -0.073 | ➡️ estable | +1047.59$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M_BALLENA | 19376 | 48.5% | -0.015 | 📈 madura (+0.05) | +918.34$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 1737 | 80.1% | +0.300 | 📈 madura (+0.03) | +866.50$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 753 | 78.6% | +0.285 | ➡️ estable | +586.68$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 1119 | 55.4% | +0.054 | 📈 madura (+0.13) | +356.72$ | 0.54$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 1513 | 58.0% | +0.080 | 📈 madura (+0.04) | +326.16$ | 0.98$ | ✅ activa |
| ORDER_FLOW_5M | 2515 | 54.7% | +0.047 | 📈 madura (+0.07) | +309.38$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 16708 | 62.4% | +0.124 | ➡️ estable | +288.97$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 661 | 82.5% | +0.324 | 📈 madura (+0.04) | +159.21$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 161 | 89.4% | +0.390 | 📈 madura (+0.09) | +110.48$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 516 | 55.8% | +0.058 | ➡️ estable | +92.90$ | 0.57$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2801 | 56.0% | +0.060 | 📉 agota (-0.08) | +70.74$ | 0.78$ | ✅ activa |
| STREAK_MOM_5M | 6227 | 51.8% | +0.018 | ➡️ estable | +58.71$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 670 | 54.5% | +0.045 | ➡️ estable | +25.84$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 450 | 47.6% | -0.024 | ➡️ estable | +19.94$ | 2.00$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 118 | 54.2% | +0.042 | 📈 madura (+0.10) | +8.10$ | 0.57$ | ✅ activa |
| STREAK_FADE_60M | 48 | 52.1% | +0.020 | 📈 madura (+0.19) | +0.80$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 590 | 94.2% | +0.441 | ➡️ estable | -1.44$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_5M | 3186 | 50.4% | +0.004 | ➡️ estable | -3.65$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 516 | 93.0% | +0.429 | ➡️ estable | -9.17$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 421 | 40.1% | -0.098 | 📈 madura (+0.05) | -14.07$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 5653 | 51.4% | +0.014 | ➡️ estable | -18.86$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1172 | 78.9% | +0.289 | ➡️ estable | -19.69$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 831 | 45.6% | -0.044 | 📉 agota (-0.07) | -22.96$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 1583 | 48.3% | -0.017 | 📈 madura (+0.07) | -30.06$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 472 | 28.0% | -0.219 | ➡️ estable | -34.47$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 278 | 21.6% | -0.282 | 📈 madura (+0.06) | -36.90$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 762 | 56.6% | +0.065 | 📉 agota (-0.10) | -44.32$ | 0.66$ | ✅ activa |
| LIQUIDACIONES_15M | 388 | 40.2% | -0.097 | 📈 madura (+0.04) | -44.91$ | 0.50$ | ⚠️ IC negativo |
| CANDIDATA9_BOT_CONSENSO | 342 | 39.8% | -0.102 | 📉 agota (-0.22) | -63.16$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 1270 | 78.2% | +0.281 | 📉 agota (-0.03) | -78.87$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_15M_FADE | 4064 | 46.9% | -0.031 | 📈 madura (+0.03) | -93.71$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 2730 | 48.0% | -0.020 | ➡️ estable | -110.42$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_5M_FADE | 6616 | 48.0% | -0.020 | 📉 agota (-0.07) | -116.56$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 1067 | 36.4% | -0.136 | 📈 madura (+0.06) | -148.93$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M | 11988 | 48.9% | -0.011 | ➡️ estable | -171.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_DEPTH_FASE0 | 23541 | 59.8% | +0.098 | ➡️ estable | -757.94$ | 0.98$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12532 | 69.0% | +0.190 | ➡️ estable | -885.10$ | 1.83$ | ✅ activa |
| BALLENAS_TARDIAS | 26437 | 40.7% | -0.093 | 📉 agota (-0.03) | -4028.43$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 54398 | 69.4% | +0.194 | ➡️ estable | -4631.76$ | 1.92$ | ✅ activa |
| FAVORITO_CONFIRMADO | 100209 | 61.1% | +0.111 | ➡️ estable | -4915.45$ | 1.13$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-09-13T10:03 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.12$ |
| 2026-09-13T10:03 | BALLENAS_TARDIAS#BNB#5min | … | ✅ WIN | +2.55$ |
| 2026-09-13T10:03 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.24$ |
| 2026-09-13T10:03 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.23$ |
| 2026-09-13T10:03 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-09-13T10:04 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $76,761.49 | 0.1min |  |
| ✅ ETH | $2,483.18 | 0.1min |  |
| ✅ SOL | $99.83 | 0.1min |  |
| ✅ XRP | $1.34 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $76,763.80 | consenso |  |
| ETH | $2,483.53 | consenso |  |
| SOL | $99.83 | consenso |  |
| XRP | $1.34 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*