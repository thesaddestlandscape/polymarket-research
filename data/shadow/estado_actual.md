# Estado del bot — 2026-07-23 15:28 UTC

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
| P&L fiel (stake fijo 1$) | +3585.08 $ |
| P&L sim compuesto | 🟢 +6814.24 $ (ficción Kelly: +26786% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +102.38 $ |
| Operaciones resueltas | 31153 (18689 WIN / 12464 LOSS) — 60.0% |
| Señales abiertas | 168 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7162 | 59.5% | +0.095 | 📉 agota (-0.04) | +2200.55$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4355 | 62.4% | +0.124 | 📉 agota (-0.04) | +2159.08$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4372 | 57.7% | +0.077 | ➡️ estable | +1265.66$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1390 | 66.5% | +0.165 | 📉 agota (-0.03) | +649.30$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2348 | 53.2% | +0.032 | 📈 madura (+0.11) | +209.45$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5450 | 68.8% | +0.188 | ➡️ estable | +107.03$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 864 | 62.7% | +0.127 | ➡️ estable | +41.50$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 291 | 82.1% | +0.319 | ➡️ estable | +17.68$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_5M | 428 | 47.0% | -0.030 | 📉 agota (-0.19) | -3.71$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 346 | 44.8% | -0.052 | 📉 agota (-0.14) | -4.33$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T15:26 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:15AM-11:20AM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T15:26 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:10AM-11:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T15:23 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 11:00AM-11:15AM ET… | ✅ WIN | +1.38$ |
| 2026-07-23T15:23 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 23, 11:00AM-11:15AM ET… | ❌ LOSS | -1.98$ |
| 2026-07-23T15:23 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 23, 11:00AM-11:15AM ET… | ❌ LOSS | -1.36$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T15:26 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,870.99 | 0.1min |  |
| ✅ ETH | $1,894.19 | 0.1min |  |
| ✅ SOL | $76.27 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,870.99 | consenso |  |
| ETH | $1,894.37 | consenso |  |
| SOL | $76.27 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*