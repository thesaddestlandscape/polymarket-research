# Estado del bot — 2026-07-23 13:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **30.13 $** |
| P&L real total | 🔴 **-21.09 $** |
| P&L real hoy | -0.15 $ |
| P&L real 7 días | -1.06 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3607.97 $ |
| P&L sim compuesto | 🟢 +6846.22 $ (ficción Kelly: +26911% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +134.36 $ |
| Operaciones resueltas | 30924 (18575 WIN / 12349 LOSS) — 60.1% |
| Señales abiertas | 157 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7136 | 59.6% | +0.096 | 📉 agota (-0.03) | +2214.53$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4333 | 62.5% | +0.125 | 📉 agota (-0.04) | +2175.00$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4343 | 57.9% | +0.079 | ➡️ estable | +1286.13$ | 0.79$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1364 | 66.5% | +0.165 | ➡️ estable | +632.39$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2327 | 53.2% | +0.032 | 📈 madura (+0.11) | +207.26$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5408 | 68.8% | +0.188 | ➡️ estable | +102.94$ | 1.88$ | ✅ activa |
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
| GBM_LATE_5M | 384 | 47.1% | -0.028 | 📉 agota (-0.22) | -1.59$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 337 | 44.8% | -0.052 | 📉 agota (-0.16) | -4.98$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T13:08 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:08 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:08 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 23, 8:45AM-9:00AM ET… | ✅ WIN | +3.45$ |
| 2026-07-23T13:08 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:08 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 23, 8:45AM-9:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T13:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,018.10 | 0.1min |  |
| ✅ ETH | $1,898.52 | 0.1min |  |
| ✅ SOL | $76.86 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,018.10 | consenso |  |
| ETH | $1,898.52 | consenso |  |
| SOL | $76.73 | consenso |  |
| XRP | $1.12 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*