# Estado del bot — 2026-07-11 18:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **22.41 $** |
| P&L real total | 🔴 **-3.03 $** |
| P&L real hoy | -2.89 $ |
| P&L real 7 días | +14.43 $ |
| Fees pagados (real) | 7.42 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +964.02 $ |
| P&L sim compuesto | 🟢 +1509.75 $ (ficción Kelly: +5935% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +230.34 $ |
| Operaciones resueltas | 9586 (5365 WIN / 4221 LOSS) — 56.0% |
| Señales abiertas | 179 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3311 | 61.0% | +0.110 | ➡️ estable | +1048.30$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 699 | 64.2% | +0.142 | ➡️ estable | +304.12$ | 1.42$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 854 | 57.4% | +0.074 | 📈 madura (+0.03) | +176.22$ | 0.74$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 52 | 65.4% | +0.148 | 📈 madura (+0.14) | +17.26$ | 1.48$ | ✅ activa |
| GBM_LATE_60M | 289 | 39.1% | -0.108 | 📈 madura (+0.07) | +10.86$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1279 | 48.9% | -0.011 | 📈 madura (+0.03) | +10.41$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 21 | 47.6% | -0.022 | — | -0.72$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 563 | 65.7% | +0.157 | 📉 agota (-0.04) | -33.53$ | 1.57$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T18:20 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 2:00PM-2:15PM ET… | ✅ WIN | +0.91$ |
| 2026-07-11T18:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 2:00PM-2:15PM ET… | ✅ WIN | +1.06$ |
| 2026-07-11T18:18 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 2:10PM-2:15PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T18:17 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 2:00PM-2:15PM ET… | ✅ WIN | +0.55$ |
| 2026-07-11T18:17 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 2:00PM-2:15PM ET… | ✅ WIN | +0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T18:20 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,282.39 | 0.1min |  |
| ✅ ETH | $1,823.96 | 0.1min |  |
| ✅ SOL | $78.20 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,282.39 | consenso |  |
| ETH | $1,823.96 | consenso |  |
| SOL | $78.09 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*