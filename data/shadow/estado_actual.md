# Estado del bot — 2026-08-11 16:21 UTC

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
| P&L fiel (stake fijo 1$) | +6146.81 $ |
| P&L sim compuesto | 🟢 +15288.40 $ (ficción Kelly: +60096% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +120.28 $ |
| Operaciones resueltas | 112201 (68928 WIN / 43273 LOSS) — 61.4% |
| Señales abiertas | 606 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11429 | 61.7% | +0.117 | ➡️ estable | +5605.71$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 13723 | 60.3% | +0.103 | ➡️ estable | +4700.02$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10472 | 59.5% | +0.095 | 📈 madura (+0.05) | +3994.62$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3611 | 65.8% | +0.158 | ➡️ estable | +1812.16$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1092 | 74.3% | +0.242 | 📈 madura (+0.06) | +990.95$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4117 | 55.8% | +0.058 | 📈 madura (+0.06) | +559.54$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 753 | 78.0% | +0.279 | 📈 madura (+0.15) | +334.54$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 462 | 54.8% | +0.047 | 📉 agota (-0.14) | +100.08$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1690 | 49.8% | -0.002 | 📈 madura (+0.07) | +62.88$ | 0.95$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1967 | 63.3% | +0.133 | ➡️ estable | +44.51$ | 1.33$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1731 | 51.4% | +0.014 | ➡️ estable | +15.29$ | 0.53$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 895 | 52.4% | +0.024 | ➡️ estable | +7.00$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1921 | 55.1% | +0.051 | 📉 agota (-0.15) | +3.47$ | 0.73$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 198 | 53.0% | +0.030 | ➡️ estable | +0.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 165 | 50.9% | +0.009 | ➡️ estable | -3.18$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 59 | 20.3% | -0.287 | 📉 agota (-0.13) | -15.58$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 668 | 79.5% | +0.294 | ➡️ estable | -15.59$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 109 | 34.9% | -0.149 | 📈 madura (+0.06) | -18.06$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 371 | 77.6% | +0.275 | 📉 agota (-0.08) | -20.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_5M | 282 | 46.8% | -0.032 | 📈 madura (+0.07) | -22.51$ | 0.95$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 162 | 38.9% | -0.110 | ➡️ estable | -23.20$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 356 | 43.0% | -0.070 | 📉 agota (-0.12) | -32.64$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3174 | 70.2% | +0.202 | ➡️ estable | -187.70$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3702 | 45.5% | -0.045 | 📈 madura (+0.08) | -701.21$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31408 | 61.7% | +0.117 | ➡️ estable | -863.27$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14637 | 69.8% | +0.198 | ➡️ estable | -1111.10$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T16:20 | FAVORITO_CONFIRMADO#SOL#15min | … | ✅ WIN | +0.60$ |
| 2026-08-11T16:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.41$ |
| 2026-08-11T16:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.39$ |
| 2026-08-11T16:20 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.37$ |
| 2026-08-11T16:20 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.35$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T16:16 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,554.61 | 0.2min |  |
| ✅ ETH | $1,862.74 | 0.2min |  |
| ✅ SOL | $74.92 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,561.80 | consenso |  |
| ETH | $1,862.74 | consenso |  |
| SOL | $74.92 | consenso |  |
| XRP | $1.00 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*