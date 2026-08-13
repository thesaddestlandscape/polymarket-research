# Estado del bot — 2026-08-13 06:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **7.08 $** |
| P&L real total | 🔴 **-44.14 $** |
| P&L real hoy | -1.07 $ |
| P&L real 7 días | -4.82 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6093.75 $ |
| P&L sim compuesto | 🟢 +16026.73 $ (ficción Kelly: +62998% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +286.93 $ |
| Operaciones resueltas | 124273 (76174 WIN / 48099 LOSS) — 61.3% |
| Señales abiertas | 412 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12207 | 61.4% | +0.114 | ➡️ estable | +5843.25$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14380 | 60.1% | +0.101 | ➡️ estable | +4928.92$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10995 | 60.0% | +0.100 | 📈 madura (+0.07) | +4433.25$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3939 | 64.1% | +0.141 | ➡️ estable | +1813.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1551 | 72.5% | +0.224 | ➡️ estable | +1338.29$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4535 | 55.6% | +0.056 | 📈 madura (+0.05) | +586.23$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 627 | 55.3% | +0.053 | ➡️ estable | +107.52$ | 0.55$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1871 | 50.4% | +0.004 | 📈 madura (+0.07) | +88.41$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1740 | 51.5% | +0.015 | ➡️ estable | +18.47$ | 0.59$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2702 | 62.0% | +0.120 | ➡️ estable | +6.36$ | 1.20$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 232 | 54.3% | +0.043 | 📈 madura (+0.03) | +5.06$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1139 | 50.9% | +0.009 | 📉 agota (-0.03) | -10.32$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2015 | 54.5% | +0.045 | 📉 agota (-0.18) | -12.11$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 161 | 89.4% | +0.390 | 📈 madura (+0.11) | -13.05$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 382 | 47.6% | -0.023 | ➡️ estable | -18.09$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 411 | 77.9% | +0.277 | 📉 agota (-0.04) | -18.89$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 711 | 78.9% | +0.288 | 📉 agota (-0.03) | -23.75$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 383 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3640 | 70.1% | +0.201 | ➡️ estable | -210.57$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4749 | 47.1% | -0.029 | 📈 madura (+0.08) | -714.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34726 | 61.4% | +0.114 | ➡️ estable | -1174.89$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16682 | 69.8% | +0.198 | ➡️ estable | -1294.71$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T06:11 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - August 13, 1:45AM-2:00AM ET… | ✅ WIN | +1.56$ |
| 2026-08-13T06:11 | GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | BNB Up or Down - August 13, 1:45AM-2:00AM ET… | ✅ WIN | +1.96$ |
| 2026-08-13T06:11 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 13, 1:45AM-2:00AM ET… | ✅ WIN | +1.96$ |
| 2026-08-13T06:11 | GBM_LATE_15M#BNB#15min | BNB Up or Down - August 13, 1:45AM-2:00AM ET… | ✅ WIN | +1.96$ |
| 2026-08-13T06:11 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 13, 1:50AM-1:55AM ET… | ✅ WIN | +2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T06:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,789.00 | 0.1min |  |
| ✅ ETH | $1,892.04 | 0.1min |  |
| ✅ SOL | $76.43 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,767.29 | consenso |  |
| ETH | $1,892.05 | consenso |  |
| SOL | $76.42 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*