# Estado del bot — 2026-07-16 16:27 UTC

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
| P&L fiel (stake fijo 1$) | +1988.40 $ |
| P&L sim compuesto | 🟢 +3507.31 $ (ficción Kelly: +13787% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +238.88 $ |
| Operaciones resueltas | 17263 (10141 WIN / 7122 LOSS) — 58.7% |
| Señales abiertas | 84 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4941 | 60.1% | +0.101 | ➡️ estable | +1519.70$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2153 | 64.8% | +0.148 | ➡️ estable | +1236.88$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2141 | 58.8% | +0.088 | ➡️ estable | +624.43$ | 0.88$ | ✅ activa |
| UPDOWN_GBM | 1612 | 50.7% | +0.007 | 📈 madura (+0.09) | +64.95$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 87 | 63.2% | +0.129 | 📈 madura (+0.14) | +39.68$ | 1.29$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 150 | 65.3% | +0.151 | 📉 agota (-0.10) | +34.87$ | 1.51$ | ✅ activa |
| STREAK_FADE_15M | 206 | 60.2% | +0.101 | 📈 madura (+0.04) | +31.61$ | 1.01$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 46 | 73.9% | +0.229 | ➡️ estable | +22.79$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 151 | 56.3% | +0.062 | 📉 agota (-0.12) | +18.24$ | 0.62$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 43 | 81.4% | +0.300 | 📉 agota (-0.08) | +1.43$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 18 | 77.8% | +0.225 | — | +1.35$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2626 | 67.6% | +0.176 | ➡️ estable | -44.37$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T16:26 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 16, 12:20PM-12:25PM ET… | ✅ WIN | +0.44$ |
| 2026-07-16T16:26 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 16, 12:20PM-12:25PM ET… | ✅ WIN | +0.33$ |
| 2026-07-16T16:26 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 16, 12:15PM-12:20PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T16:15 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 16, 12:00PM-12:15PM ET… | ✅ WIN | +0.20$ |
| 2026-07-16T16:15 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 16, 12:00PM-12:15PM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T16:26 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,480.71 | 0.1min |  |
| ✅ ETH | $1,878.17 | 0.1min |  |
| ✅ SOL | $76.29 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,497.80 | consenso |  |
| ETH | $1,878.37 | consenso |  |
| SOL | $76.29 | consenso |  |
| XRP | $1.11 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*