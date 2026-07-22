# Estado del bot — 2026-07-22 09:28 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.29 $** |
| P&L real total | 🔴 **-23.93 $** |
| P&L real hoy | +2.38 $ |
| P&L real 7 días | -7.21 $ |
| Fees pagados (real) | 9.19 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3378.43 $ |
| P&L sim compuesto | 🟢 +6408.59 $ (ficción Kelly: +25191% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +45.08 $ |
| Operaciones resueltas | 28654 (17183 WIN / 11471 LOSS) — 60.0% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6792 | 59.7% | +0.097 | ➡️ estable | +2138.92$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3989 | 62.8% | +0.128 | 📉 agota (-0.05) | +2067.16$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3971 | 58.3% | +0.083 | ➡️ estable | +1228.32$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1155 | 66.1% | +0.161 | 📉 agota (-0.05) | +514.13$ | 1.61$ | ✅ activa |
| UPDOWN_GBM | 2169 | 52.8% | +0.028 | 📈 madura (+0.11) | +179.05$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 225 | 61.3% | +0.112 | 📉 agota (-0.06) | +108.23$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4966 | 68.6% | +0.186 | ➡️ estable | +79.70$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 710 | 62.4% | +0.124 | 📉 agota (-0.04) | +25.89$ | 1.24$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 250 | 82.0% | +0.317 | ➡️ estable | +13.68$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 279 | 48.7% | -0.012 | 📉 agota (-0.14) | +8.18$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 316 | 45.3% | -0.047 | 📉 agota (-0.18) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 316 | 44.3% | -0.057 | 📉 agota (-0.09) | -24.82$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T09:24 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 5:00AM-5:15AM ET… | ✅ WIN | +1.89$ |
| 2026-07-22T09:24 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 22, 5:00AM-5:15AM ET… | ✅ WIN | +1.93$ |
| 2026-07-22T09:24 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 5:00AM-5:15AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T09:24 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 22, 5:00AM-5:15AM ET… | ✅ WIN | +1.31$ |
| 2026-07-22T09:21 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 5:00AM-5:15AM ET… | ✅ WIN | +0.68$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T09:26 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,982.24 | 0.1min |  |
| ✅ ETH | $1,923.61 | 0.1min |  |
| ✅ SOL | $77.45 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,989.50 | consenso |  |
| ETH | $1,923.61 | consenso |  |
| SOL | $77.38 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*