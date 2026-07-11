# Estado del bot — 2026-07-11 04:24 UTC

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
| P&L fiel (stake fijo 1$) | +871.71 $ |
| P&L sim compuesto | 🟢 +1338.03 $ (ficción Kelly: +5260% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +58.62 $ |
| Operaciones resueltas | 8628 (4806 WIN / 3822 LOSS) — 55.7% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3106 | 61.3% | +0.113 | ➡️ estable | +997.81$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 523 | 66.3% | +0.163 | ➡️ estable | +231.06$ | 1.63$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 649 | 57.0% | +0.070 | ➡️ estable | +118.95$ | 0.70$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 316 | 68.4% | +0.182 | 📉 agota (-0.04) | -6.20$ | 1.82$ | ✅ activa |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T04:17 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 12:00AM-12:15AM ET… | ❌ LOSS | -1.27$ |
| 2026-07-11T04:17 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 12:00AM-12:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T04:17 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 11, 12:00AM-12:15AM ET… | ❌ LOSS | -0.57$ |
| 2026-07-11T04:17 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 12:00AM-12:15AM ET… | ✅ WIN | +0.39$ |
| 2026-07-11T04:17 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 12:00AM-12:15AM ET… | ✅ WIN | +0.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T04:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,097.89 | 0.1min |  |
| ✅ ETH | $1,795.68 | 0.1min |  |
| ✅ SOL | $77.74 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,097.89 | consenso |  |
| ETH | $1,795.68 | consenso |  |
| SOL | $77.67 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*