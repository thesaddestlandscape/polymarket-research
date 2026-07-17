# Estado del bot — 2026-07-17 02:09 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **2.94 $** |
| P&L real total | 🔴 **-22.50 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -28.51 $ |
| Fees pagados (real) | 8.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2150.09 $ |
| P&L sim compuesto | 🟢 +3769.41 $ (ficción Kelly: +14817% s/ operativo) |
| P&L sim hoy (2026-07-17) | 🟢 +48.35 $ |
| Operaciones resueltas | 17935 (10595 WIN / 7340 LOSS) — 59.1% |
| Señales abiertas | 78 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5076 | 60.2% | +0.102 | ➡️ estable | +1585.24$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2284 | 65.0% | +0.150 | 📉 agota (-0.04) | +1319.83$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2264 | 59.5% | +0.094 | ➡️ estable | +709.70$ | 0.94$ | ✅ activa |
| UPDOWN_GBM | 1629 | 51.0% | +0.010 | 📈 madura (+0.09) | +71.97$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 192 | 67.2% | +0.170 | 📉 agota (-0.09) | +59.59$ | 1.70$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 114 | 64.0% | +0.138 | 📈 madura (+0.12) | +53.42$ | 1.38$ | ✅ activa |
| STREAK_FADE_15M | 207 | 60.4% | +0.103 | 📈 madura (+0.04) | +32.94$ | 1.03$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 47 | 74.5% | +0.235 | ➡️ estable | +24.66$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 154 | 56.5% | +0.064 | 📉 agota (-0.14) | +20.18$ | 0.64$ | ✅ activa |
| ORDER_FLOW_5M | 1620 | 51.3% | +0.013 | ➡️ estable | +14.54$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 23 | 78.3% | +0.260 | — | +2.31$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 60 | 81.7% | +0.306 | 📈 madura (+0.03) | +1.64$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2793 | 67.4% | +0.174 | ➡️ estable | -69.35$ | 1.74$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-17T02:06 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 16, 9:55PM-10:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-17T02:02 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 16, 9:45PM-10:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-17T02:02 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 16, 9:45PM-10:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-17T02:02 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 16, 9:45PM-10:00PM ET… | ✅ WIN | +2.00$ |
| 2026-07-17T02:02 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 16, 9:45PM-10:00PM ET… | ✅ WIN | +2.00$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-17T02:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,533.25 | 0.1min |  |
| ✅ ETH | $1,852.27 | 0.1min |  |
| ✅ SOL | $75.23 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,537.20 | consenso |  |
| ETH | $1,852.37 | consenso |  |
| SOL | $75.14 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*