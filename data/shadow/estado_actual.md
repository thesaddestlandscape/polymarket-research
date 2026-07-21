# Estado del bot — 2026-07-21 13:17 UTC

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
| P&L fiel (stake fijo 1$) | +3280.61 $ |
| P&L sim compuesto | 🟢 +6228.10 $ (ficción Kelly: +24482% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -187.38 $ |
| Operaciones resueltas | 26808 (16128 WIN / 10680 LOSS) — 60.2% |
| Señales abiertas | 117 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6515 | 59.9% | +0.099 | ➡️ estable | +2109.10$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3711 | 63.6% | +0.136 | 📉 agota (-0.04) | +2031.00$ | 1.36$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3688 | 58.8% | +0.088 | ➡️ estable | +1211.31$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 976 | 66.9% | +0.169 | 📉 agota (-0.03) | +445.95$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2055 | 52.7% | +0.026 | 📈 madura (+0.11) | +168.15$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4626 | 68.6% | +0.186 | ➡️ estable | +79.63$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 248 | 50.4% | +0.004 | 📉 agota (-0.13) | +14.62$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 249 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 586 | 62.1% | +0.121 | 📉 agota (-0.04) | +12.08$ | 1.21$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 221 | 81.4% | +0.312 | ➡️ estable | +10.41$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 205 | 50.2% | +0.002 | 📉 agota (-0.21) | +7.31$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
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
| 2026-07-21T13:13 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 9:05AM-9:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T13:10 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 9:00AM-9:05AM ET… | ❌ LOSS | -1.80$ |
| 2026-07-21T13:10 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 8:55AM-9:00AM ET… | ✅ WIN | +2.66$ |
| 2026-07-21T13:07 | STREAK_FADE_15M#ETH#15min | Ethereum Up or Down - July 21, 8:45AM-9:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T13:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T13:15 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,580.23 | 0.1min |  |
| ✅ ETH | $1,940.83 | 0.1min |  |
| ✅ SOL | $78.55 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,580.23 | consenso |  |
| ETH | $1,940.83 | consenso |  |
| SOL | $78.49 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*