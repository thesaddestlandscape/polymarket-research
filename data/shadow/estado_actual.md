# Estado del bot — 2026-07-21 11:44 UTC

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
| P&L fiel (stake fijo 1$) | +3360.78 $ |
| P&L sim compuesto | 🟢 +6314.62 $ (ficción Kelly: +24822% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -100.86 $ |
| Operaciones resueltas | 26636 (16075 WIN / 10561 LOSS) — 60.4% |
| Señales abiertas | 118 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6491 | 60.1% | +0.101 | ➡️ estable | +2134.07$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3687 | 63.9% | +0.139 | ➡️ estable | +2068.62$ | 1.39$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3664 | 59.1% | +0.091 | ➡️ estable | +1230.49$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 960 | 67.0% | +0.169 | 📉 agota (-0.03) | +440.83$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2046 | 52.7% | +0.027 | 📈 madura (+0.11) | +168.93$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 211 | 62.6% | +0.124 | ➡️ estable | +101.12$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4598 | 68.7% | +0.187 | ➡️ estable | +80.53$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 253 | 58.5% | +0.084 | 📉 agota (-0.07) | +30.08$ | 0.84$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 572 | 62.9% | +0.129 | ➡️ estable | +17.33$ | 1.29$ | ✅ activa |
| GBM_LATE_5M | 244 | 51.2% | +0.012 | 📉 agota (-0.10) | +16.66$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 100 | 79.0% | +0.284 | ➡️ estable | +16.34$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 248 | 51.6% | +0.016 | 📉 agota (-0.16) | +11.76$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 217 | 81.6% | +0.313 | ➡️ estable | +10.41$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 188 | 52.1% | +0.021 | 📉 agota (-0.21) | +10.25$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
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
| 2026-07-21T11:40 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 7:30AM-7:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T11:37 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 7:25AM-7:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T11:37 | STREAK_FADE_15M#ETH#15min | Ethereum Up or Down - July 21, 7:15AM-7:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T11:37 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 7:15AM-7:30AM ET… | ✅ WIN | +0.92$ |
| 2026-07-21T11:37 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 7:15AM-7:30AM ET… | ✅ WIN | +0.60$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T11:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,279.85 | 0.1min |  |
| ✅ ETH | $1,932.48 | 0.1min |  |
| ✅ SOL | $78.36 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,282.30 | consenso |  |
| ETH | $1,932.80 | consenso |  |
| SOL | $78.30 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*