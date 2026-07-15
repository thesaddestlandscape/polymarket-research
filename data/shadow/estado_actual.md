# Estado del bot — 2026-07-15 07:45 UTC

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
| P&L fiel (stake fijo 1$) | +1654.33 $ |
| P&L sim compuesto | 🟢 +2917.04 $ (ficción Kelly: +11466% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +108.40 $ |
| Operaciones resueltas | 14994 (8702 WIN / 6292 LOSS) — 58.0% |
| Señales abiertas | 66 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4506 | 60.2% | +0.102 | ➡️ estable | +1376.49$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1773 | 65.1% | +0.151 | ➡️ estable | +1025.89$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1723 | 58.3% | +0.083 | ➡️ estable | +472.24$ | 0.83$ | ✅ activa |
| UPDOWN_GBM | 1539 | 50.9% | +0.009 | 📈 madura (+0.08) | +73.05$ | 0.50$ | ✅ activa |
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
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 2051 | 67.7% | +0.177 | ➡️ estable | -34.36$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T07:30 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 15, 3:15AM-3:30AM ET… | ✅ WIN | +2.00$ |
| 2026-07-15T07:30 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 15, 3:15AM-3:30AM ET… | ✅ WIN | +0.50$ |
| 2026-07-15T07:30 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 15, 3:15AM-3:30AM ET… | ✅ WIN | +0.44$ |
| 2026-07-15T07:30 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 15, 3:15AM-3:30AM ET… | ✅ WIN | +1.21$ |
| 2026-07-15T07:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 15, 3:15AM-3:30AM ET… | ✅ WIN | +1.21$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T07:44 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,578.17 | 0.1min |  |
| ✅ ETH | $1,868.46 | 0.1min |  |
| ✅ SOL | $77.57 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,590.90 | consenso |  |
| ETH | $1,868.46 | consenso |  |
| SOL | $77.56 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*