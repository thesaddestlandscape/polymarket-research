# Estado del bot — 2026-07-16 10:36 UTC

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
| P&L fiel (stake fijo 1$) | +1961.29 $ |
| P&L sim compuesto | 🟢 +3438.90 $ (ficción Kelly: +13518% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +170.47 $ |
| Operaciones resueltas | 16823 (9878 WIN / 6945 LOSS) — 58.7% |
| Señales abiertas | 70 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4857 | 60.2% | +0.102 | ➡️ estable | +1515.10$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2081 | 65.0% | +0.150 | ➡️ estable | +1214.77$ | 1.49$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2055 | 59.1% | +0.091 | ➡️ estable | +618.24$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1595 | 51.0% | +0.010 | 📈 madura (+0.09) | +76.14$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 122 | 68.9% | +0.185 | 📉 agota (-0.13) | +35.66$ | 1.85$ | ✅ activa |
| STREAK_FADE_15M | 204 | 59.8% | +0.097 | 📈 madura (+0.04) | +29.12$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 77 | 61.0% | +0.108 | 📈 madura (+0.21) | +28.59$ | 1.08$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 142 | 58.5% | +0.083 | 📉 agota (-0.10) | +27.51$ | 0.83$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2525 | 67.3% | +0.173 | ➡️ estable | -67.65$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T10:33 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 16, 6:15AM-6:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:33 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 16, 6:15AM-6:30AM ET… | ✅ WIN | +0.25$ |
| 2026-07-16T10:33 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 16, 6:15AM-6:30AM ET… | ❌ LOSS | -1.13$ |
| 2026-07-16T10:33 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 16, 6:15AM-6:30AM ET… | ❌ LOSS | -1.30$ |
| 2026-07-16T10:33 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 16, 6:15AM-6:30AM ET… | ✅ WIN | +0.25$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T10:35 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,208.42 | 0.1min |  |
| ✅ ETH | $1,889.25 | 0.1min |  |
| ✅ SOL | $76.35 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,208.42 | consenso |  |
| ETH | $1,889.25 | consenso |  |
| SOL | $76.27 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*