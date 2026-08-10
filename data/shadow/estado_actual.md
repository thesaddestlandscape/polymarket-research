# Estado del bot — 2026-08-10 03:40 UTC

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
| P&L fiel (stake fijo 1$) | +6134.83 $ |
| P&L sim compuesto | 🟢 +14578.91 $ (ficción Kelly: +57307% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +203.43 $ |
| Operaciones resueltas | 102399 (62879 WIN / 39520 LOSS) — 61.4% |
| Señales abiertas | 485 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10872 | 62.2% | +0.122 | ➡️ estable | +5300.74$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13281 | 60.2% | +0.102 | ➡️ estable | +4489.46$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10152 | 59.2% | +0.092 | 📈 madura (+0.04) | +3735.27$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3544 | 66.2% | +0.162 | ➡️ estable | +1805.72$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 811 | 73.4% | +0.233 | 📈 madura (+0.05) | +694.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4024 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.27$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 708 | 77.5% | +0.275 | 📈 madura (+0.17) | +309.93$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 146 | 76.7% | +0.264 | 📉 agota (-0.05) | +77.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 314 | 80.9% | +0.307 | ➡️ estable | +63.74$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1578 | 48.7% | -0.013 | 📈 madura (+0.03) | +37.78$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1243 | 64.0% | +0.139 | ➡️ estable | +37.18$ | 1.39$ | ✅ activa |
| GBM_LATE_60M | 403 | 42.7% | -0.073 | 📈 madura (+0.12) | +20.59$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1724 | 51.3% | +0.013 | ➡️ estable | +14.94$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 683 | 53.0% | +0.030 | ➡️ estable | +11.36$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 131 | 52.7% | +0.026 | 📈 madura (+0.07) | +3.03$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 125 | 54.4% | +0.043 | 📈 madura (+0.08) | +2.76$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 136 | 94.1% | +0.435 | 📈 madura (+0.06) | +0.14$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 41 | 24.4% | -0.244 | 📉 agota (-0.10) | -8.76$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1845 | 55.0% | +0.050 | 📉 agota (-0.16) | -10.00$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 639 | 79.8% | +0.297 | 📉 agota (-0.04) | -11.26$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 74 | 33.8% | -0.158 | ➡️ estable | -12.99$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 333 | 77.2% | +0.270 | 📉 agota (-0.08) | -21.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2730 | 70.2% | +0.202 | 📉 agota (-0.04) | -173.16$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2814 | 42.9% | -0.071 | ➡️ estable | -640.76$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28196 | 61.9% | +0.119 | 📉 agota (-0.03) | -693.14$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12793 | 69.9% | +0.199 | ➡️ estable | -944.35$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T03:39 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 9, 11:25PM-11:30PM ET… | ❌ LOSS | -1.75$ |
| 2026-08-10T03:39 | UPDOWN_GBM_15M_TARDIO#BTC#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T03:39 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.84$ |
| 2026-08-10T03:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T03:39 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T03:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,986.24 | 0.1min |  |
| ✅ ETH | $1,916.77 | 0.1min |  |
| ✅ SOL | $76.82 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,986.24 | consenso |  |
| ETH | $1,917.22 | consenso |  |
| SOL | $76.66 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*