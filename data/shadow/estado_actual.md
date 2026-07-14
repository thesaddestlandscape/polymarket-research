# Estado del bot — 2026-07-14 14:10 UTC

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
| P&L fiel (stake fijo 1$) | +1571.16 $ |
| P&L sim compuesto | 🟢 +2720.88 $ (ficción Kelly: +10695% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +166.67 $ |
| Operaciones resueltas | 13879 (8034 WIN / 5845 LOSS) — 57.9% |
| Señales abiertas | 78 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4271 | 60.4% | +0.104 | ➡️ estable | +1335.64$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1572 | 65.3% | +0.153 | ➡️ estable | +937.45$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1508 | 58.2% | +0.082 | ➡️ estable | +408.81$ | 0.82$ | ✅ activa |
| UPDOWN_GBM | 1471 | 50.6% | +0.006 | 📈 madura (+0.08) | +60.90$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 103 | 59.2% | +0.090 | 📉 agota (-0.10) | +27.83$ | 0.91$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 40 | 72.5% | +0.214 | 📈 madura (+0.05) | +15.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 324 | 38.6% | -0.113 | ➡️ estable | +4.84$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 143 | 34.3% | -0.155 | 📉 agota (-0.13) | -1.21$ | 0.50$ | ⚠️ IC negativo |
| WEEKLY_PRICE | 219 | 59.4% | +0.093 | 📈 madura (+0.26) | -1.22$ | 0.93$ | ✅ activa |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1758 | 67.9% | +0.179 | ➡️ estable | -17.50$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T14:06 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 14, 9AM ET… | ❌ LOSS | -0.60$ |
| 2026-07-14T14:06 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 14, 9AM ET… | ❌ LOSS | -1.19$ |
| 2026-07-14T14:06 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 14, 9AM ET… | ✅ WIN | +1.44$ |
| 2026-07-14T14:04 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 9:45AM-10:00AM ET… | ❌ LOSS | -1.29$ |
| 2026-07-14T14:04 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 14, 9:45AM-10:00AM ET… | ❌ LOSS | -1.34$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T14:09 UTC | rechazos 1h: 6 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,663.96 | 0.1min |  |
| ✅ ETH | $1,863.32 | 0.1min |  |
| ✅ SOL | $76.80 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,673.60 | consenso |  |
| ETH | $1,863.32 | consenso |  |
| SOL | $76.75 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:6 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*