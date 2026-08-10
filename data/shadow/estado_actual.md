# Estado del bot — 2026-08-10 09:44 UTC

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
| P&L fiel (stake fijo 1$) | +6190.40 $ |
| P&L sim compuesto | 🟢 +14756.73 $ (ficción Kelly: +58006% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +381.26 $ |
| Operaciones resueltas | 104015 (63906 WIN / 40109 LOSS) — 61.4% |
| Señales abiertas | 488 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10984 | 62.1% | +0.121 | ➡️ estable | +5344.29$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13368 | 60.2% | +0.102 | ➡️ estable | +4532.51$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10204 | 59.3% | +0.093 | 📈 madura (+0.04) | +3794.96$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3561 | 66.1% | +0.161 | ➡️ estable | +1809.79$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 853 | 73.9% | +0.238 | 📈 madura (+0.06) | +761.50$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4035 | 55.9% | +0.059 | 📈 madura (+0.07) | +555.97$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 151 | 76.2% | +0.258 | 📉 agota (-0.07) | +77.76$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 319 | 80.6% | +0.304 | ➡️ estable | +62.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1586 | 48.7% | -0.013 | 📈 madura (+0.04) | +36.54$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1358 | 63.0% | +0.129 | ➡️ estable | +17.97$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 732 | 52.6% | +0.026 | ➡️ estable | +8.47$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 128 | 53.1% | +0.031 | 📈 madura (+0.06) | +0.51$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 140 | 51.4% | +0.014 | ➡️ estable | -0.83$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 142 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.45$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 646 | 79.7% | +0.296 | ➡️ estable | -12.92$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 130 | 86.9% | +0.364 | 📈 madura (+0.10) | -16.88$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1859 | 54.8% | +0.048 | 📉 agota (-0.16) | -18.45$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 342 | 77.2% | +0.270 | 📉 agota (-0.09) | -22.24$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 128 | 18.8% | -0.308 | 📈 madura (+0.09) | -25.48$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2812 | 70.2% | +0.201 | 📉 agota (-0.04) | -175.84$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2933 | 43.9% | -0.060 | 📈 madura (+0.04) | -614.41$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28726 | 61.9% | +0.119 | 📉 agota (-0.03) | -707.87$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13109 | 70.1% | +0.201 | ➡️ estable | -942.35$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T09:43 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T09:43 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.37$ |
| 2026-08-10T09:43 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.57$ |
| 2026-08-10T09:43 | FAVORITO_CONFIRMADO#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T09:43 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.26$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T09:41 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,058.14 | 0.3min |  |
| ✅ ETH | $1,917.60 | 0.3min |  |
| ✅ SOL | $76.73 | 0.3min |  |
| ✅ XRP | $1.03 | 0.3min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,019.29 | consenso |  |
| ETH | $1,917.02 | consenso |  |
| SOL | $76.68 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*