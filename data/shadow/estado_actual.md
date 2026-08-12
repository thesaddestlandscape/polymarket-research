# Estado del bot — 2026-08-12 13:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.81 $** |
| P&L real total | 🔴 **-42.41 $** |
| P&L real hoy | -2.36 $ |
| P&L real 7 días | -7.66 $ |
| Fees pagados (real) | 15.39 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5902.68 $ |
| P&L sim compuesto | 🟢 +15365.59 $ (ficción Kelly: +60399% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +109.93 $ |
| Operaciones resueltas | 118567 (72678 WIN / 45889 LOSS) — 61.3% |
| Señales abiertas | 495 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11819 | 61.4% | +0.114 | ➡️ estable | +5687.88$ | 0.53$ | ✅ activa |
| GBM_LATE_15M | 14044 | 60.2% | +0.102 | ➡️ estable | +4821.11$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10698 | 59.7% | +0.097 | 📈 madura (+0.06) | +4198.29$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3788 | 64.9% | +0.149 | ➡️ estable | +1813.68$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1272 | 72.5% | +0.224 | ➡️ estable | +1080.44$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4340 | 55.6% | +0.056 | 📈 madura (+0.06) | +560.88$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 521 | 54.7% | +0.047 | 📉 agota (-0.10) | +104.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1772 | 49.9% | -0.001 | 📈 madura (+0.08) | +58.89$ | 0.72$ | ⚠️ IC negativo |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2372 | 62.6% | +0.126 | ➡️ estable | +25.77$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 217 | 53.5% | +0.034 | ➡️ estable | +3.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1971 | 54.8% | +0.048 | 📉 agota (-0.17) | -3.24$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 190 | 51.6% | +0.016 | 📉 agota (-0.04) | -3.89$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1052 | 51.2% | +0.012 | ➡️ estable | -6.28$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 396 | 78.0% | +0.279 | 📉 agota (-0.07) | -17.26$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 693 | 78.9% | +0.288 | ➡️ estable | -23.61$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 200 | 38.0% | -0.119 | 📉 agota (-0.10) | -29.84$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 347 | 45.2% | -0.047 | 📉 agota (-0.04) | -30.71$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 371 | 31.5% | -0.184 | 📉 agota (-0.06) | -66.61$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3433 | 70.3% | +0.203 | ➡️ estable | -193.11$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4211 | 46.4% | -0.036 | 📈 madura (+0.09) | -725.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33227 | 61.5% | +0.115 | ➡️ estable | -1074.93$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15791 | 69.7% | +0.197 | ➡️ estable | -1240.43$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T13:01 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 12, 8:45AM-8:50AM ET… | ✅ WIN | +0.50$ |
| 2026-08-12T13:01 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-12T13:01 | UPDOWN_OU_5M#BTC#5min | Bitcoin Up or Down - August 12, 8:45AM-8:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-12T13:01 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 12, 8:40AM-8:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-12T13:01 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 12, 8:40AM-8:45AM ET… | ✅ WIN | +0.48$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T12:57 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,064.31 | 0.5min |  |
| ✅ ETH | $1,909.41 | 0.5min |  |
| ✅ SOL | $76.59 | 0.5min |  |
| ✅ XRP | $1.02 | 0.5min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,071.00 | consenso |  |
| ETH | $1,909.41 | consenso |  |
| SOL | $76.59 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*