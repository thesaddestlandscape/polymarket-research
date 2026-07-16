# Estado del bot — 2026-07-16 11:00 UTC

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
| P&L fiel (stake fijo 1$) | +1952.60 $ |
| P&L sim compuesto | 🟢 +3424.87 $ (ficción Kelly: +13463% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +156.44 $ |
| Operaciones resueltas | 16840 (9882 WIN / 6958 LOSS) — 58.7% |
| Señales abiertas | 70 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4861 | 60.2% | +0.102 | ➡️ estable | +1516.78$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2085 | 64.8% | +0.148 | ➡️ estable | +1208.49$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2060 | 59.1% | +0.091 | ➡️ estable | +616.98$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1595 | 51.0% | +0.010 | 📈 madura (+0.09) | +76.14$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 122 | 68.9% | +0.185 | 📉 agota (-0.13) | +35.66$ | 1.85$ | ✅ activa |
| STREAK_FADE_15M | 204 | 59.8% | +0.097 | 📈 madura (+0.04) | +29.12$ | 0.97$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 142 | 58.5% | +0.083 | 📉 agota (-0.10) | +27.51$ | 0.83$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 78 | 60.3% | +0.100 | 📈 madura (+0.17) | +26.55$ | 1.00$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2528 | 67.2% | +0.172 | ➡️ estable | -73.77$ | 1.72$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T10:51 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 6:30AM-6:45AM ET… | ❌ LOSS | -1.23$ |
| 2026-07-16T10:51 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 16, 6:30AM-6:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:51 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 16, 6:30AM-6:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:47 | GBM_LATE_15M_PYCONFIRMADO#XRP#15min | XRP Up or Down - July 16, 6:30AM-6:45AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:47 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 16, 6:30AM-6:45AM ET… | ❌ LOSS | -1.19$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T10:59 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,143.00 | 0.1min |  |
| ✅ ETH | $1,885.54 | 0.1min |  |
| ✅ SOL | $76.21 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,147.80 | consenso |  |
| ETH | $1,885.78 | consenso |  |
| SOL | $76.12 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*