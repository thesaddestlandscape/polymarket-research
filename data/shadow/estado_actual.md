# Estado del bot — 2026-08-14 10:37 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **15.57 $** |
| P&L real total | 🔴 **-45.65 $** |
| P&L real hoy | +0.67 $ |
| P&L real 7 días | -3.74 $ |
| Fees pagados (real) | 15.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5797.85 $ |
| P&L sim compuesto | 🟢 +16235.71 $ (ficción Kelly: +63820% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -43.79 $ |
| Operaciones resueltas | 133643 (81608 WIN / 52035 LOSS) — 61.1% |
| Señales abiertas | 405 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12850 | 61.1% | +0.111 | ➡️ estable | +5986.73$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 14905 | 60.1% | +0.101 | ➡️ estable | +5091.75$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11504 | 60.2% | +0.102 | 📈 madura (+0.08) | +4695.04$ | 1.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4207 | 63.2% | +0.132 | 📉 agota (-0.04) | +1855.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1968 | 70.6% | +0.206 | 📉 agota (-0.08) | +1526.13$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4810 | 55.4% | +0.054 | 📈 madura (+0.04) | +606.76$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 760 | 54.7% | +0.047 | ➡️ estable | +110.22$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 1962 | 50.6% | +0.006 | 📈 madura (+0.07) | +109.01$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 201 | 75.1% | +0.249 | 📉 agota (-0.10) | +91.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 358 | 79.3% | +0.292 | 📉 agota (-0.03) | +52.57$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 449 | 44.5% | -0.054 | 📈 madura (+0.11) | +51.92$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3256 | 62.3% | +0.122 | ➡️ estable | +28.95$ | 1.47$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 225 | 52.9% | +0.029 | 📉 agota (-0.03) | +3.73$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1295 | 51.6% | +0.016 | ➡️ estable | -3.05$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 192 | 91.7% | +0.412 | ➡️ estable | -10.39$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 174 | 89.7% | +0.392 | 📈 madura (+0.11) | -13.63$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 438 | 78.3% | +0.282 | 📉 agota (-0.03) | -14.13$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2078 | 54.5% | +0.045 | 📉 agota (-0.18) | -17.01$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 139 | 36.7% | -0.131 | 📈 madura (+0.12) | -19.60$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 464 | 48.9% | -0.011 | ➡️ estable | -19.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 746 | 79.1% | +0.290 | ➡️ estable | -23.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 169 | 20.1% | -0.295 | 📈 madura (+0.14) | -30.93$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 469 | 44.8% | -0.052 | 📉 agota (-0.06) | -32.46$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 430 | 32.1% | -0.178 | 📉 agota (-0.04) | -74.26$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3984 | 69.4% | +0.194 | ➡️ estable | -260.97$ | 1.88$ | ✅ activa |
| BALLENAS_TARDIAS | 5692 | 45.8% | -0.042 | 📈 madura (+0.06) | -903.74$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37248 | 61.2% | +0.112 | ➡️ estable | -1388.51$ | 1.42$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18152 | 69.5% | +0.195 | ➡️ estable | -1480.50$ | 1.59$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T10:37 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T10:37 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T10:37 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T10:37 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.68$ |
| 2026-08-14T10:37 | FAVORITO_CONFIRMADO#DOGE#5min | … | ✅ WIN | +0.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T10:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,828.19 | 0.1min |  |
| ✅ ETH | $1,875.23 | 0.1min |  |
| ✅ SOL | $75.55 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,834.50 | consenso |  |
| ETH | $1,875.30 | consenso |  |
| SOL | $75.46 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*