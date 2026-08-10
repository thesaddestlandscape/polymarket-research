# Estado del bot — 2026-08-10 04:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.26 $** |
| P&L real total | 🔴 **-40.96 $** |
| P&L real hoy | +0.20 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6159.82 $ |
| P&L sim compuesto | 🟢 +14655.25 $ (ficción Kelly: +57607% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +279.77 $ |
| Operaciones resueltas | 102774 (63111 WIN / 39663 LOSS) — 61.4% |
| Señales abiertas | 495 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10900 | 62.2% | +0.122 | ➡️ estable | +5328.17$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13304 | 60.3% | +0.103 | ➡️ estable | +4513.71$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10173 | 59.2% | +0.092 | 📈 madura (+0.04) | +3769.19$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3548 | 66.2% | +0.162 | ➡️ estable | +1808.75$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 826 | 73.8% | +0.238 | 📈 madura (+0.05) | +731.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4026 | 55.9% | +0.059 | 📈 madura (+0.07) | +558.44$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 147 | 76.2% | +0.258 | 📉 agota (-0.06) | +75.38$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 315 | 80.6% | +0.304 | ➡️ estable | +61.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1584 | 48.7% | -0.013 | 📈 madura (+0.03) | +35.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1268 | 63.9% | +0.139 | ➡️ estable | +35.17$ | 1.39$ | ✅ activa |
| GBM_LATE_60M | 403 | 42.7% | -0.073 | 📈 madura (+0.12) | +20.59$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 692 | 53.2% | +0.032 | ➡️ estable | +13.05$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 132 | 52.3% | +0.022 | 📈 madura (+0.04) | +2.52$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 126 | 54.0% | +0.039 | 📈 madura (+0.06) | +2.25$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 137 | 94.2% | +0.435 | 📈 madura (+0.06) | +0.22$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1847 | 55.0% | +0.049 | 📉 agota (-0.16) | -10.15$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 641 | 79.7% | +0.296 | 📉 agota (-0.04) | -12.93$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 74 | 33.8% | -0.158 | ➡️ estable | -12.99$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 333 | 77.2% | +0.270 | 📉 agota (-0.08) | -21.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2748 | 70.1% | +0.201 | 📉 agota (-0.04) | -177.71$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2844 | 43.0% | -0.070 | ➡️ estable | -638.74$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28304 | 61.9% | +0.119 | 📉 agota (-0.03) | -711.51$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12861 | 69.9% | +0.199 | ➡️ estable | -961.74$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T04:57 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.41$ |
| 2026-08-10T04:57 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 10, 12:40AM-12:45AM ET… | ❌ LOSS | -1.75$ |
| 2026-08-10T04:57 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - August 10, 12:30AM-12:45AM ET… | ✅ WIN | +2.00$ |
| 2026-08-10T04:57 | GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | XRP Up or Down - August 10, 12:30AM-12:45AM ET… | ✅ WIN | +2.00$ |
| 2026-08-10T04:57 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - August 10, 12:30AM-12:45AM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T04:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,980.72 | 0.1min |  |
| ✅ ETH | $1,916.61 | 0.1min |  |
| ✅ SOL | $76.54 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,980.72 | consenso |  |
| ETH | $1,916.61 | consenso |  |
| SOL | $76.56 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*