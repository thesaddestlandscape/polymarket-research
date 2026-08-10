# Estado del bot — 2026-08-10 12:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.54 $** |
| P&L real total | 🔴 **-42.68 $** |
| P&L real hoy | -1.52 $ |
| P&L real 7 días | -10.97 $ |
| Fees pagados (real) | 15.12 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6165.74 $ |
| P&L sim compuesto | 🟢 +14776.24 $ (ficción Kelly: +58083% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +400.76 $ |
| Operaciones resueltas | 104756 (64359 WIN / 40397 LOSS) — 61.4% |
| Señales abiertas | 493 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11037 | 62.1% | +0.121 | ➡️ estable | +5347.32$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13408 | 60.2% | +0.102 | ➡️ estable | +4540.44$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10231 | 59.3% | +0.093 | 📈 madura (+0.04) | +3809.06$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3563 | 66.0% | +0.160 | ➡️ estable | +1807.65$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 874 | 74.1% | +0.241 | 📈 madura (+0.06) | +789.06$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4036 | 55.9% | +0.059 | 📈 madura (+0.07) | +556.58$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 441 | 54.9% | +0.049 | 📉 agota (-0.13) | +96.75$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 152 | 76.3% | +0.260 | 📉 agota (-0.05) | +78.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 321 | 80.7% | +0.305 | ➡️ estable | +63.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1593 | 48.8% | -0.012 | 📈 madura (+0.04) | +37.89$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1415 | 62.9% | +0.129 | ➡️ estable | +16.37$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 744 | 52.6% | +0.025 | ➡️ estable | +8.24$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 134 | 53.7% | +0.037 | 📈 madura (+0.06) | +1.76$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 144 | 51.4% | +0.014 | ➡️ estable | -0.27$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 650 | 79.7% | +0.296 | ➡️ estable | -13.66$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 112 | 39.3% | -0.105 | 📈 madura (+0.03) | -14.78$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 80 | 31.2% | -0.183 | ➡️ estable | -16.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 132 | 87.1% | +0.366 | 📈 madura (+0.10) | -16.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1864 | 54.8% | +0.048 | 📉 agota (-0.16) | -19.03$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 346 | 77.5% | +0.273 | 📉 agota (-0.09) | -19.69$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 130 | 18.5% | -0.311 | 📈 madura (+0.09) | -26.50$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2846 | 70.2% | +0.202 | 📉 agota (-0.04) | -177.06$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2990 | 44.0% | -0.059 | 📈 madura (+0.04) | -620.88$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28972 | 61.9% | +0.119 | 📉 agota (-0.03) | -709.23$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13252 | 70.0% | +0.200 | ➡️ estable | -963.03$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T12:31 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.71$ |
| 2026-08-10T12:31 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.57$ |
| 2026-08-10T12:31 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.62$ |
| 2026-08-10T12:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T12:31 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 10, 8:10AM-8:15AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T12:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,006.57 | 0.1min |  |
| ✅ ETH | $1,915.23 | 0.1min |  |
| ✅ SOL | $76.91 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,013.60 | consenso |  |
| ETH | $1,915.23 | consenso |  |
| SOL | $76.86 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*