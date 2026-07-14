# Estado del bot — 2026-07-14 13:47 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **7.10 $** |
| P&L real total | 🔴 **-18.34 $** |
| P&L real hoy | -2.93 $ |
| P&L real 7 días | -8.40 $ |
| Fees pagados (real) | 8.21 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1581.57 $ |
| P&L sim compuesto | 🟢 +2734.32 $ (ficción Kelly: +10748% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +180.11 $ |
| Operaciones resueltas | 13852 (8024 WIN / 5828 LOSS) — 57.9% |
| Señales abiertas | 72 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4265 | 60.4% | +0.104 | ➡️ estable | +1341.85$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1568 | 65.4% | +0.154 | ➡️ estable | +939.91$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1502 | 58.3% | +0.083 | ➡️ estable | +411.65$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1470 | 50.6% | +0.006 | 📈 madura (+0.08) | +59.51$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 103 | 59.2% | +0.090 | 📉 agota (-0.10) | +27.83$ | 0.91$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 40 | 72.5% | +0.214 | 📈 madura (+0.05) | +15.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 323 | 38.7% | -0.112 | ➡️ estable | +5.44$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1749 | 68.0% | +0.180 | ➡️ estable | -14.79$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T13:47 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 14, 9:35AM-9:40AM ET… | ❌ LOSS | -1.41$ |
| 2026-07-14T13:47 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 9:35AM-9:40AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T13:45 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 9:30AM-9:45AM ET… | ✅ WIN | +1.53$ |
| 2026-07-14T13:45 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 14, 9:30AM-9:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T13:45 | LEADLAG_BTC_XRP_15M#XRP#15min | XRP Up or Down - July 14, 9:30AM-9:45AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T13:46 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,781.08 | 0.1min |  |
| ✅ ETH | $1,871.17 | 0.1min |  |
| ✅ SOL | $77.12 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,821.90 | consenso |  |
| ETH | $1,871.87 | consenso |  |
| SOL | $77.18 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*