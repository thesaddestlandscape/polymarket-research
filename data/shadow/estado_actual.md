# Estado del bot — 2026-07-21 08:06 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3356.93 $ |
| P&L sim compuesto | 🟢 +6268.86 $ (ficción Kelly: +24642% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -146.62 $ |
| Operaciones resueltas | 26313 (15894 WIN / 10419 LOSS) — 60.4% |
| Señales abiertas | 115 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6434 | 60.1% | +0.101 | ➡️ estable | +2117.20$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3630 | 64.0% | +0.140 | ➡️ estable | +2053.53$ | 1.40$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3607 | 59.2% | +0.092 | ➡️ estable | +1214.59$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 951 | 67.2% | +0.172 | ➡️ estable | +442.96$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 2042 | 52.7% | +0.027 | 📈 madura (+0.11) | +168.02$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 206 | 63.6% | +0.135 | ➡️ estable | +104.32$ | 1.35$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4543 | 68.5% | +0.185 | ➡️ estable | +58.34$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 236 | 53.0% | +0.029 | 📉 agota (-0.09) | +20.74$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 99 | 79.8% | +0.292 | 📉 agota (-0.03) | +18.38$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 554 | 62.8% | +0.128 | 📉 agota (-0.04) | +16.50$ | 1.28$ | ✅ activa |
| LATE_WINDOW_5MIN | 146 | 54.8% | +0.047 | 📉 agota (-0.24) | +15.32$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 246 | 52.0% | +0.020 | 📉 agota (-0.14) | +12.78$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 213 | 82.2% | +0.319 | ➡️ estable | +12.75$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 7 | 57.1% | +0.019 | — | +0.36$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T08:05 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 3:50AM-3:55AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T08:05 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 3:45AM-4:00AM ET… | ✅ WIN | +0.36$ |
| 2026-07-21T08:05 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 3:45AM-4:00AM ET… | ✅ WIN | +0.36$ |
| 2026-07-21T08:05 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 21, 3:45AM-4:00AM ET… | ✅ WIN | +0.36$ |
| 2026-07-21T08:05 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 3:45AM-4:00AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T08:04 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,980.01 | 0.1min |  |
| ✅ ETH | $1,933.16 | 0.1min |  |
| ✅ SOL | $78.61 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,980.01 | consenso |  |
| ETH | $1,933.16 | consenso |  |
| SOL | $78.43 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*