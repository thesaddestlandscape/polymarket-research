# Estado del bot — 2026-07-22 19:01 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **27.18 $** |
| P&L real total | 🔴 **-24.04 $** |
| P&L real hoy | +4.67 $ |
| P&L real 7 días | -4.92 $ |
| Fees pagados (real) | 9.51 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3522.65 $ |
| P&L sim compuesto | 🟢 +6658.73 $ (ficción Kelly: +26174% s/ operativo) |
| P&L sim hoy (2026-07-22) | 🟢 +295.22 $ |
| Operaciones resueltas | 29391 (17675 WIN / 11716 LOSS) — 60.1% |
| Señales abiertas | 146 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 6904 | 59.7% | +0.097 | ➡️ estable | +2179.17$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4103 | 63.0% | +0.130 | 📉 agota (-0.04) | +2155.47$ | 1.30$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4096 | 58.3% | +0.083 | ➡️ estable | +1266.83$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1225 | 66.4% | +0.163 | 📉 agota (-0.04) | +558.30$ | 1.63$ | ✅ activa |
| UPDOWN_GBM | 2210 | 53.1% | +0.031 | 📈 madura (+0.11) | +192.36$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 230 | 61.7% | +0.116 | 📉 agota (-0.05) | +110.98$ | 1.16$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5112 | 68.7% | +0.187 | ➡️ estable | +86.31$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 773 | 62.9% | +0.128 | 📉 agota (-0.03) | +37.23$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 263 | 58.2% | +0.081 | 📉 agota (-0.07) | +30.04$ | 0.81$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 119 | 79.0% | +0.285 | ➡️ estable | +20.13$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 265 | 82.3% | +0.320 | ➡️ estable | +17.16$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1653 | 51.1% | +0.011 | ➡️ estable | +11.85$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 262 | 50.8% | +0.008 | 📉 agota (-0.17) | +9.12$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 287 | 48.4% | -0.016 | 📉 agota (-0.13) | +7.03$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| BALLENAS_TARDIAS | 16 | 81.2% | +0.222 | — | -0.59$ | 2.00$ | ✅ activa |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 323 | 45.5% | -0.045 | 📉 agota (-0.17) | -1.65$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 317 | 44.2% | -0.058 | 📉 agota (-0.09) | -25.33$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-22T19:00 | GBM_LATE_5M#SOL#5min | Solana Up or Down - July 22, 2:50PM-2:55PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-22T19:00 | GBM_LATE_5M#ETH#5min | Ethereum Up or Down - July 22, 2:50PM-2:55PM ET… | ✅ WIN | +0.66$ |
| 2026-07-22T18:48 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 22, 2:30PM-2:45PM ET… | ✅ WIN | +0.36$ |
| 2026-07-22T18:48 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 22, 2:30PM-2:45PM ET… | ❌ LOSS | -1.42$ |
| 2026-07-22T18:48 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 22, 2:30PM-2:45PM ET… | ✅ WIN | +0.44$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-22T19:00 UTC | rechazos 1h: 1 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,856.95 | 0.1min |  |
| ✅ ETH | $1,929.61 | 0.1min |  |
| ✅ SOL | $77.78 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,859.80 | consenso |  |
| ETH | $1,929.96 | consenso |  |
| SOL | $77.72 | consenso |  |
| XRP | $1.14 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:1 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*