# Estado del bot — 2026-07-23 17:19 UTC

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
| P&L fiel (stake fijo 1$) | +3605.85 $ |
| P&L sim compuesto | 🟢 +6864.02 $ (ficción Kelly: +26981% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +152.16 $ |
| Operaciones resueltas | 31330 (18807 WIN / 12523 LOSS) — 60.0% |
| Señales abiertas | 167 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7181 | 59.5% | +0.095 | 📉 agota (-0.04) | +2219.89$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4377 | 62.4% | +0.124 | 📉 agota (-0.05) | +2174.60$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4395 | 57.7% | +0.077 | 📉 agota (-0.03) | +1273.15$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1402 | 66.5% | +0.165 | ➡️ estable | +653.23$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2364 | 53.1% | +0.031 | 📈 madura (+0.10) | +206.26$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5478 | 68.8% | +0.188 | ➡️ estable | +107.44$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 871 | 62.8% | +0.128 | ➡️ estable | +42.68$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 293 | 82.3% | +0.320 | ➡️ estable | +18.14$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 455 | 47.7% | -0.023 | 📉 agota (-0.14) | -0.69$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-23T17:12 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 1:00PM-1:05PM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T17:12 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 12:55PM-1:00PM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T17:08 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.37$ |
| 2026-07-23T17:08 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 12:45PM-1:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T17:08 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 12:45PM-1:00PM ET… | ✅ WIN | +2.07$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T17:18 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,729.99 | 0.1min |  |
| ✅ ETH | $1,886.80 | 0.1min |  |
| ✅ SOL | $76.00 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,732.40 | consenso |  |
| ETH | $1,887.05 | consenso |  |
| SOL | $75.92 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*