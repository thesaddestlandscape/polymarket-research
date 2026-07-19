# Estado del bot — 2026-07-19 17:52 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3093.94 $ |
| P&L sim compuesto | 🟢 +5625.39 $ (ficción Kelly: +22112% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +463.62 $ |
| Operaciones resueltas | 22951 (13908 WIN / 9043 LOSS) — 60.6% |
| Señales abiertas | 155 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5898 | 60.6% | +0.106 | ➡️ estable | +2000.93$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3126 | 65.1% | +0.151 | ➡️ estable | +1865.44$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3075 | 60.0% | +0.100 | 📈 madura (+0.04) | +1078.67$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 658 | 67.5% | +0.174 | ➡️ estable | +284.30$ | 1.74$ | ✅ activa |
| UPDOWN_GBM | 1850 | 52.1% | +0.021 | 📈 madura (+0.12) | +136.22$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 171 | 64.9% | +0.147 | 📈 madura (+0.05) | +91.10$ | 1.47$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3903 | 68.7% | +0.187 | ➡️ estable | +67.34$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 225 | 59.6% | +0.095 | ➡️ estable | +33.25$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 333 | 65.5% | +0.154 | 📉 agota (-0.05) | +21.72$ | 1.54$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 195 | 53.8% | +0.038 | 📉 agota (-0.12) | +14.61$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 71 | 78.9% | +0.281 | 📉 agota (-0.07) | +12.56$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 116 | 57.8% | +0.076 | 📈 madura (+0.05) | +7.96$ | 0.76$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 159 | 81.8% | +0.314 | ➡️ estable | +7.40$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-19T17:49 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 19, 1:30PM-1:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T17:49 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 19, 1:30PM-1:45PM ET… | ❌ LOSS | -1.39$ |
| 2026-07-19T17:49 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 19, 1:30PM-1:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T17:49 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 19, 1:30PM-1:45PM ET… | ✅ WIN | +8.77$ |
| 2026-07-19T17:49 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 19, 1:30PM-1:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T17:51 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,561.51 | 0.1min |  |
| ✅ ETH | $1,868.56 | 0.1min |  |
| ✅ SOL | $76.04 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,561.51 | consenso |  |
| ETH | $1,868.56 | consenso |  |
| SOL | $75.97 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*