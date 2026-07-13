# Estado del bot — 2026-07-13 13:46 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **11.12 $** |
| P&L real total | 🔴 **-14.32 $** |
| P&L real hoy | -3.32 $ |
| P&L real 7 días | +2.26 $ |
| Fees pagados (real) | 7.93 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1439.68 $ |
| P&L sim compuesto | 🟢 +2423.27 $ (ficción Kelly: +9525% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +209.80 $ |
| Operaciones resueltas | 12500 (7191 WIN / 5309 LOSS) — 57.5% |
| Señales abiertas | 120 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3949 | 60.9% | +0.109 | ➡️ estable | +1294.53$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1269 | 65.8% | +0.158 | ➡️ estable | +750.94$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1338 | 58.5% | +0.085 | ➡️ estable | +359.32$ | 0.85$ | ✅ activa |
| UPDOWN_GBM | 1395 | 50.1% | +0.001 | 📈 madura (+0.08) | +49.41$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 83 | 62.7% | +0.124 | 📉 agota (-0.11) | +26.32$ | 1.23$ | ✅ activa |
| STREAK_FADE_15M | 171 | 60.8% | +0.107 | 📈 madura (+0.18) | +21.49$ | 1.07$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 220 | 46.8% | -0.032 | 📉 agota (-0.04) | -15.29$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1326 | 67.4% | +0.174 | ➡️ estable | -22.82$ | 1.74$ | ✅ activa |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T13:45 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 9:30AM-9:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T13:45 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 9:30AM-9:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T13:45 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 13, 9:30AM-9:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T13:34 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 9:15AM-9:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T13:34 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 9:15AM-9:30AM ET… | ❌ LOSS | -1.91$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T13:45 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,514.79 | 0.1min |  |
| ✅ ETH | $1,770.49 | 0.1min |  |
| ✅ SOL | $75.33 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,537.00 | consenso |  |
| ETH | $1,770.49 | consenso |  |
| SOL | $75.64 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*