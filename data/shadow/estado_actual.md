# Estado del bot — 2026-07-22 19:33 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.26 $** |
| P&L real total | 🔴 **-23.96 $** |
| P&L real hoy | +4.67 $ |
| P&L real 7 días | -4.92 $ |
| Fees pagados (real) | 9.54 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3553.82 $ |
| P&L sim compuesto | 🟢 +6707.15 $ (ficción Kelly: +26365% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +343.64 $ |
| Operaciones resueltas | 29437 (17719 WIN / 11718 LOSS) — 60.2% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6911 | 59.7% | +0.097 | ➡️ estable | +2188.25$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4111 | 63.1% | +0.131 | 📉 agota (-0.04) | +2169.42$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4104 | 58.4% | +0.084 | ➡️ estable | +1274.92$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1230 | 66.5% | +0.165 | 📉 agota (-0.04) | +565.97$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2213 | 53.1% | +0.031 | 📈 madura (+0.11) | +194.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 231 | 61.9% | +0.118 | 📉 agota (-0.05) | +111.25$ | 1.18$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5121 | 68.8% | +0.187 | ➡️ estable | +91.64$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 775 | 63.0% | +0.129 | ➡️ estable | +38.16$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 264 | 58.3% | +0.083 | 📉 agota (-0.07) | +31.16$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 266 | 82.3% | +0.321 | ➡️ estable | +17.26$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 262 | 50.8% | +0.008 | 📉 agota (-0.17) | +9.12$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 288 | 48.3% | -0.017 | 📉 agota (-0.13) | +6.52$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 16 | 81.2% | +0.222 | — | -0.59$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 323 | 45.5% | -0.045 | 📉 agota (-0.17) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 317 | 44.2% | -0.058 | 📉 agota (-0.09) | -25.33$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T19:19 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 22, 3:00PM-3:15PM ET… | ✅ WIN | +2.17$ |
| 2026-07-22T19:19 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 3:00PM-3:15PM ET… | ✅ WIN | +0.25$ |
| 2026-07-22T19:19 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 22, 3:00PM-3:15PM ET… | ✅ WIN | +0.10$ |
| 2026-07-22T19:19 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 3:00PM-3:15PM ET… | ✅ WIN | +0.36$ |
| 2026-07-22T19:19 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 3:00PM-3:15PM ET… | ✅ WIN | +1.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T19:31 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,868.37 | 0.1min |  |
| ✅ ETH | $1,926.71 | 0.1min |  |
| ✅ SOL | $77.71 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,868.37 | consenso |  |
| ETH | $1,926.71 | consenso |  |
| SOL | $77.61 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*