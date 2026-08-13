# Estado del bot — 2026-08-13 08:05 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **5.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6058.30 $ |
| P&L sim compuesto | 🟢 +16023.51 $ (ficción Kelly: +62986% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +283.72 $ |
| Operaciones resueltas | 124853 (76517 WIN / 48336 LOSS) — 61.3% |
| Señales abiertas | 434 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12246 | 61.4% | +0.114 | ➡️ estable | +5850.62$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 14412 | 60.2% | +0.102 | ➡️ estable | +4945.26$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11027 | 60.0% | +0.100 | 📈 madura (+0.07) | +4458.00$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3954 | 64.1% | +0.141 | 📉 agota (-0.03) | +1810.58$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1574 | 72.4% | +0.223 | ➡️ estable | +1345.72$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4549 | 55.6% | +0.056 | 📈 madura (+0.05) | +587.03$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 640 | 55.0% | +0.050 | ➡️ estable | +101.88$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1876 | 50.4% | +0.004 | 📈 madura (+0.07) | +86.30$ | 0.76$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1740 | 51.5% | +0.015 | ➡️ estable | +18.47$ | 0.59$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2738 | 62.2% | +0.122 | ➡️ estable | +17.08$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 234 | 54.7% | +0.047 | 📈 madura (+0.05) | +6.45$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 169 | 94.1% | +0.436 | ➡️ estable | -0.21$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1152 | 51.2% | +0.012 | 📉 agota (-0.03) | -7.08$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2018 | 54.5% | +0.045 | 📉 agota (-0.18) | -13.20$ | 0.50$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 390 | 47.9% | -0.020 | 📈 madura (+0.04) | -18.39$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 713 | 79.0% | +0.289 | 📉 agota (-0.03) | -23.36$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 384 | 31.8% | -0.181 | 📉 agota (-0.05) | -67.33$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3657 | 70.1% | +0.201 | ➡️ estable | -210.21$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4802 | 47.0% | -0.030 | 📈 madura (+0.08) | -738.52$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34897 | 61.4% | +0.114 | ➡️ estable | -1191.16$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16774 | 69.8% | +0.197 | ➡️ estable | -1320.25$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T08:04 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T08:04 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.77$ |
| 2026-08-13T08:04 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-13T08:04 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.39$ |
| 2026-08-13T08:04 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T08:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,803.12 | 0.2min |  |
| ✅ ETH | $1,893.87 | 0.2min |  |
| ✅ SOL | $76.49 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,803.12 | consenso |  |
| ETH | $1,894.00 | consenso |  |
| SOL | $76.37 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*