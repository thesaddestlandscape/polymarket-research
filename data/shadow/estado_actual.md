# Estado del bot — 2026-08-06 01:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.82 $** |
| P&L real total | 🔴 **-40.40 $** |
| P&L real hoy | -1.08 $ |
| P&L real 7 días | -10.69 $ |
| Fees pagados (real) | 14.41 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6026.06 $ |
| P&L sim compuesto | 🟢 +13045.56 $ (ficción Kelly: +51280% s/ operativo) |
| P&L sim hoy (2026-08-06) | 🟢 +14.65 $ |
| Operaciones resueltas | 77119 (47319 WIN / 29800 LOSS) — 61.4% |
| Señales abiertas | 297 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9315 | 62.9% | +0.129 | ➡️ estable | +4654.23$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11952 | 60.1% | +0.101 | ➡️ estable | +3872.57$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9211 | 58.3% | +0.083 | ➡️ estable | +3031.65$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3273 | 66.7% | +0.167 | ➡️ estable | +1707.27$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 3804 | 56.0% | +0.060 | 📈 madura (+0.08) | +541.86$ | 0.60$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 412 | 54.9% | +0.048 | 📉 agota (-0.17) | +95.41$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 95 | 80.0% | +0.294 | 📈 madura (+0.11) | +63.55$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 278 | 81.3% | +0.311 | ➡️ estable | +60.61$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1414 | 48.2% | -0.018 | ➡️ estable | +34.94$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 366 | 41.8% | -0.082 | 📈 madura (+0.09) | +24.52$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| ORDER_FLOW_5M | 1714 | 51.3% | +0.013 | ➡️ estable | +14.71$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 41 | 75.6% | +0.244 | ➡️ estable | +9.06$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 571 | 80.2% | +0.301 | 📉 agota (-0.04) | -0.44$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 15 | 40.0% | -0.066 | — | -1.16$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 74 | 91.9% | +0.408 | 📉 agota (-0.05) | -3.11$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 235 | 79.1% | +0.289 | 📉 agota (-0.04) | -5.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 86 | 83.7% | +0.330 | 📈 madura (+0.04) | -15.31$ | 2.00$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1659 | 55.5% | +0.054 | 📉 agota (-0.15) | -35.63$ | 0.55$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1460 | 71.6% | +0.216 | 📉 agota (-0.06) | -86.93$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 1123 | 46.5% | -0.035 | 📉 agota (-0.22) | -93.37$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 19618 | 62.3% | +0.123 | 📉 agota (-0.06) | -437.07$ | 1.23$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7746 | 70.1% | +0.201 | ➡️ estable | -519.92$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-06T01:26 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:26 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:26 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:26 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-06T01:26 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-06T01:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,495.14 | 0.1min |  |
| ✅ ETH | $1,905.26 | 0.1min |  |
| ✅ SOL | $73.82 | 0.1min |  |
| ✅ XRP | $1.06 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,500.10 | consenso |  |
| ETH | $1,905.27 | consenso |  |
| SOL | $73.79 | consenso |  |
| XRP | $1.06 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*