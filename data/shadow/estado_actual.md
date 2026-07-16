# Estado del bot — 2026-07-16 22:22 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **4.03 $** |
| P&L real total | 🔴 **-21.41 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -28.65 $ |
| Fees pagados (real) | 8.57 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2083.45 $ |
| P&L sim compuesto | 🟢 +3651.91 $ (ficción Kelly: +14355% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +383.48 $ |
| Operaciones resueltas | 17662 (10409 WIN / 7253 LOSS) — 58.9% |
| Señales abiertas | 74 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5024 | 60.2% | +0.102 | ➡️ estable | +1560.90$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2231 | 64.9% | +0.148 | 📉 agota (-0.04) | +1279.99$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2212 | 59.3% | +0.093 | ➡️ estable | +678.91$ | 0.93$ | ✅ activa |
| UPDOWN_GBM | 1622 | 50.8% | +0.008 | 📈 madura (+0.09) | +66.55$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 174 | 66.1% | +0.159 | 📉 agota (-0.10) | +48.32$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 103 | 64.1% | +0.138 | 📈 madura (+0.10) | +47.59$ | 1.38$ | ✅ activa |
| STREAK_FADE_15M | 206 | 60.2% | +0.101 | 📈 madura (+0.04) | +31.61$ | 1.01$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 46 | 73.9% | +0.229 | ➡️ estable | +22.79$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 152 | 56.6% | +0.065 | 📉 agota (-0.13) | +19.08$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 21 | 76.2% | +0.239 | — | +1.44$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 56 | 80.4% | +0.293 | 📈 madura (+0.03) | -0.19$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2726 | 67.5% | +0.174 | ➡️ estable | -60.83$ | 1.74$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T22:21 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 16, 6:00PM-6:15PM ET… | ✅ WIN | +0.17$ |
| 2026-07-16T22:21 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 16, 6:00PM-6:15PM ET… | ❌ LOSS | -1.97$ |
| 2026-07-16T22:21 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 16, 6:00PM-6:15PM ET… | ✅ WIN | +0.32$ |
| 2026-07-16T22:21 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 6:00PM-6:15PM ET… | ✅ WIN | +0.20$ |
| 2026-07-16T22:21 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 16, 6:00PM-6:15PM ET… | ✅ WIN | +0.24$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T22:20 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,126.69 | 0.1min |  |
| ✅ ETH | $1,878.04 | 0.1min |  |
| ✅ SOL | $75.86 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,126.69 | consenso |  |
| ETH | $1,878.11 | consenso |  |
| SOL | $75.88 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*