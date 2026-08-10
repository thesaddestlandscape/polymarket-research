# Estado del bot — 2026-08-10 13:48 UTC

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
| P&L fiel (stake fijo 1$) | +6172.21 $ |
| P&L sim compuesto | 🟢 +14808.94 $ (ficción Kelly: +58211% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +433.47 $ |
| Operaciones resueltas | 105078 (64558 WIN / 40520 LOSS) — 61.4% |
| Señales abiertas | 495 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11063 | 62.1% | +0.121 | ➡️ estable | +5354.09$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13430 | 60.2% | +0.102 | ➡️ estable | +4553.94$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10248 | 59.3% | +0.093 | 📈 madura (+0.04) | +3817.08$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3566 | 66.0% | +0.160 | ➡️ estable | +1809.69$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 889 | 74.2% | +0.242 | 📈 madura (+0.07) | +804.93$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4040 | 55.9% | +0.059 | 📈 madura (+0.07) | +554.22$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 442 | 54.8% | +0.047 | 📉 agota (-0.13) | +96.24$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 152 | 76.3% | +0.260 | 📉 agota (-0.05) | +78.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 321 | 80.7% | +0.305 | ➡️ estable | +63.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1594 | 48.9% | -0.011 | 📈 madura (+0.04) | +39.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1445 | 63.1% | +0.131 | ➡️ estable | +22.65$ | 1.31$ | ✅ activa |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 752 | 52.9% | +0.029 | ➡️ estable | +11.32$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 134 | 53.7% | +0.037 | 📈 madura (+0.06) | +1.76$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 147 | 51.7% | +0.017 | ➡️ estable | -0.91$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.36$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 651 | 79.7% | +0.296 | ➡️ estable | -12.92$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 113 | 39.8% | -0.100 | 📈 madura (+0.04) | -14.30$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 80 | 31.2% | -0.183 | ➡️ estable | -16.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 132 | 87.1% | +0.366 | 📈 madura (+0.10) | -16.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1867 | 54.8% | +0.048 | 📉 agota (-0.17) | -19.61$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 346 | 77.5% | +0.273 | 📉 agota (-0.09) | -19.69$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 130 | 18.5% | -0.311 | 📈 madura (+0.09) | -26.50$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2854 | 70.1% | +0.201 | 📉 agota (-0.04) | -180.63$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3015 | 44.1% | -0.059 | 📈 madura (+0.05) | -617.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 29081 | 61.9% | +0.119 | 📉 agota (-0.03) | -723.29$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13297 | 70.0% | +0.200 | ➡️ estable | -970.36$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T13:47 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T13:47 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T13:47 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.65$ |
| 2026-08-10T13:47 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-10T13:47 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T13:45 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,594.00 | 0.1min |  |
| ✅ ETH | $1,899.67 | 0.1min |  |
| ✅ SOL | $76.31 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,600.00 | consenso |  |
| ETH | $1,900.00 | consenso |  |
| SOL | $76.30 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*