# Estado del bot — 2026-07-14 01:36 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **10.03 $** |
| P&L real total | 🔴 **-15.41 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -5.48 $ |
| Fees pagados (real) | 7.98 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1494.67 $ |
| P&L sim compuesto | 🟢 +2554.45 $ (ficción Kelly: +10041% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +0.25 $ |
| Operaciones resueltas | 13225 (7629 WIN / 5596 LOSS) — 57.7% |
| Señales abiertas | 76 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4106 | 60.7% | +0.107 | ➡️ estable | +1311.60$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1425 | 65.6% | +0.156 | ➡️ estable | +835.17$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1425 | 58.2% | +0.082 | ➡️ estable | +386.59$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1443 | 50.5% | +0.004 | 📈 madura (+0.08) | +56.25$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 94 | 59.6% | +0.094 | 📉 agota (-0.04) | +24.51$ | 0.94$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
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
| STREAK_FADE_5M | 245 | 45.3% | -0.047 | 📉 agota (-0.04) | -23.43$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1542 | 67.5% | +0.175 | ➡️ estable | -28.67$ | 1.75$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T01:32 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 9:15PM-9:30PM ET… | ✅ WIN | +1.01$ |
| 2026-07-14T01:32 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 9:15PM-9:30PM ET… | ✅ WIN | +1.92$ |
| 2026-07-14T01:32 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 13, 9:15PM-9:30PM ET… | ❌ LOSS | -1.81$ |
| 2026-07-14T01:32 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 13, 9:15PM-9:30PM ET… | ❌ LOSS | -1.37$ |
| 2026-07-14T01:32 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 9:15PM-9:30PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T01:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,417.99 | 0.1min |  |
| ✅ ETH | $1,783.74 | 0.1min |  |
| ✅ SOL | $75.25 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,439.90 | consenso |  |
| ETH | $1,783.74 | consenso |  |
| SOL | $75.16 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*