# Estado del bot — 2026-07-16 04:23 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **5.11 $** |
| P&L real total | 🔴 **-20.33 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -28.65 $ |
| Fees pagados (real) | 8.51 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1914.19 $ |
| P&L sim compuesto | 🟢 +3340.87 $ (ficción Kelly: +13132% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +72.44 $ |
| Operaciones resueltas | 16442 (9636 WIN / 6806 LOSS) — 58.6% |
| Señales abiertas | 67 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4779 | 60.3% | +0.103 | ➡️ estable | +1496.88$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2017 | 65.0% | +0.150 | ➡️ estable | +1179.69$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1982 | 59.1% | +0.091 | ➡️ estable | +598.31$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1587 | 50.9% | +0.009 | 📈 madura (+0.09) | +70.63$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 106 | 69.8% | +0.194 | 📉 agota (-0.11) | +30.71$ | 1.94$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 134 | 59.7% | +0.096 | 📉 agota (-0.06) | +30.13$ | 0.96$ | ✅ activa |
| STREAK_FADE_15M | 200 | 59.5% | +0.094 | 📈 madura (+0.05) | +25.14$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 63 | 58.7% | +0.085 | 📈 madura (+0.31) | +19.00$ | 0.85$ | ✅ activa |
| LATE_WINDOW_5MIN | 44 | 72.7% | +0.217 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 256 | 62.1% | +0.120 | 📈 madura (+0.28) | +13.84$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1615 | 51.2% | +0.012 | ➡️ estable | +13.01$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 30 | 80.0% | +0.281 | 📉 agota (-0.12) | +0.32$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 14 | 71.4% | +0.131 | — | -0.95$ | 1.31$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 147 | 33.3% | -0.164 | 📉 agota (-0.12) | -3.25$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 310 | 44.5% | -0.054 | 📉 agota (-0.06) | -22.30$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 2422 | 67.2% | +0.172 | ➡️ estable | -71.06$ | 1.72$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T04:20 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 12:00AM-12:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T04:20 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 16, 12:00AM-12:15AM ET… | ❌ LOSS | -1.51$ |
| 2026-07-16T04:20 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 16, 12:00AM-12:15AM ET… | ❌ LOSS | -2.03$ |
| 2026-07-16T04:20 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 16, 12:00AM-12:15AM ET… | ❌ LOSS | -1.22$ |
| 2026-07-16T04:20 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 16, 12:00AM-12:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T04:22 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,548.90 | 0.1min |  |
| ✅ ETH | $1,916.41 | 0.1min |  |
| ✅ SOL | $76.79 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,552.00 | consenso |  |
| ETH | $1,916.41 | consenso |  |
| SOL | $76.85 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*