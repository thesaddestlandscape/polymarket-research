# Estado del bot — 2026-08-11 08:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.16 $** |
| P&L real total | 🔴 **-40.06 $** |
| P&L real hoy | +0.86 $ |
| P&L real 7 días | -10.89 $ |
| Fees pagados (real) | 15.23 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6233.50 $ |
| P&L sim compuesto | 🟢 +15286.62 $ (ficción Kelly: +60089% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +118.50 $ |
| Operaciones resueltas | 110040 (67635 WIN / 42405 LOSS) — 61.5% |
| Señales abiertas | 556 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11308 | 61.9% | +0.118 | ➡️ estable | +5589.85$ | 0.62$ | ✅ activa |
| GBM_LATE_15M | 13629 | 60.3% | +0.103 | ➡️ estable | +4686.32$ | 1.16$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10413 | 59.5% | +0.095 | 📈 madura (+0.05) | +3963.81$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3600 | 65.9% | +0.159 | ➡️ estable | +1818.89$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1033 | 74.9% | +0.249 | 📈 madura (+0.07) | +961.75$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4075 | 55.9% | +0.058 | 📈 madura (+0.06) | +561.24$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 450 | 54.7% | +0.046 | 📉 agota (-0.13) | +98.59$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 161 | 76.4% | +0.261 | 📉 agota (-0.05) | +82.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 328 | 80.5% | +0.303 | ➡️ estable | +62.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1649 | 49.2% | -0.008 | 📈 madura (+0.05) | +41.30$ | 0.58$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1821 | 63.4% | +0.134 | ➡️ estable | +38.23$ | 1.34$ | ✅ activa |
| GBM_LATE_60M | 421 | 42.5% | -0.074 | 📈 madura (+0.10) | +28.86$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 840 | 53.0% | +0.030 | ➡️ estable | +11.67$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 185 | 54.1% | +0.040 | ➡️ estable | +3.46$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 147 | 93.9% | +0.433 | 📈 madura (+0.04) | -0.83$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1907 | 55.1% | +0.051 | 📉 agota (-0.15) | -1.27$ | 0.73$ | ✅ activa |
| STREAK_FADE_60M | 7 | 28.6% | -0.058 | — | -1.60$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 157 | 51.6% | +0.016 | ➡️ estable | -1.94$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 139 | 87.8% | +0.372 | 📈 madura (+0.10) | -15.63$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 362 | 77.9% | +0.277 | 📉 agota (-0.07) | -16.95$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 87 | 31.0% | -0.185 | ➡️ estable | -17.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 661 | 79.4% | +0.293 | 📉 agota (-0.04) | -18.27$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 143 | 39.2% | -0.107 | ➡️ estable | -19.51$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 255 | 45.5% | -0.045 | 📉 agota (-0.05) | -24.55$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 138 | 18.8% | -0.307 | 📈 madura (+0.08) | -27.07$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 329 | 43.2% | -0.068 | 📉 agota (-0.12) | -29.95$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3088 | 70.0% | +0.200 | ➡️ estable | -192.37$ | 1.98$ | ✅ activa |
| BALLENAS_TARDIAS | 3474 | 45.4% | -0.046 | 📈 madura (+0.06) | -656.68$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30775 | 61.7% | +0.117 | ➡️ estable | -844.83$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14259 | 69.9% | +0.199 | ➡️ estable | -1066.81$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T08:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.33$ |
| 2026-08-11T08:56 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.26$ |
| 2026-08-11T08:56 | FAVORITO_CONFIRMADO#BTC#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T08:56 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.84$ |
| 2026-08-11T08:56 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T08:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,042.24 | 0.2min |  |
| ✅ ETH | $1,875.72 | 0.2min |  |
| ✅ SOL | $75.86 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,045.40 | consenso |  |
| ETH | $1,875.72 | consenso |  |
| SOL | $75.86 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*