# Estado del bot — 2026-08-14 13:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 61.22 $ |
| Balance on-chain | **15.57 $** |
| P&L real total | 🔴 **-45.65 $** |
| P&L real hoy | +0.67 $ |
| P&L real 7 días | -3.74 $ |
| Fees pagados (real) | 15.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5678.57 $ |
| P&L sim compuesto | 🟢 +16104.55 $ (ficción Kelly: +63304% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -174.95 $ |
| Operaciones resueltas | 134474 (82032 WIN / 52442 LOSS) — 61.0% |
| Señales abiertas | 423 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12908 | 61.0% | +0.110 | ➡️ estable | +5960.81$ | 0.58$ | ✅ activa |
| GBM_LATE_15M | 14951 | 60.0% | +0.100 | ➡️ estable | +5083.86$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11556 | 60.1% | +0.101 | 📈 madura (+0.08) | +4674.62$ | 1.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4228 | 62.9% | +0.129 | 📉 agota (-0.04) | +1866.39$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 2007 | 70.2% | +0.202 | 📉 agota (-0.09) | +1521.69$ | 1.97$ | ✅ activa |
| UPDOWN_GBM | 4832 | 55.3% | +0.053 | 📈 madura (+0.04) | +608.70$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1970 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.84$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 772 | 54.4% | +0.044 | ➡️ estable | +107.86$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 203 | 74.9% | +0.246 | 📉 agota (-0.08) | +89.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 450 | 44.7% | -0.053 | 📈 madura (+0.12) | +52.38$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 360 | 79.2% | +0.290 | ➡️ estable | +51.02$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3300 | 62.4% | +0.124 | ➡️ estable | +36.49$ | 1.61$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 227 | 53.3% | +0.033 | 📉 agota (-0.03) | +4.64$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1310 | 51.6% | +0.016 | ➡️ estable | -2.83$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 195 | 91.8% | +0.414 | ➡️ estable | -10.06$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | 78.5% | +0.284 | ➡️ estable | -11.86$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | 89.8% | +0.393 | 📈 madura (+0.11) | -13.33$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2082 | 54.5% | +0.045 | 📉 agota (-0.18) | -16.66$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 478 | 49.2% | -0.008 | 📈 madura (+0.05) | -18.83$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 139 | 36.7% | -0.131 | 📈 madura (+0.12) | -19.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 748 | 79.1% | +0.291 | ➡️ estable | -23.37$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 170 | 20.0% | -0.297 | 📈 madura (+0.11) | -31.44$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 482 | 44.6% | -0.054 | 📉 agota (-0.06) | -34.05$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 435 | 32.2% | -0.177 | 📉 agota (-0.04) | -74.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4021 | 69.2% | +0.192 | ➡️ estable | -279.14$ | 1.84$ | ✅ activa |
| BALLENAS_TARDIAS | 5783 | 45.6% | -0.044 | 📈 madura (+0.04) | -937.09$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37464 | 61.2% | +0.112 | ➡️ estable | -1416.16$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18267 | 69.5% | +0.195 | ➡️ estable | -1494.43$ | 1.59$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T13:01 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 14, 8:45AM-8:50AM ET… | ✅ WIN | +0.50$ |
| 2026-08-14T13:01 | FAVORITO_CONFIRMADO#BTC#5min | … | ✅ WIN | +0.77$ |
| 2026-08-14T13:01 | UPDOWN_GBM#BTC#5min | Bitcoin Up or Down - August 14, 8:45AM-8:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-08-14T13:01 | BALLENAS_TARDIAS#ETH#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T13:01 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T12:58 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,687.54 | 0.2min |  |
| ✅ ETH | $1,872.20 | 0.2min |  |
| ✅ SOL | $75.38 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,700.10 | consenso |  |
| ETH | $1,872.20 | consenso |  |
| SOL | $75.38 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*