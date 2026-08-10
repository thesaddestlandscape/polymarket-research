# Estado del bot — 2026-08-10 05:53 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.98 $** |
| P&L real total | 🔴 **-42.24 $** |
| P&L real hoy | -1.08 $ |
| P&L real 7 días | -10.53 $ |
| Fees pagados (real) | 15.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6188.91 $ |
| P&L sim compuesto | 🟢 +14696.82 $ (ficción Kelly: +57771% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +321.34 $ |
| Operaciones resueltas | 103033 (63287 WIN / 39746 LOSS) — 61.4% |
| Señales abiertas | 491 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10915 | 62.2% | +0.122 | ➡️ estable | +5343.92$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13318 | 60.2% | +0.102 | ➡️ estable | +4519.09$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10181 | 59.2% | +0.092 | 📈 madura (+0.04) | +3775.84$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3551 | 66.2% | +0.162 | ➡️ estable | +1814.90$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 831 | 73.8% | +0.237 | 📈 madura (+0.05) | +733.23$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4028 | 55.9% | +0.059 | 📈 madura (+0.07) | +556.15$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 147 | 76.2% | +0.258 | 📉 agota (-0.06) | +75.38$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 315 | 80.6% | +0.304 | ➡️ estable | +61.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1585 | 48.7% | -0.013 | 📈 madura (+0.03) | +36.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1282 | 63.7% | +0.136 | ➡️ estable | +30.89$ | 1.36$ | ✅ activa |
| GBM_LATE_60M | 405 | 42.5% | -0.075 | 📈 madura (+0.12) | +18.55$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 696 | 53.0% | +0.030 | ➡️ estable | +11.81$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 134 | 51.5% | +0.015 | 📈 madura (+0.04) | -0.03$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 139 | 93.5% | +0.429 | 📈 madura (+0.04) | -1.74$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 641 | 79.7% | +0.296 | 📉 agota (-0.04) | -12.93$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1849 | 54.9% | +0.049 | 📉 agota (-0.16) | -12.94$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 335 | 77.0% | +0.269 | 📉 agota (-0.09) | -23.16$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2761 | 70.2% | +0.201 | 📉 agota (-0.04) | -175.36$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2872 | 43.4% | -0.066 | ➡️ estable | -637.79$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28389 | 61.9% | +0.119 | 📉 agota (-0.03) | -699.20$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12916 | 69.9% | +0.199 | ➡️ estable | -952.16$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T05:52 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.18$ |
| 2026-08-10T05:52 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.24$ |
| 2026-08-10T05:52 | GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | Ethereum Up or Down - August 10, 1:30AM-1:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-08-10T05:52 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - August 10, 1:30AM-1:45AM ET… | ❌ LOSS | -1.35$ |
| 2026-08-10T05:52 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - August 10, 1:30AM-1:45AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T05:51 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,019.00 | 0.1min |  |
| ✅ ETH | $1,919.69 | 0.1min |  |
| ✅ SOL | $76.84 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,019.00 | consenso |  |
| ETH | $1,919.97 | consenso |  |
| SOL | $76.73 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*