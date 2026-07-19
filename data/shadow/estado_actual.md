# Estado del bot — 2026-07-19 20:22 UTC

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
| P&L fiel (stake fijo 1$) | +3155.68 $ |
| P&L sim compuesto | 🟢 +5744.69 $ (ficción Kelly: +22581% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +582.92 $ |
| Operaciones resueltas | 23137 (14033 WIN / 9104 LOSS) — 60.7% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5931 | 60.7% | +0.107 | ➡️ estable | +2042.99$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3153 | 65.2% | +0.152 | ➡️ estable | +1908.97$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3107 | 60.1% | +0.101 | 📈 madura (+0.04) | +1109.70$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 673 | 67.8% | +0.177 | ➡️ estable | +295.94$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1858 | 52.2% | +0.022 | 📈 madura (+0.12) | +138.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 175 | 65.7% | +0.155 | 📈 madura (+0.05) | +97.45$ | 1.55$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3948 | 68.6% | +0.186 | ➡️ estable | +55.69$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 225 | 59.6% | +0.095 | ➡️ estable | +33.25$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 342 | 64.6% | +0.145 | 📉 agota (-0.05) | +15.62$ | 1.45$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 201 | 53.7% | +0.037 | 📉 agota (-0.12) | +14.46$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 74 | 78.4% | +0.276 | 📉 agota (-0.10) | +11.48$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 118 | 57.6% | +0.075 | 📈 madura (+0.07) | +8.90$ | 0.75$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 160 | 81.9% | +0.315 | ➡️ estable | +8.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-19T20:21 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 19, 4:15PM-4:20PM ET… | ✅ WIN | +0.30$ |
| 2026-07-19T20:18 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 4:00PM-4:15PM ET… | ✅ WIN | +0.57$ |
| 2026-07-19T20:18 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 19, 4:00PM-4:15PM ET… | ✅ WIN | +0.57$ |
| 2026-07-19T20:18 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 19, 4:00PM-4:15PM ET… | ✅ WIN | +0.32$ |
| 2026-07-19T20:18 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 19, 4:00PM-4:15PM ET… | ✅ WIN | +0.38$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T20:20 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,428.00 | 0.1min |  |
| ✅ ETH | $1,860.76 | 0.1min |  |
| ✅ SOL | $75.91 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,428.00 | consenso |  |
| ETH | $1,860.93 | consenso |  |
| SOL | $75.81 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*