# Estado del bot — 2026-08-09 09:29 UTC

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
| P&L fiel (stake fijo 1$) | +6054.70 $ |
| P&L sim compuesto | 🟢 +14188.09 $ (ficción Kelly: +55771% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +128.18 $ |
| Operaciones resueltas | 97684 (59881 WIN / 37803 LOSS) — 61.3% |
| Señales abiertas | 792 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10531 | 62.3% | +0.123 | ➡️ estable | +5227.87$ | 1.23$ | ✅ activa |
| GBM_LATE_15M | 13025 | 60.2% | +0.102 | ➡️ estable | +4396.21$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9999 | 58.9% | +0.089 | 📈 madura (+0.03) | +3580.06$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3515 | 66.3% | +0.163 | ➡️ estable | +1805.97$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4007 | 55.9% | +0.059 | 📈 madura (+0.07) | +561.28$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 682 | 71.7% | +0.216 | ➡️ estable | +531.12$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 137 | 75.9% | +0.255 | 📉 agota (-0.04) | +73.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 307 | 80.5% | +0.303 | ➡️ estable | +59.68$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1532 | 48.6% | -0.014 | 📈 madura (+0.04) | +40.67$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 904 | 63.7% | +0.137 | 📈 madura (+0.03) | +23.24$ | 1.37$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| STRUCT_NO_15M | 549 | 53.0% | +0.030 | ➡️ estable | +4.89$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 111 | 52.3% | +0.022 | 📈 madura (+0.06) | -0.14$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 126 | 93.7% | +0.430 | 📈 madura (+0.06) | -1.09$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 102 | 52.9% | +0.029 | 📈 madura (+0.08) | -1.88$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 628 | 79.9% | +0.298 | 📉 agota (-0.04) | -8.53$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 68 | 30.9% | -0.186 | ➡️ estable | -13.79$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 123 | 86.2% | +0.356 | 📈 madura (+0.08) | -17.70$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 317 | 77.3% | +0.271 | 📉 agota (-0.10) | -20.45$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1810 | 54.8% | +0.047 | 📉 agota (-0.17) | -22.34$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2528 | 69.9% | +0.198 | 📉 agota (-0.06) | -177.16$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 2501 | 43.2% | -0.068 | 📉 agota (-0.04) | -553.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26596 | 61.9% | +0.119 | 📉 agota (-0.05) | -685.56$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11864 | 69.8% | +0.198 | ➡️ estable | -883.17$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T09:28 | GBM_LATE_5M#SOL#5min | Solana Up or Down - August 9, 5:15AM-5:20AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-09T09:28 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T09:28 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.57$ |
| 2026-08-09T09:28 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.65$ |
| 2026-08-09T09:28 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T09:26 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,780.99 | 0.1min |  |
| ✅ ETH | $1,913.32 | 0.1min |  |
| ✅ SOL | $76.31 | 0.1min |  |
| ✅ XRP | $1.03 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,780.99 | consenso |  |
| ETH | $1,913.32 | consenso |  |
| SOL | $76.30 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*