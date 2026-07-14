# Estado del bot — 2026-07-14 18:45 UTC

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
| P&L fiel (stake fijo 1$) | +1583.33 $ |
| P&L sim compuesto | 🟢 +2758.21 $ (ficción Kelly: +10842% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +204.00 $ |
| Operaciones resueltas | 14171 (8205 WIN / 5966 LOSS) — 57.9% |
| Señales abiertas | 81 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4336 | 60.2% | +0.102 | 📉 agota (-0.03) | +1330.39$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1625 | 65.3% | +0.153 | ➡️ estable | +962.40$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1569 | 57.9% | +0.079 | ➡️ estable | +413.88$ | 0.79$ | ✅ activa |
| UPDOWN_GBM | 1484 | 50.8% | +0.008 | 📈 madura (+0.08) | +67.95$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 105 | 59.0% | +0.089 | 📉 agota (-0.12) | +29.19$ | 0.89$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 1830 | 67.8% | +0.178 | ➡️ estable | -21.75$ | 1.78$ | ✅ activa |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T18:36 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 14, 2:30PM-2:35PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T18:36 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 2:30PM-2:35PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T18:36 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 14, 2:15PM-2:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T18:36 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 14, 2:15PM-2:30PM ET… | ✅ WIN | +0.84$ |
| 2026-07-14T18:36 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 14, 2:15PM-2:30PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-14T18:44 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,533.15 | 0.1min |  |
| ✅ ETH | $1,870.77 | 0.1min |  |
| ✅ SOL | $77.16 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,533.15 | consenso |  |
| ETH | $1,870.83 | consenso |  |
| SOL | $77.11 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*