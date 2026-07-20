# Estado del bot — 2026-07-20 23:38 UTC

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
| P&L fiel (stake fijo 1$) | +3465.34 $ |
| P&L sim compuesto | 🟢 +6411.32 $ (ficción Kelly: +25202% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +412.99 $ |
| Operaciones resueltas | 25483 (15495 WIN / 9988 LOSS) — 60.8% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6301 | 60.6% | +0.106 | ➡️ estable | +2165.76$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3506 | 65.0% | +0.150 | ➡️ estable | +2122.00$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3484 | 59.9% | +0.099 | 📈 madura (+0.03) | +1251.03$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 878 | 67.4% | +0.174 | ➡️ estable | +408.52$ | 1.74$ | ✅ activa |
| UPDOWN_GBM | 2004 | 52.3% | +0.023 | 📈 madura (+0.12) | +146.57$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 198 | 65.2% | +0.150 | 📈 madura (+0.05) | +106.48$ | 1.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4408 | 68.7% | +0.187 | ➡️ estable | +78.12$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 241 | 59.8% | +0.097 | 📉 agota (-0.04) | +37.56$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| GBM_LATE_5M | 218 | 56.0% | +0.059 | ➡️ estable | +21.18$ | 0.59$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 503 | 63.6% | +0.136 | ➡️ estable | +20.38$ | 1.36$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 90 | 80.0% | +0.293 | 📉 agota (-0.04) | +17.49$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 232 | 52.2% | +0.021 | 📉 agota (-0.14) | +13.49$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 196 | 82.7% | +0.323 | ➡️ estable | +12.05$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 3 | 100.0% | +0.045 | — | +0.51$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-20T23:34 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 20, 7:15PM-7:30PM ET… | ✅ WIN | +1.27$ |
| 2026-07-20T23:34 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 20, 7:15PM-7:30PM ET… | ❌ LOSS | -1.07$ |
| 2026-07-20T23:31 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 20, 7:20PM-7:25PM ET… | ✅ WIN | +0.62$ |
| 2026-07-20T23:31 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 7:15PM-7:30PM ET… | ✅ WIN | +0.10$ |
| 2026-07-20T23:31 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 20, 7:15PM-7:30PM ET… | ✅ WIN | +0.10$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T23:36 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,177.28 | 0.1min |  |
| ✅ ETH | $1,901.93 | 0.1min |  |
| ✅ SOL | $77.72 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,178.10 | consenso |  |
| ETH | $1,901.93 | consenso |  |
| SOL | $77.64 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*