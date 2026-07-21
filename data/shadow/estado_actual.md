# Estado del bot — 2026-07-21 06:44 UTC

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
| P&L fiel (stake fijo 1$) | +3372.72 $ |
| P&L sim compuesto | 🟢 +6275.44 $ (ficción Kelly: +24668% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -140.04 $ |
| Operaciones resueltas | 26166 (15820 WIN / 10346 LOSS) — 60.5% |
| Señales abiertas | 113 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6411 | 60.2% | +0.102 | ➡️ estable | +2124.23$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3607 | 64.2% | +0.142 | ➡️ estable | +2062.94$ | 1.42$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3586 | 59.3% | +0.093 | ➡️ estable | +1219.22$ | 0.93$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 936 | 67.3% | +0.173 | 📉 agota (-0.03) | +435.46$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 2035 | 52.6% | +0.026 | 📈 madura (+0.12) | +161.36$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 204 | 63.7% | +0.136 | ➡️ estable | +104.36$ | 1.36$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4519 | 68.5% | +0.185 | ➡️ estable | +51.41$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 234 | 53.4% | +0.034 | 📉 agota (-0.08) | +21.76$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 547 | 63.1% | +0.130 | ➡️ estable | +19.66$ | 1.30$ | ✅ activa |
| LATE_WINDOW_5MIN | 131 | 57.3% | +0.071 | 📉 agota (-0.26) | +18.17$ | 0.71$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 98 | 79.6% | +0.290 | 📉 agota (-0.04) | +17.58$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 244 | 52.0% | +0.020 | 📉 agota (-0.14) | +12.72$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 209 | 82.3% | +0.320 | ➡️ estable | +12.63$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T06:43 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 2:35AM-2:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T06:43 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 2:35AM-2:40AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T06:40 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 2:30AM-2:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T06:38 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 2:25AM-2:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T06:35 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 21, 2:15AM-2:30AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T06:43 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,902.32 | 0.1min |  |
| ✅ ETH | $1,936.65 | 0.1min |  |
| ✅ SOL | $78.69 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,902.32 | consenso |  |
| ETH | $1,936.65 | consenso |  |
| SOL | $78.66 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*