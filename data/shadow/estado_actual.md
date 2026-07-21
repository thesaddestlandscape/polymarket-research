# Estado del bot — 2026-07-21 04:19 UTC

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
| P&L fiel (stake fijo 1$) | +3406.05 $ |
| P&L sim compuesto | 🟢 +6316.72 $ (ficción Kelly: +24830% s/ operativo) |
| P&L sim hoy (2026-07-21) | 🔴 -98.76 $ |
| Operaciones resueltas | 25919 (15706 WIN / 10213 LOSS) — 60.6% |
| Señales abiertas | 124 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6371 | 60.3% | +0.103 | ➡️ estable | +2137.94$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 3567 | 64.5% | +0.145 | ➡️ estable | +2082.86$ | 1.45$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 3550 | 59.5% | +0.095 | ➡️ estable | +1232.96$ | 0.95$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 912 | 67.3% | +0.173 | ➡️ estable | +423.35$ | 1.73$ | ✅ activa |
| UPDOWN_GBM | 2024 | 52.5% | +0.025 | 📈 madura (+0.12) | +152.50$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 202 | 63.9% | +0.137 | ➡️ estable | +101.38$ | 1.37$ | ✅ activa |
| FAVORITO_CONFIRMADO | 4486 | 68.6% | +0.186 | ➡️ estable | +67.05$ | 1.86$ | ✅ activa |
| WEEKLY_PRICE | 305 | 66.2% | +0.161 | 📈 madura (+0.23) | +51.01$ | 1.61$ | ✅ activa |
| STREAK_FADE_15M | 245 | 59.6% | +0.095 | 📉 agota (-0.04) | +37.39$ | 0.95$ | ✅ activa |
| GBM_LATE_5M | 228 | 54.8% | +0.048 | 📉 agota (-0.04) | +24.82$ | 0.50$ | ✅ activa |
| LATE_WINDOW_5MIN | 104 | 60.6% | +0.104 | 📉 agota (-0.20) | +20.05$ | 1.04$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 539 | 62.7% | +0.127 | 📉 agota (-0.03) | +16.63$ | 1.27$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 95 | 78.9% | +0.284 | 📉 agota (-0.08) | +15.82$ | 2.00$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 241 | 52.3% | +0.023 | 📉 agota (-0.12) | +13.22$ | 0.50$ | ✅ activa |
| ORDER_FLOW_5M | 1640 | 51.2% | +0.012 | ➡️ estable | +12.16$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 204 | 82.4% | +0.320 | ➡️ estable | +11.55$ | 2.00$ | ✅ activa |
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
| 2026-07-21T04:18 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 21, 12:05AM-12:10AM ET… | ✅ WIN | +1.45$ |
| 2026-07-21T04:15 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 12:05AM-12:10AM ET… | ✅ WIN | +0.59$ |
| 2026-07-21T04:10 | LATE_WINDOW_5MIN#BTC#5min | Bitcoin Up or Down - July 21, 12:00AM-12:05AM ET… | ❌ LOSS | -0.66$ |
| 2026-07-21T04:07 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 21, 12:00AM-12:05AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-21T04:07 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 21, 12:00AM-12:05AM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-21T04:17 UTC | rechazos 1h: 4 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,547.96 | 0.1min |  |
| ✅ ETH | $1,925.05 | 0.1min |  |
| ✅ SOL | $78.04 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,547.96 | consenso |  |
| ETH | $1,925.05 | consenso |  |
| SOL | $78.08 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:4 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*