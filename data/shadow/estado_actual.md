# Estado del bot — 2026-08-07 18:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.04 $** |
| P&L real total | 🔴 **-40.18 $** |
| P&L real hoy | +1.74 $ |
| P&L real 7 días | -6.17 $ |
| Fees pagados (real) | 14.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5912.11 $ |
| P&L sim compuesto | 🟢 +13670.65 $ (ficción Kelly: +53737% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +198.10 $ |
| Operaciones resueltas | 87694 (53564 WIN / 34130 LOSS) — 61.1% |
| Señales abiertas | 396 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9860 | 62.8% | +0.128 | ➡️ estable | +4983.43$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12527 | 60.2% | +0.102 | ➡️ estable | +4186.57$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9673 | 58.5% | +0.085 | ➡️ estable | +3295.31$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3492 | 66.4% | +0.163 | ➡️ estable | +1797.74$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 3987 | 56.0% | +0.060 | 📈 madura (+0.07) | +564.94$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 423 | 70.9% | +0.208 | 📉 agota (-0.03) | +307.67$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 657 | 76.6% | +0.265 | 📈 madura (+0.17) | +265.94$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 433 | 55.0% | +0.049 | 📉 agota (-0.13) | +98.68$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1505 | 48.4% | -0.016 | 📈 madura (+0.03) | +40.20$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 388 | 42.3% | -0.077 | 📈 madura (+0.11) | +18.21$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 161 | 65.8% | +0.156 | 📉 agota (-0.03) | +16.35$ | 1.56$ | ✅ activa |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 267 | 53.2% | +0.032 | ➡️ estable | +3.40$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 597 | 80.6% | +0.305 | 📉 agota (-0.03) | +2.61$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 75 | 52.0% | +0.019 | 📈 madura (+0.16) | +1.78$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 63 | 50.8% | +0.008 | 📈 madura (+0.04) | -0.54$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 99 | 92.9% | +0.421 | ➡️ estable | -2.23$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 23 | 26.1% | -0.220 | — | -4.37$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 68 | 39.7% | -0.100 | 📈 madura (+0.14) | -8.55$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 56 | 30.4% | -0.190 | 📉 agota (-0.03) | -11.61$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 103 | 86.4% | +0.357 | 📈 madura (+0.04) | -13.58$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 284 | 76.8% | +0.266 | 📉 agota (-0.10) | -22.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 91 | 14.3% | -0.349 | ➡️ estable | -25.14$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1735 | 54.7% | +0.047 | 📉 agota (-0.16) | -41.85$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 307 | 33.9% | -0.160 | 📈 madura (+0.04) | -49.43$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2006 | 69.7% | +0.197 | 📉 agota (-0.06) | -156.55$ | 1.97$ | ✅ activa |
| BALLENAS_TARDIAS | 1803 | 41.5% | -0.085 | 📉 agota (-0.19) | -309.40$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 23133 | 61.8% | +0.118 | 📉 agota (-0.06) | -600.56$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9839 | 69.3% | +0.193 | ➡️ estable | -768.24$ | 1.93$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T18:02 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T18:02 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T18:02 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T18:02 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T18:02 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T18:00 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,685.86 | 0.2min |  |
| ✅ ETH | $1,908.93 | 0.2min |  |
| ✅ SOL | $73.43 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,696.00 | consenso |  |
| ETH | $1,908.93 | consenso |  |
| SOL | $73.28 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*