# Estado del bot — 2026-07-10 16:15 UTC

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
| P&L fiel (stake fijo 1$) | +780.20 $ |
| P&L sim compuesto | 🟢 +1185.81 $ (ficción Kelly: +4661% s/ operativo) |
| P&L sim hoy (2026-07-10) | 🟢 +273.88 $ |
| Operaciones resueltas | 7820 (4319 WIN / 3501 LOSS) — 55.2% |
| Señales abiertas | 191 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 2920 | 61.5% | +0.115 | ➡️ estable | +953.66$ | 1.15$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 375 | 67.2% | +0.171 | 📈 madura (+0.06) | +157.60$ | 1.71$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 466 | 57.7% | +0.077 | 📈 madura (+0.11) | +83.73$ | 0.77$ | ✅ activa |
| ORDER_FLOW_5M | 1570 | 51.3% | +0.013 | ➡️ estable | +17.57$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 118 | 61.0% | +0.108 | 📈 madura (+0.13) | +16.00$ | 1.08$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO | 100 | 75.0% | +0.245 | 📈 madura (+0.10) | +8.17$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 233 | 37.8% | -0.121 | 📈 madura (+0.06) | +5.37$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 26 | 57.7% | +0.071 | — | +1.86$ | 0.71$ | ✅ activa |
| UPDOWN_GBM | 1220 | 48.6% | -0.014 | ➡️ estable | +1.52$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-10T16:14 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 12:05PM-12:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T16:14 | FAVORITO_CONFIRMADO#BTC#5min | Bitcoin Up or Down - July 10, 12:05PM-12:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T16:12 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 12:05PM-12:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-10T16:08 | PRICE_TARGET_GBM#SOL#atexpiry | Will the price of Solana be above $80 on July 10?… | ✅ WIN | +0.77$ |
| 2026-07-10T16:08 | WEEKLY_PRICE#ETH | Will the price of Ethereum be between $1,700 and $… | ✅ WIN | +1.01$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-10T16:14 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,954.64 | 0.1min |  |
| ✅ ETH | $1,790.34 | 0.1min |  |
| ✅ SOL | $78.11 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,964.20 | consenso |  |
| ETH | $1,790.47 | consenso |  |
| SOL | $77.98 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*