# Estado del bot — 2026-08-10 04:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.06 $** |
| P&L real total | 🔴 **-41.16 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.45 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6167.96 $ |
| P&L sim compuesto | 🟢 +14641.96 $ (ficción Kelly: +57555% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +266.49 $ |
| Operaciones resueltas | 102576 (62998 WIN / 39578 LOSS) — 61.4% |
| Señales abiertas | 495 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10883 | 62.2% | +0.122 | ➡️ estable | +5317.00$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13292 | 60.2% | +0.102 | ➡️ estable | +4504.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10162 | 59.2% | +0.092 | 📈 madura (+0.04) | +3756.60$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3546 | 66.2% | +0.162 | ➡️ estable | +1808.75$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 819 | 73.6% | +0.236 | 📈 madura (+0.05) | +717.67$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4024 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.27$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 146 | 76.7% | +0.264 | 📉 agota (-0.05) | +77.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 314 | 80.9% | +0.307 | ➡️ estable | +63.74$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1582 | 48.7% | -0.013 | 📈 madura (+0.04) | +38.82$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1254 | 63.9% | +0.139 | ➡️ estable | +34.99$ | 1.39$ | ✅ activa |
| GBM_LATE_60M | 403 | 42.7% | -0.073 | 📈 madura (+0.12) | +20.59$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 687 | 53.3% | +0.033 | ➡️ estable | +13.60$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 132 | 52.3% | +0.022 | 📈 madura (+0.04) | +2.52$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 126 | 54.0% | +0.039 | 📈 madura (+0.06) | +2.25$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 136 | 94.1% | +0.435 | 📈 madura (+0.06) | +0.14$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1846 | 55.0% | +0.050 | 📉 agota (-0.16) | -8.62$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 74 | 33.8% | -0.158 | ➡️ estable | -12.99$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 640 | 79.7% | +0.296 | 📉 agota (-0.04) | -13.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 333 | 77.2% | +0.270 | 📉 agota (-0.08) | -21.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2739 | 70.1% | +0.201 | 📉 agota (-0.04) | -177.22$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2827 | 43.0% | -0.070 | ➡️ estable | -642.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28247 | 61.9% | +0.119 | 📉 agota (-0.03) | -699.63$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12823 | 69.9% | +0.199 | ➡️ estable | -948.27$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T04:15 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 10, 12:00AM-12:05AM ET… | ✅ WIN | +1.66$ |
| 2026-08-10T04:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.39$ |
| 2026-08-10T04:15 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.39$ |
| 2026-08-10T04:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-10T04:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T04:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,997.14 | 0.1min |  |
| ✅ ETH | $1,918.30 | 0.1min |  |
| ✅ SOL | $76.68 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,999.90 | consenso |  |
| ETH | $1,918.30 | consenso |  |
| SOL | $76.63 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*