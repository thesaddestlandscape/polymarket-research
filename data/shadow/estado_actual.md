# Estado del bot — 2026-08-11 05:10 UTC

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
| P&L fiel (stake fijo 1$) | +6205.42 $ |
| P&L sim compuesto | 🟢 +15164.62 $ (ficción Kelly: +59609% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🔴 -3.50 $ |
| Operaciones resueltas | 109027 (67014 WIN / 42013 LOSS) — 61.5% |
| Señales abiertas | 503 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11254 | 61.9% | +0.119 | ➡️ estable | +5558.97$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13582 | 60.3% | +0.103 | ➡️ estable | +4632.22$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10371 | 59.4% | +0.094 | 📈 madura (+0.05) | +3916.37$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3594 | 65.9% | +0.159 | ➡️ estable | +1817.18$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 995 | 74.8% | +0.247 | 📈 madura (+0.07) | +912.87$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4066 | 55.9% | +0.059 | 📈 madura (+0.07) | +559.64$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 159 | 76.7% | +0.264 | 📉 agota (-0.03) | +83.84$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 326 | 80.7% | +0.305 | ➡️ estable | +64.41$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1639 | 49.2% | -0.008 | 📈 madura (+0.05) | +42.94$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1746 | 62.9% | +0.129 | ➡️ estable | +24.50$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1726 | 51.4% | +0.014 | ➡️ estable | +15.92$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 416 | 42.3% | -0.077 | 📈 madura (+0.10) | +13.94$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 823 | 53.0% | +0.030 | ➡️ estable | +11.37$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 176 | 54.0% | +0.039 | ➡️ estable | -0.87$ | 0.50$ | ✅ activa |
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
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3040 | 70.0% | +0.200 | ➡️ estable | -190.61$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3376 | 45.2% | -0.048 | 📈 madura (+0.06) | -640.08$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30443 | 61.8% | +0.118 | ➡️ estable | -802.67$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14074 | 70.0% | +0.200 | ➡️ estable | -1033.19$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T05:07 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.77$ |
| 2026-08-11T05:07 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T05:07 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T05:07 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T05:07 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T05:05 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,936.69 | 0.1min |  |
| ✅ ETH | $1,874.27 | 0.1min |  |
| ✅ SOL | $76.03 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,950.10 | consenso |  |
| ETH | $1,874.27 | consenso |  |
| SOL | $76.01 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*