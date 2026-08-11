# Estado del bot — 2026-08-11 09:06 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.16 $** |
| P&L real total | 🔴 **-40.06 $** |
| P&L real hoy | +0.86 $ |
| P&L real 7 días | -10.89 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6228.00 $ |
| P&L sim compuesto | 🟢 +15279.92 $ (ficción Kelly: +60063% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +111.80 $ |
| Operaciones resueltas | 110091 (67665 WIN / 42426 LOSS) — 61.5% |
| Señales abiertas | 551 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11311 | 61.8% | +0.118 | ➡️ estable | +5588.61$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 13630 | 60.3% | +0.103 | ➡️ estable | +4685.47$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10414 | 59.5% | +0.095 | 📈 madura (+0.05) | +3961.77$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3601 | 65.9% | +0.159 | ➡️ estable | +1817.82$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1034 | 74.9% | +0.248 | 📈 madura (+0.07) | +959.71$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4075 | 55.9% | +0.058 | 📈 madura (+0.06) | +561.24$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 451 | 54.5% | +0.045 | 📉 agota (-0.13) | +98.08$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1650 | 49.2% | -0.008 | 📈 madura (+0.05) | +42.65$ | 0.60$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1826 | 63.3% | +0.133 | ➡️ estable | +35.60$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 421 | 42.5% | -0.074 | 📈 madura (+0.10) | +28.86$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 841 | 52.9% | +0.029 | ➡️ estable | +11.05$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 185 | 54.1% | +0.040 | ➡️ estable | +3.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 147 | 93.9% | +0.433 | 📈 madura (+0.04) | -0.83$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 157 | 51.6% | +0.016 | ➡️ estable | -1.94$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 139 | 87.8% | +0.372 | 📈 madura (+0.10) | -15.63$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 362 | 77.9% | +0.277 | 📉 agota (-0.07) | -16.95$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 87 | 31.0% | -0.185 | ➡️ estable | -17.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 661 | 79.4% | +0.293 | 📉 agota (-0.04) | -18.27$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 143 | 39.2% | -0.107 | ➡️ estable | -19.51$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 256 | 45.3% | -0.047 | 📉 agota (-0.05) | -25.06$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 138 | 18.8% | -0.307 | 📈 madura (+0.08) | -27.07$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 330 | 43.3% | -0.066 | 📉 agota (-0.11) | -29.41$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3090 | 70.0% | +0.200 | ➡️ estable | -191.51$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 3477 | 45.4% | -0.046 | 📈 madura (+0.06) | -655.39$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30792 | 61.7% | +0.117 | ➡️ estable | -844.12$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14271 | 69.9% | +0.199 | ➡️ estable | -1066.79$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T09:05 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.31$ |
| 2026-08-11T09:05 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - August 11, 4:50AM-4:55AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-11T09:05 | STREAK_MOM_5M#SOL#5min | Solana Up or Down - August 11, 4:50AM-4:55AM ET… | ✅ WIN | +0.54$ |
| 2026-08-11T09:05 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 11, 4:50AM-4:55AM ET… | ✅ WIN | +1.36$ |
| 2026-08-11T09:05 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.37$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T09:03 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,067.37 | 0.1min |  |
| ✅ ETH | $1,877.16 | 0.1min |  |
| ✅ SOL | $75.91 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,072.80 | consenso |  |
| ETH | $1,877.16 | consenso |  |
| SOL | $75.81 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*