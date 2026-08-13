# Estado del bot — 2026-08-13 05:41 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **7.08 $** |
| P&L real total | 🔴 **-44.14 $** |
| P&L real hoy | -1.07 $ |
| P&L real 7 días | -4.82 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6092.82 $ |
| P&L sim compuesto | 🟢 +16011.73 $ (ficción Kelly: +62939% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +271.94 $ |
| Operaciones resueltas | 124146 (76101 WIN / 48045 LOSS) — 61.3% |
| Señales abiertas | 409 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12192 | 61.4% | +0.114 | ➡️ estable | +5833.80$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 14369 | 60.2% | +0.102 | ➡️ estable | +4930.07$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10986 | 60.0% | +0.100 | 📈 madura (+0.07) | +4427.24$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3933 | 64.2% | +0.142 | ➡️ estable | +1814.46$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1539 | 72.6% | +0.226 | ➡️ estable | +1333.82$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4530 | 55.6% | +0.056 | 📈 madura (+0.05) | +582.81$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 626 | 55.3% | +0.053 | ➡️ estable | +106.48$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1867 | 50.4% | +0.004 | 📈 madura (+0.07) | +88.45$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1739 | 51.5% | +0.015 | ➡️ estable | +17.98$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 232 | 54.3% | +0.043 | 📈 madura (+0.03) | +5.06$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2699 | 61.9% | +0.119 | ➡️ estable | +4.33$ | 1.19$ | ✅ activa |
| LIQUIDACIONES_60M | 206 | 53.4% | +0.034 | ➡️ estable | +2.84$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1133 | 50.9% | +0.009 | 📉 agota (-0.03) | -10.18$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2014 | 54.5% | +0.045 | 📉 agota (-0.18) | -12.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 161 | 89.4% | +0.390 | 📈 madura (+0.11) | -13.05$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 378 | 47.6% | -0.024 | ➡️ estable | -17.92$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 411 | 77.9% | +0.277 | 📉 agota (-0.04) | -18.89$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 710 | 78.9% | +0.288 | 📉 agota (-0.03) | -24.43$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 158 | 20.3% | -0.294 | 📈 madura (+0.12) | -28.37$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 383 | 31.6% | -0.183 | 📉 agota (-0.06) | -67.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3633 | 70.1% | +0.201 | ➡️ estable | -210.01$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4749 | 47.1% | -0.029 | 📈 madura (+0.08) | -714.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34700 | 61.4% | +0.114 | ➡️ estable | -1171.64$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16667 | 69.8% | +0.198 | ➡️ estable | -1288.13$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T05:41 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T05:41 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T05:41 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.18$ |
| 2026-08-13T05:41 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-13T05:41 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.28$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T05:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,863.67 | 0.1min |  |
| ✅ ETH | $1,895.30 | 0.1min |  |
| ✅ SOL | $76.44 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,863.67 | consenso |  |
| ETH | $1,895.69 | consenso |  |
| SOL | $76.25 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*