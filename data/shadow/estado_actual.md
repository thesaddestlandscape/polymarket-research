# Estado del bot — 2026-08-09 20:34 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.06 $** |
| P&L real total | 🔴 **-41.16 $** |
| P&L real hoy | -1.16 $ |
| P&L real 7 días | -11.53 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6025.32 $ |
| P&L sim compuesto | 🟢 +14288.75 $ (ficción Kelly: +56166% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +228.84 $ |
| Operaciones resueltas | 100432 (61586 WIN / 38846 LOSS) — 61.3% |
| Señales abiertas | 865 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10731 | 62.2% | +0.122 | ➡️ estable | +5252.76$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13168 | 60.2% | +0.102 | ➡️ estable | +4419.27$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10072 | 59.0% | +0.090 | 📈 madura (+0.03) | +3634.57$ | 0.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3524 | 66.3% | +0.163 | ➡️ estable | +1807.14$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 734 | 72.2% | +0.221 | 📈 madura (+0.05) | +592.67$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4011 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.98$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 708 | 77.5% | +0.275 | 📈 madura (+0.17) | +309.93$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 437 | 55.1% | +0.051 | 📉 agota (-0.13) | +98.04$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 140 | 76.4% | +0.261 | 📉 agota (-0.04) | +76.28$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 309 | 80.6% | +0.304 | ➡️ estable | +60.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1556 | 48.8% | -0.012 | 📈 madura (+0.03) | +44.73$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1106 | 63.7% | +0.137 | 📈 madura (+0.03) | +26.82$ | 1.37$ | ✅ activa |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 399 | 42.4% | -0.076 | 📈 madura (+0.12) | +15.41$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 326 | 55.5% | +0.055 | 📉 agota (-0.14) | +13.14$ | 0.55$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 635 | 52.8% | +0.027 | ➡️ estable | +7.59$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 123 | 53.7% | +0.036 | 📈 madura (+0.09) | +7.38$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 116 | 55.2% | +0.051 | 📈 madura (+0.10) | +3.21$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 133 | 94.0% | +0.433 | 📈 madura (+0.06) | -0.27$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 41 | 24.4% | -0.244 | 📉 agota (-0.10) | -8.76$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 634 | 80.0% | +0.299 | 📉 agota (-0.03) | -8.96$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 95 | 41.1% | -0.088 | 📈 madura (+0.05) | -10.79$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 70 | 30.0% | -0.194 | ➡️ estable | -14.81$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1830 | 54.8% | +0.047 | 📉 agota (-0.16) | -16.59$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 125 | 86.4% | +0.358 | 📈 madura (+0.08) | -17.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 325 | 77.2% | +0.271 | 📉 agota (-0.07) | -20.58$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 342 | 32.5% | -0.174 | ➡️ estable | -58.67$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2658 | 70.0% | +0.200 | 📉 agota (-0.05) | -179.13$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2654 | 42.5% | -0.075 | 📉 agota (-0.03) | -608.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 27561 | 61.9% | +0.119 | 📉 agota (-0.04) | -694.64$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12437 | 69.9% | +0.199 | ➡️ estable | -932.20$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T20:33 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T20:33 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.26$ |
| 2026-08-09T20:33 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T20:33 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.28$ |
| 2026-08-09T20:33 | FAVORITO_CONFIRMADO#DOGE#5min | … | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T20:31 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,060.00 | 0.2min |  |
| ✅ ETH | $1,918.45 | 0.2min |  |
| ✅ SOL | $77.22 | 0.2min |  |
| ✅ XRP | $1.04 | 0.2min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,092.07 | consenso |  |
| ETH | $1,919.03 | consenso |  |
| SOL | $77.16 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*