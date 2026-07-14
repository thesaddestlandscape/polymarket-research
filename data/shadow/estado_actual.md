# Estado del bot — 2026-07-14 08:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **9.30 $** |
| P&L real total | 🔴 **-16.14 $** |
| P&L real hoy | -0.72 $ |
| P&L real 7 días | -6.20 $ |
| Fees pagados (real) | 8.11 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1558.80 $ |
| P&L sim compuesto | 🟢 +2689.25 $ (ficción Kelly: +10571% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +135.04 $ |
| Operaciones resueltas | 13549 (7837 WIN / 5712 LOSS) — 57.8% |
| Señales abiertas | 73 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4191 | 60.6% | +0.106 | ➡️ estable | +1342.49$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1502 | 65.6% | +0.156 | ➡️ estable | +914.03$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1454 | 58.3% | +0.082 | ➡️ estable | +398.02$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1455 | 50.4% | +0.004 | 📈 madura (+0.09) | +55.09$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 96 | 59.4% | +0.092 | 📉 agota (-0.06) | +25.92$ | 0.92$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1658 | 67.9% | +0.178 | ➡️ estable | -14.79$ | 1.78$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T08:07 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 14, 12:00AM-4:00AM ET… | ❌ LOSS | -1.53$ |
| 2026-07-14T08:05 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 3:45AM-4:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T08:05 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 3:45AM-4:00AM ET… | ✅ WIN | +1.38$ |
| 2026-07-14T08:05 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 3:45AM-4:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T08:05 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 14, 3:45AM-4:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T08:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,440.81 | 0.1min |  |
| ✅ ETH | $1,777.67 | 0.1min |  |
| ✅ SOL | $75.05 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,440.81 | consenso |  |
| ETH | $1,777.67 | consenso |  |
| SOL | $74.86 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*