# Estado del bot — 2026-07-22 03:56 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **23.79 $** |
| P&L real total | 🔴 **-27.43 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3357.70 $ |
| P&L sim compuesto | 🟢 +6382.14 $ (ficción Kelly: +25087% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +18.63 $ |
| Operaciones resueltas | 28123 (16887 WIN / 11236 LOSS) — 60.0% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6719 | 59.8% | +0.098 | ➡️ estable | +2132.19$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3913 | 63.1% | +0.131 | 📉 agota (-0.04) | +2065.76$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3887 | 58.5% | +0.085 | ➡️ estable | +1238.16$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1101 | 66.3% | +0.163 | 📉 agota (-0.03) | +492.09$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2127 | 52.6% | +0.026 | 📈 madura (+0.11) | +170.39$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4867 | 68.6% | +0.186 | ➡️ estable | +79.91$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 685 | 62.8% | +0.127 | 📉 agota (-0.04) | +26.92$ | 1.27$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 115 | 78.3% | +0.278 | ➡️ estable | +18.22$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 269 | 49.4% | -0.006 | 📉 agota (-0.13) | +14.32$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 244 | 82.0% | +0.317 | ➡️ estable | +13.13$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1648 | 51.1% | +0.011 | ➡️ estable | +11.24$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 274 | 45.6% | -0.043 | 📉 agota (-0.22) | -2.32$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T03:55 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 21, 11:40PM-11:45PM ET… | ✅ WIN | +1.30$ |
| 2026-07-22T03:55 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 11:30PM-11:45PM ET… | ✅ WIN | +0.36$ |
| 2026-07-22T03:55 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 11:30PM-11:45PM ET… | ✅ WIN | +0.56$ |
| 2026-07-22T03:52 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 11:40PM-11:45PM ET… | ✅ WIN | +0.46$ |
| 2026-07-22T03:52 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 11:40PM-11:45PM ET… | ✅ WIN | +1.16$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T03:54 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,255.35 | 0.1min |  |
| ✅ ETH | $1,932.01 | 0.1min |  |
| ✅ SOL | $77.97 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,255.35 | consenso |  |
| ETH | $1,932.01 | consenso |  |
| SOL | $78.00 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*