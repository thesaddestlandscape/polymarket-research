# Estado del bot — 2026-08-11 05:27 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | -32.86 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6203.18 $ |
| P&L sim compuesto | 🟢 +15171.47 $ (ficción Kelly: +59636% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +3.35 $ |
| Operaciones resueltas | 109118 (67065 WIN / 42053 LOSS) — 61.5% |
| Señales abiertas | 481 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11258 | 61.9% | +0.119 | ➡️ estable | +5558.81$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13587 | 60.3% | +0.103 | ➡️ estable | +4640.03$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10375 | 59.4% | +0.094 | 📈 madura (+0.05) | +3923.61$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3594 | 65.9% | +0.159 | ➡️ estable | +1817.18$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 999 | 74.9% | +0.248 | 📈 madura (+0.07) | +922.47$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4066 | 55.9% | +0.059 | 📈 madura (+0.07) | +559.64$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 159 | 76.7% | +0.264 | 📉 agota (-0.03) | +83.84$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 326 | 80.7% | +0.305 | ➡️ estable | +64.41$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1640 | 49.2% | -0.008 | 📈 madura (+0.05) | +43.43$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1754 | 62.9% | +0.129 | ➡️ estable | +24.74$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1728 | 51.4% | +0.014 | ➡️ estable | +16.96$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 417 | 42.2% | -0.078 | 📈 madura (+0.09) | +13.43$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 826 | 53.0% | +0.030 | ➡️ estable | +11.82$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 178 | 53.9% | +0.039 | ➡️ estable | +0.43$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1905 | 55.1% | +0.051 | 📉 agota (-0.15) | -0.93$ | 0.51$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 145 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.08$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 153 | 51.6% | +0.016 | ➡️ estable | -1.79$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 137 | 87.6% | +0.371 | 📈 madura (+0.10) | -15.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 660 | 79.5% | +0.295 | 📉 agota (-0.03) | -16.23$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 360 | 77.8% | +0.276 | 📉 agota (-0.08) | -17.28$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 142 | 38.7% | -0.111 | ➡️ estable | -20.04$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 135 | 18.5% | -0.310 | 📈 madura (+0.07) | -27.97$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3046 | 70.0% | +0.200 | ➡️ estable | -192.60$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3383 | 45.2% | -0.048 | 📈 madura (+0.06) | -641.64$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30473 | 61.8% | +0.118 | ➡️ estable | -817.92$ | 1.17$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14088 | 70.0% | +0.200 | ➡️ estable | -1035.05$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T05:26 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T05:26 | STRUCT_NO_15M#ETH#15min | Ethereum Up or Down - August 11, 1:00AM-1:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-11T05:26 | GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | BNB Up or Down - August 11, 1:00AM-1:15AM ET… | ✅ WIN | +1.96$ |
| 2026-08-11T05:26 | GBM_LATE_15M_TARDIO#BNB#15min | BNB Up or Down - August 11, 1:00AM-1:15AM ET… | ✅ WIN | +1.96$ |
| 2026-08-11T05:26 | GBM_LATE_15M#BNB#15min | BNB Up or Down - August 11, 1:00AM-1:15AM ET… | ✅ WIN | +1.41$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T05:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,968.61 | 0.1min |  |
| ✅ ETH | $1,873.70 | 0.1min |  |
| ✅ SOL | $75.81 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,978.50 | consenso |  |
| ETH | $1,874.61 | consenso |  |
| SOL | $76.00 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*