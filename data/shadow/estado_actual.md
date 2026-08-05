# Estado del bot — 2026-08-05 16:46 UTC

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
| P&L fiel (stake fijo 1$) | +6019.96 $ |
| P&L sim compuesto | 🟢 +12898.34 $ (ficción Kelly: +50701% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +546.94 $ |
| Operaciones resueltas | 75006 (46059 WIN / 28947 LOSS) — 61.4% |
| Señales abiertas | 366 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9179 | 62.9% | +0.129 | ➡️ estable | +4594.94$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11790 | 60.1% | +0.101 | ➡️ estable | +3826.48$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9105 | 58.2% | +0.082 | ➡️ estable | +2966.11$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3207 | 66.8% | +0.167 | ➡️ estable | +1671.76$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 3753 | 56.0% | +0.060 | 📈 madura (+0.07) | +529.17$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 409 | 54.5% | +0.045 | 📉 agota (-0.18) | +93.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 275 | 81.8% | +0.316 | 📈 madura (+0.03) | +63.37$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 91 | 79.1% | +0.285 | 📈 madura (+0.11) | +56.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1386 | 48.0% | -0.020 | ➡️ estable | +26.95$ | 0.50$ | ⚠️ IC negativo |
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
| BALLENAS_TARDIAS | 900 | 51.0% | +0.010 | 📉 agota (-0.25) | -54.83$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1359 | 72.4% | +0.224 | 📉 agota (-0.05) | -81.43$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 18893 | 62.4% | +0.124 | 📉 agota (-0.06) | -427.29$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7337 | 70.2% | +0.202 | ➡️ estable | -470.66$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T16:45 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T16:45 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T16:45 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.80$ |
| 2026-08-05T16:45 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T16:45 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T16:43 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,656.64 | 0.1min |  |
| ✅ ETH | $1,892.09 | 0.1min |  |
| ✅ SOL | $74.38 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,674.40 | consenso |  |
| ETH | $1,892.85 | consenso |  |
| SOL | $74.32 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*