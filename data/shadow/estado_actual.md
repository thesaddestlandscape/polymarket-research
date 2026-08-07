# Estado del bot — 2026-08-07 16:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.64 $** |
| P&L real total | 🔴 **-40.58 $** |
| P&L real hoy | +1.35 $ |
| P&L real 7 días | -6.56 $ |
| Fees pagados (real) | 14.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5932.09 $ |
| P&L sim compuesto | 🟢 +13666.71 $ (ficción Kelly: +53721% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +194.15 $ |
| Operaciones resueltas | 87197 (53279 WIN / 33918 LOSS) — 61.1% |
| Señales abiertas | 388 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9824 | 62.8% | +0.128 | ➡️ estable | +4969.25$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12498 | 60.2% | +0.102 | ➡️ estable | +4167.67$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9653 | 58.5% | +0.085 | ➡️ estable | +3279.00$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3484 | 66.4% | +0.164 | ➡️ estable | +1800.70$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 3983 | 56.0% | +0.060 | 📈 madura (+0.07) | +567.24$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 406 | 70.7% | +0.206 | 📉 agota (-0.04) | +292.84$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 657 | 76.6% | +0.265 | 📈 madura (+0.17) | +265.94$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 433 | 55.0% | +0.049 | 📉 agota (-0.13) | +98.68$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1501 | 48.5% | -0.015 | 📈 madura (+0.04) | +44.53$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 386 | 42.5% | -0.075 | 📈 madura (+0.11) | +20.25$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 121 | 68.6% | +0.183 | 📈 madura (+0.04) | +17.96$ | 1.83$ | ✅ activa |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 263 | 53.6% | +0.036 | ➡️ estable | +4.45$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 596 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 73 | 50.7% | +0.007 | 📈 madura (+0.12) | -0.02$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 60 | 50.0% | +0.000 | 📈 madura (+0.06) | -1.27$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 97 | 92.8% | +0.419 | ➡️ estable | -2.40$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 21 | 28.6% | -0.196 | — | -3.35$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 62 | 38.7% | -0.109 | 📈 madura (+0.12) | -8.36$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 103 | 86.4% | +0.357 | 📈 madura (+0.04) | -13.58$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 281 | 77.6% | +0.274 | 📉 agota (-0.08) | -15.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 86 | 14.0% | -0.352 | ➡️ estable | -23.83$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1732 | 54.7% | +0.047 | 📉 agota (-0.16) | -41.44$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 299 | 33.8% | -0.161 | 📈 madura (+0.06) | -48.45$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1986 | 69.7% | +0.197 | 📉 agota (-0.07) | -156.20$ | 1.97$ | ✅ activa |
| BALLENAS_TARDIAS | 1765 | 42.0% | -0.080 | 📉 agota (-0.18) | -288.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22978 | 61.8% | +0.118 | 📉 agota (-0.06) | -585.96$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9755 | 69.3% | +0.193 | ➡️ estable | -765.54$ | 1.93$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T16:10 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T16:10 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.35$ |
| 2026-08-07T16:10 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.57$ |
| 2026-08-07T16:10 | UPDOWN_GBM_15M_TARDIO#XRP#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-07T16:10 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.54$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T16:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,957.00 | 0.1min |  |
| ✅ ETH | $1,919.36 | 0.1min |  |
| ✅ SOL | $73.95 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,932.09 | consenso |  |
| ETH | $1,919.45 | consenso |  |
| SOL | $73.92 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*