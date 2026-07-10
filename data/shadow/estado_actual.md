# Estado del bot — 2026-07-10 13:24 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **26.01 $** |
| P&L real total | 🟢 **+0.57 $** |
| P&L real hoy | -5.44 $ |
| P&L real 7 días | +2.82 $ |
| Fees pagados (real) | 7.14 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +704.38 $ |
| P&L sim compuesto | 🟢 +1090.98 $ (ficción Kelly: +4288% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +179.05 $ |
| Operaciones resueltas | 7608 (4154 WIN / 3454 LOSS) — 54.6% |
| Señales abiertas | 170 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2878 | 61.3% | +0.113 | ➡️ estable | +930.56$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 339 | 65.2% | +0.151 | ➡️ estable | +122.84$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 424 | 55.7% | +0.056 | 📈 madura (+0.07) | +60.80$ | 0.56$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 114 | 59.6% | +0.095 | 📈 madura (+0.10) | +12.36$ | 0.95$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 227 | 38.3% | -0.116 | 📈 madura (+0.07) | +7.56$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 1212 | 48.6% | -0.014 | ➡️ estable | +1.31$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 24 | 54.2% | +0.038 | — | +0.89$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO | 46 | 67.4% | +0.167 | 📉 agota (-0.04) | -0.65$ | 1.67$ | ✅ activa |
| PRICE_TARGET_GBM | 132 | 34.1% | -0.157 | 📉 agota (-0.10) | -0.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 159 | 55.3% | +0.053 | 📈 madura (+0.14) | -15.64$ | 0.53$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T13:19 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 9:00AM-9:15AM ET… | ❌ LOSS | -1.77$ |
| 2026-07-10T13:19 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 10, 9:00AM-9:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T13:19 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 10, 9:00AM-9:15AM ET… | ❌ LOSS | -0.75$ |
| 2026-07-10T13:19 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 10, 9:00AM-9:15AM ET… | ✅ WIN | +0.58$ |
| 2026-07-10T13:19 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 9:00AM-9:15AM ET… | ✅ WIN | +0.28$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T13:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,149.54 | 0.1min |  |
| ✅ ETH | $1,793.33 | 0.1min |  |
| ✅ SOL | $78.96 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,164.30 | consenso |  |
| ETH | $1,793.68 | consenso |  |
| SOL | $78.84 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*