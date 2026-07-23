# Estado del bot — 2026-07-23 07:06 UTC

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
| P&L fiel (stake fijo 1$) | +3629.86 $ |
| P&L sim compuesto | 🟢 +6851.45 $ (ficción Kelly: +26932% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +139.59 $ |
| Operaciones resueltas | 30447 (18319 WIN / 12128 LOSS) — 60.2% |
| Señales abiertas | 139 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7061 | 59.7% | +0.097 | 📉 agota (-0.03) | +2217.37$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4259 | 62.8% | +0.128 | 📉 agota (-0.04) | +2191.67$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4264 | 58.3% | +0.083 | ➡️ estable | +1307.41$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1339 | 66.5% | +0.165 | ➡️ estable | +619.43$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2307 | 53.1% | +0.031 | 📈 madura (+0.11) | +203.46$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 240 | 60.8% | +0.107 | 📉 agota (-0.07) | +110.47$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5313 | 68.7% | +0.187 | ➡️ estable | +88.06$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 830 | 62.8% | +0.127 | ➡️ estable | +35.48$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 130 | 79.2% | +0.288 | ➡️ estable | +23.71$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 282 | 81.9% | +0.317 | ➡️ estable | +15.20$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 328 | 47.9% | -0.021 | 📉 agota (-0.19) | +7.05$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 23 | 87.0% | +0.340 | — | +1.32$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 331 | 45.6% | -0.044 | 📉 agota (-0.15) | -1.92$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-23T07:04 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.26$ |
| 2026-07-23T07:04 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 2:55AM-3:00AM ET… | ✅ WIN | +0.51$ |
| 2026-07-23T07:04 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 23, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T07:04 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-23T07:04 | GBM_LATE_15M#XRP#15min | XRP Up or Down - July 23, 2:45AM-3:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T07:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,757.51 | 0.1min |  |
| ✅ ETH | $1,924.16 | 0.1min |  |
| ✅ SOL | $77.48 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,757.51 | consenso |  |
| ETH | $1,924.16 | consenso |  |
| SOL | $77.50 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*