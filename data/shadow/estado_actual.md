# Estado del bot — 2026-08-11 14:55 UTC

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
| P&L fiel (stake fijo 1$) | +6153.49 $ |
| P&L sim compuesto | 🟢 +15257.75 $ (ficción Kelly: +59975% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🟢 +89.63 $ |
| Operaciones resueltas | 111772 (68670 WIN / 43102 LOSS) — 61.4% |
| Señales abiertas | 615 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11413 | 61.8% | +0.118 | ➡️ estable | +5600.37$ | 0.60$ | ✅ activa |
| GBM_LATE_15M | 13708 | 60.3% | +0.103 | ➡️ estable | +4690.49$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10460 | 59.5% | +0.095 | 📈 madura (+0.05) | +3981.96$ | 1.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3609 | 65.8% | +0.158 | ➡️ estable | +1813.49$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1076 | 74.3% | +0.242 | 📈 madura (+0.05) | +977.66$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4107 | 55.9% | +0.059 | 📈 madura (+0.06) | +560.45$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 460 | 54.8% | +0.048 | 📉 agota (-0.14) | +100.06$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 162 | 76.5% | +0.262 | 📉 agota (-0.05) | +82.81$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 329 | 80.5% | +0.304 | ➡️ estable | +63.37$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1685 | 49.7% | -0.003 | 📈 madura (+0.07) | +59.92$ | 0.91$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1935 | 63.5% | +0.134 | ➡️ estable | +45.76$ | 1.35$ | ✅ activa |
| GBM_LATE_60M | 422 | 42.7% | -0.073 | 📈 madura (+0.10) | +31.37$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1729 | 51.5% | +0.015 | ➡️ estable | +18.29$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 892 | 52.5% | +0.025 | ➡️ estable | +7.55$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1920 | 55.2% | +0.052 | 📉 agota (-0.15) | +3.98$ | 0.76$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 195 | 53.3% | +0.033 | ➡️ estable | +1.04$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 160 | 52.5% | +0.025 | ➡️ estable | -0.49$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 149 | 94.0% | +0.434 | 📈 madura (+0.04) | -0.58$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 8 | 25.0% | -0.080 | — | -2.11$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 142 | 88.0% | +0.375 | 📈 madura (+0.12) | -15.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 369 | 78.0% | +0.279 | 📉 agota (-0.07) | -16.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 667 | 79.5% | +0.294 | ➡️ estable | -16.51$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 104 | 32.7% | -0.170 | 📈 madura (+0.04) | -19.39$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 161 | 39.1% | -0.107 | ➡️ estable | -22.69$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 278 | 46.4% | -0.036 | 📈 madura (+0.05) | -23.40$ | 0.76$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 140 | 18.6% | -0.310 | 📈 madura (+0.08) | -28.09$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 352 | 43.2% | -0.068 | 📉 agota (-0.12) | -31.65$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 353 | 31.7% | -0.182 | 📉 agota (-0.04) | -62.59$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3160 | 70.1% | +0.201 | ➡️ estable | -191.74$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3659 | 45.4% | -0.046 | 📈 madura (+0.08) | -707.33$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 31281 | 61.7% | +0.117 | ➡️ estable | -857.52$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14564 | 69.8% | +0.198 | ➡️ estable | -1102.34$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T14:54 | BALLENAS_TARDIAS#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:54 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:54 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-11T14:54 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.60$ |
| 2026-08-11T14:54 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.71$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T14:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,946.17 | 0.1min |  |
| ✅ ETH | $1,876.91 | 0.1min |  |
| ✅ SOL | $75.21 | 0.1min |  |
| ✅ XRP | $1.00 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,947.80 | consenso |  |
| ETH | $1,876.91 | consenso |  |
| SOL | $75.44 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*