# Estado del bot — 2026-08-14 15:46 UTC

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
| P&L fiel (stake fijo 1$) | +5640.42 $ |
| P&L sim compuesto | 🟢 +16100.03 $ (ficción Kelly: +63286% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -179.48 $ |
| Operaciones resueltas | 135431 (82577 WIN / 52854 LOSS) — 61.0% |
| Señales abiertas | 473 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12970 | 61.0% | +0.110 | ➡️ estable | +5959.41$ | 0.56$ | ✅ activa |
| GBM_LATE_15M | 15002 | 60.0% | +0.100 | ➡️ estable | +5101.72$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11607 | 60.2% | +0.102 | 📈 madura (+0.08) | +4707.63$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4249 | 62.9% | +0.129 | 📉 agota (-0.04) | +1870.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2055 | 70.0% | +0.200 | 📉 agota (-0.10) | +1541.56$ | 1.95$ | ✅ activa |
| UPDOWN_GBM | 4864 | 55.3% | +0.053 | 📈 madura (+0.04) | +606.34$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1975 | 50.6% | +0.006 | 📈 madura (+0.07) | +109.30$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 788 | 54.6% | +0.046 | ➡️ estable | +106.20$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 207 | 74.9% | +0.246 | 📉 agota (-0.07) | +94.05$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 451 | 44.6% | -0.054 | 📈 madura (+0.12) | +50.85$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3351 | 62.3% | +0.122 | ➡️ estable | +30.44$ | 1.39$ | ✅ activa |
| ORDER_FLOW_5M | 1758 | 51.6% | +0.016 | ➡️ estable | +22.17$ | 0.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 252 | 54.4% | +0.043 | ➡️ estable | +4.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_60M | 232 | 52.2% | +0.021 | 📉 agota (-0.06) | -0.84$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 1318 | 51.7% | +0.017 | ➡️ estable | -1.96$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 197 | 91.9% | +0.415 | ➡️ estable | -9.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 443 | 78.3% | +0.282 | ➡️ estable | -13.90$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 2086 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.33$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 495 | 49.3% | -0.007 | 📈 madura (+0.09) | -18.54$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 140 | 36.4% | -0.134 | 📈 madura (+0.12) | -20.11$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 750 | 79.1% | +0.290 | ➡️ estable | -25.27$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 499 | 44.7% | -0.053 | 📉 agota (-0.04) | -34.66$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 449 | 32.1% | -0.178 | 📉 agota (-0.04) | -77.97$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4052 | 69.2% | +0.192 | ➡️ estable | -279.05$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5898 | 45.5% | -0.045 | 📈 madura (+0.03) | -966.74$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37702 | 61.2% | +0.112 | ➡️ estable | -1418.24$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18423 | 69.5% | +0.195 | ➡️ estable | -1519.23$ | 1.55$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T15:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.14$ |
| 2026-08-14T15:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T15:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.31$ |
| 2026-08-14T15:46 | BALLENAS_TARDIAS#DOGE#5min | … | ✅ WIN | +0.52$ |
| 2026-08-14T15:46 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | … | ✅ WIN | +0.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T15:43 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,929.49 | 0.1min |  |
| ✅ ETH | $1,879.96 | 0.1min |  |
| ✅ SOL | $75.69 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,947.30 | consenso |  |
| ETH | $1,879.96 | consenso |  |
| SOL | $75.61 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*