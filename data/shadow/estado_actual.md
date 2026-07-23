# Estado del bot — 2026-07-23 11:18 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **30.16 $** |
| P&L real total | 🔴 **-21.06 $** |
| P&L real hoy | +0.93 $ |
| P&L real 7 días | +0.02 $ |
| Fees pagados (real) | 9.81 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3628.46 $ |
| P&L sim compuesto | 🟢 +6896.34 $ (ficción Kelly: +27108% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +184.48 $ |
| Operaciones resueltas | 30761 (18500 WIN / 12261 LOSS) — 60.1% |
| Señales abiertas | 144 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7111 | 59.6% | +0.096 | 📉 agota (-0.03) | +2227.84$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4309 | 62.7% | +0.127 | 📉 agota (-0.04) | +2191.06$ | 1.27$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4319 | 58.0% | +0.080 | ➡️ estable | +1301.42$ | 0.80$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1350 | 66.6% | +0.166 | ➡️ estable | +628.40$ | 1.66$ | ✅ activa |
| UPDOWN_GBM | 2316 | 53.2% | +0.031 | 📈 madura (+0.11) | +205.83$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 242 | 60.7% | +0.107 | 📉 agota (-0.06) | +110.40$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5376 | 68.8% | +0.188 | ➡️ estable | +97.92$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 854 | 63.0% | +0.130 | ➡️ estable | +48.58$ | 1.30$ | ✅ activa |
| STREAK_FADE_15M | 270 | 58.5% | +0.085 | 📉 agota (-0.06) | +34.12$ | 0.85$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 131 | 79.4% | +0.289 | ➡️ estable | +24.29$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 288 | 82.3% | +0.321 | ➡️ estable | +18.59$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 264 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.21$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 357 | 48.2% | -0.018 | 📉 agota (-0.21) | +8.31$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 25 | 88.0% | +0.352 | — | +2.05$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| LATE_WINDOW_5MIN | 336 | 44.9% | -0.050 | 📉 agota (-0.16) | -4.47$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 319 | 44.2% | -0.058 | 📉 agota (-0.08) | -25.29$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T11:16 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 7:05AM-7:10AM ET… | ✅ WIN | +0.50$ |
| 2026-07-23T11:10 | GBM_LATE_5M#XRP#5min | XRP Up or Down - July 23, 6:55AM-7:00AM ET… | ✅ WIN | +0.75$ |
| 2026-07-23T11:10 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 23, 6:55AM-7:00AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-23T11:07 | BALLENAS_CONFIRMADAS_15M#XRP#15min | XRP Up or Down - July 23, 6:45AM-7:00AM ET… | ✅ WIN | +0.80$ |
| 2026-07-23T11:07 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 23, 6:45AM-7:00AM ET… | ❌ LOSS | -2.04$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T11:16 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,673.99 | 0.1min |  |
| ✅ ETH | $1,927.73 | 0.1min |  |
| ✅ SOL | $77.84 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,678.00 | consenso |  |
| ETH | $1,927.73 | consenso |  |
| SOL | $77.81 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*