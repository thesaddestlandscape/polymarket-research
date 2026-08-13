# Estado del bot — 2026-08-13 11:55 UTC

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
| P&L fiel (stake fijo 1$) | +5968.82 $ |
| P&L sim compuesto | 🟢 +15983.85 $ (ficción Kelly: +62830% s/ operativo) |
| P&L sim hoy (2026-08-13) | 🟢 +244.06 $ |
| Operaciones resueltas | 126017 (77160 WIN / 48857 LOSS) — 61.2% |
| Señales abiertas | 469 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12331 | 61.3% | +0.113 | ➡️ estable | +5855.59$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14469 | 60.2% | +0.102 | ➡️ estable | +4969.21$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11092 | 60.0% | +0.100 | 📈 madura (+0.07) | +4475.48$ | 1.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3972 | 63.9% | +0.139 | 📉 agota (-0.03) | +1818.58$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1626 | 72.3% | +0.223 | ➡️ estable | +1380.28$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4570 | 55.6% | +0.056 | 📈 madura (+0.05) | +585.50$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 780 | 77.9% | +0.279 | 📈 madura (+0.14) | +342.55$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 670 | 54.2% | +0.042 | ➡️ estable | +95.71$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 189 | 76.2% | +0.259 | 📉 agota (-0.07) | +93.60$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1887 | 50.5% | +0.004 | 📈 madura (+0.07) | +89.13$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 350 | 79.7% | +0.295 | ➡️ estable | +56.33$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 440 | 43.6% | -0.063 | 📈 madura (+0.12) | +45.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2813 | 62.3% | +0.123 | ➡️ estable | +20.39$ | 1.23$ | ✅ activa |
| ORDER_FLOW_5M | 1744 | 51.5% | +0.015 | ➡️ estable | +18.39$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 330 | 55.5% | +0.054 | 📉 agota (-0.14) | +12.22$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 38 | 78.9% | +0.275 | 📉 agota (-0.10) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 237 | 54.4% | +0.044 | 📈 madura (+0.04) | +4.46$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 208 | 52.9% | +0.029 | ➡️ estable | +0.29$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 170 | 93.5% | +0.430 | ➡️ estable | -2.25$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 1161 | 51.3% | +0.013 | ➡️ estable | -5.77$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 198 | 34.3% | -0.155 | 📉 agota (-0.08) | -6.26$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 396 | 43.9% | -0.060 | 📉 agota (-0.13) | -6.46$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 164 | 89.6% | +0.392 | 📈 madura (+0.11) | -12.77$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2022 | 54.5% | +0.044 | 📉 agota (-0.18) | -14.00$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 70 | 21.4% | -0.278 | 📉 agota (-0.08) | -17.69$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 414 | 78.0% | +0.279 | 📉 agota (-0.04) | -18.15$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 129 | 36.4% | -0.134 | 📈 madura (+0.13) | -18.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 408 | 47.8% | -0.022 | 📈 madura (+0.03) | -22.46$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 425 | 45.2% | -0.048 | 📉 agota (-0.04) | -26.21$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 716 | 78.8% | +0.287 | 📉 agota (-0.03) | -26.93$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 159 | 20.1% | -0.295 | 📈 madura (+0.12) | -28.88$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 234 | 38.5% | -0.114 | ➡️ estable | -33.75$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 386 | 31.6% | -0.183 | 📉 agota (-0.05) | -68.35$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3694 | 70.0% | +0.200 | ➡️ estable | -219.00$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 4934 | 46.7% | -0.033 | 📈 madura (+0.07) | -786.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 35235 | 61.3% | +0.113 | ➡️ estable | -1224.58$ | 1.06$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 16955 | 69.7% | +0.197 | ➡️ estable | -1343.94$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-13T11:54 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T11:54 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.37$ |
| 2026-08-13T11:54 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-13T11:54 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.57$ |
| 2026-08-13T11:54 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-13T11:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,395.51 | 0.2min |  |
| ✅ ETH | $1,876.55 | 0.2min |  |
| ✅ SOL | $75.56 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,408.20 | consenso |  |
| ETH | $1,877.24 | consenso |  |
| SOL | $75.56 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*