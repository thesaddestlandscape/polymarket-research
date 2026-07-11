# Estado del bot — 2026-07-11 16:09 UTC

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
| P&L fiel (stake fijo 1$) | +977.21 $ |
| P&L sim compuesto | 🟢 +1511.81 $ (ficción Kelly: +5943% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +232.40 $ |
| Operaciones resueltas | 9431 (5286 WIN / 4145 LOSS) — 56.0% |
| Señales abiertas | 178 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3279 | 61.3% | +0.113 | ➡️ estable | +1058.75$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 674 | 64.8% | +0.148 | ➡️ estable | +298.84$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 822 | 57.9% | +0.079 | 📈 madura (+0.05) | +180.67$ | 0.79$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 524 | 65.6% | +0.156 | 📉 agota (-0.05) | -33.06$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T16:09 | WEEKLY_PRICE#ETH | Will the price of Ethereum be between $1,700 and $… | ❌ LOSS | -0.51$ |
| 2026-07-11T16:07 | PRICE_TARGET_GBM#SOL#atexpiry | Will the price of Solana be above $80 on July 11?… | ✅ WIN | +0.88$ |
| 2026-07-11T16:07 | WEEKLY_PRICE#BTC | Will the price of Bitcoin be between $64,000 and $… | ❌ LOSS | -1.27$ |
| 2026-07-11T16:07 | WEEKLY_PRICE#SOL | Will the price of Solana be between $70 and $80 on… | ❌ LOSS | -0.51$ |
| 2026-07-11T16:06 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 11:45AM-12:00PM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T16:08 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,089.79 | 0.1min |  |
| ✅ ETH | $1,812.87 | 0.1min |  |
| ✅ SOL | $78.18 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,100.00 | consenso |  |
| ETH | $1,813.14 | consenso |  |
| SOL | $78.19 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*