# Estado del bot — 2026-07-14 16:10 UTC

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
| P&L fiel (stake fijo 1$) | +1572.97 $ |
| P&L sim compuesto | 🟢 +2737.69 $ (ficción Kelly: +10761% s/ operativo) |
| P&L sim hoy (2026-07-14) | 🟢 +183.48 $ |
| Operaciones resueltas | 14027 (8120 WIN / 5907 LOSS) — 57.9% |
| Señales abiertas | 80 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4300 | 60.2% | +0.102 | ➡️ estable | +1322.47$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1596 | 65.4% | +0.154 | ➡️ estable | +952.22$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1536 | 58.0% | +0.080 | ➡️ estable | +409.55$ | 0.80$ | ✅ activa |
| UPDOWN_GBM | 1478 | 50.8% | +0.008 | 📈 madura (+0.08) | +68.47$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 105 | 59.0% | +0.089 | 📉 agota (-0.12) | +29.19$ | 0.89$ | ✅ activa |
| STREAK_FADE_15M | 178 | 60.1% | +0.100 | 📈 madura (+0.12) | +18.42$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1593 | 51.2% | +0.012 | ➡️ estable | +13.78$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| GBM_LATE_60M | 324 | 38.6% | -0.113 | ➡️ estable | +4.84$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1792 | 67.8% | +0.178 | ➡️ estable | -21.39$ | 1.78$ | ✅ activa |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-14T16:07 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 14, 11AM ET… | ❌ LOSS | -1.74$ |
| 2026-07-14T16:06 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-14T16:06 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -1.39$ |
| 2026-07-14T16:06 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 14, 11:45AM-12:00PM ET… | ❌ LOSS | -1.14$ |
| 2026-07-14T16:06 | WEEKLY_PRICE#ETH | Will the price of Ethereum be between $1,800 and $… | ❌ LOSS | -1.27$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-14T16:09 UTC | rechazos 1h: 7 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,786.40 | 0.1min |  |
| ✅ ETH | $1,874.15 | 0.1min |  |
| ✅ SOL | $77.46 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,790.90 | consenso |  |
| ETH | $1,874.39 | consenso |  |
| SOL | $77.34 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:7 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*