# Estado del bot — 2026-08-11 14:40 UTC

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
| P&L fiel (stake fijo 1$) | +6141.12 $ |
| P&L sim compuesto | 🟢 +15235.75 $ (ficción Kelly: +59889% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +67.63 $ |
| Operaciones resueltas | 111689 (68619 WIN / 43070 LOSS) — 61.4% |
| Señales abiertas | 617 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11407 | 61.7% | +0.117 | ➡️ estable | +5589.60$ | 0.58$ | ✅ activa |
| GBM_LATE_15M | 13702 | 60.2% | +0.102 | ➡️ estable | +4682.60$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10455 | 59.4% | +0.094 | 📈 madura (+0.05) | +3970.20$ | 1.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3609 | 65.8% | +0.158 | ➡️ estable | +1813.49$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1072 | 74.2% | +0.241 | 📈 madura (+0.05) | +969.79$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4105 | 55.8% | +0.058 | 📈 madura (+0.06) | +559.42$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 459 | 54.7% | +0.047 | 📉 agota (-0.14) | +99.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1681 | 49.7% | -0.003 | 📈 madura (+0.06) | +60.50$ | 0.87$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1930 | 63.4% | +0.134 | ➡️ estable | +42.49$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 891 | 52.4% | +0.024 | ➡️ estable | +7.07$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1920 | 55.2% | +0.052 | 📉 agota (-0.15) | +3.98$ | 0.76$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 195 | 53.3% | +0.033 | ➡️ estable | +1.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 160 | 52.5% | +0.025 | ➡️ estable | -0.49$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 666 | 79.6% | +0.295 | ➡️ estable | -14.47$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 369 | 78.0% | +0.279 | 📉 agota (-0.07) | -16.21$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 99 | 32.3% | -0.173 | ➡️ estable | -18.85$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 276 | 46.7% | -0.032 | 📈 madura (+0.05) | -22.38$ | 1.13$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 160 | 38.8% | -0.111 | ➡️ estable | -23.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 350 | 42.9% | -0.071 | 📉 agota (-0.12) | -32.61$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3157 | 70.2% | +0.202 | ➡️ estable | -188.53$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3650 | 45.5% | -0.045 | 📈 madura (+0.09) | -697.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31264 | 61.7% | +0.117 | ➡️ estable | -858.27$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14555 | 69.9% | +0.199 | ➡️ estable | -1095.21$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T14:39 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.62$ |
| 2026-08-11T14:39 | LIQUIDACIONES_5M#SOL#5min | Solana Up or Down - August 11, 10:15AM-10:20AM ET… | ✅ WIN | +0.49$ |
| 2026-08-11T14:39 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T14:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,898.50 | 0.1min |  |
| ✅ ETH | $1,877.06 | 0.1min |  |
| ✅ SOL | $75.65 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,898.50 | consenso |  |
| ETH | $1,877.06 | consenso |  |
| SOL | $75.53 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*