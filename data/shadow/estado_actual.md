# Estado del bot — 2026-08-11 09:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.07 $** |
| P&L real total | 🔴 **-41.15 $** |
| P&L real hoy | -0.23 $ |
| P&L real 7 días | -11.98 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6211.24 $ |
| P&L sim compuesto | 🟢 +15275.30 $ (ficción Kelly: +60044% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +107.18 $ |
| Operaciones resueltas | 110298 (67784 WIN / 42514 LOSS) — 61.5% |
| Señales abiertas | 559 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11324 | 61.8% | +0.118 | ➡️ estable | +5588.42$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 13640 | 60.3% | +0.103 | ➡️ estable | +4688.48$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10419 | 59.5% | +0.095 | 📈 madura (+0.05) | +3967.91$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3602 | 65.9% | +0.158 | ➡️ estable | +1816.75$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1042 | 74.8% | +0.247 | 📈 madura (+0.06) | +968.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4077 | 55.9% | +0.059 | 📈 madura (+0.06) | +562.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 452 | 54.6% | +0.046 | 📉 agota (-0.13) | +98.56$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1654 | 49.3% | -0.007 | 📈 madura (+0.06) | +47.87$ | 0.70$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1838 | 63.2% | +0.132 | ➡️ estable | +33.30$ | 1.32$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 850 | 52.7% | +0.027 | ➡️ estable | +9.31$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 186 | 54.3% | +0.043 | ➡️ estable | +4.23$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 158 | 51.9% | +0.019 | ➡️ estable | -1.64$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 140 | 87.9% | +0.373 | 📈 madura (+0.10) | -15.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 362 | 77.9% | +0.277 | 📉 agota (-0.07) | -16.95$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 662 | 79.5% | +0.294 | 📉 agota (-0.03) | -17.44$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 88 | 30.7% | -0.189 | ➡️ estable | -18.20$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 144 | 38.9% | -0.110 | ➡️ estable | -20.02$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 259 | 45.2% | -0.048 | 📉 agota (-0.04) | -25.60$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 139 | 18.7% | -0.309 | 📈 madura (+0.08) | -27.58$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 333 | 43.5% | -0.064 | 📉 agota (-0.10) | -28.94$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3100 | 70.1% | +0.201 | ➡️ estable | -189.98$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3492 | 45.4% | -0.046 | 📈 madura (+0.06) | -661.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30854 | 61.7% | +0.117 | ➡️ estable | -859.31$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14310 | 69.9% | +0.199 | ➡️ estable | -1074.28$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T09:49 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T09:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T09:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T09:49 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T09:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T09:47 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,197.50 | 0.1min |  |
| ✅ ETH | $1,878.54 | 0.1min |  |
| ✅ SOL | $75.69 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,199.80 | consenso |  |
| ETH | $1,878.77 | consenso |  |
| SOL | $75.69 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*