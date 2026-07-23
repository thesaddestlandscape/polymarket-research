# Estado del bot — 2026-07-23 20:23 UTC

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
| P&L fiel (stake fijo 1$) | +3633.79 $ |
| P&L sim compuesto | 🟢 +6913.92 $ (ficción Kelly: +27177% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +202.07 $ |
| Operaciones resueltas | 31590 (18964 WIN / 12626 LOSS) — 60.0% |
| Señales abiertas | 172 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7223 | 59.6% | +0.096 | 📉 agota (-0.04) | +2242.55$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4413 | 62.5% | +0.124 | 📉 agota (-0.05) | +2193.43$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4436 | 57.7% | +0.077 | 📉 agota (-0.03) | +1286.72$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1422 | 66.3% | +0.163 | ➡️ estable | +656.67$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2382 | 53.1% | +0.031 | 📈 madura (+0.10) | +206.04$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 245 | 60.8% | +0.107 | 📉 agota (-0.06) | +111.22$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5527 | 68.8% | +0.187 | ➡️ estable | +95.35$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 883 | 62.9% | +0.128 | ➡️ estable | +41.93$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | 79.9% | +0.294 | ➡️ estable | +25.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 297 | 82.2% | +0.319 | ➡️ estable | +18.09$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 487 | 47.6% | -0.024 | 📉 agota (-0.08) | +0.33$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-23T20:16 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 4:05PM-4:10PM ET… | ✅ WIN | +1.06$ |
| 2026-07-23T20:16 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 4:00PM-4:05PM ET… | ✅ WIN | +1.06$ |
| 2026-07-23T20:12 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 3:45PM-4:00PM ET… | ✅ WIN | +0.23$ |
| 2026-07-23T20:12 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 3:45PM-4:00PM ET… | ✅ WIN | +0.92$ |
| 2026-07-23T20:12 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 23, 3:45PM-4:00PM ET… | ✅ WIN | +1.77$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T20:21 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,090.10 | 0.1min |  |
| ✅ ETH | $1,885.10 | 0.1min |  |
| ✅ SOL | $76.10 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,090.10 | consenso |  |
| ETH | $1,885.21 | consenso |  |
| SOL | $76.06 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*