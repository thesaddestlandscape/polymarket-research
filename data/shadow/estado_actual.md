# Estado del bot — 2026-08-07 13:43 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.21 $** |
| P&L real total | 🔴 **-42.01 $** |
| P&L real hoy | -0.09 $ |
| P&L real 7 días | -8.00 $ |
| Fees pagados (real) | 14.60 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5929.83 $ |
| P&L sim compuesto | 🟢 +13613.33 $ (ficción Kelly: +53511% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +140.77 $ |
| Operaciones resueltas | 86454 (52846 WIN / 33608 LOSS) — 61.1% |
| Señales abiertas | 399 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9775 | 62.8% | +0.128 | ➡️ estable | +4944.59$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12456 | 60.1% | +0.101 | ➡️ estable | +4132.93$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9625 | 58.5% | +0.085 | ➡️ estable | +3256.46$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3473 | 66.5% | +0.164 | ➡️ estable | +1803.93$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 3976 | 56.0% | +0.060 | 📈 madura (+0.07) | +565.97$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 383 | 69.5% | +0.194 | 📉 agota (-0.04) | +260.17$ | 1.94$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1496 | 48.4% | -0.016 | 📈 madura (+0.03) | +38.22$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 68 | 67.6% | +0.171 | 📉 agota (-0.06) | +8.42$ | 1.71$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 243 | 51.9% | +0.018 | ➡️ estable | -0.13$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 70 | 50.0% | +0.000 | 📈 madura (+0.08) | -0.70$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 57 | 50.9% | +0.008 | 📈 madura (+0.15) | -0.92$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 97 | 92.8% | +0.419 | ➡️ estable | -2.40$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 60 | 40.0% | -0.097 | 📈 madura (+0.12) | -7.34$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 102 | 86.3% | +0.356 | 📈 madura (+0.04) | -13.68$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 279 | 77.8% | +0.276 | 📉 agota (-0.07) | -14.52$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 80 | 13.8% | -0.354 | ➡️ estable | -22.59$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1727 | 54.7% | +0.047 | 📉 agota (-0.16) | -40.91$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 286 | 33.2% | -0.167 | 📈 madura (+0.05) | -49.43$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1951 | 69.9% | +0.198 | 📉 agota (-0.06) | -151.31$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 1718 | 42.5% | -0.075 | 📉 agota (-0.18) | -263.49$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22765 | 61.9% | +0.119 | 📉 agota (-0.06) | -558.25$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9614 | 69.5% | +0.195 | ➡️ estable | -723.11$ | 1.95$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T13:41 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T13:41 | GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | BNB Up or Down - August 7, 9:15AM-9:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-08-07T13:41 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 7, 9:15AM-9:30AM ET… | ✅ WIN | +2.04$ |
| 2026-08-07T13:41 | GBM_LATE_15M#BNB#15min | BNB Up or Down - August 7, 9:15AM-9:30AM ET… | ✅ WIN | +2.04$ |
| 2026-08-07T13:41 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T13:39 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,235.00 | 0.1min |  |
| ✅ ETH | $1,931.58 | 0.1min |  |
| ✅ SOL | $74.22 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,250.40 | consenso |  |
| ETH | $1,931.99 | consenso |  |
| SOL | $74.03 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*