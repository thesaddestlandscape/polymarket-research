# Estado del bot — 2026-08-07 11:42 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.94 $** |
| P&L real total | 🔴 **-42.28 $** |
| P&L real hoy | -0.36 $ |
| P&L real 7 días | -8.27 $ |
| Fees pagados (real) | 14.60 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5951.92 $ |
| P&L sim compuesto | 🟢 +13612.41 $ (ficción Kelly: +53508% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +139.86 $ |
| Operaciones resueltas | 85901 (52509 WIN / 33392 LOSS) — 61.1% |
| Señales abiertas | 379 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9737 | 62.8% | +0.128 | ➡️ estable | +4941.87$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12422 | 60.1% | +0.101 | ➡️ estable | +4126.52$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9606 | 58.5% | +0.085 | ➡️ estable | +3246.31$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3463 | 66.4% | +0.164 | ➡️ estable | +1800.29$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 3970 | 55.9% | +0.059 | 📈 madura (+0.07) | +558.97$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 370 | 69.7% | +0.196 | 📉 agota (-0.04) | +258.28$ | 1.96$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 125 | 76.8% | +0.264 | 📉 agota (-0.04) | +71.48$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 298 | 80.9% | +0.307 | ➡️ estable | +59.80$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1494 | 48.4% | -0.016 | 📈 madura (+0.03) | +39.18$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 32 | 68.8% | +0.176 | ➡️ estable | +5.20$ | 1.76$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 66 | 50.0% | +0.000 | 📈 madura (+0.09) | -0.28$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 57 | 50.9% | +0.008 | 📈 madura (+0.15) | -0.92$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 221 | 51.1% | +0.011 | 📉 agota (-0.05) | -1.74$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 96 | 92.7% | +0.418 | ➡️ estable | -2.50$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 57 | 36.8% | -0.127 | ➡️ estable | -8.73$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 100 | 86.0% | +0.353 | 📈 madura (+0.04) | -13.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 275 | 77.5% | +0.273 | 📉 agota (-0.08) | -17.11$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 75 | 14.7% | -0.344 | ➡️ estable | -20.04$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1722 | 54.6% | +0.046 | 📉 agota (-0.16) | -44.81$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 276 | 32.6% | -0.173 | ➡️ estable | -49.33$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1928 | 69.9% | +0.199 | 📉 agota (-0.06) | -146.16$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 1675 | 42.3% | -0.077 | 📉 agota (-0.18) | -256.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22600 | 62.0% | +0.120 | 📉 agota (-0.06) | -540.93$ | 1.20$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9508 | 69.6% | +0.196 | ➡️ estable | -711.00$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T11:42 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.54$ |
| 2026-08-07T11:42 | FAVORITO_CONFIRMADO#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T11:42 | GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | BNB Up or Down - August 7, 7:15AM-7:30AM ET… | ✅ WIN | +1.88$ |
| 2026-08-07T11:42 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 7, 7:15AM-7:30AM ET… | ✅ WIN | +1.88$ |
| 2026-08-07T11:42 | GBM_LATE_15M#BNB#15min | BNB Up or Down - August 7, 7:15AM-7:30AM ET… | ✅ WIN | +1.88$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T11:40 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,979.00 | 0.1min |  |
| ✅ ETH | $1,914.20 | 0.1min |  |
| ✅ SOL | $73.65 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,979.00 | consenso |  |
| ETH | $1,914.48 | consenso |  |
| SOL | $73.55 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*