# Estado del bot — 2026-07-21 22:13 UTC

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
| P&L fiel (stake fijo 1$) | +3339.02 $ |
| P&L sim compuesto | 🟢 +6337.08 $ (ficción Kelly: +24910% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -78.40 $ |
| Operaciones resueltas | 27628 (16607 WIN / 11021 LOSS) — 60.1% |
| Señales abiertas | 123 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6645 | 59.9% | +0.099 | ➡️ estable | +2130.28$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3841 | 63.4% | +0.134 | 📉 agota (-0.04) | +2060.39$ | 1.34$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3810 | 58.7% | +0.087 | ➡️ estable | +1235.21$ | 0.87$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1060 | 66.5% | +0.165 | 📉 agota (-0.03) | +472.39$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2093 | 52.7% | +0.026 | 📈 madura (+0.11) | +168.64$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 217 | 61.8% | +0.116 | 📉 agota (-0.04) | +104.09$ | 1.16$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4768 | 68.5% | +0.185 | ➡️ estable | +67.85$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 259 | 57.9% | +0.079 | 📉 agota (-0.08) | +27.80$ | 0.79$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 651 | 62.7% | +0.126 | 📉 agota (-0.06) | +24.50$ | 1.26$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 109 | 79.8% | +0.293 | 📈 madura (+0.04) | +22.23$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 261 | 49.0% | -0.010 | 📉 agota (-0.12) | +13.73$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 235 | 81.7% | +0.314 | ➡️ estable | +11.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 254 | 51.2% | +0.012 | 📉 agota (-0.16) | +10.81$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| LATE_WINDOW_5MIN | 247 | 47.0% | -0.030 | 📉 agota (-0.24) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 11 | 72.7% | +0.106 | — | -1.83$ | 1.06$ | ✅ activa |
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
| 2026-07-21T22:09 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 6:00PM-6:05PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T22:09 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 21, 6:00PM-6:05PM ET… | ✅ WIN | +0.33$ |
| 2026-07-21T22:09 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 5:45PM-6:00PM ET… | ✅ WIN | +1.27$ |
| 2026-07-21T22:09 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 21, 5:45PM-6:00PM ET… | ❌ LOSS | -1.76$ |
| 2026-07-21T22:09 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 5:45PM-6:00PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T22:12 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,272.66 | 0.1min |  |
| ✅ ETH | $1,920.77 | 0.1min |  |
| ✅ SOL | $78.05 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,278.60 | consenso |  |
| ETH | $1,920.93 | consenso |  |
| SOL | $77.97 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*