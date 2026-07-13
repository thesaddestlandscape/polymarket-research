# Estado del bot — 2026-07-13 10:23 UTC

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
| P&L fiel (stake fijo 1$) | +1424.64 $ |
| P&L sim compuesto | 🟢 +2395.37 $ (ficción Kelly: +9416% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +181.90 $ |
| Operaciones resueltas | 12296 (7072 WIN / 5224 LOSS) — 57.5% |
| Señales abiertas | 115 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3899 | 61.0% | +0.110 | ➡️ estable | +1288.68$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1224 | 65.9% | +0.159 | ➡️ estable | +728.44$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1311 | 58.2% | +0.082 | ➡️ estable | +339.40$ | 0.82$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1274 | 67.8% | +0.178 | ➡️ estable | -8.99$ | 1.78$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 210 | 45.7% | -0.042 | 📉 agota (-0.06) | -17.80$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T10:22 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 6:15AM-6:20AM ET… | ✅ WIN | +0.48$ |
| 2026-07-13T10:22 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 13, 6:15AM-6:20AM ET… | ✅ WIN | +0.48$ |
| 2026-07-13T10:22 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 6:10AM-6:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T10:17 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 6:00AM-6:15AM ET… | ✅ WIN | +2.00$ |
| 2026-07-13T10:17 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 13, 6:10AM-6:15AM ET… | ❌ LOSS | -1.36$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T10:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,023.93 | 0.1min |  |
| ✅ ETH | $1,780.90 | 0.1min |  |
| ✅ SOL | $76.37 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,023.93 | consenso |  |
| ETH | $1,781.56 | consenso |  |
| SOL | $76.16 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*