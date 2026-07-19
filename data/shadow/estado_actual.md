# Estado del bot — 2026-07-19 13:54 UTC

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
| P&L fiel (stake fijo 1$) | +3022.11 $ |
| P&L sim compuesto | 🟢 +5490.09 $ (ficción Kelly: +21581% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +328.32 $ |
| Operaciones resueltas | 22592 (13661 WIN / 8931 LOSS) — 60.5% |
| Señales abiertas | 146 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5841 | 60.6% | +0.106 | ➡️ estable | +1969.93$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3067 | 65.0% | +0.150 | ➡️ estable | +1827.15$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3017 | 59.9% | +0.099 | 📈 madura (+0.03) | +1058.38$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 623 | 67.9% | +0.178 | ➡️ estable | +281.26$ | 1.78$ | ✅ activa |
| UPDOWN_GBM | 1828 | 52.0% | +0.020 | 📈 madura (+0.12) | +131.84$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 170 | 65.3% | +0.151 | 📈 madura (+0.06) | +91.61$ | 1.51$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3826 | 68.5% | +0.185 | ➡️ estable | +41.28$ | 1.85$ | ✅ activa |
| STREAK_FADE_15M | 225 | 59.6% | +0.095 | ➡️ estable | +33.25$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 309 | 65.0% | +0.150 | 📉 agota (-0.05) | +18.00$ | 1.49$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 192 | 53.6% | +0.036 | 📉 agota (-0.11) | +14.03$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 63 | 77.8% | +0.269 | 📉 agota (-0.05) | +10.04$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 328 | 38.7% | -0.112 | ➡️ estable | +6.48$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 152 | 81.6% | +0.312 | ➡️ estable | +6.17$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 108 | 56.5% | +0.064 | 📈 madura (+0.05) | +3.26$ | 0.64$ | ✅ activa |
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
| 2026-07-19T13:50 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 9:30AM-9:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-19T13:50 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 19, 9:30AM-9:45AM ET… | ✅ WIN | +0.41$ |
| 2026-07-19T13:50 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 19, 9:30AM-9:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T13:50 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 9:30AM-9:45AM ET… | ❌ LOSS | -1.53$ |
| 2026-07-19T13:50 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 19, 9:30AM-9:45AM ET… | ❌ LOSS | -1.71$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T13:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,404.74 | 0.1min |  |
| ✅ ETH | $1,870.07 | 0.1min |  |
| ✅ SOL | $76.14 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,412.20 | consenso |  |
| ETH | $1,870.07 | consenso |  |
| SOL | $76.00 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*