# Estado del bot — 2026-07-24 01:32 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3673.34 $ |
| P&L sim compuesto | 🟢 +6989.18 $ (ficción Kelly: +27473% s/ operativo) |
| P&L sim hoy (2026-07-24) | 🟢 +14.81 $ |
| Operaciones resueltas | 32001 (19218 WIN / 12783 LOSS) — 60.1% |
| Señales abiertas | 126 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7279 | 59.6% | +0.096 | 📉 agota (-0.03) | +2263.00$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4474 | 62.4% | +0.124 | 📉 agota (-0.05) | +2214.80$ | 1.24$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4508 | 57.6% | +0.076 | 📉 agota (-0.04) | +1289.98$ | 0.76$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1454 | 66.2% | +0.162 | ➡️ estable | +667.37$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2402 | 53.2% | +0.032 | 📈 madura (+0.09) | +208.66$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 247 | 60.7% | +0.106 | 📉 agota (-0.07) | +112.24$ | 1.06$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5615 | 68.8% | +0.188 | ➡️ estable | +111.54$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 906 | 63.0% | +0.130 | ➡️ estable | +45.62$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 275 | 58.2% | +0.081 | 📉 agota (-0.05) | +31.20$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 138 | 80.4% | +0.300 | ➡️ estable | +28.45$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 306 | 82.0% | +0.318 | ➡️ estable | +18.05$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1661 | 51.2% | +0.012 | ➡️ estable | +12.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 266 | 50.8% | +0.007 | 📉 agota (-0.17) | +9.14$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 26 | 88.5% | +0.357 | — | +2.42$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LATE_WINDOW_5MIN | 350 | 45.1% | -0.048 | 📉 agota (-0.12) | -2.09$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| GBM_LATE_5M | 522 | 47.3% | -0.027 | 📉 agota (-0.03) | -4.69$ | 0.50$ | ⚠️ IC negativo |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-24T01:25 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 9:15PM-9:20PM ET… | ❌ LOSS | -0.75$ |
| 2026-07-24T01:22 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 23, 9:00PM-9:15PM ET… | ✅ WIN | +1.06$ |
| 2026-07-24T01:22 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 9:00PM-9:15PM ET… | ✅ WIN | +0.45$ |
| 2026-07-24T01:22 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 23, 9:00PM-9:15PM ET… | ✅ WIN | +0.92$ |
| 2026-07-24T01:22 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 23, 9:00PM-9:15PM ET… | ✅ WIN | +0.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-24T01:30 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,051.39 | 0.1min |  |
| ✅ ETH | $1,873.30 | 0.1min |  |
| ✅ SOL | $75.94 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,051.39 | consenso |  |
| ETH | $1,874.07 | consenso |  |
| SOL | $75.96 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*