# Estado del bot — 2026-07-23 15:56 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| P&L real hoy | -2.32 $ |
| P&L real 7 días | -3.23 $ |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3588.58 $ |
| P&L sim compuesto | 🟢 +6827.83 $ (ficción Kelly: +26839% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +115.97 $ |
| Operaciones resueltas | 31181 (18708 WIN / 12473 LOSS) — 60.0% |
| Señales abiertas | 170 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7165 | 59.5% | +0.095 | 📉 agota (-0.04) | +2205.29$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4359 | 62.4% | +0.124 | 📉 agota (-0.04) | +2165.74$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4375 | 57.7% | +0.077 | ➡️ estable | +1267.20$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1391 | 66.5% | +0.165 | 📉 agota (-0.03) | +647.26$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2351 | 53.2% | +0.032 | 📈 madura (+0.11) | +207.69$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5453 | 68.8% | +0.188 | ➡️ estable | +109.39$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 865 | 62.8% | +0.127 | ➡️ estable | +41.84$ | 1.26$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 292 | 82.2% | +0.320 | ➡️ estable | +18.02$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 435 | 47.1% | -0.029 | 📉 agota (-0.18) | -2.24$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 348 | 44.8% | -0.051 | 📉 agota (-0.14) | -4.38$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T15:47 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:35AM-11:40AM ET… | ✅ WIN | +0.49$ |
| 2026-07-23T15:47 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 11:35AM-11:40AM ET… | ✅ WIN | +1.48$ |
| 2026-07-23T15:47 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:30AM-11:35AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T15:37 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 23, 11:25AM-11:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T15:37 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 11:25AM-11:30AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T15:47 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,848.12 | 0.1min |  |
| ✅ ETH | $1,889.89 | 0.1min |  |
| ✅ SOL | $76.26 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,861.70 | consenso |  |
| ETH | $1,889.89 | consenso |  |
| SOL | $76.23 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*