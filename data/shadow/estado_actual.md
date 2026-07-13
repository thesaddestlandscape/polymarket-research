# Estado del bot — 2026-07-13 10:02 UTC

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
| P&L fiel (stake fijo 1$) | +1411.76 $ |
| P&L sim compuesto | 🟢 +2367.22 $ (ficción Kelly: +9305% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +153.75 $ |
| Operaciones resueltas | 12264 (7049 WIN / 5215 LOSS) — 57.5% |
| Señales abiertas | 117 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3892 | 61.0% | +0.110 | ➡️ estable | +1278.98$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1217 | 65.7% | +0.157 | ➡️ estable | +711.72$ | 1.57$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1306 | 58.0% | +0.080 | ➡️ estable | +332.81$ | 0.80$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1269 | 67.8% | +0.178 | ➡️ estable | -8.08$ | 1.78$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 202 | 46.5% | -0.034 | ➡️ estable | -13.83$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T10:01 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 5:55AM-6:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T10:01 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 13, 5AM ET… | ✅ WIN | +0.55$ |
| 2026-07-13T10:01 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 13, 5AM ET… | ✅ WIN | +1.14$ |
| 2026-07-13T10:01 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 13, 5AM ET… | ✅ WIN | +1.32$ |
| 2026-07-13T09:52 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 5:30AM-5:45AM ET… | ✅ WIN | +0.97$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T10:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,039.00 | 0.1min |  |
| ✅ ETH | $1,784.19 | 0.1min |  |
| ✅ SOL | $76.63 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,039.40 | consenso |  |
| ETH | $1,784.58 | consenso |  |
| SOL | $76.56 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*