# Estado del bot — 2026-07-23 13:36 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.07 $** |
| P&L real total | 🔴 **-22.15 $** |
| P&L real hoy | -1.24 $ |
| P&L real 7 días | -2.15 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3590.51 $ |
| P&L sim compuesto | 🟢 +6808.97 $ (ficción Kelly: +26765% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +97.12 $ |
| Operaciones resueltas | 30975 (18591 WIN / 12384 LOSS) — 60.0% |
| Señales abiertas | 156 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7142 | 59.5% | +0.095 | 📉 agota (-0.03) | +2204.91$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4340 | 62.4% | +0.124 | 📉 agota (-0.04) | +2160.99$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4350 | 57.8% | +0.078 | ➡️ estable | +1275.66$ | 0.78$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1368 | 66.6% | +0.166 | ➡️ estable | +638.62$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2330 | 53.3% | +0.033 | 📈 madura (+0.11) | +209.25$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5416 | 68.7% | +0.187 | ➡️ estable | +96.07$ | 1.87$ | ✅ activa |
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
| LATE_WINDOW_5MIN | 342 | 44.7% | -0.052 | 📉 agota (-0.16) | -4.31$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 394 | 46.7% | -0.033 | 📉 agota (-0.22) | -7.35$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T13:35 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 9:20AM-9:25AM ET… | ✅ WIN | +0.42$ |
| 2026-07-23T13:35 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 23, 9:15AM-9:30AM ET… | ✅ WIN | +1.50$ |
| 2026-07-23T13:35 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 23, 9:15AM-9:30AM ET… | ❌ LOSS | -1.19$ |
| 2026-07-23T13:35 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 9:15AM-9:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T13:35 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 9:15AM-9:30AM ET… | ❌ LOSS | -1.97$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T13:34 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,135.19 | 0.1min |  |
| ✅ ETH | $1,903.95 | 0.1min |  |
| ✅ SOL | $76.95 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,135.19 | consenso |  |
| ETH | $1,903.95 | consenso |  |
| SOL | $76.90 | consenso |  |
| XRP | $1.12 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*