# Estado del bot — 2026-07-21 21:13 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.65 $** |
| P&L real total | 🔴 **-26.57 $** |
| P&L real hoy | -1.12 $ |
| P&L real 7 días | -10.37 $ |
| Fees pagados (real) | 9.02 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3337.64 $ |
| P&L sim compuesto | 🟢 +6319.72 $ (ficción Kelly: +24842% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -95.77 $ |
| Operaciones resueltas | 27532 (16554 WIN / 10978 LOSS) — 60.1% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6630 | 59.9% | +0.099 | ➡️ estable | +2129.00$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3826 | 63.4% | +0.134 | 📉 agota (-0.03) | +2062.49$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3797 | 58.7% | +0.087 | ➡️ estable | +1225.32$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1047 | 66.7% | +0.166 | 📉 agota (-0.03) | +470.87$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2086 | 52.6% | +0.026 | 📈 madura (+0.11) | +168.13$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4754 | 68.5% | +0.185 | ➡️ estable | +68.22$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 257 | 58.0% | +0.079 | 📉 agota (-0.09) | +28.03$ | 0.79$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 643 | 62.7% | +0.126 | 📉 agota (-0.05) | +20.10$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 107 | 79.4% | +0.289 | ➡️ estable | +20.07$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 260 | 49.2% | -0.008 | 📉 agota (-0.12) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 234 | 81.6% | +0.314 | ➡️ estable | +10.90$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 243 | 47.3% | -0.027 | 📉 agota (-0.24) | +0.48$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 10 | 70.0% | +0.083 | — | -2.01$ | 0.83$ | ✅ activa |
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
| 2026-07-21T21:11 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 4PM ET… | ✅ WIN | +1.16$ |
| 2026-07-21T21:08 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 21, 4:45PM-5:00PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T21:08 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 21, 4PM ET… | ✅ WIN | +0.76$ |
| 2026-07-21T21:08 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 21, 4PM ET… | ✅ WIN | +1.38$ |
| 2026-07-21T21:04 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 4:50PM-4:55PM ET… | ❌ LOSS | -0.57$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T21:11 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,320.29 | 0.1min |  |
| ✅ ETH | $1,921.33 | 0.1min |  |
| ✅ SOL | $78.01 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,321.50 | consenso |  |
| ETH | $1,921.33 | consenso |  |
| SOL | $77.90 | consenso |  |
| XRP | $1.15 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*