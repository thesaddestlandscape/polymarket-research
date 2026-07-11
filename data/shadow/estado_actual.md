# Estado del bot — 2026-07-11 18:03 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **22.42 $** |
| P&L real total | 🔴 **-3.02 $** |
| P&L real hoy | -2.89 $ |
| P&L real 7 días | +14.43 $ |
| Fees pagados (real) | 7.42 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +963.61 $ |
| P&L sim compuesto | 🟢 +1507.83 $ (ficción Kelly: +5927% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +228.42 $ |
| Operaciones resueltas | 9574 (5358 WIN / 4216 LOSS) — 56.0% |
| Señales abiertas | 170 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3310 | 61.0% | +0.110 | ➡️ estable | +1046.76$ | 1.10$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 697 | 64.1% | +0.141 | ➡️ estable | +302.69$ | 1.41$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 853 | 57.3% | +0.073 | 📈 madura (+0.03) | +175.71$ | 0.73$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 52 | 65.4% | +0.148 | 📈 madura (+0.14) | +17.26$ | 1.48$ | ✅ activa |
| GBM_LATE_60M | 288 | 39.2% | -0.107 | 📈 madura (+0.08) | +11.37$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1279 | 48.9% | -0.011 | 📈 madura (+0.03) | +10.41$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 19 | 47.4% | -0.023 | — | -0.70$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 558 | 65.9% | +0.159 | 📉 agota (-0.04) | -32.51$ | 1.59$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T18:01 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 1:45PM-2:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-11T18:01 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 11, 1:45PM-2:00PM ET… | ✅ WIN | +1.76$ |
| 2026-07-11T18:01 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 1:45PM-2:00PM ET… | ❌ LOSS | -1.22$ |
| 2026-07-11T18:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 1:45PM-2:00PM ET… | ❌ LOSS | -1.76$ |
| 2026-07-11T18:01 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 11, 1:45PM-2:00PM ET… | ❌ LOSS | -1.68$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T18:02 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,280.92 | 0.1min |  |
| ✅ ETH | $1,823.65 | 0.1min |  |
| ✅ SOL | $78.03 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,280.92 | consenso |  |
| ETH | $1,823.65 | consenso |  |
| SOL | $78.02 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*