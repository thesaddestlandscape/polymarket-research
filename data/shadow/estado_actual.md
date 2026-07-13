# Estado del bot — 2026-07-13 17:55 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **10.03 $** |
| P&L real total | 🔴 **-15.41 $** |
| P&L real hoy | -4.41 $ |
| P&L real 7 días | +1.17 $ |
| Fees pagados (real) | 7.98 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1479.87 $ |
| P&L sim compuesto | 🟢 +2499.63 $ (ficción Kelly: +9826% s/ operativo) |
| P&L sim hoy (2026-07-13) | 🟢 +286.16 $ |
| Operaciones resueltas | 12774 (7367 WIN / 5407 LOSS) — 57.7% |
| Señales abiertas | 127 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4004 | 60.9% | +0.109 | ➡️ estable | +1299.37$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1328 | 65.7% | +0.157 | ➡️ estable | +774.96$ | 1.57$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1366 | 58.6% | +0.086 | ➡️ estable | +383.43$ | 0.86$ | ✅ activa |
| UPDOWN_GBM | 1411 | 50.4% | +0.004 | 📈 madura (+0.08) | +57.19$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 86 | 62.8% | +0.125 | 📉 agota (-0.04) | +29.77$ | 1.25$ | ✅ activa |
| STREAK_FADE_15M | 173 | 60.7% | +0.106 | 📈 madura (+0.16) | +20.86$ | 1.06$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1400 | 67.5% | +0.175 | ➡️ estable | -19.60$ | 1.74$ | ✅ activa |
| STREAK_FADE_5M | 239 | 46.4% | -0.035 | 📉 agota (-0.04) | -20.37$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-13T17:54 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 1:45PM-1:50PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T17:52 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 13, 1:45PM-1:50PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T17:50 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 13, 1:40PM-1:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-13T17:48 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 13, 1:30PM-1:45PM ET… | ✅ WIN | +0.10$ |
| 2026-07-13T17:48 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 13, 1:30PM-1:45PM ET… | ✅ WIN | +2.08$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-13T17:54 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $61,951.08 | 0.1min |  |
| ✅ ETH | $1,763.32 | 0.1min |  |
| ✅ SOL | $74.82 | 0.1min |  |
| ✅ XRP | $1.06 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $61,963.90 | consenso |  |
| ETH | $1,764.05 | consenso |  |
| SOL | $74.87 | consenso |  |
| XRP | $1.06 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*