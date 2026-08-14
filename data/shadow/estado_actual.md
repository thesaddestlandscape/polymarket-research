# Estado del bot — 2026-08-14 12:04 UTC

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
| P&L fiel (stake fijo 1$) | +5748.01 $ |
| P&L sim compuesto | 🟢 +16200.51 $ (ficción Kelly: +63681% s/ operativo) |
| P&L sim hoy (2026-08-14) | 🔴 -78.99 $ |
| Operaciones resueltas | 134133 (81871 WIN / 52262 LOSS) — 61.0% |
| Señales abiertas | 425 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 12884 | 61.1% | +0.111 | ➡️ estable | +5977.55$ | 0.59$ | ✅ activa |
| GBM_LATE_15M | 14934 | 60.1% | +0.100 | ➡️ estable | +5092.14$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 11533 | 60.2% | +0.102 | 📈 madura (+0.08) | +4697.13$ | 1.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 4216 | 63.1% | +0.131 | 📉 agota (-0.04) | +1848.59$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 1991 | 70.6% | +0.206 | 📉 agota (-0.08) | +1542.96$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4820 | 55.4% | +0.054 | 📈 madura (+0.04) | +611.43$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 800 | 77.9% | +0.278 | 📈 madura (+0.12) | +344.10$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1967 | 50.7% | +0.007 | 📈 madura (+0.07) | +110.37$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 766 | 54.6% | +0.046 | ➡️ estable | +109.93$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 202 | 75.2% | +0.250 | 📉 agota (-0.08) | +91.49$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 359 | 79.4% | +0.292 | 📉 agota (-0.03) | +53.06$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 449 | 44.5% | -0.054 | 📈 madura (+0.11) | +51.92$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 3284 | 62.3% | +0.123 | ➡️ estable | +33.26$ | 1.55$ | ✅ activa |
| ORDER_FLOW_5M | 1756 | 51.6% | +0.016 | ➡️ estable | +21.93$ | 0.61$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 331 | 55.3% | +0.053 | 📉 agota (-0.14) | +11.71$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 44 | 81.8% | +0.304 | 📉 agota (-0.08) | +7.91$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 251 | 54.6% | +0.045 | 📈 madura (+0.03) | +4.72$ | 0.50$ | ✅ activa |
| LIQUIDACIONES_60M | 226 | 53.1% | +0.031 | 📉 agota (-0.03) | +4.19$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 35 | 48.6% | -0.014 | 📉 agota (-0.08) | -0.09$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_60M | 13 | 30.8% | -0.108 | — | -2.67$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 1303 | 51.5% | +0.015 | ➡️ estable | -4.16$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 201 | 35.3% | -0.145 | 📉 agota (-0.05) | -5.67$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 397 | 44.1% | -0.059 | 📉 agota (-0.13) | -5.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 192 | 91.7% | +0.412 | ➡️ estable | -10.39$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 440 | 78.4% | +0.283 | 📉 agota (-0.03) | -13.15$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 175 | 89.7% | +0.393 | 📈 madura (+0.11) | -13.46$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 2080 | 54.5% | +0.045 | 📉 agota (-0.18) | -16.12$ | 0.50$ | ✅ activa |
| STREAK_FADE_5M | 470 | 49.1% | -0.008 | 📈 madura (+0.04) | -18.76$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 78 | 21.8% | -0.275 | 📉 agota (-0.07) | -19.02$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_5M | 139 | 36.7% | -0.131 | 📈 madura (+0.12) | -19.60$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 747 | 79.1% | +0.290 | ➡️ estable | -23.47$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_FADE | 169 | 20.1% | -0.295 | 📈 madura (+0.14) | -30.93$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 475 | 44.6% | -0.053 | 📉 agota (-0.06) | -33.51$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_15M | 256 | 38.7% | -0.112 | 📈 madura (+0.04) | -36.72$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 435 | 32.2% | -0.177 | 📉 agota (-0.04) | -74.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4008 | 69.3% | +0.193 | ➡️ estable | -269.52$ | 1.86$ | ✅ activa |
| BALLENAS_TARDIAS | 5750 | 45.7% | -0.043 | 📈 madura (+0.04) | -922.15$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 37378 | 61.2% | +0.112 | ➡️ estable | -1402.01$ | 1.41$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 18223 | 69.5% | +0.195 | ➡️ estable | -1490.94$ | 1.58$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-14T12:03 | BALLENAS_TARDIAS#XRP#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T12:03 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +13.93$ |
| 2026-08-14T12:03 | FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | … | ✅ WIN | +0.47$ |
| 2026-08-14T12:03 | BALLENAS_TARDIAS#BNB#5min | … | ❌ LOSS | -1.07$ |
| 2026-08-14T12:03 | BALLENAS_TARDIAS#SOL#5min | … | ❌ LOSS | -1.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-14T12:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,816.11 | 0.2min |  |
| ✅ ETH | $1,875.96 | 0.2min |  |
| ✅ SOL | $75.45 | 0.2min |  |
| ✅ XRP | $1.00 | 0.2min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,816.11 | consenso |  |
| ETH | $1,876.21 | consenso |  |
| SOL | $75.45 | consenso |  |
| XRP | $1.00 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*