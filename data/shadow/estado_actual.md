# Estado del bot — 2026-07-21 10:23 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **0.78 $** |
| P&L real total | 🔴 **-24.66 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -9.25 $ |
| Fees pagados (real) | 8.68 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3326.83 $ |
| P&L sim compuesto | 🟢 +6260.34 $ (ficción Kelly: +24608% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -155.14 $ |
| Operaciones resueltas | 26534 (16002 WIN / 10532 LOSS) — 60.3% |
| Señales abiertas | 111 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6471 | 60.0% | +0.100 | ➡️ estable | +2118.79$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3667 | 63.9% | +0.139 | ➡️ estable | +2050.44$ | 1.39$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3644 | 59.1% | +0.091 | ➡️ estable | +1218.26$ | 0.91$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 959 | 66.9% | +0.169 | 📉 agota (-0.03) | +439.02$ | 1.69$ | ✅ activa |
| UPDOWN_GBM | 2045 | 52.7% | +0.027 | 📈 madura (+0.11) | +167.92$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 211 | 62.6% | +0.124 | ➡️ estable | +101.12$ | 1.24$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4583 | 68.6% | +0.186 | ➡️ estable | +73.12$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 243 | 51.4% | +0.014 | 📉 agota (-0.11) | +17.17$ | 0.50$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 100 | 79.0% | +0.284 | ➡️ estable | +16.34$ | 2.00$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 567 | 62.6% | +0.126 | 📉 agota (-0.04) | +14.40$ | 1.26$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 248 | 51.6% | +0.016 | 📉 agota (-0.16) | +11.76$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 173 | 52.0% | +0.020 | 📉 agota (-0.23) | +9.72$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 216 | 81.5% | +0.312 | ➡️ estable | +9.48$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 8 | 50.0% | +0.000 | — | -0.26$ | 0.50$ | ✅ activa |
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
| 2026-07-21T10:22 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 6:10AM-6:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T10:22 | GBM_LATE_5M#BTC#5min | Bitcoin Up or Down - July 21, 6:10AM-6:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T10:19 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 6:10AM-6:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T10:19 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 6:05AM-6:10AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T10:19 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 6:00AM-6:15AM ET… | ✅ WIN | +0.61$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T10:21 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,297.71 | 0.1min |  |
| ✅ ETH | $1,943.45 | 0.1min |  |
| ✅ SOL | $78.33 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,315.60 | consenso |  |
| ETH | $1,943.45 | consenso |  |
| SOL | $78.36 | consenso |  |
| XRP | $1.13 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*