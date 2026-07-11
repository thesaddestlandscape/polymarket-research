# Estado del bot — 2026-07-11 09:53 UTC

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
| P&L fiel (stake fijo 1$) | +930.41 $ |
| P&L sim compuesto | 🟢 +1430.54 $ (ficción Kelly: +5623% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +151.14 $ |
| Operaciones resueltas | 8989 (5025 WIN / 3964 LOSS) — 55.9% |
| Señales abiertas | 171 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3190 | 61.4% | +0.114 | ➡️ estable | +1037.71$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 592 | 65.2% | +0.152 | 📉 agota (-0.04) | +261.39$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 733 | 57.7% | +0.077 | 📈 madura (+0.04) | +154.24$ | 0.77$ | ✅ activa |
| STREAK_FADE_15M | 127 | 62.2% | +0.120 | 📈 madura (+0.13) | +20.22$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 46 | 63.0% | +0.125 | 📈 madura (+0.20) | +10.89$ | 1.25$ | ✅ activa |
| GBM_LATE_60M | 269 | 39.8% | -0.101 | 📈 madura (+0.12) | +10.64$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1255 | 48.4% | -0.016 | ➡️ estable | -2.42$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 409 | 67.2% | +0.172 | 📉 agota (-0.04) | -18.98$ | 1.72$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T09:51 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 5:30AM-5:45AM ET… | ❌ LOSS | -1.48$ |
| 2026-07-11T09:51 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 5:30AM-5:45AM ET… | ✅ WIN | +0.35$ |
| 2026-07-11T09:51 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 5:30AM-5:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T09:51 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 11, 5:30AM-5:45AM ET… | ❌ LOSS | -0.90$ |
| 2026-07-11T09:45 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 5:30AM-5:45AM ET… | ✅ WIN | +1.01$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T09:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,111.57 | 0.1min |  |
| ✅ ETH | $1,797.12 | 0.1min |  |
| ✅ SOL | $77.92 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,127.70 | consenso |  |
| ETH | $1,797.12 | consenso |  |
| SOL | $77.83 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*