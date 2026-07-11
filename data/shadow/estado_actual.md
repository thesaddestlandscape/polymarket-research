# Estado del bot — 2026-07-11 01:49 UTC

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
| P&L fiel (stake fijo 1$) | +836.92 $ |
| P&L sim compuesto | 🟢 +1299.34 $ (ficción Kelly: +5107% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +19.93 $ |
| Operaciones resueltas | 8461 (4703 WIN / 3758 LOSS) — 55.6% |
| Señales abiertas | 159 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3070 | 61.4% | +0.114 | ➡️ estable | +987.72$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 494 | 67.0% | +0.169 | ➡️ estable | +218.38$ | 1.69$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 614 | 56.8% | +0.068 | 📈 madura (+0.04) | +106.39$ | 0.68$ | ✅ activa |
| ORDER_FLOW_5M | 1573 | 51.4% | +0.014 | ➡️ estable | +18.85$ | 0.50$ | ✅ activa |
| STREAK_FADE_15M | 121 | 62.0% | +0.118 | 📈 madura (+0.13) | +18.64$ | 1.18$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 249 | 38.2% | -0.118 | 📈 madura (+0.07) | +6.50$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 34 | 61.8% | +0.111 | 📈 madura (+0.26) | +6.47$ | 1.11$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 267 | 67.8% | +0.177 | 📉 agota (-0.06) | -1.22$ | 1.77$ | ✅ activa |
| UPDOWN_GBM | 1247 | 48.5% | -0.015 | ➡️ estable | -2.72$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 306 | 44.8% | -0.052 | 📉 agota (-0.05) | -22.14$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T01:45 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 10, 9:30PM-9:45PM ET… | ✅ WIN | +1.84$ |
| 2026-07-11T01:45 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 10, 9:30PM-9:45PM ET… | ✅ WIN | +0.72$ |
| 2026-07-11T01:45 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 10, 9:30PM-9:45PM ET… | ✅ WIN | +1.97$ |
| 2026-07-11T01:45 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 10, 9:30PM-9:45PM ET… | ✅ WIN | +1.84$ |
| 2026-07-11T01:45 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 10, 9:30PM-9:45PM ET… | ✅ WIN | +1.66$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T01:48 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,045.79 | 0.1min |  |
| ✅ ETH | $1,790.49 | 0.1min |  |
| ✅ SOL | $77.58 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,045.79 | consenso |  |
| ETH | $1,790.69 | consenso |  |
| SOL | $77.58 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*