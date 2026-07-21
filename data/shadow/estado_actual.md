# Estado del bot — 2026-07-21 13:28 UTC

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
| P&L fiel (stake fijo 1$) | +3270.68 $ |
| P&L sim compuesto | 🟢 +6212.92 $ (ficción Kelly: +24422% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -202.56 $ |
| Operaciones resueltas | 26827 (16134 WIN / 10693 LOSS) — 60.1% |
| Señales abiertas | 112 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6519 | 59.9% | +0.099 | ➡️ estable | +2105.22$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3715 | 63.5% | +0.135 | 📉 agota (-0.04) | +2026.33$ | 1.35$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3692 | 58.8% | +0.088 | ➡️ estable | +1208.56$ | 0.88$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 976 | 66.9% | +0.169 | 📉 agota (-0.03) | +445.95$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2055 | 52.7% | +0.026 | 📈 madura (+0.11) | +168.15$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4629 | 68.6% | +0.186 | ➡️ estable | +76.61$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 248 | 50.4% | +0.004 | 📉 agota (-0.13) | +14.62$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 249 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.30$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 589 | 62.0% | +0.119 | 📉 agota (-0.05) | +10.91$ | 1.19$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 222 | 81.5% | +0.312 | ➡️ estable | +10.71$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 205 | 50.2% | +0.002 | 📉 agota (-0.21) | +7.31$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
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
| 2026-07-21T13:22 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 21, 9:00AM-9:15AM ET… | ✅ WIN | +0.30$ |
| 2026-07-21T13:22 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 9:00AM-9:15AM ET… | ✅ WIN | +0.27$ |
| 2026-07-21T13:22 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 21, 9:00AM-9:15AM ET… | ❌ LOSS | -0.87$ |
| 2026-07-21T13:22 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 9:00AM-9:15AM ET… | ❌ LOSS | -2.00$ |
| 2026-07-21T13:22 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 9:00AM-9:15AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T13:27 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,404.99 | 0.1min |  |
| ✅ ETH | $1,936.07 | 0.1min |  |
| ✅ SOL | $78.35 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,406.00 | consenso |  |
| ETH | $1,936.07 | consenso |  |
| SOL | $78.33 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*