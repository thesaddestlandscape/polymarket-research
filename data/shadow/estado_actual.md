# Estado del bot — 2026-07-21 19:31 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.53 $** |
| P&L real total | 🔴 **-27.69 $** |
| P&L real hoy | -4.91 $ |
| P&L real 7 días | -14.16 $ |
| Fees pagados (real) | 8.95 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3302.55 $ |
| P&L sim compuesto | 🟢 +6244.78 $ (ficción Kelly: +24547% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -170.70 $ |
| Operaciones resueltas | 27371 (16442 WIN / 10929 LOSS) — 60.1% |
| Señales abiertas | 125 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6604 | 59.9% | +0.099 | ➡️ estable | +2114.57$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3801 | 63.4% | +0.134 | 📉 agota (-0.04) | +2047.12$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3772 | 58.7% | +0.087 | ➡️ estable | +1214.78$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1026 | 66.7% | +0.166 | ➡️ estable | +460.96$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2079 | 52.5% | +0.025 | 📈 madura (+0.11) | +163.28$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4724 | 68.4% | +0.184 | ➡️ estable | +54.37$ | 1.84$ | ✅ activa |
| STREAK_FADE_15M | 256 | 58.2% | +0.081 | 📉 agota (-0.08) | +29.43$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 105 | 79.0% | +0.285 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 257 | 49.8% | -0.002 | 📉 agota (-0.13) | +15.77$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_CONFIRMADAS_15M | 632 | 62.2% | +0.121 | 📉 agota (-0.06) | +11.38$ | 1.21$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 231 | 81.4% | +0.311 | ➡️ estable | +9.32$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 236 | 48.3% | -0.017 | 📉 agota (-0.22) | +3.15$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-21T19:27 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 21, 3:00PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T19:27 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 3:00PM-3:15PM ET… | ❌ LOSS | -1.89$ |
| 2026-07-21T19:27 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 21, 3:00PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T19:27 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 3:00PM-3:15PM ET… | ✅ WIN | +0.69$ |
| 2026-07-21T19:27 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 21, 3:00PM-3:15PM ET… | ✅ WIN | +2.40$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T19:30 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,367.52 | 0.1min |  |
| ✅ ETH | $1,923.19 | 0.1min |  |
| ✅ SOL | $77.92 | 0.1min |  |
| ✅ XRP | $1.16 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,369.90 | consenso |  |
| ETH | $1,923.19 | consenso |  |
| SOL | $77.85 | consenso |  |
| XRP | $1.16 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*