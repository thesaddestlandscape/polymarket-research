# Estado del bot — 2026-07-20 13:41 UTC

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
| P&L fiel (stake fijo 1$) | +3389.92 $ |
| P&L sim compuesto | 🟢 +6246.02 $ (ficción Kelly: +24552% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +247.70 $ |
| Operaciones resueltas | 24602 (14958 WIN / 9644 LOSS) — 60.8% |
| Señales abiertas | 132 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6160 | 60.7% | +0.107 | ➡️ estable | +2149.51$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3375 | 65.3% | +0.153 | ➡️ estable | +2077.52$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3346 | 60.1% | +0.101 | 📈 madura (+0.04) | +1229.01$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 796 | 67.0% | +0.169 | ➡️ estable | +356.99$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 1945 | 52.0% | +0.020 | 📈 madura (+0.11) | +130.32$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4245 | 68.7% | +0.187 | ➡️ estable | +82.61$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 57 | 71.9% | +0.212 | 📈 madura (+0.08) | +28.08$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 205 | 56.6% | +0.065 | ➡️ estable | +20.74$ | 0.65$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 436 | 63.8% | +0.137 | ➡️ estable | +15.91$ | 1.37$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 182 | 83.0% | +0.326 | ➡️ estable | +13.31$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 222 | 52.3% | +0.022 | 📉 agota (-0.16) | +12.02$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
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
| 2026-07-20T13:34 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 20, 9:25AM-9:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-20T13:34 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 20, 9:15AM-9:30AM ET… | ✅ WIN | +2.17$ |
| 2026-07-20T13:34 | UPDOWN_GBM#DOGE#15min | Dogecoin Up or Down - July 20, 9:15AM-9:30AM ET… | ✅ WIN | +0.64$ |
| 2026-07-20T13:32 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 20, 9:15AM-9:30AM ET… | ❌ LOSS | -0.69$ |
| 2026-07-20T13:32 | UPDOWN_GBM_15M_TARDIO#BNB#15min | BNB Up or Down - July 20, 9:15AM-9:30AM ET… | ✅ WIN | +1.73$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T13:39 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,654.39 | 0.1min |  |
| ✅ ETH | $1,877.35 | 0.1min |  |
| ✅ SOL | $76.98 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,655.20 | consenso |  |
| ETH | $1,878.12 | consenso |  |
| SOL | $76.94 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*