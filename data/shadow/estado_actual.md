# Estado del bot — 2026-07-15 04:29 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **6.02 $** |
| P&L real total | 🔴 **-19.42 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -17.49 $ |
| Fees pagados (real) | 8.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1636.72 $ |
| P&L sim compuesto | 🟢 +2882.99 $ (ficción Kelly: +11332% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +74.34 $ |
| Operaciones resueltas | 14796 (8592 WIN / 6204 LOSS) — 58.1% |
| Señales abiertas | 62 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4465 | 60.2% | +0.102 | ➡️ estable | +1370.44$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1741 | 65.2% | +0.152 | ➡️ estable | +1013.36$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1682 | 58.3% | +0.083 | ➡️ estable | +447.41$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1530 | 50.8% | +0.008 | 📈 madura (+0.08) | +64.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 112 | 59.8% | +0.096 | 📉 agota (-0.09) | +30.74$ | 0.97$ | ✅ activa |
| STREAK_FADE_15M | 187 | 59.9% | +0.098 | 📈 madura (+0.08) | +21.10$ | 0.98$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1604 | 51.2% | +0.012 | ➡️ estable | +12.52$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 5 | 40.0% | -0.018 | — | -0.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 4 | 0.0% | -0.067 | — | -2.04$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_PYCONFIRMADO | 18 | 33.3% | -0.135 | — | -2.44$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1997 | 68.0% | +0.179 | ➡️ estable | -16.29$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T04:22 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 15, 12:00AM-12:15AM ET… | ❌ LOSS | -1.30$ |
| 2026-07-15T04:22 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 15, 12:00AM-12:15AM ET… | ❌ LOSS | -1.16$ |
| 2026-07-15T04:22 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 15, 12:00AM-12:15AM ET… | ✅ WIN | +1.44$ |
| 2026-07-15T04:22 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 15, 12:00AM-12:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-15T04:22 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 15, 12:00AM-12:15AM ET… | ❌ LOSS | -1.30$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T04:28 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,752.00 | 0.1min |  |
| ✅ ETH | $1,876.14 | 0.1min |  |
| ✅ SOL | $77.69 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,752.00 | consenso |  |
| ETH | $1,876.14 | consenso |  |
| SOL | $77.67 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*