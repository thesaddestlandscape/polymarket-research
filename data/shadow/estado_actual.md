# Estado del bot — 2026-07-11 15:50 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.09 $** |
| P&L real total | 🔴 **-4.35 $** |
| P&L real hoy | -4.22 $ |
| P&L real 7 días | +13.10 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +973.68 $ |
| P&L sim compuesto | 🟢 +1510.84 $ (ficción Kelly: +5939% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +231.43 $ |
| Operaciones resueltas | 9382 (5261 WIN / 4121 LOSS) — 56.1% |
| Señales abiertas | 186 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3275 | 61.3% | +0.113 | ➡️ estable | +1059.52$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 671 | 65.0% | +0.149 | ➡️ estable | +298.26$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 818 | 57.8% | +0.078 | 📈 madura (+0.05) | +176.72$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 50 | 64.0% | +0.135 | 📈 madura (+0.15) | +14.72$ | 1.35$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 283 | 38.9% | -0.111 | 📈 madura (+0.09) | +6.08$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1270 | 48.7% | -0.013 | 📈 madura (+0.03) | +4.94$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 3 | 33.3% | -0.015 | — | -0.53$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 513 | 66.5% | +0.164 | ➡️ estable | -25.61$ | 1.64$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T15:50 | STREAK_FADE_5M#SOL#5min | Solana Up or Down - July 11, 11:40AM-11:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T15:46 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 11:30AM-11:45AM ET… | ✅ WIN | +0.09$ |
| 2026-07-11T15:46 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 11:30AM-11:45AM ET… | ✅ WIN | +0.06$ |
| 2026-07-11T15:46 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 11, 11:30AM-11:45AM ET… | ✅ WIN | +0.06$ |
| 2026-07-11T15:46 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 11:40AM-11:45AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T15:49 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,992.36 | 0.1min |  |
| ✅ ETH | $1,808.84 | 0.1min |  |
| ✅ SOL | $78.08 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,992.36 | consenso |  |
| ETH | $1,808.85 | consenso |  |
| SOL | $78.03 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*