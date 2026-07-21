# Estado del bot — 2026-07-21 08:01 UTC

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
| P&L fiel (stake fijo 1$) | +3365.73 $ |
| P&L sim compuesto | 🟢 +6280.79 $ (ficción Kelly: +24689% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -134.69 $ |
| Operaciones resueltas | 26292 (15886 WIN / 10406 LOSS) — 60.4% |
| Señales abiertas | 119 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6431 | 60.1% | +0.101 | ➡️ estable | +2121.51$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3627 | 64.1% | +0.141 | ➡️ estable | +2059.44$ | 1.41$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3604 | 59.2% | +0.092 | ➡️ estable | +1217.65$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 949 | 67.1% | +0.171 | ➡️ estable | +439.82$ | 1.71$ | ✅ activa |
| UPDOWN_GBM | 2042 | 52.7% | +0.027 | 📈 madura (+0.11) | +168.02$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 205 | 63.9% | +0.138 | ➡️ estable | +106.36$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4537 | 68.5% | +0.185 | ➡️ estable | +58.29$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 236 | 53.0% | +0.029 | 📉 agota (-0.09) | +20.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 99 | 79.8% | +0.292 | 📉 agota (-0.03) | +18.38$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 553 | 62.7% | +0.127 | 📉 agota (-0.04) | +16.15$ | 1.27$ | ✅ activa |
| LATE_WINDOW_5MIN | 145 | 55.2% | +0.051 | 📉 agota (-0.25) | +15.83$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 246 | 52.0% | +0.020 | 📉 agota (-0.14) | +12.78$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 212 | 82.1% | +0.318 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 7 | 57.1% | +0.019 | — | +0.36$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T07:51 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 3:45AM-3:50AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T07:51 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 3:40AM-3:45AM ET… | ✅ WIN | +0.38$ |
| 2026-07-21T07:51 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 3:30AM-3:45AM ET… | ❌ LOSS | -0.94$ |
| 2026-07-21T07:51 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 3:30AM-3:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T07:51 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 3:30AM-3:45AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T07:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,980.01 | 0.1min |  |
| ✅ ETH | $1,933.16 | 0.1min |  |
| ✅ SOL | $78.62 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,980.01 | consenso |  |
| ETH | $1,933.16 | consenso |  |
| SOL | $78.43 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*