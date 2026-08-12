# Estado del bot — 2026-08-12 21:39 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.15 $** |
| P&L real total | 🔴 **-43.07 $** |
| P&L real hoy | -3.02 $ |
| P&L real 7 días | -8.32 $ |
| Fees pagados (real) | 15.47 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5940.29 $ |
| P&L sim compuesto | 🟢 +15604.37 $ (ficción Kelly: +61338% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +348.71 $ |
| Operaciones resueltas | 121436 (74394 WIN / 47042 LOSS) — 61.3% |
| Señales abiertas | 548 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12011 | 61.4% | +0.114 | ➡️ estable | +5740.00$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14222 | 60.1% | +0.101 | ➡️ estable | +4854.05$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10840 | 59.8% | +0.098 | 📈 madura (+0.06) | +4299.32$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3853 | 64.6% | +0.146 | ➡️ estable | +1817.30$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1407 | 72.5% | +0.225 | ➡️ estable | +1203.44$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4443 | 55.7% | +0.057 | 📈 madura (+0.05) | +582.92$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 577 | 55.6% | +0.056 | ➡️ estable | +109.51$ | 0.66$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 181 | 76.2% | +0.260 | 📉 agota (-0.05) | +88.08$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1810 | 50.1% | +0.001 | 📈 madura (+0.07) | +68.14$ | 0.73$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 344 | 80.2% | +0.301 | ➡️ estable | +60.16$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2544 | 62.6% | +0.126 | ➡️ estable | +32.48$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1736 | 51.4% | +0.014 | ➡️ estable | +17.62$ | 0.54$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_PYCONFIRMADO | 228 | 54.4% | +0.043 | 📈 madura (+0.03) | +7.03$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 196 | 51.5% | +0.015 | 📉 agota (-0.03) | -4.19$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1078 | 51.2% | +0.012 | 📉 agota (-0.03) | -6.77$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1992 | 54.6% | +0.046 | 📉 agota (-0.18) | -9.62$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 159 | 89.3% | +0.388 | 📈 madura (+0.11) | -13.27$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 127 | 36.2% | -0.136 | 📈 madura (+0.12) | -18.93$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 404 | 77.7% | +0.276 | 📉 agota (-0.06) | -20.72$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 703 | 78.9% | +0.289 | ➡️ estable | -23.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 366 | 46.7% | -0.033 | ➡️ estable | -24.99$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 152 | 20.4% | -0.292 | 📈 madura (+0.12) | -27.06$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 417 | 44.4% | -0.056 | 📉 agota (-0.07) | -30.01$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 222 | 37.4% | -0.125 | 📉 agota (-0.04) | -34.14$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 376 | 31.4% | -0.185 | 📉 agota (-0.05) | -68.14$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3530 | 69.9% | +0.199 | ➡️ estable | -216.07$ | 1.96$ | ✅ activa |
| BALLENAS_TARDIAS | 4495 | 46.6% | -0.034 | 📈 madura (+0.08) | -738.13$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33995 | 61.4% | +0.114 | ➡️ estable | -1127.23$ | 1.08$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16227 | 69.7% | +0.197 | ➡️ estable | -1278.60$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T21:38 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T21:38 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T21:38 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.77$ |
| 2026-08-12T21:38 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.77$ |
| 2026-08-12T21:38 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T21:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,439.18 | 0.2min |  |
| ✅ ETH | $1,876.28 | 0.2min |  |
| ✅ SOL | $75.57 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,439.18 | consenso |  |
| ETH | $1,876.28 | consenso |  |
| SOL | $75.49 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*