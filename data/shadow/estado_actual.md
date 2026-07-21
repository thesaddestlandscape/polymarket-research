# Estado del bot — 2026-07-21 14:04 UTC

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
| P&L fiel (stake fijo 1$) | +3302.19 $ |
| P&L sim compuesto | 🟢 +6243.10 $ (ficción Kelly: +24541% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -172.38 $ |
| Operaciones resueltas | 26873 (16170 WIN / 10703 LOSS) — 60.2% |
| Señales abiertas | 125 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6527 | 59.9% | +0.099 | ➡️ estable | +2114.07$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3723 | 63.6% | +0.136 | 📉 agota (-0.04) | +2040.97$ | 1.36$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3697 | 58.8% | +0.088 | ➡️ estable | +1214.08$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 981 | 66.9% | +0.168 | ➡️ estable | +449.46$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 2056 | 52.7% | +0.027 | 📈 madura (+0.11) | +169.49$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4637 | 68.5% | +0.185 | ➡️ estable | +68.04$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 251 | 51.0% | +0.010 | 📉 agota (-0.11) | +18.83$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 593 | 62.2% | +0.122 | 📉 agota (-0.04) | +13.24$ | 1.22$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 250 | 51.6% | +0.016 | 📉 agota (-0.15) | +11.79$ | 0.50$ | ✅ activa |
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
| 2026-07-21T13:54 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +2.19$ |
| 2026-07-21T13:54 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +1.84$ |
| 2026-07-21T13:54 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +1.84$ |
| 2026-07-21T13:54 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +1.84$ |
| 2026-07-21T13:54 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 21, 9:30AM-9:45AM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T14:02 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,694.84 | 0.1min |  |
| ✅ ETH | $1,938.60 | 0.1min |  |
| ✅ SOL | $78.54 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,694.84 | consenso |  |
| ETH | $1,938.57 | consenso |  |
| SOL | $78.41 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*