# Estado del bot — 2026-07-23 16:53 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **26.91 $** |
| P&L real total | 🔴 **-24.31 $** |
| P&L real hoy | -2.32 $ |
| P&L real 7 días | -3.23 $ |
| Fees pagados (real) | 9.91 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3604.25 $ |
| P&L sim compuesto | 🟢 +6862.60 $ (ficción Kelly: +26976% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +150.74 $ |
| Operaciones resueltas | 31305 (18793 WIN / 12512 LOSS) — 60.0% |
| Señales abiertas | 151 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7178 | 59.5% | +0.095 | 📉 agota (-0.04) | +2217.35$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4373 | 62.5% | +0.124 | 📉 agota (-0.04) | +2174.13$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4391 | 57.7% | +0.077 | ➡️ estable | +1271.59$ | 0.77$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1401 | 66.5% | +0.164 | 📉 agota (-0.03) | +651.27$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2362 | 53.1% | +0.031 | 📈 madura (+0.10) | +205.15$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5473 | 68.9% | +0.189 | ➡️ estable | +114.81$ | 1.89$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 870 | 62.8% | +0.127 | ➡️ estable | +41.87$ | 1.27$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 132 | 79.5% | +0.291 | ➡️ estable | +24.61$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 293 | 82.3% | +0.320 | ➡️ estable | +18.14$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 265 | 50.9% | +0.009 | 📉 agota (-0.16) | +9.65$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 12 | 83.3% | +0.171 | — | +2.98$ | 1.71$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 451 | 47.7% | -0.023 | 📉 agota (-0.15) | -0.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 348 | 44.8% | -0.051 | 📉 agota (-0.14) | -4.38$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T16:51 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 23, 12:30PM-12:45PM ET… | ❌ LOSS | -1.98$ |
| 2026-07-23T16:51 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 23, 12:30PM-12:45PM ET… | ✅ WIN | +0.44$ |
| 2026-07-23T16:51 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 12:30PM-12:45PM ET… | ❌ LOSS | -1.25$ |
| 2026-07-23T16:51 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 12:40PM-12:45PM ET… | ❌ LOSS | -1.42$ |
| 2026-07-23T16:51 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 12:35PM-12:40PM ET… | ✅ WIN | +0.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T16:51 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,709.00 | 0.0min |  |
| ✅ ETH | $1,887.47 | 0.0min |  |
| ✅ SOL | $76.04 | 0.0min |  |
| ✅ XRP | $1.11 | 0.0min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,708.20 | consenso |  |
| ETH | $1,888.17 | consenso |  |
| SOL | $76.03 | consenso |  |
| XRP | $1.11 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*