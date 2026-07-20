# Estado del bot — 2026-07-20 21:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -13.66 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3424.43 $ |
| P&L sim compuesto | 🟢 +6348.97 $ (ficción Kelly: +24957% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +350.65 $ |
| Operaciones resueltas | 25307 (15375 WIN / 9932 LOSS) — 60.8% |
| Señales abiertas | 147 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6274 | 60.6% | +0.106 | ➡️ estable | +2162.33$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3479 | 65.1% | +0.151 | ➡️ estable | +2121.91$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3461 | 59.9% | +0.099 | 📈 madura (+0.03) | +1246.26$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 854 | 66.6% | +0.166 | 📉 agota (-0.03) | +374.79$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 1983 | 52.2% | +0.022 | 📈 madura (+0.11) | +139.70$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 192 | 65.6% | +0.155 | 📈 madura (+0.08) | +105.61$ | 1.55$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4381 | 68.6% | +0.186 | ➡️ estable | +69.09$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 238 | 60.1% | +0.100 | ➡️ estable | +40.35$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 76 | 68.4% | +0.179 | 📉 agota (-0.05) | +28.48$ | 1.79$ | ✅ activa |
| GBM_LATE_5M | 215 | 56.3% | +0.062 | ➡️ estable | +20.66$ | 0.62$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 493 | 63.5% | +0.134 | ➡️ estable | +18.12$ | 1.34$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 90 | 80.0% | +0.293 | 📉 agota (-0.04) | +17.49$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 232 | 52.2% | +0.021 | 📉 agota (-0.14) | +13.49$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 194 | 82.5% | +0.321 | ➡️ estable | +11.08$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 2 | 100.0% | +0.025 | — | +0.38$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-20T21:56 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 5:45PM-5:50PM ET… | ✅ WIN | +1.09$ |
| 2026-07-20T21:50 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 5:40PM-5:45PM ET… | ✅ WIN | +0.53$ |
| 2026-07-20T21:50 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 5:30PM-5:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T21:50 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 20, 5:30PM-5:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T21:50 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 20, 5:30PM-5:45PM ET… | ✅ WIN | +1.01$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T21:56 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,262.60 | 0.1min |  |
| ✅ ETH | $1,901.91 | 0.1min |  |
| ✅ SOL | $77.78 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,268.80 | consenso |  |
| ETH | $1,902.00 | consenso |  |
| SOL | $77.76 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*