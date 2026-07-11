# Estado del bot — 2026-07-11 16:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.08 $** |
| P&L real total | 🔴 **-4.36 $** |
| P&L real hoy | -4.22 $ |
| P&L real 7 días | +13.10 $ |
| Fees pagados (real) | 7.36 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +976.28 $ |
| P&L sim compuesto | 🟢 +1509.57 $ (ficción Kelly: +5934% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +230.17 $ |
| Operaciones resueltas | 9435 (5288 WIN / 4147 LOSS) — 56.0% |
| Señales abiertas | 182 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3280 | 61.3% | +0.112 | ➡️ estable | +1057.28$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 675 | 64.7% | +0.147 | ➡️ estable | +297.43$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 823 | 58.0% | +0.079 | 📈 madura (+0.05) | +181.17$ | 0.79$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 50 | 64.0% | +0.135 | 📈 madura (+0.15) | +14.72$ | 1.35$ | ✅ activa |
| GBM_LATE_60M | 285 | 39.3% | -0.106 | 📈 madura (+0.09) | +10.70$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| UPDOWN_GBM | 1272 | 48.7% | -0.013 | ➡️ estable | +3.92$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 7 | 57.1% | +0.019 | — | +0.43$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 525 | 65.7% | +0.157 | 📉 agota (-0.04) | -32.91$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T16:15 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 12:00PM-12:15PM ET… | ❌ LOSS | -1.41$ |
| 2026-07-11T16:15 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 12:00PM-12:15PM ET… | ✅ WIN | +0.15$ |
| 2026-07-11T16:15 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 12:00PM-12:15PM ET… | ✅ WIN | +0.50$ |
| 2026-07-11T16:15 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 11, 12:00PM-12:15PM ET… | ❌ LOSS | -1.48$ |
| 2026-07-11T16:09 | WEEKLY_PRICE#ETH | Will the price of Ethereum be between $1,700 and $… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T16:15 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,072.82 | 0.1min |  |
| ✅ ETH | $1,810.12 | 0.1min |  |
| ✅ SOL | $78.31 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,078.90 | consenso |  |
| ETH | $1,810.49 | consenso |  |
| SOL | $78.12 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*