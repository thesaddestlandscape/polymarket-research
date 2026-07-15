# Estado del bot — 2026-07-15 08:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **5.99 $** |
| P&L real total | 🔴 **-19.45 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -17.49 $ |
| Fees pagados (real) | 8.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1650.21 $ |
| P&L sim compuesto | 🟢 +2912.41 $ (ficción Kelly: +11448% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +103.77 $ |
| Operaciones resueltas | 15028 (8720 WIN / 6308 LOSS) — 58.0% |
| Señales abiertas | 60 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4513 | 60.1% | +0.101 | ➡️ estable | +1371.56$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1779 | 65.0% | +0.150 | ➡️ estable | +1021.55$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1730 | 58.2% | +0.082 | ➡️ estable | +469.84$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1541 | 50.9% | +0.009 | 📈 madura (+0.08) | +70.31$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 114 | 59.6% | +0.095 | 📉 agota (-0.07) | +30.83$ | 0.95$ | ✅ activa |
| STREAK_FADE_15M | 191 | 59.7% | +0.096 | 📈 madura (+0.08) | +20.86$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1604 | 51.2% | +0.012 | ➡️ estable | +12.52$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 10 | 50.0% | +0.000 | — | -0.11$ | 0.50$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 7 | 14.3% | -0.097 | — | -1.75$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_PYCONFIRMADO | 25 | 32.0% | -0.167 | — | -2.56$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2063 | 67.8% | +0.178 | ➡️ estable | -24.58$ | 1.78$ | ✅ activa |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T08:04 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 15, 3:45AM-4:00AM ET… | ✅ WIN | +1.32$ |
| 2026-07-15T08:04 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 15, 3:45AM-4:00AM ET… | ✅ WIN | +1.32$ |
| 2026-07-15T08:04 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 15, 3:45AM-4:00AM ET… | ✅ WIN | +0.75$ |
| 2026-07-15T08:04 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 15, 3:45AM-4:00AM ET… | ✅ WIN | +0.97$ |
| 2026-07-15T08:04 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 15, 3:45AM-4:00AM ET… | ✅ WIN | +0.64$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T08:13 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,535.29 | 0.1min |  |
| ✅ ETH | $1,872.52 | 0.1min |  |
| ✅ SOL | $77.45 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,537.00 | consenso |  |
| ETH | $1,872.52 | consenso |  |
| SOL | $77.35 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*