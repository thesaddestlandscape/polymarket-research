# Estado del bot — 2026-07-11 21:31 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.32 $** |
| P&L real total | 🔴 **-4.12 $** |
| P&L real hoy | -4.00 $ |
| P&L real 7 días | +13.32 $ |
| Fees pagados (real) | 7.52 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1001.75 $ |
| P&L sim compuesto | 🟢 +1561.84 $ (ficción Kelly: +6139% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +282.44 $ |
| Operaciones resueltas | 9801 (5509 WIN / 4292 LOSS) — 56.2% |
| Señales abiertas | 180 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3354 | 61.1% | +0.111 | ➡️ estable | +1058.75$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 735 | 64.4% | +0.143 | 📉 agota (-0.04) | +310.54$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 897 | 57.6% | +0.076 | ➡️ estable | +182.28$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 134 | 61.9% | +0.118 | 📈 madura (+0.13) | +21.31$ | 1.18$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1286 | 49.0% | -0.010 | 📈 madura (+0.04) | +12.59$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 297 | 38.7% | -0.112 | 📈 madura (+0.04) | +10.33$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 38 | 55.3% | +0.050 | 📈 madura (+0.14) | +1.61$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 620 | 66.8% | +0.167 | 📉 agota (-0.05) | -11.70$ | 1.67$ | ✅ activa |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T21:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 11, 5:00PM-5:15PM ET… | ❌ LOSS | -1.84$ |
| 2026-07-11T21:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 5:00PM-5:15PM ET… | ❌ LOSS | -0.85$ |
| 2026-07-11T21:18 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 11, 5:00PM-5:15PM ET… | ✅ WIN | +0.61$ |
| 2026-07-11T21:18 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 5:00PM-5:15PM ET… | ✅ WIN | +0.19$ |
| 2026-07-11T21:18 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 11, 5:00PM-5:15PM ET… | ✅ WIN | +0.35$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T21:30 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,315.17 | 0.1min |  |
| ✅ ETH | $1,824.35 | 0.1min |  |
| ✅ SOL | $78.24 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,332.40 | consenso |  |
| ETH | $1,825.00 | consenso |  |
| SOL | $78.18 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*