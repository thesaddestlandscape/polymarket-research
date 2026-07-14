# Estado del bot — 2026-07-14 22:50 UTC

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
| P&L fiel (stake fijo 1$) | +1627.48 $ |
| P&L sim compuesto | 🟢 +2833.51 $ (ficción Kelly: +11138% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +279.30 $ |
| Operaciones resueltas | 14432 (8377 WIN / 6055 LOSS) — 58.0% |
| Señales abiertas | 71 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4392 | 60.3% | +0.103 | 📉 agota (-0.03) | +1350.20$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1677 | 65.4% | +0.154 | ➡️ estable | +990.77$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1618 | 58.1% | +0.081 | ➡️ estable | +428.69$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1501 | 50.8% | +0.008 | 📈 madura (+0.07) | +66.85$ | 0.50$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1901 | 67.9% | +0.179 | ➡️ estable | -12.25$ | 1.79$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T22:49 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 6:30PM-6:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T22:49 | GBM_LATE_15M_PYCONFIRMADO#BTC#15min | Bitcoin Up or Down - July 14, 6:30PM-6:45PM ET… | ✅ WIN | +1.45$ |
| 2026-07-14T22:49 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 6:30PM-6:45PM ET… | ❌ LOSS | -1.88$ |
| 2026-07-14T22:49 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 14, 6:30PM-6:45PM ET… | ❌ LOSS | -1.67$ |
| 2026-07-14T22:49 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 6:30PM-6:45PM ET… | ✅ WIN | +2.08$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T22:49 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,880.46 | 0.1min |  |
| ✅ ETH | $1,885.88 | 0.1min |  |
| ✅ SOL | $77.79 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,882.70 | consenso |  |
| ETH | $1,885.88 | consenso |  |
| SOL | $77.78 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*