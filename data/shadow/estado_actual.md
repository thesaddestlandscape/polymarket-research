# Estado del bot — 2026-07-13 09:02 UTC

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
| P&L fiel (stake fijo 1$) | +1404.59 $ |
| P&L sim compuesto | 🟢 +2352.06 $ (ficción Kelly: +9246% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +138.59 $ |
| Operaciones resueltas | 12219 (7018 WIN / 5201 LOSS) — 57.4% |
| Señales abiertas | 105 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3880 | 61.0% | +0.110 | ➡️ estable | +1271.68$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1206 | 65.9% | +0.159 | ➡️ estable | +713.77$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1302 | 57.9% | +0.079 | ➡️ estable | +328.84$ | 0.79$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1253 | 67.7% | +0.176 | ➡️ estable | -13.34$ | 1.76$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 200 | 46.5% | -0.035 | ➡️ estable | -14.52$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T09:02 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 13, 4:45AM-5:00AM ET… | ✅ WIN | +0.26$ |
| 2026-07-13T09:02 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 13, 4:45AM-5:00AM ET… | ✅ WIN | +1.77$ |
| 2026-07-13T09:02 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 13, 4:45AM-5:00AM ET… | ✅ WIN | +1.33$ |
| 2026-07-13T09:02 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 13, 4:45AM-5:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-13T09:02 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 4:45AM-5:00AM ET… | ✅ WIN | +1.38$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T09:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,134.50 | 0.1min |  |
| ✅ ETH | $1,788.29 | 0.1min |  |
| ✅ SOL | $76.71 | 0.1min |  |
| ✅ XRP | $1.08 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,141.70 | consenso |  |
| ETH | $1,788.29 | consenso |  |
| SOL | $76.67 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*