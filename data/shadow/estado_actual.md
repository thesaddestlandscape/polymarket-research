# Estado del bot — 2026-07-22 04:14 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **22.73 $** |
| P&L real total | 🔴 **-28.49 $** |
| P&L real hoy | +1.28 $ |
| P&L real 7 días | -8.31 $ |
| Fees pagados (real) | 9.06 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3371.67 $ |
| P&L sim compuesto | 🟢 +6385.39 $ (ficción Kelly: +25100% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +21.88 $ |
| Operaciones resueltas | 28159 (16903 WIN / 11256 LOSS) — 60.0% |
| Señales abiertas | 145 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6723 | 59.8% | +0.097 | ➡️ estable | +2137.78$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3917 | 63.1% | +0.131 | 📉 agota (-0.04) | +2076.60$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3891 | 58.5% | +0.085 | ➡️ estable | +1238.74$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1102 | 66.2% | +0.162 | 📉 agota (-0.03) | +490.16$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2130 | 52.7% | +0.027 | 📈 madura (+0.11) | +173.55$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 223 | 61.4% | +0.113 | 📉 agota (-0.05) | +108.06$ | 1.13$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4876 | 68.5% | +0.185 | ➡️ estable | +68.38$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 687 | 62.6% | +0.126 | 📉 agota (-0.04) | +22.84$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 115 | 78.3% | +0.278 | ➡️ estable | +18.22$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 270 | 49.6% | -0.004 | 📉 agota (-0.12) | +14.54$ | 0.50$ | ⚠️ IC negativo |
| ORDER_FLOW_5M | 1650 | 51.2% | +0.012 | ➡️ estable | +12.38$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 245 | 81.6% | +0.314 | ➡️ estable | +11.09$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 256 | 51.2% | +0.012 | 📉 agota (-0.15) | +10.84$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 278 | 45.3% | -0.046 | 📉 agota (-0.23) | -3.37$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 315 | 44.1% | -0.058 | 📉 agota (-0.08) | -25.36$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T04:13 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 22, 12:00AM-12:05AM ET… | ✅ WIN | +0.48$ |
| 2026-07-22T04:07 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 11:55PM-12:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T04:07 | ORDER_FLOW_5M#DOGE#5min | Dogecoin Up or Down - July 21, 11:55PM-12:00AM ET… | ✅ WIN | +0.49$ |
| 2026-07-22T04:07 | BALLENAS_CONFIRMADAS_15M#SOL#15min | Solana Up or Down - July 21, 11:45PM-12:00AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T04:07 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 21, 11:45PM-12:00AM ET… | ✅ WIN | +2.05$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T04:12 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,304.85 | 0.1min |  |
| ✅ ETH | $1,932.55 | 0.1min |  |
| ✅ SOL | $78.09 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,304.85 | consenso |  |
| ETH | $1,932.55 | consenso |  |
| SOL | $78.06 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*