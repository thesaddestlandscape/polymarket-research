# Estado del bot — 2026-08-11 07:56 UTC

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
| P&L fiel (stake fijo 1$) | +6210.78 $ |
| P&L sim compuesto | 🟢 +15237.42 $ (ficción Kelly: +59896% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +69.30 $ |
| Operaciones resueltas | 109726 (67446 WIN / 42280 LOSS) — 61.5% |
| Señales abiertas | 570 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11292 | 61.9% | +0.119 | ➡️ estable | +5575.53$ | 0.63$ | ✅ activa |
| GBM_LATE_15M | 13616 | 60.3% | +0.103 | ➡️ estable | +4664.14$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10404 | 59.4% | +0.094 | 📈 madura (+0.05) | +3946.99$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3596 | 65.9% | +0.159 | ➡️ estable | +1816.88$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1028 | 74.9% | +0.249 | 📈 madura (+0.06) | +946.21$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4069 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.20$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 446 | 54.7% | +0.047 | 📉 agota (-0.13) | +98.58$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 159 | 76.7% | +0.264 | 📉 agota (-0.03) | +83.84$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 326 | 80.7% | +0.305 | ➡️ estable | +64.41$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1647 | 49.2% | -0.008 | 📈 madura (+0.05) | +43.85$ | 0.64$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1800 | 63.3% | +0.133 | ➡️ estable | +37.30$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 420 | 42.4% | -0.076 | 📈 madura (+0.09) | +19.21$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1728 | 51.4% | +0.014 | ➡️ estable | +16.96$ | 0.57$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 834 | 53.1% | +0.031 | ➡️ estable | +12.76$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 182 | 53.8% | +0.038 | ➡️ estable | +1.22$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 145 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.08$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 157 | 51.6% | +0.016 | ➡️ estable | -1.94$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 137 | 87.6% | +0.371 | 📈 madura (+0.10) | -15.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 660 | 79.5% | +0.295 | 📉 agota (-0.03) | -16.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 360 | 77.8% | +0.276 | 📉 agota (-0.08) | -17.28$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 87 | 31.0% | -0.185 | ➡️ estable | -17.69$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 142 | 38.7% | -0.111 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 253 | 45.1% | -0.049 | 📉 agota (-0.07) | -25.54$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 138 | 18.8% | -0.307 | 📈 madura (+0.08) | -27.07$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 327 | 43.4% | -0.065 | 📉 agota (-0.11) | -28.93$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3068 | 70.0% | +0.200 | ➡️ estable | -194.90$ | 1.97$ | ✅ activa |
| BALLENAS_TARDIAS | 3439 | 45.3% | -0.047 | 📈 madura (+0.06) | -652.74$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30685 | 61.7% | +0.117 | ➡️ estable | -830.03$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14197 | 69.9% | +0.199 | ➡️ estable | -1055.23$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T07:56 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.26$ |
| 2026-08-11T07:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.26$ |
| 2026-08-11T07:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.33$ |
| 2026-08-11T07:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T07:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.39$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T07:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,027.04 | 0.2min |  |
| ✅ ETH | $1,876.45 | 0.2min |  |
| ✅ SOL | $75.68 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,027.04 | consenso |  |
| ETH | $1,876.48 | consenso |  |
| SOL | $75.67 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*