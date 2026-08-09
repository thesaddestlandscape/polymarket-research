# Estado del bot — 2026-08-09 16:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.36 $** |
| P&L real total | 🔴 **-41.86 $** |
| P&L real hoy | -1.86 $ |
| P&L real 7 días | -12.23 $ |
| Fees pagados (real) | 15.00 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6010.14 $ |
| P&L sim compuesto | 🟢 +14235.84 $ (ficción Kelly: +55958% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +175.93 $ |
| Operaciones resueltas | 99406 (60945 WIN / 38461 LOSS) — 61.3% |
| Señales abiertas | 862 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10650 | 62.2% | +0.121 | ➡️ estable | +5217.65$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13112 | 60.1% | +0.101 | ➡️ estable | +4394.45$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10042 | 59.0% | +0.090 | 📈 madura (+0.03) | +3613.03$ | 0.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3523 | 66.3% | +0.163 | ➡️ estable | +1808.21$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 714 | 71.8% | +0.218 | 📈 madura (+0.03) | +564.39$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4011 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.98$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 708 | 77.5% | +0.275 | 📈 madura (+0.17) | +309.93$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 437 | 55.1% | +0.051 | 📉 agota (-0.13) | +98.04$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 140 | 76.4% | +0.261 | 📉 agota (-0.04) | +76.28$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 309 | 80.6% | +0.304 | ➡️ estable | +60.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1553 | 48.8% | -0.012 | 📈 madura (+0.04) | +46.73$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1020 | 63.3% | +0.133 | ➡️ estable | +19.58$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 326 | 55.5% | +0.055 | 📉 agota (-0.14) | +13.14$ | 0.55$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 119 | 52.9% | +0.029 | 📈 madura (+0.07) | +5.16$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 131 | 93.9% | +0.432 | 📈 madura (+0.06) | -0.45$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 108 | 53.7% | +0.036 | 📈 madura (+0.04) | -0.83$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 606 | 51.8% | +0.018 | 📉 agota (-0.05) | -1.79$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 39 | 25.6% | -0.232 | 📉 agota (-0.11) | -7.74$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 634 | 80.0% | +0.299 | 📉 agota (-0.03) | -8.96$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 93 | 39.8% | -0.100 | 📈 madura (+0.05) | -11.67$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 70 | 30.0% | -0.194 | ➡️ estable | -14.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 125 | 86.4% | +0.358 | 📈 madura (+0.08) | -17.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 324 | 77.2% | +0.270 | 📉 agota (-0.07) | -21.34$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 248 | 44.8% | -0.052 | 📉 agota (-0.07) | -25.98$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1824 | 54.7% | +0.047 | 📉 agota (-0.16) | -28.40$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 342 | 32.5% | -0.174 | ➡️ estable | -58.67$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2613 | 70.1% | +0.201 | 📉 agota (-0.05) | -170.18$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2588 | 42.7% | -0.073 | 📉 agota (-0.04) | -573.49$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 27189 | 61.9% | +0.119 | 📉 agota (-0.04) | -683.09$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12229 | 69.9% | +0.199 | ➡️ estable | -900.06$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T16:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.43$ |
| 2026-08-09T16:15 | FAVORITO_CONFIRMADO#DOGE#5min | … | ✅ WIN | +0.57$ |
| 2026-08-09T16:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.29$ |
| 2026-08-09T16:15 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.39$ |
| 2026-08-09T16:15 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 9, 11:55AM-12:00PM ET… | ✅ WIN | +0.52$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T16:14 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,210.00 | 0.1min |  |
| ✅ ETH | $1,924.82 | 0.1min |  |
| ✅ SOL | $77.30 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,210.00 | consenso |  |
| ETH | $1,925.03 | consenso |  |
| SOL | $77.40 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*