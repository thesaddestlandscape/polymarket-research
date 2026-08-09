# Estado del bot — 2026-08-09 08:16 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.44 $** |
| P&L real total | 🔴 **-40.78 $** |
| P&L real hoy | -0.78 $ |
| P&L real 7 días | -11.15 $ |
| Fees pagados (real) | 14.97 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6035.81 $ |
| P&L sim compuesto | 🟢 +14162.55 $ (ficción Kelly: +55670% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +102.64 $ |
| Operaciones resueltas | 97371 (59700 WIN / 37671 LOSS) — 61.3% |
| Señales abiertas | 779 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10511 | 62.4% | +0.124 | ➡️ estable | +5212.39$ | 1.23$ | ✅ activa |
| GBM_LATE_15M | 13010 | 60.2% | +0.102 | ➡️ estable | +4385.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9988 | 58.9% | +0.089 | 📈 madura (+0.03) | +3553.96$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3512 | 66.3% | +0.163 | ➡️ estable | +1803.21$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4004 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.54$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 675 | 71.6% | +0.215 | ➡️ estable | +506.24$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1528 | 48.6% | -0.014 | 📈 madura (+0.04) | +40.72$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 877 | 63.7% | +0.137 | 📈 madura (+0.03) | +23.30$ | 1.37$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 539 | 52.9% | +0.029 | ➡️ estable | +4.13$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 109 | 53.2% | +0.032 | 📈 madura (+0.10) | +3.43$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 126 | 93.7% | +0.430 | 📈 madura (+0.06) | -1.09$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 102 | 52.9% | +0.029 | 📈 madura (+0.08) | -1.88$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 627 | 80.1% | +0.300 | 📉 agota (-0.04) | -6.49$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 67 | 31.3% | -0.181 | 📈 madura (+0.08) | -13.28$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 121 | 87.6% | +0.370 | 📈 madura (+0.11) | -13.62$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 315 | 77.8% | +0.276 | 📉 agota (-0.10) | -16.37$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1810 | 54.8% | +0.047 | 📉 agota (-0.17) | -22.34$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2511 | 69.9% | +0.199 | 📉 agota (-0.06) | -175.65$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 2476 | 43.3% | -0.067 | 📉 agota (-0.05) | -544.34$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26488 | 61.9% | +0.119 | 📉 agota (-0.05) | -662.22$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11812 | 69.8% | +0.198 | ➡️ estable | -879.52$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T08:14 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 9, 4:00AM-4:05AM ET… | ✅ WIN | +0.50$ |
| 2026-08-09T08:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.23$ |
| 2026-08-09T08:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.23$ |
| 2026-08-09T08:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.37$ |
| 2026-08-09T08:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T08:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,866.78 | 0.1min |  |
| ✅ ETH | $1,921.82 | 0.1min |  |
| ✅ SOL | $76.42 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,866.78 | consenso |  |
| ETH | $1,921.82 | consenso |  |
| SOL | $76.39 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*