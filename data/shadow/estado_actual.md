# Estado del bot — 2026-07-21 05:39 UTC

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
| P&L fiel (stake fijo 1$) | +3401.04 $ |
| P&L sim compuesto | 🟢 +6305.14 $ (ficción Kelly: +24784% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -110.34 $ |
| Operaciones resueltas | 26067 (15782 WIN / 10285 LOSS) — 60.5% |
| Señales abiertas | 115 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6395 | 60.3% | +0.103 | ➡️ estable | +2131.91$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3591 | 64.4% | +0.143 | ➡️ estable | +2075.59$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3572 | 59.4% | +0.094 | ➡️ estable | +1224.81$ | 0.94$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 927 | 67.3% | +0.173 | ➡️ estable | +432.49$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 2032 | 52.6% | +0.026 | 📈 madura (+0.12) | +156.94$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 204 | 63.7% | +0.136 | ➡️ estable | +104.36$ | 1.36$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4504 | 68.6% | +0.186 | ➡️ estable | +59.51$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 249 | 59.4% | +0.094 | 📉 agota (-0.04) | +37.12$ | 0.94$ | ✅ activa |
| GBM_LATE_5M | 228 | 54.8% | +0.048 | 📉 agota (-0.04) | +24.82$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 121 | 59.5% | +0.093 | 📉 agota (-0.27) | +20.18$ | 0.94$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 544 | 63.1% | +0.130 | 📉 agota (-0.03) | +19.12$ | 1.30$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 96 | 79.2% | +0.286 | 📉 agota (-0.08) | +15.96$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 242 | 52.1% | +0.020 | 📉 agota (-0.13) | +12.71$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 207 | 82.1% | +0.318 | ➡️ estable | +11.27$ | 2.00$ | ✅ activa |
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
| 2026-07-21T05:37 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 1:30AM-1:35AM ET… | ✅ WIN | +0.67$ |
| 2026-07-21T05:37 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 1:30AM-1:35AM ET… | ✅ WIN | +1.11$ |
| 2026-07-21T05:35 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 1:25AM-1:30AM ET… | ✅ WIN | +0.50$ |
| 2026-07-21T05:35 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 21, 1:15AM-1:30AM ET… | ✅ WIN | +0.14$ |
| 2026-07-21T05:35 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 1:15AM-1:30AM ET… | ✅ WIN | +0.10$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T05:37 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,548.27 | 0.1min |  |
| ✅ ETH | $1,923.81 | 0.1min |  |
| ✅ SOL | $78.44 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,549.00 | consenso |  |
| ETH | $1,923.81 | consenso |  |
| SOL | $78.39 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*