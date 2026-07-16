# Estado del bot — 2026-07-16 19:28 UTC

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
| P&L fiel (stake fijo 1$) | +2032.94 $ |
| P&L sim compuesto | 🟢 +3565.99 $ (ficción Kelly: +14017% s/ operativo) |
| P&L sim hoy (2026-07-16) | 🟢 +297.56 $ |
| Operaciones resueltas | 17466 (10275 WIN / 7191 LOSS) — 58.8% |
| Señales abiertas | 81 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4984 | 60.2% | +0.101 | ➡️ estable | +1539.43$ | 1.02$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2194 | 64.8% | +0.148 | 📉 agota (-0.04) | +1252.24$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2179 | 59.1% | +0.091 | ➡️ estable | +652.68$ | 0.91$ | ✅ activa |
| UPDOWN_GBM | 1617 | 50.7% | +0.007 | 📈 madura (+0.09) | +64.46$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 98 | 62.2% | +0.120 | 📈 madura (+0.06) | +39.66$ | 1.20$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 159 | 64.8% | +0.146 | 📉 agota (-0.14) | +35.06$ | 1.46$ | ✅ activa |
| STREAK_FADE_15M | 206 | 60.2% | +0.101 | 📈 madura (+0.04) | +31.61$ | 1.01$ | ✅ activa |
| WEEKLY_PRICE | 273 | 63.7% | +0.136 | 📈 madura (+0.26) | +29.85$ | 1.36$ | ✅ activa |
| LATE_WINDOW_5MIN | 46 | 73.9% | +0.229 | ➡️ estable | +22.79$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 152 | 56.6% | +0.065 | 📉 agota (-0.13) | +19.08$ | 0.65$ | ✅ activa |
| ORDER_FLOW_5M | 1617 | 51.2% | +0.012 | ➡️ estable | +13.02$ | 0.50$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 18 | 77.8% | +0.225 | — | +1.35$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 50 | 80.0% | +0.288 | ➡️ estable | -0.41$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 11 | 45.5% | -0.021 | — | -0.62$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 148 | 33.1% | -0.167 | 📉 agota (-0.12) | -3.76$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 2674 | 67.6% | +0.176 | ➡️ estable | -47.72$ | 1.76$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-16T19:23 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 16, 3:00PM-3:15PM ET… | ✅ WIN | +1.77$ |
| 2026-07-16T19:23 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 16, 3:00PM-3:15PM ET… | ✅ WIN | +0.85$ |
| 2026-07-16T19:23 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 16, 3:00PM-3:15PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-16T19:19 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 16, 3:00PM-3:15PM ET… | ✅ WIN | +2.00$ |
| 2026-07-16T19:19 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 16, 3:00PM-3:15PM ET… | ❌ LOSS | -1.33$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-16T19:27 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,135.50 | 0.1min |  |
| ✅ ETH | $1,870.69 | 0.1min |  |
| ✅ SOL | $75.67 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,143.00 | consenso |  |
| ETH | $1,871.01 | consenso |  |
| SOL | $75.60 | consenso |  |
| XRP | $1.09 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*