# Estado del bot — 2026-07-22 02:34 UTC

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
| P&L fiel (stake fijo 1$) | +3369.80 $ |
| P&L sim compuesto | 🟢 +6403.03 $ (ficción Kelly: +25169% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +39.53 $ |
| Operaciones resueltas | 28007 (16827 WIN / 11180 LOSS) — 60.1% |
| Señales abiertas | 132 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6705 | 59.8% | +0.098 | ➡️ estable | +2138.25$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3898 | 63.2% | +0.132 | 📉 agota (-0.04) | +2075.83$ | 1.32$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3872 | 58.6% | +0.086 | ➡️ estable | +1247.61$ | 0.86$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1091 | 66.5% | +0.164 | ➡️ estable | +491.42$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2120 | 52.6% | +0.026 | 📈 madura (+0.11) | +172.80$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 222 | 61.3% | +0.112 | 📉 agota (-0.05) | +105.71$ | 1.12$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4841 | 68.5% | +0.185 | ➡️ estable | +72.44$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 679 | 62.4% | +0.124 | 📉 agota (-0.05) | +22.80$ | 1.24$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 113 | 79.6% | +0.291 | ➡️ estable | +21.99$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 265 | 49.1% | -0.009 | 📉 agota (-0.14) | +15.04$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 242 | 82.2% | +0.320 | ➡️ estable | +14.51$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1647 | 51.1% | +0.011 | ➡️ estable | +11.75$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 260 | 45.8% | -0.042 | 📉 agota (-0.23) | -3.54$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T02:33 | UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | Bitcoin Up or Down - July 21, 10:15PM-10:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T02:33 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 10:15PM-10:30PM ET… | ✅ WIN | +0.76$ |
| 2026-07-22T02:33 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 21, 10:15PM-10:30PM ET… | ✅ WIN | +1.84$ |
| 2026-07-22T02:33 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 10:15PM-10:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T02:33 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 10:15PM-10:30PM ET… | ❌ LOSS | -1.53$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T02:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,293.55 | 0.1min |  |
| ✅ ETH | $1,928.15 | 0.1min |  |
| ✅ SOL | $78.35 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,319.90 | consenso |  |
| ETH | $1,928.77 | consenso |  |
| SOL | $78.25 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*