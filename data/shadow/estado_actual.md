# Estado del bot — 2026-07-11 14:19 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **23.84 $** |
| P&L real total | 🔴 **-1.60 $** |
| P&L real hoy | -1.46 $ |
| P&L real 7 días | +15.85 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +958.08 $ |
| P&L sim compuesto | 🟢 +1476.77 $ (ficción Kelly: +5805% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +197.36 $ |
| Operaciones resueltas | 9284 (5194 WIN / 4090 LOSS) — 55.9% |
| Señales abiertas | 169 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3253 | 61.3% | +0.113 | ➡️ estable | +1055.26$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 651 | 64.7% | +0.146 | ➡️ estable | +284.95$ | 1.46$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 796 | 58.0% | +0.080 | 📈 madura (+0.04) | +175.31$ | 0.80$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 48 | 62.5% | +0.120 | 📈 madura (+0.15) | +12.30$ | 1.20$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 281 | 39.1% | -0.108 | 📈 madura (+0.10) | +7.10$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1266 | 48.7% | -0.013 | 📈 madura (+0.03) | +3.71$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 490 | 65.1% | +0.150 | 📉 agota (-0.04) | -38.59$ | 1.50$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T14:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 10:00AM-10:15AM ET… | ❌ LOSS | -1.74$ |
| 2026-07-11T14:18 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 10:00AM-10:15AM ET… | ❌ LOSS | -0.95$ |
| 2026-07-11T14:18 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 10:00AM-10:15AM ET… | ✅ WIN | +0.48$ |
| 2026-07-11T14:18 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 10:00AM-10:15AM ET… | ✅ WIN | +0.44$ |
| 2026-07-11T14:18 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 11, 10:00AM-10:15AM ET… | ✅ WIN | +0.79$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T14:18 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,236.82 | 0.1min |  |
| ✅ ETH | $1,801.67 | 0.1min |  |
| ✅ SOL | $78.27 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,236.82 | consenso |  |
| ETH | $1,801.67 | consenso |  |
| SOL | $78.20 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*