# Estado del bot — 2026-08-10 11:13 UTC

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
| P&L fiel (stake fijo 1$) | +6172.27 $ |
| P&L sim compuesto | 🟢 +14772.82 $ (ficción Kelly: +58069% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +397.35 $ |
| Operaciones resueltas | 104420 (64148 WIN / 40272 LOSS) — 61.4% |
| Señales abiertas | 489 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11014 | 62.1% | +0.121 | ➡️ estable | +5350.22$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 13391 | 60.2% | +0.102 | ➡️ estable | +4537.30$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10222 | 59.3% | +0.093 | 📈 madura (+0.04) | +3801.66$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3561 | 66.1% | +0.161 | ➡️ estable | +1809.79$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 868 | 74.1% | +0.240 | 📈 madura (+0.06) | +781.13$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4035 | 55.9% | +0.059 | 📈 madura (+0.07) | +555.97$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 441 | 54.9% | +0.049 | 📉 agota (-0.13) | +96.75$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 151 | 76.2% | +0.258 | 📉 agota (-0.07) | +77.76$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 319 | 80.6% | +0.304 | ➡️ estable | +62.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1588 | 48.7% | -0.013 | 📈 madura (+0.04) | +36.38$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 406 | 42.4% | -0.076 | 📈 madura (+0.11) | +18.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1390 | 62.9% | +0.129 | ➡️ estable | +17.71$ | 1.29$ | ✅ activa |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| STRUCT_NO_15M | 738 | 52.7% | +0.027 | ➡️ estable | +9.41$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 131 | 52.7% | +0.026 | 📈 madura (+0.07) | +0.34$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 142 | 51.4% | +0.014 | 📈 madura (+0.04) | -0.81$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 142 | 93.7% | +0.431 | 📈 madura (+0.04) | -1.45$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 649 | 79.7% | +0.296 | ➡️ estable | -13.75$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 112 | 39.3% | -0.105 | 📈 madura (+0.03) | -14.78$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 80 | 31.2% | -0.183 | ➡️ estable | -16.05$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 130 | 86.9% | +0.364 | 📈 madura (+0.10) | -16.88$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1862 | 54.8% | +0.048 | 📉 agota (-0.16) | -17.85$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 343 | 77.3% | +0.271 | 📉 agota (-0.09) | -21.52$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 129 | 18.6% | -0.309 | 📈 madura (+0.09) | -25.99$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2830 | 70.2% | +0.202 | 📉 agota (-0.04) | -175.56$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2966 | 44.0% | -0.060 | 📈 madura (+0.04) | -618.42$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28857 | 61.9% | +0.119 | 📉 agota (-0.03) | -707.73$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13183 | 70.0% | +0.200 | ➡️ estable | -954.96$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T11:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T11:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T11:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.37$ |
| 2026-08-10T11:11 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T11:11 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.47$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T11:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,941.12 | 0.2min |  |
| ✅ ETH | $1,914.76 | 0.2min |  |
| ✅ SOL | $76.72 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,956.50 | consenso |  |
| ETH | $1,915.25 | consenso |  |
| SOL | $76.67 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*