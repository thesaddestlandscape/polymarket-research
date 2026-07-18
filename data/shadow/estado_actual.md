# Estado del bot — 2026-07-18 12:57 UTC

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
| P&L fiel (stake fijo 1$) | +2703.01 $ |
| P&L sim compuesto | 🟢 +4838.43 $ (ficción Kelly: +19019% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +333.67 $ |
| Operaciones resueltas | 20616 (12402 WIN / 8214 LOSS) — 60.2% |
| Señales abiertas | 105 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5519 | 60.4% | +0.104 | ➡️ estable | +1787.81$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2742 | 65.0% | +0.150 | ➡️ estable | +1598.05$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2681 | 60.1% | +0.101 | 📈 madura (+0.03) | +921.57$ | 1.01$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 450 | 68.2% | +0.181 | ➡️ estable | +187.90$ | 1.81$ | ✅ activa |
| UPDOWN_GBM | 1761 | 51.8% | +0.018 | 📈 madura (+0.12) | +120.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 162 | 66.7% | +0.165 | 📈 madura (+0.12) | +93.90$ | 1.65$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 218 | 60.6% | +0.105 | 📈 madura (+0.05) | +39.44$ | 1.04$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3401 | 68.4% | +0.184 | ➡️ estable | +27.70$ | 1.84$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 163 | 67.5% | +0.173 | ➡️ estable | +24.91$ | 1.73$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 174 | 55.7% | +0.057 | 📉 agota (-0.12) | +18.23$ | 0.57$ | ✅ activa |
| ORDER_FLOW_5M | 1630 | 51.3% | +0.013 | ➡️ estable | +14.21$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 47 | 83.0% | +0.316 | 📈 madura (+0.09) | +12.81$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 113 | 81.4% | +0.309 | ➡️ estable | +3.57$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 19 | 57.9% | +0.068 | — | -0.01$ | 0.68$ | ✅ activa |
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
| 2026-07-18T12:56 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 18, 8:45AM-8:50AM ET… | ✅ WIN | +0.49$ |
| 2026-07-18T12:51 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 18, 8:40AM-8:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-18T12:51 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 18, 8:30AM-8:45AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-18T12:51 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 18, 8:30AM-8:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-18T12:51 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 18, 8:30AM-8:45AM ET… | ❌ LOSS | -1.17$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T12:55 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,160.40 | 0.1min |  |
| ✅ ETH | $1,845.42 | 0.1min |  |
| ✅ SOL | $75.03 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,163.10 | consenso |  |
| ETH | $1,845.42 | consenso |  |
| SOL | $74.97 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*