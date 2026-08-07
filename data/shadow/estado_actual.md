# Estado del bot — 2026-08-07 14:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.35 $** |
| P&L real total | 🔴 **-41.87 $** |
| P&L real hoy | +0.06 $ |
| P&L real 7 días | -7.85 $ |
| Fees pagados (real) | 14.63 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5923.43 $ |
| P&L sim compuesto | 🟢 +13624.92 $ (ficción Kelly: +53557% s/ operativo) |
| P&L sim hoy (2026-08-07) | 🟢 +152.37 $ |
| Operaciones resueltas | 86713 (52992 WIN / 33721 LOSS) — 61.1% |
| Señales abiertas | 389 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9793 | 62.8% | +0.128 | ➡️ estable | +4955.21$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 12473 | 60.1% | +0.101 | ➡️ estable | +4146.13$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9634 | 58.5% | +0.085 | ➡️ estable | +3268.37$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3477 | 66.5% | +0.165 | ➡️ estable | +1805.48$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 3979 | 56.0% | +0.060 | 📈 madura (+0.07) | +565.69$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 392 | 70.2% | +0.201 | 📉 agota (-0.05) | +271.80$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 634 | 76.0% | +0.259 | 📈 madura (+0.18) | +240.56$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 430 | 55.1% | +0.051 | 📉 agota (-0.13) | +100.76$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 126 | 77.0% | +0.266 | 📉 agota (-0.05) | +72.54$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 299 | 80.9% | +0.307 | ➡️ estable | +60.86$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1499 | 48.5% | -0.015 | 📈 madura (+0.04) | +44.77$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 385 | 42.3% | -0.076 | 📈 madura (+0.11) | +19.93$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1722 | 51.4% | +0.014 | ➡️ estable | +15.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 318 | 55.7% | +0.056 | 📉 agota (-0.13) | +14.27$ | 0.56$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 90 | 67.8% | +0.174 | ➡️ estable | +11.29$ | 1.74$ | ✅ activa |
| RESOLUTION_SNIPER | 27 | 77.8% | +0.259 | — | +4.05$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 595 | 80.5% | +0.304 | 📉 agota (-0.03) | +2.18$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 253 | 52.6% | +0.025 | ➡️ estable | +1.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 72 | 50.0% | +0.000 | 📈 madura (+0.11) | -0.28$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 59 | 50.8% | +0.008 | 📈 madura (+0.11) | -0.76$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 97 | 92.8% | +0.419 | ➡️ estable | -2.40$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 15 | 26.7% | -0.154 | — | -2.81$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 61 | 39.3% | -0.103 | 📈 madura (+0.11) | -7.85$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 55 | 30.9% | -0.184 | 📉 agota (-0.04) | -11.10$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 102 | 86.3% | +0.356 | 📈 madura (+0.04) | -13.68$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 279 | 77.8% | +0.276 | 📉 agota (-0.07) | -14.52$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 82 | 13.4% | -0.357 | ➡️ estable | -23.61$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1729 | 54.7% | +0.047 | 📉 agota (-0.16) | -41.06$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 290 | 33.1% | -0.168 | 📈 madura (+0.04) | -50.47$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1962 | 69.8% | +0.198 | 📉 agota (-0.06) | -154.27$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 1737 | 42.3% | -0.077 | 📉 agota (-0.18) | -273.41$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 22842 | 61.9% | +0.119 | 📉 agota (-0.06) | -579.30$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9658 | 69.5% | +0.195 | ➡️ estable | -735.35$ | 1.95$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-07T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-07T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.33$ |
| 2026-08-07T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-07T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.39$ |
| 2026-08-07T14:31 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-07T14:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,036.82 | 0.2min |  |
| ✅ ETH | $1,921.20 | 0.2min |  |
| ✅ SOL | $74.13 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,036.82 | consenso |  |
| ETH | $1,921.20 | consenso |  |
| SOL | $74.00 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*