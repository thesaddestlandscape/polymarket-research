# Estado del bot — 2026-08-14 14:47 UTC

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
| P&L fiel (stake fijo 1$) | +5580.24 $ |
| P&L sim compuesto | 🟢 +15990.35 $ (ficción Kelly: +62855% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -289.15 $ |
| Operaciones resueltas | 135082 (82331 WIN / 52751 LOSS) — 60.9% |
| Señales abiertas | 459 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12947 | 61.0% | +0.110 | ➡️ estable | +5946.11$ | 0.55$ | ✅ activa |
| GBM_LATE_15M | 14984 | 60.0% | +0.100 | ➡️ estable | +5083.41$ | 0.93$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11587 | 60.1% | +0.101 | 📈 madura (+0.07) | +4677.37$ | 1.75$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4239 | 62.9% | +0.129 | 📉 agota (-0.04) | +1871.54$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2035 | 69.9% | +0.199 | 📉 agota (-0.10) | +1520.12$ | 1.94$ | ✅ activa |
| UPDOWN_GBM | 4854 | 55.2% | +0.052 | 📈 madura (+0.04) | +597.16$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1973 | 50.6% | +0.006 | 📈 madura (+0.07) | +109.31$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 785 | 54.5% | +0.045 | ➡️ estable | +105.95$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 204 | 74.5% | +0.243 | 📉 agota (-0.08) | +87.41$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 450 | 44.7% | -0.053 | 📈 madura (+0.12) | +52.38$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 361 | 78.9% | +0.288 | 📉 agota (-0.03) | +48.98$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3336 | 62.2% | +0.122 | ➡️ estable | +28.74$ | 1.37$ | ✅ activa |
| ORDER_FLOW_5M | 1757 | 51.6% | +0.016 | ➡️ estable | +20.59$ | 0.57$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 231 | 52.4% | +0.024 | 📉 agota (-0.05) | +0.22$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1313 | 51.7% | +0.017 | ➡️ estable | -1.39$ | 0.50$ | ✅ activa |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 195 | 91.8% | +0.414 | ➡️ estable | -10.06$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | 78.5% | +0.284 | ➡️ estable | -11.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2086 | 54.5% | +0.045 | 📉 agota (-0.18) | -15.33$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 140 | 36.4% | -0.134 | 📈 madura (+0.12) | -20.11$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 487 | 48.9% | -0.011 | 📈 madura (+0.06) | -20.41$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 749 | 79.0% | +0.290 | ➡️ estable | -25.41$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 491 | 45.0% | -0.050 | 📉 agota (-0.04) | -32.60$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 440 | 32.0% | -0.179 | 📉 agota (-0.03) | -76.36$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4038 | 69.1% | +0.191 | ➡️ estable | -281.45$ | 1.83$ | ✅ activa |
| BALLENAS_TARDIAS | 5862 | 45.5% | -0.045 | 📈 madura (+0.03) | -955.59$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37618 | 61.2% | +0.112 | ➡️ estable | -1438.13$ | 1.37$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18370 | 69.4% | +0.194 | ➡️ estable | -1523.03$ | 1.45$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T14:47 | BALLENAS_TARDIAS#BNB#5min | … | ✅ WIN | +0.65$ |
| 2026-08-14T14:47 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T14:47 | FAVORITO_CONFIRMADO#BNB#5min | … | ✅ WIN | +0.43$ |
| 2026-08-14T14:47 | FAVORITO_CONFIRMADO#SOL#15min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T14:47 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | … | ✅ WIN | +0.28$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T14:44 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,679.35 | 0.2min |  |
| ✅ ETH | $1,868.66 | 0.2min |  |
| ✅ SOL | $75.26 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,679.35 | consenso |  |
| ETH | $1,869.01 | consenso |  |
| SOL | $75.26 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*