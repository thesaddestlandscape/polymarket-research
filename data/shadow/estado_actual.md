# Estado del bot — 2026-08-10 07:42 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.80 $** |
| P&L real total | 🔴 **-42.42 $** |
| P&L real hoy | -1.26 $ |
| P&L real 7 días | -10.71 $ |
| Fees pagados (real) | 15.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6169.21 $ |
| P&L sim compuesto | 🟢 +14701.80 $ (ficción Kelly: +57790% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +326.33 $ |
| Operaciones resueltas | 103510 (63585 WIN / 39925 LOSS) — 61.4% |
| Señales abiertas | 501 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10946 | 62.1% | +0.121 | ➡️ estable | +5329.21$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13344 | 60.2% | +0.102 | ➡️ estable | +4513.06$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10190 | 59.2% | +0.092 | 📈 madura (+0.04) | +3783.46$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3558 | 66.1% | +0.161 | ➡️ estable | +1813.01$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 838 | 73.7% | +0.237 | 📈 madura (+0.05) | +747.89$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4032 | 55.9% | +0.059 | 📈 madura (+0.07) | +556.96$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 149 | 76.5% | +0.262 | 📉 agota (-0.06) | +77.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 317 | 80.8% | +0.306 | ➡️ estable | +63.85$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1585 | 48.7% | -0.013 | 📈 madura (+0.03) | +36.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1318 | 63.1% | +0.131 | ➡️ estable | +20.69$ | 1.31$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 713 | 52.6% | +0.026 | ➡️ estable | +8.35$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 137 | 51.8% | +0.018 | 📈 madura (+0.06) | +0.98$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 141 | 93.6% | +0.430 | 📈 madura (+0.04) | -1.52$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1855 | 54.9% | +0.049 | 📉 agota (-0.16) | -12.80$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 644 | 79.7% | +0.296 | ➡️ estable | -13.97$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 130 | 86.9% | +0.364 | 📈 madura (+0.10) | -16.88$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 339 | 77.3% | +0.271 | 📉 agota (-0.09) | -21.06$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2789 | 70.2% | +0.202 | 📉 agota (-0.04) | -173.44$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2908 | 43.8% | -0.062 | 📈 madura (+0.03) | -628.59$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28544 | 61.9% | +0.119 | 📉 agota (-0.03) | -707.41$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13013 | 70.0% | +0.200 | ➡️ estable | -943.32$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T07:40 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.29$ |
| 2026-08-10T07:40 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-10T07:40 | BALLENAS_TARDIAS#DOGE#5min | … | ✅ WIN | +2.97$ |
| 2026-08-10T07:40 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 10, 3:15AM-3:30AM ET… | ✅ WIN | +1.96$ |
| 2026-08-10T07:40 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T07:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,270.81 | 0.1min |  |
| ✅ ETH | $1,928.38 | 0.1min |  |
| ✅ SOL | $77.07 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,274.70 | consenso |  |
| ETH | $1,928.80 | consenso |  |
| SOL | $77.01 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*