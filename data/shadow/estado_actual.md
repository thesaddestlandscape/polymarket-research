# Estado del bot — 2026-07-21 03:57 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3416.17 $ |
| P&L sim compuesto | 🟢 +6333.15 $ (ficción Kelly: +24894% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -82.34 $ |
| Operaciones resueltas | 25885 (15693 WIN / 10192 LOSS) — 60.6% |
| Señales abiertas | 116 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6367 | 60.4% | +0.104 | ➡️ estable | +2141.38$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3563 | 64.6% | +0.145 | ➡️ estable | +2087.17$ | 1.45$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3546 | 59.5% | +0.095 | ➡️ estable | +1236.42$ | 0.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 910 | 67.4% | +0.173 | ➡️ estable | +423.21$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 2023 | 52.4% | +0.024 | 📈 madura (+0.12) | +151.96$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 202 | 63.9% | +0.137 | ➡️ estable | +101.38$ | 1.37$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4477 | 68.7% | +0.187 | ➡️ estable | +70.19$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 244 | 59.8% | +0.098 | 📉 agota (-0.03) | +39.16$ | 0.98$ | ✅ activa |
| GBM_LATE_5M | 225 | 55.1% | +0.051 | 📉 agota (-0.04) | +24.39$ | 0.51$ | ✅ activa |
| LATE_WINDOW_5MIN | 101 | 61.4% | +0.112 | 📉 agota (-0.24) | +20.79$ | 1.12$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 537 | 62.8% | +0.127 | 📉 agota (-0.04) | +16.72$ | 1.27$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 95 | 78.9% | +0.284 | 📉 agota (-0.08) | +15.82$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 240 | 52.5% | +0.025 | 📉 agota (-0.11) | +13.83$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1640 | 51.2% | +0.012 | ➡️ estable | +12.16$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 204 | 82.4% | +0.320 | ➡️ estable | +11.55$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T03:56 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 11:45PM-11:50PM ET… | ✅ WIN | +0.39$ |
| 2026-07-21T03:53 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 20, 11:45PM-11:50PM ET… | ✅ WIN | +1.36$ |
| 2026-07-21T03:48 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 11:40PM-11:45PM ET… | ❌ LOSS | -0.78$ |
| 2026-07-21T03:48 | BALLENAS_TARDIAS#BTC#15min | … | ✅ WIN | +0.21$ |
| 2026-07-21T03:48 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 11:30PM-11:45PM ET… | ✅ WIN | +0.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T03:56 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,488.78 | 0.1min |  |
| ✅ ETH | $1,925.17 | 0.1min |  |
| ✅ SOL | $78.18 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,488.78 | consenso |  |
| ETH | $1,925.39 | consenso |  |
| SOL | $78.18 | consenso |  |
| XRP | $1.12 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*