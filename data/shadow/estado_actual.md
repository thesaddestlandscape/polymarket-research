# Estado del bot — 2026-07-14 20:00 UTC

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
| P&L fiel (stake fijo 1$) | +1593.08 $ |
| P&L sim compuesto | 🟢 +2778.07 $ (ficción Kelly: +10920% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +223.86 $ |
| Operaciones resueltas | 14248 (8253 WIN / 5995 LOSS) — 57.9% |
| Señales abiertas | 84 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4352 | 60.2% | +0.102 | 📉 agota (-0.03) | +1339.14$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1641 | 65.4% | +0.154 | ➡️ estable | +972.81$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1584 | 58.1% | +0.081 | ➡️ estable | +426.73$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1489 | 50.8% | +0.008 | 📈 madura (+0.07) | +66.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 106 | 58.5% | +0.083 | 📉 agota (-0.15) | +27.15$ | 0.83$ | ✅ activa |
| STREAK_FADE_15M | 181 | 59.7% | +0.096 | 📈 madura (+0.10) | +18.59$ | 0.96$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1851 | 67.6% | +0.176 | ➡️ estable | -30.89$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T19:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 3:30PM-3:45PM ET… | ✅ WIN | +0.76$ |
| 2026-07-14T19:51 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 14, 3:30PM-3:45PM ET… | ✅ WIN | +0.76$ |
| 2026-07-14T19:51 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 3:30PM-3:45PM ET… | ✅ WIN | +0.22$ |
| 2026-07-14T19:51 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 3:30PM-3:45PM ET… | ✅ WIN | +0.60$ |
| 2026-07-14T19:47 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 3:30PM-3:45PM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T19:59 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,578.10 | 0.1min |  |
| ✅ ETH | $1,877.11 | 0.1min |  |
| ✅ SOL | $77.19 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,578.10 | consenso |  |
| ETH | $1,877.41 | consenso |  |
| SOL | $77.12 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*