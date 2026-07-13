# Estado del bot — 2026-07-13 20:00 UTC

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
| P&L fiel (stake fijo 1$) | +1468.11 $ |
| P&L sim compuesto | 🟢 +2496.58 $ (ficción Kelly: +9814% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +283.11 $ |
| Operaciones resueltas | 12893 (7428 WIN / 5465 LOSS) — 57.6% |
| Señales abiertas | 123 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4030 | 60.8% | +0.108 | ➡️ estable | +1297.16$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1353 | 65.7% | +0.157 | ➡️ estable | +788.69$ | 1.57$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1382 | 58.5% | +0.085 | ➡️ estable | +381.96$ | 0.85$ | ✅ activa |
| UPDOWN_GBM | 1419 | 50.3% | +0.003 | 📈 madura (+0.08) | +51.92$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 88 | 61.4% | +0.111 | 📉 agota (-0.04) | +28.70$ | 1.11$ | ✅ activa |
| STREAK_FADE_15M | 175 | 60.6% | +0.105 | 📈 madura (+0.15) | +20.89$ | 1.04$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 142 | 34.5% | -0.153 | 📉 agota (-0.12) | -0.70$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1434 | 67.4% | +0.174 | ➡️ estable | -23.34$ | 1.74$ | ✅ activa |
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T19:45 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 13, 3:30PM-3:45PM ET… | ✅ WIN | +0.30$ |
| 2026-07-13T19:45 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 13, 3:30PM-3:45PM ET… | ❌ LOSS | -1.42$ |
| 2026-07-13T19:45 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 13, 3:30PM-3:45PM ET… | ✅ WIN | +1.92$ |
| 2026-07-13T19:45 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 3:30PM-3:45PM ET… | ✅ WIN | +0.33$ |
| 2026-07-13T19:45 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 3:30PM-3:45PM ET… | ✅ WIN | +0.30$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T19:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,153.11 | 0.1min |  |
| ✅ ETH | $1,770.62 | 0.1min |  |
| ✅ SOL | $75.17 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,169.70 | consenso |  |
| ETH | $1,770.62 | consenso |  |
| SOL | $74.98 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*