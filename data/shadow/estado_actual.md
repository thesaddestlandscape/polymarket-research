# Estado del bot — 2026-07-14 06:25 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **10.39 $** |
| P&L real total | 🔴 **-15.05 $** |
| P&L real hoy | +0.37 $ |
| P&L real 7 días | -5.11 $ |
| Fees pagados (real) | 8.07 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1562.77 $ |
| P&L sim compuesto | 🟢 +2691.85 $ (ficción Kelly: +10581% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +137.64 $ |
| Operaciones resueltas | 13467 (7790 WIN / 5677 LOSS) — 57.8% |
| Señales abiertas | 74 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4169 | 60.7% | +0.107 | ➡️ estable | +1347.74$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1482 | 65.8% | +0.158 | ➡️ estable | +918.00$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1448 | 58.3% | +0.083 | ➡️ estable | +399.31$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1453 | 50.4% | +0.004 | 📈 madura (+0.09) | +55.28$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 95 | 58.9% | +0.088 | 📉 agota (-0.05) | +24.00$ | 0.88$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1627 | 67.8% | +0.178 | ➡️ estable | -20.95$ | 1.77$ | ✅ activa |
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T06:20 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 2:00AM-2:15AM ET… | ❌ LOSS | -0.92$ |
| 2026-07-14T06:20 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 2:00AM-2:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T06:20 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 2:00AM-2:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T06:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 2:00AM-2:15AM ET… | ✅ WIN | +0.64$ |
| 2026-07-14T06:20 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 14, 2:00AM-2:15AM ET… | ✅ WIN | +0.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T06:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,600.25 | 0.1min |  |
| ✅ ETH | $1,784.15 | 0.1min |  |
| ✅ SOL | $75.32 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,600.25 | consenso |  |
| ETH | $1,784.62 | consenso |  |
| SOL | $75.17 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*