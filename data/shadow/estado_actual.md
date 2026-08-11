# Estado del bot — 2026-08-11 08:25 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6202.30 $ |
| P&L sim compuesto | 🟢 +15236.55 $ (ficción Kelly: +59892% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +68.43 $ |
| Operaciones resueltas | 109895 (67542 WIN / 42353 LOSS) — 61.5% |
| Señales abiertas | 548 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11300 | 61.9% | +0.119 | ➡️ estable | +5576.26$ | 0.62$ | ✅ activa |
| GBM_LATE_15M | 13625 | 60.3% | +0.103 | ➡️ estable | +4666.57$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10410 | 59.5% | +0.095 | 📈 madura (+0.05) | +3951.46$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3599 | 65.9% | +0.159 | ➡️ estable | +1816.89$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1030 | 74.9% | +0.248 | 📈 madura (+0.06) | +947.17$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4073 | 55.9% | +0.059 | 📈 madura (+0.06) | +560.08$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 450 | 54.7% | +0.046 | 📉 agota (-0.13) | +98.59$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1649 | 49.2% | -0.008 | 📈 madura (+0.05) | +41.30$ | 0.58$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1810 | 63.4% | +0.134 | ➡️ estable | +39.81$ | 1.34$ | ✅ activa |
| GBM_LATE_60M | 421 | 42.5% | -0.074 | 📈 madura (+0.10) | +28.86$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 835 | 53.1% | +0.030 | ➡️ estable | +12.25$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 185 | 54.1% | +0.040 | ➡️ estable | +3.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 146 | 93.8% | +0.432 | 📈 madura (+0.04) | -0.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 157 | 51.6% | +0.016 | ➡️ estable | -1.94$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 139 | 87.8% | +0.372 | 📈 madura (+0.10) | -15.63$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 660 | 79.5% | +0.295 | 📉 agota (-0.03) | -16.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 362 | 77.9% | +0.277 | 📉 agota (-0.07) | -16.95$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 87 | 31.0% | -0.185 | ➡️ estable | -17.69$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 142 | 38.7% | -0.111 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 254 | 45.3% | -0.047 | 📉 agota (-0.05) | -25.04$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 138 | 18.8% | -0.307 | 📈 madura (+0.08) | -27.07$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 328 | 43.3% | -0.067 | 📉 agota (-0.12) | -29.44$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3077 | 70.0% | +0.200 | ➡️ estable | -194.58$ | 1.97$ | ✅ activa |
| BALLENAS_TARDIAS | 3459 | 45.3% | -0.047 | 📈 madura (+0.06) | -655.99$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30732 | 61.7% | +0.117 | ➡️ estable | -837.58$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14225 | 69.9% | +0.199 | ➡️ estable | -1062.83$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T08:24 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T08:24 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T08:24 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.80$ |
| 2026-08-11T08:24 | ORDER_FLOW_5M#ETH#5min | Ethereum Up or Down - August 11, 4:05AM-4:10AM ET… | ✅ WIN | +1.33$ |
| 2026-08-11T08:24 | UPDOWN_GBM#XRP#5min | XRP Up or Down - August 11, 4:05AM-4:10AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T08:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,997.96 | 0.1min |  |
| ✅ ETH | $1,874.79 | 0.1min |  |
| ✅ SOL | $75.60 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,999.90 | consenso |  |
| ETH | $1,874.79 | consenso |  |
| SOL | $75.60 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*