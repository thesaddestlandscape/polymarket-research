# Estado del bot — 2026-07-13 10:12 UTC

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
| P&L fiel (stake fijo 1$) | +1416.68 $ |
| P&L sim compuesto | 🟢 +2381.07 $ (ficción Kelly: +9360% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +167.60 $ |
| Operaciones resueltas | 12279 (7060 WIN / 5219 LOSS) — 57.5% |
| Señales abiertas | 121 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3895 | 61.0% | +0.110 | ➡️ estable | +1284.41$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1220 | 65.8% | +0.158 | ➡️ estable | +717.54$ | 1.58$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1308 | 58.1% | +0.081 | ➡️ estable | +335.29$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1384 | 50.1% | +0.001 | 📈 madura (+0.08) | +50.45$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 165 | 62.4% | +0.123 | 📈 madura (+0.24) | +28.93$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1272 | 67.9% | +0.179 | ➡️ estable | -4.91$ | 1.79$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 206 | 45.6% | -0.043 | 📉 agota (-0.04) | -16.89$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T10:12 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 13, 6:05AM-6:10AM ET… | ❌ LOSS | -1.53$ |
| 2026-07-13T10:12 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 6:05AM-6:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T10:08 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 6:00AM-6:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T10:08 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 5:45AM-6:00AM ET… | ✅ WIN | +1.44$ |
| 2026-07-13T10:06 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 13, 6:00AM-6:05AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T10:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,016.64 | 0.1min |  |
| ✅ ETH | $1,780.21 | 0.1min |  |
| ✅ SOL | $76.27 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,021.00 | consenso |  |
| ETH | $1,780.34 | consenso |  |
| SOL | $76.21 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*