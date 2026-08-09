# Estado del bot — 2026-08-09 07:58 UTC

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
| P&L fiel (stake fijo 1$) | +6044.41 $ |
| P&L sim compuesto | 🟢 +14172.52 $ (ficción Kelly: +55710% s/ operativo) |
| P&L sim hoy (2026-08-09) | 🟢 +112.61 $ |
| Operaciones resueltas | 97302 (59659 WIN / 37643 LOSS) — 61.3% |
| Señales abiertas | 773 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10509 | 62.4% | +0.124 | ➡️ estable | +5212.20$ | 1.23$ | ✅ activa |
| GBM_LATE_15M | 13008 | 60.2% | +0.102 | ➡️ estable | +4387.88$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9986 | 58.9% | +0.089 | 📈 madura (+0.03) | +3556.51$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3512 | 66.3% | +0.163 | ➡️ estable | +1803.21$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4004 | 55.9% | +0.059 | 📈 madura (+0.07) | +563.54$ | 0.59$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 674 | 71.7% | +0.216 | ➡️ estable | +508.28$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 436 | 55.0% | +0.050 | 📉 agota (-0.14) | +97.89$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1527 | 48.6% | -0.014 | 📈 madura (+0.03) | +40.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 872 | 63.8% | +0.137 | 📈 madura (+0.03) | +23.27$ | 1.37$ | ✅ activa |
| GBM_LATE_60M | 398 | 42.5% | -0.075 | 📈 madura (+0.12) | +16.84$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 537 | 52.9% | +0.029 | ➡️ estable | +4.18$ | 0.50$ | ✅ activa |
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
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2507 | 70.0% | +0.199 | 📉 agota (-0.06) | -174.14$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2474 | 43.3% | -0.067 | 📉 agota (-0.04) | -543.66$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 26459 | 61.9% | +0.119 | 📉 agota (-0.05) | -661.84$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11793 | 69.8% | +0.198 | ➡️ estable | -878.53$ | 1.98$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-09T07:57 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-09T07:57 | FAVORITO_CONFIRMADO#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T07:57 | FAVORITO_CONFIRMADO#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-09T07:57 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.31$ |
| 2026-08-09T07:57 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-09T07:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,767.14 | 0.1min |  |
| ✅ ETH | $1,916.34 | 0.1min |  |
| ✅ SOL | $76.31 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,787.10 | consenso |  |
| ETH | $1,916.34 | consenso |  |
| SOL | $76.24 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*