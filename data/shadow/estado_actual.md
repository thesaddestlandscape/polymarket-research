# Estado del bot — 2026-07-14 12:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **8.21 $** |
| P&L real total | 🔴 **-17.23 $** |
| P&L real hoy | -1.81 $ |
| P&L real 7 días | -7.29 $ |
| Fees pagados (real) | 8.15 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1556.74 $ |
| P&L sim compuesto | 🟢 +2693.26 $ (ficción Kelly: +10587% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +139.06 $ |
| Operaciones resueltas | 13741 (7949 WIN / 5792 LOSS) — 57.8% |
| Señales abiertas | 72 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4241 | 60.4% | +0.104 | ➡️ estable | +1322.00$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1547 | 65.3% | +0.153 | ➡️ estable | +920.60$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1481 | 58.1% | +0.081 | ➡️ estable | +398.56$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1466 | 50.6% | +0.006 | 📈 madura (+0.08) | +59.93$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 99 | 59.6% | +0.094 | 📉 agota (-0.07) | +27.72$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1713 | 68.2% | +0.182 | ➡️ estable | -2.51$ | 1.81$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T11:52 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 14, 7:30AM-7:45AM ET… | ❌ LOSS | -1.72$ |
| 2026-07-14T11:52 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 7:30AM-7:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T11:52 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 7:30AM-7:45AM ET… | ✅ WIN | +1.44$ |
| 2026-07-14T11:47 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 7:30AM-7:45AM ET… | ❌ LOSS | -1.27$ |
| 2026-07-14T11:47 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 14, 7:30AM-7:45AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T11:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,768.00 | 0.1min |  |
| ✅ ETH | $1,795.87 | 0.1min |  |
| ✅ SOL | $75.39 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,774.60 | consenso |  |
| ETH | $1,795.87 | consenso |  |
| SOL | $75.32 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*