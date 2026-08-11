# Estado del bot — 2026-08-11 18:38 UTC

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
| P&L fiel (stake fijo 1$) | +6113.74 $ |
| P&L sim compuesto | 🟢 +15282.29 $ (ficción Kelly: +60072% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +114.17 $ |
| Operaciones resueltas | 112802 (69279 WIN / 43523 LOSS) — 61.4% |
| Señales abiertas | 634 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11450 | 61.8% | +0.118 | ➡️ estable | +5614.78$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 13741 | 60.3% | +0.103 | ➡️ estable | +4708.36$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10481 | 59.5% | +0.095 | 📈 madura (+0.05) | +4001.09$ | 1.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3619 | 65.8% | +0.158 | ➡️ estable | +1815.33$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1097 | 74.4% | +0.243 | 📈 madura (+0.06) | +999.14$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4130 | 55.8% | +0.058 | 📈 madura (+0.06) | +557.79$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 465 | 54.8% | +0.048 | 📉 agota (-0.13) | +100.95$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1695 | 49.9% | -0.001 | 📈 madura (+0.07) | +63.60$ | 0.96$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2014 | 62.9% | +0.128 | ➡️ estable | +30.22$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1731 | 51.4% | +0.014 | ➡️ estable | +15.29$ | 0.53$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 899 | 52.3% | +0.023 | ➡️ estable | +5.95$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1927 | 55.1% | +0.051 | 📉 agota (-0.16) | +5.50$ | 0.71$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 200 | 53.5% | +0.035 | ➡️ estable | +1.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 170 | 50.6% | +0.006 | ➡️ estable | -4.53$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 671 | 79.4% | +0.293 | ➡️ estable | -16.20$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 115 | 35.7% | -0.141 | 📈 madura (+0.08) | -18.06$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 373 | 77.7% | +0.276 | 📉 agota (-0.08) | -18.91$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 289 | 47.4% | -0.026 | 📈 madura (+0.09) | -21.17$ | 1.14$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 165 | 39.4% | -0.105 | ➡️ estable | -22.76$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 141 | 18.4% | -0.311 | 📈 madura (+0.08) | -28.60$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 363 | 42.7% | -0.073 | 📉 agota (-0.11) | -34.21$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 354 | 31.9% | -0.180 | ➡️ estable | -62.07$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3205 | 70.2% | +0.202 | ➡️ estable | -188.65$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3767 | 45.8% | -0.042 | 📈 madura (+0.10) | -688.02$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31598 | 61.7% | +0.117 | ➡️ estable | -884.73$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14771 | 69.8% | +0.198 | ➡️ estable | -1131.02$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T18:36 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.03$ |
| 2026-08-11T18:36 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T18:36 | LIQUIDACIONES_5M#BTC#5min | Bitcoin Up or Down - August 11, 2:10PM-2:15PM ET… | ✅ WIN | +0.48$ |
| 2026-08-11T18:36 | GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | BNB Up or Down - August 11, 2:00PM-2:15PM ET… | ✅ WIN | +1.96$ |
| 2026-08-11T18:36 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 11, 2:00PM-2:15PM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T18:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,514.86 | 0.2min |  |
| ✅ ETH | $1,863.69 | 0.2min |  |
| ✅ SOL | $75.23 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,527.40 | consenso |  |
| ETH | $1,863.93 | consenso |  |
| SOL | $75.22 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*