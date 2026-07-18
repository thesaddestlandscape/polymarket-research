# Estado del bot — 2026-07-18 13:10 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -24.52 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2716.25 $ |
| P&L sim compuesto | 🟢 +4859.10 $ (ficción Kelly: +19100% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +354.34 $ |
| Operaciones resueltas | 20643 (12425 WIN / 8218 LOSS) — 60.2% |
| Señales abiertas | 103 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5523 | 60.4% | +0.104 | ➡️ estable | +1794.04$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2745 | 65.0% | +0.150 | ➡️ estable | +1599.17$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2685 | 60.1% | +0.101 | 📈 madura (+0.03) | +921.97$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 454 | 68.5% | +0.184 | ➡️ estable | +194.23$ | 1.84$ | ✅ activa |
| UPDOWN_GBM | 1762 | 51.9% | +0.019 | 📈 madura (+0.12) | +122.56$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 218 | 60.6% | +0.105 | 📈 madura (+0.05) | +39.44$ | 1.04$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3407 | 68.4% | +0.184 | ➡️ estable | +29.71$ | 1.84$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 165 | 67.9% | +0.177 | ➡️ estable | +25.94$ | 1.77$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 175 | 56.0% | +0.059 | 📉 agota (-0.12) | +18.77$ | 0.59$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 47 | 83.0% | +0.316 | 📈 madura (+0.09) | +12.81$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 114 | 81.6% | +0.310 | ➡️ estable | +4.31$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 20 | 60.0% | +0.091 | — | +0.48$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T13:06 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 18, 9:00AM-9:05AM ET… | ✅ WIN | +0.49$ |
| 2026-07-18T13:06 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 18, 8:45AM-9:00AM ET… | ✅ WIN | +0.58$ |
| 2026-07-18T13:06 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 18, 8:45AM-9:00AM ET… | ✅ WIN | +0.38$ |
| 2026-07-18T13:06 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 18, 8:45AM-9:00AM ET… | ✅ WIN | +2.17$ |
| 2026-07-18T13:06 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 18, 8:45AM-9:00AM ET… | ✅ WIN | +0.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T13:08 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,113.61 | 0.1min |  |
| ✅ ETH | $1,842.11 | 0.1min |  |
| ✅ SOL | $74.85 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,120.90 | consenso |  |
| ETH | $1,842.07 | consenso |  |
| SOL | $74.86 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*