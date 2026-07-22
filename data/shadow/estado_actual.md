# Estado del bot — 2026-07-22 05:08 UTC

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
| P&L fiel (stake fijo 1$) | +3396.06 $ |
| P&L sim compuesto | 🟢 +6434.29 $ (ficción Kelly: +25292% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +70.78 $ |
| Operaciones resueltas | 28268 (16973 WIN / 11295 LOSS) — 60.0% |
| Señales abiertas | 138 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6737 | 59.8% | +0.098 | ➡️ estable | +2151.95$ | 0.98$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3931 | 63.1% | +0.131 | 📉 agota (-0.04) | +2093.23$ | 1.31$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3905 | 58.5% | +0.085 | ➡️ estable | +1251.95$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1115 | 66.1% | +0.161 | 📉 agota (-0.04) | +490.49$ | 1.61$ | ✅ activa |
| UPDOWN_GBM | 2139 | 52.6% | +0.026 | 📈 madura (+0.11) | +173.97$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 224 | 61.2% | +0.111 | 📉 agota (-0.06) | +107.55$ | 1.11$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4892 | 68.5% | +0.185 | ➡️ estable | +68.86$ | 1.85$ | ✅ activa |
| WEEKLY_PRICE | 321 | 67.3% | +0.172 | 📈 madura (+0.23) | +63.81$ | 1.72$ | ✅ activa |
| STREAK_FADE_15M | 260 | 58.1% | +0.080 | 📉 agota (-0.08) | +29.21$ | 0.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 694 | 62.2% | +0.122 | 📉 agota (-0.04) | +23.61$ | 1.22$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 117 | 78.6% | +0.282 | ➡️ estable | +19.54$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 273 | 49.8% | -0.002 | 📉 agota (-0.12) | +14.30$ | 0.50$ | ⚠️ IC negativo |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 247 | 81.8% | +0.315 | ➡️ estable | +12.39$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 257 | 51.0% | +0.010 | 📉 agota (-0.15) | +9.66$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 330 | 38.8% | -0.111 | ➡️ estable | +6.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 287 | 46.0% | -0.040 | 📉 agota (-0.18) | -0.87$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 13 | 76.9% | +0.152 | — | -1.30$ | 1.52$ | ✅ activa |
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
| 2026-07-22T05:07 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 22, 12:45AM-1:00AM ET… | ❌ LOSS | -0.91$ |
| 2026-07-22T05:07 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 22, 12:50AM-12:55AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-22T05:07 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 12:45AM-1:00AM ET… | ❌ LOSS | -1.61$ |
| 2026-07-22T05:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 22, 12:45AM-1:00AM ET… | ✅ WIN | +2.08$ |
| 2026-07-22T05:07 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 22, 12:45AM-1:00AM ET… | ❌ LOSS | -1.88$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T05:06 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,241.79 | 0.1min |  |
| ✅ ETH | $1,932.06 | 0.1min |  |
| ✅ SOL | $77.91 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,267.00 | consenso |  |
| ETH | $1,932.06 | consenso |  |
| SOL | $77.89 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*