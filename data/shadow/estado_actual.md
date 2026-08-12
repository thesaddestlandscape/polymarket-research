# Estado del bot — 2026-08-12 10:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **8.81 $** |
| P&L real total | 🔴 **-42.41 $** |
| P&L real hoy | -2.36 $ |
| P&L real 7 días | -7.66 $ |
| Fees pagados (real) | 15.39 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5977.25 $ |
| P&L sim compuesto | 🟢 +15407.14 $ (ficción Kelly: +60563% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +151.49 $ |
| Operaciones resueltas | 117645 (72150 WIN / 45495 LOSS) — 61.3% |
| Señales abiertas | 473 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11755 | 61.5% | +0.115 | ➡️ estable | +5705.25$ | 0.57$ | ✅ activa |
| GBM_LATE_15M | 13988 | 60.2% | +0.102 | ➡️ estable | +4808.00$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10649 | 59.7% | +0.097 | 📈 madura (+0.06) | +4177.02$ | 1.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3766 | 65.0% | +0.150 | ➡️ estable | +1818.22$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1222 | 73.1% | +0.230 | ➡️ estable | +1073.38$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4315 | 55.5% | +0.055 | 📈 madura (+0.05) | +554.45$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 506 | 54.7% | +0.047 | 📉 agota (-0.11) | +106.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 175 | 75.4% | +0.251 | 📉 agota (-0.05) | +79.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1756 | 49.9% | -0.001 | 📈 madura (+0.07) | +60.93$ | 0.77$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 340 | 80.0% | +0.298 | ➡️ estable | +58.13$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2318 | 62.6% | +0.125 | ➡️ estable | +23.48$ | 1.25$ | ✅ activa |
| ORDER_FLOW_5M | 1733 | 51.5% | +0.015 | ➡️ estable | +18.16$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 215 | 53.0% | +0.030 | ➡️ estable | +1.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 158 | 93.7% | +0.431 | ➡️ estable | -1.55$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1965 | 54.9% | +0.049 | 📉 agota (-0.17) | -2.63$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1023 | 51.4% | +0.014 | ➡️ estable | -4.33$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 188 | 51.1% | +0.011 | 📉 agota (-0.04) | -6.39$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 154 | 89.0% | +0.385 | 📈 madura (+0.11) | -13.79$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 393 | 77.9% | +0.277 | 📉 agota (-0.06) | -19.24$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 689 | 79.0% | +0.289 | ➡️ estable | -24.09$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 193 | 38.3% | -0.115 | 📉 agota (-0.04) | -28.26$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 345 | 44.9% | -0.050 | 📉 agota (-0.04) | -31.73$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 370 | 31.6% | -0.183 | 📉 agota (-0.06) | -66.10$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3398 | 70.3% | +0.203 | ➡️ estable | -188.33$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4127 | 46.5% | -0.035 | 📈 madura (+0.10) | -704.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 32990 | 61.5% | +0.115 | ➡️ estable | -1048.09$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15642 | 69.8% | +0.198 | ➡️ estable | -1219.14$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T10:16 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T10:16 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 12, 6:00AM-6:05AM ET… | ✅ WIN | +1.20$ |
| 2026-08-12T10:16 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T10:16 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | … | ✅ WIN | +0.52$ |
| 2026-08-12T10:16 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T10:14 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,074.11 | 0.1min |  |
| ✅ ETH | $1,910.71 | 0.1min |  |
| ✅ SOL | $76.75 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,074.11 | consenso |  |
| ETH | $1,910.91 | consenso |  |
| SOL | $76.75 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*