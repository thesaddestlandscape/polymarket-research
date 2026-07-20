# Estado del bot — 2026-07-20 23:27 UTC

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
| P&L fiel (stake fijo 1$) | +3467.02 $ |
| P&L sim compuesto | 🟢 +6411.47 $ (ficción Kelly: +25202% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +413.15 $ |
| Operaciones resueltas | 25455 (15479 WIN / 9976 LOSS) — 60.8% |
| Señales abiertas | 153 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6297 | 60.6% | +0.106 | ➡️ estable | +2168.83$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3502 | 65.0% | +0.150 | ➡️ estable | +2126.26$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3481 | 59.9% | +0.099 | 📈 madura (+0.03) | +1251.74$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 872 | 67.2% | +0.172 | ➡️ estable | +400.16$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 2000 | 52.4% | +0.024 | 📈 madura (+0.12) | +149.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 197 | 65.0% | +0.148 | 📈 madura (+0.05) | +104.64$ | 1.48$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4404 | 68.7% | +0.187 | ➡️ estable | +77.11$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 241 | 59.8% | +0.097 | 📉 agota (-0.04) | +37.56$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 502 | 63.7% | +0.137 | ➡️ estable | +21.18$ | 1.37$ | ✅ activa |
| GBM_LATE_5M | 218 | 56.0% | +0.059 | ➡️ estable | +21.18$ | 0.59$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 90 | 80.0% | +0.293 | 📉 agota (-0.04) | +17.49$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 232 | 52.2% | +0.021 | 📉 agota (-0.14) | +13.49$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 195 | 82.6% | +0.322 | ➡️ estable | +11.95$ | 2.00$ | ✅ activa |
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
| 2026-07-20T23:26 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 20, 7:20PM-7:25PM ET… | ✅ WIN | +0.48$ |
| 2026-07-20T23:23 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 20, 7:00PM-7:15PM ET… | ✅ WIN | +1.27$ |
| 2026-07-20T23:23 | UPDOWN_GBM#BNB#15min | BNB Up or Down - July 20, 7:00PM-7:15PM ET… | ✅ WIN | +1.33$ |
| 2026-07-20T23:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 7:00PM-7:15PM ET… | ✅ WIN | +0.10$ |
| 2026-07-20T23:20 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 20, 7:00PM-7:15PM ET… | ✅ WIN | +0.95$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T23:25 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,219.06 | 0.1min |  |
| ✅ ETH | $1,901.52 | 0.1min |  |
| ✅ SOL | $77.69 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,219.06 | consenso |  |
| ETH | $1,901.52 | consenso |  |
| SOL | $77.68 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*