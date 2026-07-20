# Estado del bot — 2026-07-20 11:11 UTC

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
| P&L fiel (stake fijo 1$) | +3372.06 $ |
| P&L sim compuesto | 🟢 +6211.02 $ (ficción Kelly: +24414% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +212.69 $ |
| Operaciones resueltas | 24413 (14842 WIN / 9571 LOSS) — 60.8% |
| Señales abiertas | 130 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6129 | 60.7% | +0.107 | ➡️ estable | +2139.93$ | 1.07$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3349 | 65.3% | +0.153 | ➡️ estable | +2060.33$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3316 | 60.3% | +0.102 | 📈 madura (+0.04) | +1230.70$ | 1.02$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 781 | 67.5% | +0.174 | ➡️ estable | +356.63$ | 1.74$ | ✅ activa |
| UPDOWN_GBM | 1936 | 52.0% | +0.020 | 📈 madura (+0.11) | +130.45$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 182 | 65.9% | +0.158 | 📈 madura (+0.09) | +97.69$ | 1.58$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4196 | 68.6% | +0.186 | ➡️ estable | +75.97$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 235 | 60.0% | +0.099 | ➡️ estable | +38.58$ | 0.99$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 196 | 57.7% | +0.076 | ➡️ estable | +23.90$ | 0.76$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 425 | 63.8% | +0.137 | ➡️ estable | +16.14$ | 1.37$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 178 | 82.6% | +0.322 | ➡️ estable | +11.75$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 219 | 52.1% | +0.020 | 📉 agota (-0.15) | +11.32$ | 0.50$ | ✅ activa |
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
| 2026-07-20T11:07 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 7:00AM-7:05AM ET… | ❌ LOSS | -1.77$ |
| 2026-07-20T11:05 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 20, 6:45AM-7:00AM ET… | ❌ LOSS | -1.86$ |
| 2026-07-20T11:05 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 6:45AM-7:00AM ET… | ✅ WIN | +1.21$ |
| 2026-07-20T11:05 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 20, 6:45AM-7:00AM ET… | ❌ LOSS | -1.33$ |
| 2026-07-20T11:05 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 20, 6:45AM-7:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T11:10 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,272.71 | 0.1min |  |
| ✅ ETH | $1,867.63 | 0.1min |  |
| ✅ SOL | $76.56 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,272.71 | consenso |  |
| ETH | $1,867.95 | consenso |  |
| SOL | $76.34 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*