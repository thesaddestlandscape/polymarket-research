# Estado del bot — 2026-07-20 05:25 UTC

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
| P&L fiel (stake fijo 1$) | +3346.06 $ |
| P&L sim compuesto | 🟢 +6137.70 $ (ficción Kelly: +24126% s/ operativo) |
| P&L sim hoy (2026-07-20) | 🟢 +139.38 $ |
| Operaciones resueltas | 23918 (14558 WIN / 9360 LOSS) — 60.9% |
| Señales abiertas | 127 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6048 | 60.9% | +0.109 | ➡️ estable | +2143.78$ | 1.09$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3268 | 65.5% | +0.155 | ➡️ estable | +2031.65$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3231 | 60.4% | +0.104 | 📈 madura (+0.05) | +1209.16$ | 1.04$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 752 | 67.3% | +0.172 | ➡️ estable | +333.24$ | 1.72$ | ✅ activa |
| UPDOWN_GBM | 1904 | 52.1% | +0.021 | 📈 madura (+0.12) | +134.01$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 180 | 65.6% | +0.154 | 📈 madura (+0.07) | +96.33$ | 1.54$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4104 | 68.8% | +0.188 | ➡️ estable | +77.29$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 229 | 59.8% | +0.097 | ➡️ estable | +35.37$ | 0.97$ | ✅ activa |
| LATE_WINDOW_5MIN | 55 | 70.9% | +0.202 | ➡️ estable | +23.91$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 394 | 64.7% | +0.146 | ➡️ estable | +19.83$ | 1.46$ | ✅ activa |
| GBM_LATE_5M | 155 | 57.4% | +0.073 | 📉 agota (-0.04) | +17.74$ | 0.73$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 83 | 79.5% | +0.288 | 📉 agota (-0.11) | +15.82$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1638 | 51.2% | +0.012 | ➡️ estable | +13.23$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 212 | 52.4% | +0.023 | 📉 agota (-0.12) | +11.76$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 171 | 82.5% | +0.321 | ➡️ estable | +10.45$ | 2.00$ | ✅ activa |
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
| 2026-07-20T05:21 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 1:15AM-1:20AM ET… | ✅ WIN | +0.80$ |
| 2026-07-20T05:19 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 20, 1:10AM-1:15AM ET… | ✅ WIN | +1.50$ |
| 2026-07-20T05:16 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 20, 1:10AM-1:15AM ET… | ✅ WIN | +2.00$ |
| 2026-07-20T05:16 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 20, 1:00AM-1:15AM ET… | ✅ WIN | +0.64$ |
| 2026-07-20T05:16 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 20, 1:00AM-1:15AM ET… | ✅ WIN | +1.32$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-20T05:23 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,052.96 | 0.1min |  |
| ✅ ETH | $1,854.80 | 0.1min |  |
| ✅ SOL | $75.93 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,086.50 | consenso |  |
| ETH | $1,855.34 | consenso |  |
| SOL | $75.93 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*