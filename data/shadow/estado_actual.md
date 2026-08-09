# Estado del bot — 2026-08-09 23:45 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.06 $** |
| P&L real total | 🔴 **-41.16 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.45 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6048.12 $ |
| P&L sim compuesto | 🟢 +14371.88 $ (ficción Kelly: +56493% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +311.97 $ |
| Operaciones resueltas | 101297 (62135 WIN / 39162 LOSS) — 61.3% |
| Señales abiertas | 873 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10797 | 62.1% | +0.121 | ➡️ estable | +5272.76$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13224 | 60.2% | +0.102 | ➡️ estable | +4446.66$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10105 | 59.1% | +0.091 | 📈 madura (+0.04) | +3672.91$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3530 | 66.2% | +0.162 | ➡️ estable | +1807.42$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 771 | 72.6% | +0.226 | 📈 madura (+0.06) | +644.80$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4012 | 55.9% | +0.059 | 📈 madura (+0.07) | +562.26$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 708 | 77.5% | +0.275 | 📈 madura (+0.17) | +309.93$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 141 | 76.6% | +0.262 | 📉 agota (-0.04) | +76.61$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 310 | 80.6% | +0.304 | ➡️ estable | +60.89$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1561 | 48.8% | -0.012 | 📈 madura (+0.03) | +42.36$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1166 | 64.0% | +0.140 | 📈 madura (+0.03) | +32.73$ | 1.40$ | ✅ activa |
| GBM_LATE_60M | 400 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.72$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 659 | 52.8% | +0.028 | ➡️ estable | +9.64$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 127 | 52.8% | +0.027 | 📈 madura (+0.10) | +4.67$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 120 | 55.0% | +0.049 | 📈 madura (+0.10) | +3.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 134 | 94.0% | +0.434 | 📈 madura (+0.06) | -0.10$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 41 | 24.4% | -0.244 | 📉 agota (-0.10) | -8.76$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 635 | 79.8% | +0.297 | 📉 agota (-0.04) | -11.00$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 103 | 41.7% | -0.081 | 📈 madura (+0.09) | -11.06$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 70 | 30.0% | -0.194 | ➡️ estable | -14.81$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1836 | 54.7% | +0.047 | 📉 agota (-0.16) | -17.07$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 127 | 86.6% | +0.360 | 📈 madura (+0.11) | -17.26$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 329 | 76.9% | +0.267 | 📉 agota (-0.08) | -24.01$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 343 | 32.4% | -0.175 | 📉 agota (-0.03) | -59.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2695 | 70.1% | +0.201 | 📉 agota (-0.04) | -175.77$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2717 | 42.4% | -0.076 | ➡️ estable | -641.48$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 27844 | 61.9% | +0.119 | 📉 agota (-0.04) | -704.73$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12594 | 69.9% | +0.199 | ➡️ estable | -942.80$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T23:44 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T23:44 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.84$ |
| 2026-08-09T23:44 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.71$ |
| 2026-08-09T23:44 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.54$ |
| 2026-08-09T23:44 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.71$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T23:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,826.96 | 0.2min |  |
| ✅ ETH | $1,909.61 | 0.2min |  |
| ✅ SOL | $76.30 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,831.30 | consenso |  |
| ETH | $1,910.00 | consenso |  |
| SOL | $76.30 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*