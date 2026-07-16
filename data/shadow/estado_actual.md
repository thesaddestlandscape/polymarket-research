# Estado del bot — 2026-07-16 12:30 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **4.03 $** |
| P&L real total | 🔴 **-21.41 $** |
| P&L real hoy | -1.11 $ |
| P&L real 7 días | -28.65 $ |
| Fees pagados (real) | 8.57 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1968.96 $ |
| P&L sim compuesto | 🟢 +3449.93 $ (ficción Kelly: +13561% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +181.50 $ |
| Operaciones resueltas | 16950 (9951 WIN / 6999 LOSS) — 58.7% |
| Señales abiertas | 71 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4885 | 60.2% | +0.102 | ➡️ estable | +1522.80$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2104 | 64.8% | +0.148 | 📉 agota (-0.03) | +1217.68$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2083 | 59.1% | +0.091 | ➡️ estable | +625.13$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1599 | 51.0% | +0.010 | 📈 madura (+0.09) | +73.62$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 129 | 67.4% | +0.172 | 📉 agota (-0.12) | +33.55$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 206 | 60.2% | +0.101 | 📈 madura (+0.04) | +31.61$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 81 | 60.5% | +0.102 | 📈 madura (+0.15) | +28.43$ | 1.02$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 143 | 58.0% | +0.079 | 📉 agota (-0.10) | +25.47$ | 0.79$ | ✅ activa |
| LATE_WINDOW_5MIN | 44 | 72.7% | +0.217 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 256 | 62.1% | +0.120 | 📈 madura (+0.28) | +13.84$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 36 | 80.6% | +0.289 | 📉 agota (-0.05) | +0.82$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 16 | 75.0% | +0.178 | — | -0.19$ | 1.78$ | ✅ activa |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 147 | 33.3% | -0.164 | 📉 agota (-0.12) | -3.25$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 313 | 44.4% | -0.056 | 📉 agota (-0.07) | -23.62$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO | 2555 | 67.3% | +0.173 | ➡️ estable | -69.77$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T12:18 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 16, 8:00AM-8:15AM ET… | ✅ WIN | +0.19$ |
| 2026-07-16T12:18 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 16, 8:00AM-8:15AM ET… | ❌ LOSS | -1.01$ |
| 2026-07-16T12:18 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 16, 8:00AM-8:15AM ET… | ❌ LOSS | -1.36$ |
| 2026-07-16T12:18 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 16, 8:00AM-8:15AM ET… | ❌ LOSS | -0.72$ |
| 2026-07-16T12:18 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 16, 8:00AM-8:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T12:29 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,071.33 | 0.1min |  |
| ✅ ETH | $1,877.58 | 0.1min |  |
| ✅ SOL | $76.16 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,071.33 | consenso |  |
| ETH | $1,877.79 | consenso |  |
| SOL | $76.04 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*