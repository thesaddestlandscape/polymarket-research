# Estado del bot — 2026-07-20 22:14 UTC

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
| P&L fiel (stake fijo 1$) | +3443.59 $ |
| P&L sim compuesto | 🟢 +6375.78 $ (ficción Kelly: +25062% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +377.46 $ |
| Operaciones resueltas | 25333 (15399 WIN / 9934 LOSS) — 60.8% |
| Señales abiertas | 148 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6278 | 60.6% | +0.106 | ➡️ estable | +2168.22$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3482 | 65.1% | +0.151 | ➡️ estable | +2127.32$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3465 | 59.9% | +0.099 | 📈 madura (+0.03) | +1251.46$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 856 | 66.7% | +0.167 | 📉 agota (-0.03) | +377.79$ | 1.67$ | ✅ activa |
| UPDOWN_GBM | 1985 | 52.2% | +0.022 | 📈 madura (+0.12) | +141.19$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 192 | 65.6% | +0.155 | 📈 madura (+0.08) | +105.61$ | 1.55$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4387 | 68.6% | +0.186 | ➡️ estable | +70.25$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 238 | 60.1% | +0.100 | ➡️ estable | +40.35$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| GBM_LATE_5M | 215 | 56.3% | +0.062 | ➡️ estable | +20.66$ | 0.62$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 496 | 63.7% | +0.137 | ➡️ estable | +20.30$ | 1.37$ | ✅ activa |
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
| 2026-07-20T22:07 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 20, 5:45PM-6:00PM ET… | ✅ WIN | +2.17$ |
| 2026-07-20T22:07 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 20, 5:45PM-6:00PM ET… | ✅ WIN | +0.86$ |
| 2026-07-20T22:07 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 20, 5PM ET… | ✅ WIN | +1.02$ |
| 2026-07-20T22:04 | FAVORITO_CONFIRMADO#BTC#60min | Bitcoin Up or Down - July 20, 5PM ET… | ✅ WIN | +1.17$ |
| 2026-07-20T22:02 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 5:55PM-6:00PM ET… | ✅ WIN | +1.30$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T22:13 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,158.00 | 0.1min |  |
| ✅ ETH | $1,898.41 | 0.1min |  |
| ✅ SOL | $77.78 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,158.00 | consenso |  |
| ETH | $1,898.41 | consenso |  |
| SOL | $77.70 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*