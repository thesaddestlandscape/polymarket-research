# Estado del bot — 2026-07-22 07:18 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.43 $** |
| P&L real total | 🔴 **-26.79 $** |
| P&L real hoy | +0.87 $ |
| P&L real 7 días | -8.72 $ |
| Fees pagados (real) | 9.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3380.40 $ |
| P&L sim compuesto | 🟢 +6402.30 $ (ficción Kelly: +25166% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +38.79 $ |
| Operaciones resueltas | 28467 (17075 WIN / 11392 LOSS) — 60.0% |
| Señales abiertas | 137 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6764 | 59.7% | +0.097 | ➡️ estable | +2131.25$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3963 | 62.9% | +0.128 | 📉 agota (-0.04) | +2062.90$ | 1.29$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3936 | 58.3% | +0.083 | ➡️ estable | +1222.50$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1134 | 66.3% | +0.163 | 📉 agota (-0.05) | +511.81$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2156 | 52.8% | +0.028 | 📈 madura (+0.11) | +181.90$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4927 | 68.7% | +0.187 | ➡️ estable | +90.12$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 262 | 58.0% | +0.080 | 📉 agota (-0.08) | +28.71$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 701 | 62.5% | +0.124 | 📉 agota (-0.03) | +26.05$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 248 | 81.9% | +0.316 | ➡️ estable | +12.69$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 275 | 49.5% | -0.005 | 📉 agota (-0.12) | +10.22$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 312 | 45.2% | -0.048 | 📉 agota (-0.17) | -1.59$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T07:14 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 3:00AM-3:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T07:08 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 2:55AM-3:00AM ET… | ✅ WIN | +1.13$ |
| 2026-07-22T07:08 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 2:45AM-3:00AM ET… | ✅ WIN | +1.50$ |
| 2026-07-22T07:08 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 22, 2:45AM-3:00AM ET… | ✅ WIN | +0.46$ |
| 2026-07-22T07:08 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 2:45AM-3:00AM ET… | ✅ WIN | +1.01$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T07:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,866.60 | 0.1min |  |
| ✅ ETH | $1,915.68 | 0.1min |  |
| ✅ SOL | $77.24 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,869.20 | consenso |  |
| ETH | $1,915.68 | consenso |  |
| SOL | $77.20 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*