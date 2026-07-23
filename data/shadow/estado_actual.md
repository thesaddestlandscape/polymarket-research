# Estado del bot — 2026-07-23 07:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.40 $** |
| P&L real total | 🔴 **-21.82 $** |
| P&L real hoy | +0.17 $ |
| P&L real 7 días | -0.74 $ |
| Fees pagados (real) | 9.73 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3637.83 $ |
| P&L sim compuesto | 🟢 +6864.12 $ (ficción Kelly: +26982% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +152.26 $ |
| Operaciones resueltas | 30474 (18339 WIN / 12135 LOSS) — 60.2% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7065 | 59.7% | +0.097 | 📉 agota (-0.03) | +2221.86$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4262 | 62.8% | +0.128 | 📉 agota (-0.04) | +2196.27$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4267 | 58.2% | +0.082 | ➡️ estable | +1306.16$ | 0.82$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1341 | 66.5% | +0.165 | ➡️ estable | +619.31$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2308 | 53.2% | +0.032 | 📈 madura (+0.11) | +204.57$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 240 | 60.8% | +0.107 | 📉 agota (-0.07) | +110.47$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5319 | 68.8% | +0.187 | ➡️ estable | +89.57$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 832 | 62.9% | +0.128 | ➡️ estable | +36.81$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 268 | 58.6% | +0.085 | 📉 agota (-0.07) | +34.45$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 130 | 79.2% | +0.288 | ➡️ estable | +23.71$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 282 | 81.9% | +0.317 | ➡️ estable | +15.20$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 331 | 47.7% | -0.023 | 📉 agota (-0.18) | +6.44$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 23 | 87.0% | +0.340 | — | +1.32$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 12 | 50.0% | +0.000 | — | -0.28$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 332 | 45.5% | -0.045 | 📉 agota (-0.15) | -2.43$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 318 | 44.0% | -0.059 | 📉 agota (-0.09) | -25.84$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T07:31 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 3:20AM-3:25AM ET… | ❌ LOSS | -0.58$ |
| 2026-07-23T07:25 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 23, 3:15AM-3:20AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T07:25 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 3:15AM-3:20AM ET… | ✅ WIN | +0.56$ |
| 2026-07-23T07:22 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 3:10AM-3:15AM ET… | ❌ LOSS | -0.58$ |
| 2026-07-23T07:18 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 3:00AM-3:15AM ET… | ✅ WIN | +0.19$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T07:31 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,397.07 | 0.1min |  |
| ✅ ETH | $1,914.07 | 0.1min |  |
| ✅ SOL | $77.12 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,397.07 | consenso |  |
| ETH | $1,914.71 | consenso |  |
| SOL | $77.12 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*