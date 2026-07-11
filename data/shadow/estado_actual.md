# Estado del bot — 2026-07-11 08:02 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **25.30 $** |
| P&L real total | 🔴 **-0.14 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +17.32 $ |
| Fees pagados (real) | 7.27 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +923.47 $ |
| P&L sim compuesto | 🟢 +1410.62 $ (ficción Kelly: +5545% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +131.22 $ |
| Operaciones resueltas | 8863 (4950 WIN / 3913 LOSS) — 55.9% |
| Señales abiertas | 169 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3162 | 61.4% | +0.114 | ➡️ estable | +1026.73$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 567 | 66.0% | +0.159 | ➡️ estable | +262.17$ | 1.59$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 705 | 57.7% | +0.077 | ➡️ estable | +147.40$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 263 | 39.2% | -0.108 | 📈 madura (+0.11) | +10.26$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 44 | 63.6% | +0.130 | 📈 madura (+0.17) | +9.50$ | 1.30$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1253 | 48.5% | -0.015 | ➡️ estable | -1.35$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 374 | 66.8% | +0.168 | 📉 agota (-0.04) | -21.16$ | 1.68$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T08:00 | FAVORITO_CONFIRMADO#ETH#240min | Ethereum Up or Down - July 11, 12:00AM-4:00AM ET… | ✅ WIN | +0.40$ |
| 2026-07-11T08:00 | FAVORITO_CONFIRMADO#SOL#240min | Solana Up or Down - July 11, 12:00AM-4:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T07:49 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 3:30AM-3:45AM ET… | ❌ LOSS | -1.31$ |
| 2026-07-11T07:49 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 3:30AM-3:45AM ET… | ✅ WIN | +0.83$ |
| 2026-07-11T07:49 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 3:30AM-3:45AM ET… | ✅ WIN | +0.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T08:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,111.32 | 0.1min |  |
| ✅ ETH | $1,798.32 | 0.1min |  |
| ✅ SOL | $78.01 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,116.10 | consenso |  |
| ETH | $1,798.32 | consenso |  |
| SOL | $77.93 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*