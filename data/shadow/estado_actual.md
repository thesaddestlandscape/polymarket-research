# Estado del bot — 2026-07-13 16:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **10.03 $** |
| P&L real total | 🔴 **-15.41 $** |
| P&L real hoy | -4.41 $ |
| P&L real 7 días | +1.17 $ |
| Fees pagados (real) | 7.98 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1463.33 $ |
| P&L sim compuesto | 🟢 +2466.64 $ (ficción Kelly: +9696% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +253.17 $ |
| Operaciones resueltas | 12672 (7298 WIN / 5374 LOSS) — 57.6% |
| Señales abiertas | 112 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3982 | 60.8% | +0.108 | ➡️ estable | +1292.37$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1306 | 65.7% | +0.157 | ➡️ estable | +763.48$ | 1.57$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1352 | 58.5% | +0.085 | ➡️ estable | +378.49$ | 0.85$ | ✅ activa |
| UPDOWN_GBM | 1405 | 50.2% | +0.002 | 📈 madura (+0.08) | +49.02$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 85 | 62.4% | +0.121 | 📉 agota (-0.08) | +27.77$ | 1.21$ | ✅ activa |
| STREAK_FADE_15M | 173 | 60.7% | +0.106 | 📈 madura (+0.16) | +20.86$ | 1.06$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 142 | 34.5% | -0.153 | 📉 agota (-0.12) | -0.70$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 228 | 47.4% | -0.026 | 📉 agota (-0.07) | -15.52$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1374 | 67.3% | +0.173 | ➡️ estable | -23.83$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T16:16 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 12:00PM-12:15PM ET… | ✅ WIN | +2.26$ |
| 2026-07-13T16:16 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 13, 12:00PM-12:15PM ET… | ✅ WIN | +1.02$ |
| 2026-07-13T16:16 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 12:00PM-12:15PM ET… | ✅ WIN | +0.88$ |
| 2026-07-13T16:16 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 12:00PM-12:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T16:16 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 13, 12:00PM-12:15PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T16:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,469.68 | 0.1min |  |
| ✅ ETH | $1,776.61 | 0.1min |  |
| ✅ SOL | $75.80 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,478.00 | consenso |  |
| ETH | $1,776.82 | consenso |  |
| SOL | $75.86 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*