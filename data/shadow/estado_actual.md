# Estado del bot — 2026-07-11 03:06 UTC

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
| P&L fiel (stake fijo 1$) | +865.71 $ |
| P&L sim compuesto | 🟢 +1326.25 $ (ficción Kelly: +5213% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +46.84 $ |
| Operaciones resueltas | 8530 (4749 WIN / 3781 LOSS) — 55.7% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3084 | 61.4% | +0.114 | ➡️ estable | +989.45$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 504 | 66.9% | +0.168 | ➡️ estable | +230.44$ | 1.68$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 627 | 56.9% | +0.069 | 📈 madura (+0.03) | +112.31$ | 0.69$ | ✅ activa |
| ORDER_FLOW_5M | 1573 | 51.4% | +0.014 | ➡️ estable | +18.85$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| GBM_LATE_60M | 255 | 38.8% | -0.111 | 📈 madura (+0.08) | +11.22$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 36 | 63.9% | +0.132 | 📈 madura (+0.25) | +7.44$ | 1.32$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 290 | 68.6% | +0.185 | ➡️ estable | -0.76$ | 1.85$ | ✅ activa |
| UPDOWN_GBM | 1248 | 48.6% | -0.014 | ➡️ estable | -1.68$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T03:02 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 10, 10:45PM-11:00PM ET… | ✅ WIN | +0.41$ |
| 2026-07-11T03:02 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 10, 10:45PM-11:00PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T03:02 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 10, 10:45PM-11:00PM ET… | ❌ LOSS | -0.60$ |
| 2026-07-11T03:01 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 10, 10PM ET… | ✅ WIN | +0.07$ |
| 2026-07-11T03:01 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 10, 10PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T03:05 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,091.77 | 0.1min |  |
| ✅ ETH | $1,793.63 | 0.1min |  |
| ✅ SOL | $77.71 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,100.90 | consenso |  |
| ETH | $1,793.63 | consenso |  |
| SOL | $77.65 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*