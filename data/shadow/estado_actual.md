# Estado del bot — 2026-07-23 21:01 UTC

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
| P&L fiel (stake fijo 1$) | +3645.98 $ |
| P&L sim compuesto | 🟢 +6936.62 $ (ficción Kelly: +27267% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +224.76 $ |
| Operaciones resueltas | 31637 (19000 WIN / 12637 LOSS) — 60.1% |
| Señales abiertas | 156 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7228 | 59.6% | +0.096 | 📉 agota (-0.04) | +2246.55$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4421 | 62.5% | +0.125 | 📉 agota (-0.05) | +2202.87$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4445 | 57.7% | +0.077 | 📉 agota (-0.03) | +1288.45$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1425 | 66.3% | +0.163 | 📉 agota (-0.03) | +656.72$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2383 | 53.2% | +0.032 | 📈 madura (+0.10) | +207.31$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 245 | 60.8% | +0.107 | 📉 agota (-0.06) | +111.22$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5538 | 68.8% | +0.188 | ➡️ estable | +99.84$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 886 | 62.8% | +0.127 | ➡️ estable | +41.10$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | 79.9% | +0.294 | ➡️ estable | +25.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 299 | 82.3% | +0.321 | ➡️ estable | +19.16$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 492 | 47.8% | -0.022 | 📉 agota (-0.06) | +1.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-23T20:51 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 4:30PM-4:45PM ET… | ✅ WIN | +0.84$ |
| 2026-07-23T20:51 | UPDOWN_GBM_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 4:30PM-4:45PM ET… | ❌ LOSS | -1.74$ |
| 2026-07-23T20:51 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 4:30PM-4:45PM ET… | ✅ WIN | +0.80$ |
| 2026-07-23T20:51 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 23, 4:30PM-4:45PM ET… | ✅ WIN | +0.75$ |
| 2026-07-23T20:51 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 4:30PM-4:45PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T20:57 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,076.89 | 0.1min |  |
| ✅ ETH | $1,884.05 | 0.1min |  |
| ✅ SOL | $76.14 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,088.60 | consenso |  |
| ETH | $1,884.40 | consenso |  |
| SOL | $76.06 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*