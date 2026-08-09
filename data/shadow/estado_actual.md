# Estado del bot — 2026-08-09 08:40 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.44 $** |
| P&L real total | 🔴 **-40.78 $** |
| P&L real hoy | -0.78 $ |
| P&L real 7 días | -11.15 $ |
| Fees pagados (real) | 14.97 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6042.91 $ |
| P&L sim compuesto | 🟢 +14168.76 $ (ficción Kelly: +55695% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +108.85 $ |
| Operaciones resueltas | 97474 (59762 WIN / 37712 LOSS) — 61.3% |
| Señales abiertas | 787 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10518 | 62.4% | +0.123 | ➡️ estable | +5215.42$ | 1.23$ | ✅ activa |
| GBM_LATE_15M | 13016 | 60.2% | +0.102 | ➡️ estable | +4388.61$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9992 | 58.9% | +0.089 | 📈 madura (+0.03) | +3562.49$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3515 | 66.3% | +0.163 | ➡️ estable | +1805.97$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4006 | 55.9% | +0.059 | 📈 madura (+0.07) | +562.90$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 676 | 71.6% | +0.215 | ➡️ estable | +508.32$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 137 | 75.9% | +0.255 | 📉 agota (-0.04) | +73.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 307 | 80.5% | +0.303 | ➡️ estable | +59.68$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1529 | 48.6% | -0.014 | 📈 madura (+0.03) | +39.37$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 886 | 63.9% | +0.139 | 📈 madura (+0.04) | +25.77$ | 1.39$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| STRUCT_NO_15M | 543 | 53.0% | +0.030 | ➡️ estable | +5.05$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 109 | 53.2% | +0.032 | 📈 madura (+0.10) | +3.43$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 126 | 93.7% | +0.430 | 📈 madura (+0.06) | -1.09$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 102 | 52.9% | +0.029 | 📈 madura (+0.08) | -1.88$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 627 | 80.1% | +0.300 | 📉 agota (-0.04) | -6.49$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 67 | 31.3% | -0.181 | 📈 madura (+0.08) | -13.28$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 121 | 87.6% | +0.370 | 📈 madura (+0.11) | -13.62$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 315 | 77.8% | +0.276 | 📉 agota (-0.10) | -16.37$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1810 | 54.8% | +0.047 | 📉 agota (-0.17) | -22.34$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2517 | 69.9% | +0.199 | 📉 agota (-0.06) | -178.61$ | 1.99$ | ✅ activa |
| BALLENAS_TARDIAS | 2486 | 43.2% | -0.068 | 📉 agota (-0.05) | -552.21$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26522 | 61.9% | +0.119 | 📉 agota (-0.04) | -664.24$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11825 | 69.8% | +0.198 | ➡️ estable | -880.72$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T08:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.31$ |
| 2026-08-09T08:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.16$ |
| 2026-08-09T08:39 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +1.77$ |
| 2026-08-09T08:39 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T08:39 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.26$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T08:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,841.43 | 0.1min |  |
| ✅ ETH | $1,919.93 | 0.1min |  |
| ✅ SOL | $76.38 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,841.43 | consenso |  |
| ETH | $1,919.95 | consenso |  |
| SOL | $76.36 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*