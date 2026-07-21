# Estado del bot — 2026-07-21 07:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3371.94 $ |
| P&L sim compuesto | 🟢 +6277.65 $ (ficción Kelly: +24676% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -137.83 $ |
| Operaciones resueltas | 26222 (15853 WIN / 10369 LOSS) — 60.5% |
| Señales abiertas | 113 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6420 | 60.2% | +0.102 | ➡️ estable | +2121.40$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3616 | 64.1% | +0.141 | ➡️ estable | +2059.45$ | 1.41$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3594 | 59.2% | +0.092 | ➡️ estable | +1216.14$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 941 | 67.3% | +0.172 | 📉 agota (-0.03) | +438.68$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 2037 | 52.7% | +0.027 | 📈 madura (+0.12) | +163.21$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 204 | 63.7% | +0.136 | ➡️ estable | +104.36$ | 1.36$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4528 | 68.6% | +0.185 | ➡️ estable | +57.26$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 234 | 53.4% | +0.034 | 📉 agota (-0.08) | +21.76$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 551 | 63.0% | +0.129 | 📉 agota (-0.03) | +19.13$ | 1.29$ | ✅ activa |
| LATE_WINDOW_5MIN | 138 | 57.2% | +0.071 | 📉 agota (-0.24) | +18.51$ | 0.68$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 98 | 79.6% | +0.290 | 📉 agota (-0.04) | +17.58$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 210 | 82.4% | +0.321 | ➡️ estable | +13.46$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 246 | 52.0% | +0.020 | 📉 agota (-0.14) | +12.78$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-21T07:16 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 3:05AM-3:10AM ET… | ✅ WIN | +0.44$ |
| 2026-07-21T07:16 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 3:00AM-3:15AM ET… | ✅ WIN | +2.08$ |
| 2026-07-21T07:16 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 3:00AM-3:15AM ET… | ❌ LOSS | -0.99$ |
| 2026-07-21T07:16 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 3:00AM-3:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T07:16 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 3:00AM-3:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T07:16 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,862.04 | 0.1min |  |
| ✅ ETH | $1,934.69 | 0.1min |  |
| ✅ SOL | $78.61 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,872.20 | consenso |  |
| ETH | $1,934.69 | consenso |  |
| SOL | $78.61 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*