# Estado del bot — 2026-08-12 13:36 UTC

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
| P&L fiel (stake fijo 1$) | +5905.47 $ |
| P&L sim compuesto | 🟢 +15378.49 $ (ficción Kelly: +60450% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +122.84 $ |
| Operaciones resueltas | 118759 (72787 WIN / 45972 LOSS) — 61.3% |
| Señales abiertas | 507 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11830 | 61.4% | +0.114 | ➡️ estable | +5692.97$ | 0.53$ | ✅ activa |
| GBM_LATE_15M | 14055 | 60.2% | +0.102 | ➡️ estable | +4814.16$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10708 | 59.7% | +0.097 | 📈 madura (+0.06) | +4201.68$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3794 | 64.8% | +0.148 | ➡️ estable | +1811.17$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1281 | 72.5% | +0.225 | ➡️ estable | +1099.45$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4348 | 55.6% | +0.056 | 📈 madura (+0.06) | +562.94$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 524 | 54.6% | +0.046 | 📉 agota (-0.11) | +103.27$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1777 | 49.9% | -0.001 | 📈 madura (+0.08) | +60.75$ | 0.73$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2383 | 62.7% | +0.126 | ➡️ estable | +27.86$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 218 | 53.2% | +0.032 | ➡️ estable | +2.63$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1974 | 54.9% | +0.049 | 📉 agota (-0.17) | -2.98$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 190 | 51.6% | +0.016 | 📉 agota (-0.04) | -3.89$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1055 | 51.2% | +0.012 | ➡️ estable | -6.82$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 397 | 77.8% | +0.277 | 📉 agota (-0.07) | -19.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 693 | 78.9% | +0.288 | ➡️ estable | -23.61$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 200 | 38.0% | -0.119 | 📉 agota (-0.10) | -29.84$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 352 | 45.5% | -0.045 | 📉 agota (-0.03) | -30.27$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 402 | 44.3% | -0.057 | 📉 agota (-0.09) | -32.09$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 372 | 31.5% | -0.184 | 📉 agota (-0.06) | -67.12$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3438 | 70.3% | +0.203 | ➡️ estable | -194.02$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4232 | 46.4% | -0.036 | 📈 madura (+0.09) | -728.38$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33276 | 61.5% | +0.115 | ➡️ estable | -1076.67$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15814 | 69.8% | +0.198 | ➡️ estable | -1240.55$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T13:36 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.41$ |
| 2026-08-12T13:36 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T13:36 | UPDOWN_GBM#DOGE#5min | Dogecoin Up or Down - August 12, 9:15AM-9:20AM ET… | ✅ WIN | +0.52$ |
| 2026-08-12T13:36 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.21$ |
| 2026-08-12T13:36 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T13:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,925.19 | 0.2min |  |
| ✅ ETH | $1,905.59 | 0.2min |  |
| ✅ SOL | $76.38 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,952.40 | consenso |  |
| ETH | $1,905.59 | consenso |  |
| SOL | $76.38 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*