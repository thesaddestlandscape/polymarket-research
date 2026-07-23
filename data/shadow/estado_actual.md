# Estado del bot — 2026-07-23 19:50 UTC

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
| P&L fiel (stake fijo 1$) | +3630.44 $ |
| P&L sim compuesto | 🟢 +6913.03 $ (ficción Kelly: +27174% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +201.17 $ |
| Operaciones resueltas | 31548 (18941 WIN / 12607 LOSS) — 60.0% |
| Señales abiertas | 161 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7217 | 59.6% | +0.096 | 📉 agota (-0.04) | +2238.78$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4408 | 62.5% | +0.124 | 📉 agota (-0.05) | +2192.19$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4430 | 57.7% | +0.077 | 📉 agota (-0.03) | +1284.22$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1418 | 66.4% | +0.163 | ➡️ estable | +655.51$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2379 | 53.1% | +0.031 | 📈 madura (+0.10) | +205.72$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 245 | 60.8% | +0.107 | 📉 agota (-0.06) | +111.22$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5517 | 68.8% | +0.188 | ➡️ estable | +102.98$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 881 | 62.9% | +0.129 | ➡️ estable | +42.05$ | 1.29$ | ✅ activa |
| STREAK_FADE_15M | 271 | 58.7% | +0.086 | 📉 agota (-0.06) | +35.54$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | 79.9% | +0.294 | ➡️ estable | +25.87$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 296 | 82.4% | +0.322 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 482 | 47.5% | -0.025 | 📉 agota (-0.09) | -1.35$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-23T19:49 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 23, 3:30PM-3:45PM ET… | ✅ WIN | +0.41$ |
| 2026-07-23T19:49 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 23, 3:30PM-3:45PM ET… | ✅ WIN | +1.27$ |
| 2026-07-23T19:49 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 23, 3:30PM-3:45PM ET… | ✅ WIN | +1.53$ |
| 2026-07-23T19:49 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 3:30PM-3:45PM ET… | ✅ WIN | +1.96$ |
| 2026-07-23T19:49 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 23, 3:30PM-3:45PM ET… | ✅ WIN | +1.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T19:49 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,677.47 | 0.1min |  |
| ✅ ETH | $1,872.55 | 0.1min |  |
| ✅ SOL | $75.58 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,692.00 | consenso |  |
| ETH | $1,872.78 | consenso |  |
| SOL | $75.53 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*