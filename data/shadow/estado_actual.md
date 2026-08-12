# Estado del bot — 2026-08-12 12:39 UTC

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
| P&L fiel (stake fijo 1$) | +5935.97 $ |
| P&L sim compuesto | 🟢 +15404.43 $ (ficción Kelly: +60552% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +148.77 $ |
| Operaciones resueltas | 118425 (72609 WIN / 45816 LOSS) — 61.3% |
| Señales abiertas | 493 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11807 | 61.5% | +0.115 | ➡️ estable | +5699.42$ | 0.54$ | ✅ activa |
| GBM_LATE_15M | 14033 | 60.2% | +0.102 | ➡️ estable | +4823.87$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10689 | 59.7% | +0.097 | 📈 madura (+0.06) | +4202.78$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3782 | 64.9% | +0.149 | ➡️ estable | +1816.71$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1264 | 72.6% | +0.226 | ➡️ estable | +1081.63$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4334 | 55.5% | +0.055 | 📈 madura (+0.05) | +557.84$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 519 | 54.7% | +0.047 | 📉 agota (-0.09) | +105.11$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 341 | 80.1% | +0.299 | ➡️ estable | +58.81$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1769 | 49.9% | -0.001 | 📈 madura (+0.07) | +58.42$ | 0.71$ | ⚠️ IC negativo |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2362 | 62.5% | +0.125 | 📉 agota (-0.03) | +23.41$ | 1.25$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 217 | 53.5% | +0.034 | ➡️ estable | +3.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1969 | 54.9% | +0.048 | 📉 agota (-0.17) | -3.15$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 190 | 51.6% | +0.016 | 📉 agota (-0.04) | -3.89$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1046 | 51.2% | +0.012 | 📉 agota (-0.03) | -6.17$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 396 | 78.0% | +0.279 | 📉 agota (-0.07) | -17.26$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 692 | 78.9% | +0.288 | ➡️ estable | -24.58$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 200 | 38.0% | -0.119 | 📉 agota (-0.10) | -29.84$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 347 | 45.2% | -0.047 | 📉 agota (-0.04) | -30.71$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 370 | 31.6% | -0.183 | 📉 agota (-0.06) | -66.10$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3429 | 70.3% | +0.202 | ➡️ estable | -194.34$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4200 | 46.5% | -0.035 | 📈 madura (+0.09) | -721.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33193 | 61.5% | +0.115 | ➡️ estable | -1060.93$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15776 | 69.8% | +0.198 | ➡️ estable | -1234.21$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T12:38 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T12:38 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T12:38 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T12:38 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T12:38 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T12:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,195.10 | 0.2min |  |
| ✅ ETH | $1,912.68 | 0.2min |  |
| ✅ SOL | $76.95 | 0.2min |  |
| ✅ XRP | $1.02 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,199.40 | consenso |  |
| ETH | $1,912.68 | consenso |  |
| SOL | $76.95 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*