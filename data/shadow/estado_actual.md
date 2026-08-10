# Estado del bot — 2026-08-10 05:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **9.10 $** |
| P&L real total | 🔴 **-42.12 $** |
| P&L real hoy | -0.96 $ |
| P&L real 7 días | -10.41 $ |
| Fees pagados (real) | 15.03 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6186.18 $ |
| P&L sim compuesto | 🟢 +14692.27 $ (ficción Kelly: +57753% s/ operativo) |
| P&L sim hoy (2026-08-10) | 🟢 +316.80 $ |
| Operaciones resueltas | 102849 (63161 WIN / 39688 LOSS) — 61.4% |
| Señales abiertas | 485 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 10907 | 62.2% | +0.122 | ➡️ estable | +5350.15$ | 1.22$ | ✅ activa |
| GBM_LATE_15M | 13310 | 60.3% | +0.103 | ➡️ estable | +4524.08$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10177 | 59.3% | +0.092 | 📈 madura (+0.04) | +3777.54$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3549 | 66.2% | +0.162 | ➡️ estable | +1810.87$ | 1.62$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 829 | 73.9% | +0.239 | 📈 madura (+0.05) | +737.20$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4026 | 55.9% | +0.059 | 📈 madura (+0.07) | +558.44$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 710 | 77.6% | +0.275 | 📈 madura (+0.17) | +311.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 438 | 55.3% | +0.052 | 📉 agota (-0.13) | +98.28$ | 0.52$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 147 | 76.2% | +0.258 | 📉 agota (-0.06) | +75.38$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 315 | 80.6% | +0.304 | ➡️ estable | +61.70$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1584 | 48.7% | -0.013 | 📈 madura (+0.03) | +35.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1270 | 63.8% | +0.138 | ➡️ estable | +33.03$ | 1.38$ | ✅ activa |
| GBM_LATE_60M | 404 | 42.6% | -0.074 | 📈 madura (+0.12) | +19.06$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 693 | 53.2% | +0.032 | ➡️ estable | +13.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 29 | 79.3% | +0.274 | — | +6.30$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_60M | 127 | 53.5% | +0.035 | 📈 madura (+0.05) | +1.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 32 | 50.0% | +0.000 | 📉 agota (-0.11) | +0.39$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 137 | 94.2% | +0.435 | 📈 madura (+0.06) | +0.22$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 134 | 51.5% | +0.015 | 📈 madura (+0.04) | -0.03$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 5 | 20.0% | -0.054 | — | -1.57$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 44 | 22.7% | -0.261 | 📉 agota (-0.08) | -10.29$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1848 | 54.9% | +0.049 | 📉 agota (-0.16) | -11.41$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 641 | 79.7% | +0.296 | 📉 agota (-0.04) | -12.93$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 75 | 33.3% | -0.162 | ➡️ estable | -13.50$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 110 | 40.0% | -0.098 | 📈 madura (+0.04) | -13.76$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 129 | 86.8% | +0.363 | 📈 madura (+0.11) | -17.07$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 334 | 76.9% | +0.268 | 📉 agota (-0.09) | -23.95$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 125 | 18.4% | -0.311 | 📈 madura (+0.07) | -25.36$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 344 | 32.3% | -0.176 | ➡️ estable | -59.69$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2752 | 70.1% | +0.200 | 📉 agota (-0.04) | -179.04$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 2851 | 43.1% | -0.069 | ➡️ estable | -639.48$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 28325 | 61.9% | +0.119 | 📉 agota (-0.03) | -712.38$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12873 | 69.9% | +0.199 | ➡️ estable | -960.21$ | 1.99$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-10T05:11 | UPDOWN_GBM_15M_TARDIO#BTC#15min | … | ✅ WIN | +2.11$ |
| 2026-08-10T05:11 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.84$ |
| 2026-08-10T05:11 | FAVORITO_CONFIRMADO#ETH#5min | … | ✅ WIN | +0.68$ |
| 2026-08-10T05:11 | FAVORITO_CONFIRMADO#SOL#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-10T05:11 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.35$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-10T05:09 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,972.54 | 0.2min |  |
| ✅ ETH | $1,916.22 | 0.2min |  |
| ✅ SOL | $76.70 | 0.2min |  |
| ✅ XRP | $1.03 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,979.90 | consenso |  |
| ETH | $1,916.29 | consenso |  |
| SOL | $76.60 | consenso |  |
| XRP | $1.03 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*