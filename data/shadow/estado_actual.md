# Estado del bot — 2026-08-12 11:39 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.81 $** |
| P&L real total | 🔴 **-42.41 $** |
| P&L real hoy | -2.36 $ |
| P&L real 7 días | -7.66 $ |
| Fees pagados (real) | 15.39 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5926.88 $ |
| P&L sim compuesto | 🟢 +15369.23 $ (ficción Kelly: +60414% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +113.58 $ |
| Operaciones resueltas | 118061 (72375 WIN / 45686 LOSS) — 61.3% |
| Señales abiertas | 509 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11784 | 61.5% | +0.115 | ➡️ estable | +5697.86$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14014 | 60.2% | +0.102 | ➡️ estable | +4819.50$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10670 | 59.7% | +0.097 | 📈 madura (+0.06) | +4188.24$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3770 | 65.0% | +0.150 | ➡️ estable | +1823.00$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1245 | 72.6% | +0.226 | ➡️ estable | +1069.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4316 | 55.4% | +0.054 | 📈 madura (+0.05) | +553.89$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 513 | 54.4% | +0.044 | 📉 agota (-0.11) | +102.45$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 175 | 75.4% | +0.251 | 📉 agota (-0.05) | +79.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1763 | 49.9% | -0.001 | 📈 madura (+0.07) | +60.03$ | 0.73$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 340 | 80.0% | +0.298 | ➡️ estable | +58.13$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2345 | 62.6% | +0.126 | ➡️ estable | +27.48$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1734 | 51.4% | +0.014 | ➡️ estable | +17.65$ | 0.55$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 216 | 53.2% | +0.032 | ➡️ estable | +2.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 159 | 93.7% | +0.432 | ➡️ estable | -1.38$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1968 | 54.8% | +0.048 | 📉 agota (-0.17) | -3.33$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1035 | 51.5% | +0.015 | ➡️ estable | -3.53$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 188 | 51.1% | +0.011 | 📉 agota (-0.04) | -6.39$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 155 | 89.0% | +0.385 | 📈 madura (+0.11) | -13.64$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 394 | 77.9% | +0.278 | 📉 agota (-0.07) | -18.48$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 691 | 78.9% | +0.288 | ➡️ estable | -25.25$ | 1.98$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 198 | 37.9% | -0.120 | 📉 agota (-0.09) | -29.81$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 346 | 45.1% | -0.049 | 📉 agota (-0.05) | -31.23$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 370 | 31.6% | -0.183 | 📉 agota (-0.06) | -66.10$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3415 | 70.2% | +0.202 | ➡️ estable | -194.96$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4169 | 46.4% | -0.036 | 📈 madura (+0.09) | -720.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33104 | 61.5% | +0.115 | ➡️ estable | -1062.93$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15712 | 69.8% | +0.198 | ➡️ estable | -1232.64$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T11:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.26$ |
| 2026-08-12T11:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-12T11:39 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.62$ |
| 2026-08-12T11:39 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.62$ |
| 2026-08-12T11:39 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T11:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,101.60 | 0.2min |  |
| ✅ ETH | $1,910.39 | 0.2min |  |
| ✅ SOL | $76.68 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,101.60 | consenso |  |
| ETH | $1,910.83 | consenso |  |
| SOL | $76.68 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*