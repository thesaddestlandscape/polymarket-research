# Estado del bot — 2026-07-18 00:54 UTC

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
| P&L fiel (stake fijo 1$) | +2550.04 $ |
| P&L sim compuesto | 🟢 +4555.12 $ (ficción Kelly: +17905% s/ operativo) |
| P&L sim hoy (2026-07-18) | 🟢 +50.36 $ |
| Operaciones resueltas | 19726 (11807 WIN / 7919 LOSS) — 59.9% |
| Señales abiertas | 94 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5383 | 60.4% | +0.104 | ➡️ estable | +1735.70$ | 1.04$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2578 | 65.3% | +0.153 | ➡️ estable | +1542.11$ | 1.53$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2549 | 59.9% | +0.099 | ➡️ estable | +855.56$ | 0.99$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 373 | 68.9% | +0.188 | 📈 madura (+0.04) | +160.00$ | 1.88$ | ✅ activa |
| UPDOWN_GBM | 1719 | 51.8% | +0.018 | 📈 madura (+0.12) | +118.68$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 157 | 66.2% | +0.160 | 📈 madura (+0.12) | +90.54$ | 1.60$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 214 | 60.7% | +0.106 | 📈 madura (+0.06) | +39.05$ | 1.06$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 166 | 55.4% | +0.054 | 📉 agota (-0.14) | +18.38$ | 0.54$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 96 | 67.7% | +0.173 | 📈 madura (+0.18) | +13.88$ | 1.73$ | ✅ activa |
| ORDER_FLOW_5M | 1627 | 51.2% | +0.012 | ➡️ estable | +12.76$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 37 | 83.8% | +0.321 | 📈 madura (+0.11) | +10.70$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 93 | 81.7% | +0.311 | ➡️ estable | +1.94$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 3187 | 67.8% | +0.178 | ➡️ estable | -31.14$ | 1.78$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-18T00:49 | ORDER_FLOW_5M#XRP#5min | XRP Up or Down - July 17, 8:40PM-8:45PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-18T00:49 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 17, 8:30PM-8:45PM ET… | ✅ WIN | +1.81$ |
| 2026-07-18T00:49 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 17, 8:30PM-8:45PM ET… | ✅ WIN | +0.97$ |
| 2026-07-18T00:49 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 17, 8:30PM-8:45PM ET… | ✅ WIN | +0.48$ |
| 2026-07-18T00:49 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 17, 8:30PM-8:45PM ET… | ✅ WIN | +0.64$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-18T00:53 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,888.93 | 0.1min |  |
| ✅ ETH | $1,841.35 | 0.1min |  |
| ✅ SOL | $75.08 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,888.93 | consenso |  |
| ETH | $1,841.35 | consenso |  |
| SOL | $75.09 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*