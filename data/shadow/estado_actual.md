# Estado del bot — 2026-07-23 13:17 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.42 $** |
| P&L real total | 🔴 **-21.80 $** |
| P&L real hoy | -1.24 $ |
| P&L real 7 días | -2.15 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3606.06 $ |
| P&L sim compuesto | 🟢 +6839.44 $ (ficción Kelly: +26885% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +127.58 $ |
| Operaciones resueltas | 30930 (18576 WIN / 12354 LOSS) — 60.1% |
| Señales abiertas | 159 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7137 | 59.5% | +0.095 | 📉 agota (-0.03) | +2213.51$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4334 | 62.5% | +0.125 | 📉 agota (-0.04) | +2172.96$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4344 | 57.9% | +0.079 | ➡️ estable | +1284.77$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1364 | 66.5% | +0.165 | ➡️ estable | +632.39$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2327 | 53.2% | +0.032 | 📈 madura (+0.11) | +207.26$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5409 | 68.8% | +0.188 | ➡️ estable | +100.90$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 858 | 62.8% | +0.128 | ➡️ estable | +44.23$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 288 | 82.3% | +0.321 | ➡️ estable | +18.59$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 338 | 45.0% | -0.050 | 📉 agota (-0.15) | -3.26$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 385 | 47.0% | -0.030 | 📉 agota (-0.22) | -3.63$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T13:15 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 23, 9:00AM-9:05AM ET… | ✅ WIN | +1.71$ |
| 2026-07-23T13:12 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 23, 9:00AM-9:05AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:12 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -1.36$ |
| 2026-07-23T13:12 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:12 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -1.02$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T13:15 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,002.72 | 0.1min |  |
| ✅ ETH | $1,898.07 | 0.1min |  |
| ✅ SOL | $76.74 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,008.00 | consenso |  |
| ETH | $1,898.07 | consenso |  |
| SOL | $76.77 | consenso |  |
| XRP | $1.12 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*