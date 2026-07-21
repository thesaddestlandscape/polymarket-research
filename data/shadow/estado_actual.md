# Estado del bot — 2026-07-21 07:34 UTC

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
| P&L fiel (stake fijo 1$) | +3370.06 $ |
| P&L sim compuesto | 🟢 +6286.35 $ (ficción Kelly: +24710% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -129.13 $ |
| Operaciones resueltas | 26264 (15875 WIN / 10389 LOSS) — 60.4% |
| Señales abiertas | 96 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6427 | 60.1% | +0.101 | ➡️ estable | +2120.60$ | 1.01$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3623 | 64.1% | +0.141 | ➡️ estable | +2056.46$ | 1.41$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3600 | 59.2% | +0.092 | ➡️ estable | +1217.30$ | 0.92$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 947 | 67.2% | +0.171 | ➡️ estable | +440.75$ | 1.71$ | ✅ activa |
| UPDOWN_GBM | 2041 | 52.7% | +0.027 | 📈 madura (+0.11) | +167.22$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 205 | 63.9% | +0.138 | ➡️ estable | +106.36$ | 1.38$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4534 | 68.6% | +0.186 | ➡️ estable | +61.58$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 250 | 59.2% | +0.091 | 📉 agota (-0.05) | +35.59$ | 0.91$ | ✅ activa |
| GBM_LATE_5M | 235 | 53.2% | +0.032 | 📉 agota (-0.08) | +21.25$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 551 | 63.0% | +0.129 | 📉 agota (-0.03) | +19.13$ | 1.29$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 98 | 79.6% | +0.290 | 📉 agota (-0.04) | +17.58$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 140 | 56.4% | +0.063 | 📉 agota (-0.24) | +17.49$ | 0.60$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 211 | 82.5% | +0.322 | ➡️ estable | +14.43$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 246 | 52.0% | +0.020 | 📉 agota (-0.14) | +12.78$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 6 | 100.0% | +0.112 | — | +1.04$ | 1.12$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 7 | 57.1% | +0.019 | — | +0.36$ | 0.50$ | ⏳ acumulando |
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
| 2026-07-21T07:32 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 21, 3:25AM-3:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T07:32 | UPDOWN_GBM_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 3:15AM-3:30AM ET… | ✅ WIN | +1.93$ |
| 2026-07-21T07:32 | UPDOWN_GBM#BTC#15min | Bitcoin Up or Down - July 21, 3:15AM-3:30AM ET… | ✅ WIN | +2.46$ |
| 2026-07-21T07:32 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 21, 3:15AM-3:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T07:32 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 21, 3:15AM-3:30AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T07:32 UTC | rechazos 1h: 3 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,867.35 | 0.1min |  |
| ✅ ETH | $1,933.01 | 0.1min |  |
| ✅ SOL | $78.57 | 0.1min |  |
| ✅ XRP | $1.13 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,879.70 | consenso |  |
| ETH | $1,933.01 | consenso |  |
| SOL | $78.43 | consenso |  |
| XRP | $1.13 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:3 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*