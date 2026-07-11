# Estado del bot — 2026-07-11 16:03 UTC

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
| P&L fiel (stake fijo 1$) | +973.34 $ |
| P&L sim compuesto | 🟢 +1505.93 $ (ficción Kelly: +5920% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +226.52 $ |
| Operaciones resueltas | 9418 (5279 WIN / 4139 LOSS) — 56.1% |
| Señales abiertas | 170 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3278 | 61.3% | +0.113 | ➡️ estable | +1056.89$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 673 | 64.8% | +0.147 | ➡️ estable | +296.84$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 821 | 57.9% | +0.078 | 📈 madura (+0.05) | +178.67$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 50 | 64.0% | +0.135 | 📈 madura (+0.15) | +14.72$ | 1.35$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 284 | 39.1% | -0.108 | 📈 madura (+0.09) | +8.27$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1272 | 48.7% | -0.013 | ➡️ estable | +3.92$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 7 | 57.1% | +0.019 | — | +0.43$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 135 | 34.1% | -0.157 | 📉 agota (-0.12) | -1.02$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 187 | 59.4% | +0.093 | 📈 madura (+0.26) | -10.28$ | 0.93$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 521 | 65.6% | +0.156 | 📉 agota (-0.04) | -33.08$ | 1.56$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T16:02 | UPDOWN_GBM#BTC#daily | Bitcoin Up or Down on July 11?… | ❌ LOSS | -0.51$ |
| 2026-07-11T16:01 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 11:45AM-12:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T16:01 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 11:45AM-12:00PM ET… | ✅ WIN | +1.32$ |
| 2026-07-11T16:01 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 11:45AM-12:00PM ET… | ❌ LOSS | -1.13$ |
| 2026-07-11T16:01 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 11:45AM-12:00PM ET… | ✅ WIN | +1.13$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T16:02 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,120.18 | 0.1min |  |
| ✅ ETH | $1,813.52 | 0.1min |  |
| ✅ SOL | $78.37 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,126.30 | consenso |  |
| ETH | $1,813.52 | consenso |  |
| SOL | $78.35 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*