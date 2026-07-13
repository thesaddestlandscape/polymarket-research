# Estado del bot — 2026-07-13 07:02 UTC

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
| P&L fiel (stake fijo 1$) | +1408.76 $ |
| P&L sim compuesto | 🟢 +2348.12 $ (ficción Kelly: +9230% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +134.65 $ |
| Operaciones resueltas | 12086 (6951 WIN / 5135 LOSS) — 57.5% |
| Señales abiertas | 108 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3849 | 61.2% | +0.112 | ➡️ estable | +1281.33$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1181 | 66.1% | +0.161 | ➡️ estable | +701.17$ | 1.61$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1282 | 58.0% | +0.080 | ➡️ estable | +327.18$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1372 | 49.8% | -0.002 | 📈 madura (+0.07) | +33.07$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_15M | 163 | 62.6% | +0.124 | 📈 madura (+0.23) | +29.22$ | 1.24$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 322 | 38.8% | -0.111 | ➡️ estable | +6.13$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1215 | 68.3% | +0.183 | 📈 madura (+0.04) | +3.64$ | 1.83$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 196 | 46.4% | -0.035 | ➡️ estable | -14.42$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T07:02 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 13, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T07:02 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 13, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T07:00 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T07:00 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T07:00 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 13, 2:45AM-3:00AM ET… | ❌ LOSS | -0.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T07:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,736.43 | 0.1min |  |
| ✅ ETH | $1,776.28 | 0.1min |  |
| ✅ SOL | $76.23 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,745.40 | consenso |  |
| ETH | $1,776.49 | consenso |  |
| SOL | $76.30 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*