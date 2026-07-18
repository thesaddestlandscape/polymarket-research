# Estado del bot — 2026-07-18 19:21 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2799.32 $ |
| P&L sim compuesto | 🟢 +5025.95 $ (ficción Kelly: +19756% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +521.18 $ |
| Operaciones resueltas | 21115 (12723 WIN / 8392 LOSS) — 60.3% |
| Señales abiertas | 113 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5602 | 60.5% | +0.105 | ➡️ estable | +1843.97$ | 1.05$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2827 | 65.1% | +0.150 | ➡️ estable | +1665.54$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2769 | 60.2% | +0.102 | 📈 madura (+0.03) | +973.83$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 486 | 68.5% | +0.184 | ➡️ estable | +212.75$ | 1.84$ | ✅ activa |
| UPDOWN_GBM | 1776 | 52.1% | +0.021 | 📈 madura (+0.13) | +132.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 165 | 66.7% | +0.165 | 📈 madura (+0.11) | +93.99$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3506 | 68.3% | +0.183 | ➡️ estable | +21.61$ | 1.83$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 179 | 55.3% | +0.052 | 📉 agota (-0.13) | +17.61$ | 0.53$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 210 | 64.8% | +0.146 | 📉 agota (-0.04) | +13.26$ | 1.46$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 50 | 80.0% | +0.288 | ➡️ estable | +10.00$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 125 | 81.6% | +0.311 | ➡️ estable | +4.78$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 31 | 54.8% | +0.045 | ➡️ estable | +0.34$ | 0.50$ | ✅ activa |
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
| 2026-07-18T19:17 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 18, 3:00PM-3:15PM ET… | ✅ WIN | +0.36$ |
| 2026-07-18T19:17 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 18, 3:00PM-3:15PM ET… | ✅ WIN | +0.36$ |
| 2026-07-18T19:17 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 18, 3:00PM-3:15PM ET… | ✅ WIN | +0.36$ |
| 2026-07-18T19:17 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 18, 3:00PM-3:15PM ET… | ✅ WIN | +1.70$ |
| 2026-07-18T19:17 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 18, 3:00PM-3:15PM ET… | ✅ WIN | +1.36$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T19:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,483.14 | 0.1min |  |
| ✅ ETH | $1,856.87 | 0.1min |  |
| ✅ SOL | $75.38 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,486.30 | consenso |  |
| ETH | $1,856.87 | consenso |  |
| SOL | $75.20 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*