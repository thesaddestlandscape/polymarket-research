# Estado del bot — 2026-08-05 19:28 UTC

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
| P&L fiel (stake fijo 1$) | +6036.76 $ |
| P&L sim compuesto | 🟢 +12963.27 $ (ficción Kelly: +50956% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +611.87 $ |
| Operaciones resueltas | 75662 (46458 WIN / 29204 LOSS) — 61.4% |
| Señales abiertas | 350 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9222 | 62.8% | +0.128 | ➡️ estable | +4604.99$ | 1.29$ | ✅ activa |
| GBM_LATE_15M | 11843 | 60.1% | +0.101 | ➡️ estable | +3831.92$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9142 | 58.2% | +0.082 | ➡️ estable | +2979.30$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3223 | 66.8% | +0.168 | ➡️ estable | +1682.37$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 3765 | 56.0% | +0.060 | 📈 madura (+0.08) | +533.96$ | 0.60$ | ✅ activa |
| WEEKLY_PRICE | 617 | 75.7% | +0.256 | 📈 madura (+0.18) | +220.45$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 409 | 54.5% | +0.045 | 📉 agota (-0.18) | +93.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 276 | 81.9% | +0.317 | ➡️ estable | +64.69$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 94 | 79.8% | +0.292 | 📈 madura (+0.10) | +61.71$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1401 | 48.1% | -0.019 | ➡️ estable | +31.78$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 363 | 41.3% | -0.086 | 📈 madura (+0.08) | +22.91$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1710 | 51.2% | +0.012 | ➡️ estable | +12.04$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 567 | 80.4% | +0.303 | 📉 agota (-0.03) | +2.45$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM_FADE | 7 | 28.6% | -0.058 | — | -1.28$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 73 | 91.8% | +0.407 | 📉 agota (-0.05) | -3.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 226 | 79.2% | +0.289 | ➡️ estable | -5.42$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 393 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.72$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 83 | 84.3% | +0.335 | 📈 madura (+0.07) | -13.55$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_TARDIAS | 968 | 50.1% | +0.001 | 📉 agota (-0.24) | -38.55$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1649 | 55.5% | +0.055 | 📉 agota (-0.15) | -39.59$ | 0.55$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1391 | 72.3% | +0.223 | 📉 agota (-0.05) | -84.42$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 19113 | 62.4% | +0.124 | 📉 agota (-0.06) | -424.80$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7472 | 70.2% | +0.202 | ➡️ estable | -480.10$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T19:27 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.37$ |
| 2026-08-05T19:27 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T19:27 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.43$ |
| 2026-08-05T19:27 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-05T19:27 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +3.13$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T19:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,829.96 | 0.2min |  |
| ✅ ETH | $1,916.79 | 0.2min |  |
| ✅ SOL | $74.49 | 0.2min |  |
| ✅ XRP | $1.07 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,849.80 | consenso |  |
| ETH | $1,917.30 | consenso |  |
| SOL | $74.41 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*