# Estado del bot — 2026-07-11 05:00 UTC

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
| P&L fiel (stake fijo 1$) | +882.31 $ |
| P&L sim compuesto | 🟢 +1358.09 $ (ficción Kelly: +5338% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +78.69 $ |
| Operaciones resueltas | 8657 (4827 WIN / 3830 LOSS) — 55.8% |
| Señales abiertas | 175 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3114 | 61.4% | +0.114 | ➡️ estable | +1006.22$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 530 | 66.4% | +0.164 | ➡️ estable | +238.36$ | 1.64$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 657 | 56.9% | +0.069 | ➡️ estable | +122.31$ | 0.69$ | ✅ activa |
| STREAK_FADE_15M | 123 | 61.8% | +0.116 | 📈 madura (+0.12) | +18.59$ | 1.16$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 39 | 66.7% | +0.159 | 📈 madura (+0.34) | +10.37$ | 1.58$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 257 | 38.5% | -0.114 | 📈 madura (+0.08) | +10.20$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1249 | 48.6% | -0.014 | ➡️ estable | -0.62$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 322 | 68.6% | +0.185 | ➡️ estable | -5.20$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T04:52 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 12:30AM-12:45AM ET… | ❌ LOSS | -0.87$ |
| 2026-07-11T04:52 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 12:30AM-12:45AM ET… | ✅ WIN | +0.48$ |
| 2026-07-11T04:52 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 12:30AM-12:45AM ET… | ✅ WIN | +1.92$ |
| 2026-07-11T04:52 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 11, 12:30AM-12:45AM ET… | ✅ WIN | +0.79$ |
| 2026-07-11T04:47 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 11, 12:30AM-12:45AM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T04:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,089.46 | 0.1min |  |
| ✅ ETH | $1,794.81 | 0.1min |  |
| ✅ SOL | $77.73 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,089.46 | consenso |  |
| ETH | $1,794.81 | consenso |  |
| SOL | $77.62 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*