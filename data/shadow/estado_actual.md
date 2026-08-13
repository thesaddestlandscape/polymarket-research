# Estado del bot — 2026-08-13 01:26 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **7.08 $** |
| P&L real total | 🔴 **-44.14 $** |
| P&L real hoy | -1.07 $ |
| P&L real 7 días | -4.82 $ |
| Fees pagados (real) | 15.49 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6063.47 $ |
| P&L sim compuesto | 🟢 +15852.30 $ (ficción Kelly: +62312% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +112.51 $ |
| Operaciones resueltas | 122738 (75240 WIN / 47498 LOSS) — 61.3% |
| Señales abiertas | 399 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12097 | 61.4% | +0.114 | ➡️ estable | +5792.84$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14289 | 60.2% | +0.102 | ➡️ estable | +4893.02$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10908 | 59.9% | +0.099 | 📈 madura (+0.06) | +4365.16$ | 1.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3889 | 64.5% | +0.145 | ➡️ estable | +1819.75$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1461 | 72.6% | +0.225 | ➡️ estable | +1267.92$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4492 | 55.5% | +0.055 | 📈 madura (+0.05) | +572.99$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 604 | 55.6% | +0.056 | ➡️ estable | +109.26$ | 0.64$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 184 | 76.1% | +0.258 | 📉 agota (-0.06) | +88.87$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1838 | 50.3% | +0.003 | 📈 madura (+0.08) | +82.42$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 346 | 80.1% | +0.299 | ➡️ estable | +58.28$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 433 | 43.4% | -0.066 | 📈 madura (+0.11) | +39.18$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1738 | 51.5% | +0.015 | ➡️ estable | +19.38$ | 0.60$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2621 | 62.2% | +0.122 | ➡️ estable | +18.68$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 329 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.77$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 37 | 78.4% | +0.269 | 📉 agota (-0.18) | +6.14$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 231 | 54.1% | +0.041 | 📈 madura (+0.04) | +4.82$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 166 | 94.0% | +0.435 | ➡️ estable | -0.55$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 202 | 53.0% | +0.029 | ➡️ estable | -0.66$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1103 | 51.2% | +0.012 | 📉 agota (-0.04) | -6.71$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2001 | 54.6% | +0.046 | 📉 agota (-0.18) | -8.87$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 160 | 89.4% | +0.389 | 📈 madura (+0.11) | -13.12$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 408 | 77.9% | +0.278 | 📉 agota (-0.04) | -18.25$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 373 | 46.9% | -0.031 | ➡️ estable | -23.84$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 706 | 78.9% | +0.288 | 📉 agota (-0.03) | -24.67$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 153 | 20.3% | -0.294 | 📈 madura (+0.11) | -27.57$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 422 | 44.8% | -0.052 | 📉 agota (-0.05) | -27.67$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 223 | 37.2% | -0.127 | 📉 agota (-0.05) | -34.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 378 | 31.2% | -0.187 | 📉 agota (-0.06) | -69.16$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3577 | 70.0% | +0.200 | ➡️ estable | -212.02$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4631 | 46.9% | -0.031 | 📈 madura (+0.09) | -725.85$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 34333 | 61.5% | +0.115 | ➡️ estable | -1123.53$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16432 | 69.8% | +0.198 | ➡️ estable | -1271.75$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T01:25 | BALLENAS_TARDIAS#BNB#5min | … | ✅ WIN | +0.31$ |
| 2026-08-13T01:25 | BALLENAS_TARDIAS#XRP#5min | … | ✅ WIN | +0.14$ |
| 2026-08-13T01:25 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.31$ |
| 2026-08-13T01:25 | GBM_LATE_5M#XRP#5min | XRP Up or Down - August 12, 9:10PM-9:15PM ET… | ✅ WIN | +2.00$ |
| 2026-08-13T01:25 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.35$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T01:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,504.00 | 0.1min |  |
| ✅ ETH | $1,878.96 | 0.1min |  |
| ✅ SOL | $75.61 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,504.00 | consenso |  |
| ETH | $1,879.38 | consenso |  |
| SOL | $75.64 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*