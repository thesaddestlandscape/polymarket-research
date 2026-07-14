# Estado del bot — 2026-07-14 16:04 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **7.10 $** |
| P&L real total | 🔴 **-18.34 $** |
| P&L real hoy | -2.93 $ |
| P&L real 7 días | -8.40 $ |
| Fees pagados (real) | 8.21 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1577.27 $ |
| P&L sim compuesto | 🟢 +2744.91 $ (ficción Kelly: +10790% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +190.70 $ |
| Operaciones resueltas | 14021 (8119 WIN / 5902 LOSS) — 57.9% |
| Señales abiertas | 71 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4299 | 60.2% | +0.102 | 📉 agota (-0.03) | +1323.61$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1595 | 65.5% | +0.154 | ➡️ estable | +953.61$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1536 | 58.0% | +0.080 | ➡️ estable | +409.55$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1478 | 50.8% | +0.008 | 📈 madura (+0.08) | +68.47$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 105 | 59.0% | +0.089 | 📉 agota (-0.12) | +29.19$ | 0.89$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 237 | 61.2% | +0.111 | 📈 madura (+0.29) | +8.65$ | 1.11$ | ✅ activa |
| GBM_LATE_60M | 324 | 38.6% | -0.113 | ➡️ estable | +4.84$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1790 | 67.9% | +0.179 | ➡️ estable | -17.60$ | 1.78$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T16:00 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 11:45AM-12:00PM ET… | ✅ WIN | +0.48$ |
| 2026-07-14T16:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -1.38$ |
| 2026-07-14T16:00 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 11:45AM-12:00PM ET… | ✅ WIN | +0.61$ |
| 2026-07-14T16:00 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T16:00 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -1.83$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T16:03 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,687.04 | 0.1min |  |
| ✅ ETH | $1,870.28 | 0.1min |  |
| ✅ SOL | $77.24 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,687.04 | consenso |  |
| ETH | $1,870.28 | consenso |  |
| SOL | $77.15 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*