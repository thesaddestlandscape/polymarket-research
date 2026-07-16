# Estado del bot — 2026-07-16 10:30 UTC

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
| P&L fiel (stake fijo 1$) | +1961.05 $ |
| P&L sim compuesto | 🟢 +3438.78 $ (ficción Kelly: +13517% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +170.35 $ |
| Operaciones resueltas | 16813 (9871 WIN / 6942 LOSS) — 58.7% |
| Señales abiertas | 69 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4855 | 60.2% | +0.102 | ➡️ estable | +1515.41$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2079 | 65.0% | +0.150 | 📉 agota (-0.03) | +1215.65$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2053 | 59.1% | +0.091 | ➡️ estable | +617.83$ | 0.91$ | ✅ activa |
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
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 35 | 80.0% | +0.284 | 📉 agota (-0.04) | +0.57$ | 2.00$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2522 | 67.3% | +0.173 | ➡️ estable | -68.28$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T10:17 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 16, 6:00AM-6:15AM ET… | ✅ WIN | +1.55$ |
| 2026-07-16T10:17 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 16, 6:00AM-6:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:17 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 16, 6:00AM-6:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T10:17 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 16, 6:00AM-6:15AM ET… | ❌ LOSS | -1.96$ |
| 2026-07-16T10:17 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 16, 6:00AM-6:15AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T10:29 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,126.26 | 0.1min |  |
| ✅ ETH | $1,885.85 | 0.1min |  |
| ✅ SOL | $76.25 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,132.80 | consenso |  |
| ETH | $1,886.00 | consenso |  |
| SOL | $76.14 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*