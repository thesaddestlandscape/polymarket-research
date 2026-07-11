# Estado del bot — 2026-07-11 19:15 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **21.36 $** |
| P&L real total | 🔴 **-4.08 $** |
| P&L real hoy | -4.00 $ |
| P&L real 7 días | +13.32 $ |
| Fees pagados (real) | 7.42 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +979.34 $ |
| P&L sim compuesto | 🟢 +1530.37 $ (ficción Kelly: +6016% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +250.96 $ |
| Operaciones resueltas | 9642 (5407 WIN / 4235 LOSS) — 56.1% |
| Señales abiertas | 184 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3323 | 61.1% | +0.111 | ➡️ estable | +1052.62$ | 1.11$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 709 | 64.3% | +0.143 | 📉 agota (-0.04) | +305.61$ | 1.43$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 866 | 57.6% | +0.076 | ➡️ estable | +181.43$ | 0.76$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 53 | 66.0% | +0.155 | 📈 madura (+0.15) | +19.18$ | 1.54$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| UPDOWN_GBM | 1279 | 48.9% | -0.011 | 📈 madura (+0.03) | +10.41$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 292 | 39.0% | -0.109 | 📈 madura (+0.05) | +10.33$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 24 | 54.2% | +0.038 | — | +0.76$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 578 | 66.1% | +0.160 | 📉 agota (-0.05) | -26.81$ | 1.60$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T19:07 | GBM_LATE_60M#SOL#60min | Solana Up or Down - July 11, 2PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T19:07 | GBM_LATE_60M#ETH#60min | Ethereum Up or Down - July 11, 2PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T19:07 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 11, 2PM ET… | ❌ LOSS | -1.60$ |
| 2026-07-11T19:07 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 11, 2PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T19:03 | GBM_LATE_60M#BTC#60min | Bitcoin Up or Down - July 11, 2PM ET… | ✅ WIN | +0.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T19:15 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,269.07 | 0.1min |  |
| ✅ ETH | $1,825.58 | 0.1min |  |
| ✅ SOL | $78.05 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,269.07 | consenso |  |
| ETH | $1,825.58 | consenso |  |
| SOL | $78.03 | consenso |  |
| XRP | $1.12 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*