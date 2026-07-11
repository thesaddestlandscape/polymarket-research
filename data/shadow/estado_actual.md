# Estado del bot — 2026-07-11 22:34 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **18.55 $** |
| P&L real total | 🔴 **-6.88 $** |
| P&L real hoy | -6.75 $ |
| P&L real 7 días | +10.57 $ |
| Fees pagados (real) | 7.56 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1007.81 $ |
| P&L sim compuesto | 🟢 +1563.37 $ (ficción Kelly: +6145% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +283.96 $ |
| Operaciones resueltas | 9878 (5558 WIN / 4320 LOSS) — 56.3% |
| Señales abiertas | 175 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3368 | 61.1% | +0.111 | ➡️ estable | +1057.57$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 748 | 64.6% | +0.145 | 📉 agota (-0.05) | +315.42$ | 1.45$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 911 | 57.6% | +0.076 | ➡️ estable | +179.59$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 54 | 64.8% | +0.143 | 📈 madura (+0.10) | +17.14$ | 1.43$ | ✅ activa |
| UPDOWN_GBM | 1288 | 49.0% | -0.010 | 📈 madura (+0.04) | +12.58$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 299 | 38.8% | -0.111 | 📈 madura (+0.05) | +10.09$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 49 | 53.1% | +0.029 | ➡️ estable | +0.99$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 640 | 67.2% | +0.171 | ➡️ estable | -8.26$ | 1.71$ | ✅ activa |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T22:30 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 6:15PM-6:30PM ET… | ✅ WIN | +0.10$ |
| 2026-07-11T22:30 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 6:15PM-6:30PM ET… | ✅ WIN | +0.56$ |
| 2026-07-11T22:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 6:15PM-6:30PM ET… | ✅ WIN | +0.42$ |
| 2026-07-11T22:30 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 11, 6:15PM-6:30PM ET… | ❌ LOSS | -1.94$ |
| 2026-07-11T22:30 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 6:15PM-6:30PM ET… | ✅ WIN | +0.55$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T22:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,242.36 | 0.1min |  |
| ✅ ETH | $1,815.09 | 0.1min |  |
| ✅ SOL | $78.00 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,243.10 | consenso |  |
| ETH | $1,815.21 | consenso |  |
| SOL | $77.93 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*