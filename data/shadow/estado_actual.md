# Estado del bot — 2026-07-21 04:30 UTC

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
| P&L fiel (stake fijo 1$) | +3413.66 $ |
| P&L sim compuesto | 🟢 +6321.61 $ (ficción Kelly: +24849% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -93.87 $ |
| Operaciones resueltas | 25944 (15719 WIN / 10225 LOSS) — 60.6% |
| Señales abiertas | 122 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6375 | 60.3% | +0.103 | ➡️ estable | +2140.12$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3571 | 64.5% | +0.145 | ➡️ estable | +2085.81$ | 1.45$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3553 | 59.5% | +0.095 | ➡️ estable | +1231.67$ | 0.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 914 | 67.4% | +0.174 | ➡️ estable | +426.31$ | 1.74$ | ✅ activa |
| UPDOWN_GBM | 2026 | 52.5% | +0.025 | 📈 madura (+0.12) | +155.02$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 203 | 64.0% | +0.139 | ➡️ estable | +104.87$ | 1.39$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4489 | 68.6% | +0.186 | ➡️ estable | +63.05$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 246 | 59.3% | +0.093 | 📉 agota (-0.05) | +35.71$ | 0.93$ | ✅ activa |
| GBM_LATE_5M | 228 | 54.8% | +0.048 | 📉 agota (-0.04) | +24.82$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 106 | 60.4% | +0.102 | 📉 agota (-0.18) | +19.84$ | 1.02$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 540 | 62.8% | +0.127 | 📉 agota (-0.03) | +17.15$ | 1.27$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 95 | 78.9% | +0.284 | 📉 agota (-0.08) | +15.82$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 241 | 52.3% | +0.023 | 📉 agota (-0.12) | +13.22$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1641 | 51.1% | +0.011 | ➡️ estable | +11.65$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 205 | 82.0% | +0.316 | ➡️ estable | +9.51$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 6 | 66.7% | +0.037 | — | +0.87$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T04:26 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 12:15AM-12:20AM ET… | ❌ LOSS | -0.57$ |
| 2026-07-21T04:26 | ORDER_FLOW_5M#BNB#5min | BNB Up or Down - July 21, 12:15AM-12:20AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T04:23 | GBM_LATE_15M_PYCONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 12:00AM-12:15AM ET… | ✅ WIN | +3.49$ |
| 2026-07-21T04:23 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 12:00AM-12:15AM ET… | ✅ WIN | +0.08$ |
| 2026-07-21T04:23 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 12:00AM-12:15AM ET… | ❌ LOSS | -1.16$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T04:28 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,520.04 | 0.1min |  |
| ✅ ETH | $1,922.52 | 0.1min |  |
| ✅ SOL | $78.06 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,529.60 | consenso |  |
| ETH | $1,922.52 | consenso |  |
| SOL | $78.04 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*