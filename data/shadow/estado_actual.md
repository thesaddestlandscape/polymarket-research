# Estado del bot — 2026-07-14 13:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **8.21 $** |
| P&L real total | 🔴 **-17.23 $** |
| P&L real hoy | -1.81 $ |
| P&L real 7 días | -7.29 $ |
| Fees pagados (real) | 8.15 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1577.43 $ |
| P&L sim compuesto | 🟢 +2724.41 $ (ficción Kelly: +10709% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +170.20 $ |
| Operaciones resueltas | 13814 (8000 WIN / 5814 LOSS) — 57.9% |
| Señales abiertas | 61 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4258 | 60.4% | +0.104 | ➡️ estable | +1337.12$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1561 | 65.5% | +0.155 | ➡️ estable | +941.27$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1493 | 58.3% | +0.083 | ➡️ estable | +407.79$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1469 | 50.6% | +0.006 | 📈 madura (+0.08) | +58.18$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 100 | 60.0% | +0.098 | 📉 agota (-0.08) | +28.31$ | 0.98$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 39 | 71.8% | +0.207 | 📈 madura (+0.06) | +13.83$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1739 | 68.0% | +0.179 | ➡️ estable | -15.21$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T13:01 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 8:55AM-9:00AM ET… | ✅ WIN | +0.40$ |
| 2026-07-14T13:01 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 14, 8:55AM-9:00AM ET… | ✅ WIN | +0.80$ |
| 2026-07-14T13:01 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 8:45AM-9:00AM ET… | ✅ WIN | +0.17$ |
| 2026-07-14T13:01 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 8:50AM-8:55AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T13:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 8:45AM-9:00AM ET… | ✅ WIN | +1.40$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T13:01 UTC | rechazos 1h: 8 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,841.96 | 0.1min |  |
| ✅ ETH | $1,851.31 | 0.1min |  |
| ✅ SOL | $76.78 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,842.10 | consenso |  |
| ETH | $1,851.56 | consenso |  |
| SOL | $76.64 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:8 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*