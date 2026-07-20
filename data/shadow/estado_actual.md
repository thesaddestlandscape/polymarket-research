# Estado del bot — 2026-07-20 07:01 UTC

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
| P&L fiel (stake fijo 1$) | +3365.92 $ |
| P&L sim compuesto | 🟢 +6174.92 $ (ficción Kelly: +24272% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +176.59 $ |
| Operaciones resueltas | 24074 (14654 WIN / 9420 LOSS) — 60.9% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6071 | 60.8% | +0.108 | ➡️ estable | +2133.47$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3290 | 65.4% | +0.154 | ➡️ estable | +2035.41$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3254 | 60.4% | +0.104 | 📈 madura (+0.05) | +1222.25$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 765 | 67.3% | +0.173 | ➡️ estable | +344.26$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 1919 | 52.2% | +0.022 | 📈 madura (+0.11) | +135.12$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 180 | 65.6% | +0.154 | 📈 madura (+0.07) | +96.33$ | 1.54$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4130 | 68.8% | +0.188 | ➡️ estable | +82.40$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 233 | 59.7% | +0.096 | ➡️ estable | +35.46$ | 0.96$ | ✅ activa |
| GBM_LATE_5M | 175 | 58.9% | +0.088 | ➡️ estable | +29.45$ | 0.88$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 399 | 64.9% | +0.148 | ➡️ estable | +22.06$ | 1.48$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 215 | 52.6% | +0.025 | 📉 agota (-0.12) | +12.57$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 173 | 82.1% | +0.317 | 📉 agota (-0.03) | +9.06$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 5 | 60.0% | +0.018 | — | +0.32$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-20T07:00 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 20, 2:45AM-3:00AM ET… | ✅ WIN | +0.62$ |
| 2026-07-20T07:00 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 20, 2:45AM-3:00AM ET… | ❌ LOSS | -1.23$ |
| 2026-07-20T07:00 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 20, 2:45AM-3:00AM ET… | ❌ LOSS | -1.69$ |
| 2026-07-20T07:00 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 20, 2:45AM-3:00AM ET… | ❌ LOSS | -1.02$ |
| 2026-07-20T07:00 | UPDOWN_GBM#SOL#15min | Solana Up or Down - July 20, 2:45AM-3:00AM ET… | ✅ WIN | +1.56$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T06:59 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,825.93 | 0.1min |  |
| ✅ ETH | $1,847.29 | 0.1min |  |
| ✅ SOL | $75.63 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,836.00 | consenso |  |
| ETH | $1,848.15 | consenso |  |
| SOL | $75.56 | consenso |  |
| XRP | $1.08 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*