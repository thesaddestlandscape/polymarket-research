# Estado del bot — 2026-07-22 04:44 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **24.36 $** |
| P&L real total | 🔴 **-26.86 $** |
| P&L real hoy | +0.67 $ |
| P&L real 7 días | -8.92 $ |
| Fees pagados (real) | 9.08 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3381.41 $ |
| P&L sim compuesto | 🟢 +6410.00 $ (ficción Kelly: +25197% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +46.49 $ |
| Operaciones resueltas | 28215 (16943 WIN / 11272 LOSS) — 60.0% |
| Señales abiertas | 148 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6731 | 59.8% | +0.098 | ➡️ estable | +2145.20$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3925 | 63.1% | +0.131 | 📉 agota (-0.04) | +2083.98$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3899 | 58.5% | +0.085 | ➡️ estable | +1243.06$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1109 | 66.3% | +0.162 | 📉 agota (-0.04) | +491.95$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2134 | 52.7% | +0.027 | 📈 madura (+0.11) | +174.25$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4883 | 68.5% | +0.185 | ➡️ estable | +70.58$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 691 | 62.4% | +0.123 | 📉 agota (-0.04) | +21.15$ | 1.23$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 270 | 49.6% | -0.004 | 📉 agota (-0.12) | +14.54$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 247 | 81.8% | +0.315 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1650 | 51.2% | +0.012 | ➡️ estable | +12.38$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 283 | 45.6% | -0.044 | 📉 agota (-0.21) | -2.98$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T04:40 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 12:25AM-12:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T04:40 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 22, 12:25AM-12:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T04:37 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 22, 12:15AM-12:30AM ET… | ✅ WIN | +0.41$ |
| 2026-07-22T04:37 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 12:15AM-12:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T04:37 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 22, 12:15AM-12:30AM ET… | ❌ LOSS | -1.87$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T04:42 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,346.70 | 0.1min |  |
| ✅ ETH | $1,935.20 | 0.1min |  |
| ✅ SOL | $78.15 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,350.30 | consenso |  |
| ETH | $1,935.20 | consenso |  |
| SOL | $78.08 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*