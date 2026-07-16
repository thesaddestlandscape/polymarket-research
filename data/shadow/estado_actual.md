# Estado del bot — 2026-07-16 03:51 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **5.14 $** |
| P&L real total | 🔴 **-20.30 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -27.54 $ |
| Fees pagados (real) | 8.51 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1912.18 $ |
| P&L sim compuesto | 🟢 +3340.33 $ (ficción Kelly: +13130% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +71.90 $ |
| Operaciones resueltas | 16407 (9616 WIN / 6791 LOSS) — 58.6% |
| Señales abiertas | 67 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4774 | 60.3% | +0.103 | ➡️ estable | +1496.16$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2012 | 65.0% | +0.150 | ➡️ estable | +1177.71$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1977 | 59.1% | +0.091 | ➡️ estable | +598.08$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1585 | 50.9% | +0.009 | 📈 madura (+0.09) | +71.15$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 134 | 59.7% | +0.096 | 📉 agota (-0.06) | +30.13$ | 0.96$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 101 | 70.3% | +0.199 | 📉 agota (-0.11) | +29.52$ | 1.99$ | ✅ activa |
| STREAK_FADE_15M | 200 | 59.5% | +0.094 | 📈 madura (+0.05) | +25.14$ | 0.94$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 62 | 59.7% | +0.094 | 📈 madura (+0.33) | +20.51$ | 0.94$ | ✅ activa |
| LATE_WINDOW_5MIN | 44 | 72.7% | +0.217 | ➡️ estable | +18.78$ | 2.00$ | ✅ activa |
| WEEKLY_PRICE | 256 | 62.1% | +0.120 | 📈 madura (+0.28) | +13.84$ | 1.20$ | ✅ activa |
| ORDER_FLOW_5M | 1612 | 51.2% | +0.012 | ➡️ estable | +12.40$ | 0.50$ | ✅ activa |
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
| FAVORITO_CONFIRMADO | 2413 | 67.2% | +0.172 | ➡️ estable | -68.90$ | 1.72$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T03:51 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 15, 11:45PM-11:50PM ET… | ✅ WIN | +0.57$ |
| 2026-07-16T03:49 | ORDER_FLOW_5M#SOL#5min | Solana Up or Down - July 15, 11:40PM-11:45PM ET… | ✅ WIN | +0.59$ |
| 2026-07-16T03:49 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 15, 11:30PM-11:45PM ET… | ❌ LOSS | -1.27$ |
| 2026-07-16T03:49 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 15, 11:30PM-11:45PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T03:49 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 15, 11:30PM-11:45PM ET… | ✅ WIN | +1.71$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T03:50 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,579.31 | 0.1min |  |
| ✅ ETH | $1,919.65 | 0.1min |  |
| ✅ SOL | $76.84 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,587.80 | consenso |  |
| ETH | $1,919.65 | consenso |  |
| SOL | $76.84 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*