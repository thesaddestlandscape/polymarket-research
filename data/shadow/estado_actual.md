# Estado del bot — 2026-08-11 10:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.07 $** |
| P&L real total | 🔴 **-41.15 $** |
| P&L real hoy | -0.23 $ |
| P&L real 7 días | -11.98 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6204.55 $ |
| P&L sim compuesto | 🟢 +15276.57 $ (ficción Kelly: +60049% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +108.45 $ |
| Operaciones resueltas | 110395 (67842 WIN / 42553 LOSS) — 61.5% |
| Señales abiertas | 560 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11330 | 61.8% | +0.118 | ➡️ estable | +5586.13$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 13644 | 60.3% | +0.103 | ➡️ estable | +4692.04$ | 1.16$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10422 | 59.5% | +0.095 | 📈 madura (+0.05) | +3973.68$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3602 | 65.9% | +0.158 | ➡️ estable | +1816.75$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1042 | 74.8% | +0.247 | 📈 madura (+0.06) | +968.51$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4077 | 55.9% | +0.059 | 📈 madura (+0.06) | +562.22$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 452 | 54.6% | +0.046 | 📉 agota (-0.13) | +98.56$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1657 | 49.4% | -0.006 | 📈 madura (+0.05) | +48.32$ | 0.71$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1842 | 63.2% | +0.132 | ➡️ estable | +34.04$ | 1.32$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 855 | 52.5% | +0.025 | ➡️ estable | +7.62$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 186 | 54.3% | +0.043 | ➡️ estable | +4.23$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 158 | 51.9% | +0.019 | ➡️ estable | -1.64$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1908 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.78$ | 0.71$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 140 | 87.9% | +0.373 | 📈 madura (+0.10) | -15.48$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 363 | 78.0% | +0.278 | 📉 agota (-0.06) | -16.38$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 662 | 79.5% | +0.294 | 📉 agota (-0.03) | -17.44$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 88 | 30.7% | -0.189 | ➡️ estable | -18.20$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 146 | 38.4% | -0.115 | ➡️ estable | -22.05$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 263 | 45.6% | -0.043 | ➡️ estable | -24.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 337 | 43.3% | -0.066 | 📉 agota (-0.12) | -29.99$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3103 | 70.1% | +0.201 | ➡️ estable | -190.19$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3499 | 45.4% | -0.046 | 📈 madura (+0.07) | -663.56$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30885 | 61.7% | +0.117 | ➡️ estable | -858.77$ | 1.14$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14328 | 69.9% | +0.199 | ➡️ estable | -1075.17$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T10:11 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T10:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T10:11 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.14$ |
| 2026-08-11T10:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T10:11 | LIQUIDACIONES_15M#ETH#15min | Ethereum Up or Down - August 11, 5:45AM-6:00AM ET… | ❌ LOSS | -0.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T10:07 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,236.89 | 0.3min |  |
| ✅ ETH | $1,885.44 | 0.3min |  |
| ✅ SOL | $75.87 | 0.3min |  |
| ✅ XRP | $1.01 | 0.3min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,237.50 | consenso |  |
| ETH | $1,885.75 | consenso |  |
| SOL | $75.87 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*