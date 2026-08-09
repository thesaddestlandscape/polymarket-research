# Estado del bot — 2026-08-09 05:27 UTC

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
| P&L fiel (stake fijo 1$) | +6013.64 $ |
| P&L sim compuesto | 🟢 +14114.59 $ (ficción Kelly: +55482% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +54.68 $ |
| Operaciones resueltas | 96654 (59222 WIN / 37432 LOSS) — 61.3% |
| Señales abiertas | 739 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10474 | 62.4% | +0.124 | ➡️ estable | +5197.64$ | 1.24$ | ✅ activa |
| GBM_LATE_15M | 12977 | 60.2% | +0.102 | ➡️ estable | +4378.68$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9965 | 58.9% | +0.089 | ➡️ estable | +3532.81$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3512 | 66.3% | +0.163 | ➡️ estable | +1803.21$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4004 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.54$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 657 | 71.7% | +0.216 | ➡️ estable | +493.77$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1519 | 48.5% | -0.015 | ➡️ estable | +37.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 824 | 64.3% | +0.143 | 📈 madura (+0.06) | +30.44$ | 1.43$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 518 | 52.9% | +0.029 | ➡️ estable | +4.14$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 106 | 51.9% | +0.019 | 📈 madura (+0.05) | -0.02$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 124 | 93.5% | +0.429 | 📈 madura (+0.06) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 100 | 52.0% | +0.020 | 📈 madura (+0.04) | -4.32$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 626 | 80.2% | +0.301 | 📉 agota (-0.04) | -4.45$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 67 | 31.3% | -0.181 | 📈 madura (+0.08) | -13.28$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 118 | 87.3% | +0.367 | 📈 madura (+0.11) | -14.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 312 | 77.6% | +0.274 | 📉 agota (-0.10) | -17.44$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1805 | 54.7% | +0.047 | 📉 agota (-0.16) | -21.35$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2473 | 69.8% | +0.198 | 📉 agota (-0.06) | -179.27$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 2417 | 42.9% | -0.071 | 📉 agota (-0.05) | -534.58$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26236 | 61.9% | +0.119 | 📉 agota (-0.05) | -652.62$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11657 | 69.7% | +0.197 | ➡️ estable | -887.34$ | 1.97$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T05:26 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T05:26 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | Solana Up or Down - August 9, 1:00AM-1:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-09T05:26 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - August 9, 1:00AM-1:15AM ET… | ✅ WIN | +0.57$ |
| 2026-08-09T05:26 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - August 9, 1:00AM-1:15AM ET… | ✅ WIN | +0.57$ |
| 2026-08-09T05:26 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - August 9, 1:00AM-1:15AM ET… | ✅ WIN | +0.42$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T05:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,726.46 | 0.1min |  |
| ✅ ETH | $1,913.21 | 0.1min |  |
| ✅ SOL | $75.97 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,730.50 | consenso |  |
| ETH | $1,913.21 | consenso |  |
| SOL | $75.94 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*