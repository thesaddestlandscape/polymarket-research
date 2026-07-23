# Estado del bot — 2026-07-23 16:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| P&L real hoy | -2.32 $ |
| P&L real 7 días | -3.23 $ |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3589.88 $ |
| P&L sim compuesto | 🟢 +6844.14 $ (ficción Kelly: +26903% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +132.28 $ |
| Operaciones resueltas | 31264 (18762 WIN / 12502 LOSS) — 60.0% |
| Señales abiertas | 163 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7171 | 59.5% | +0.095 | 📉 agota (-0.04) | +2212.10$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4366 | 62.4% | +0.124 | 📉 agota (-0.04) | +2169.68$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4384 | 57.7% | +0.077 | ➡️ estable | +1270.14$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1396 | 66.4% | +0.164 | 📉 agota (-0.03) | +647.34$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2359 | 53.0% | +0.030 | 📈 madura (+0.10) | +203.50$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5467 | 68.9% | +0.189 | ➡️ estable | +113.84$ | 1.89$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 869 | 62.7% | +0.127 | ➡️ estable | +41.48$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 293 | 82.3% | +0.320 | ➡️ estable | +18.14$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 446 | 47.5% | -0.025 | 📉 agota (-0.16) | -1.04$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 348 | 44.8% | -0.051 | 📉 agota (-0.14) | -4.38$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T16:31 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 12:20PM-12:25PM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T16:24 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 12:15PM-12:20PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T16:24 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 23, 12:00PM-12:15PM ET… | ❌ LOSS | -1.35$ |
| 2026-07-23T16:24 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 12:00PM-12:15PM ET… | ✅ WIN | +0.88$ |
| 2026-07-23T16:21 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 12:10PM-12:15PM ET… | ✅ WIN | +0.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T16:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,740.87 | 0.1min |  |
| ✅ ETH | $1,887.01 | 0.1min |  |
| ✅ SOL | $76.08 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,751.70 | consenso |  |
| ETH | $1,887.82 | consenso |  |
| SOL | $76.03 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*