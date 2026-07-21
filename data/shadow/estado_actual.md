# Estado del bot — 2026-07-21 21:37 UTC

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
| P&L fiel (stake fijo 1$) | +3344.59 $ |
| P&L sim compuesto | 🟢 +6335.95 $ (ficción Kelly: +24905% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -79.53 $ |
| Operaciones resueltas | 27574 (16579 WIN / 10995 LOSS) — 60.1% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6637 | 59.9% | +0.099 | ➡️ estable | +2130.81$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3833 | 63.4% | +0.134 | 📉 agota (-0.03) | +2064.26$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3802 | 58.7% | +0.087 | ➡️ estable | +1234.77$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1053 | 66.6% | +0.165 | ➡️ estable | +470.52$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2089 | 52.7% | +0.027 | 📈 madura (+0.11) | +169.17$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4759 | 68.5% | +0.185 | ➡️ estable | +66.16$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 258 | 57.8% | +0.077 | 📉 agota (-0.08) | +26.71$ | 0.77$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 647 | 62.8% | +0.127 | 📉 agota (-0.05) | +24.83$ | 1.27$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 108 | 79.6% | +0.291 | 📈 madura (+0.04) | +21.35$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 260 | 49.2% | -0.008 | 📉 agota (-0.12) | +14.24$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 235 | 81.7% | +0.314 | ➡️ estable | +11.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 245 | 46.9% | -0.030 | 📉 agota (-0.25) | -0.54$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T21:36 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 5:25PM-5:30PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T21:36 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 5:20PM-5:25PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T21:36 | BALLENAS_CONFIRMADAS_15M#DOGE#15min | Dogecoin Up or Down - July 21, 5:15PM-5:30PM ET… | ✅ WIN | +0.49$ |
| 2026-07-21T21:36 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 5:15PM-5:30PM ET… | ✅ WIN | +1.50$ |
| 2026-07-21T21:36 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 21, 5:15PM-5:30PM ET… | ✅ WIN | +1.27$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T21:35 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,249.99 | 0.1min |  |
| ✅ ETH | $1,923.82 | 0.1min |  |
| ✅ SOL | $78.07 | 0.1min |  |
| ✅ XRP | $1.15 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,252.10 | consenso |  |
| ETH | $1,923.82 | consenso |  |
| SOL | $77.99 | consenso |  |
| XRP | $1.15 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*