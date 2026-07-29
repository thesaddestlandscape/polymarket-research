# Estado del bot — 2026-07-29 23:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **21.50 $** |
| P&L real total | 🔴 **-29.72 $** |
| P&L real hoy | +1.97 $ |
| P&L real 7 días | -1.01 $ |
| Fees pagados (real) | 11.55 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +4887.03 $ |
| P&L sim compuesto | 🟢 +9331.05 $ (ficción Kelly: +36679% s/ operativo) |
| P&L sim hoy (2026-07-29) | 🟢 +694.51 $ |
| Operaciones resueltas | 42505 (25450 WIN / 17055 LOSS) — 59.9% |
| Señales abiertas | 88 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 6361 | 62.1% | +0.121 | 📉 agota (-0.07) | +3137.39$ | 1.21$ | ✅ activa |
| GBM_LATE_15M | 9174 | 59.5% | +0.095 | ➡️ estable | +2793.51$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 6359 | 56.7% | +0.067 | 📉 agota (-0.07) | +1798.90$ | 0.67$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 2422 | 65.3% | +0.153 | ➡️ estable | +1086.29$ | 1.53$ | ✅ activa |
| UPDOWN_GBM | 3125 | 54.0% | +0.040 | 📈 madura (+0.06) | +310.79$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 457 | 73.5% | +0.234 | 📈 madura (+0.27) | +132.04$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 320 | 55.0% | +0.050 | 📉 agota (-0.23) | +97.50$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 207 | 81.2% | +0.309 | 📈 madura (+0.03) | +47.29$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 1456 | 59.4% | +0.094 | 📉 agota (-0.06) | +29.78$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 304 | 56.2% | +0.062 | 📉 agota (-0.11) | +20.40$ | 0.62$ | ✅ activa |
| ORDER_FLOW_5M | 1688 | 51.1% | +0.011 | ➡️ estable | +11.00$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 310 | 51.0% | +0.010 | 📉 agota (-0.11) | +9.65$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 40 | 90.0% | +0.381 | ➡️ estable | +7.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 459 | 80.4% | +0.303 | ➡️ estable | +6.19$ | 2.00$ | ✅ activa |
| BALLENAS_TARDIAS | 85 | 80.0% | +0.293 | 📉 agota (-0.20) | +5.28$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 343 | 39.1% | -0.109 | 📈 madura (+0.03) | +4.07$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 17 | 88.2% | +0.291 | — | +3.97$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 10 | 90.0% | +0.167 | — | +2.83$ | 1.67$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 6 | 100.0% | +0.112 | — | +0.19$ | 1.12$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1 | 0.0% | -0.008 | — | -0.51$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 25 | 48.0% | -0.019 | — | -1.25$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 1004 | 46.8% | -0.032 | ➡️ estable | -2.46$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 72 | 81.9% | +0.311 | 📉 agota (-0.13) | -4.08$ | 2.00$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 386 | 43.5% | -0.064 | 📉 agota (-0.16) | -7.81$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 7014 | 67.6% | +0.176 | ➡️ estable | -60.32$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-29T23:11 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 29, 6:45PM-6:50PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-29T23:11 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 29, 6:30PM-6:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-29T23:11 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 29, 6:30PM-6:45PM ET… | ❌ LOSS | -1.78$ |
| 2026-07-29T23:11 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 29, 6:30PM-6:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-29T23:11 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 29, 6:30PM-6:45PM ET… | ❌ LOSS | -1.86$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-29T23:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,891.88 | 0.2min |  |
| ✅ ETH | $1,903.98 | 0.2min |  |
| ✅ SOL | $73.44 | 0.2min |  |
| ✅ XRP | $1.07 | 0.2min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,834.02 | consenso |  |
| ETH | $1,901.65 | consenso |  |
| SOL | $73.35 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*