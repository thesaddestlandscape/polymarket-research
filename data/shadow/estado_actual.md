# Estado del bot — 2026-07-20 22:26 UTC

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
| P&L fiel (stake fijo 1$) | +3452.07 $ |
| P&L sim compuesto | 🟢 +6383.10 $ (ficción Kelly: +25091% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +384.77 $ |
| Operaciones resueltas | 25354 (15414 WIN / 9940 LOSS) — 60.8% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6282 | 60.6% | +0.106 | ➡️ estable | +2167.33$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3486 | 65.1% | +0.151 | ➡️ estable | +2127.07$ | 1.51$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3468 | 59.9% | +0.099 | 📈 madura (+0.03) | +1251.80$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 859 | 66.8% | +0.168 | ➡️ estable | +383.63$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 1987 | 52.3% | +0.023 | 📈 madura (+0.12) | +142.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 192 | 65.6% | +0.155 | 📈 madura (+0.08) | +105.61$ | 1.55$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4390 | 68.6% | +0.186 | ➡️ estable | +69.00$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 238 | 60.1% | +0.100 | ➡️ estable | +40.35$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 78 | 69.2% | +0.188 | 📉 agota (-0.05) | +30.95$ | 1.88$ | ✅ activa |
| GBM_LATE_5M | 216 | 56.5% | +0.064 | ➡️ estable | +22.20$ | 0.64$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 497 | 63.8% | +0.137 | ➡️ estable | +20.95$ | 1.37$ | ✅ activa |
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
| 2026-07-20T22:22 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 20, 6:10PM-6:15PM ET… | ✅ WIN | +1.53$ |
| 2026-07-20T22:22 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 20, 6:00PM-6:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T22:22 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 20, 6:00PM-6:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T22:22 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 20, 6:00PM-6:15PM ET… | ❌ LOSS | -1.71$ |
| 2026-07-20T22:19 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 20, 6:00PM-6:15PM ET… | ✅ WIN | +1.75$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T22:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,173.01 | 0.1min |  |
| ✅ ETH | $1,897.18 | 0.1min |  |
| ✅ SOL | $77.68 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,173.40 | consenso |  |
| ETH | $1,897.18 | consenso |  |
| SOL | $77.66 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*