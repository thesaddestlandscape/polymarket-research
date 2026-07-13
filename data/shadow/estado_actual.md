# Estado del bot — 2026-07-13 11:23 UTC

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
| P&L fiel (stake fijo 1$) | +1408.83 $ |
| P&L sim compuesto | 🟢 +2368.07 $ (ficción Kelly: +9308% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +154.60 $ |
| Operaciones resueltas | 12349 (7092 WIN / 5257 LOSS) — 57.4% |
| Señales abiertas | 119 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3913 | 60.9% | +0.109 | ➡️ estable | +1277.53$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1238 | 65.6% | +0.156 | ➡️ estable | +720.67$ | 1.56$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1317 | 58.2% | +0.082 | ➡️ estable | +341.72$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1384 | 50.1% | +0.001 | 📈 madura (+0.08) | +50.45$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| STREAK_FADE_15M | 167 | 61.7% | +0.115 | 📈 madura (+0.22) | +24.85$ | 1.15$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| FAVORITO_CONFIRMADO | 1291 | 67.6% | +0.176 | ➡️ estable | -15.59$ | 1.76$ | ✅ activa |
| STREAK_FADE_5M | 210 | 45.7% | -0.042 | 📉 agota (-0.06) | -17.80$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T11:19 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 7:00AM-7:15AM ET… | ✅ WIN | +1.27$ |
| 2026-07-13T11:19 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 13, 7:00AM-7:15AM ET… | ✅ WIN | +0.51$ |
| 2026-07-13T11:19 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 13, 7:00AM-7:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T11:19 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 13, 7:00AM-7:15AM ET… | ❌ LOSS | -1.31$ |
| 2026-07-13T11:19 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 7:00AM-7:15AM ET… | ✅ WIN | +1.27$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T11:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,945.58 | 0.1min |  |
| ✅ ETH | $1,778.85 | 0.1min |  |
| ✅ SOL | $76.48 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,959.60 | consenso |  |
| ETH | $1,778.85 | consenso |  |
| SOL | $76.31 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*