# Estado del bot — 2026-10-10 05:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 90.71 $ |
| Balance on-chain | **24.58 $** |
| P&L real total | 🔴 **-66.13 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +2.59 $ |
| Fees pagados (real) | 26.35 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +35640.06 $ |
| P&L sim compuesto | 🟢 +115381.46 $ (ficción Kelly: +453543% s/ operativo) |
| P&L sim hoy (2026-10-10) | 🟢 +439.83 $ |
| Operaciones resueltas | 941584 (538214 WIN / 403370 LOSS) — 57.2% |
| Señales abiertas | 198073 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_TARDIO | 45310 | 66.2% | +0.162 | ➡️ estable (últ. 1000) | +31106.78$ | 1.82$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 48201 | 59.5% | +0.095 | ➡️ estable (últ. 1000) | +25456.40$ | 0.87$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 28654 | 67.7% | +0.177 | 📉 agota (-0.04) (últ. 1000) | +22533.44$ | 1.76$ | ✅ activa |
| GBM_LATE_15M | 47862 | 59.3% | +0.093 | ➡️ estable (últ. 1000) | +21931.70$ | 0.90$ | ✅ activa |
| GBM_LATE_5M | 11857 | 65.7% | +0.157 | ➡️ estable (últ. 1000) | +7211.27$ | 1.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 20975 | 50.7% | +0.007 | 📉 agota (-0.04) (últ. 1000) | +6039.87$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 68744 | 55.0% | +0.050 | 📈 madura (+0.05) (últ. 1000) | +6001.14$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 8086 | 63.5% | +0.135 | ➡️ estable (últ. 1000) | +3854.42$ | 1.40$ | ✅ activa |
| CANDIDATA10_CONFIRMACION_CRUZADA | 28537 | 48.2% | -0.018 | ➡️ estable (últ. 1000) | +3664.18$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M_BALLENA | 41349 | 49.8% | -0.002 | 📉 agota (-0.03) (últ. 1000) | +1978.13$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_5M_BALLENA | 103579 | 42.6% | -0.074 | ➡️ estable (últ. 1000) | +1699.65$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 3109 | 80.6% | +0.306 | ➡️ estable (últ. 1000) | +1529.10$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 1335 | 78.9% | +0.288 | ➡️ estable (últ. 1000) | +1083.88$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 2731 | 56.9% | +0.069 | ➡️ estable (últ. 1000) | +958.20$ | 0.69$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 3271 | 59.1% | +0.091 | 📉 agota (-0.05) (últ. 1000) | +756.66$ | 1.00$ | ✅ activa |
| ORDER_FLOW_5M | 3063 | 56.5% | +0.065 | ➡️ estable (últ. 1000) | +595.21$ | 1.23$ | ✅ activa |
| RESOLUTION_SNIPER | 406 | 89.7% | +0.395 | ➡️ estable | +373.66$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1025 | 85.0% | +0.349 | 📈 madura (+0.07) (últ. 1000) | +325.24$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 1232 | 58.8% | +0.088 | 📈 madura (+0.07) (últ. 1000) | +316.83$ | 0.88$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 29472 | 61.8% | +0.118 | 📉 agota (-0.03) (últ. 1000) | +242.21$ | 1.17$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 3354 | 56.8% | +0.068 | ➡️ estable (últ. 1000) | +145.44$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 536 | 52.2% | +0.022 | 📈 madura (+0.13) | +113.01$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 10496 | 51.6% | +0.016 | ➡️ estable (últ. 1000) | +77.59$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_DEPTH_FASE0 | 5861 | 48.0% | -0.020 | 📉 agota (-0.10) (últ. 1000) | +76.20$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 360 | 49.7% | -0.003 | 📉 agota (-0.07) | +65.33$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 3311 | 51.3% | +0.013 | 📉 agota (-0.04) (últ. 1000) | +58.89$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 959 | 54.5% | +0.045 | ➡️ estable | +54.91$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 225 | 52.9% | +0.029 | ➡️ estable | +5.93$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 836 | 94.3% | +0.442 | 📈 madura (+0.03) | +4.61$ | 2.00$ | ✅ activa |
| 0.5000 | 1 | 0.0% | -0.008 | — | +0.00$ | 0.90$ | ⏳ acumulando |
| MOMENTUM_IBS_5M | 3357 | 50.4% | +0.004 | ➡️ estable (últ. 1000) | -3.35$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 93 | 45.2% | -0.047 | 📉 agota (-0.13) | -8.86$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1828 | 79.1% | +0.291 | ➡️ estable (últ. 1000) | -12.51$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 497 | 25.6% | -0.243 | 📈 madura (+0.08) | -20.42$ | 0.00$ | 🚫 desactivada |
| ORDER_FLOW_5M_REACTIVO | 1075 | 48.1% | -0.019 | 📈 madura (+0.08) (últ. 1000) | -21.28$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 1502 | 46.0% | -0.040 | ➡️ estable (últ. 1000) | -23.89$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 795 | 42.8% | -0.072 | 📈 madura (+0.07) | -32.80$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 997 | 92.8% | +0.427 | ➡️ estable | -33.81$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 500 | 42.4% | -0.076 | 📈 madura (+0.08) | -40.68$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 958 | 29.7% | -0.202 | 📈 madura (+0.04) | -42.04$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 9199 | 51.3% | +0.013 | ➡️ estable (últ. 1000) | -46.51$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1417 | 56.9% | +0.069 | ➡️ estable (últ. 1000) | -66.26$ | 0.69$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 1462 | 74.3% | +0.242 | 📉 agota (-0.09) (últ. 1000) | -101.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 3746 | 48.0% | -0.020 | ➡️ estable (últ. 1000) | -142.98$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M_FADE | 6285 | 44.1% | -0.059 | 📈 madura (+0.06) (últ. 1000) | -144.80$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 1162 | 36.1% | -0.138 | ➡️ estable (últ. 1000) | -154.14$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_5M_FADE | 8456 | 46.8% | -0.032 | ➡️ estable (últ. 1000) | -173.09$ | 0.50$ | ⚠️ IC negativo |
| CANDIDATA9_BOT_CONSENSO | 1488 | 39.8% | -0.102 | ➡️ estable (últ. 1000) | -189.14$ | 0.50$ | ⚠️ IC negativo |
| MOMENTUM_IBS_15M | 14666 | 48.8% | -0.012 | ➡️ estable (últ. 1000) | -217.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_DEPTH_FASE0 | 51186 | 60.0% | +0.100 | ➡️ estable (últ. 1000) | -1282.53$ | 1.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 21679 | 69.5% | +0.195 | ➡️ estable (últ. 1000) | -1383.95$ | 1.94$ | ✅ activa |
| BALLENAS_TARDIAS | 41060 | 42.1% | -0.079 | 📉 agota (-0.07) (últ. 1000) | -5534.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 86936 | 69.9% | +0.199 | ➡️ estable (últ. 1000) | -6546.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 156474 | 61.2% | +0.112 | ➡️ estable (últ. 1000) | -6642.18$ | 1.14$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-10-10T04:58 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.21$ |
| 2026-10-10T04:58 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.26$ |
| 2026-10-10T04:58 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-10-10T04:58 | FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | … | ✅ WIN | +0.77$ |
| 2026-10-10T04:58 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +2.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-10-10T05:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $82,614.26 | 0.1min |  |
| ✅ ETH | $2,492.66 | 0.1min |  |
| ✅ SOL | $109.77 | 0.1min |  |
| ✅ XRP | $1.41 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $82,614.26 | consenso |  |
| ETH | $2,492.91 | consenso |  |
| SOL | $109.77 | consenso |  |
| XRP | $1.41 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*