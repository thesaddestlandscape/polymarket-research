# Estado del bot — 2026-08-19 10:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |
| Fees pagados (real) | 15.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5562.56 $ |
| P&L sim compuesto | 🟢 +19042.06 $ (ficción Kelly: +74851% s/ operativo) |
| P&L sim hoy (2026-08-19) | 🟢 +872.93 $ |
| Operaciones resueltas | 182299 (109078 WIN / 73221 LOSS) — 59.8% |
| Señales abiertas | 1467 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 15439 | 59.8% | +0.098 | 📉 agota (-0.05) | +6834.31$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 13580 | 61.0% | +0.110 | 📈 madura (+0.09) | +5842.19$ | 1.67$ | ✅ activa |
| GBM_LATE_15M | 17073 | 59.7% | +0.097 | ➡️ estable | +5835.86$ | 0.84$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 3812 | 67.8% | +0.178 | 📉 agota (-0.06) | +2559.14$ | 1.74$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 5263 | 59.1% | +0.091 | 📉 agota (-0.13) | +2283.58$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 6689 | 54.8% | +0.048 | ➡️ estable | +762.86$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 933 | 78.6% | +0.285 | 📈 madura (+0.09) | +382.06$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 2258 | 52.3% | +0.023 | 📈 madura (+0.09) | +243.76$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 1042 | 55.5% | +0.055 | ➡️ estable | +173.60$ | 0.56$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5434 | 63.4% | +0.134 | ➡️ estable | +154.97$ | 1.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 266 | 77.1% | +0.269 | ➡️ estable | +153.34$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_5M_BALLENA | 3219 | 44.0% | -0.060 | 📈 madura (+0.03) | +126.98$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 500 | 45.4% | -0.046 | 📈 madura (+0.14) | +72.07$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1871 | 52.3% | +0.023 | 📈 madura (+0.03) | +65.51$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 398 | 79.9% | +0.297 | ➡️ estable | +62.37$ | 2.00$ | ✅ activa |
| MOMENTUM_IBS_15M | 875 | 53.7% | +0.037 | ➡️ estable | +42.98$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 400 | 54.0% | +0.040 | ➡️ estable | +36.76$ | 1.45$ | ✅ activa |
| MOMENTUM_IBS_5M_FADE | 2765 | 51.7% | +0.017 | ➡️ estable | +25.16$ | 0.50$ | ✅ activa |
| MOMENTUM_IBS_15M_BALLENA | 1151 | 46.2% | -0.038 | 📉 agota (-0.05) | +18.52$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 365 | 54.2% | +0.042 | 📉 agota (-0.11) | +9.03$ | 0.50$ | ✅ activa |
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
| STREAK_MOM_5M | 1146 | 49.4% | -0.006 | 📈 madura (+0.06) | -29.07$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 847 | 79.1% | +0.290 | 📉 agota (-0.03) | -30.05$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 848 | 48.7% | -0.013 | ➡️ estable | -31.95$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 239 | 37.2% | -0.127 | 📈 madura (+0.04) | -33.17$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 193 | 19.2% | -0.305 | 📈 madura (+0.11) | -34.48$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 257 | 38.5% | -0.114 | 📈 madura (+0.04) | -37.23$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 758 | 37.5% | -0.125 | 📈 madura (+0.12) | -98.03$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5439 | 67.4% | +0.174 | 📉 agota (-0.05) | -487.60$ | 1.58$ | ✅ activa |
| BALLENAS_TARDIAS | 9065 | 42.8% | -0.072 | 📉 agota (-0.08) | -1448.73$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 24277 | 69.3% | +0.192 | ➡️ estable | -2099.79$ | 1.82$ | ✅ activa |
| FAVORITO_CONFIRMADO | 47733 | 60.9% | +0.109 | ➡️ estable | -2223.89$ | 1.13$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-19T10:12 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - August 19, 6:00AM-6:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-19T10:12 | MOMENTUM_IBS_5M_FADE#BNB#5min | BNB Up or Down - August 19, 6:00AM-6:05AM ET… | ❌ LOSS | -0.58$ |
| 2026-08-19T10:12 | MOMENTUM_IBS_5M_FADE#SOL#5min | Solana Up or Down - August 19, 6:00AM-6:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-19T10:10 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - August 19, 5:45AM-6:00AM ET… | ✅ WIN | +0.45$ |
| 2026-08-19T10:10 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - August 19, 5:45AM-6:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-19T10:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,320.42 | 0.1min |  |
| ✅ ETH | $1,916.75 | 0.1min |  |
| ✅ SOL | $77.18 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,322.70 | consenso |  |
| ETH | $1,916.84 | consenso |  |
| SOL | $77.18 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*