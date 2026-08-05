# Estado del bot — 2026-08-05 12:30 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **11.90 $** |
| P&L real total | 🔴 **-39.32 $** |
| P&L real hoy | -4.57 $ |
| P&L real 7 días | -9.67 $ |
| Fees pagados (real) | 14.38 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +5889.17 $ |
| P&L sim compuesto | 🟢 +12630.73 $ (ficción Kelly: +49649% s/ operativo) |
| P&L sim hoy (2026-08-05) | 🟢 +279.32 $ |
| Operaciones resueltas | 73944 (45357 WIN / 28587 LOSS) — 61.3% |
| Señales abiertas | 347 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M_ESPACIO_ATR | 9112 | 62.8% | +0.128 | ➡️ estable | +4530.73$ | 1.28$ | ✅ activa |
| GBM_LATE_15M | 11719 | 60.1% | +0.101 | ➡️ estable | +3795.98$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 9047 | 58.0% | +0.080 | ➡️ estable | +2906.13$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 3167 | 66.7% | +0.166 | ➡️ estable | +1633.14$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 3725 | 55.9% | +0.059 | 📈 madura (+0.07) | +518.07$ | 0.59$ | ✅ activa |
| WEEKLY_PRICE | 598 | 75.3% | +0.252 | 📈 madura (+0.18) | +204.07$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 405 | 54.8% | +0.048 | 📉 agota (-0.18) | +94.77$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 272 | 81.6% | +0.314 | ➡️ estable | +61.04$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_IBS_ALTO | 88 | 78.4% | +0.278 | 📈 madura (+0.11) | +53.29$ | 2.00$ | ✅ activa |
| STREAK_FADE_15M | 307 | 56.0% | +0.060 | 📉 agota (-0.12) | +19.35$ | 0.60$ | ✅ activa |
| GBM_LATE_5M | 1362 | 47.7% | -0.023 | ➡️ estable | +17.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 324 | 51.5% | +0.015 | 📉 agota (-0.07) | +12.60$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1710 | 51.2% | +0.012 | ➡️ estable | +12.04$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 359 | 40.7% | -0.093 | 📈 madura (+0.09) | +10.17$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 26 | 76.9% | +0.250 | — | +3.90$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 30 | 50.0% | +0.000 | 📉 agota (-0.18) | +0.91$ | 0.50$ | ✅ activa |
| PRICE_TARGET_GBM_FADE | 2 | 50.0% | +0.000 | — | +0.18$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STREAK_FADE_60M | 3 | 33.3% | -0.015 | — | -0.55$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 562 | 80.2% | +0.301 | 📉 agota (-0.03) | -0.73$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 218 | 79.8% | +0.295 | 📉 agota (-0.04) | -1.74$ | 2.00$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_15MIN_EXTREMO | 70 | 91.4% | +0.403 | 📉 agota (-0.05) | -3.47$ | 2.00$ | ✅ activa |
| LIQUIDACIONES_15M | 9 | 11.1% | -0.143 | — | -3.73$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_60M_FADE | 8 | 0.0% | -0.160 | — | -4.08$ | 0.00$ | 🚫 desactivada |
| LIQUIDACIONES_60M | 12 | 16.7% | -0.171 | — | -4.21$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 193 | 33.7% | -0.162 | 📉 agota (-0.09) | -5.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 392 | 43.9% | -0.061 | 📉 agota (-0.14) | -6.21$ | 0.50$ | ⚠️ IC negativo |
| LIQUIDACIONES_5M | 33 | 27.3% | -0.214 | 📉 agota (-0.18) | -7.83$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO_60MIN_EXTREMO | 81 | 84.0% | +0.331 | 📈 madura (+0.07) | -13.79$ | 2.00$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 247 | 44.9% | -0.050 | 📉 agota (-0.06) | -25.47$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |
| BALLENAS_CONFIRMADAS_15M | 1633 | 55.7% | +0.057 | 📉 agota (-0.14) | -31.78$ | 0.57$ | ✅ activa |
| BALLENAS_TARDIAS | 795 | 51.7% | +0.017 | 📉 agota (-0.30) | -70.55$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1312 | 72.6% | +0.225 | 📉 agota (-0.05) | -77.96$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 18537 | 62.4% | +0.124 | 📉 agota (-0.06) | -438.77$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7123 | 70.0% | +0.200 | ➡️ estable | -479.64$ | 2.00$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-08-05T12:28 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - August 5, 8:15AM-8:20AM ET… | ✅ WIN | +1.92$ |
| 2026-08-05T12:28 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | … | ✅ WIN | +0.26$ |
| 2026-08-05T12:28 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | … | ✅ WIN | +0.35$ |
| 2026-08-05T12:28 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | … | ✅ WIN | +0.35$ |
| 2026-08-05T12:28 | FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | … | ✅ WIN | +0.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-08-05T12:27 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,444.00 | 0.1min |  |
| ✅ ETH | $1,878.73 | 0.1min |  |
| ✅ SOL | $74.20 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,415.65 | consenso |  |
| ETH | $1,878.69 | consenso |  |
| SOL | $74.12 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*