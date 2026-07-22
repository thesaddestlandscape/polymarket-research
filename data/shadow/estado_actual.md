# Estado del bot — 2026-07-22 05:21 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.45 $** |
| P&L real total | 🔴 **-26.77 $** |
| P&L real hoy | +0.67 $ |
| P&L real 7 días | -8.92 $ |
| Fees pagados (real) | 9.10 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3389.80 $ |
| P&L sim compuesto | 🟢 +6421.52 $ (ficción Kelly: +25242% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +58.01 $ |
| Operaciones resueltas | 28291 (16983 WIN / 11308 LOSS) — 60.0% |
| Señales abiertas | 141 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6741 | 59.8% | +0.098 | ➡️ estable | +2147.74$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3935 | 63.1% | +0.131 | 📉 agota (-0.04) | +2088.56$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3908 | 58.5% | +0.085 | ➡️ estable | +1246.57$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1117 | 66.1% | +0.160 | 📉 agota (-0.04) | +490.14$ | 1.60$ | ✅ activa |
| UPDOWN_GBM | 2140 | 52.6% | +0.026 | 📈 madura (+0.10) | +172.63$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4895 | 68.5% | +0.185 | ➡️ estable | +69.68$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 261 | 58.2% | +0.082 | 📉 agota (-0.08) | +30.75$ | 0.82$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 696 | 62.4% | +0.123 | 📉 agota (-0.04) | +24.98$ | 1.23$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 273 | 49.8% | -0.002 | 📉 agota (-0.12) | +14.30$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 247 | 81.8% | +0.315 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| LATE_WINDOW_5MIN | 290 | 45.9% | -0.041 | 📉 agota (-0.18) | -1.41$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-22T05:20 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 1:05AM-1:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T05:20 | STREAK_FADE_15M#XRP#15min | XRP Up or Down - July 22, 1:00AM-1:15AM ET… | ✅ WIN | +1.54$ |
| 2026-07-22T05:20 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 22, 1:00AM-1:15AM ET… | ✅ WIN | +0.82$ |
| 2026-07-22T05:20 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 1:00AM-1:15AM ET… | ✅ WIN | +0.30$ |
| 2026-07-22T05:20 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 1:00AM-1:15AM ET… | ❌ LOSS | -1.80$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T05:19 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,153.63 | 0.1min |  |
| ✅ ETH | $1,927.44 | 0.1min |  |
| ✅ SOL | $77.87 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,154.20 | consenso |  |
| ETH | $1,927.81 | consenso |  |
| SOL | $77.76 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*