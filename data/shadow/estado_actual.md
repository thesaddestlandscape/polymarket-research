# Estado del bot — 2026-07-22 19:45 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.63 $** |
| P&L real total | 🔴 **-23.59 $** |
| P&L real hoy | +5.12 $ |
| P&L real 7 días | -4.47 $ |
| Fees pagados (real) | 9.56 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3552.87 $ |
| P&L sim compuesto | 🟢 +6712.40 $ (ficción Kelly: +26385% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +348.89 $ |
| Operaciones resueltas | 29460 (17734 WIN / 11726 LOSS) — 60.2% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6915 | 59.8% | +0.098 | ➡️ estable | +2194.50$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4115 | 63.1% | +0.131 | 📉 agota (-0.04) | +2169.63$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4107 | 58.3% | +0.083 | ➡️ estable | +1275.71$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1231 | 66.5% | +0.165 | 📉 agota (-0.04) | +566.22$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2217 | 53.1% | +0.031 | 📈 madura (+0.11) | +191.58$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 232 | 61.6% | +0.115 | 📉 agota (-0.06) | +110.74$ | 1.15$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5124 | 68.8% | +0.188 | ➡️ estable | +92.36$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 776 | 63.0% | +0.130 | ➡️ estable | +38.49$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 264 | 58.3% | +0.083 | 📉 agota (-0.07) | +31.16$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 120 | 79.2% | +0.287 | ➡️ estable | +20.40$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 267 | 82.4% | +0.322 | ➡️ estable | +17.38$ | 2.00$ | ✅ activa |
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
| 2026-07-22T19:38 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 22, 3:15PM-3:30PM ET… | ❌ LOSS | -1.34$ |
| 2026-07-22T19:34 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 3:15PM-3:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T19:34 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 3:15PM-3:30PM ET… | ✅ WIN | +0.33$ |
| 2026-07-22T19:34 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 22, 3:15PM-3:30PM ET… | ✅ WIN | +0.27$ |
| 2026-07-22T19:34 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 3:15PM-3:30PM ET… | ✅ WIN | +0.25$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T19:43 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,876.31 | 0.1min |  |
| ✅ ETH | $1,925.18 | 0.1min |  |
| ✅ SOL | $77.61 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,876.31 | consenso |  |
| ETH | $1,925.97 | consenso |  |
| SOL | $77.58 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*