# Estado del bot — 2026-07-13 12:39 UTC

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
| P&L fiel (stake fijo 1$) | +1430.21 $ |
| P&L sim compuesto | 🟢 +2399.93 $ (ficción Kelly: +9434% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +186.46 $ |
| Operaciones resueltas | 12431 (7148 WIN / 5283 LOSS) — 57.5% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3933 | 60.9% | +0.109 | ➡️ estable | +1287.43$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1255 | 65.7% | +0.157 | ➡️ estable | +738.64$ | 1.57$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1328 | 58.3% | +0.083 | ➡️ estable | +347.76$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1391 | 50.2% | +0.002 | 📈 madura (+0.08) | +51.81$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 80 | 63.7% | +0.134 | 📉 agota (-0.07) | +26.87$ | 1.34$ | ✅ activa |
| STREAK_FADE_15M | 168 | 61.3% | +0.112 | 📈 madura (+0.20) | +23.17$ | 1.12$ | ✅ activa |
| ORDER_FLOW_5M | 1591 | 51.2% | +0.012 | ➡️ estable | +13.79$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 38 | 71.1% | +0.200 | 📈 madura (+0.05) | +12.03$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 140 | 34.3% | -0.155 | 📉 agota (-0.14) | -0.83$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| STREAK_FADE_5M | 216 | 46.8% | -0.032 | 📉 agota (-0.05) | -15.23$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1311 | 67.5% | +0.175 | ➡️ estable | -19.89$ | 1.74$ | ✅ activa |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T12:35 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 8:15AM-8:30AM ET… | ✅ WIN | +2.90$ |
| 2026-07-13T12:35 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 13, 8:15AM-8:30AM ET… | ✅ WIN | +2.38$ |
| 2026-07-13T12:35 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 13, 8:15AM-8:30AM ET… | ✅ WIN | +2.36$ |
| 2026-07-13T12:35 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 13, 8:15AM-8:30AM ET… | ✅ WIN | +2.00$ |
| 2026-07-13T12:35 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 13, 8:15AM-8:30AM ET… | ❌ LOSS | -1.53$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T12:38 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $62,567.62 | 0.1min |  |
| ✅ ETH | $1,768.64 | 0.1min |  |
| ✅ SOL | $75.78 | 0.1min |  |
| ✅ XRP | $1.07 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $62,568.10 | consenso |  |
| ETH | $1,768.64 | consenso |  |
| SOL | $75.70 | consenso |  |
| XRP | $1.07 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*