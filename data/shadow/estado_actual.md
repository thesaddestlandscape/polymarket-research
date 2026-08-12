# Estado del bot — 2026-08-12 08:27 UTC

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
| P&L fiel (stake fijo 1$) | +6008.65 $ |
| P&L sim compuesto | 🟢 +15396.11 $ (ficción Kelly: +60519% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +140.45 $ |
| Operaciones resueltas | 117046 (71789 WIN / 45257 LOSS) — 61.3% |
| Señales abiertas | 500 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11710 | 61.6% | +0.116 | ➡️ estable | +5703.72$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 13950 | 60.2% | +0.102 | ➡️ estable | +4800.64$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10615 | 59.7% | +0.096 | 📈 madura (+0.05) | +4160.31$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3757 | 65.1% | +0.151 | ➡️ estable | +1821.87$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1191 | 73.5% | +0.234 | ➡️ estable | +1068.96$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4310 | 55.5% | +0.055 | 📈 madura (+0.05) | +557.14$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 495 | 54.5% | +0.045 | 📉 agota (-0.12) | +105.79$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 174 | 75.9% | +0.256 | 📉 agota (-0.04) | +81.74$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 339 | 80.2% | +0.301 | ➡️ estable | +60.17$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1752 | 49.8% | -0.002 | 📈 madura (+0.07) | +59.31$ | 0.74$ | ⚠️ IC negativo |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2284 | 62.7% | +0.126 | ➡️ estable | +26.81$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1732 | 51.4% | +0.014 | ➡️ estable | +16.86$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 213 | 53.1% | +0.030 | ➡️ estable | +1.39$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1008 | 51.9% | +0.019 | ➡️ estable | +0.36$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 157 | 93.6% | +0.431 | ➡️ estable | -1.65$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1961 | 54.8% | +0.048 | 📉 agota (-0.17) | -3.15$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 187 | 50.8% | +0.008 | 📉 agota (-0.04) | -7.88$ | 0.50$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 152 | 88.8% | +0.383 | 📈 madura (+0.12) | -14.03$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 389 | 77.9% | +0.277 | 📉 agota (-0.07) | -18.56$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 686 | 78.9% | +0.288 | ➡️ estable | -26.00$ | 1.93$ | ✅ activa |
| GBM_LATE_60M_FADE | 150 | 20.0% | -0.296 | 📈 madura (+0.10) | -26.91$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 333 | 45.9% | -0.040 | ➡️ estable | -27.33$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 191 | 38.2% | -0.117 | 📉 agota (-0.06) | -28.21$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 368 | 31.5% | -0.184 | 📉 agota (-0.05) | -66.08$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3370 | 70.4% | +0.203 | ➡️ estable | -186.45$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4083 | 46.4% | -0.036 | 📈 madura (+0.09) | -697.89$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 32827 | 61.5% | +0.115 | ➡️ estable | -1054.47$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15541 | 69.8% | +0.198 | ➡️ estable | -1217.83$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T08:26 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T08:26 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.60$ |
| 2026-08-12T08:26 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.52$ |
| 2026-08-12T08:26 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T08:26 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T08:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,750.82 | 0.1min |  |
| ✅ ETH | $1,892.29 | 0.1min |  |
| ✅ SOL | $76.36 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,754.60 | consenso |  |
| ETH | $1,892.29 | consenso |  |
| SOL | $76.33 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*