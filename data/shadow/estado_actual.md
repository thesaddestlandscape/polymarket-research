# Estado del bot — 2026-08-14 17:12 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **16.11 $** |
| P&L real total | 🔴 **-45.11 $** |
| P&L real hoy | +1.22 $ |
| P&L real 7 días | -3.19 $ |
| Fees pagados (real) | 15.64 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5666.00 $ |
| P&L sim compuesto | 🟢 +16156.82 $ (ficción Kelly: +63510% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -122.68 $ |
| Operaciones resueltas | 135994 (82929 WIN / 53065 LOSS) — 61.0% |
| Señales abiertas | 448 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 13000 | 61.0% | +0.110 | ➡️ estable | +5961.82$ | 0.56$ | ✅ activa |
| GBM_LATE_15M | 15032 | 60.1% | +0.101 | ➡️ estable | +5122.06$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11634 | 60.2% | +0.102 | 📈 madura (+0.08) | +4716.56$ | 1.76$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4268 | 62.9% | +0.129 | 📉 agota (-0.04) | +1881.29$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2082 | 69.8% | +0.198 | 📉 agota (-0.10) | +1548.72$ | 1.93$ | ✅ activa |
| UPDOWN_GBM | 4879 | 55.3% | +0.053 | 📈 madura (+0.04) | +610.62$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 824 | 77.9% | +0.278 | 📈 madura (+0.12) | +352.20$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1976 | 50.6% | +0.006 | 📈 madura (+0.07) | +108.79$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 792 | 54.5% | +0.045 | ➡️ estable | +106.17$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 208 | 75.0% | +0.248 | 📉 agota (-0.08) | +96.40$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 452 | 44.7% | -0.053 | 📈 madura (+0.12) | +50.96$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3378 | 62.3% | +0.123 | ➡️ estable | +33.18$ | 1.44$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 254 | 54.7% | +0.047 | 📈 madura (+0.04) | +5.19$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 233 | 52.4% | +0.023 | 📉 agota (-0.06) | -0.25$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1332 | 51.6% | +0.016 | ➡️ estable | -3.16$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 204 | 36.3% | -0.136 | 📉 agota (-0.04) | -4.98$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 446 | 78.5% | +0.283 | ➡️ estable | -12.57$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 179 | 89.9% | +0.395 | 📈 madura (+0.11) | -12.90$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2087 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.93$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 85 | 22.4% | -0.270 | ➡️ estable | -19.72$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 504 | 49.0% | -0.010 | 📈 madura (+0.08) | -20.14$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 149 | 36.2% | -0.136 | 📈 madura (+0.05) | -21.71$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 508 | 45.1% | -0.049 | 📉 agota (-0.04) | -33.13$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 456 | 32.5% | -0.175 | ➡️ estable | -77.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4071 | 69.2% | +0.192 | ➡️ estable | -282.27$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5956 | 45.5% | -0.045 | 📈 madura (+0.03) | -971.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37837 | 61.2% | +0.112 | ➡️ estable | -1418.04$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18500 | 69.5% | +0.195 | ➡️ estable | -1520.89$ | 1.61$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T17:11 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | … | ✅ WIN | +0.23$ |
| 2026-08-14T17:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.35$ |
| 2026-08-14T17:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T17:11 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.41$ |
| 2026-08-14T17:11 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T17:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,086.62 | 0.2min |  |
| ✅ ETH | $1,883.33 | 0.2min |  |
| ✅ SOL | $75.48 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,086.62 | consenso |  |
| ETH | $1,883.33 | consenso |  |
| SOL | $75.44 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*