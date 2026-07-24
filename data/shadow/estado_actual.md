# Estado del bot — 2026-07-24 07:30 UTC

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
| P&L fiel (stake fijo 1$) | +3744.16 $ |
| P&L sim compuesto | 🟢 +7098.18 $ (ficción Kelly: +27902% s/ operativo) |
| P&L sim hoy (2026-07-24) | 🟢 +123.81 $ |
| Operaciones resueltas | 32479 (19503 WIN / 12976 LOSS) — 60.0% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7351 | 59.5% | +0.095 | 📉 agota (-0.03) | +2276.58$ | 0.95$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4545 | 62.4% | +0.123 | 📉 agota (-0.05) | +2252.86$ | 1.23$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4581 | 57.5% | +0.075 | 📉 agota (-0.04) | +1303.44$ | 0.75$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1502 | 66.2% | +0.162 | ➡️ estable | +694.50$ | 1.62$ | ✅ activa |
| UPDOWN_GBM | 2427 | 53.4% | +0.034 | 📈 madura (+0.09) | +225.08$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 248 | 60.5% | +0.104 | 📉 agota (-0.08) | +111.73$ | 1.04$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5715 | 68.8% | +0.188 | ➡️ estable | +111.41$ | 1.88$ | ✅ activa |
| WEEKLY_PRICE | 352 | 69.0% | +0.189 | 📈 madura (+0.23) | +69.51$ | 1.89$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 948 | 62.6% | +0.125 | ➡️ estable | +42.67$ | 1.25$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 142 | 81.0% | +0.306 | 📈 madura (+0.04) | +30.61$ | 2.00$ | ✅ activa |
| STREAK_FADE_15M | 280 | 57.9% | +0.078 | 📉 agota (-0.06) | +29.14$ | 0.78$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 316 | 81.6% | +0.314 | ➡️ estable | +15.26$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1661 | 51.2% | +0.012 | ➡️ estable | +12.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 269 | 51.3% | +0.013 | 📉 agota (-0.16) | +10.74$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 337 | 38.9% | -0.111 | ➡️ estable | +4.86$ | 0.50$ | ⚠️ IC negativo |
| BALLENAS_TARDIAS | 29 | 89.7% | +0.371 | — | +3.37$ | 2.00$ | ✅ activa |
| RESOLUTION_SNIPER | 13 | 84.6% | +0.195 | — | +3.10$ | 1.95$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 13 | 53.8% | +0.022 | — | +0.20$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 541 | 47.7% | -0.023 | 📉 agota (-0.04) | -1.17$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 350 | 45.1% | -0.048 | 📉 agota (-0.12) | -2.09$ | 0.50$ | ⚠️ IC negativo |
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
| 2026-07-24T07:19 | FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | Solana Up or Down - July 24, 3:00AM-3:15AM ET… | ✅ WIN | +0.25$ |
| 2026-07-24T07:19 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 24, 3:00AM-3:15AM ET… | ✅ WIN | +0.25$ |
| 2026-07-24T07:19 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 24, 3:00AM-3:15AM ET… | ✅ WIN | +0.19$ |
| 2026-07-24T07:19 | UPDOWN_GBM_15M_TARDIO#SOL#15min | Solana Up or Down - July 24, 3:00AM-3:15AM ET… | ✅ WIN | +1.03$ |
| 2026-07-24T07:19 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 24, 3:00AM-3:15AM ET… | ✅ WIN | +2.17$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-24T07:28 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,616.27 | 0.1min |  |
| ✅ ETH | $1,897.46 | 0.1min |  |
| ✅ SOL | $76.11 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,625.80 | consenso |  |
| ETH | $1,897.46 | consenso |  |
| SOL | $76.12 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*