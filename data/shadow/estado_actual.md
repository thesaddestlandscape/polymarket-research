# Estado del bot — 2026-07-23 09:54 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **30.16 $** |
| P&L real total | 🔴 **-21.06 $** |
| P&L real hoy | +0.93 $ |
| P&L real 7 días | +0.02 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3638.93 $ |
| P&L sim compuesto | 🟢 +6900.79 $ (ficción Kelly: +27126% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +188.93 $ |
| Operaciones resueltas | 30660 (18448 WIN / 12212 LOSS) — 60.2% |
| Señales abiertas | 151 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7095 | 59.7% | +0.097 | 📉 agota (-0.03) | +2232.46$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4293 | 62.7% | +0.127 | 📉 agota (-0.04) | +2194.19$ | 1.27$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4303 | 58.1% | +0.081 | ➡️ estable | +1308.34$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1350 | 66.6% | +0.166 | ➡️ estable | +628.40$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2316 | 53.2% | +0.031 | 📈 madura (+0.11) | +205.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 241 | 61.0% | +0.109 | 📉 agota (-0.06) | +110.91$ | 1.09$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5354 | 68.8% | +0.188 | ➡️ estable | +97.44$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 844 | 62.9% | +0.129 | ➡️ estable | +38.71$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 286 | 82.2% | +0.319 | ➡️ estable | +17.38$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 341 | 48.7% | -0.013 | 📉 agota (-0.19) | +10.09$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 24 | 87.5% | +0.346 | — | +1.67$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 336 | 44.9% | -0.050 | 📉 agota (-0.16) | -4.47$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 319 | 44.2% | -0.058 | 📉 agota (-0.08) | -25.29$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T09:53 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 23, 5:30AM-5:45AM ET… | ❌ LOSS | -1.47$ |
| 2026-07-23T09:53 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 23, 5:30AM-5:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T09:53 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 23, 5:30AM-5:45AM ET… | ❌ LOSS | -0.54$ |
| 2026-07-23T09:50 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 23, 5:30AM-5:45AM ET… | ✅ WIN | +0.75$ |
| 2026-07-23T09:37 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 5:15AM-5:30AM ET… | ❌ LOSS | -1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T09:52 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,646.51 | 0.1min |  |
| ✅ ETH | $1,925.49 | 0.1min |  |
| ✅ SOL | $77.53 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,650.00 | consenso |  |
| ETH | $1,925.61 | consenso |  |
| SOL | $77.49 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*