# Estado del bot — 2026-07-13 17:18 UTC

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
| P&L fiel (stake fijo 1$) | +1464.58 $ |
| P&L sim compuesto | 🟢 +2464.23 $ (ficción Kelly: +9686% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +250.76 $ |
| Operaciones resueltas | 12740 (7339 WIN / 5401 LOSS) — 57.6% |
| Señales abiertas | 112 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3997 | 60.8% | +0.108 | ➡️ estable | +1288.02$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1321 | 65.6% | +0.155 | ➡️ estable | +762.70$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1360 | 58.5% | +0.084 | ➡️ estable | +375.29$ | 0.84$ | ✅ activa |
| UPDOWN_GBM | 1411 | 50.4% | +0.004 | 📈 madura (+0.08) | +57.19$ | 0.50$ | ✅ activa |
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
| STREAK_FADE_5M | 233 | 47.6% | -0.023 | 📉 agota (-0.05) | -15.15$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1393 | 67.3% | +0.173 | ➡️ estable | -26.47$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T17:17 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 13, 1:10PM-1:15PM ET… | ✅ WIN | +0.32$ |
| 2026-07-13T17:17 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 13, 1:10PM-1:15PM ET… | ✅ WIN | +0.44$ |
| 2026-07-13T17:17 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 1:00PM-1:15PM ET… | ✅ WIN | +0.25$ |
| 2026-07-13T17:17 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 1:00PM-1:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T17:17 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 1:00PM-1:15PM ET… | ✅ WIN | +1.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T17:17 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,247.36 | 0.1min |  |
| ✅ ETH | $1,772.37 | 0.1min |  |
| ✅ SOL | $75.38 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,247.36 | consenso |  |
| ETH | $1,772.37 | consenso |  |
| SOL | $75.33 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*