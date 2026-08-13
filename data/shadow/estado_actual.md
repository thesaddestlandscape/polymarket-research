# Estado del bot — 2026-08-13 10:13 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **5.97 $** |
| P&L real total | 🔴 **-45.25 $** |
| P&L real hoy | -2.18 $ |
| P&L real 7 días | -5.93 $ |
| Fees pagados (real) | 15.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6040.54 $ |
| P&L sim compuesto | 🟢 +16054.17 $ (ficción Kelly: +63106% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +314.38 $ |
| Operaciones resueltas | 125508 (76894 WIN / 48614 LOSS) — 61.3% |
| Señales abiertas | 423 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12297 | 61.4% | +0.114 | ➡️ estable | +5869.26$ | 0.61$ | ✅ activa |
| GBM_LATE_15M | 14445 | 60.2% | +0.102 | ➡️ estable | +4967.67$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11064 | 60.0% | +0.100 | 📈 madura (+0.07) | +4476.99$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3967 | 64.0% | +0.140 | 📉 agota (-0.03) | +1817.75$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1605 | 72.3% | +0.223 | ➡️ estable | +1367.15$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4561 | 55.5% | +0.055 | 📈 madura (+0.05) | +583.70$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 657 | 54.5% | +0.045 | ➡️ estable | +97.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1879 | 50.4% | +0.004 | 📈 madura (+0.07) | +89.79$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1742 | 51.5% | +0.015 | ➡️ estable | +18.45$ | 0.58$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2777 | 62.3% | +0.123 | ➡️ estable | +17.66$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 236 | 54.2% | +0.042 | 📈 madura (+0.03) | +3.90$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 207 | 53.1% | +0.031 | ➡️ estable | +2.33$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 170 | 93.5% | +0.430 | ➡️ estable | -2.25$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 1157 | 51.4% | +0.014 | ➡️ estable | -4.68$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2021 | 54.5% | +0.045 | 📉 agota (-0.18) | -13.49$ | 0.50$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 399 | 47.9% | -0.021 | 📈 madura (+0.03) | -20.30$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 715 | 78.9% | +0.288 | 📉 agota (-0.04) | -24.89$ | 2.00$ | ✅ activa |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 159 | 20.1% | -0.295 | 📈 madura (+0.12) | -28.88$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 228 | 38.2% | -0.117 | ➡️ estable | -33.46$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 385 | 31.7% | -0.182 | 📉 agota (-0.05) | -67.84$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3682 | 70.0% | +0.200 | ➡️ estable | -216.21$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4879 | 46.9% | -0.031 | 📈 madura (+0.08) | -753.79$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 35084 | 61.4% | +0.114 | ➡️ estable | -1214.37$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16871 | 69.8% | +0.198 | ➡️ estable | -1323.20$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T10:12 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.37$ |
| 2026-08-13T10:12 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-13T10:12 | GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | Bitcoin Up or Down - August 13, 5:45AM-6:00AM ET… | ✅ WIN | +0.72$ |
| 2026-08-13T10:12 | GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | Ethereum Up or Down - August 13, 5:45AM-6:00AM ET… | ✅ WIN | +1.16$ |
| 2026-08-13T10:12 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - August 13, 5:45AM-6:00AM ET… | ✅ WIN | +0.87$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T10:10 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,665.74 | 0.2min |  |
| ✅ ETH | $1,883.75 | 0.2min |  |
| ✅ SOL | $75.93 | 0.2min |  |
| ✅ XRP | $1.01 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,679.20 | consenso |  |
| ETH | $1,883.83 | consenso |  |
| SOL | $76.00 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*