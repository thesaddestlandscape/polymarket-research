# Estado del bot — 2026-07-20 09:02 UTC

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
| P&L fiel (stake fijo 1$) | +3370.32 $ |
| P&L sim compuesto | 🟢 +6204.50 $ (ficción Kelly: +24389% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +206.17 $ |
| Operaciones resueltas | 24256 (14754 WIN / 9502 LOSS) — 60.8% |
| Señales abiertas | 121 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6099 | 60.8% | +0.108 | ➡️ estable | +2139.00$ | 1.08$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3318 | 65.5% | +0.155 | ➡️ estable | +2057.62$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3283 | 60.4% | +0.104 | 📈 madura (+0.05) | +1231.19$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 779 | 67.4% | +0.173 | ➡️ estable | +353.08$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 1936 | 52.0% | +0.020 | 📈 madura (+0.11) | +130.45$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4163 | 68.7% | +0.186 | ➡️ estable | +73.52$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 234 | 59.8% | +0.097 | ➡️ estable | +37.13$ | 0.98$ | ✅ activa |
| GBM_LATE_5M | 188 | 58.0% | +0.079 | ➡️ estable | +27.34$ | 0.79$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 410 | 64.4% | +0.143 | ➡️ estable | +19.29$ | 1.43$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 218 | 51.8% | +0.018 | 📉 agota (-0.15) | +10.78$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 175 | 82.3% | +0.319 | 📉 agota (-0.03) | +9.79$ | 2.00$ | ✅ activa |
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
| 2026-07-20T09:01 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 4:55AM-5:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-20T09:01 | UPDOWN_GBM_15M_TARDIO#DOGE#15min | Dogecoin Up or Down - July 20, 4:45AM-5:00AM ET… | ✅ WIN | +1.70$ |
| 2026-07-20T09:01 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 20, 4:45AM-5:00AM ET… | ✅ WIN | +1.62$ |
| 2026-07-20T09:01 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 4:45AM-5:00AM ET… | ✅ WIN | +1.13$ |
| 2026-07-20T09:01 | UPDOWN_GBM#ETH#15min | Ethereum Up or Down - July 20, 4:45AM-5:00AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T09:01 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,998.00 | 0.1min |  |
| ✅ ETH | $1,858.57 | 0.1min |  |
| ✅ SOL | $76.08 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,998.00 | consenso |  |
| ETH | $1,858.57 | consenso |  |
| SOL | $76.08 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*