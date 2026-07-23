# Estado del bot — 2026-07-23 22:06 UTC

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
| P&L fiel (stake fijo 1$) | +3650.44 $ |
| P&L sim compuesto | 🟢 +6943.60 $ (ficción Kelly: +27294% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +231.74 $ |
| Operaciones resueltas | 31718 (19045 WIN / 12673 LOSS) — 60.0% |
| Señales abiertas | 161 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7240 | 59.6% | +0.096 | 📉 agota (-0.04) | +2250.51$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4435 | 62.5% | +0.125 | 📉 agota (-0.05) | +2208.98$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4460 | 57.7% | +0.077 | 📉 agota (-0.04) | +1288.72$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1428 | 66.3% | +0.163 | ➡️ estable | +658.87$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2385 | 53.2% | +0.032 | 📈 madura (+0.10) | +208.13$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 246 | 61.0% | +0.109 | 📉 agota (-0.06) | +112.75$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5556 | 68.8% | +0.188 | ➡️ estable | +98.10$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 891 | 62.7% | +0.127 | ➡️ estable | +40.21$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | 79.9% | +0.294 | ➡️ estable | +25.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 301 | 82.1% | +0.318 | ➡️ estable | +17.76$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 501 | 47.5% | -0.025 | 📉 agota (-0.07) | -2.00$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-23T22:04 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 5:50PM-5:55PM ET… | ❌ LOSS | -1.02$ |
| 2026-07-23T21:55 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 23, 5:40PM-5:45PM ET… | ✅ WIN | +1.32$ |
| 2026-07-23T21:55 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 23, 5:40PM-5:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T21:55 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 5:30PM-5:45PM ET… | ✅ WIN | +0.38$ |
| 2026-07-23T21:55 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 23, 5:30PM-5:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T22:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,118.26 | 0.1min |  |
| ✅ ETH | $1,881.24 | 0.1min |  |
| ✅ SOL | $76.01 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,121.30 | consenso |  |
| ETH | $1,881.24 | consenso |  |
| SOL | $75.99 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*