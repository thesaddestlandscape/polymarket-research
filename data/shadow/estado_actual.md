# Estado del bot — 2026-07-13 08:51 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **13.33 $** |
| P&L real total | 🔴 **-12.11 $** |
| P&L real hoy | -1.10 $ |
| P&L real 7 días | +4.47 $ |
| Fees pagados (real) | 7.82 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1399.95 $ |
| P&L sim compuesto | 🟢 +2341.87 $ (ficción Kelly: +9205% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +128.40 $ |
| Operaciones resueltas | 12196 (7002 WIN / 5194 LOSS) — 57.4% |
| Señales abiertas | 125 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3875 | 61.0% | +0.110 | ➡️ estable | +1269.98$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1202 | 65.9% | +0.159 | ➡️ estable | +709.96$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1297 | 57.9% | +0.079 | ➡️ estable | +329.92$ | 0.79$ | ✅ activa |
| UPDOWN_GBM | 1381 | 50.0% | +0.000 | 📈 madura (+0.07) | +47.59$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 165 | 62.4% | +0.123 | 📈 madura (+0.24) | +28.93$ | 1.23$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 200 | 46.5% | -0.035 | ➡️ estable | -14.52$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1247 | 67.6% | +0.176 | ➡️ estable | -16.23$ | 1.75$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T08:47 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 4:30AM-4:45AM ET… | ✅ WIN | +3.76$ |
| 2026-07-13T08:47 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 13, 4:30AM-4:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T08:47 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 13, 4:30AM-4:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T08:47 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 4:30AM-4:45AM ET… | ✅ WIN | +1.56$ |
| 2026-07-13T08:47 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 13, 4:30AM-4:45AM ET… | ❌ LOSS | -1.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T08:50 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,090.41 | 0.1min |  |
| ✅ ETH | $1,789.63 | 0.1min |  |
| ✅ SOL | $76.73 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,098.90 | consenso |  |
| ETH | $1,789.63 | consenso |  |
| SOL | $76.62 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*