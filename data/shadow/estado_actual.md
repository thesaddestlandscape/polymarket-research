# Estado del bot — 2026-08-05 16:35 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.90 $** |
| P&L real total | 🔴 **-39.32 $** |
| P&L real hoy | -4.57 $ |
| P&L real 7 días | -9.67 $ |
| Fees pagados (real) | 14.38 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6009.28 $ |
| P&L sim compuesto | 🟢 +12875.67 $ (ficción Kelly: +50612% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +524.27 $ |
| Operaciones resueltas | 74963 (46026 WIN / 28937 LOSS) — 61.4% |
| Señales abiertas | 361 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9175 | 62.9% | +0.129 | ➡️ estable | +4593.04$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11785 | 60.1% | +0.101 | ➡️ estable | +3826.03$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9102 | 58.2% | +0.082 | ➡️ estable | +2960.97$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3204 | 66.8% | +0.167 | ➡️ estable | +1668.99$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 3752 | 55.9% | +0.059 | 📈 madura (+0.07) | +527.17$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 409 | 54.5% | +0.045 | 📉 agota (-0.18) | +93.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 274 | 81.8% | +0.315 | ➡️ estable | +62.36$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 90 | 78.9% | +0.283 | 📈 madura (+0.11) | +54.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1385 | 47.9% | -0.021 | ➡️ estable | +25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| GBM_LATE_60M | 360 | 40.8% | -0.091 | 📈 madura (+0.08) | +14.58$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1710 | 51.2% | +0.012 | ➡️ estable | +12.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 564 | 80.3% | +0.302 | 📉 agota (-0.03) | +0.09$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 71 | 91.5% | +0.404 | 📉 agota (-0.05) | -3.40$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 222 | 79.3% | +0.290 | 📉 agota (-0.04) | -4.99$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 82 | 84.1% | +0.333 | 📈 madura (+0.07) | -13.67$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1641 | 55.6% | +0.056 | 📉 agota (-0.15) | -32.21$ | 0.56$ | ✅ activa |
| BALLENAS_TARDIAS | 897 | 51.1% | +0.011 | 📉 agota (-0.25) | -52.81$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1355 | 72.3% | +0.223 | 📉 agota (-0.05) | -83.01$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 18882 | 62.4% | +0.124 | 📉 agota (-0.06) | -431.26$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7331 | 70.2% | +0.202 | ➡️ estable | -473.05$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T16:34 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.39$ |
| 2026-08-05T16:34 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.28$ |
| 2026-08-05T16:34 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.41$ |
| 2026-08-05T16:34 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.41$ |
| 2026-08-05T16:34 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T16:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,690.64 | 0.1min |  |
| ✅ ETH | $1,895.06 | 0.1min |  |
| ✅ SOL | $74.38 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,690.90 | consenso |  |
| ETH | $1,895.06 | consenso |  |
| SOL | $74.36 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*