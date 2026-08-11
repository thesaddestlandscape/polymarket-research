# Estado del bot — 2026-08-11 00:42 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **10.30 $** |
| P&L real total | 🔴 **-40.92 $** |
| P&L real hoy | -32.86 $ |
| P&L real 7 días | -11.75 $ |
| Fees pagados (real) | 15.20 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +6249.51 $ |
| P&L sim compuesto | 🟢 +15162.69 $ (ficción Kelly: +59602% s/ operativo) |
| P&L sim hoy (2026-08-11) | 🔴 -5.43 $ |
| Operaciones resueltas | 107926 (66341 WIN / 41585 LOSS) — 61.5% |
| Señales abiertas | 462 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 11206 | 61.9% | +0.119 | ➡️ estable | +5550.33$ | 1.19$ | ✅ activa |
| GBM_LATE_15M | 13548 | 60.3% | +0.103 | ➡️ estable | +4613.86$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 10344 | 59.4% | +0.094 | 📈 madura (+0.05) | +3900.49$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3587 | 66.0% | +0.160 | ➡️ estable | +1817.65$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 977 | 74.6% | +0.246 | 📈 madura (+0.07) | +892.89$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 4061 | 55.9% | +0.059 | 📈 madura (+0.07) | +565.87$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 732 | 77.9% | +0.278 | 📈 madura (+0.16) | +326.70$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 445 | 54.6% | +0.046 | 📉 agota (-0.13) | +96.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 157 | 77.1% | +0.267 | 📉 agota (-0.05) | +85.58$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 324 | 80.9% | +0.307 | ➡️ estable | +66.15$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 1622 | 49.1% | -0.009 | 📈 madura (+0.05) | +40.66$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1658 | 62.8% | +0.128 | 📉 agota (-0.03) | +17.95$ | 1.28$ | ✅ activa |
| GBM_LATE_60M | 410 | 42.4% | -0.075 | 📈 madura (+0.11) | +15.68$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1725 | 51.4% | +0.014 | ➡️ estable | +15.43$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 327 | 51.7% | +0.017 | 📉 agota (-0.07) | +13.04$ | 0.50$ | ✅ activa |
| STRUCT_NO_15M | 790 | 53.2% | +0.032 | ➡️ estable | +12.27$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 328 | 55.2% | +0.052 | 📉 agota (-0.14) | +11.28$ | 0.52$ | ✅ activa |
| RESOLUTION_SNIPER | 32 | 81.2% | +0.294 | 📉 agota (-0.11) | +6.65$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1895 | 55.1% | +0.051 | 📉 agota (-0.15) | +3.29$ | 0.51$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 33 | 48.5% | -0.014 | 📉 agota (-0.13) | -0.12$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 169 | 53.3% | +0.032 | ➡️ estable | -0.31$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 144 | 93.8% | +0.432 | 📈 madura (+0.04) | -1.25$ | 2.00$ | ✅ activa |
| STREAK_FADE_60M | 6 | 16.7% | -0.075 | — | -2.08$ | 0.50$ | ⏳ acumulando |
| LIQUIDACIONES_60M | 148 | 50.7% | +0.007 | ➡️ estable | -3.73$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM | 195 | 33.3% | -0.165 | 📉 agota (-0.09) | -6.73$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 395 | 43.8% | -0.062 | 📉 agota (-0.14) | -6.75$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM_FADE | 52 | 21.2% | -0.278 | 📉 agota (-0.11) | -13.27$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 135 | 87.4% | +0.369 | 📈 madura (+0.10) | -16.19$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_5M | 86 | 31.4% | -0.182 | ➡️ estable | -17.18$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 656 | 79.4% | +0.293 | 📉 agota (-0.03) | -18.62$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 356 | 77.5% | +0.274 | 📉 agota (-0.09) | -19.91$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 140 | 38.6% | -0.113 | ➡️ estable | -20.01$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 251 | 44.6% | -0.053 | 📉 agota (-0.08) | -26.50$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_FADE | 132 | 18.2% | -0.313 | 📈 madura (+0.06) | -27.52$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 325 | 43.7% | -0.063 | 📉 agota (-0.10) | -27.91$ | 0.50$ | 🚫 desactivada |
| UPDOWN_OU_5M | 347 | 32.0% | -0.179 | 📉 agota (-0.03) | -61.22$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2984 | 70.1% | +0.201 | ➡️ estable | -186.39$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 3269 | 45.0% | -0.050 | 📈 madura (+0.06) | -630.44$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 30050 | 61.8% | +0.118 | ➡️ estable | -784.73$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13856 | 70.0% | +0.200 | ➡️ estable | -1004.92$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-11T00:41 | BALLENAS_TARDIAS#SOL#5min | … | ✅ WIN | +0.33$ |
| 2026-08-11T00:41 | BALLENAS_TARDIAS#ETH#5min | … | ✅ WIN | +0.11$ |
| 2026-08-11T00:41 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.43$ |
| 2026-08-11T00:41 | FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | … | ✅ WIN | +0.31$ |
| 2026-08-11T00:41 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | … | ✅ WIN | +0.43$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-11T00:39 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,933.96 | 0.1min |  |
| ✅ ETH | $1,872.67 | 0.1min |  |
| ✅ SOL | $75.89 | 0.1min |  |
| ✅ XRP | $1.01 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,945.90 | consenso |  |
| ETH | $1,873.04 | consenso |  |
| SOL | $75.89 | consenso |  |
| XRP | $1.01 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*