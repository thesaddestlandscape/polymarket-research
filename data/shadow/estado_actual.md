# Estado del bot — 2026-07-21 12:36 UTC

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
| P&L fiel (stake fijo 1$) | +3306.37 $ |
| P&L sim compuesto | 🟢 +6254.16 $ (ficción Kelly: +24584% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -161.32 $ |
| Operaciones resueltas | 26728 (16098 WIN / 10630 LOSS) — 60.2% |
| Señales abiertas | 134 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6504 | 60.0% | +0.100 | ➡️ estable | +2117.17$ | 1.00$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3700 | 63.7% | +0.137 | 📉 agota (-0.03) | +2044.29$ | 1.37$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3677 | 58.9% | +0.089 | ➡️ estable | +1217.62$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 968 | 66.8% | +0.168 | 📉 agota (-0.03) | +440.76$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 2050 | 52.7% | +0.027 | 📈 madura (+0.11) | +168.30$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4614 | 68.6% | +0.186 | ➡️ estable | +78.15$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 253 | 58.5% | +0.084 | 📉 agota (-0.07) | +30.08$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 247 | 50.6% | +0.006 | 📉 agota (-0.12) | +15.13$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 579 | 62.5% | +0.125 | 📉 agota (-0.04) | +14.38$ | 1.25$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 249 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 219 | 81.7% | +0.314 | ➡️ estable | +11.66$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 197 | 50.8% | +0.008 | 📉 agota (-0.22) | +7.64$ | 0.50$ | ✅ activa |
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
| 2026-07-21T12:35 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 21, 8:15AM-8:30AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T12:35 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 21, 8:15AM-8:30AM ET… | ❌ LOSS | -2.04$ |
| 2026-07-21T12:35 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 21, 8:15AM-8:30AM ET… | ❌ LOSS | -1.71$ |
| 2026-07-21T12:35 | GBM_LATE_15M#ETH#15min | Ethereum Up or Down - July 21, 8:15AM-8:30AM ET… | ❌ LOSS | -0.60$ |
| 2026-07-21T12:35 | BALLENAS_CONFIRMADAS_15M#ETH#15min | Ethereum Up or Down - July 21, 8:15AM-8:30AM ET… | ❌ LOSS | -0.57$ |

## Calidad de datos

⚠️ **DEGRADED** — última verificación 2026-07-21T12:34 UTC | rechazos 1h: 6 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,487.65 | 0.1min |  |
| ✅ ETH | $1,941.69 | 0.1min |  |
| ✅ SOL | $78.38 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,492.80 | consenso |  |
| ETH | $1,941.69 | consenso |  |
| SOL | $78.31 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:6 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*