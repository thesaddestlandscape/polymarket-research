# Estado del bot — 2026-07-10 22:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.92 $** |
| P&L real total | 🔴 **-0.52 $** |
| P&L real hoy | -6.53 $ |
| P&L real 7 días | +1.73 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +825.34 $ |
| P&L sim compuesto | 🟢 +1264.72 $ (ficción Kelly: +4971% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +352.79 $ |
| Operaciones resueltas | 8232 (4568 WIN / 3664 LOSS) — 55.5% |
| Señales abiertas | 186 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3018 | 61.4% | +0.114 | ➡️ estable | +971.79$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 454 | 67.4% | +0.173 | 📈 madura (+0.04) | +212.98$ | 1.73$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 563 | 57.0% | +0.070 | 📈 madura (+0.06) | +96.29$ | 0.70$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 120 | 61.7% | +0.115 | 📈 madura (+0.13) | +17.48$ | 1.15$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 242 | 38.8% | -0.111 | 📈 madura (+0.08) | +9.40$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 30 | 63.3% | +0.125 | 📈 madura (+0.29) | +4.75$ | 1.25$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 203 | 69.0% | +0.188 | 📉 agota (-0.10) | -2.73$ | 1.88$ | ✅ activa |
| UPDOWN_GBM | 1240 | 48.5% | -0.014 | ➡️ estable | -3.15$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T22:30 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 6:15PM-6:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-10T22:30 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 6:15PM-6:30PM ET… | ✅ WIN | +5.23$ |
| 2026-07-10T22:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 6:15PM-6:30PM ET… | ❌ LOSS | -1.13$ |
| 2026-07-10T22:30 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 6:15PM-6:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T22:30 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 10, 6:15PM-6:30PM ET… | ✅ WIN | +1.24$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T22:31 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,043.28 | 0.1min |  |
| ✅ ETH | $1,793.14 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,043.28 | consenso |  |
| ETH | $1,793.14 | consenso |  |
| SOL | $77.98 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*