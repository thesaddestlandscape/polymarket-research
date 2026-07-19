# Estado del bot — 2026-07-19 06:37 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -17.21 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +2945.76 $ |
| P&L sim compuesto | 🟢 +5330.18 $ (ficción Kelly: +20952% s/ operativo) |
| P&L sim hoy (2026-07-19) | 🟢 +168.42 $ |
| Operaciones resueltas | 22064 (13341 WIN / 8723 LOSS) — 60.5% |
| Señales abiertas | 127 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 5745 | 60.6% | +0.106 | ➡️ estable | +1925.59$ | 1.06$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 2973 | 65.3% | +0.152 | ➡️ estable | +1763.77$ | 1.52$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 2921 | 60.0% | +0.100 | 📈 madura (+0.04) | +1011.38$ | 1.00$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 590 | 68.3% | +0.182 | ➡️ estable | +263.85$ | 1.82$ | ✅ activa |
| UPDOWN_GBM | 1814 | 52.0% | +0.020 | 📈 madura (+0.13) | +127.71$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 167 | 65.9% | +0.157 | 📈 madura (+0.09) | +89.91$ | 1.57$ | ✅ activa |
| FAVORITO_CONFIRMADO | 3707 | 68.6% | +0.186 | ➡️ estable | +57.81$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 295 | 65.8% | +0.157 | 📈 madura (+0.25) | +49.68$ | 1.57$ | ✅ activa |
| STREAK_FADE_15M | 223 | 59.6% | +0.096 | ➡️ estable | +33.70$ | 0.96$ | ✅ activa |
| LATE_WINDOW_5MIN | 49 | 73.5% | +0.225 | ➡️ estable | +24.54$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 278 | 64.7% | +0.146 | ➡️ estable | +17.96$ | 1.46$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 189 | 54.0% | +0.039 | 📉 agota (-0.11) | +14.45$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1631 | 51.3% | +0.013 | ➡️ estable | +13.70$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 60 | 78.3% | +0.274 | 📉 agota (-0.03) | +10.45$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 327 | 38.5% | -0.114 | ➡️ estable | +6.13$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 140 | 81.4% | +0.310 | ➡️ estable | +5.31$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 89 | 57.3% | +0.071 | ➡️ estable | +4.71$ | 0.71$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 3 | 66.7% | +0.015 | — | +0.37$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 149 | 32.9% | -0.169 | 📉 agota (-0.12) | -4.27$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-19T06:36 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 19, 2:15AM-2:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-19T06:36 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 19, 2:15AM-2:30AM ET… | ✅ WIN | +0.22$ |
| 2026-07-19T06:36 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | Ethereum Up or Down - July 19, 2:15AM-2:30AM ET… | ❌ LOSS | -1.73$ |
| 2026-07-19T06:36 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 19, 2:15AM-2:30AM ET… | ✅ WIN | +2.08$ |
| 2026-07-19T06:36 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 19, 2:15AM-2:30AM ET… | ✅ WIN | +2.08$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-19T06:36 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,687.79 | 0.1min |  |
| ✅ ETH | $1,868.33 | 0.1min |  |
| ✅ SOL | $76.03 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,687.79 | consenso |  |
| ETH | $1,868.33 | consenso |  |
| SOL | $75.97 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*