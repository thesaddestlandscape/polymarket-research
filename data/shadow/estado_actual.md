# Estado del bot — 2026-07-21 13:05 UTC

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
| P&L fiel (stake fijo 1$) | +3298.67 $ |
| P&L sim compuesto | 🟢 +6248.77 $ (ficción Kelly: +24563% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -166.71 $ |
| Operaciones resueltas | 26781 (16123 WIN / 10658 LOSS) — 60.2% |
| Señales abiertas | 131 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6511 | 59.9% | +0.099 | ➡️ estable | +2114.79$ | 0.99$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3707 | 63.6% | +0.136 | 📉 agota (-0.04) | +2038.42$ | 1.36$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3684 | 58.9% | +0.089 | ➡️ estable | +1214.88$ | 0.89$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 974 | 66.8% | +0.168 | 📉 agota (-0.03) | +443.55$ | 1.68$ | ✅ activa |
| UPDOWN_GBM | 2053 | 52.7% | +0.027 | 📈 madura (+0.11) | +170.19$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 212 | 62.3% | +0.121 | 📉 agota (-0.04) | +100.61$ | 1.21$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4623 | 68.6% | +0.186 | ➡️ estable | +82.45$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 255 | 58.4% | +0.084 | 📉 agota (-0.07) | +29.94$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 102 | 79.4% | +0.288 | ➡️ estable | +18.84$ | 2.00$ | ✅ activa |
| GBM_LATE_5M | 247 | 50.6% | +0.006 | 📉 agota (-0.12) | +15.13$ | 0.50$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 583 | 62.4% | +0.124 | 📉 agota (-0.04) | +14.23$ | 1.24$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 249 | 51.8% | +0.018 | 📉 agota (-0.15) | +12.30$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1644 | 51.1% | +0.011 | ➡️ estable | +11.30$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 220 | 81.4% | +0.311 | ➡️ estable | +9.62$ | 2.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 203 | 50.2% | +0.002 | 📉 agota (-0.22) | +6.44$ | 0.50$ | ✅ activa |
| GBM_LATE_60M | 329 | 38.6% | -0.113 | ➡️ estable | +5.97$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 7 | 100.0% | +0.136 | — | +1.20$ | 1.36$ | ⏳ acumulando |
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
| 2026-07-21T13:04 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 8:50AM-8:55AM ET… | ✅ WIN | +0.34$ |
| 2026-07-21T13:04 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 21, 8:50AM-8:55AM ET… | ✅ WIN | +1.27$ |
| 2026-07-21T13:04 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 21, 8:50AM-8:55AM ET… | ✅ WIN | +0.93$ |
| 2026-07-21T13:04 | FAVORITO_CONFIRMADO#SOL#60min | Solana Up or Down - July 21, 8AM ET… | ✅ WIN | +1.41$ |
| 2026-07-21T13:04 | FAVORITO_CONFIRMADO#ETH#60min | Ethereum Up or Down - July 21, 8AM ET… | ❌ LOSS | -1.29$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T13:04 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $66,470.96 | 0.1min |  |
| ✅ ETH | $1,939.86 | 0.1min |  |
| ✅ SOL | $78.51 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $66,487.70 | consenso |  |
| ETH | $1,939.86 | consenso |  |
| SOL | $78.42 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*