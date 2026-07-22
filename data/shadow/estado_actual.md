# Estado del bot — 2026-07-22 03:21 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3360.77 $ |
| P&L sim compuesto | 🟢 +6382.03 $ (ficción Kelly: +25087% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +18.52 $ |
| Operaciones resueltas | 28076 (16860 WIN / 11216 LOSS) — 60.1% |
| Señales abiertas | 137 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6713 | 59.8% | +0.098 | ➡️ estable | +2132.71$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3906 | 63.1% | +0.131 | 📉 agota (-0.04) | +2065.55$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3881 | 58.5% | +0.085 | ➡️ estable | +1236.51$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1098 | 66.5% | +0.165 | ➡️ estable | +496.62$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2124 | 52.7% | +0.027 | 📈 madura (+0.11) | +173.07$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4857 | 68.5% | +0.185 | ➡️ estable | +75.40$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 682 | 62.6% | +0.126 | 📉 agota (-0.04) | +24.98$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 115 | 78.3% | +0.278 | ➡️ estable | +18.22$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 269 | 49.4% | -0.006 | 📉 agota (-0.13) | +14.32$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 243 | 81.9% | +0.316 | ➡️ estable | +12.47$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 267 | 45.7% | -0.043 | 📉 agota (-0.22) | -1.70$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T03:20 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 21, 11:00PM-11:15PM ET… | ❌ LOSS | -1.73$ |
| 2026-07-22T03:20 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 11:00PM-11:15PM ET… | ❌ LOSS | -0.78$ |
| 2026-07-22T03:20 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 11:00PM-11:15PM ET… | ✅ WIN | +0.99$ |
| 2026-07-22T03:20 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 11:00PM-11:15PM ET… | ❌ LOSS | -1.53$ |
| 2026-07-22T03:20 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 11:00PM-11:15PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T03:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,175.99 | 0.1min |  |
| ✅ ETH | $1,927.19 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,177.50 | consenso |  |
| ETH | $1,927.19 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*