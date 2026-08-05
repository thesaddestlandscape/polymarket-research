# Estado del bot — 2026-08-05 21:50 UTC

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
| P&L fiel (stake fijo 1$) | +6036.72 $ |
| P&L sim compuesto | 🟢 +13008.76 $ (ficción Kelly: +51135% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +657.35 $ |
| Operaciones resueltas | 76189 (46785 WIN / 29404 LOSS) — 61.4% |
| Señales abiertas | 396 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9261 | 62.9% | +0.129 | ➡️ estable | +4630.93$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11889 | 60.1% | +0.101 | ➡️ estable | +3849.90$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9177 | 58.2% | +0.082 | ➡️ estable | +3000.54$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3247 | 66.7% | +0.167 | ➡️ estable | +1692.33$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 3784 | 56.0% | +0.060 | 📈 madura (+0.08) | +542.06$ | 0.60$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 409 | 54.5% | +0.045 | 📉 agota (-0.18) | +93.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 276 | 81.9% | +0.317 | ➡️ estable | +64.69$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 94 | 79.8% | +0.292 | 📈 madura (+0.10) | +61.71$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1408 | 48.2% | -0.018 | ➡️ estable | +32.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 364 | 41.5% | -0.085 | 📈 madura (+0.08) | +23.66$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1710 | 51.2% | +0.012 | ➡️ estable | +12.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 567 | 80.4% | +0.303 | 📉 agota (-0.03) | +2.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 11 | 72.7% | +0.106 | — | +1.50$ | 1.06$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 73 | 91.8% | +0.407 | 📉 agota (-0.05) | -3.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 229 | 79.0% | +0.288 | 📉 agota (-0.03) | -6.60$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 86 | 83.7% | +0.330 | 📈 madura (+0.04) | -15.31$ | 2.00$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1654 | 55.4% | +0.054 | 📉 agota (-0.15) | -39.72$ | 0.54$ | ✅ activa |
| BALLENAS_TARDIAS | 1027 | 48.0% | -0.020 | 📉 agota (-0.25) | -83.57$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1409 | 72.3% | +0.223 | 📉 agota (-0.05) | -84.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 19294 | 62.4% | +0.124 | 📉 agota (-0.06) | -417.72$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7554 | 70.3% | +0.203 | ➡️ estable | -479.41$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T21:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T21:49 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.31$ |
| 2026-08-05T21:49 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.74$ |
| 2026-08-05T21:49 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T21:49 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T21:47 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,613.49 | 0.2min |  |
| ✅ ETH | $1,906.45 | 0.2min |  |
| ✅ SOL | $74.06 | 0.2min |  |
| ✅ XRP | $1.06 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,613.49 | consenso |  |
| ETH | $1,906.45 | consenso |  |
| SOL | $74.06 | consenso |  |
| XRP | $1.06 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*