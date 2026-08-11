# Estado del bot — 2026-08-11 11:38 UTC

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
| P&L fiel (stake fijo 1$) | +6212.25 $ |
| P&L sim compuesto | 🟢 +15287.26 $ (ficción Kelly: +60091% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +119.14 $ |
| Operaciones resueltas | 110797 (68097 WIN / 42700 LOSS) — 61.5% |
| Señales abiertas | 553 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11355 | 61.8% | +0.118 | ➡️ estable | +5584.87$ | 0.58$ | ✅ activa |
| GBM_LATE_15M | 13661 | 60.3% | +0.103 | ➡️ estable | +4680.27$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10430 | 59.5% | +0.095 | 📈 madura (+0.05) | +3972.69$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3603 | 65.8% | +0.158 | ➡️ estable | +1815.68$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1047 | 74.6% | +0.245 | 📈 madura (+0.06) | +966.33$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4079 | 55.9% | +0.059 | 📈 madura (+0.06) | +563.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 454 | 54.8% | +0.048 | 📉 agota (-0.13) | +99.55$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1670 | 49.6% | -0.004 | 📈 madura (+0.06) | +59.45$ | 0.90$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1869 | 63.3% | +0.133 | ➡️ estable | +37.27$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 868 | 52.4% | +0.024 | ➡️ estable | +7.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 190 | 54.2% | +0.042 | ➡️ estable | +4.10$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1912 | 55.1% | +0.051 | 📉 agota (-0.15) | +1.43$ | 0.74$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 158 | 51.9% | +0.019 | ➡️ estable | -1.64$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 140 | 87.9% | +0.373 | 📈 madura (+0.10) | -15.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 364 | 78.0% | +0.279 | 📉 agota (-0.07) | -15.97$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 663 | 79.5% | +0.294 | ➡️ estable | -16.72$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 89 | 30.3% | -0.192 | ➡️ estable | -18.71$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 155 | 38.1% | -0.118 | 📉 agota (-0.04) | -23.61$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 267 | 46.1% | -0.039 | ➡️ estable | -23.68$ | 0.91$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 341 | 43.1% | -0.069 | 📉 agota (-0.12) | -31.04$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 348 | 31.9% | -0.180 | ➡️ estable | -61.73$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3122 | 70.1% | +0.201 | ➡️ estable | -189.26$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3549 | 45.4% | -0.045 | 📈 madura (+0.07) | -675.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31007 | 61.8% | +0.118 | ➡️ estable | -843.36$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14396 | 69.9% | +0.199 | ➡️ estable | -1068.68$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T11:37 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.15$ |
| 2026-08-11T11:37 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 11, 7:20AM-7:25AM ET… | ✅ WIN | +2.08$ |
| 2026-08-11T11:37 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.35$ |
| 2026-08-11T11:37 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T11:37 | FAVORITO_CONFIRMADO#XRP#5min | … | ✅ WIN | +0.68$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T11:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,281.21 | 0.2min |  |
| ✅ ETH | $1,890.19 | 0.2min |  |
| ✅ SOL | $76.08 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,281.21 | consenso |  |
| ETH | $1,890.19 | consenso |  |
| SOL | $76.08 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*