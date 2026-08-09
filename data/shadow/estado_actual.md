# Estado del bot — 2026-08-09 00:13 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.44 $** |
| P&L real total | 🔴 **-40.78 $** |
| P&L real hoy | -0.77 $ |
| P&L real 7 días | -11.14 $ |
| Fees pagados (real) | 14.97 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5990.74 $ |
| P&L sim compuesto | 🟢 +14036.73 $ (ficción Kelly: +55176% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🔴 -23.18 $ |
| Operaciones resueltas | 95316 (58385 WIN / 36931 LOSS) — 61.3% |
| Señales abiertas | 672 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10381 | 62.4% | +0.124 | ➡️ estable | +5116.57$ | 1.24$ | ✅ activa |
| GBM_LATE_15M | 12901 | 60.2% | +0.102 | ➡️ estable | +4334.96$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9906 | 58.8% | +0.088 | ➡️ estable | +3499.35$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3511 | 66.3% | +0.163 | ➡️ estable | +1805.25$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4003 | 56.0% | +0.060 | 📈 madura (+0.07) | +564.93$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 605 | 72.2% | +0.222 | ➡️ estable | +472.08$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1517 | 48.5% | -0.015 | ➡️ estable | +38.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 723 | 63.8% | +0.137 | 📈 madura (+0.06) | +23.74$ | 1.37$ | ✅ activa |
| GBM_LATE_60M | 396 | 42.2% | -0.078 | 📈 madura (+0.11) | +16.21$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| STRUCT_NO_15M | 485 | 53.4% | +0.034 | 📈 madura (+0.03) | +7.83$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 99 | 54.5% | +0.045 | 📈 madura (+0.14) | +5.48$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 96 | 53.1% | +0.031 | ➡️ estable | -1.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 121 | 93.4% | +0.427 | 📈 madura (+0.07) | -1.75$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 621 | 80.2% | +0.301 | 📉 agota (-0.03) | -3.69$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 62 | 30.6% | -0.188 | 📈 madura (+0.03) | -12.68$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 117 | 87.2% | +0.366 | 📈 madura (+0.12) | -14.19$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 307 | 77.9% | +0.277 | 📉 agota (-0.10) | -14.55$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1794 | 54.6% | +0.046 | 📉 agota (-0.16) | -27.37$ | 0.50$ | ✅ activa |
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2407 | 69.9% | +0.199 | 📉 agota (-0.06) | -171.16$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 2329 | 42.6% | -0.074 | 📉 agota (-0.07) | -503.55$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 25770 | 61.9% | +0.119 | 📉 agota (-0.04) | -615.81$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11400 | 69.6% | +0.196 | ➡️ estable | -868.69$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T00:13 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.31$ |
| 2026-08-09T00:13 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T00:13 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T00:13 | FAVORITO_CONFIRMADO#ETH#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T00:13 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - August 8, 7:45PM-8:00PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T00:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,904.44 | 0.1min |  |
| ✅ ETH | $1,915.06 | 0.1min |  |
| ✅ SOL | $76.00 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,904.44 | consenso |  |
| ETH | $1,915.06 | consenso |  |
| SOL | $75.92 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*