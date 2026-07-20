# Estado del bot — 2026-07-20 07:29 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3367.19 $ |
| P&L sim compuesto | 🟢 +6184.50 $ (ficción Kelly: +24310% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +186.18 $ |
| Operaciones resueltas | 24121 (14683 WIN / 9438 LOSS) — 60.9% |
| Señales abiertas | 136 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6078 | 60.8% | +0.108 | ➡️ estable | +2134.13$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3297 | 65.5% | +0.154 | ➡️ estable | +2038.70$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3261 | 60.4% | +0.104 | 📈 madura (+0.05) | +1222.45$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 766 | 67.4% | +0.173 | ➡️ estable | +345.54$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 1925 | 52.1% | +0.021 | 📈 madura (+0.11) | +133.46$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 181 | 65.7% | +0.156 | 📈 madura (+0.07) | +97.05$ | 1.56$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4138 | 68.8% | +0.188 | ➡️ estable | +87.40$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 233 | 59.7% | +0.096 | ➡️ estable | +35.46$ | 0.96$ | ✅ activa |
| GBM_LATE_5M | 182 | 58.8% | +0.087 | ➡️ estable | +29.76$ | 0.87$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 400 | 65.0% | +0.149 | ➡️ estable | +22.28$ | 1.49$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 216 | 52.3% | +0.023 | 📉 agota (-0.14) | +11.92$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 174 | 82.2% | +0.318 | 📉 agota (-0.03) | +9.28$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-20T07:28 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 3:15AM-3:20AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T07:25 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 20, 3:20AM-3:25AM ET… | ❌ LOSS | -1.36$ |
| 2026-07-20T07:25 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 3:20AM-3:25AM ET… | ✅ WIN | +0.77$ |
| 2026-07-20T07:20 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 20, 3:10AM-3:15AM ET… | ✅ WIN | +1.56$ |
| 2026-07-20T07:20 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 3:10AM-3:15AM ET… | ✅ WIN | +1.96$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T07:28 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,006.25 | 0.1min |  |
| ✅ ETH | $1,854.37 | 0.1min |  |
| ✅ SOL | $75.94 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,010.30 | consenso |  |
| ETH | $1,854.37 | consenso |  |
| SOL | $75.80 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*