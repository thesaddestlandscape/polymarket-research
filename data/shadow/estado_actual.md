# Estado del bot — 2026-08-12 10:46 UTC

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
| P&L fiel (stake fijo 1$) | +5967.04 $ |
| P&L sim compuesto | 🟢 +15411.28 $ (ficción Kelly: +60579% s/ operativo) |
| P&L sim hoy (2026-08-12) | 🟢 +155.63 $ |
| Operaciones resueltas | 117783 (72229 WIN / 45554 LOSS) — 61.3% |
| Señales abiertas | 482 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11765 | 61.5% | +0.115 | ➡️ estable | +5700.76$ | 0.56$ | ✅ activa |
| GBM_LATE_15M | 13997 | 60.2% | +0.102 | ➡️ estable | +4814.17$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10658 | 59.7% | +0.097 | 📈 madura (+0.06) | +4189.26$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3766 | 65.0% | +0.150 | ➡️ estable | +1818.22$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1231 | 72.9% | +0.229 | ➡️ estable | +1074.75$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4315 | 55.5% | +0.055 | 📈 madura (+0.05) | +554.45$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 756 | 77.9% | +0.278 | 📈 madura (+0.14) | +334.57$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 508 | 54.7% | +0.047 | 📉 agota (-0.11) | +106.35$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 175 | 75.4% | +0.251 | 📉 agota (-0.05) | +79.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1760 | 49.9% | -0.001 | 📈 madura (+0.07) | +60.84$ | 0.75$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 340 | 80.0% | +0.298 | ➡️ estable | +58.13$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 432 | 43.5% | -0.065 | 📈 madura (+0.11) | +39.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2328 | 62.6% | +0.126 | ➡️ estable | +25.42$ | 1.26$ | ✅ activa |
| ORDER_FLOW_5M | 1733 | 51.5% | +0.015 | ➡️ estable | +18.16$ | 0.58$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.00$ | 🚫 desactivada |
| RESOLUTION_SNIPER | 34 | 76.5% | +0.250 | 📉 agota (-0.21) | +5.63$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 215 | 53.0% | +0.030 | ➡️ estable | +1.36$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 34 | 50.0% | +0.000 | 📉 agota (-0.05) | +0.47$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 159 | 93.7% | +0.432 | ➡️ estable | -1.38$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 10 | 30.0% | -0.083 | — | -2.19$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 1965 | 54.9% | +0.049 | 📉 agota (-0.17) | -2.63$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1026 | 51.4% | +0.014 | ➡️ estable | -4.87$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 188 | 51.1% | +0.011 | 📉 agota (-0.04) | -6.39$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 196 | 33.7% | -0.162 | 📉 agota (-0.08) | -6.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 154 | 89.0% | +0.385 | 📈 madura (+0.11) | -13.79$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM_FADE | 61 | 21.3% | -0.278 | 📉 agota (-0.10) | -15.54$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 393 | 77.9% | +0.277 | 📉 agota (-0.06) | -19.24$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 123 | 35.0% | -0.148 | 📈 madura (+0.07) | -20.27$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 690 | 79.0% | +0.289 | ➡️ estable | -23.21$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 151 | 20.5% | -0.291 | 📈 madura (+0.11) | -26.55$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_15M | 196 | 38.3% | -0.116 | 📉 agota (-0.07) | -28.79$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 345 | 44.9% | -0.050 | 📉 agota (-0.04) | -31.73$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 396 | 44.2% | -0.058 | 📉 agota (-0.09) | -32.03$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 370 | 31.6% | -0.183 | 📉 agota (-0.06) | -66.10$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3404 | 70.3% | +0.203 | ➡️ estable | -188.83$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 4143 | 46.4% | -0.036 | 📈 madura (+0.10) | -711.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 33026 | 61.5% | +0.115 | ➡️ estable | -1051.61$ | 1.10$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15661 | 69.8% | +0.198 | ➡️ estable | -1221.08$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-12T10:45 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - August 12, 6:25AM-6:30AM ET… | ❌ LOSS | -1.83$ |
| 2026-08-12T10:45 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T10:45 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-12T10:45 | FAVORITO_CONFIRMADO#SOL#5min | … | ✅ WIN | +0.68$ |
| 2026-08-12T10:45 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-12T10:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,046.81 | 0.1min |  |
| ✅ ETH | $1,909.51 | 0.1min |  |
| ✅ SOL | $76.81 | 0.1min |  |
| ✅ XRP | $1.02 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,046.81 | consenso |  |
| ETH | $1,909.51 | consenso |  |
| SOL | $76.72 | consenso |  |
| XRP | $1.02 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*