# Estado del bot — 2026-08-11 12:54 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.07 $** |
| P&L real total | 🔴 **-41.15 $** |
| P&L real hoy | -0.23 $ |
| P&L real 7 días | -11.98 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6206.37 $ |
| P&L sim compuesto | 🟢 +15299.33 $ (ficción Kelly: +60139% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +131.21 $ |
| Operaciones resueltas | 111167 (68332 WIN / 42835 LOSS) — 61.5% |
| Señales abiertas | 570 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11376 | 61.7% | +0.117 | ➡️ estable | +5580.98$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 13675 | 60.3% | +0.103 | ➡️ estable | +4679.27$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10439 | 59.5% | +0.095 | 📈 madura (+0.05) | +3973.27$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3607 | 65.8% | +0.158 | ➡️ estable | +1816.60$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1052 | 74.6% | +0.246 | 📈 madura (+0.06) | +970.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4091 | 55.9% | +0.059 | 📈 madura (+0.06) | +563.73$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 454 | 54.8% | +0.048 | 📉 agota (-0.13) | +99.55$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1674 | 49.6% | -0.004 | 📈 madura (+0.07) | +58.62$ | 0.88$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1893 | 63.5% | +0.135 | ➡️ estable | +45.42$ | 1.35$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 881 | 52.3% | +0.023 | ➡️ estable | +6.25$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 190 | 54.2% | +0.042 | ➡️ estable | +4.10$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1916 | 55.2% | +0.052 | 📉 agota (-0.15) | +2.10$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 158 | 51.9% | +0.019 | ➡️ estable | -1.64$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 665 | 79.5% | +0.295 | ➡️ estable | -15.23$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 366 | 78.1% | +0.280 | 📉 agota (-0.06) | -15.39$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 91 | 29.7% | -0.199 | 📉 agota (-0.07) | -19.73$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 270 | 46.7% | -0.033 | ➡️ estable | -22.25$ | 1.40$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 157 | 38.2% | -0.116 | ➡️ estable | -23.68$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 344 | 42.7% | -0.072 | 📉 agota (-0.12) | -32.57$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3138 | 70.1% | +0.201 | ➡️ estable | -189.97$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3597 | 45.5% | -0.045 | 📈 madura (+0.08) | -682.20$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31112 | 61.8% | +0.118 | ➡️ estable | -826.53$ | 1.16$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14464 | 69.9% | +0.199 | ➡️ estable | -1075.63$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T12:53 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.11$ |
| 2026-08-11T12:53 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T12:53 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +1.37$ |
| 2026-08-11T12:53 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T12:53 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T12:49 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,269.00 | 0.2min |  |
| ✅ ETH | $1,887.63 | 0.2min |  |
| ✅ SOL | $75.84 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,275.10 | consenso |  |
| ETH | $1,887.63 | consenso |  |
| SOL | $75.83 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*