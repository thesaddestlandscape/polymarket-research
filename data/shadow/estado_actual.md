# Estado del bot — 2026-07-17 01:25 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **2.94 $** |
| P&L real total | 🔴 **-22.50 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -28.51 $ |
| Fees pagados (real) | 8.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2143.15 $ |
| P&L sim compuesto | 🟢 +3751.63 $ (ficción Kelly: +14747% s/ operativo) |
| P&L sim hoy (2026-07-17) | 🟢 +30.56 $ |
| Operaciones resueltas | 17877 (10558 WIN / 7319 LOSS) — 59.1% |
| Señales abiertas | 81 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5065 | 60.2% | +0.102 | ➡️ estable | +1581.33$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2274 | 65.0% | +0.150 | 📉 agota (-0.04) | +1315.21$ | 1.50$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2254 | 59.5% | +0.095 | ➡️ estable | +708.24$ | 0.95$ | ✅ activa |
| UPDOWN_GBM | 1628 | 50.9% | +0.009 | 📈 madura (+0.09) | +71.52$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 187 | 66.8% | +0.167 | 📉 agota (-0.08) | +54.99$ | 1.67$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 112 | 64.3% | +0.140 | 📈 madura (+0.10) | +53.46$ | 1.40$ | ✅ activa |
| STREAK_FADE_15M | 206 | 60.2% | +0.101 | 📈 madura (+0.04) | +31.61$ | 1.01$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 46 | 73.9% | +0.229 | ➡️ estable | +22.79$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 153 | 56.9% | +0.068 | 📉 agota (-0.12) | +20.69$ | 0.68$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 23 | 78.3% | +0.260 | — | +2.31$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 60 | 81.7% | +0.306 | 📈 madura (+0.03) | +1.64$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2780 | 67.4% | +0.174 | ➡️ estable | -67.91$ | 1.73$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-17T01:20 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 16, 9:00PM-9:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-17T01:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 16, 9:00PM-9:15PM ET… | ✅ WIN | +0.54$ |
| 2026-07-17T01:20 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 16, 9:00PM-9:15PM ET… | ✅ WIN | +0.15$ |
| 2026-07-17T01:20 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 16, 9:00PM-9:15PM ET… | ✅ WIN | +1.58$ |
| 2026-07-17T01:20 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 16, 9:00PM-9:15PM ET… | ✅ WIN | +0.88$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-17T01:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,814.31 | 0.1min |  |
| ✅ ETH | $1,858.79 | 0.1min |  |
| ✅ SOL | $75.51 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,814.31 | consenso |  |
| ETH | $1,858.80 | consenso |  |
| SOL | $75.42 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*