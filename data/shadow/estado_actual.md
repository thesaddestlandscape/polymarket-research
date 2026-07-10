# Estado del bot — 2026-07-10 23:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **24.37 $** |
| P&L real total | 🔴 **-1.07 $** |
| P&L real hoy | -7.62 $ |
| P&L real 7 días | +0.64 $ |
| Fees pagados (real) | 7.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +833.26 $ |
| P&L sim compuesto | 🟢 +1286.74 $ (ficción Kelly: +5058% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +374.81 $ |
| Operaciones resueltas | 8305 (4614 WIN / 3691 LOSS) — 55.6% |
| Señales abiertas | 182 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3035 | 61.4% | +0.114 | ➡️ estable | +977.35$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 466 | 67.6% | +0.175 | ➡️ estable | +219.52$ | 1.75$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 579 | 57.0% | +0.070 | 📈 madura (+0.05) | +101.37$ | 0.70$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 245 | 38.4% | -0.115 | 📈 madura (+0.08) | +7.87$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 30 | 63.3% | +0.125 | 📈 madura (+0.29) | +4.75$ | 1.25$ | ✅ activa |
| FAVORITO_CONFIRMADO | 223 | 69.5% | +0.193 | 📉 agota (-0.05) | +3.61$ | 1.93$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1244 | 48.5% | -0.015 | ➡️ estable | -4.28$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T23:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 7:15PM-7:30PM ET… | ✅ WIN | +1.78$ |
| 2026-07-10T23:30 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 7:15PM-7:30PM ET… | ✅ WIN | +1.59$ |
| 2026-07-10T23:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 10, 7:15PM-7:30PM ET… | ✅ WIN | +0.77$ |
| 2026-07-10T23:30 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 10, 7:15PM-7:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T23:30 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 10, 7:15PM-7:30PM ET… | ✅ WIN | +1.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T23:32 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,159.89 | 0.1min |  |
| ✅ ETH | $1,795.04 | 0.1min |  |
| ✅ SOL | $78.08 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,159.89 | consenso |  |
| ETH | $1,795.11 | consenso |  |
| SOL | $78.05 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*