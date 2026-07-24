# Estado del bot — 2026-07-24 10:26 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.92 $** |
| P&L real total | 🔴 **-23.30 $** |
| P&L real hoy | +1.01 $ |
| P&L real 7 días | -0.02 $ |
| Fees pagados (real) | 9.94 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3798.32 $ |
| P&L sim compuesto | 🟢 +7184.89 $ (ficción Kelly: +28242% s/ operativo) |
| P&L sim hoy (2026-07-24) | 🟢 +210.52 $ |
| Operaciones resueltas | 32689 (19656 WIN / 13033 LOSS) — 60.1% |
| Señales abiertas | 118 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7392 | 59.6% | +0.096 | 📉 agota (-0.03) | +2296.83$ | 0.96$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4584 | 62.5% | +0.125 | 📉 agota (-0.05) | +2282.88$ | 1.25$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4618 | 57.5% | +0.075 | 📉 agota (-0.04) | +1308.68$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1517 | 66.4% | +0.164 | ➡️ estable | +705.78$ | 1.64$ | ✅ activa |
| UPDOWN_GBM | 2434 | 53.4% | +0.034 | 📈 madura (+0.09) | +226.02$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5767 | 68.8% | +0.188 | ➡️ estable | +127.58$ | 1.88$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 249 | 60.6% | +0.106 | 📉 agota (-0.08) | +111.96$ | 1.06$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 960 | 62.8% | +0.128 | ➡️ estable | +45.78$ | 1.28$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 142 | 81.0% | +0.306 | 📈 madura (+0.04) | +30.61$ | 2.00$ | ✅ activa |
| STREAK_FADE_15M | 280 | 57.9% | +0.078 | 📉 agota (-0.06) | +29.14$ | 0.78$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 318 | 81.8% | +0.316 | ➡️ estable | +15.85$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1661 | 51.2% | +0.012 | ➡️ estable | +12.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 270 | 51.1% | +0.011 | 📉 agota (-0.16) | +10.17$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 337 | 38.9% | -0.111 | ➡️ estable | +4.86$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 29 | 89.7% | +0.371 | — | +3.37$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 13 | 84.6% | +0.195 | — | +3.10$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 14 | 57.1% | +0.044 | — | +0.65$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| LATE_WINDOW_5MIN | 350 | 45.1% | -0.048 | 📉 agota (-0.12) | -2.09$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_5M | 543 | 47.5% | -0.025 | 📉 agota (-0.05) | -2.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 320 | 44.1% | -0.059 | 📉 agota (-0.08) | -26.41$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-24T10:21 | GBM_LATE_15M_ESPACIO_ATR#BTC#15min | Bitcoin Up or Down - July 24, 6:00AM-6:15AM ET… | ✅ WIN | +1.07$ |
| 2026-07-24T10:21 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 24, 6:00AM-6:15AM ET… | ✅ WIN | +0.38$ |
| 2026-07-24T10:21 | GBM_LATE_15M#BTC#15min | Bitcoin Up or Down - July 24, 6:00AM-6:15AM ET… | ✅ WIN | +0.39$ |
| 2026-07-24T10:21 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 24, 6:00AM-6:15AM ET… | ✅ WIN | +0.44$ |
| 2026-07-24T10:21 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 24, 6:00AM-6:15AM ET… | ✅ WIN | +0.92$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-24T10:24 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,944.88 | 0.1min |  |
| ✅ ETH | $1,883.40 | 0.1min |  |
| ✅ SOL | $75.56 | 0.1min |  |
| ✅ XRP | $1.11 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,946.50 | consenso |  |
| ETH | $1,883.40 | consenso |  |
| SOL | $75.44 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*