# Estado del bot — 2026-08-19 10:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |
| Fees pagados (real) | 15.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5556.82 $ |
| P&L sim compuesto | 🟢 +19017.52 $ (ficción Kelly: +74754% s/ operativo) |
| P&L sim hoy (2026-08-19) | 🟢 +848.39 $ |
| Operaciones resueltas | 182255 (109064 WIN / 73191 LOSS) — 59.8% |
| Señales abiertas | 1482 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 15434 | 59.8% | +0.098 | 📉 agota (-0.05) | +6788.13$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 13577 | 61.0% | +0.110 | 📈 madura (+0.09) | +5848.31$ | 1.68$ | ✅ activa |
| GBM_LATE_15M | 17068 | 59.7% | +0.097 | ➡️ estable | +5837.67$ | 0.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 3808 | 67.9% | +0.178 | 📉 agota (-0.06) | +2567.30$ | 1.74$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 5263 | 59.1% | +0.091 | 📉 agota (-0.13) | +2283.58$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 6689 | 54.8% | +0.048 | ➡️ estable | +762.86$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 933 | 78.6% | +0.285 | 📈 madura (+0.09) | +382.06$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 2258 | 52.3% | +0.023 | 📈 madura (+0.09) | +243.76$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 1041 | 55.5% | +0.055 | ➡️ estable | +175.13$ | 0.57$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5434 | 63.4% | +0.134 | ➡️ estable | +154.97$ | 1.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 266 | 77.1% | +0.269 | ➡️ estable | +153.34$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_5M_BALLENA | 3219 | 44.0% | -0.060 | 📈 madura (+0.03) | +126.98$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 500 | 45.4% | -0.046 | 📈 madura (+0.14) | +72.07$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1871 | 52.3% | +0.023 | 📈 madura (+0.03) | +65.51$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 398 | 79.9% | +0.297 | ➡️ estable | +62.37$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_15M | 869 | 53.9% | +0.038 | ➡️ estable | +45.16$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 400 | 54.0% | +0.040 | ➡️ estable | +36.76$ | 1.45$ | ✅ activa |
| MOMENTUM_IBS_5M_FADE | 2752 | 51.7% | +0.017 | ➡️ estable | +24.84$ | 0.50$ | ✅ activa |
| MOMENTUM_IBS_15M_BALLENA | 1150 | 46.3% | -0.037 | 📉 agota (-0.05) | +19.03$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 364 | 54.1% | +0.041 | 📉 agota (-0.11) | +8.58$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 49 | 75.5% | +0.245 | 📉 agota (-0.07) | +6.70$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 311 | 54.0% | +0.040 | 📈 madura (+0.03) | +5.51$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 555 | 80.0% | +0.299 | 📈 madura (+0.05) | +3.10$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 2066 | 51.9% | +0.019 | ➡️ estable | +2.38$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2194 | 54.8% | +0.048 | 📉 agota (-0.16) | +1.57$ | 0.50$ | ✅ activa |
| MOMENTUM_IBS_5M | 970 | 50.1% | +0.001 | 📉 agota (-0.08) | +0.48$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 42 | 50.0% | +0.000 | 📉 agota (-0.13) | +0.24$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 15 | 40.0% | -0.066 | — | -1.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 401 | 44.6% | -0.053 | 📉 agota (-0.11) | -3.88$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 306 | 49.3% | -0.006 | 📉 agota (-0.05) | -7.62$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 218 | 36.2% | -0.136 | 📉 agota (-0.06) | -7.98$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 264 | 92.0% | +0.417 | 📉 agota (-0.04) | -12.60$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 231 | 90.9% | +0.406 | 📈 madura (+0.08) | -12.96$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| MOMENTUM_IBS_15M_FADE | 399 | 44.4% | -0.056 | 📈 madura (+0.07) | -24.07$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 114 | 22.8% | -0.267 | 📈 madura (+0.07) | -24.37$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 1143 | 49.5% | -0.005 | 📈 madura (+0.06) | -27.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 847 | 79.1% | +0.290 | 📉 agota (-0.03) | -30.05$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 847 | 48.6% | -0.014 | ➡️ estable | -32.44$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 239 | 37.2% | -0.127 | 📈 madura (+0.04) | -33.17$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 193 | 19.2% | -0.305 | 📈 madura (+0.11) | -34.48$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 257 | 38.5% | -0.114 | 📈 madura (+0.04) | -37.23$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 758 | 37.5% | -0.125 | 📈 madura (+0.12) | -98.03$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5438 | 67.5% | +0.174 | 📉 agota (-0.05) | -486.53$ | 1.58$ | ✅ activa |
| BALLENAS_TARDIAS | 9065 | 42.8% | -0.072 | 📉 agota (-0.08) | -1448.73$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 24277 | 69.3% | +0.192 | ➡️ estable | -2099.79$ | 1.82$ | ✅ activa |
| FAVORITO_CONFIRMADO | 47733 | 60.9% | +0.109 | ➡️ estable | -2223.89$ | 1.13$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-19T09:58 | STREAK_FADE_5M#DOGE#5min | Dogecoin Up or Down - August 19, 5:45AM-5:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-19T09:58 | STREAK_MOM_5M#DOGE#5min | Dogecoin Up or Down - August 19, 5:45AM-5:50AM ET… | ✅ WIN | +0.49$ |
| 2026-08-19T09:58 | MOMENTUM_IBS_5M_FADE#BNB#5min | BNB Up or Down - August 19, 5:45AM-5:50AM ET… | ✅ WIN | +0.55$ |
| 2026-08-19T09:58 | MOMENTUM_IBS_5M_FADE#DOGE#5min | Dogecoin Up or Down - August 19, 5:45AM-5:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-19T09:58 | MOMENTUM_IBS_5M_FADE#BTC#5min | Bitcoin Up or Down - August 19, 5:45AM-5:50AM ET… | ✅ WIN | +0.48$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-19T10:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,353.43 | 0.1min |  |
| ✅ ETH | $1,916.70 | 0.1min |  |
| ✅ SOL | $77.19 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,365.20 | consenso |  |
| ETH | $1,916.70 | consenso |  |
| SOL | $77.19 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*