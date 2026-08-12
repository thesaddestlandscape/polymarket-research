# Estado del bot — 2026-08-12 14:54 UTC

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
| P&L fiel (stake fijo 1$) | +5938.08 $ |
| P&L sim compuesto | 🟢 +15458.40 $ (ficción Kelly: +60764% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +202.75 $ |
| Operaciones resueltas | 119195 (73048 WIN / 46147 LOSS) — 61.3% |
| Señales abiertas | 512 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11856 | 61.5% | +0.115 | ➡️ estable | +5712.83$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14082 | 60.2% | +0.102 | ➡️ estable | +4830.07$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10727 | 59.7% | +0.097 | 📈 madura (+0.06) | +4228.58$ | 1.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3806 | 64.8% | +0.148 | ➡️ estable | +1814.64$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1305 | 72.6% | +0.225 | ➡️ estable | +1129.25$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4379 | 55.5% | +0.055 | 📈 madura (+0.05) | +569.98$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 532 | 55.1% | +0.051 | 📉 agota (-0.08) | +107.18$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 176 | 75.6% | +0.253 | 📉 agota (-0.06) | +80.39$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1782 | 49.9% | -0.001 | 📈 madura (+0.08) | +61.23$ | 0.73$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 342 | 80.1% | +0.299 | ➡️ estable | +59.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2408 | 62.7% | +0.127 | ➡️ estable | +31.81$ | 1.27$ | ✅ activa |
| ORDER_FLOW_5M | 1735 | 51.5% | +0.015 | ➡️ estable | +19.02$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 219 | 53.4% | +0.034 | ➡️ estable | +3.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 160 | 93.8% | +0.432 | ➡️ estable | -1.28$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 190 | 51.6% | +0.016 | 📉 agota (-0.04) | -3.89$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1978 | 54.8% | +0.048 | 📉 agota (-0.17) | -6.02$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1056 | 51.2% | +0.012 | ➡️ estable | -6.34$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 157 | 89.2% | +0.387 | 📈 madura (+0.11) | -13.42$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 397 | 77.8% | +0.277 | 📉 agota (-0.07) | -19.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 694 | 79.0% | +0.289 | ➡️ estable | -23.23$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 357 | 46.2% | -0.038 | 📉 agota (-0.03) | -27.88$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 403 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.60$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 208 | 37.0% | -0.129 | 📉 agota (-0.08) | -32.93$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 372 | 31.5% | -0.184 | 📉 agota (-0.06) | -67.12$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3453 | 70.1% | +0.200 | ➡️ estable | -205.07$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 4279 | 46.4% | -0.036 | 📈 madura (+0.08) | -735.83$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33388 | 61.5% | +0.115 | ➡️ estable | -1070.85$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15878 | 69.7% | +0.197 | ➡️ estable | -1256.32$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T14:53 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T14:53 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T14:53 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.74$ |
| 2026-08-12T14:53 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T14:53 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T14:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,534.00 | 0.1min |  |
| ✅ ETH | $1,892.59 | 0.1min |  |
| ✅ SOL | $75.56 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,534.00 | consenso |  |
| ETH | $1,892.59 | consenso |  |
| SOL | $75.56 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*