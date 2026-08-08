# Estado del bot — 2026-08-08 19:07 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.90 $** |
| P&L real total | 🔴 **-40.32 $** |
| P&L real hoy | -0.96 $ |
| P&L real 7 días | -8.20 $ |
| Fees pagados (real) | 14.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5988.92 $ |
| P&L sim compuesto | 🟢 +14041.41 $ (ficción Kelly: +55194% s/ operativo) |
| P&L sim hoy (2026-08-08) | 🟢 +311.13 $ |
| Operaciones resueltas | 94092 (57615 WIN / 36477 LOSS) — 61.2% |
| Señales abiertas | 614 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10293 | 62.5% | +0.125 | ➡️ estable | +5100.89$ | 1.25$ | ✅ activa |
| GBM_LATE_15M | 12836 | 60.2% | +0.102 | ➡️ estable | +4315.84$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9872 | 58.8% | +0.088 | ➡️ estable | +3479.71$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3511 | 66.3% | +0.163 | ➡️ estable | +1805.25$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 4003 | 56.0% | +0.060 | 📈 madura (+0.07) | +564.93$ | 0.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 571 | 72.0% | +0.219 | ➡️ estable | +445.17$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 682 | 77.1% | +0.270 | 📈 madura (+0.17) | +290.58$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 435 | 54.9% | +0.049 | 📉 agota (-0.13) | +97.45$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 136 | 75.7% | +0.254 | 📉 agota (-0.04) | +71.24$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | 80.7% | +0.305 | ➡️ estable | +61.72$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1517 | 48.5% | -0.015 | ➡️ estable | +38.60$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 395 | 42.0% | -0.079 | 📈 madura (+0.11) | +15.50$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1723 | 51.4% | +0.014 | ➡️ estable | +15.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 626 | 62.9% | +0.129 | 📈 madura (+0.03) | +12.88$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 323 | 55.4% | +0.054 | 📉 agota (-0.14) | +12.10$ | 0.54$ | ✅ activa |
| RESOLUTION_SNIPER | 28 | 78.6% | +0.267 | — | +4.53$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 91 | 52.7% | +0.027 | 📈 madura (+0.16) | +4.24$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 462 | 52.2% | +0.022 | ➡️ estable | +0.52$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 91 | 52.7% | +0.027 | 📈 madura (+0.03) | -1.60$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 120 | 93.3% | +0.426 | 📈 madura (+0.06) | -1.90$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 618 | 80.3% | +0.302 | 📉 agota (-0.03) | -2.71$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 394 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.24$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 32 | 25.0% | -0.235 | ➡️ estable | -6.52$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 86 | 40.7% | -0.091 | 📈 madura (+0.11) | -10.02$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 62 | 30.6% | -0.188 | 📈 madura (+0.03) | -12.68$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 116 | 87.1% | +0.364 | 📈 madura (+0.12) | -14.37$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 305 | 77.7% | +0.275 | 📉 agota (-0.10) | -16.07$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 324 | 43.8% | -0.061 | 📉 agota (-0.10) | -27.40$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1787 | 54.5% | +0.045 | 📉 agota (-0.17) | -31.11$ | 0.50$ | ✅ activa |
| UPDOWN_OU_5M | 337 | 32.3% | -0.176 | ➡️ estable | -58.65$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2349 | 70.1% | +0.201 | 📉 agota (-0.06) | -161.34$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2216 | 42.7% | -0.073 | 📉 agota (-0.08) | -446.33$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 25315 | 61.9% | +0.119 | 📉 agota (-0.05) | -593.73$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11172 | 69.6% | +0.196 | ➡️ estable | -846.04$ | 1.96$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-08T19:06 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.39$ |
| 2026-08-08T19:06 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.60$ |
| 2026-08-08T19:06 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-08T19:06 | FAVORITO_CONFIRMADO#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-08T19:06 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-08T19:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,995.46 | 0.1min |  |
| ✅ ETH | $1,919.82 | 0.1min |  |
| ✅ SOL | $76.11 | 0.1min |  |
| ✅ XRP | $1.04 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,995.46 | consenso |  |
| ETH | $1,919.82 | consenso |  |
| SOL | $76.07 | consenso |  |
| XRP | $1.04 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*