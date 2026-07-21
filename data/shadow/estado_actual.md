# Estado del bot — 2026-07-21 13:52 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.78 $** |
| P&L real total | 🟢 **+0.34 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3289.62 $ |
| P&L sim compuesto | 🟢 +6229.17 $ (ficción Kelly: +24486% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -186.31 $ |
| Operaciones resueltas | 26858 (16158 WIN / 10700 LOSS) — 60.2% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6524 | 59.9% | +0.099 | ➡️ estable | +2110.31$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3720 | 63.6% | +0.136 | 📉 agota (-0.04) | +2034.73$ | 1.36$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3694 | 58.8% | +0.088 | ➡️ estable | +1210.93$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 979 | 66.8% | +0.168 | 📉 agota (-0.03) | +445.42$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 2055 | 52.7% | +0.026 | 📈 madura (+0.11) | +168.15$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4635 | 68.6% | +0.186 | ➡️ estable | +72.12$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 251 | 51.0% | +0.010 | 📉 agota (-0.11) | +18.83$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 593 | 62.2% | +0.122 | 📉 agota (-0.04) | +13.24$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 249 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.30$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 222 | 81.5% | +0.312 | ➡️ estable | +10.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 208 | 50.0% | +0.000 | 📉 agota (-0.21) | +6.17$ | 0.50$ | ✅ activa |
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
| 2026-07-21T13:51 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 9:40AM-9:45AM ET… | ❌ LOSS | -1.70$ |
| 2026-07-21T13:48 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 9:35AM-9:40AM ET… | ✅ WIN | +1.31$ |
| 2026-07-21T13:48 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 9:35AM-9:40AM ET… | ✅ WIN | +1.08$ |
| 2026-07-21T13:48 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +1.77$ |
| 2026-07-21T13:48 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +2.05$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T13:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,510.93 | 0.1min |  |
| ✅ ETH | $1,931.41 | 0.1min |  |
| ✅ SOL | $78.43 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,510.93 | consenso |  |
| ETH | $1,931.60 | consenso |  |
| SOL | $78.33 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*