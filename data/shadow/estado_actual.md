# Estado del bot — 2026-07-23 13:23 UTC

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
| P&L fiel (stake fijo 1$) | +3595.05 $ |
| P&L sim compuesto | 🟢 +6817.92 $ (ficción Kelly: +26800% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +106.06 $ |
| Operaciones resueltas | 30955 (18583 WIN / 12372 LOSS) — 60.0% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7140 | 59.5% | +0.095 | 📉 agota (-0.03) | +2208.48$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4338 | 62.4% | +0.124 | 📉 agota (-0.04) | +2165.00$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4348 | 57.8% | +0.078 | ➡️ estable | +1278.89$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1366 | 66.5% | +0.165 | ➡️ estable | +635.68$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2329 | 53.2% | +0.032 | 📈 madura (+0.11) | +208.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5414 | 68.7% | +0.187 | ➡️ estable | +96.21$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 859 | 62.9% | +0.128 | ➡️ estable | +44.83$ | 1.28$ | ✅ activa |
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
| LATE_WINDOW_5MIN | 339 | 44.8% | -0.051 | 📉 agota (-0.15) | -3.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 388 | 46.6% | -0.033 | 📉 agota (-0.23) | -6.27$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T13:22 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 9:10AM-9:15AM ET… | ❌ LOSS | -0.56$ |
| 2026-07-23T13:18 | BALLENAS_CONFIRMADAS_15M#DOGE#15min | Dogecoin Up or Down - July 23, 9:00AM-9:15AM ET… | ✅ WIN | +0.60$ |
| 2026-07-23T13:18 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 23, 9:05AM-9:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T13:18 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 23, 9:05AM-9:10AM ET… | ✅ WIN | +0.76$ |
| 2026-07-23T13:18 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 23, 9:05AM-9:10AM ET… | ✅ WIN | +0.68$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T13:21 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,000.33 | 0.1min |  |
| ✅ ETH | $1,897.77 | 0.1min |  |
| ✅ SOL | $76.76 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,000.33 | consenso |  |
| ETH | $1,897.77 | consenso |  |
| SOL | $76.68 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*