# Estado del bot — 2026-07-14 23:02 UTC

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
| P&L fiel (stake fijo 1$) | +1625.14 $ |
| P&L sim compuesto | 🟢 +2829.41 $ (ficción Kelly: +11122% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +275.20 $ |
| Operaciones resueltas | 14441 (8381 WIN / 6060 LOSS) — 58.0% |
| Señales abiertas | 70 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4392 | 60.3% | +0.103 | 📉 agota (-0.03) | +1350.20$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1678 | 65.4% | +0.154 | ➡️ estable | +988.73$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1619 | 58.1% | +0.081 | ➡️ estable | +429.73$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1503 | 50.8% | +0.008 | 📈 madura (+0.07) | +66.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 107 | 58.9% | +0.087 | 📉 agota (-0.14) | +27.63$ | 0.87$ | ✅ activa |
| STREAK_FADE_15M | 183 | 60.1% | +0.100 | 📈 madura (+0.10) | +20.99$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_PYCONFIRMADO | 5 | 80.0% | +0.054 | — | +2.95$ | 0.54$ | ⏳ acumulando |
| GBM_LATE_5M | 2 | 100.0% | +0.025 | — | +0.96$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 2 | 0.0% | -0.025 | — | -1.02$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1906 | 67.8% | +0.178 | ➡️ estable | -15.29$ | 1.78$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T23:01 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 6:45PM-7:00PM ET… | ✅ WIN | +0.25$ |
| 2026-07-14T23:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 6:45PM-7:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T23:01 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 6:45PM-7:00PM ET… | ✅ WIN | +1.03$ |
| 2026-07-14T23:01 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 14, 6:45PM-7:00PM ET… | ❌ LOSS | -1.22$ |
| 2026-07-14T23:01 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 6:55PM-7:00PM ET… | ✅ WIN | +1.53$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T23:00 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,823.42 | 0.1min |  |
| ✅ ETH | $1,881.30 | 0.1min |  |
| ✅ SOL | $77.69 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,823.42 | consenso |  |
| ETH | $1,881.30 | consenso |  |
| SOL | $77.58 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*