# Estado del bot — 2026-08-09 09:23 UTC

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
| P&L fiel (stake fijo 1$) | +6062.57 $ |
| P&L sim compuesto | 🟢 +14199.51 $ (ficción Kelly: +55816% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +139.60 $ |
| Operaciones resueltas | 97653 (59867 WIN / 37786 LOSS) — 61.3% |
| Señales abiertas | 794 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10527 | 62.4% | +0.124 | ➡️ estable | +5228.10$ | 1.23$ | ✅ activa |
| GBM_LATE_15M | 13024 | 60.2% | +0.102 | ➡️ estable | +4398.25$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9998 | 58.9% | +0.089 | 📈 madura (+0.03) | +3582.10$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3515 | 66.3% | +0.163 | ➡️ estable | +1805.97$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4007 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.28$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 681 | 71.8% | +0.217 | ➡️ estable | +533.16$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 137 | 75.9% | +0.255 | 📉 agota (-0.04) | +73.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 307 | 80.5% | +0.303 | ➡️ estable | +59.68$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1531 | 48.7% | -0.013 | 📈 madura (+0.04) | +41.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 903 | 63.8% | +0.138 | 📈 madura (+0.03) | +24.31$ | 1.38$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| STRUCT_NO_15M | 547 | 53.0% | +0.030 | ➡️ estable | +4.99$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 111 | 52.3% | +0.022 | 📈 madura (+0.06) | -0.14$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 126 | 93.7% | +0.430 | 📈 madura (+0.06) | -1.09$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 102 | 52.9% | +0.029 | 📈 madura (+0.08) | -1.88$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 628 | 79.9% | +0.298 | 📉 agota (-0.04) | -8.53$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 67 | 31.3% | -0.181 | 📈 madura (+0.08) | -13.28$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 123 | 86.2% | +0.356 | 📈 madura (+0.08) | -17.70$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 317 | 77.3% | +0.271 | 📉 agota (-0.10) | -20.45$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1810 | 54.8% | +0.047 | 📉 agota (-0.17) | -22.34$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2524 | 69.9% | +0.199 | 📉 agota (-0.06) | -175.85$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 2498 | 43.2% | -0.068 | 📉 agota (-0.04) | -554.68$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26587 | 61.9% | +0.119 | 📉 agota (-0.05) | -683.37$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11861 | 69.8% | +0.198 | ➡️ estable | -882.81$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T09:22 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.24$ |
| 2026-08-09T09:22 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.37$ |
| 2026-08-09T09:22 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T09:22 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.84$ |
| 2026-08-09T09:22 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.62$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T09:20 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,775.96 | 0.1min |  |
| ✅ ETH | $1,913.75 | 0.1min |  |
| ✅ SOL | $76.37 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,775.96 | consenso |  |
| ETH | $1,913.75 | consenso |  |
| SOL | $76.39 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*