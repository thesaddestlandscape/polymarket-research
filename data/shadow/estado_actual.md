# Estado del bot — 2026-08-13 12:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **15.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5978.31 $ |
| P&L sim compuesto | 🟢 +16012.24 $ (ficción Kelly: +62941% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +272.45 $ |
| Operaciones resueltas | 126136 (77237 WIN / 48899 LOSS) — 61.2% |
| Señales abiertas | 469 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12341 | 61.3% | +0.113 | ➡️ estable | +5858.89$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14475 | 60.2% | +0.102 | ➡️ estable | +4980.00$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11100 | 60.0% | +0.100 | 📈 madura (+0.07) | +4484.46$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3976 | 63.9% | +0.139 | 📉 agota (-0.03) | +1816.86$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1630 | 72.3% | +0.222 | ➡️ estable | +1380.43$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4582 | 55.5% | +0.055 | 📈 madura (+0.05) | +584.76$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 674 | 54.2% | +0.041 | ➡️ estable | +95.73$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1889 | 50.5% | +0.005 | 📈 madura (+0.07) | +92.49$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2818 | 62.3% | +0.123 | ➡️ estable | +20.66$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1744 | 51.5% | +0.015 | ➡️ estable | +18.39$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 237 | 54.4% | +0.044 | 📈 madura (+0.04) | +4.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 209 | 52.6% | +0.026 | ➡️ estable | -0.22$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 171 | 93.6% | +0.431 | ➡️ estable | -2.17$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 11 | 27.3% | -0.106 | — | -2.70$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1161 | 51.3% | +0.013 | ➡️ estable | -5.77$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 2024 | 54.5% | +0.045 | 📉 agota (-0.18) | -12.24$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 408 | 47.8% | -0.022 | 📈 madura (+0.03) | -22.46$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 426 | 45.1% | -0.049 | 📉 agota (-0.05) | -26.72$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 717 | 78.8% | +0.287 | 📉 agota (-0.03) | -26.86$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 159 | 20.1% | -0.295 | 📈 madura (+0.12) | -28.88$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 236 | 38.6% | -0.113 | ➡️ estable | -33.82$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 386 | 31.6% | -0.183 | 📉 agota (-0.05) | -68.35$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3699 | 70.0% | +0.200 | ➡️ estable | -220.07$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4940 | 46.7% | -0.033 | 📈 madura (+0.07) | -789.87$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 35265 | 61.4% | +0.114 | ➡️ estable | -1218.56$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16968 | 69.7% | +0.197 | ➡️ estable | -1340.99$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T12:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.23$ |
| 2026-08-13T12:14 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T12:14 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.29$ |
| 2026-08-13T12:14 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-13T12:14 | UPDOWN_GBM_15M_TARDIO#SOL#15min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T12:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,456.85 | 0.2min |  |
| ✅ ETH | $1,880.83 | 0.2min |  |
| ✅ SOL | $75.73 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,466.30 | consenso |  |
| ETH | $1,881.01 | consenso |  |
| SOL | $75.73 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*