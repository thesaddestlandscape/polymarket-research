# Estado del bot — 2026-07-11 00:21 UTC

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
| P&L fiel (stake fijo 1$) | +827.52 $ |
| P&L sim compuesto | 🟢 +1282.38 $ (ficción Kelly: +5041% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +2.98 $ |
| Operaciones resueltas | 8371 (4648 WIN / 3723 LOSS) — 55.5% |
| Señales abiertas | 164 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3048 | 61.5% | +0.114 | ➡️ estable | +978.47$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 476 | 67.2% | +0.172 | ➡️ estable | +217.09$ | 1.72$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 592 | 57.1% | +0.071 | 📈 madura (+0.05) | +102.27$ | 0.71$ | ✅ activa |
| ORDER_FLOW_5M | 1571 | 51.4% | +0.014 | ➡️ estable | +18.87$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 248 | 37.9% | -0.120 | 📈 madura (+0.06) | +6.34$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 33 | 60.6% | +0.100 | 📈 madura (+0.18) | +4.99$ | 1.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 244 | 67.6% | +0.175 | 📉 agota (-0.06) | -1.05$ | 1.75$ | ✅ activa |
| UPDOWN_GBM | 1246 | 48.5% | -0.015 | ➡️ estable | -3.59$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T00:16 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 8:10PM-8:15PM ET… | ✅ WIN | +0.19$ |
| 2026-07-11T00:16 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 8:10PM-8:15PM ET… | ✅ WIN | +0.22$ |
| 2026-07-11T00:16 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 8:00PM-8:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-11T00:16 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 10, 8:05PM-8:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T00:16 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 10, 8:05PM-8:10PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T00:20 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,017.24 | 0.1min |  |
| ✅ ETH | $1,791.69 | 0.1min |  |
| ✅ SOL | $77.85 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,032.10 | consenso |  |
| ETH | $1,792.20 | consenso |  |
| SOL | $77.87 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*