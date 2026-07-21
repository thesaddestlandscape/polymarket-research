# Estado del bot — 2026-07-21 09:20 UTC

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
| P&L fiel (stake fijo 1$) | +3353.68 $ |
| P&L sim compuesto | 🟢 +6272.30 $ (ficción Kelly: +24655% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -143.18 $ |
| Operaciones resueltas | 26423 (15957 WIN / 10466 LOSS) — 60.4% |
| Señales abiertas | 121 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6451 | 60.1% | +0.101 | ➡️ estable | +2116.64$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3647 | 64.0% | +0.140 | ➡️ estable | +2051.47$ | 1.40$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3624 | 59.1% | +0.091 | ➡️ estable | +1217.55$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 959 | 66.9% | +0.169 | 📉 agota (-0.03) | +439.02$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2045 | 52.7% | +0.027 | 📈 madura (+0.11) | +167.92$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 206 | 63.6% | +0.135 | ➡️ estable | +104.32$ | 1.35$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4565 | 68.6% | +0.186 | ➡️ estable | +71.00$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 236 | 53.0% | +0.029 | 📉 agota (-0.09) | +20.74$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 561 | 62.9% | +0.129 | 📉 agota (-0.03) | +17.45$ | 1.29$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 100 | 79.0% | +0.284 | ➡️ estable | +16.34$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 160 | 54.4% | +0.043 | 📉 agota (-0.26) | +13.26$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 247 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.27$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 215 | 81.9% | +0.316 | ➡️ estable | +11.52$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
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
| 2026-07-21T09:18 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 5:05AM-5:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T09:16 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 5:00AM-5:05AM ET… | ✅ WIN | +0.50$ |
| 2026-07-21T09:10 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 4:55AM-5:00AM ET… | ✅ WIN | +0.50$ |
| 2026-07-21T09:10 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 21, 4AM ET… | ✅ WIN | +1.38$ |
| 2026-07-21T09:07 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 4:45AM-5:00AM ET… | ✅ WIN | +0.72$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T09:18 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,164.13 | 0.1min |  |
| ✅ ETH | $1,938.97 | 0.1min |  |
| ✅ SOL | $78.25 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,164.13 | consenso |  |
| ETH | $1,938.97 | consenso |  |
| SOL | $78.20 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*