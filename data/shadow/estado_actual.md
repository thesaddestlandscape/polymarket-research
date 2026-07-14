# Estado del bot — 2026-07-14 20:12 UTC

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
| P&L fiel (stake fijo 1$) | +1586.97 $ |
| P&L sim compuesto | 🟢 +2765.81 $ (ficción Kelly: +10872% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +211.60 $ |
| Operaciones resueltas | 14271 (8263 WIN / 6008 LOSS) — 57.9% |
| Señales abiertas | 81 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4355 | 60.2% | +0.102 | 📉 agota (-0.03) | +1337.91$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1645 | 65.3% | +0.153 | ➡️ estable | +968.73$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1588 | 58.0% | +0.080 | ➡️ estable | +423.22$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1491 | 50.8% | +0.008 | 📈 madura (+0.07) | +65.62$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 106 | 58.5% | +0.083 | 📉 agota (-0.15) | +27.15$ | 0.83$ | ✅ activa |
| STREAK_FADE_15M | 182 | 59.9% | +0.098 | 📈 madura (+0.10) | +19.07$ | 0.98$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 1860 | 67.6% | +0.176 | ➡️ estable | -33.63$ | 1.75$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T20:07 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 3:45PM-4:00PM ET… | ✅ WIN | +0.54$ |
| 2026-07-14T20:07 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 14, 3:45PM-4:00PM ET… | ✅ WIN | +0.51$ |
| 2026-07-14T20:07 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 3:45PM-4:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-14T20:07 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 3:45PM-4:00PM ET… | ✅ WIN | +1.35$ |
| 2026-07-14T20:07 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 3:45PM-4:00PM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T20:11 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,445.14 | 0.1min |  |
| ✅ ETH | $1,875.16 | 0.1min |  |
| ✅ SOL | $77.04 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,445.14 | consenso |  |
| ETH | $1,875.16 | consenso |  |
| SOL | $77.02 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*