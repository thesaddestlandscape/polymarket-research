# Estado del bot — 2026-07-22 02:23 UTC

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
| P&L fiel (stake fijo 1$) | +3356.90 $ |
| P&L sim compuesto | 🟢 +6382.79 $ (ficción Kelly: +25090% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +19.28 $ |
| Operaciones resueltas | 27978 (16810 WIN / 11168 LOSS) — 60.1% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6701 | 59.8% | +0.098 | ➡️ estable | +2134.79$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3893 | 63.2% | +0.132 | 📉 agota (-0.04) | +2067.85$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3866 | 58.6% | +0.086 | ➡️ estable | +1239.65$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1087 | 66.3% | +0.163 | ➡️ estable | +484.69$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2118 | 52.6% | +0.026 | 📈 madura (+0.11) | +173.38$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4836 | 68.5% | +0.185 | ➡️ estable | +77.23$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | 80.4% | +0.298 | 📈 madura (+0.03) | +24.03$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 678 | 62.4% | +0.124 | 📉 agota (-0.05) | +22.04$ | 1.23$ | ✅ activa |
| GBM_LATE_5M | 265 | 49.1% | -0.009 | 📉 agota (-0.14) | +15.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 241 | 82.2% | +0.319 | ➡️ estable | +13.75$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 260 | 45.8% | -0.042 | 📉 agota (-0.23) | -3.54$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T02:22 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 10:10PM-10:15PM ET… | ✅ WIN | +0.48$ |
| 2026-07-22T02:10 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 9:45PM-10:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T02:10 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 9:45PM-10:00PM ET… | ✅ WIN | +0.22$ |
| 2026-07-22T02:10 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 9:45PM-10:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T02:10 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 21, 9:45PM-10:00PM ET… | ❌ LOSS | -1.66$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T02:21 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,418.21 | 0.1min |  |
| ✅ ETH | $1,932.60 | 0.1min |  |
| ✅ SOL | $78.38 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,418.21 | consenso |  |
| ETH | $1,932.71 | consenso |  |
| SOL | $78.36 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*